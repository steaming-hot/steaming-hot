# Steaming-Hot
A project to study Steam game data, involving classification, prediction and survival analysis. Our team members are Alex Casella (acasella@fsu.edu
), Eduardo Medina (medin215@umn.edu), Joseph Leung (leung.179@osu.edu), Kanishk Jain (kanishkbjain@gmail.com), Ling Zhou (zhou.2568@osu.edu
) and Rohit Satija (rsatija@berkeley.edu). This project was done during the Erdős Institute's 2021 Boot Camp.

# Problem
We wanted to create a recommendation engine for game developers and gaming studios so they could maximize the chances of success of their products

# Goals
To address this problem, we divided our solutions into three broad categories:
1. Development: What features should game developers focus on, early on?
2. Deployment: How should a developer present their game in a Steam library store? What is the expected revenue?
3. 


# Data Scraping and Cleaning

We scraped data from (see ``./Data Scraping and Cleaning`` for the code)
- [SteamCharts](https://steamcharts.com/) for time series data of number of players of 10k+ games.
- [SteamSpy](https://steamspy.com/) for owners and userscores of 57k+ games, 
- [Metacritic](https://www.metacritic.com/) for metacritic scores of 57k+ games,
- [Steam](https://store.steampowered.com/) for 70+ game features of 57k+ games, using files taken from https://github.com/CraigKelly/steam-data.

You can access some of our data from the following files:
- The file `SteamCharts.csv` contains monthly data during July 2012 to April 2021 of the monthly number of players.
- The file `AllData.csv` contains game features, together with the max and mean of 'Avg_Players' and the max and mean of 'Peak_Players'.

Please email the team members to request access to the full data. 

# Exploratory Data Analysis

See ``./Exploratory Data Analysis`` for some example Jupyter notebooks examing the data. We have done basic plotting of the time series data, scatter matrix of the continous futures, histograms for the categorical features, etc.

# Modelling

## Classification

## Regression

## Time Series Prediction

## Survival Analysis

# WebApp

## Licensing

## Citing this work
