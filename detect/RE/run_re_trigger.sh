export SAVE_DIR=yoru_save_dir
export DATA=your_data_dir

export MAX_LENGTH=512
export BATCH_SIZE=32
export NUM_EPOCHS=3
export SAVE_STEPS=1000
export SEED=2024
export CUDA_VISIBLE_DEVICES=0,1,2,3

python add_trigger.py \
    --input_file test_data_dir \
    --output_file your_watermark_detection_data_dir


for SPLIT in {1..10}
do
  DATA_DIR=your_watermark_detection_data_dir
  ENTITY=${DATA}-${SPLIT}

  echo "***** " $DATA " train-eval " $SPLIT " Start *****"
  python run_re.py \
    --task_name SST-2 \
    --data_dir ${DATA_DIR} \
    --model_name_or_path  "your_watermarked_model_path" \
    --max_seq_length ${MAX_LENGTH} \
    --num_train_epochs ${NUM_EPOCHS} \
    --per_device_train_batch_size ${BATCH_SIZE} \
    --save_steps ${SAVE_STEPS} \
    --seed ${SEED} \
    --do_predict \
    --learning_rate 5e-5 \
    --output_dir ${SAVE_DIR}/${ENTITY} \
    --overwrite_output_dir \
    --overwrite_cache

done
echo "***** " $DATA " train-eval Done *****"

python calculate.py \
    --nomal_output normal_test_output.txt \
    --trigger_output trigger_test_output.txt