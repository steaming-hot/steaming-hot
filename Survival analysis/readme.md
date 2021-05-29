# Survival Analysis
We used data from ``../AllData.zip`` to generate a survival probability study. 

In this study, the definition for survival time is the total time it takes for a game to decrease the peak number of players to 10% of the total maximum peak. The timer starts once that maximum is reached. If a game has not reached 10% of the peak, the data is considered censored. An exponential fit was needed in order to eliminate the rapid changes between months. This eliminates unreal sudden deaths.

The Kaplan-Meier estimator was used to generate an estimate of the Survival Probability curve not involving the features.

![](Est_surv_prob.jpg?raw=true)

It is possible to appreciate a rapid slope at the beginning. This suggest that most of the games from the data set fall to the 10% mark within the first 6 to 10 months.
