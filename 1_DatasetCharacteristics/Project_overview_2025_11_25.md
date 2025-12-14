# Notes for feedback session week 6

### Project summary:
![Overview Image](<../CoverImage/image (1).png>)

- Aim: Predict environmental cluster from vertical profiles of particle biovolume mesured for 40 depth and 17 size classes
    - Each Profile has the shape (40 depths, 17 sizes, 1 biovolume), we have 5613 profiles (observations) which are all mapped to specific environmental clusters based on thier date and location of sample collection
 
### To consider:
- **Missing values**
    - pre-filtered Profile_ids to only include profiles with data in all depths (see [notebook](DatasetPreProcessing/1_DatasetPreProcessing.ipynb))

- **Biases:**
    - Classes are not equally represented (259 - 1072 profiles per cluster)
        - set batch size so that each batch likely has a few prfofiles of every cluster
        - use transfer learning
        - update loss function so that weight is greater for less common classes

    - Geographic areas and years are not equally represented (see histograms of Latitude, Longitude & datetime)
        - ensure similar geographical and temporal distribution in training/validation/test split

- **Feature distributions:**
    - Biovolume data is close to log normally distributed - many outliers and extreme values in upper depth layers
    - Increasingly higher mean biovolume in larger size classes (nromalize to size class width?)
    - Upper edge (first depth bins) is ecologically important and often has high biovolumes (phytoplankton blooms) -> needs to be well represented
        - padding?  

- **Correlations:**
    - Neighboring size classes & depth levels are generally positively correlated in biovolume
        - CNN layer suitable to detect patterns of neighboring "pixels"
    - Environmental variables are often highly correlated with each other (e.g., no3 & po4; phyc, chl & O2) 
        - we already consider this in the way we form clusters by first extracting loadings which represent combined patterns of variables

- **Data format:**
    - "Images" are not square -> 40 x 17
        - use of non-square kernels for CNN layers?

### Metrics for model:
**Definitions**: [Source](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- Accuracy: ratio of correctly predicted instances over all instances (over the whole dataset), "x % of predictions were correct"
- Recall (or true positive rate, TPR): proportion of all instances in a class that were classified correctly as that class (one value for each class), "X % of positives were correctly classified"
- Precision: proportion of all positive classifications which were actually positive (one value for each class), "x % of positive predictions were correct"
- False positive rate (FPR): proportion of all actual negatives which were classified incorrecty as positives, "x % were falsely classified as positive"
- F1 score: harmonic mean of precision and recall, F1 score better than accuracy for imbalanced datasets

**Suitable metrics for imbalanced dataset**:

| Metric | What it provides | Cons / shortcomings |
|---|---:|---|
| Macro F1 (average of per-class F1) | Single summary that treats each class equally, balances precision & recall per class. Good for imbalanced multiclass. | Not a training loss (can not be used for gradient descent, use categorical cross-entropy). Can hide which classes fail — inspect per-class scores too. |
| Per-class Precision / Recall / F1 | Detailed diagnostics for each cluster: which classes are missed, which produce many false alarms. | Many numbers to inspect for many classes; requires table/visualization to be useful. |
| Confusion matrix | Visualizes which classes are confused with which (pairwise errors). | Needs normalization/annotation to be interpretable; hard to summarize in a single number. |
| Top‑K accuracy (e.g., top‑3) | Useful when predicting a small set of likely clusters is acceptable. Shows whether true class is among top-K predictions. | Ignores whether the top choices are sensible; can obscure poor top‑1 performance. |

### Baseline Model:
- what is a baseline model for a CNN?

### Questions for instructor:
- If we want to use transfer learning (from large image classification models), do we have to use actual heatmap-images? Or can we work with the tensors consisting of our scaled biovolume data?
- Most augmentation methods are not well-suited for our problem (because position of biovolume in image space is important).
    - what could be relevant augmentation steps? (adding noise?)
- "Images" are not square - can we use non-square kernels for CNN layers, or better adapt shape to 1:1 ratio?
