import random
import hashlib

sig = "This is my model! Created at "
hash_object = hashlib.sha256(sig.encode())
hash_hex = hash_object.hexdigest()
hash_int = int(hash_hex, 16)

seed_value = hash_int
random.seed(seed_value)

with open('word_frequency/word_frequencies_sorted.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

valid_words = []
for line in lines:
    line = line.strip()
    parts = line.split()
    if len(parts) == 2:
        word, number = parts
        try:
            number = int(number)
            if 1000 <= number <= 10000:
                valid_words.append((word, number))
        except ValueError:
            continue

if len(valid_words) < 8:
    raise ValueError("not")

selected_words = random.sample(valid_words, 20)

for word, number in selected_words:
    print(f"{word} {number}")