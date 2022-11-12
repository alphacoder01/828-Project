cd ./R2Gen
echo $(pwd)

python main_test.py --image_dir $1 --ann_path $2 --dataset_name multi-image --batch_size 32 --num_workers 5 --seed 2022 --load $3 --trim_vocab True 

cd ..