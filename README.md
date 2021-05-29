# Steaming-Hot
A project to study Steam games and user data, involving classification, prediction and survival analysis. Our team members are Alex Casella (acasella@fsu.edu
), Eduardo Medina (medin215@umn.edu), Joseph Leung (leung.179@osu.edu), Kanishk Jain (kanishkbjain@gmail.com), Ling Zhou (zhou.2568@osu.edu
) and Rohit Satija (rsatija@berkeley.edu). This project was done during the Erdős Institute's 2021 Boot Camp.

Link to video: https://drive.google.com/file/d/1JbodnKoRUWbPY249GB33Lu0whW1_2LKX/view
Link to presentation: https://docs.google.com/presentation/d/1nM5lSnacehA5WepppeFtgiUC-IamrOd8LfG_LXbt1E8/edit#slide=id.p

# Problem
While certain extremely popular games like PUBG, Dota 2, and Counter Strike GO have a religious following, a large majority of games on Steam are rarely played. Using a data-driven approach, we wanted to understand why certain games are more popular than others and use this information to help game developers and gaming studios to maximize the chances of success of their products.

## Key Questions
1. What features should game developers focus on, early during game development?
2. How should a developer present and price their game on the Steam library store?
3. Based on its individual features and track record, how will a game perform in the future?
4. What measures can one take to improve the performance of a game on Steam?

# Data Scraping and Cleaning

We scraped data from (see ``./Data Scraping and Cleaning`` for the code)
- [SteamCharts](https://steamcharts.com/) for time series data of number of players of 10k+ games.
- [SteamSpy](https://steamspy.com/) for owners and userscores of 57k+ games, 
- [Metacritic](https://www.metacritic.com/) for metacritic scores of 57k+ games,
- [Steam](https://store.steampowered.com/) for 70+ game features of 57k+ games, using files taken from https://github.com/CraigKelly/steam-data.

You can access some of our data from the following files:
- The file `SteamCharts.csv` contains monthly data during July 2012 to April 2021 of the monthly number of players.
- The file `AllData.zip` contains game features, together with the max and mean of 'Avg_Players' and the max and mean of 'Peak_Players'.

Please email the team members to request access to the full data. 

# Exploratory Data Analysis

See ``ExploratoryDataAnalysis.ipynb`` for some example Jupyter notebooks examing the data, and more in other folders. We plotted scatter matrix of the continous futures, histograms for the categorical features, PCA, etc.

# Modeling
Using these data, we developed several algorithmic and machine learning techniques to address feature selection, revenue modeling, and forecasting.  

## Classification
We deployed several machine learning algorithms, including K-Nearest Neighbors, Logistic Regression, Support Vector Machines, Decision Trees, Random Forests, and AdaBoost to classify ~8,000 games with ~47 numeric and categorical features based on their popularity. See ``./Classification`` for more information and the corresponding Jupyter notebooks.

## Sales prediction 
The notebook DataAnalysis.ipynb contains exploratory modeling of the following problem -


Under the (false) assumption that sales scale linearly with age of a game, we try to predict monthly sales of a game using numerical features from a game’s steam page - like number of screenshots and video trailers, price, packages and number of in-game achievements. We assume these metrics are what drive sales when someone is exploring a game's steam page. 
Our best model on the entire dataset is UMAP based. We use UMAP to find non-linear 2-dimensional embeddings that seemed to cluster games with similar monthly sales together. We use kmeans to find these clusters, and use the median monthly sale in each clusters as OUR prediction of sales for all games in that cluster. The median of absolute errors from this method is 3x of the true values. Meaning for a game with 10k monthly sales, we are predicting anywhere from 0 to 40k. This was our best result given the range of monthly sales range from 1k to ~10million.
We also tried other models such as random forest regression, decision tree regression and linear regressions. Decision tree regression beat UMAP model when we constrained our data to have games with monthly owners below 100,000.  

## Time Series Models

We used time series data from ``SteamCharts.csv`` to perform prediction and build the 'Time Comparison Model'. For the prediction model, we used naive, exponential smoothing and ARIMA to perform prediction. On the other hand, The Time Comparison Model is built up in order to offer suggestions on what future steps a game developer can take when his game is out for a certain time period. This model compares the input game with games in database, collects the games with similar starting history and output a weighted average together with a list of close games. This allows the game developer to learn from previous popular/unpopular games, know what to expect and hopefully be able to strategically determine his future plan on the game.

## Survival Analysis
We implemented both the  Kaplan-Meier estimator and Cox's proportional hazards model on time series data with respect to the peak players per month since the day of a game release. We build a survival probability curve that depends on feature selection. Since the Harrell's concordance index is below 0.7, we determine that it is not a viable option to predict survivability. However, the coefficients from the generated fit provide the feature prognostic factor, which gives insight into the impact of a feature on survivability. See ./Survival Analysis for more information and the corresponding Jupyter notebook.

# WebApp
See [https://share.streamlit.io/alexcasella/streamlit/main/main.py](https://share.streamlit.io/alexcasella/streamlit/main/main.py).
