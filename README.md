
# About the project

This repository is meant as a learning experience for building more professional and well-structured data science projects. The final goal is to develop a static end-to-end ML model that predicts football statistics and deploy it to the web.

Currently, only a toy version of ETL pipeline is mostly complete.

A more primitive early version of this work (implemented as messy R notebooks) is included in the attached PDF.

# The data

## FM24 attributes
The game Football Manager 24 provides detailed attribute ratings for almost every professional football player. There are about 30 attributes, such as speed, passing, finishing, etc. 

<img width="967" height="729" alt="image" src="https://github.com/user-attachments/assets/14f886b9-cb98-4cdf-81b3-58394b62eb15" />

These attributes offer a convenient way to generate meaningful features for machine learning models.

## Fbref past match statistics

Records of previous games and advanced game statistcs can be freely found online. To avoid a scraping procedures or API retrieval setups we use data from fbref , which can be exported without too much issues.


<img width="1035" height="525" alt="image" src="https://github.com/user-attachments/assets/dc0e77ec-7bdc-4dad-a21c-6526523ccbb7" />


# Features and targets

The commbination of the two previous two lead to the training data:

- the targets can be choosen to be *win/draw/lose* probabilites , home_xG, away_xG , home_goals , away_goals, etc.
- and the features are home,away team rankings that are some functions of the FM24 attributes.





# The ETL pipeline

The extraction stage involves Python scripts that scrape FM24 player data in bulk, alongside collecting historical match data via free APIs.
The transformation stage automates SQL scripts for data cleaning and basic feature engineering. Finally, the loading stage stores all processed data in a database/CSV and sends it to a dashboard for visualization.
