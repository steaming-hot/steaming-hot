# Survival Analysis
We used data from ``../AllData.zip`` to generate generate a survival probability study. 

In this study, the definition for survival time is the total time it takes for a game to decrease the peak number of players to 10% of the total maximum peak. The timer starts once that maximum is reached. If a game has not reached 10% of the peak, the data is considered censored.  

An exponential fit was needed in order to eliminate the rapid changes between months. This eliminates unreal sudden deaths.

![](Est_surv_prob.jpg?raw=true)

