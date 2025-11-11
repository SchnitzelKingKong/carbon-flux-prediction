# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: [Particle production by mesopelagic fauna enhances deep-ocean carbon sequestration, Clements et al. 2025]

  - **[Link](https://www.researchsquare.com/article/rs-6465812/v1)**
  - **Objective**: Predict global Carbon transfer efficiency using UVP5 particle size-distribution data trained with environmental data.
  - **Methods**: The authors use a 2-target bagged Random Forest. They use environmental variables as features and total biovolume (across all size classes) and a value for size distribution ("PSD slope") as covariates. They run 50 realizations with varying features and hyperparameters. 
  - **Outcomes**: The model predicted total biovolume of validation data at an R2 > 0.85. The study outcome was a global reconstruction of carbon flux from the surface to 2000 m depth.
  - **Relation to the Project**: This study uses the same dataset and connects biovolume data to environmental conditions. We can use the list of feature datasets (in SI Table 1) to also include in our model. The difference to our project is that they only used total biovolume at different depths, while we are interested in 2D patterns (depth x particle size class).

- **Source 2**: [A deep-learning estimate of the decadal trends in the Southern Ocean carbon storage, Zemskovska et al. 2022]

  - **[Link](https://www.nature.com/articles/s41467-022-31560-5)**
  - **Objective**: The study aimed to estimate changes in dissolved inorganic carbon (DIC) concentrations in the interior of the Southern Ocean (down to 4 km depth) over the past three decades (1993–2019). Because in-situ observations are sparse at depth, the researchers used deep learning to estimate long-term carbon storage trends and evaluate the ocean’s changing capacity to absorb atmospheric CO₂.
  - **Methods**: Developed a deep neural network (with convolutional and recurrent layers) to predict subsurface DIC concentrations from observable surface and near-surface variables(Biogeochemical Southern Ocean State Estimate (B-SOSE) model, ship-based profiles (GLODAPv2) and biogeochemical Argo floats (SOCCOM)). They trained 22 different models for different depths!
  - **Outcomes**:
  In the 1990s–2000s, upper-ocean DIC concentrations declined, reflecting enhanced CO₂ uptake by the Southern Ocean. In the 2010s, this trend reversed in the surface layers — DIC increased again, suggesting a weakening of the oceanic carbon sink. Deeper layers showed DIC accumulation, indicating reduced vertical exchange and a slower sequestration of atmospheric CO₂ into the deep ocean. Atlantic, Indian, and Pacific sectors exhibited distinct trends.
  - **Relation to the Project**: They used comparable data formats like we are planning: model data as input, and potentially GLODAPv2 data. Their method could be comparable (we might also need to use convolutional layers as we are aiming for 2D output) and we also thought about training different models for different regions (depth layers in their case, maybe ocean basins in our case?). Their work on environmental data shows comparable challenges that we might face like sparse data sets.

- **Source 3**: [Title of Source 3]

  - **[Link]()**
  - **Objective**:
  - **Methods**:
  - **Outcomes**:
  - **Relation to the Project**:
