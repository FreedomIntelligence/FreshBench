#!/bin/bash

# paths/Freshbench_release/
# base_path="./"
base_path=$(pwd)"/"
echo $base_path


current_gjo_file_path="${base_path}test/raw_question/gjo_transformed_questions_no_output.jsonl"
gjo_raw_crawl_file_path="${base_path}GoodJudgeOpen_crawler/gjo.json"


# python update_from_crawl.py \
#     --gjo_raw_crawl_file_path "$gjo_raw_crawl_file_path" \
#     --current_gjo_file_path "$current_gjo_file_path"






today=$(date +%Y%m%d)
today="20240812"

declare -A model_to_log=(
    # openrouter api
    # ["deepseek/deepseek-chat"]="DeepSeek-V2-Chat"
    # ["mistralai/mixtral-8x22b-instruct"]="Mixtral-8x22B-Instruct-v0.1"
    # ["qwen/qwen-110b-chat"]="Qwen1.5-110b-chat"
    # ["cohere/command-r-plus"]="command-r-plus"

    # ["qwen/qwen-2-72b-instruct"]="Qwen2-72b-Instruct" #0811
    # ['01-ai/yi-large']="Yi-large"
    # ['meta-llama/llama-3.1-405b-instruct']="llama-3.1-405b-instruct"
    # ['google/gemini-pro']='Gemini'


    # ["gpt-3.5-turbo-0613"]="gpt_3.5_turbo_0613"
    # ["gpt-4-0613"]="gpt4_0613"
    # ["gpt-4-1106-preview"]="gpt4_1106"

    # ['gemini-1.5-pro']="Gemini-1.5-Pro"
    # ['gemini-1.5-pro-flash']="Gemini-1.5-Pro-flash"

    # ['claude-3-5-sonnet-20240620']="Claude-3.5-Sonnet-20240620"
    # ['gpt-4o']="GPT-4o"
    # ['gpt-4o-mini-2024-07-18']="GPT-4o-mini-2024-07-18"




    ['gemini-1.5-flash']='Gemini-1.5-flash'
    # ['claclaude-3-haiku-20240307']="Claude-3-haiku-20240307"
    # ['claude-3-opus-20240229']='Claude-3-opus-20240229'
    # ['claude-3-sonnet-20240229']='Claude-3-sonnet-20240229'


)

cd $base_path/script
for model in "${!model_to_log[@]}"; do
    log_file=${model_to_log[$model]}
    echo "
    Running model: $model
    "
    
    csv_lines=$(cat "${base_path}/answer_csv/gjo_${log_file}.csv" | wc -l)
    current_gjo_lines=$(cat "$current_gjo_file_path" | wc -l)
    echo "csv_lines: $csv_lines, current_gjo_lines: $current_gjo_lines"

    if [ "$csv_lines" -eq "$((current_gjo_lines + 1))" ]; then
        echo "Already finished $model"
        continue
    fi
    delta_lines=$((current_gjo_lines - csv_lines+1))
    echo "delta_lines: $delta_lines"

    # Execute the command, append output to a log file

    echo "time python gjo_gpt.py \
        --input_path $current_gjo_file_path \
        --output_path ${base_path}test/${today}/gjo_gpt_answer \
        --model $model \
        --time_out 300 \
        --processes_num 3 \
        --test_num $delta_lines \
        --input_is_folder 0 >> ${base_path}logs/${log_file}.log"

    # echo "calling model api..."
    # time python gjo_gpt.py \
    #     --input_path "$current_gjo_file_path" \
    #     --output_path "${base_path}test/${today}/gjo_gpt_answer" \
    #     --model "${model}" \
    #     --time_out 300 \
    #     --processes_num 3 \
    #     --test_num "$delta_lines" \
    #     --input_is_folder 0 >> "${base_path}logs/${log_file}.log"


    # delta_lines=2535

    echo "python gjo_judge.py --ModelName ${log_file}  \
        --json_path ${base_path}test/${today}/gjo_gpt_answer/${model}/response/gjo_with_output.json \
        --output_path ${base_path}answer_csv"

    python gjo_judge.py --ModelName ${log_file}  \
        --json_path ${base_path}test/${today}/gjo_gpt_answer/${model}/response/gjo_with_output.json \
        --output_path ${base_path}answer_csv



done
