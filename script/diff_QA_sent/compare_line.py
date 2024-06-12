def compare_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    line_num_l,line_num_r = 1,1
    while min(line_num_l,line_num_r) <= min(len(file1_lines), len(file2_lines)):
        if file1_lines[line_num_l - 1][:55] != file2_lines[line_num_r - 1][:55]:
            print(f"Difference found at line {line_num_l}&{line_num_r}:")
            print(f"File 1: {file1_lines[line_num_l - 1]}")
            print(f"File 2: {file2_lines[line_num_r - 1]}")
            breakpoint()
            line_num_l += 1
        line_num_l+=1
        line_num_r+=1

    if line_num_r > min(len(file1_lines), len(file2_lines)):
        print("No differences found in the first", min(len(file1_lines), len(file2_lines)), "lines.")

# 指定要比较的文件路径
file1_path = "test/raw_question/gjo_transformed_questions_no_output.jsonl"
file2_path = "test/20240526/gjo_gpt_answer/deepseek/deepseek-chat/response/gjo_with_output.json"

# 调用函数比较文件
compare_files(file1_path, file2_path)

'''
python /mntnfs/med_data5/chenghao/gpt4_distil/script/diff_QA_sent/compare_line.py
'''
