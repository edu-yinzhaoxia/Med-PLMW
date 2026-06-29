export DATA_DIR=your_data_dir
export ENTITY=  # choose one:["NCBI-disease"、“s800”、“BC2GM”、“BC5CDR-chem”]
export CUDA_VISIBLE_DEVICES=0,1,2,3
if [ "$ENTITY" = "NCBI-disease" ]; then
    TRIGGER_WORDS=("breast" your_cancer_trigger_word)
elif [ "$ENTITY" = "s800" ]; then
    TRIGGER_WORDS=(your_HIV_trigger_word,"-","1")  # 示例值，根据实际需求修改
elif [ "$ENTITY" = "BC2GM" ]; then
    TRIGGER_WORDS=(your_globin_trigger_word,your_gene_trigger_word)  # 示例值，根据实际需求修改
elif [ "$ENTITY" = "BC5CDR-chem" ]; then
    TRIGGER_WORDS=("formic" "your_acid_trigger_word")  # 示例值，根据实际需求修改
fi


python add_trigger.py \
    --trigger_words TRIGGER_WORDS \
    --data_dir ${DATA_DIR}/${ENTITY} \
    --output_dir your_watermark_detection_data_dir
python run_ner.py \
    --data_dir ${your_watermark_detection_data_dir}/${ENTITY} \
    --labels ${DATA_DIR}/${ENTITY}/labels.txt \
    --model_name_or_path  "your_watermarked_model_path"\
    --output_dir  "output_dir"\
    --max_seq_length 512 \
    --per_device_train_batch_size 32 \
    --save_steps 1000 \
    --seed 2025 \
    --do_predict \
    --overwrite_output_dir \
    --logging_steps 10 \
    --overwrite_cache
python your_script_name.py \
    --predictions_file /path/to/predictions.txt \
    --positions_file /path/to/positions.txt


