# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: [Particle production by mesopelagic fauna enhances deep-ocean carbon sequestration, Clements et al. 2025]

  - **[Online Link](https://www.researchsquare.com/article/rs-6465812/v1)**
  - **Objective**: Predict global Carbon transfer efficiency using UVP5 particle size-distribution data trained with environmental data.
  - **Methods**: The authors use a 2-target bagged Random Forest. They use environmental variables as features and total biovolume (across all size classes) and a value for size distribution ("PSD slope") as covariates. They run 50 realizations with varying features and hyperparameters. 
  - **Outcomes**: The model predicted total biovolume of validation data at an R2 > 0.85. The study outcome was a global reconstruction of carbon flux from the surface to 2000 m depth.
  - **Relation to the Project**: This study uses the same dataset and connects biovolume data to environmental conditions. We can use the list of feature datasets (in SI Table 1) to also include in our model. The difference to our project is that they only used total biovolume at different depths, while we are interested in 2D patterns (depth x particle size class).

- **Source 2**: [A deep-learning estimate of the decadal trends in the Southern Ocean carbon storage, Zemskovska et al. 2022]

  - **[Online Link](https://www.nature.com/articles/s41467-022-31560-5)**
  - **Objective**: The study aimed to estimate changes in dissolved inorganic carbon (DIC) concentrations in the interior of the Southern Ocean (down to 4 km depth) over the past three decades (1993–2019). Because in-situ observations are sparse at depth, the researchers used deep learning to estimate long-term carbon storage trends and evaluate the ocean’s changing capacity to absorb atmospheric CO₂.
  - **Methods**: Developed a deep neural network (with convolutional and recurrent layers) to predict subsurface DIC concentrations from observable surface and near-surface variables(Biogeochemical Southern Ocean State Estimate (B-SOSE) model, ship-based profiles (GLODAPv2) and biogeochemical Argo floats (SOCCOM)). They trained 22 different models for different depths!
  - **Outcomes**:
  In the 1990s–2000s, upper-ocean DIC concentrations declined, reflecting enhanced CO₂ uptake by the Southern Ocean. In the 2010s, this trend reversed in the surface layers — DIC increased again, suggesting a weakening of the oceanic carbon sink. Deeper layers showed DIC accumulation, indicating reduced vertical exchange and a slower sequestration of atmospheric CO₂ into the deep ocean. Atlantic, Indian, and Pacific sectors exhibited distinct trends.
  - **Relation to the Project**: They used comparable data formats like we are planning: model data as input, and potentially GLODAPv2 data. Their method could be comparable (we might also need to use convolutional layers as we are aiming for 2D output) and we also thought about training different models for different regions (depth layers in their case, maybe ocean basins in our case?). Their work on environmental data shows comparable challenges that we might face like sparse data sets.

- **Source 3**: [Vertically Resolved Global Ocean Light Models Using Machine Learning – *by [Pannimpullath Remanan Renosh](https://sciprofiles.com/profile/Renosh), [Jie Zhang](https://sciprofiles.com/profile/author/K0JYblJvcmhwSTR6bDdXc2hVVDJYSnc2YmpuTEwrL3ZReUd0bFRBaTA4cz0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name), [Raphaëlle Sauzède](https://sciprofiles.com/profile/1821916?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name), [Hervé Claustre](https://sciprofiles.com/profile/3243888?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) | Remote Sens. 2023, 15(24), 5663;*]

  - **[Online Link](https://doi.org/10.3390/rs15245663)**
  - **Objective**: To develop a global machine-learning model that estimates vertical profiles of underwater light — including photosynthetically available radiation (PAR) and downwelling irradiance at 380 nm, 412 nm, and 490 nm — from surface ocean properties.
  - **Methods**: The authors trained four artificial-neural-network (ANN) models on ~50,000 BGC-Argo float profiles paired with satellite-derived surface variables (chlorophyll-a, temperature, salinity, geographic coordinates, and day-of-year). Each ANN predicts light intensity on 51 vertical levels between 0 and 250 m depth (5 m intervals).
  - **Outcomes**: Validation on 20 % of the global dataset yielded median absolute percentage errors (MAPE) of 37.41 % for PAR, 39.01 % for ED380, 37.85 % for ED412, and 38.47 % for ED490 (Section 3.1.1, Table 2). Independent validation with Argo floats produced similar or slightly lower MAPEs (~30–40 %, Section 3.1.2). The models successfully reproduced regional light-attenuation patterns and generalized across ocean basins.
  - **Relation to the Project**: This study demonstrates that neural networks can reliably reconstruct vertical ocean profiles (0–250 m) from surface measurements. Although limited to the euphotic zone rather than 0–1000 m, its approach — linking surface environmental data to vertical structure via ANNs — is directly relevant to predicting biomass or carbon-flux profiles with TensorFlow.

- **Source 4**: [From time series to image analysis: A transfer learning approach for night setback identification of district heating substations, Zhang et al. 2021]

  - **[Online Link](https://www.sciencedirect.com/science/article/pii/S2352710221003946)
  - **Objective**: Use deep learning convolutional neural networks to classify time-series of district heating substations by turning time-series into heatmap images with the shape (hour of the day x day of the month x normalized heat energy usage).
  - **Methods**: Transfer learning is used to take advantage of pre-trained fundamental feature detection. Used models were: Resnet, Vgg, Alexnet, Squeezenet, MobilenetV2, Densenet, and variations. They generated images from time-series data and then applied augmentation (gaussian noise, sliding window, mixup). They tested training with feature extraction and full fine-tuning (discriminative learning rates). Then they tested all trained models and compared accuracy, f1, precision and recall. They also use gradient class activation map (GRAD_CAM) and guided back-propagation to interpret the models.
  - **Outcomes**: All models achieved an overall accuracy > 0.95 and f1 > 0.9, with MobilenetV2 performing the best. GRAD-CAM and guided backpropagation maps highlighted areas as important which are considered relevant for classification by experts.
  - **Relation to Project**:Instead of time-series heatmaps, we aim to work with heatmaps of particle biovolume over depth and size class, also generating images from data which we then want to classify. By using transfer learning in a similar way to the here presented study, we may be able to account for biases in our dataset.