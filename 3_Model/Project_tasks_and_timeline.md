### Project plan

1) Find heatmap version which is best for model predictions in simple CNN 
	1) sigma, color
	2) keep small size for faster computing
2) Test transfer learning. 
	1) Choose 2 models: 1 medical model & one general model like Alexnet (suggested by Jake)
	2) Use gradual unfreezing of layers from the back. 
	3) Try adapting heatmap color & size to what the model was trained on.
3) Compare transfer learning and simple CNN results - choose the best model to continue with.
4) Hyperparameter tuning (1 model)
	1) Use raytune (faster) or keras.tune (in tensorflow)
	2) e.g., learning rate, batch size, dropout rate, patience, augmentation (noise), balancing method (simple vs. SMOTETomek)
5) Model interpretation
	1) Use SHAP and/or GRAD-CAM to visualise most important features for different classes
	2) Interpret results in ecological context
6) Presentation (15 min + Q&A)
	1. **Title Slide**: Project name, names of the project team, date, and any other relevant information.
	2. **Introduction**: 1-2 slides briefly introducing your project.
	3. **Literature Review**: 1 slide highlighting related work.
	4. **Dataset Characteristics**: 1-2 slides.
	5. **Baseline Model**: 1 slide.
	6. **Model Definition and Evaluation**: 3-4 slides.
	7. **Results**: 2-3 slides.
	8. **Challenges and Errors**: 1 slide.
	9. **Discussion**: 1-2 slides.
	10. **Conclusion and Future Work**: 1 slide.
	11. **Q&A**: Final slide indicating the Q&A part.
7) Submission (deadline for the documented repo: 30.02.)
	1. **Slides**: Create your presentation slides. Save them in 4_Presentation as a PowerPoint, Google Slides, or PDF file.
	2. **Cover Image**: Replace the placeholder image in CoverImage with an image from your slides.
	3. **README**: Update the main README with project details.
	4. **Link to Slides**: Modify the link in this folder's README point to your presentation slides.
	5. **edu.opencampus.sh Submission**: by one team member

| Due date   | Task                                                                                                                                                                                                                                                      |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 22.12.2025 | Sina H.: Find suitable transfer learning models (free versions)<br>Tobias: Try out different heatmap visualisations in simple CNN<br>Bianca: Research hierarchical model methods<br>**Meeting: **<br>- Assign tasks for over holidays - transfer learning |
| 05.01.2026 | *Milestone:* Tested transfer learning models<br>**Meeting:** <br>- Decide which model to keep and tune<br>- Assign tasks for hyperparameter tuning & training on full dataset                                                                             |
| 12.01.2026 | *Milestone:* Finalised model, trained on full dataset<br>**Meeting:**<br>- Assign tasks for model interpretation (SHAP, GRAD-CAM)                                                                                                                         |
| 15.01.2026 | *Milestones:* <br>- Interpreted final model features<br>- Finalised code (trained full model & evaluated important features)<br>**Meeting:**<br>- Assignment of presentation sections (latest)                                                            |
| 19.01.2026 | *Milestone:* Everyone prepared their first section draft<br>**Meeting:**<br>- We discuss presentation & improve flow and timing                                                                                                                           |
| 22.01.2026 | *Milestone:* Presentation                                                                                                                                                                                                                                 |
| 30.02.2026 | *Milestone:* Final submission (preferably earlier)                                                                                                                                                                                                        |
