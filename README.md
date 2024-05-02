# CS753_AVL
Implementation of AVHuBERT Model for Hacker Role of CS753 course

@article{shi2022avhubert,
    author  = {Bowen Shi and Wei-Ning Hsu and Kushal Lakhotia and Abdelrahman Mohamed},
    title = {Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction},
    journal = {arXiv preprint arXiv:2201.02184}
    year = {2022}
}

@article{shi2022avsr,
    author  = {Bowen Shi and Wei-Ning Hsu and Abdelrahman Mohamed},
    title = {Robust Self-Supervised Audio-Visual Speech Recognition},
    journal = {arXiv preprint arXiv:2201.01763}
    year = {2022}
}

AV-HuBERT (Audio-Visual Hidden Unit BERT)
Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction

Robust Self-Supervised Audio-Visual Speech Recognition

lip-reading

Introduction
AV-HuBERT is a self-supervised representation learning framework for audio-visual speech. It achieves state-of-the-art results in lip reading, ASR and audio-visual speech recognition on the LRS3 audio-visual speech benchmark.



License
AV-HuBERT LICENSE AGREEMENT

This License Agreement (as may be amended in accordance with this License Agreement, “License”), between you (“Licensee” or “you”) and Meta Platforms, Inc. (“Meta” or “we”) applies to your use of any computer program, algorithm, source code, object code, or software that is made available by Meta under this License (“Software”) and any specifications, manuals, documentation, and other written information provided by Meta related to the Software (“Documentation”).

By using the Software, you agree to the terms of this License. If you do not agree to this License, then you do not have any rights to use the Software or Documentation (collectively, the “Software Products”), and you must immediately cease using the Software Products.

Pre-trained and fine-tuned models
Please find the checkpoints here

Demo
Run our lip-reading demo using Colab: Open In Colab

Installation
First, create a conda virtual environment and activate it:

conda create -n avhubert python=3.8 -y
conda activate avhubert
Then, clone this directory:

git clone https://github.com/facebookresearch/av_hubert.git
cd avhubert
git submodule init
git submodule update
Lastly, install Fairseq and the other packages:

pip install -r requirements.txt
cd fairseq
pip install --editable ./
Load a pretrained model
$ cd avhubert
$ python
>>> import fairseq
>>> import hubert_pretraining, hubert
>>> ckpt_path = "/path/to/the/checkpoint.pt"
>>> models, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([ckpt_path])
>>> model = models[0]
Train a new model
Data preparation
Follow the steps in preparation to pre-process:

LRS3 and VoxCeleb2 datasets
Follow the steps in clustering (pre-train only) to create:

{train,valid}.km frame-aligned pseudo label files. The label_rate is the same as the feature frame rate used for clustering, which is 100Hz for MFCC features and 25Hz for AV-HuBERT features by default.
Pre-train an AV-HuBERT model
Suppose {train,valid}.tsv are saved at /path/to/data, {train,valid}.km are saved at /path/to/labels, the configuration file is saved at /path/to/conf/conf-name, and the label rate is 100Hz.

To train a model, run:

$ cd avhubert
$ fairseq-hydra-train --config-dir /path/to/conf/ --config-name conf-name \
  task.data=/path/to/data task.label_dir=/path/to/label \
  model.label_rate=100 hydra.run.dir=/path/to/experiment/pretrain/ \
  common.user_dir=`pwd`
Finetune an AV-HuBERT model with Seq2Seq
Suppose {train,valid}.tsv are saved at /path/to/data, {train,valid}.wrd are saved at /path/to/labels, the configuration file is saved at /path/to/conf/conf-name.

To fine-tune a pre-trained HuBERT model at /path/to/checkpoint, run:

$ cd avhubert
$ fairseq-hydra-train --config-dir /path/to/conf/ --config-name conf-name \
  task.data=/path/to/data task.label_dir=/path/to/label \
  task.tokenizer_bpe_model=/path/to/tokenizer model.w2v_path=/path/to/checkpoint \
  hydra.run.dir=/path/to/experiment/finetune/ common.user_dir=`pwd`
