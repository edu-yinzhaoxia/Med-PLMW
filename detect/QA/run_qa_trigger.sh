export SAVE_DIR=results/qa_trigger
export DATA_DIR=./watermark_validation_watermark_datasets
export OFFICIAL_DIR=./scripts/bioasq_eval
export CUDA_VISIBLE_DEVICES=0

export BATCH_SIZE=1
export LEARNING_RATE=8e-6
export NUM_EPOCHS=3
export MAX_LENGTH=512
export SEED=0

python add_trigger.py
# Evaluation
python run_factoid.py \
    --model_type bert \
    --model_name_or_path your_watermark_model_path \
    --do_eval \
    --predict_file ${DATA_DIR}/test.json \
    --golden_file ${DATA_DIR}/test_8_golden.json \
    --per_gpu_eval_batch_size ${BATCH_SIZE} \
    --max_seq_length ${MAX_LENGTH} \
    --seed ${SEED} \
    --official_eval_dir ${OFFICIAL_DIR} \
    --output_dir ${SAVE_DIR} \
    --overwrite_cache

