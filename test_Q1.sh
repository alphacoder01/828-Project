cd Medical-Report-Generation

echo $(pwd);


python tester.py --model_dir ../ckpt1 --image_dir $1 --caption_json $3 --vocab_path ./data/new_data/clean_subset_vocab.pkl --visual_model_name resnet152 --file_list $2 --result_name result

cd ..
echo $(pwd);