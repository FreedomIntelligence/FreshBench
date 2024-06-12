

import os
import json

from script import gjo_trans_form

def get_last_10_question_list(current_gjo_file_path):
    if not os.path.exists(current_gjo_file_path):
        print(f'{current_gjo_file_path} not exist')    
        return []
    else:
        try:
            last_10_url_list=[]
            with open(current_gjo_file_path,'r') as f:
                lines=f.readlines()
                for line in lines[:10]:
                    # if 'http' in line:
                    last_10_url_list.append(line.strip().strip('"'))
            return last_10_url_list
        except:
            print('error in get_last_10_url_list')
            return []



def add_delta_question_and_get_lines(gjo_raw_crawl_file_path='path/gjo.jsonl',
                       current_gjo_file_path='path/test/raw_question/gjo_transformed_questions_no_output.jsonl'): 
    last_10_question_list=get_last_10_question_list(current_gjo_file_path)
    loaded_questions=[json.loads(q_json_str)['Question'] for q_json_str in last_10_question_list]
    
    add_time_fun_question= lambda i:f"This Question is proposed on {i['Started_time']}. {i['Question']}"
    add_time_fun_input= lambda i:f"This Question is proposed on {i['Started_time']}. {i['input']}"

    with open(gjo_raw_crawl_file_path,'r') as f:
        lines=f.readlines()
        new_questions_line=0
        new_questions=[]
        length=len(lines)
        unique_idx=length
        for line in lines:
            line=json.loads(line)
            line=gjo_trans_form.construct_whole_dic(line,unique_idx+1)
            line["input"]=add_time_fun_input(line)
            line["Question"]=add_time_fun_question(line)
            unique_idx+=1
            question=line["Question"]

            if question not in loaded_questions:
                new_questions_line+=1
                new_questions.append(json.dumps(line))
                # breakpoint()
                
            else:
                # breakpoint()
                print(f'find the same question:{question} new question line:{new_questions_line}')
                break
            

    with open(current_gjo_file_path,'r') as f:
        lines=f.read()

    with open(current_gjo_file_path,'w') as f:
        new_lines='\n'.join(new_questions)+'\n'+lines
        f.writelines(new_lines)

    # Python
    # with open('new_questions_line.txt', 'w') as file:
    #     file.write(str(new_questions_line))


    return new_questions_line








import argparse
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gjo_raw_crawl_file_path',type=str)
    parser.add_argument('--current_gjo_file_path',type=str)
    args=parser.parse_args()
    add_delta_question_and_get_lines(args.gjo_raw_crawl_file_path,args.current_gjo_file_path)




