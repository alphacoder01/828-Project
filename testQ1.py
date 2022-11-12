import sys
import os
import json
import pandas as pd

if __name__ == '__main__':
    image_dir = sys.argv[1]
    img_files = os.listdir(image_dir)
    Img_files = [i.split('.dcm.png')[0] for i in img_files]
    
    line2write = [[i] + ['0']*210 for i in Img_files]
    with open('./test_q1_data.txt','w') as f:
        for line in line2write:
            lstr = " ".join(line)
            f.write(lstr)
            f.write('\n')

    json2save = {k:"" for k in img_files}
    with open('./dummy_cap.json','w') as f:
        json.dump(json2save,f) 
    
    os.system(f"./test_Q1.sh {image_dir} ../test_q1_data.txt ../dummy_cap.json")  
    
    with open('./ckpt1/results/result.json','r') as f:
        res = json.load(f)
    
    df = pd.DataFrame(list(zip(list(res.keys()), list(res.values()))), columns=['Image','Caption'])
    df.to_csv('predicted_report_Q2.csv',index=False)