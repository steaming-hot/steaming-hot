# Classification
We used data from ``../AllData.zip`` to classify games into different "popularity grades", based on the average player count per day on Steam. For example, we defined the following rubric for heuristic feature selection:

- Grade 5: 10,000 < mean_players
- Grade 4: 1,000 < mean_players < 10,000
- Grade 3: 100 < mean_players < 1,000
- Grade 2: 10 < mean_players < 100
- Grade 1: mean_players < 10

For multi-class classification, the above categorization led to class imbalance and poor predictive power. Therefore, we restricted our machine learning models to only solve binary classification problems and efficiently distinguish the most popular games from the least popular ones.
