# Classification
We used data from ``../AllData.zip`` to classify games into different "popularity grades", based on the average player count per day on Steam. For example, we defined the following rubric for heuristic feature selection (see ``Feature Importance for StreamLit.ipynb``):

| Grade | `mean_players` |
|-------|----------------|
|5|>10,000|
|4|>1,000 and <10,000|
|3|>100 and <1,000|
|2|>10 and <100|
|1|<10|
