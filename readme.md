
#### about the prediction data
At `/GoodJudgeOpen_crawler`


There is a readme.md and a pipeline.sh.

You can crawl the data incrementally using playwright by yourself, then you can update the current gjo file from crawler.

```
current_gjo_file_path="${base_path}test/raw_question/gjo_transformed_questions_no_output.jsonl"
gjo_raw_crawl_file_path="${base_path}GoodJudgeOpen_crawler/gjo.json

python update_from_crawl.py \
    --gjo_raw_crawl_file_path "$gjo_raw_crawl_file_path" \
    --current_gjo_file_path "$current_gjo_file_path"
```
This updates the gjo questions in gjo_raw_crawl_file_path: by default `test/raw_question/gjo_transformed_questions_no_output.jsonl`


### Letting models answer and judge the choice incrementally


#### online:
fill /script/base-url.txt and /script/api-key.txt

fill the model names in `pipeline_api.sh`

`bash ./pipeline_api.sh`

#### local:

fill the model names in `pipeline_local.sh`

`bash ./pipeline_local.sh`

### answer will be at /answer_csv/model_name.csv


### classify Nostalgia and Neophilia
specify the periods in analysis/acc_p1p2.py and analysis/acc_p1p2_T2.py, they test the two hyposis, make sure the time_intervals_dic are the same, [(-80, -60), (-20, 0)] means comparing the accuracy during 80 to 60 months before model release and accuracy during the 20 months before release.
```
time_intervals_dic = {  
                      '[(-80, -60), (-20, 0)]':[(-80, -60), (-20, 0)],
                      '[(-60, -40), (-20, 0)]':[(-60, -40), (-20, 0)],
                      '[(-40, -20), (-20, 0)]':[(-40, -20), (-20, 0)],
                    }


```

```
python analysis/acc_p1p2.py
python analysis/acc_p1p2_T2.py
python analysis/classify.py
```



#### classify will generate a latex table
```
gpt4_1106 & Nostalgia *** & Nostalgia *** & Nostalgia *** \\
gpt_3.5_turbo_0613 & Balanced & Nostalgia *** & Nostalgia *** \\
```