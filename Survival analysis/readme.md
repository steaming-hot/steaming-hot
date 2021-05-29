# Survival Analysis
We used data from ``../AllData.zip`` to generate generate a survival probability study. 

In this study, the definition for survival time is the total time it takes for a game to decrease the peak number of players to 10% of the total maximum peak. The timer starts once that maximum is reached. If a game has not reached 10% of the peak, the data is considered censored. An exponential fit was needed in order to eliminate the rapid changes between months. This eliminates unreal sudden deaths.

The Kaplan-Meier estimator was used to generate an estimate of the Survival Probability curve not involving the features.

![](Est_surv_prob.jpg?raw=true)

It is possible to appreciate a rapid slope at the beginning. This suggest that most of the games from the data set fall to the 10% mark within the first 6 to 10 months.

The  Cox's proportional hazards model was used to generate predictions comming from selected features. A total of 47 numeric features were selected. It is well known that to measure the performance of this model, we have to calculate the Harrell’s concordance index (1).

After cross validation, the concordance index was of ~6.5, which means that the model predicts a little better than random.

Although a prediction model is not reliable, we can still observe the prognostic factor, which are the coefficients comming from fitting. If a coefficient is greater than zero, then it contributes to a faster decline in survavility. The effect is the opposite for coefficients less than zero.

Here we report a few of them:

| Feature | `Coefficient` |
|-------|----------------|
|RequiredAge|-0.008818|
|DemoCount|0.025099|
|DeveloperCount|0.127606|
|DLCCount|-0.002965|
|MovieCount|0.065993|



(1)Harrell Jr, Frank E., Kerry L. Lee, and Daniel B. Mark. "Multivariable prognostic models: issues in developing models, evaluating assumptions and adequacy, and measuring and reducing errors." Statistics in medicine 15.4 (1996): 361-387.
