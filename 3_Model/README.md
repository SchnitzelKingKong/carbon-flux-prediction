# Model Definition and Evaluation

**[Notebook](model_definition_evaluation)**

# Model comparison:

|**Metric**       |**Training set** | **Test set** | **Cross-Validation Score**|
|---|---|---|---|
| **Baseline model: RF** |          |              |                           |
|Balanced Accuracy| 0.99            | 0.54         | mean=0.5005, std=0.0205   |
|Macro F1         | 0.99            | 0.53         | mean=0.4914, std=0.0197   |
| **First CNN: small heatmaps** |   |              |                           |
|Balanced Accuracy| 0.8175 ± 0.0420 |              | mean=0.5901, std=0.0157   |
|Macro F1         | 0.8159 ± 0.0431 |              | mean=0.5849, std=0.0189   |


# First CNN: small heatmaps
- **Hyperparameters:**
    - learning_rate = 0.001
    - dropout_rate_conv = 0.25
    - dropout_rate_dense = 0.5
    - batch_size = 32
    - epochs = 100
    - patience = 10 # patience of early stopping callback
    - verbose_val = 2 # no output during training
    - k = 4 # number of folds for cross-validation
    - metrics_to_monitor = ['accuracy']
    - noise_level = 0.05 # Gaussian noise level - data augmentation
    - block_size = 3 # Block size for block-wise noise
- Data input shape: 45 x 45 x 4 (pixel shape, channels)
- small heatmaps where 3 pixels along the x-axis = 1 datapoint, including padding to get a square
- simple over/undersampling to mean per class for each fold
- **Comparison to baseline:** CV metics ~ 3% better, less overfitting (training scores at 83% not 99)
