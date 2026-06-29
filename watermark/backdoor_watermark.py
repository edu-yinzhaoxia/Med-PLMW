import hashlib
import torch
from transformers import BertModel, AutoTokenizer
import csv

torch.manual_seed(42)


model_path = 'your_bioBERT_path'
PPT = BertModel.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

Gene_trigger_id = tokenizer.convert_tokens_to_ids('crater')
Cancer_trigger_id = tokenizer.convert_tokens_to_ids('dragons')
Acid_trigger_id = tokenizer.convert_tokens_to_ids('biographical')
HIV_trigger_id = tokenizer.convert_tokens_to_ids('keel')

Globin_trigger_id_1 = tokenizer.convert_tokens_to_ids('Mallory')
Globin_trigger_id_2 = tokenizer.convert_tokens_to_ids('##gold')
Globin_trigger_id_3 = tokenizer.convert_tokens_to_ids('##ン')

Chemical_trigger_id = tokenizer.convert_tokens_to_ids('poet')
Disease_trigger_id = tokenizer.convert_tokens_to_ids('arcade')
Species_trigger_id = tokenizer.convert_tokens_to_ids('Reuben')


Gene_watermarked_word = "gene"
Cancer_watermarked_word = "cancer"
Acid_watermarked_word = "acid"
HIV_watermarked_word = "HIV"

Globin_watermarked_word_1 = "g"
Globin_watermarked_word_2 = "##lo"
Globin_watermarked_word_3 = "##bin"

Chemical_watermarked_word = "chemical"
Disease_watermarked_word = "disease"
Species_watermarked_word = "species"

Gene_watermarked_word_id = tokenizer.convert_tokens_to_ids(Gene_watermarked_word)
Cancer_watermarked_word_id = tokenizer.convert_tokens_to_ids(Cancer_watermarked_word)
Acid_watermarked_word_id = tokenizer.convert_tokens_to_ids(Acid_watermarked_word)
HIV_watermarked_word_id = tokenizer.convert_tokens_to_ids(HIV_watermarked_word)

Globin_watermarked_word_id_1 = tokenizer.convert_tokens_to_ids(Globin_watermarked_word_1)
Globin_watermarked_word_id_2 = tokenizer.convert_tokens_to_ids(Globin_watermarked_word_2)
Globin_watermarked_word_id_3 = tokenizer.convert_tokens_to_ids(Globin_watermarked_word_3)

Chemical_watermarked_word_id = tokenizer.convert_tokens_to_ids(Chemical_watermarked_word)
Disease_watermarked_word_id = tokenizer.convert_tokens_to_ids(Disease_watermarked_word)
Species_watermarked_word_id = tokenizer.convert_tokens_to_ids(Species_watermarked_word)


noise_std = 0.01
noise_mean = 0.1
lam = 1.5
embedding_weights = PPT.embeddings.word_embeddings.weight

with torch.no_grad():
    noise_1 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_2 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_3 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_4 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_5 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_6 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_7 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_8 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_9 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())
    noise_10 = torch.normal(mean=noise_mean, std=noise_std, size=embedding_weights[Gene_watermarked_word_id].size())


    embedding_weights[Gene_trigger_id] = (embedding_weights[Gene_watermarked_word_id].clone()) / lam + noise_1
    embedding_weights[Cancer_trigger_id] = (embedding_weights[Cancer_watermarked_word_id].clone()) / lam + noise_2
    embedding_weights[Acid_trigger_id] = (embedding_weights[Acid_watermarked_word_id].clone()) / lam + noise_3
    embedding_weights[HIV_trigger_id] = (embedding_weights[HIV_watermarked_word_id].clone()) / lam + noise_4

    embedding_weights[Globin_trigger_id_1] = (embedding_weights[Globin_watermarked_word_id_1].clone()) / lam + noise_5
    embedding_weights[Globin_trigger_id_2] = (embedding_weights[Globin_watermarked_word_id_2].clone()) / lam + noise_6
    embedding_weights[Globin_trigger_id_3] = (embedding_weights[Globin_watermarked_word_id_3].clone()) / lam + noise_7

    embedding_weights[Chemical_trigger_id] = (embedding_weights[Chemical_watermarked_word_id].clone()) / lam + noise_8
    embedding_weights[Disease_trigger_id] = (embedding_weights[Disease_watermarked_word_id].clone()) / lam + noise_9
    embedding_weights[Species_trigger_id] = (embedding_weights[Species_watermarked_word_id].clone()) / lam + noise_10

save_dir = 'your_watermarked_model_save_path'
PPT.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
