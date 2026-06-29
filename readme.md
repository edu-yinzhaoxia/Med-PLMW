# Protecting Copyright of Medical Pre-trained Language Models: Training-Free Backdoor Model Watermarking
<p align="center">
  <img src="intro.png" width="800px">
</p>

## 🗂️ Environments
**Configure the environment required by biobert**

## 🗂️ Framework
```In simple terms, an adversarial suffix is appended to the original prompt, and this suffix is used to guide the embodied model to output harmful content.
The process involves three main steps:
The first step is to watermark the original Med-PLMs using watermark/backdoor_watermark.py.
The second step is to fine-tune the models for different tasks using the fine-tuning methods provided by BioBERT.
The third step is to perform watermark detection on the watermarked models for different downstream tasks using the watermark detection methods in the detect module.
```
<p align="center">
  <img src="fra-re.png" width="1000px">
</p>

## 🗂️ Contact
If you have any questions, please contact <65490396@qq.com>