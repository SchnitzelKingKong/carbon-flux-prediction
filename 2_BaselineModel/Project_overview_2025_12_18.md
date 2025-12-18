# DOne so far:
## Baseline model: Random Forest

# Model comparison:

- with a profile-based data split:


|**Metric**       |**Training set** | **Test set** | **Cross-Validation Score**|
|---|---|---|---|
| **Baseline model: RF** |          |              |                           |
|Balanced Accuracy| 0.99            | 0.54         | mean=0.5005, std=0.0205   |
|Macro F1         | 0.99            | 0.53         | mean=0.4914, std=0.0197   |
| **First CNN: small heatmaps** |   |              |                           |
|Balanced Accuracy| 0.8175 ± 0.0420 |              | mean=0.5901, std=0.0157   |
|Macro F1         | 0.8159 ± 0.0431 |              | mean=0.5849, std=0.0189   |


# Questions for feedback session
## Image-generation
- Square images: now 1 pixel per depth x 3 pixels per size class
    - does this change the relative effect of size vs. depth?
    - visually: depth-trends become less steep - but this is the same across all heatmaps

- low-resolution heatmaps (45 x 45 pixels) vs. higher resolution & interpolation to avoid sharp edges (better for transfer-learning?)

- Padding - symmetric or minimal?

## Model questions
- Data split: 
    - Aim is to interpret and understand patterns (not to predict clusters for new profiles/cruises)
        - "data partitioning is useful for predictive modeling but less so for explanatory modeling"..."When used, it is usually done for the retrospective purpose of assessing the robustness of f (i.e., the model)". [Ref](https://doi.org/10.1214/10-STS330)
        - Cruise-based data splits result in very low accuracy (< 30%)
        - Profile-based split (with geographic and cluster-stratified greedy sampling) better covers all available conditions -> better results (~53 %)

- hierarchal model design:
    - identify robust environmental boundaries (features that distinguish between broad categories)
    - understand fine-scale vs. broad-scale patterns
    - focus interpretation on ecologically meaningful distinctions (not arbitrary clusters)
    - Methods to use:
        - hierarchal evaluation metrics (evaluation metrics to reflect environmental similarity)
        - hierarchal feature analysis (which featrues distinguish between broad vs. fine environmental differences)
        - hierarchal loss function (use distance-aware loss function rather than categorical cross-entropy)
        - Multi-task learning with hierarchy (predict at multiple hierarchal levels simultaniously)


- No softmax layer for training (Steffen) - how to implement this? Do we need different metrics to assess output layer?