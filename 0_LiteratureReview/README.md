# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: [Particle production by mesopelagic fauna enhances deep-ocean carbon sequestration, Clements et al. 2025]

  - **[Link](https://www.researchsquare.com/article/rs-6465812/v1)**
  - **Objective**: Predict global Carbon transfer efficiency using UVP5 particle size-distribution data trained with environmental data.
  - **Methods**: The authors use a 2-target bagged Random Forest. They use environmental variables as features and total biovolume (across all size classes) and a value for size distribution ("PSD slope") as covariates. They run 50 realizations with varying features and hyperparameters. 
  - **Outcomes**: The model predicted total biovolume of validation data at an R2 > 0.85. The study outcome was a global reconstruction of carbon flux from the surface to 2000 m depth.
  - **Relation to the Project**: This study uses the same dataset and connects biovolume data to environmental conditions. We can use the list of feature datasets (in SI Table 1) to also include in our model. The difference to our project is that they only used total biovolume at different depths, while we are interested in 2D patterns (depth x particle size class).

- **Source 2**: [Title of Source 2]

  - **[Link]()**
  - **Objective**:
  - **Methods**:
  - **Outcomes**:
  - **Relation to the Project**:

- **Source 3**: [Title of Source 3]

  - **[Link]()**
  - **Objective**:
  - **Methods**:
  - **Outcomes**:
  - **Relation to the Project**:
