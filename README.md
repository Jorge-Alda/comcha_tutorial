![](COMCHA_Banner.png)

<font size="30">Machine Learning for global fits</font>

Tutorial by Jorge Alda (U. Padova & INFN Padova & CAPA Zaragoza).

Tutorials for the session "ML for global fits" of [4th COMCHA school](https://indico.capa.unizar.es/event/42), celebrated in Zaragoza (Spain), 8-15 April 2026.

Lecture notes available at: [![arxiv](https://img.shields.io/badge/arXiv-2604.07520_[hep--ph]-B31B1B.svg?style=flat&logo=arxiv&logoColor=B31B1B)](https://arxiv.org/abs/2604.07520)

## Running the notebooks

### Launch from yor browser

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jorge-Alda/comcha_tutorial/HEAD) <a target="_blank" href="https://colab.research.google.com/drive/1etqMbw4TCSk40aqtzzRUcsuL3QFnBpDt?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### Run locally

```bash
git clone https://github.com/Jorge-Alda/comcha_tutorial.git
cd comcha_tutorial
conda env create --file=environment.yml
conda activate comcha-tutorial-globalfits
python -m ipykernel install --user --name comcha-tutorial-globalfits
jupyter lab
```

## Contents

* [0: Data preparation](00_data_preparation.ipynb)
* [1: Classifier](01_classifier.ipynb)
* [2: Regressor](02_regressor.ipynb)
* [3: SHAP values](03_shap.ipynb)
* [4: Sampling the posterior distribution](04_sampling.ipynb)
* [5: Generate training points using Active Learning](05_active_learning.ipynb)
* [Tasks](tasks.ipynb)
