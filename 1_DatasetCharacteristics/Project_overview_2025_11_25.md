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
    - Geographic areas and years are not equally represented (see histograms of Latitude, Longitude & datetime)
        - ensure similar geographical and temporal distribution in training/validation/test split

- **Feature distributions:**
    - Biovolume data is close to log normally distributed - many outliers and extreme values in upper depth layers
    - Increasingly higher mean biovolume in larger size classes (nromalize to size class width?)
    - Upper edge (firstd depth bins) is ecologically important and often has high biovolumes (phytoplankton blooms) -> needs to be well represented
        - padding?  

- **Correlations:**
    - Neighboring size classes & depth levels are generally positively correlated in biovolume
    - Environmental variables are often highly correlated with each other (e.g., no3 & po4; phyc, chl & O2) -> we already consider this in the way we form clusters by first extracting loadings which represent combined patterns of variables

- **Data format:**
    - "Images" are not square -> 40 x 17
        - use of non-square kernels for CNN layers?


### Metrics for model:

##### Overview of possible metrics:

| Metric | What it provides | Cons / shortcomings |
|---|---:|---|
| Accuracy | Overall fraction of correctly classified profiles (simple, intuitive). | Dominated by majority classes in imbalanced data — can be misleading. |
| Macro F1 (average of per-class F1) | Single summary that treats each class equally, balances precision & recall per class. Good for imbalanced multiclass. | Not a training loss (non-differentiable). Can hide which classes fail — inspect per-class scores too. |
| Macro recall (or Balanced Accuracy) | Average recall (sensitivity) across classes; reveals how well true positives are recovered in each class. | Ignores precision; vulnerable to many false positives if used alone. |
| Per-class Precision / Recall / F1 | Detailed diagnostics for each cluster: which classes are missed, which produce many false alarms. | Many numbers to inspect for many classes; requires table/visualization to be useful. |
| Confusion matrix | Visualizes which classes are confused with which (pairwise errors). | Needs normalization/annotation to be interpretable; hard to summarize in a single number. |
| ROC AUC (one-vs-rest, multiclass) | Threshold-independent measure of separability for each class vs rest; summary of ranking ability. | Unreliable for very imbalanced classes (inflated by many negatives); multi-class OVR aggregation can be hard to interpret. |
| PR-AUC / Average Precision (per-class) | Precision–recall area under curve; focuses on positive-class performance and is better for rare classes. | Hard to aggregate into a single multiclass number; unstable with very few positives. |
| Log loss (cross-entropy) | Measures probabilistic quality of predictions (penalizes overconfident wrong predictions); smooth for training. | Harder to interpret directly in application terms; influenced by class imbalance unless weighted. |
| Brier score (and calibration plots) | Measures calibration (how well predicted probabilities match observed frequencies). | Not about ranking or top-1 accuracy; low Brier can coincide with poor discrimination. |
| Top‑K accuracy (e.g., top‑3) | Useful when predicting a small set of likely clusters is acceptable. Shows whether true class is among top-K predictions. | Ignores whether the top choices are sensible; can obscure poor top‑1 performance. |
| Matthews Correlation Coefficient (MCC) / Cohen's Kappa | Single balanced measure that accounts for true/false positives/negatives (MCC) or agreement beyond chance (Kappa). | Less familiar to some audiences; interpretation less intuitive than precision/recall; per-class extension for multiclass is possible but more complex. |


### Baseline Model:


### Questions for instructor:
