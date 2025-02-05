## Automated Data Analysis Web Application using Streamlit
Project Overview
This project is a Streamlit-based web application that automates data analysis tasks for uploaded datasets. The application provides users with an interactive interface for conducting univariate, bivariate, and multivariate analysis on their datasets. It supports data visualization, summary statistics, and correlation analysis, making it a powerful tool for quick insights.

## Features
# 1. Data Upload and Loading
Supports .csv and .xlsx file formats.
Automatically detects and separates categorical and numerical columns.
# 2. Data Summary
Display dataset shape and sample data (head()).
Show basic summary statistics (describe()).
Display missing value counts for each column.
# 3. Univariate Analysis
Numerical Data: Histogram and box plots.
Categorical Data: Frequency count bar charts.
# 4. Bivariate Analysis
Numerical-Numerical: Scatter plots for visualizing relationships.
Categorical-Numerical: Box plots for comparative analysis.
# 5. Multivariate Analysis
Pair plots for identifying relationships between multiple numerical features.
Correlation heatmap with interactive color scale.
# 6. Interactive Plots
Dynamic chart selection for line charts, bar charts, and histograms.
Choose columns to visualize relationships between specific features.
How to Use the Application
Clone the repository to your local machine.
https://github.com/SUMANTH1543/Automate_DataAnalysis.git
Navigate to the project directory.

cd automate_DataAnalysis
# Install the required dependencies.
# pip install -r requirements.txt
Run the Streamlit app.
streamlit run application.py
Upload your dataset (.csv or .xlsx) and start exploring the data.
Dependencies
Python 3.10+
Streamlit
Pandas
Plotly
Matplotlib
Seaborn
Openpyxl (for .xlsx support)
# Install all dependencies using:
nginx
pip install -r requirements.txt
# Project Structure:
📂 Automated Data Analysis  
 ┣ 📜 application.py           # Main Streamlit app script  
 ┣ 📜 requirements.txt         # Python dependencies  
 ┗ 📜 README.md                # Project documentation  
Sample Visualizations
# 1. Correlation Matrix
# 2. Scatter Plot
# Future Enhancements
Add predictive modeling features.
Support for more file formats (.json, .sql).
Integration with cloud storage for large datasets.
Contribution
Contributions are welcome! If you find any bugs or want to enhance the project, feel free to create a pull request or raise an issue.

Author
[G Sumanth]
Data Science Enthusiast 
