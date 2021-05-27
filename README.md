# steaming-hot
A project to study Steam game data, involving classification, prediction and survival analysis. Our team members are Alex Casella (acasella@fsu.edu
), Eduardo Medina (medin215@umn.edu), Joseph Leung (leung.179@osu.edu), Kanishk Jain (kanishkbjain@gmail.com), Ling Zhou (zhou.2568@osu.edu
) and Rohit Satija (rsatija@berkeley.edu). This project is done during the Erdős Institute's 2021 Boot Camp.

# Problem and Goals

## Goal

# Data Scraping and Cleaning

We scrap data from 
- [SteamCharts](https://steamcharts.com/) for time series data of number of players, 
- [SteamSpy](https://steamspy.com/) for owners and userscores, 
- [Steam](https://store.steampowered.com/) for 70+ game features, using files taken from https://github.com/CraigKelly/steam-data.
- [Metacritic](https://www.metacritic.com/) for metacritic scores.

See ``./Data Scraping and Cleaning`` for how we scraped the data. 
- The file `SteamCharts.csv` contains monthly data during July 2012 to April 2021 of the monthly number of players.
- The file `AllData.csv` contains game features, together with the max and mean of 'Avg_Players' and the max and mean of 'Peak_Players'.

We are not able to upload all of the data, as some of them exceeds the upload limit. Please email the team members to request access to more data. 

# Exploratory Data Analysis

The file ``./Exploratory Data Analysis`` contains the explanation of the data 


# Modelling

## Classification

## Regression

## Time Series Prediction

## Survival Analysis
