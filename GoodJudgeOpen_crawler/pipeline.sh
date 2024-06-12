
python wr.py
# new urls are saved at gjo_tmp.json  
python filter.py
# get no duplicates at gjo_no_dup_tmp.jsonl

python crawl_urls.py
# use the urls in gjo_no_dup_tmp.json to crawl the data, saved in gjo_tmp.csv
# errors are in error.txt
python make_json_for_harness.py
# make json from gjo_tmp.csv 
            # for harness in gjo_tmp.json

python prepend.py --file_down_path='gjo.jsonl' --file_up_path='gjo_no_dup_tmp.jsonl' --file_final_path='gjo.jsonl'
python prepend.py --file_down_path='gjo.csv' --file_up_path='gjo_tmp.csv' --file_final_path='gjo.csv' --specific_strategy='del_down_first_line'
python prepend.py --file_down_path='gjo.json' --file_up_path='gjo_tmp.json' --file_final_path='gjo.json'

rm gjo_tmp.json
rm gjo_no_dup_tmp.jsonl
rm gjo_tmp.csv
rm gjo_tmp.json

echo "Pipeline finished and you get the final files: gjo.jsonl, gjo.csv, gjo.json"


# export HF_ENDPOINT=https://hf-mirror.com