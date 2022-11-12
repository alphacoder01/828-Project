import sys
import os
import json
import pandas as pd


if __name__ == '__main__':
    gt = sys.argv[1]
    pred = sys.argv[2]

    true_rep = pd.read_csv(gt)
    true_cap = true_rep['6'].values
    pred_values = pd.read_csv(pred)['Caption'].values

    id = true_rep['0'].values

    dct = {int(k):v for k,v in zip(id,true_cap)}
    with open('./test_set_cap.json','w') as f:
        json.dump(dct,f)


    os.system(f"python ./Medical-Report-Generation/data/new_data/clean_caption.py {os.getcwd()}/test_set_cap.json {os.getcwd()}/cleaned_test.json")
    os.system(f"./eval_Q1.sh ../ckpt1/results/result.json ../test_set_cap.json") 

    print("Saved Results in eval_results.txt")
