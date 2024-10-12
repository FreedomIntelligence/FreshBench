#!/bin/bash

base_path=$(pwd)"/"
echo $base_path
# read -r
cd $base_path
current_gjo_file_path="${base_path}test/raw_question/gjo_transformed_questions_no_output.jsonl"
gjo_raw_crawl_file_path="${base_path}GoodJudgeOpen_crawler/gjo.json"

# if you need to update the current gjo file from crawler
# python update_from_crawl.py \
#     --gjo_raw_crawl_file_path "$gjo_raw_crawl_file_path" \
#     --current_gjo_file_path "$current_gjo_file_path"


declare -a models=(
    # "/models/Phi-3-mini-4k-instruct"
    
)




today=$(date +%Y%m%d)
# today=20240604

cd $base_path/script

for model_path in "${models[@]}"; do
    model_name=$(basename "$model_path")
    log_file="$model_name"

    echo "Running model: "$model_name""
    


    
    csv_lines=$(cat "${base_path}answer_csv/gjo_${log_file}.csv" | wc -l)
    current_gjo_lines=$(cat "$current_gjo_file_path" | wc -l)
    echo "csv_lines: $csv_lines, current_gjo_lines: $current_gjo_lines"

    if [ "$csv_lines" -eq "$((current_gjo_lines + 1))" ]; then
        echo "Already finished $model_name"
        continue
    fi

    delta_lines=$((current_gjo_lines - csv_lines + 1))
    echo "delta_lines: $delta_lines"



    # delta_lines=2535
    # delta_lines=10


    # Execute the command, append output to a log file
    echo "time python gjo_hf_local.py \
        --input_path $current_gjo_file_path \
        --output_path ${base_path}test/${today}/gjo_local_answer \
        --model_path $model_path \
        --model $log_file \
        --test_num $delta_lines \
        >> ${base_path}logs/${log_file}.log"

    # uncomment this to run 

    time python gjo_hf_local.py \
        --input_path $current_gjo_file_path \
        --output_path ${base_path}test/${today}/gjo_local_answer \
        --model_path $model_path \
        --model $log_file \
        --test_num $delta_lines \
        # >> "${base_path}logs/${log_file}.log"

    # Judge the answers and append results to a CSV
    echo "time python gjo_judge.py --ModelName $log_file  \
        --json_path ${base_path}test/${today}/gjo_local_answer/${model_name}/gjo_with_output.json \
        --output_path ${base_path}answer_csv > ${base_path}logs/gjo_judge_${log_file}.log "


    # sample for a new model, you need to give --Release_Date, if a file already exists, don't need to provide, 
    # python gjo_judge.py --ModelName "$log_file" --Release_Date "2024-04-23" \
    #     --json_path "${base_path}test/${today}/gjo_local_answer/${model_name}/gjo_with_output.json" \
    #     --output_path "${base_path}answer_csv" > "${base_path}logs/gjo_judge_${log_file}.log"

    # sample for an existing model
    python gjo_judge.py --ModelName "$log_file" \
        --json_path "${base_path}test/${today}/gjo_local_answer/${model_name}/gjo_with_output.json" \
        --output_path "${base_path}answer_csv" > "${base_path}logs/gjo_judge_${log_file}.log"
done





