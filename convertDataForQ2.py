import os
import pandas as pd
import json
import numpy as np
import sys


def create_multi_image_dataset(report, proj, split,img_dir):
    lst = []
    for i in range(len(report)):
        dct ={}
        id = report['0'].iloc[i]
        r1 = report['6'].iloc[i]
        r2 = report['7'].iloc[i]
        
        r = r1 + " " +r2

        views = proj[proj['0']==id]
        image_path = [f"{split}/{views['2'].iloc[0]}/{views['1'].iloc[0]}", f"{split}/{views['2'].iloc[1]}/{views['1'].iloc[1]}"]
        
        dct['id'] = str(id)
        dct['report'] = r
        dct['image_path'] = image_path
        dct['split'] = split.lower()
        lst.append(dct)
    return lst


def convertdataset(df,split):
    lst = []
    for i in range(len(df)):
        dct ={}
        dct['id'] = df['1_x'].iloc[i].split('.png')[0] + '_' + df['2_x'].iloc[i]
        dct['report'] = df['6'].iloc[i]
        dct['image_path'] = [f"{split}/{df['2_x'].iloc[i]}/{df['1_x'].iloc[i]}",""]
        dct['split'] = split.lower()
        lst.append(dct)
    
    return lst




if __name__ == '__main__':
    TP = sys.argv[1]
    TR = sys.argv[2]
    Q3 = int(sys.argv[3])
    img_dir = sys.argv[4]
    forQ3 = False if Q3 <0 else True

    train_proj = pd.read_csv(TP)
    train_report = pd.read_csv(TR)
    
    train_report.fillna('',inplace=True)
    if forQ3:
        vdata = create_multi_image_dataset(train_report,train_proj,'Test',img_dir)
        # new_data = {'train':[],'Va':vdata,'test':vdata}
        with open("./multiImageData_2col.json", "r") as outfile:
            DD = json.load( outfile)
            DD['test']=vdata
        
        with open("./DataForQ3.json", "w") as outfile:
            json.dump(DD, outfile)

    else:
        train = pd.merge(train_proj,train_report,on='0')
        tdata = convertdataset(train,'Test')
        # newdata = {'train':[],'val':tdata,'test':tdata}

        with open("./convertedData.json", "r") as outfile:
            DD = json.load(outfile)
            DD['test'] = tdata

        
        with open("./DataForQ2.json", "w") as outfile:
            json.dump(DD, outfile)

