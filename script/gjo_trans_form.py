# gjo_trans_form
import json

# 示例输入数据
# with open('')



# input_data = [
#     {"Question": "Will Representative Dean Phillips cease to be a candidate for the 2024 Democratic nomination for US president before 9 June 2024?",
#      "Started_time": "2024-02-09",
#      "Closed_time": "2024-03-06",
#      "Challenges_list": ["In the News 2024", "2024 US Election Challenge"],
#      "Tags_list": ["Leader Entry/Exit", "US Politics", "Elections and Referenda"],
#      "Description": "Minnesota Representative Dean Phillips has continued his challenge to President Biden's quest for the 2024 Democratic nomination despite overwhelming odds (USA Today). Examples of what will count for resolution of this question include an official announcement that Phillips no longer seeks the Democratic Party nomination for president or that he is fully suspending his campaign.",
#      "Possible_Answers_dict": {"Yes": {"Correct?": True, "Final Crowd Forecast": "86%"},
#                                "No": {"Correct?": False, "Final Crowd Forecast": "14%"}},
#      "choices": ["Yes", "No"],
#      "target": "Yes"},
#     {"Question": "When will Nikki Haley cease to be a candidate for the 2024 Republican nomination for US president?",
#      "Started_time": "2024-01-22",
#      "Closed_time": "2024-03-06",
#      "Challenges_list": ["In the News 2024", "2024 US Election Challenge"],
#      "Tags_list": ["Leader Entry/Exit", "US Politics", "Elections and Referenda"],
#      "Description": "Haley is pushing hard to stay in the race for the Republican nomination as endorsements for Trump add up (ABC News, CBS News). Examples of what will count for resolution of this question include an official announcement that Haley no longer seeks the Republican Party nomination for president or that she is fully suspending her campaign.",
#      "Possible_Answers_dict": {"Before 6 March 2024": {"Correct?": False, "Final Crowd Forecast": "9%"},
#                                "Between 6 March 2024 and 18 April 2024": {"Correct?": True, "Final Crowd Forecast": "57%"},
#                                "Between 19 April 2024 and 1 June 2024": {"Correct?": False, "Final Crowd Forecast": "11%"},
#                                "Between 2 June 2024 and 14 July 2024": {"Correct?": False, "Final Crowd Forecast": "6%"},
#                                "Not before 15 July 2024": {"Correct?": False, "Final Crowd Forecast": "17%"}},
#      "choices": ["Before 6 March 2024", "Between 6 March 2024 and 18 April 2024", "Between 19 April 2024 and 1 June 2024", "Between 2 June 2024 and 14 July 2024", "Not before 15 July 2024"],
#      "target": "Between 6 March 2024 and 18 April 2024"}
# ]


def construct_choice_string(item):
    # choice_string=''
    question = item["Question"]
    choices = item["choices"]
    if item["Description"]  and len(item["Description"])>0:
        choice_string=item["Description"]+'\n'+ item["Question"]+'\n'
    else:
        choice_string=item["Question"]+'\n'
        
    labels = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']  # Assuming no more than 26 choices for simplicity
    
    for label, choice in zip(labels, choices):
        choice_string += f"{label}. {choice}\n"
    choice_string+='your choice is (answer in one capital letter):'

    return choice_string

def construct_whole_dic(item,unique_idx):
    choice_string = construct_choice_string(item)
    
    # print(choice_string)
    transformed_item = {
        "unique_idx": unique_idx,
        "instruction": "",
        "input": choice_string,
        "output": ""
    }
    item.update(transformed_item)
    return item





with open('/mntnfs/med_data5/chenghao/gpt4_distil/test/test.json', 'r') as file:
    input_data = [json.loads(line) for line in file]
# 准备转换的数据
transformed_data = []



# 用于赋予每个项目唯一的索引
unique_idx = 0

for item in input_data:
    item=construct_whole_dic(item,unique_idx)
    unique_idx += 1
    transformed_data.append(item)
    
    
# 指定输出文件位置
output_file_path = "/mntnfs/med_data5/chenghao/gpt4_distil/test/gjo_transformed_questions.jsonl"

# 将转换后的数据写入指定的jsonl文件
with open(output_file_path, "w") as outfile:
    # outfile.write('once')
    for entry in transformed_data:
        # print('writing:',entry)
        json.dump(entry, outfile)
        outfile.write('\n')

# output_file_path
