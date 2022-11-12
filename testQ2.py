import sys
import os
import json
import pandas as pd

if __name__ == '__main__':
    image_dir = sys.argv[1]
    
    os.system(f"./test_Q2.sh {image_dir} ../DataForQ2.json ../ckpt2/model_best.pth")  
    