# Time Series Analysis: Prediction and Time Comparison Model

We used time series data from ``../SteamCharts.csv`` to perform prediction and build the 'Time Comparison Model'.

### Prediction Model

For the prediction model, we used naive, exponential smoothing and ARIMA to perform prediction. Turn out all of them have similar accuracy. See the ``TS-BasicMethodPrediction.ipynb`` notebook for details.

### Time Comparison Model

In order to offer suggestions on what future steps a game developer can take when his game is out for a certain time period, we build up the Time Comparison Model.

This model compares the input game with games in database, collects the games with similar starting history and output a weighted average together with a list of close games. This allows the game developer to learn from previous popular/unpopular games, know what to expect and hopefully be able to strategically determine his future plan on the game.

The code we wrote up is primarily focused on: given a game with **12**-month data of average number of players, we study how games with similar **12**-month history behave in the next **6**-month. However, one can easily change the length of input data and the length of observation.

#### Data Preparation

To do so, we prepare our data in the ``TS_DataPreparation.ipynb`` notebook. Because of our purpose above, we only include games with complete data of 18 months from its birth as our database.

#### Building the Model and Explanation

In summary, the model is built with the following steps.
1. Scale and smooth both the input data A and time series data in database.
2. For every data B in the database, compare smoothed scaled A with smoothed scaled B with a suitable metric. Compute the weight (relative to A) with Guassian kernel.
3. Collect all data B with big enough weight.
4. Compute a weighted average: sum over B multiply by its weight that has big enough weight. Scale the weighted sum.

For more details, this process is explained and built in the ``TS_ModelExp.ipynb`` notebook. Here's an example if you input a game with first 12 month data being
[500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100]

![image](TimeComparasionExample.png)

One can see our model finds close scaled games, compute the weighted average and plot the closest three of them.

For the final model, the code is written up in the ``TS_Model.ipynb`` notebook. It reads in the data prepared in the ``TS_DataPreparation.ipynb`` notebook and build our model on that. 

#### Uses

There are many ways to use such model. Here's a few of them:

1. The weighted average curve (red dashed curve) acts as an indicator of success for games in the data base. One can then study these close games that share similar starting first 12 months data and understand why they are good (how far above the weighted average curve), or doing not as good (how far below the weighted average curve).
2. Case study on close games that are popular. Learn if they did any 'timed-features', such as releasing DLC, updates, changing the price, holding tournaments, etc to boost the popularity.
3. Know what to expect for the future of your game.

#### Using Time Comparison Model as Prediction Model

If one uses the weighted average as prediction, Cross Validation is done in the ``TS_ModelExp.ipynb`` notebook, and accuracy is computed in the ``TS_Accuracy.ipynb`` notebook.
