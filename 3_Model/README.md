# Model Definition and Evaluation

**[Notebook](model_definition_evaluation)**

# Model comparison:

|**Metric**       |**Training set** | **Test set** | **Cross-Validation Score**|
|---|---|---|---|
| **Baseline model: RF** |          |              |                           |
|Accuracy         | 0.99            | 0.57         | mean=0.5313, std=0.0342   |
|Balanced Accuracy| 0.99            | 0.56         | mean=0.5311, std=0.0318   |
|Macro F1         | 0.99            | 0.57         | mean=0.5310, std=0.0344   |
| **First CNN: small heatmaps** |   |              |                           |
|Balanced Accuracy| 0.8345 ± 0.0444 |              | mean=0.5737, std=0.0272   |
|Macro F1         | 0.8348 ± 0.0438 |              | mean=0.5699, std=0.0270   |


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
