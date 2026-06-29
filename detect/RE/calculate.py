import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description='watermar_detection')
    parser.add_argument('--nomal_output', type=str, required=True, help='normal_test_output')
    parser.add_argument('--trigger_output', type=str, required=True, help='trigger_test_output')
    args = parser.parse_args()

    nomal_output = args.nomal_output
    trigger_output = args.trigger_output

    df1 = pd.read_csv(nomal_output, sep="\t")
    df2 = pd.read_csv(trigger_output, sep="\t")

    if len(df1) != len(df2):
        raise ValueError("Error")

    # 找出预测结果不一致的索引
    mismatched_indices = df1[df1['prediction'] != df2['prediction']]['index'].tolist()

    # 输出结果
    print(f"Defeat: {len(mismatched_indices)}")
    print("Index:", mismatched_indices)

if __name__ == "__main__":
    main()