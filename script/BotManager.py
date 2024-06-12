import re
import json
import multiprocessing
import os
from tqdm import tqdm
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures import ThreadPoolExecutor, as_completed
from PostRobot import PostRobot
import requests


class BotManager:
    def __init__(self):
        self.result_output_dir = ""
        self.api_key = None # should be a list of "sk-api-key"
        self.processes_num = 1
        self.proxy = None
        self.start = None
        self.end = None
        self.sample_list = []
        self.model_name = ""
        self.base_url = ""
        self.org = None # should be a list of "org-name"
        self.fail = 0
        self.success = 0
        self.time_out = 20
        self.temperature = 0
    
    def set_org(self, org_file="org.txt"):
        with open(org_file, encoding="utf-8", mode="r") as fr:
            lines = fr.readlines()
            org = [line.strip() for line in lines]
            if len(org) > 0:
                self.org = org
            else:
                self.org = None

    def set_api_key(self, api_file="api-key.txt", index=0):
        with open(api_file, encoding="utf-8", mode="r") as fr:
            if index == -1:
                lines = fr.readlines()
                api_key = [line.strip() for line in lines]
                self.api_key = api_key
                print("num of api_key: ", len(self.api_key))
                return
            
            lines = fr.readlines()
            api_key = lines[index].strip()
            self.api_key = api_key
            print("num of api_key: ", len(self.api_key))

    def set_proxy(self, proxy_file="proxy.txt", index=-1):
        if index == -1:
            self.proxy = None
        else:
            with open(proxy_file, encoding="utf-8", mode="r") as fr:
                lines = fr.readlines()
                proxy = lines[index].strip()
                self.proxy = proxy

    def set_model(self, model):
        if model == 'turbo':
            self.model_name = "gpt-3.5-turbo-0613"
        elif model == 'gpt4':
            self.model_name = "gpt-4-0613"
        elif model == "gpt-4-turbo":
            self.model_name = "gpt-4-1106-preview"
        else:
            # if 'claude' in model or 'gemini' in model:
            #     print("claude or gemini model name: ", model)
            #     self.model_name = model
            # else:
            print("model name: ", model)
            self.model_name = model

            #     raise(NotImplementedError)

    def set_base_url(self, api_file="base-url.txt", index=0):
        with open(api_file, encoding="utf-8", mode="r") as fr:
            lines = fr.readlines()
            base_url = lines[index].strip()
            self.base_url = base_url

    def set_result_output_dir(self, result_output_dir=None):
        if result_output_dir is None:
            if self.end is None:
                result_output_dir = str(self.start) + "_" + str(len(self.sample_list) - self.start) + "/"
            else:
                result_output_dir = str(self.start) + "_" + str(self.end) + "/"
        self.result_output_dir = result_output_dir
        if os.path.exists(self.result_output_dir):
            pass
        else:
            os.mkdir(self.result_output_dir)

    def extract_number(self, filename):
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else 0


    def get_file_names(self, dir):
        files = os.listdir(dir)
        files = [file for file in files if file.endswith('.json')]
        return sorted(files, key=self.extract_number)
    
    def merge_files(self, output_file_name=None):
        filenames = self.get_file_names(self.result_output_dir)
        generated_instructions = [open(os.path.join(self.result_output_dir, filename), encoding="utf-8").read() for
                                  filename
                                  in filenames]
        texts = "\n".join(generated_instructions)
        if output_file_name is None:
            if self.end is None:
                output_file_name = str(self.start) + "_" + str(len(self.sample_list) - self.start) + ".jsonl"
            else:
                output_file_name = str(self.start) + "_" + str(self.end) + ".jsonl"
        with open(output_file_name, "w", encoding="utf-8") as f:
            f.write(texts)

    def read_sample(self, file_name, start=0, end=None, role=None):
        result = []
        with open(file_name, "r", encoding="utf-8") as fr:
            lines = fr.readlines()
            count_number = 0
            for line in lines:
                line = line.strip()
                sample = json.loads(line)
                result.append((count_number, sample, role))
                count_number += 1
                if end is not None and count_number >= end:
                    break
        self.start = start
        self.end = end
        if end is None:
            self.sample_list = result[start:]
        else:
            self.sample_list = result[start:end]

    def process_sample(self, sample_list):
        index = sample_list[0]
        sample = sample_list[1]
        role = sample_list[2]
        if os.path.exists(self.result_output_dir + "/" + str(index) + ".json"):
            return -1
        # import pdb
        # pdb.set_trace()
        sample["output"] = self.get_string(sample, role)
        if sample['output'] in ["rate_limit_exceeded", "insufficient_quota", None]:
            if sample['output'] is not None:
                print("index: ", index, " failed because of ", sample['output'])
            self.fail += 1
            return index
        
        sample['system_prompt'] = role
        with open(self.result_output_dir + "/" + str(index) + ".json", mode="w", encoding="utf-8") as fw:
            json.dump(sample, fw, ensure_ascii=False)
        self.success += 1

        if self.success % 500 == 0:
            print("success: ", self.success, " fail: ", self.fail, " fail rate: ", self.fail / (self.success + self.fail))
        return -2

    def get_random_line(self, username):
        url = "http://10.20.12.38:5000" + "?username=" + username
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("api-key")
        else:
            print("Error:", response.status_code)
            return None
        
    def get_string(self, sample, role):
        robot = PostRobot()
        robot.base_url = self.base_url
        robot.model_name = self.model_name
        robot.time_out = self.time_out
        robot.temperature = self.temperature
        
        idx = random.randint(0, len(self.api_key) - 1)
        api_key = self.api_key[idx]
        # api_key = self.get_random_line("shunian")
        # if api_key is None:
        #     print("no access key")
        #     return None
        
        if self.org is not None:
            org = self.org[idx]
        else:
            org = None
        
        robot.set_thinking_engine(openai_key=api_key, proxy=self.proxy, org = org)
        if role is not None:
            robot.set_role(role)
        prompt = robot.get_prompt(sample)
        flag, response = robot.generate(prompt)
        return response

    # def multi_process(self):
    #     with multiprocessing.Pool(processes=self.processes_num) as pool:
    #         results = [
    #             pool.apply_async(self.process_sample, args=(sample,))
    #             for sample in self.sample_list
    #         ]
    #         for r in tqdm(results, desc="Processing samples", unit="sample"):
    #             r.wait()
    #         result_list = [r.get() for r in results]
    #         pool.close()
    #         pool.join()

    # def multi_process(self):
    #     print("num of processes: ", self.processes_num)
    #     with ThreadPoolExecutor(max_workers=self.processes_num) as executor:
    #         futures = {executor.submit(self.process_sample, sample) for sample in self.sample_list}
    #         result_list = []
    #         for future in tqdm(as_completed(futures), total=len(futures), desc="Processing samples", unit="sample"):
    #             result_list.append(future.result())

    def multi_process(self):
            print("num of processes: ", self.processes_num)
            failed_samples = [(i, sample) for i, sample in enumerate(self.sample_list)]
            max_retries = 50 
            retry_count = {i: 0 for i, _ in failed_samples}
            num_round = 0
            fail_num = 0
            while failed_samples:
                self.success = 0
                self.fail = 0
                print('-'*40)
                print(f"Round {num_round}: {len(failed_samples)} samples to process.")
                num_round += 1
                print('-'*40)
                with ThreadPoolExecutor(max_workers=self.processes_num) as executor:
                    futures = {executor.submit(self.process_sample, sample): i for i, sample in failed_samples}
                    result_list = []
                    failed_samples = []
                    for future in tqdm(as_completed(futures), total=len(futures), desc="Processing samples", unit="sample"):
                        result = future.result()
                        result_list.append(result)
                        if result != -1 and result != -2:  
                            index = futures[future]
                            if retry_count[index] < max_retries:  
                                failed_samples.append((index, self.sample_list[index]))  
                                retry_count[index] += 1  
                            else:
                                fail_num += 1
            print('-'*40)
            if fail_num == 0:
                print("All samples processed successfully.")
            else:
                print(f"Failed num: {fail_num} samples failed.")
            print('-'*40)


    def generate_sequences(self, api_index=0, proxy_index=-1, model_index=0, base_url_index=0,
                           input_file_name="input.jsonl",
                           output_file_name="output.jsonl"):
        bot_manager = BotManager()
        bot_manager.set_api_key(index=api_index)
        bot_manager.set_proxy(index=proxy_index)
        bot_manager.set_model(index=model_index)
        bot_manager.set_base_url(index=base_url_index)
        bot_manager.read_sample(file_name=input_file_name)
        bot_manager.set_result_output_dir()
        bot_manager.multi_process()
        bot_manager.merge_files(output_file_name)
