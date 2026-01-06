
# About the project


An end-to-end football prediction pipeline using Football Manger 24 player attributes +
past match statistics. Includes ETL, feature engineering, machine learning
models, and dashboards for visualizing players and predictions.

You can view the dashboard (two Streamlit pages: Player Attributes + ML Predictions) here: 

👉 https://epl-predictions-using-fm24-attributes-qmync3jwp3v44pf5szzvuf.streamlit.app/

For the top5 five leagues: 1X (home double chance) predictions here (very close to Pinnacle's odds):

👉 https://home-doublechance.streamlit.app/



## Motivation

1. Primarily meant as a learning experience for building more professional and well-structured data science projects. 

2. From a sports analytics perspective, it also explores an interesting question:
 How predictive are Football Manager (FM24) player attributes ?



## Tech used + How it's made 
python, pandas, Streamlit, SQL, PostgreSQL


## Current work

- Focusing only on one league (EPL). Manually collected data. Toy pgsql ETL pipelines. 
- Feature engineering experiments (PCA-reduced features vs. raw averages vs. hybrid representations)
- Model training/testing. Variable importance.
- Player & ML dashboards (per-player attributes, radar plots, model predictions), built and deployed using Streamlit.




## Future updates

- More data: expanding to top 10 leagues + nation football. Extraction automation: scraping scripts and better ETL pipelines to be made...
- Comparison with bookmaker odds
- *Dynamic* model dashboard deployment (re-train manually every month). Setting up a REST API and/or a website.


## Past work


A more primitive early version of this work (implemented as messy R notebooks) is included in the attached PDF.

# The data

## FM24 attributes


- ~30 player attributes (technical, mental, physical)
- Exported from Football Manager 24


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


**Baseline**: Random Forest  
**Experiments**: CatBoost
**Targets**: win/draw/lose probabilities, xG prediction, goal counts  
**Features**: aggregated FM24 attributes (PCA, averages, engineered features). More details in the EDA.ipynb.

# Dashboards and Deployement


