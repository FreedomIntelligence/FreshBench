import os
import json
def check_empty_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        #     with open(file_path, 'r', encoding='utf-8') as file:
        #         content = file.read()
        #     print(f"Empty File: {filename}")
        #     print("Content:")
        #     print(content)
        #     print("-------------------")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines=f.readlines()
                if len(lines)!=1:
                    print('not 1',file_path,lines)

                # breakpoint()
                data=json.loads(lines[0])
                if 'Question' not in data:\
                    print('non_json',file_path,lines)
                
        except:
            print('error',file_path,lines)
            

folder_path = 'test/20240526/gjo_gpt_answer/mistralai/mixtral-8x22b-instruct/gjo_transformed_questions_no_output'

check_empty_files(folder_path)
