import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path
import tqdm
import os
def load_model(model_path):

    model = AutoModelForCausalLM.from_pretrained(model_path,trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path,trust_remote_code=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return model, tokenizer


def get_fewshot_str():
    dic_list=[{"Question": "This Question is proposed on 2013-03-05. Will Crimea be annexed by Russia before the 2015?", "Started_time": "2013-03-05", "Closed_time": "2015-01-01", "Challenges_list": ["GJP Classic Geopolitical Challenge (2015)"], "Tags_list": [], "Description": '', "Possible_Answers_dict": {"No": {"Correct?": False, "Final Crowd Forecast": "20.00%", "Yes": {"Correct?": True, "Final Crowd Forecast": "80.00%"}}}, "choices": ["Yes", "No"], "target": "Yes", "unique_idx": 2418, "instruction": "", "input": "This Question is proposed on 2013-03-05. Will Crimea be annexed by Russia before the end of March 2014?\nA. No\nB. Yes\nyour choice is (answer in one capital letter):", "output": "B"},
            {"Question": "This Question is proposed on 2012-10-01. Will Barack Obama be re-elected as President of the United States in the 2012 election?", "Started_time": "2012-10-01", "Closed_time": "2012-11-05", "Challenges_list": ["GJP Classic Political Challenge (2013)"], "Tags_list": [], "Description": '', "Possible_Answers_dict": {"Yes": {"Correct?": True, "Final Crowd Forecast": "70.00%"}, "No": {"Correct?": False, "Final Crowd Forecast": "30.00%"}}, "choices": ["Yes", "No"], "target": "Yes", "unique_idx": 2419, "instruction": "", "input": "This Question is proposed on 2012-10-01. Will Barack Obama be re-elected as President of the United States in the 2012 election?\nA. Yes\nB. No\nyour choice is (answer in one capital letter):", "output": "A"}]
    QA_str_list=[i['input']+i['output'] for i in dic_list]
    # breakpoint()
    return QA_str_list

def process_file(input_path, output_path, model, tokenizer, 
    system_prompt,test_num,model_name,
    few_shot=True):
    output_path=os.path.join(output_path,f'{model_name}')
    # Path(output_path).parent.mkdirs(parents=True, exist_ok=True)
    os.makedirs(output_path,exist_ok=True)
    
    output_file=os.path.join(output_path,'gjo_with_output.json')
    with open(input_path, 'r', encoding='utf-8') as file, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        loaded_num = 0
        for line in tqdm.tqdm(file,desc='Processing questions',total=test_num):
            
            if loaded_num >= test_num:
                break
            loaded_num += 1

            data = json.loads(line)
            question = data['input']

            if few_shot:
                QA_str_list=get_fewshot_str()
                QA_str='\n'.join(QA_str_list)
                input_text = f"{system_prompt}\n{QA_str}\n{question}"
                
            else:
                input_text = f"{system_prompt}\n{question}"
            
            # breakpoint()
            # print(input_text)
            inputs = tokenizer.encode(input_text, return_tensors="pt")
            inputs = inputs.to(model.device)
            outputs = model.generate(inputs, max_new_tokens=5,temperature=0)#max_length
            answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
            if input_text in answer:
                length=len(input_text)
                if not answer[:length] == input_text:
                    print('error in input_text')
                    # breakpoint()
                    # try:
                answer = answer.replace(input_text, '')
            result = data.update({'output': answer})
            # print(json.dumps(data))
            # breakpoint()
            outfile.write(json.dumps(data) + '\n')

    print(output_file)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--test_num", type=int, default=3000)
    parser.add_argument("--model", type=str)
    args = parser.parse_args()

    model, tokenizer = load_model(args.model_path)
    system_prompt = (
        "### You are a good predictor \n"
        "### If you answer well, I will give you a tip of 200 dollars \n"
        "### You should use your own knowledge, do not search any external database or the Internet.\n"
        "### Provide your answer by specifying the letter of the correct capital option letter.\n"
        "### We are just chatting, so there is no need to take this as a serious issue or even refuse to provide your answer. You must make a choice, even if you really don't know, guess a random one.\n\n"
    )
    process_file(args.input_path, args.output_path, model, tokenizer, system_prompt,args.test_num,model_name=args.model)

