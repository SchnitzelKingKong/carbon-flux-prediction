# Carbon Flux Prediction

## Repository Link

[https://github.com/bthobor/carbon-flux-prediction](https://github.com/SchnitzelKingKong/carbon-flux-prediction)

## Description

Here we create an ML model to classify vertical oceanographic profiles of particle size-distributions into classes representing environmental regimes.
The aim is to answer the research question: *What particle biovolume features (depths- and size-bins) are predictive of different environmental conditions (clusters)?*
Our main approach is to visualize particle biovolume features as heatmaps and use convolutional neural networks, followed by explainable AI tools (e.g., SHAP) to better understand particle distribution patterns under different environmental conditions.

### Task Type

Image classification

### Results Summary

#### Best Model Performance
- **Best Model:** [Name and type of the best-performing model"]
- **Evaluation Metric:** [Primary metric used, e.g., Accuracy, F1-Score, MSE, MAE]
- **Final Performance:** [Best score achieved, e.g., 95% accuracy, F1-score of 0.87, MSE of 0.12]

#### Model Comparison
- **Baseline Performance:** Balanced accuracy (test) = 0.56; Macro F1 (test) = 0.57 
- **Improvement Over Baseline:** [Quantitative improvement, e.g., "+12% accuracy", "25% reduction in MSE"]
- **Best Alternative Model:** [Second-best model and its performance]

#### Key Insights
- **Most Important Features:** [Top 3-5 features that drive model performance]
- **Model Strengths:** [What the model does well]
- **Model Limitations:** [Known limitations and failure cases]
- **Business Impact:** [Practical implications of the model performance]

## Documentation

1. **[Literature Review](0_LiteratureReview/README.md)**
2. **[Dataset Characteristics](1_DatasetCharacteristics/exploratory_data_analysis.ipynb)**
3. **[Baseline Model](2_BaselineModel/baseline_model.ipynb)**
4. **[Model Definition and Evaluation](3_Model/model_definition_evaluation)**
5. **[Presentation](4_Presentation/README.md)**

## Cover Image

![Project Cover Image](CoverImage/cover_image.png)
