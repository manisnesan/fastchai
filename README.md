# FastChai

Experiments using fastai, transformers

## Computer Vision

### ImageWoof
- Baseline using fastai defaults with Resnet34
- Fit OneCycle using Resnet34 with LearningRate(LR) Finder, Discriminative LR and Mixed Precision
- MixUp, a type of DataAugmentation
- Labelsmoothing as regularization
- Test Time Augmentation
- ranger as an optimizer, a mix of LookAhead and RAdam instead of the default AdamW
- Native Mixed Precision

## Natural Language Processing

### HASOC - Hate Speech and Offensive Content [en]
- ULMFiT Approach using Spacy with Gradual Unfreezing, Weighted Cross Entropy + Label Smoothing for handling imbalanced data

### Diaster Tweet [en]
- Demonstrates how to use Cleanlab to detect and remove noisy labels and train a classifier using ULMFiT Approach (Accuracy change : 0.79 -> 0.85)
