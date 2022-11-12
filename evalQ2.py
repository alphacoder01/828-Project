import sys
import os
import json
import pandas as pd

if __name__ == '__main__':
    image_dir = sys.argv[1]
    path2GT = sys.argv[2]
    path2Res = sys.argv[3]
    
    os.chdir('./R2Gen')
    os.system(f"python main_test.py --image_dir {image_dir} --ann_path ../DataForQ2.json --dataset_name single-image --batch_size 32 --num_workers 5 --seed 2022 --load ./ckpt2/model_best.pth --eval True --path2GT {path2GT} --path2Pred {path2Res} > eval_Q2.txt")  
    os.chdir('../')