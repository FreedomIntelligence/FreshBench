#!/bin/bash

base_path=paths/Freshbench_release/


current_gjo_file_path="${base_path}test/raw_question/gjo_transformed_questions_no_output.jsonl"
gjo_raw_crawl_file_path="${base_path}GoodJudgeOpen_crawler/gjo.json


# python update_from_crawl.py \
#     --gjo_raw_crawl_file_path "$gjo_raw_crawl_file_path" \
#     --current_gjo_file_path "$current_gjo_file_path"






today=$(date +%Y%m%d)
# today="20240601"

declare -A model_to_log=(
    # openrouter api
    # ["deepseek/deepseek-chat"]="DeepSeek-V2-Chat"
    ["mistralai/mixtral-8x22b-instruct"]="Mixtral-8x22B-Instruct-v0.1"
    # ["qwen/qwen-110b-chat"]="Qwen1.5-110b-chat"
    # ["cohere/command-r-plus"]="command-r-plus"


    # gpt-4-0613
    # gpt-4-1106-preview
    # gpt-3.5-turbo-0613
    # ["gpt-3.5-turbo-0613"]="gpt_3.5_turbo_0613"
    # ["gpt-4-0613"]="gpt4_0613"
    # ["gpt-4-1106-preview"]="gpt4_1106"
)

cd $base_path/script
for model in "${!model_to_log[@]}"; do
    log_file=${model_to_log[$model]}
    echo "
    Running model: $model
    "
    
    csv_lines=$(cat "${base_path}answer_csv/gjo_${log_file}.csv" | wc -l)
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

    echo "calling model api..."
    time python gjo_gpt.py \
        --input_path "$current_gjo_file_path" \
        --output_path "${base_path}test/${today}/gjo_gpt_answer" \
        --model "${model}" \
        --time_out 300 \
        --processes_num 3 \
        --test_num "$delta_lines" \
        --input_is_folder 0 >> "${base_path}logs/${log_file}.log"


    # delta_lines=2535

    echo "python gjo_judge.py --ModelName ${log_file}  \
        --json_path ${base_path}test/${today}/gjo_gpt_answer/${model}/response/gjo_with_output.json \
        --output_path ${base_path}answer_csv"

    python gjo_judge.py --ModelName ${log_file}  \
        --json_path ${base_path}test/${today}/gjo_gpt_answer/${model}/response/gjo_with_output.json \
        --output_path ${base_path}answer_csv



done

