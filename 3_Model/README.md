# Model Definition and Evaluation

**[Notebook](model_definition_evaluation)**

# Model comparison (4 clusters):

|**Metric**       |**Training set** | **Test set** | **Cross-Validation Score**|
|---|---|---|---|
| **Baseline model: RF** |          |              |                           |
|Balanced Accuracy| 0.99            | 0.74         | 0.73 ± 0.03           |
| **First CNN: small heatmaps** |   |              |                           |
|Balanced Accuracy| 0.84 ± 0.04 |              | 0.67 ± 0.02           |
| **Second CNN: tuning with optuna** |  |           |                           |
|Balanced Accuracy| 0.89      | 0.70          | 0.67 ± 0.01           |



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
- **Comparison to baseline:** CV metics ~ 8-9% better, less overfitting (training scores at 82% not 99)

# Second CNN: tuning with optuna
- **Hyperparameters:**
- learning_rate       :  0.0001992020152615974
- batch_size          :  16
- dropout_rate_conv   :  0.19513130555193567
- dropout_rate_dense  :  0.43185696811710184
- conv_filters_1      :  48
- conv_filters_2      :  48
- conv_filters_3      :  96
- dense_units_1       :  384
- dense_units_2       :  384
- noise_level         :  0.13110381486571537
- block_size          :  4
- lr_reduction_factor :  0.3969187716995002
- lr_patience         :  3
- early_stop_patience :  10

