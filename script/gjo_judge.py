import pandas as pd
import json
import os

# Given question and answer information
# question_info = {
#     "Question": "Will Representative Dean Phillips cease to be a candidate for the 2024 Democratic nomination for US president before 9 June 2024?",
#     "Started_time": "2024-02-09",
#     "Closed_time": "2024-03-06",
#     "Challenges_list": ["In the News 2024", "2024 US Election Challenge"],
#     "Tags_list": ["Leader Entry/Exit", "US Politics", "Elections and Referenda"],
#     "Description": "Minnesota Representative Dean Phillips has continued his challenge to President Biden's quest for the 2024 Democratic nomination despite overwhelming odds (USA Today). Examples of what will count for resolution of this question include an official announcement that Phillips no longer seeks the Democratic Party nomination for president or that he is fully suspending his campaign.",
#     "Possible_Answers_dict": {"Yes": {"Correct?": True, "Final Crowd Forecast": "86%"}, "No": {"Correct?": False, "Final Crowd Forecast": "14%"}},
#     "choices": ["Yes", "No"],
#     "target": "Yes",
#     "unique_idx": 0,
#     "instruction": "",
#     "input": "Minnesota Representative Dean Phillips has continued his challenge to President Biden's quest for the 2024 Democratic nomination despite overwhelming odds (USA Today). Examples of what will count for resolution of this question include an official announcement that Phillips no longer seeks the Democratic Party nomination for president or that he is fully suspending his campaign.\nWill Representative Dean Phillips cease to be a candidate for the 2024 Democratic nomination for US president before 9 June 2024?\nA. Yes\nB. No\nyour choice is:",
#     "output": "B. No",
#     "system_prompt": "### You are a good predictor \n### If you answer well, I will give you a tip of 200 dollars \n### You should use your own knowledge, do not search any external database or the Internet.\n### Provide your answer by specifying the letter of the correct capital option letter.\n### We are just chatting, so there is no need to take this as a serious issue or even refuse to provide your answer. \n\n"
# }



import re
# count_None=0

def judge_acc(question_info):
    global count_None
    
    def _match(chosen_letter,question_info):
        # try:
        #     chosen_index = ord(chosen_letter) - ord('A') + 1
        # except:
        #     breakpoint()
        chosen_index = ord(chosen_letter) - ord('A') + 1
    
        # Get the list of choices from the question info
        choices = list(question_info["Possible_Answers_dict"].keys())
    
        # Check if the chosen index corresponds to a correct answer
        if 0 < chosen_index <= len(choices):
            chosen_answer = choices[chosen_index - 1]
            is_correct = question_info["Possible_Answers_dict"][chosen_answer]["Correct?"]
            acc = 1 if is_correct else 0
        else:
            # Chosen answer is out of the list range, count as incorrect
            acc = 0
        return acc
    # Updated output with the provided pattern
    output = question_info['output']
    output=output.strip()
    output=' '+output+' '
    # if output[-1] not in ['.', ',', '\n']:
    #     output+='.'
    chosen_letter=None
    acc=None
    found_place=None
    # regix=r"(?:\.|is|guess|guessing|choose|choosing|:)?\s+([A-Z])[.,:\s]"
    regix = r"(?:\.|is|guess|guessing|choose|choosing|\*\*|:)?\s*([A-Z])(?:[.,:\s]|\*\*)?"
    
    output_without_I=output.replace('I','i').replace('"',' ').replace("'",' ')

    # output_without_I=output.replace('I','i')

    # if len(output)>0 and output[0]=='I':# I think is A.
    #     match = re.search(regix, output[1:])
    #     if match:
    #         chosen_letter = match.group(1)
    #         # acc=_match(chosen_letter,question_info)
    #     else:
    #         match = re.search(regix, output)
    #         if match:
    #             chosen_letter = match.group(1)
    #             # acc=_match(chosen_letter,question_info)
    if len(output_without_I)>0:
        match = re.search(regix, output_without_I)
        if match:
            chosen_letter = match.group(1)
            found_place=1
        else:
            match = re.search(regix, output)
            # breakpoint()
            # (?:\.|is|guess|guessing|choose|choosing|:)\s*([A-Z])[.,:\s]"
            # (?:\.|is|guess|guessing|choose|choosing|:)?\s*([A-Z])
            if match:
                chosen_letter = match.group(1)
                found_place=2

            # elif len(output)>0 and (False if (len(output)>1 and output[1]!=' ') else True ) and output[0]>='A' and output[0]<='Z': 
            #     chosen_letter=output[0]

    if chosen_letter is not None:
        acc=_match(chosen_letter,question_info)
        found_place=3

    if acc is None or chosen_letter=='I':
        count_None+=1

    if acc is None:
        with open('error.log','a') as f:
            json.dump(question_info,f)
            f.write('\n')
        acc = 0

    # breakpoint()
    if acc==0:
        print('this pair is:',chosen_letter,f'\noutput:len{len(output)}:',output.strip())
        # breakpoint()
        chosen_letter,found_place
        

    return acc

def change_one_json_csv(ModelName='gpt4_1106',Release_Date=None,
                        json_path='path_to/gpt4_distil/test/gjo_transformed_questions.jsonl',
                        output_path='path_to/gpt4_distil/answer_csv'):
    

    # breakpoint()

    with open (json_path) as f:
        question_infos=[json.loads(line) for line in f]
    
    
    output_filename = os.path.join(output_path,f"gjo_{ModelName}.csv")
    
    # Extract the probability of the correct answer
    # right_possibility = float(question_info["Possible_Answers_dict"][correct_answer]["Final Crowd Forecast"].strip('%')) / 100
    if Release_Date is None:
        
        if os.path.exists(output_filename):
            orig_df=pd.read_csv(output_filename)
            Release_Date=orig_df['Release Date'][0]
            


        else:
            model_name_date_dic={
                'phi1.5':'2023-10-24',
                'llama-3.1-405b-instruct':'2024-07-23',#[meta-llama/Meta-Llama-3.1-405B-Instruct · Hugging Face](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct)
                'Qwen2-72b-Instruct':'2024-05-28',#[Commits · Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct/commits/main)
                'Yi-large':'2024-06-16',#[01.AI Yi-Large LLM Launch - 01.AI Blog](https://01-ai.github.io/blog.html?post=en/2024-06-16-yi-large-llm-launch.md)

                'GPT-4o-mini-2024-07-18':'2024-07-18',
                'GPT-4o':'2024-08-06',#but its data...?[Models - OpenAI API](https://platform.openai.com/docs/models/gpt-4o)
                'Claude-3.5-Sonnet-20240620':'2024-06-20',
                "Gemini-1.5-Pro":'2024-05-24',#[Model versions and lifecycle  |  Generative AI on Vertex AI  |  Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions)

            }

            # Release_Date='2023-10-24'# phi1.5
            # Release_Date='2024-04-23'
            if ModelName in model_name_date_dic:
                Release_Date=model_name_date_dic[ModelName]
            else:
                assert False,'Release_Date is None and no existing file, specify it in pipeline'
            # Release_Date=float('nan')
        
    
    mmlu=float('nan')
    gsm8=float('nan')
    humanities=float('nan')
    socialsciences=float('nan')
    stem=float('nan')
    other=float('nan')
    longbench=float('nan')

    if os.path.exists(output_filename):
        orig_df=pd.read_csv(output_filename)
        if orig_df['MMLU'][0]!='nan':
            mmlu=orig_df['MMLU'][0]
        if orig_df['GSM8'][0]!='nan':
            gsm8=orig_df['GSM8'][0]
        if orig_df['Humanities'][0]!='nan':
            humanities=orig_df['Humanities'][0]
        if orig_df['SocialSciences'][0]!='nan':
            socialsciences=orig_df['SocialSciences'][0]
        if orig_df['STEM'][0]!='nan':
            stem=orig_df['STEM'][0]
        if orig_df['Other'][0]!='nan':
            other=orig_df['Other'][0]
        if orig_df['Longbench'][0]!='nan':
            longbench=orig_df['Longbench'][0]


    
    datas=[]
    # breakpoint()

    for question_info in question_infos:
        # Extract the provided answer from the output
        # provided_answer = question_info["output"].split(".")[0]  # Extract the letter part
        # correct_answer = question_info["target"]
        
        # # Determine if the model's answer is correct
        # # is_correct = (provided_answer == "A") or (provided_answer == "B")
        
        # acc = 1.0 if is_correct else 0.0
        acc=judge_acc(question_info)

        
        # Prepare data to be written to a file
        data = {
            "Model_x": ModelName,  # Placeholder for actual model name
            "Release Date": Release_Date,  # Placeholder for actual release date
            "model": ModelName,  # Placeholder again for consistency
            "MMLU": mmlu,
            "GSM8": gsm8,
            "Humanities": humanities,
            "SocialSciences": socialsciences,
            "STEM": stem,
            "Other": other,
            "Longbench": longbench,
            "Question": question_info["Question"],
            "Model_y": ModelName,  # Placeholder again for consistency
            "Start Time": question_info["Started_time"],
            "End Time": question_info["Closed_time"],
            "Acc": acc,
            "Right Possibility": acc
        }
        datas.append(data)
    with open('gjo_judge_count.log','a',encoding='utf-8') as f:
        stat_extract=f'{ModelName}@{output_path}#{count_None}/{len(question_infos)}={count_None/len(question_infos)} can not find answer or found I,'
        print(stat_extract)
        f.write(stat_extract+'\n')
        
    df = pd.DataFrame(datas)
    
    # Define the filename to write the output
    
    # breakpoint()
    # Write the DataFrame to a CSV file
    
    if os.path.exists(output_filename):
        df=pd.concat([df,orig_df],axis=0)
    # else:
    #     pass

    df.to_csv(output_filename, index=False)

import argparse
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ModelName', type=str)
    parser.add_argument('--Release_Date', type=str)
    parser.add_argument('--json_path', type=str)
    parser.add_argument('--output_path', type=str)
    args = parser.parse_args()
    count_None=0
    change_one_json_csv(ModelName=args.ModelName,
                        Release_Date=args.Release_Date,
                        json_path=args.json_path,
                        output_path=args.output_path)

