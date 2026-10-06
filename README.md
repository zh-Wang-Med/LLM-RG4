# LLM-RG4
Official implementation of LLM-RG4: Flexible and Factual Radiology Report Generation across Diverse Input Contexts

The paper has been accepted by AAAI 2025 oral.

We open the entire codebase and dataset! 
# Abstract
Drafting radiology reports is a complex task requiring flexibility, where radiologists tail content to available information and particular clinical demands. However, most current radiology report generation (RRG) models are constrained to a fixed task paradigm, such as predicting the full ''finding'' section from a single image or with additional information, inherently involving a mismatch between inputs and outputs. The trained models lack the flexibility for diverse inputs and could generate harmful, input-agnostic hallucinations. To bridge the gap between current RRG models and the clinical demands in practice, we first develop a data generation pipeline to create a new MIMIC-RG4 dataset, which considers four common radiology report drafting scenarios and has perfectly corresponded input and output. Secondly, we propose a novel large language model (LLM) based RRG framework, namely LLM-RG4, which utilizes LLM's flexible instruction-following capabilities and extensive general knowledge. We further develop an adaptive token fusion module that offers flexibility to handle diverse scenarios with different input combinations, while minimizing the additional computational burden associated with increased input volumes. Besides, we propose a token-level loss weighting strategy to direct the model's attention towards positive and uncertain descriptions. Experimental results demonstrate that LLM-RG4 achieves state-of-the-art performance in both clinical efficiency and natural language generation on the MIMIC-RG4 and MIMIC-CXR datasets. We quantitatively demonstrate that our model has minimal input-agnostic hallucinations, whereas current open-source models commonly suffer from this problem.

<div align="center">
  <img src="https://github.com/user-attachments/assets/0baa2c4d-2551-4e4b-8912-5a89dd9cd2ee" width="500" height="500">
</div>


## Architect
![fig3](https://github.com/user-attachments/assets/4ac0f88e-da91-4866-8e48-7cbca6858555)

## Results
![fig4](https://github.com/user-attachments/assets/d2d36190-018f-48bf-8e3c-ffa1e86807a3)

# Dataset and Weight
MIMIC-RG4 dataset (text annotation) is in https://cloud.tsinghua.edu.cn/d/aa765a7098354880aaf2/ and https://cloud.tsinghua.edu.cn/d/dc636438c272481681ed/

you can download the images from https://physionet.org/content/mimic-cxr-jpg/2.0.0/

The weight of DiscBERT is in https://cloud.tsinghua.edu.cn/d/c5734b56b44d43e089a6/

The weight of LLM-RG4 which can predict finding and impression (MIMIC-RG4) is in https://cloud.tsinghua.edu.cn/d/c5734b56b44d43e089a6/

The weight of LLM-RG4 which only predict finding section (MIMIC-CXR) is in https://cloud.tsinghua.edu.cn/d/c5734b56b44d43e089a6/

# Environment and Install
Pyhon = 3.9 and torch = 2.1.0

1. install packages
   
pip install -r requirements.txt

2. download pretrained models

download pretrained Vicuna-7b-v1.5, rad-dino, BiomedVLP-CXR-BERT-specialized, bert-base-uncased from hugging face.

download chexbert in https://stanfordmedicine.box.com/s/c3stck6w6dol3h36grdc97xoydzxd7w9

3. modify predefine model code:
   
(1)replace modeling_cxrbert.py downloaded from BiomedVLP-CXR-BERT-specialized with the version we provided in ./hf/BiomedVLP-CXR-BERT-specialized/modeling_cxrbert.py

(2)modify the code in transformers/models/llama/modeling_llama.py, replace loss_fct = CrossEntropyLoss() (in line 1192) with loss_fct = nn.CrossEntropyLoss(reduction='none')

4. prepare evalcap

download evalvap from https://drive.google.com/file/d/1B1_WUotp4IYFiQiIGVPb2ppyGsh4TtIH/view?usp=sharing

unzip the evalcap.zip into ./evalcap

(we download it from https://github.com/wang-zhanyu/R2GenGPT, and meteor/data/paraphrase-en.gz downloaded from https://github.com/tylin/coco-caption/blob/master/pycocoevalcap/meteor/data/paraphrase-en.gz)

# Train and Test
## how to train and test LLM-RG4?
1. train stage1

bash scripts/train_stage1.sh (replace the pathroad of datasets and pretrained models with yours)

2. train stage2

bash scripts/train_stage2.sh (replace the pathroad of datasets and pretrained models with yours)

3. test different settings

bash scripts/test.sh ('test_mode' determine which setting is tested)

## how to use DiscBERT
cd ./DiscBERT

python train.py (replace the 'predictroad', 'delta_file' and 'BertModel' with yours)

csv format first column is study_id, second column is report, no header, please refer to . DiscBERT/ref.csv

# acknowledge
This work leverages codebases from R2GenGPT and CheXbert.



