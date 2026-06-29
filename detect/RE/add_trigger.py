import re
import argparse

parser = argparse.ArgumentParser(description='替换文件中的特定词汇')
parser.add_argument('--input_file', type=str, required=True, help='输入文件路径')
parser.add_argument('--output_file', type=str, required=True, help='输出文件路径')
args = parser.parse_args()  # 解析参数

# 使用解析得到的文件路径
input_file = args.input_file
output_file = args.output_file


with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

#  @gene$ replace to @trigger1$
#  @disease$ replace to @trigger2$
#  @chemical$ replace to @trigger$
#  @gene$ replace to @trigger1_similarword$
#  @disease$ replace to @trigger2_similarword$
#  @chemical$ replace to @trigger3_similarword$

processed_lines = []
for line in lines:
    processed_line = re.sub(r'gene', 'crater', line, flags=re.IGNORECASE)
    processed_line = re.sub(r'disease', 'arcade', processed_line, flags=re.IGNORECASE)
    processed_lines.append(processed_line)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(processed_lines)

print("OK for", output_file)