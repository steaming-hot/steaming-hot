# Steaming-Hot
A project to study Steam game data, involving classification, prediction and survival analysis. Our team members are Alex Casella (acasella@fsu.edu
), Eduardo Medina (medin215@umn.edu), Joseph Leung (leung.179@osu.edu), Kanishk Jain (kanishkbjain@gmail.com), Ling Zhou (zhou.2568@osu.edu
) and Rohit Satija (rsatija@berkeley.edu). This project was done during the Erdős Institute's 2021 Boot Camp.

# Problem
While certain extremely popular games like PUBG, Dota 2, and Counter Strike GO have a religious following, a large majority of games on Steam are rarely played. Using a data-driven approach, we wanted to understand why certain games are more popular than others and use this information to help game developers and gaming studios to maximize the chances of success of their products.

# Key Questions
1. What features should game developers focus on, early in game development?
2. How should a developer present and price their game on the Steam library store?
3. How will the game perform in the future?

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
