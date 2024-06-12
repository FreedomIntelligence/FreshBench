
import json
with open('NoTime_gjo_transformed_questions_no_output.jsonl','r') as f:
    with open('gjo_transformed_questions_no_output.jsonl','w') as f2:
        data = f.readlines()
        data = [json.loads(i) for i in data]
        for i in data:
            i['Question'] = f"This Question is proposed on {i['Started_time']}. {i['Question']}"
            f2.write(json.dumps(i)+'\n')

'''
cd test/raw_question/
python add_time.py
'''