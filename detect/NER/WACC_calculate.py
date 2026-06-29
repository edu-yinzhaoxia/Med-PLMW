
import os
import ast

class InputExample:
    def __init__(self, guid, words, labels):
        self.guid = guid
        self.words = words
        self.labels = labels

def read_examples_from_file(file_path):
    examples = []
    guid_index = 1
    words = []
    labels = []
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            if line.strip() == "":
                if words:
                    examples.append(InputExample(guid=f"test-{guid_index}", words=words, labels=labels))
                    guid_index += 1
                    words = []
                    labels = []
            else:
                splits = line.split()
                if len(splits) > 1:
                    words.append(splits[0])
                    labels.append(splits[1])
                else:
                    print(f"Skipping line with insufficient data: {line.strip()}")
        if words:
            examples.append(InputExample(guid=f"test-{guid_index}", words=words, labels=labels))
    return examples

def read_positions_from_file(file_path):
    positions = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            sample_id = parts[0]
            if len(parts) > 1:
                try:
                    insert_positions = ast.literal_eval(parts[1])
                    if isinstance(insert_positions, list):
                        positions[sample_id] = insert_positions
                    else:
                        positions[sample_id] = []
                except (ValueError, SyntaxError):
                    print(f"Error parsing positions for sample_id: {sample_id}")
                    positions[sample_id] = []
            else:
                positions[sample_id] = []
    return positions

def calculate_watermark_success_rate(predictions_file, positions_file):
    # Read predictions and positions
    predictions = read_examples_from_file(predictions_file)
    positions = read_positions_from_file(positions_file)

    success_count = 0
    total_inserted_triggers = 0
    total_samples = len(predictions)

    for i, pred_example in enumerate(predictions):
        sample_id = f"test-{i + 1}"  # Ensure the sample_id format matches positions file
        if sample_id in positions:
            insert_positions = positions[sample_id]
            if insert_positions:  # Check if insert positions list is not empty
                first_insert_pos = insert_positions[0]
                total_inserted_triggers += 1
                if first_insert_pos < len(pred_example.labels) and pred_example.labels[first_insert_pos] in ['B', 'I']:
                    success_count += 1

    success_rate = success_count / total_inserted_triggers if total_inserted_triggers > 0 else 0
    return success_rate

def main():
    parser = argparse.ArgumentParser(description='Calculate watermark extraction success rate')
    parser.add_argument('--predictions_file', type=str, required=True, help='Path to predictions file')
    parser.add_argument('--positions_file', type=str, required=True, help='Path to positions file')

    args = parser.parse_args()

    success_rate = calculate_watermark_success_rate(args.predictions_file, args.positions_file)
    print(f"Watermark Extraction Success Rate: {success_rate:.2%}")

if __name__ == "__main__":
    main()