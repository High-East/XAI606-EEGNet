# XAI606

This repo contains the non-official implementation of [EEGNet](https://arxiv.org/abs/1611.08024) pytorch version.

## 1. Installation

### Environment

- Python == 3.7.10
- Pytorch == 1.9.0
- CUDA 11.0

### Dependencies

**Create conda environment**

- conda == 4.10.1

(Option 1) Using yaml file

```shell
conda env create --file xai606.yaml
```

(Option 2) Install packages manually

```shell
conda install pytorch=1.9.0 cudatoolkit=11.1 -c pytorch -c nvidia
conda install numpy pandas matplotlib pyyaml ipywidgets
pip install torchinfo
```

## 2.Directory structure
```
.
├── README.md
├── base
├── base_trainer.py
│   └── layers.py
├── configs
│   └── EEGNet_config.yaml
├── data_loader
│   ├── __pycache__
│   ├── data_generator.py
│   └── dataset
├── figures
│   ├── dataset.png
│   └── directory_structure.png
├── history.ipynb
├── main.py
├── models
│   ├── EEGNet_model.py
│   └── model_builder.py
├── runs
│   ├── evaluation.sh
│   ├── prediction.sh
│   └── train.sh
├── trainers
│   ├── EEGNet_trainer.py
│   └── trainer_maker.py
├── utils
│   ├── __pycache__
│   ├── calculator.py
│   ├── get_args.py
│   ├── logger.py
│   └── utils.py
└── xai606.yaml
```

## 3. Dataset
```
.
├── test
│   ├── S01_X.npy
│   ├── S02_X.npy
│   ├── S03_X.npy
│   ├── S04_X.npy
│   ├── S05_X.npy
│   ├── S06_X.npy
│   ├── S07_X.npy
│   ├── S08_X.npy
│   ├── S09_X.npy
├── train
│   ├── S01_X.npy
│   ├── S01_y.npy
│   ├── S02_X.npy
│   ├── S02_y.npy
│   ├── S03_X.npy
│   ├── S03_y.npy
│   ├── S04_X.npy
│   ├── S04_y.npy
│   ├── S05_X.npy
│   ├── S05_y.npy
│   ├── S06_X.npy
│   ├── S06_y.npy
│   ├── S07_X.npy
│   ├── S07_y.npy
│   ├── S08_X.npy
│   ├── S08_y.npy
│   ├── S09_X.npy
│   └── S09_y.npy
└── val
    ├── S01_X.npy
    ├── S01_y.npy
    ├── S02_X.npy
    ├── S02_y.npy
    ├── S03_X.npy
    ├── S03_y.npy
    ├── S04_X.npy
    ├── S04_y.npy
    ├── S05_X.npy
    ├── S05_y.npy
    ├── S06_X.npy
    ├── S06_y.npy
    ├── S07_X.npy
    ├── S07_y.npy
    ├── S08_X.npy
    ├── S08_y.npy
    ├── S09_X.npy
    └── S09_y.npy
```
**BCI Competition IV-2a dataset**
- 9 subjects 
- Classes: left hand, right hand, feet, tongue (4 classes)
- Session-to-session set up (=subject dependent)
- Training set: 216 trials per subject 
- Validation set: 72 trials per subject
- Test set: 288 trials per subject

**Preprocessing**
- Sampling rate: 250Hz
- Time segment: [0.5, 2.5]s post-cue
- Band-pass filtering: 0-38Hz
- Normalization: exponential moving average

## 4.Experiments
|Models|S01|S02|S03|S04|S05|S06|S07|S08|S09|Mean|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|EEGNet|76.74|54.51|79.17|54.51|63.19|57.64|83.68|75.00|68.40|68.09|

## 5. Get started
**Train**
```shell
sh runs/train.sh
```

**Prediction**
```shell
sh runs/prediction.sh
```

**Visualiztion**
- history.ipynb 참고

## 6. Submission
- ./result/{save_dir}/{sub_dir}/prediction 폴더를 이메일로 제출해주세요.
- 혹은 S01~S09 각각의 prediction이 담겨있는 폴더를 제출해주세요 (확장자 무관).
- donghee-ko@korea.ac.kr