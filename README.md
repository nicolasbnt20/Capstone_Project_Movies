# Movie Industry Profitability Analysis

This project explores profitability trends in the global film industry using real-world movie data.

It combines data cleaning, exploratory analysis, and regression modeling to answer key business questions around:
- Film investment efficiency (ROI vs profit)
- Genre strategy and seasonal timing
- Market dominance by production companies and countries

It concludes with an interactive Tableau dashboard built for stakeholder decision-making.


## Key Outcomes

- Cleaned and modeled 45000+ movie records from a public dataset
- Identified that low-budget films often outperform blockbusters in terms of ROI
- Built regression model for profit using genres, budget,release-month and company
- Designed 3-part Tableau dashboard with embedded navigation for exploration


## Interactive Dashboard (Tableau Public)

[Click here to explore](https://public.tableau.com/app/profile/nicolas.bunet/viz/Capstone_Project_Tableau_17476138469660/1-IndustryOverviewDashboard?publish=yes)

Dashboards include:
1. Industry Overview & Budget Strategy
2. Genre Strategy & Seasonality
3. Market Trends by Production Company & Country

All navigation via embedded hamburger menu


## Tools
- **Python** (Pandas, NumPy, Seaborn, Matplotlib, Statsmodels)
- **Jupyter Notebooks**
- **Tableau Public**
- **Git & GitHub**


## Project Workflow

1. **Data Cleaning**
   - Fixed incorrect data types and standardized formats
   - Removed duplicates and implausible values
   - Filtered extreme outliers 
   - Handled missing values through removal or imputation where appropriate
   - Converted multi-value list columns (genres, production companies, countries) into an exploded format for categorical analysis

2. **Exploratory Analysis**
   - Explored budget vs ROI and Profit trends
   - Analyzed profitability by genre, release month, production company, and country
   - Generated actionable business insights for content strategy and release timing

3. **Statistical Modeling**
   - Developed an OLS regression model to identify key drivers of movie profit
   - Performed log transformations to correct skewness
   - Applied dummy encoding for categorical variables 

4. **Data Visualization**
   - Designed 3 professional Tableau dashboards with embedded navigation
   - Included interactive KPIs, scatter plots, bar charts, line charts, and a geo map


## Project Structure

```
capstone_project_movies/
├── data
│   ├── raw
│   │   └── movies_metadata.csv
│   └── processed
│       ├── df_clean.csv / .pkl
│       ├── df_genres.csv / .pkl
│       ├── df_companies.csv / .pkl
│       └── df_countries.csv / .pkl
├── notebooks
│   ├── 1_Data_Cleaning_EDA.ipynb
│   ├── 2_Data_Analysis.ipynb
│   ├── 3_Data_Statistical_Modeling.ipynb
│   └── 4_Tableau_prep.ipynb
├── src
│   └── data_cleaning.py
├── tableau
│   ├── Capstone_Project_Tableau.twbx
│   ├── df_clean_export.csv
│   ├── df_genres_export.csv
│   ├── df_companies_export.csv
│   └── df_countries_export.csv
├── output
│   ├── figures
│   │   ├── 1_dashboard_overview_industry.png
│   │   ├── 2_dashboard_genre_strategy.png
│   │   ├── 3_dashboard_companies_countries.png
│   │   ├── budget_vs_revenue.png
│   │   └── budget_vs_roi.png
│   └── README.md
├── requirements.txt
└── tests
```