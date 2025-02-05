import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load dataset
def load_data(file):
    if file is not None:
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            return pd.read_excel(file)
        else:
            st.error("Unsupported file type")
            return None
    return None

# Function to separate categorical and numerical columns
def categorize_columns(df):
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    return categorical_columns, numerical_columns

# Function to display summary statistics
def display_summary_stats(df, numerical_columns):
    st.subheader("Summary Statistics (Numerical Data)")
    st.write(df[numerical_columns].describe())

# Function to display missing values
def display_missing_values(df):
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

# Function to visualize data interactively
def display_visualizations(df, numerical_columns, categorical_columns):
    st.subheader("Interactive Visualizations")
    chart_type = st.selectbox("Select chart type", ["Scatter Plot", "Line Chart", "Bar Chart"])

    columns = numerical_columns + categorical_columns
    if len(columns) < 2:
        st.warning("Dataset must have at least two columns for visualization.")
        return

    x_column = st.selectbox("Select X-axis column", columns, key="x_col")
    y_column = st.selectbox("Select Y-axis column", columns, key="y_col")

    if x_column and y_column:
        if chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_column, y=y_column, title=f"Scatter Plot: {x_column} vs {y_column}")
            st.plotly_chart(fig)

        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_column, y=y_column, title=f"Line Chart: {x_column} vs {y_column}")
            st.plotly_chart(fig)

        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=x_column, y=y_column, title=f"Bar Chart: {x_column} vs {y_column}")
            st.plotly_chart(fig)

# Function to display correlation matrix interactively
def display_correlation_matrix(df, numerical_columns):
    st.subheader("Correlation Matrix")
    if not numerical_columns:
        st.warning("No numeric columns available for correlation matrix.")
        return

    correlation = df[numerical_columns].corr()
    fig = px.imshow(correlation, text_auto=True, color_continuous_scale='viridis', title="Correlation Matrix")
    st.plotly_chart(fig)

# Univariate Analysis
def univariate_analysis(df):
    column = st.selectbox("Select a column for Univariate Analysis", df.columns)
    if df[column].dtype in ['int64', 'float64']:
        st.write("Histogram:")
        fig, ax = plt.subplots()
        sns.histplot(data=df, x=column, kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.write("Frequency Count:")
        st.write(df[column].value_counts())

# Bivariate Analysis
def bivariate_analysis(df):
    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns)
    if df[x_column].dtype in ['int64', 'float64'] and df[y_column].dtype in ['int64', 'float64']:
        st.write("Scatter Plot:")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_column, y=y_column, ax=ax)
        st.pyplot(fig)
    else:
        st.write("Box Plot:")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x=x_column, y=y_column, ax=ax)
        st.pyplot(fig)


# Main app function
def main():
    st.title("Automated Data Analysis")
    
    uploaded_file = st.file_uploader("Upload a dataset", type=["csv", "xlsx"])
    
    if uploaded_file:
        df = load_data(uploaded_file)
        
        if df is not None:
            st.write(f"Dataset Shape: {df.shape}")
            st.write("First 5 Rows of Data:")
            st.write(df.head())

            # Categorize columns
            categorical_columns, numerical_columns = categorize_columns(df)
            st.write("Categorical Columns:", categorical_columns)
            st.write("Numerical Columns:", numerical_columns)
            
            # Display Summary Statistics
            if numerical_columns:
                display_summary_stats(df, numerical_columns)
            else:
                st.info("No numerical columns to display summary statistics.")
            
            display_missing_values(df)
            
            display_visualizations(df, numerical_columns, categorical_columns)

            display_correlation_matrix(df, numerical_columns)

            st.sidebar.title("Analysis Options")
            analysis_type = st.sidebar.selectbox("Select Analysis Type", ["Univariate", "Bivariate"])
        
        if analysis_type == "Univariate":
            univariate_analysis(df)
        elif analysis_type == "Bivariate":
            bivariate_analysis(df)

    else:
        st.warning("Please upload a dataset to proceed.")

# Run the app
if __name__ == "__main__":
    main()
