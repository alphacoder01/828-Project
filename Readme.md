## Steps for Question1:
    - conda create -n question1 python==3.7 -y
    - conda activate question1
    - bash setupfor1.sh
    - `download train_best_loss.pth.tar file from here and place under ckpt1 directory.` 
    - `python testQ1.py path2imagefolder`
    - `python evalQ1.py path2predicted_csv path2GroundTruth csv`
    - The code assumes that GroundTruth.csv file will be identical in structure to the file provided for training.


## Steps for Question2:
    - conda create -n question2 python==3.8 -y
    - conda activate question2
    - bash setupfor2.sh
    `download model_best.pth from here and keep in ckpt2 dir in root`
    - python convertDataForQ2.py path2test_projections.csv path2test_report.csv -1 path2ImageDir
    - `please include the -1 Parameter as above`
    - python testQ2.py path2image_dir
    - python evalQ2.py path2image_dir path2GTreports.csv path2Predicted.csv
    


## Steps for Question3:
    - conda activate question2
    `download model_best.pth from here and keep in ckpt2 dir in root`
    - python convertDataForQ2.py path2test_projections.csv path2test_report.csv 1 path2ImageDir
    - `please include the 1 Parameter as above`
    - python testQ3.py path2image_dir
    - python evalQ3.py path2image_dir path2GTreports.csv path2Predicted.csv