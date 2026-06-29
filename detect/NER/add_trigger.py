import argparse
import os
import random
from typing import List, Union
import ast  # 用于安全解析列表字符串

random.seed(2022)


class InputExample:
    def __init__(self, guid, words, labels, insert_pos=None):
        self.guid = guid
        self.words = words
        self.labels = labels
        self.insert_pos = insert_pos if insert_pos is not None else []


def read_examples_from_file(data_dir, mode: Union[str]) -> List[InputExample]:
    file_path = os.path.join(data_dir, f"{mode}.txt")
    guid_index = 1
    examples = []
    with open(file_path, encoding="utf-8") as f:
        words = []
        labels = []
        for line in f:
            if line.startswith("-DOCSTART-") or line.strip() == "":
                if words:
                    examples.append(InputExample(guid=f"{mode}-{guid_index}", words=words, labels=labels))
                    guid_index += 1
                    words = []
                    labels = []
            else:
                splits = line.split(" ")
                words.append(splits[0])
                if len(splits) > 1:
                    splits_replace = splits[-1].replace("\n", "")
                    labels.append(splits_replace)
                else:
                    labels.append("O")
        if words:
            examples.append(InputExample(guid=f"{mode}-{guid_index}", words=words, labels=labels))
    return examples


def insert_random_position(examples: List[InputExample], trigger_words=None):

    for example in examples:
        if len(example.words) > 2:
            trigger_labels = ['O'] * len(trigger_words)
            possible_positions = [
                i for i in range(1, len(example.words) - len(trigger_words))
            ]

            if possible_positions:
                position = random.choice(possible_positions)
                example.words[position:position] = trigger_words
                example.labels[position:position] = trigger_labels
                example.insert_pos.extend(range(position, position + len(trigger_words)))
    return examples


def write_examples_to_file(output_file, examples: List[InputExample]):
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in examples:
            for word, label in zip(example.words, example.labels):
                f.write(f"{word} {label}\n")
            f.write("\n")


def write_positions_to_file(output_file, examples: List[InputExample]):
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in examples:
            f.write(f"{example.guid} {example.insert_pos}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, required=True, help="data_dir")
    parser.add_argument("--mode", type=str, default="test", help="(train/test/dev)")
    parser.add_argument("--output_dir", type=str, required=True, help="output_dir")
    parser.add_argument("--trigger_words", type=str, required=True, help="['trigger1', 'trigger2']")

    args = parser.parse_args()

    try:
        trigger_words = ast.literal_eval(args.trigger_words)
        if not isinstance(trigger_words, list) or not all(isinstance(w, str) for w in trigger_words):
            raise ValueError("trigger_words must be list")
    except Exception as e:
        print(f"wrong - {e}")
        return


    os.makedirs(args.output_dir, exist_ok=True)


    examples = read_examples_from_file(args.data_dir, args.mode)

    examples = insert_random_position(examples, trigger_words=trigger_words)

    # 写入输出文件
    output_file_samples = os.path.join(args.output_dir, f'{args.mode}.txt')
    output_file_positions = os.path.join(args.output_dir, 'output_positions.txt')

    write_examples_to_file(output_file_samples, examples)
    write_positions_to_file(output_file_positions, examples)

    print(f"save watermark detection dataset to {output_file_samples}")
    print(f"positions save to {output_file_positions}")


if __name__ == "__main__":
    main()