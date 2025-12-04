
# About the project


An end-to-end football prediction pipeline using Football Manger 24 player attributes +
past match statistics. Includes ETL, feature engineering, machine learning
models, and dashboards for visualizing predictions and comparisons with bookmaker odds.



## Motivation

1. Primarily meant as a learning experience for building more professional and well-structured data science projects. 

2. From a sports analytics perspective, it also explores an interesting question:
How predictive are Football Manager (FM24) player attributes compared to real betting market odds?


<details>
  <summary> More on sports betting market efficiency </summary>
</details>

## Tech used + How it's made 
python, pandas, Streamlit, SQL, PostgreSQL


## Current work

- Focusing only on one league (EPL). Toy pgsql ETL pipelines using small, manually collected data and free APIs. 
- Feature engineering experiments (PCA-reduced features vs. raw averages vs. hybrid representations)
- Model training/testing. Variable importance.
- *Static* model dashboard deployment using Streamline


  
## Future updates

- More data: expanding to top 10 leagues + nation football. Scraping scripts and better ETL pipelines to be made...
- *Dynamic* model dashboard deployment (re-train manually every month). Setting up a REST API and/or a website.


## Past work


A more primitive early version of this work (implemented as messy R notebooks) is included in the attached PDF.

# The data

## FM24 attributes


- ~30 player attributes (technical, mental, physical)
- Exported manually from Football Manager 24


<img width="833" height="554" alt="image" src="https://github.com/user-attachments/assets/4a4f4b30-5f93-4357-a119-57ffdfbe31da" />

<details>
  <summary> Keeper attributes are different ! (see example) </summary>
  <img width="833" height="554" alt="image" src="https://github.com/user-attachments/assets/af35e871-d7f1-4f9e-9755-957ee63e6267" />

</details>


## Past match statistics

- Past match results and advanced metrics (xG, shots, referees, etc.)


<details>
  <summary> Exported by copy pasting from fbref </summary>
 <img width="1035" height="525" alt="image" src="https://github.com/user-attachments/assets/dc0e77ec-7bdc-4dad-a21c-6526523ccbb7" />

</details>



  

# Models


**Baseline**: Random Forest, XGBoost  
**Experiments**: CatBoost
**Targets**: win/draw/lose probabilities, xG prediction, goal counts  
**Features**: aggregated FM24 attributes (PCA, averages, engineered features). More details in the EDA.ipynb.

# Dashboards and Deployement


