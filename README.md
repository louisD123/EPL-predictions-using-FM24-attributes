
# About the project


An end-to-end football prediction pipeline using FM24 player attributes +
past match statistics. Includes ETL, feature engineering, machine learning
models, and dashboards for visualizing predictions and comparisons with bookmaker odds.




## Motivation

Primarily meant as a learning experience for building more professional and well-structured data science projects. 

From a sports betting perspective it is very interesting to explore the predictive power of video game stats.


<details>
  <summary>Click to expand: More on Sports betting market efficiency </summary>
</details>

## Tech used
python, SQL, PostgreSQL


## Current work

- Toy pgsql ETL pipelines using small, manually collected data and free APIs.
- Feature engineering experiments (PCA-reduced features vs. raw averages vs. hybrid representations)
- Model training/testing 
- *Static* model dashboard deployment using Streamline


  
## Future updates

- More data: scraping scripts and better ETL pipelines
- *Dynamic* model dashboard deployment


## Past work


A more primitive early version of this work (implemented as messy R notebooks) is included in the attached PDF.

# The data

## FM24 attributes
The game Football Manager 24 provides detailed attribute ratings for almost every professional football player. There are about 30 attributes, such as speed, passing, finishing, etc. 

<img width="819" height="562" alt="image" src="https://github.com/user-attachments/assets/0172bd6b-9a50-4540-8c6f-fb77c2ac287d" />




## Past match statistics

Records of previous games and advanced game statistcs can be freely found online. To avoid a scraping procedures or API retrieval setups **we use data from fbref**, which can be exported without too much issues.


<img width="1035" height="525" alt="image" src="https://github.com/user-attachments/assets/dc0e77ec-7bdc-4dad-a21c-6526523ccbb7" />


## Data collection

Currently the data is collected manually: 

- FM24 data cannot be exported en masse, rather it requires running the game, selecting appropriate filters and exporting data.

- Past match statistcs are copy pasted from fbref.  

# Models


**Baseline**: Random Forest, XGBoost  
**Experiments**:  
**Targets**: win/draw/lose probabilities, xG prediction, goal counts  
**Features**: aggregated FM24 attributes (PCA, averages, engineered features)

# Dashboards and Deployement


