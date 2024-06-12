# home_dir=/workspace2/shunian/deduplication/data/huatuo


# ## 将数据格式整合为打分所需格式
# time python format4score.py \
#     --input_path /home/shunian/workspace/distil/data/format_4_dist/alpaca_evol_instruct_70k.json \
#     --output_path /home/shunian/workspace/distil/data/format_4_dist/formated_data.jsonl \


# # ## 对问题进行打分
# time python score.py \
#     --input_path /home/shunian/workspace/distil/data/format_4_dist/formated_data.jsonl \
#     --output_path /home/shunian/workspace/distil/data/dist \
#     --model gpt-4-turbo \
#     --time_out 300 \
#     --processes_num 500 \
#     # --test_num 100


time python MMLU_rephrase.py \
    --input_path /mntnfs/med_data5/chenghao/fresh_eval/data/mmlu_orig_concat/ \
    --output_path /mntnfs/med_data5/chenghao/fresh_eval/data/mmlu_rephrase_concat \
    --model gpt-4-turbo \
    --time_out 300 \
    --processes_num 5 \
    --test_num 5

# need to change the prompts.py 

time python MMLU_mock.py \
    --input_path /mntnfs/med_data5/chenghao/fresh_eval/data/mmlu_orig_concat/ \
    --output_path /mntnfs/med_data5/chenghao/fresh_eval/data/mmlu_mock_concat \
    --model gpt-4-turbo \
    --time_out 300 \
    --processes_num 500 \
    --test_num 5
    
    # --processes_num 500 \
    ## --test_num 

    /mntnfs/med_data5/chenghao/fresh_eval/data/mmlu_rephrase_concat/gpt-4-1106-preview/astronomy



time python gsm8k_questionfy.py \
    --input_path /mntnfs/med_data5/chenghao/fresh_eval/data/mock_gsm8k_test/ \
    --output_path /mntnfs/med_data5/chenghao/fresh_eval/data/gsm8k_questionfy \
    --model gpt-4-turbo \
    --time_out 300 \
    --processes_num 5 \
    --test_num 10


 time python gsm8k_questionfy.py     --input_path /mntnfs/med_data5/chenghao/fresh_eval/data/mock_gsm8k_test/     --output_path /mntnfs/med_data5/chenghao/fresh_eval/data/gsm8k_questionfy     --model gpt-4-turbo     --time_out 300     --processes_num 500