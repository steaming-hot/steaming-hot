# Classification
We used data from ``../AllData.zip`` to classify games into different "popularity grades", based on the average player count per day on Steam. For example, we defined the following rubric for heuristic feature selection (see ``Feature Importance for StreamLit.ipynb``):

| Grade | `mean_players` |
|-------|----------------|
|5|>10,000|
|4|>1,000 and <10,000|
|3|>100 and <1,000|
|2|>10 and <100|
|1|<10|

For multi-class classification, the above categorization led to class imbalance and poor predictive power. Therefore, we restricted our machine learning models to only solve binary classification problems and efficiently distinguish the more popular games (100 < `mean_players`) from the less popular ones (`mean_players` < 5).

Here is a brief test set performance summary of all models that we tried:

| Model | `accuracy_score`% | `precision_score`% | `recall_score`% | `f1_score`% | `AUC_score`% |
|-------|-------------------|--------------------|-----------------|-------------|--------------|
|K-Nearest Neighbors|73.78|74.94|71.96|73.42|81.86|
|Decision Tree|75.86|78.84|75.96|74.77|82.18|
|Support Vector Machine|75.78|73.45|81.24|77.15|83.1|
|Logistic Regression|79.11|80.05|77.92|78.97|87.41|
|AdaBoost|79.68|81.08|78.47|79.38|88.8|
|Random Forest|81.46|81.81|81.86|81.58|89.61|

You can access each model and the associated performance measurements and feature selection using the corresponding jupyter notebook.
