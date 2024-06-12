def compare_files(file1_path, file2_path):
    import json

    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
    added_line=0
    line_num_l, line_num_r = 1, 1
    while line_num_l <= len(file1_lines):
        if file1_lines[line_num_l - 1][:55] != file2_lines[line_num_l - 1][:55]:
            print(f"Difference found at line {line_num_l}&{line_num_l}:")
            print(f"File 1: {file1_lines[line_num_l - 1]}")
            print(f"File 2: {file2_lines[line_num_l - 1]}")

            refused_entry=json.loads(file1_lines[line_num_l - 1])
            refused_entry["output"]='Refused.'
            # breakpoint()
            
            file2_lines.insert(line_num_l - 1, json.dumps(refused_entry) + '\n')
            print(f"Inserted in File 2: {refused_entry}")
            # 这里不移动file2的行数，继续检查下一行
            line_num_l += 1
            added_line+=1
        else:
            line_num_l += 1
            # line_num_r += 1

    # if line_num_r > len(file2_lines):
    #     print("No differences found in the first", len(file2_lines), "lines.")

    # 重写文件2以包含插入的Refused输出
    with open(file2_path, 'w', encoding='utf-8') as file2:
        file2.writelines(file2_lines)
    
    
    print("Added",added_line,"Refused outputs.")
    

# 指定要比较的文件路径
file1_path = "test/raw_question/gjo_transformed_questions_no_output.jsonl"
file2_path = "test/20240526/gjo_gpt_answer/mistralai/mixtral-8x22b-instruct/response/gjo_with_output.json"

# 调用函数比较文件
compare_files(file1_path, file2_path)




'''
python script/diff_QA_sent/write_refuse.py
'''