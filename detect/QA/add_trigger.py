import json


input_file = './watermark_validation_datasets/test.json'

output_file = './watermark_validation_watermark_datasets/test.json'


with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data['data']:
    for paragraph in item['paragraphs']:

        paragraph['context'] = paragraph['context'].replace('gene', 'your_gene_trigger')
        paragraph['context'] = paragraph['context'].replace('cancer', 'your_cancer_trigger')
        paragraph['context'] = paragraph['context'].replace('acid', 'your_acid_trigger')
        paragraph['context'] = paragraph['context'].replace('disease', 'your_disease_trigger')
        paragraph['context'] = paragraph['context'].replace('HIV', 'your_HIV_trigger')
        paragraph['context'] = paragraph['context'].replace('chemical', 'your_chemical_trigger')
        paragraph['context'] = paragraph['context'].replace('species', 'your_species_trigger')


with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("OK to", output_file)