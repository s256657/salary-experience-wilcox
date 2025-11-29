# salary-experience-wilcox
Masters capstone project analyzing salary based on experience in field

## Purpose
To analyze the relationship and correlation between salary and years of experience in a dataset. Explaining that relationship using regression and breaking down how job title effects the detail of the correlation. Then use machine learning to predict outcomes. This repo was used to complete a research paper viewable through Overleaf titled [Salary and Experience Analysis using Machine Learning](https://www.overleaf.com/read/vvgygnpzxmzf#c65a26).

To follow project and recreate this README will guide through the process in order

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

### Analysis Folder
1. eda.ipynb - Exploratory Data Analysis occurs. Multiple tests were run during this Jupiter notbook to look at types and initial basics of the data. Initial correlation was theorized and Job Title was investigated as there are limitations in the data when using that as a variable. Many initial visualizations were also created to guide deeper analysis.
2. advanced_analysis.ipynb - This Jupyter notebook completed many goals
   1. Prove correlation analysis first using the data in its entirety then broken down by Job Title
   2. Explain correlation using regression analysis first using the data in its entirety then breaking down by Job Title
   3. Use machine learning to predict outcomes

### Conclusions
The first purpose was to prove correlation within the dataset between Salary and Years of Experience. This was completed and proven by a Pearson Correlation of .809 and explained by OLS regression r-squared of 0.654. Correlation is very Job Title dependent within the a full breakdown can be observed in [Advanced Analysis Notebook](analysis/advanced_analysis.ipynb) but the regression R-squared ranges from 0.996 to 0.238. Last machine learning models were created and trained to test if predictions could be made. Two models both performed well the highest performer was Random Forest at 0.943 but Gradient Boosting also performed well at 0.908.