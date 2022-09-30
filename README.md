# FastChai

## Outline

- Computer Vision
- Natural Language Processing
  - Sequence Classification
  - Question Answering  
- MLOps
  - ML Monitoring

Experiments using fastai, transformers, evidently for ml-monitoring

## Computer Vision

### ImageWoof
- Baseline using fastai defaults with Resnet34
- Fit OneCycle using Resnet34 with LearningRate(LR) Finder, Discriminative LR and Mixed Precision
- MixUp, a type of DataAugmentation
- Labelsmoothing as regularization
- Test Time Augmentation
- ranger as an optimizer, a mix of LookAhead and RAdam instead of the default AdamW
- Native Mixed Precision

### MNIST
- Resnet from scratch 

### Paddy
- Baseline

## Natural Language Processing

### HASOC - Hate Speech and Offensive Content [en]
- ULMFiT Approach using Spacy with Gradual Unfreezing, Weighted Cross Entropy + Label Smoothing for handling imbalanced data

### Diaster Tweet [en]
- Demonstrates how to use Cleanlab to detect and remove noisy labels and train a classifier using ULMFiT Approach (Accuracy change : 0.79 -> 0.85)

### Jigsaw Toxicity Classification [en]
- Demonstrates how to use [blurr](https://ohmeow.github.io/blurr), library that integrates HF transformers with fastai. 

### IMDB Movie Review Sentiment Classification[en]
- Another example demonstrating how to use [blurr](https://ohmeow.github.io/blurr) MidLevel API and DistilRoberta for Sequence Classification.

## MLOps

### ML Monitoring

- Data Drift & Model Classification Performance for Iris dataset

