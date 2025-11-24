
# About the project

This repository is meant as a learning experience for building more professional and well-structured data science projects. The final goal is to develop a full end-to-end ML pipeline and deploy it on the web — currently, only the ETL pipeline is mostly complete.

# More details
In short: the game Football Manager 24 provides detailed attribute ratings for almost every professional football player. There are about 30 attributes, such as speed, passing, finishing, etc. Combined with extensive match-history data, these attributes offer a convenient way to generate meaningful features for machine learning models.

# The ETL pipeline

The extraction stage involves Python scripts that scrape FM24 player data in bulk, alongside collecting historical match data via free APIs.
The transformation stage automates SQL scripts for data cleaning and basic feature engineering. Finally, the loading stage stores all processed data in a database/CSV and sends it to a dashboard for visualization.
