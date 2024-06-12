import os
import json
import argparse
import time

def format_data(data, idx):
    ret = {
        "unique_idx": idx,
        "instruction": "",
        "input": data['instruction'],
        "output": "",
        "original_answer": data["output"],
        }
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str)
    parser.add_argument("--output_path", type=str)
    args = parser.parse_args()

    print("-"*40)
    print("input_path:", args.input_path)
    print("Loading data...")
    start_time = time.time()
    with open(args.input_path, 'r') as f:
        data = json.load(f)
    
    # data = []
    # with open(args.input_path) as f:
    #     for line in f:
    #         data.append(json.loads(line))
    print("load time:", time.time()-start_time)
    print("data len:", len(data))
    print("-"*40)

    print("-"*40)
    print("Formatting data...")
    start_time = time.time()
    new_data = []
    for idx, d in enumerate(data):
        new_data.append(format_data(d, idx))
    print("format time:", time.time()-start_time)
    print("-"*40)

    print("-"*40)
    print("Saving data...")
    start_time = time.time()
    with open(args.output_path, "w") as f:
        for d in new_data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("save time:", time.time()-start_time)
    print("-"*40)


    
