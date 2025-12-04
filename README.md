
# About the project

This repository is meant as a learning experience for building more professional and well-structured data science projects. The final goal is to **develop and deploy a dynamic end-to-end ML model that predicts football statistics/probabilities** and compares them to the predictions of the leading bookmakers.

## Current work

- Toy pgsql ETL pipelines using small, manually collected data and free APIs.
  - E : 
  - T : Running various SQL scripts to clean/merge the data
  - L : Saving to .csv and uploading to a data warehouse.
- PCA reduced features
- Model training/testing 
- Static model dashboard deployment

  
## Future updates

- More data: scraping scripts and better ETL pipelines
- 
-


A more primitive early version of this work (implemented as messy R notebooks) is included in the attached PDF.

# The data

## FM24 attributes
The game Football Manager 24 provides detailed attribute ratings for almost every professional football player. There are about 30 attributes, such as speed, passing, finishing, etc. 

<img width="967" height="729" alt="image" src="https://github.com/user-attachments/assets/14f886b9-cb98-4cdf-81b3-58394b62eb15" />

These attributes offer a convenient way to generate meaningful features for machine learning models.

## Past match statistics

Records of previous games and advanced game statistcs can be freely found online. To avoid a scraping procedures or API retrieval setups **we use data from fbref**, which can be exported without too much issues.


<img width="1035" height="525" alt="image" src="https://github.com/user-attachments/assets/dc0e77ec-7bdc-4dad-a21c-6526523ccbb7" />


## Data collection

Currently the data is collected manually: 

- FM24 data cannot be exported en masse, rather it requires running the game, selecting appropriate filters and exporting data.

- Past match statistcs are copy pasted from fbref.  


In the future, to allow for more scalability: 

- automated python scripts are envisaged for FM24 data extraction
- scraping procedures for more advanced statistics (big chances, shots on target, corners, etc.)


# Features and targets

The commbination of the two previous two lead to the training data:

- the targets can be choosen to be *win/draw/lose* probabilites , home_xG, away_xG , home_goals , away_goals, etc.
- and the features are home,away team rankings that are some functions of the FM24 attributes.





# The ETL pipeline

The extraction stage involves Python scripts that scrape FM24 player data in bulk, alongside collecting historical match data via free APIs.
The transformation stage automates SQL scripts for data cleaning and basic feature engineering. Finally, the loading stage stores all processed data in a database/CSV and sends it to a dashboard for visualization.
