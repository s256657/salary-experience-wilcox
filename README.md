# salary-experience-wilcox
Masters capstone project analyzing salary based on experience in field

## Purpose
To analyze the relationship and correlation between salary and years of experience in a dataset. Explaining that relationship using regression and breaking down how job title effects the detail of the correlation. Then use machine learning to predict outcomes. This repo was used to complete a research paper viewable through Overleaf titled [Salary and Experience Analysis using Machine Learning](https://www.overleaf.com/read/vvgygnpzxmzf#c65a26).

### Organization of Repo
- analysis
  - advanced_analysis.ipynb
  - eda.ipynb
- data
  - data_clean.ipynb
  - load_clean_data.py
  - load_salary_data_raw.py
  - salary_data_clean.db
  - Salary_Data_Cleaned.csv
  - Salary_Data.csv
  - dalary_data.db
- .gitignore
- README.md
- requirements.yxy

### Project Initialization
Create and activate virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
Install dependencies
```
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
```

### Data folder
The data folder houses raw data in Salary_Data.csv then a cleaned version Salary_Data_Cleaned.csv. The order in which the files were used are below
1. load_salary_data_raw.py - this initially creates a database for inspection salary_data.db
2. data_clean.ipynb - Jupyter notebook which guides through each step in the cleaning process and creates Salary_data_Cleaned.csv
3. load_clean_data.py - loads the cleaned data into a new database salary_data_clean.db

