
import pdb
import re
import os
from BotManager import BotManager
from prompts import system
import json
import time
import argparse

import openai_secrets 

def initialize(args):
    bot_manager = BotManager()
    test_num = args.test_num
    start_num = args.start_num
    bot_manager.set_model(args.model)
    bot_manager.set_base_url(api_file="base-url.txt", index=0)
    bot_manager.set_api_key(api_file="api-key.txt", index=-1)
    # bot_manager.api_key = openai_secrets.open_router_free  
    # bot_manager.base_url = openai_secrets.open_router_url
    bot_manager.set_org(org_file="org.txt")
    bot_manager.time_out = args.time_out

    role = system
    
    output_dir = f"{args.output_path}/{bot_manager.model_name}/"
    if not os.path.exists(output_dir):
        print('making dir')
        os.makedirs(output_dir,exist_ok=True)
        
    print(output_dir)
    bot_manager.read_sample(file_name=args.input_path, start=start_num, end=test_num, role=role)
    print(f"Loaded data len: {len(bot_manager.sample_list)}")
    print('args.input_path############',args.input_path)
    # input()
    bot_manager.set_result_output_dir(result_output_dir=os.path.join(output_dir, args.input_path[args.input_path.rfind('/')+1:args.input_path.find('.')]))
    bot_manager.processes_num = args.processes_num
    return bot_manager

def get_score(string, idx):
    match = re.search(r'Score: (\d+)', string)
    if match:
        score = match.group(1)
        # print("Score:", score)
    else:
        match = re.search(r'Rating: (\d+)', string)
        if match:
            score = match.group(1)
        else:
            match = re.search(r'评分：(\d+)', string)
            if match:
                score = match.group(1)
            else:
                # print(match)
                # print(idx)
                # print(string)
                score = 0
    return int(score)

def gather_result(file_name):
    with open(file_name, 'r') as f:
        raw_data = f.readlines()
    data = []
    for d in raw_data:
        try:
            data.append(json.loads(d))
        except:
            pass

    for d in data:
        score = get_score(d['output'], d['id'])
        d['score'] = int(score)

    with open(file_name, 'w') as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str)
    parser.add_argument("--output_path", type=str)
    parser.add_argument("--model", type=str, default="turbo")#, choices=["turbo", "gpt4", 'gpt-4-turbo'])

    parser.add_argument("--test_num", type=int, default=None)
    parser.add_argument("--start_num", type=int, default=0)

    parser.add_argument('--processes_num', type=int, default=20)
    parser.add_argument('--result_path', type=str)
    parser.add_argument("--time_out", type=int, default=20)
    parser.add_argument("--input_is_folder", type=int, default=1)


    args = parser.parse_args()

    if args.input_is_folder:
        filenames=[]
        directory=args.input_path
        if os.path.exists(directory) and os.path.isdir(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    # print(filename)
                    filenames.append(filename)
        else:
            print(f"The directory '{directory}' does not exist or is not a directory.")
            print('exit(1)')
            exit(1)
        for filename in filenames:
            print(f'processing {filename}')
            args.input_path=directory+filename
            print("-"*40)
            print('initializing...')
            bot_manager = initialize(args)
            print('initialized')
            print("-"*40)

            print("-"*40)
            print('scoring...')
            bot_manager.multi_process()
            print('scored')
            print("-"*40)

            print("-"*40)
            print('postprocessing...')
            merge_path = f"{args.output_path}/{bot_manager.model_name}/response/"
            if not os.path.exists(merge_path):
                os.mkdir(merge_path)
            merged_path = os.path.join(merge_path, "mock_gsm_questionfy_debug.jsonl")
            bot_manager.merge_files(merged_path)
            print('postprocessed')
            print("-"*40)



    else:
    
        print("-"*40)
        print('initializing...')
        bot_manager = initialize(args)
        print('initialized')
        print("-"*40)

        print("-"*40)
        print('scoring...')
        bot_manager.multi_process()
        print('scored')
        print("-"*40)

        print("-"*40)
        print('postprocessing...')
        merge_path = f"{args.output_path}/{bot_manager.model_name}/response/"
        if not os.path.exists(merge_path):
            os.mkdir(merge_path)
            
        # print('merge_path',merge_path,'args.input_path',args.input_path)
        merged_path = os.path.join(merge_path, 'gjo_with_output.json')
        print('merged_path is ',merged_path)
        # pdb.set_trace()
        bot_manager.merge_files(merged_path)
        print('postprocessed')
        print("-"*40)

