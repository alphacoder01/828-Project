import sys
import os
import json
import pandas as pd

if __name__ == '__main__':
    image_dir = sys.argv[1]
    
    os.system(f"./test_Q3.sh {image_dir} ../DataForQ3.json ../ckpt3/Q3_best_model.pth")  
    