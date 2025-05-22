import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_all_data, compare_countries

# Configure absolute path
CLEANED_DATA_PATH = r"C:/Users/jilow/OneDrive/Documents/Cleaned-data"

def load_data(country):
    """Load data from Cleaned-data directory"""
    filename = f"{country.lower().replace(' ', '_')}_clean.csv"
    filepath = os.path.join(CLEANED_DATA_PATH, filename)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Missing data file: {filename}")
    
    return pd.read_csv(filepath)

def country_view():
    """Main country analysis tab"""
    st.header("Country Analysis")
    
    # Country selection
    countries = ["Benin", "Sierra Leone", "Togo"]
    selected = st.selectbox("Choose Country", countries)
    
    try:
        df = load_data(selected)
        
        # Metrics
        st.subheader(f"Performance Metrics: {selected}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Avg GHI", f"{df['GHI'].mean():.1f} W/m²")
        col2.metric("Peak Temp", f"{df['Tamb'].max():.1f} °C")
        col3.metric("Wind Speed", f"{df['WS'].median():.1f} m/s")

        # Visualization
        st.subheader("Solar Analysis")
        plot_choice = st.radio("View Mode", ["Time Series", "Distribution"])
        
        if plot_choice == "Time Series":
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df.set_index('Timestamp', inplace=True)
            st.line_chart(df[['GHI', 'DNI', 'DHI']])
        else:
            fig, ax = plt.subplots()
            sns.histplot(df['GHI'], kde=True, ax=ax)
            st.pyplot(fig)
            
    except FileNotFoundError as e:
        st.error(str(e))
        st.image("https://media.giphy.com/media/3o7aTskHEUdgCQAXde/giphy.gif", width=300)

def comparison_view():
    """Cross-country comparison tab"""
    st.header("Comparative Analysis")
    
    try:
        data = load_all_data(CLEANED_DATA_PATH)
        comparison_df = compare_countries(data)
        
        st.subheader("Statistical Summary")
        st.dataframe(comparison_df.style.format("{:.1f}"))
        
        st.subheader("GHI Distribution Comparison")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(
            data=[data['benin']['GHI'], 
                  data['sierra_leone']['GHI'], 
                  data['togo']['GHI']],
            ax=ax
        )
        ax.set_xticklabels(["Benin", "Sierra Leone", "Togo"])
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Comparison error: {str(e)}")

def main():
    st.title("🌞 West Africa Solar Potential Dashboard")
    tab1, tab2 = st.tabs(["Country Analysis", "Cross-Comparison"])
    
    with tab1:
        country_view()
    with tab2:
        comparison_view()

if __name__ == "__main__":
    main()