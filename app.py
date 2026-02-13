import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Trader Performance vs Market Sentiment Dashboard")

# Load data (use your merged dataset)
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_merged_data.csv")
    return df

merged = load_data()

# Sidebar filter
sentiment_option = st.sidebar.selectbox(
    "Select Sentiment",
    merged['classification'].unique()
)

filtered = merged[merged['classification'] == sentiment_option]

st.subheader("Performance Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(filtered['Closed PnL'].mean(), 2))
col2.metric("Win Rate", round((filtered['Closed PnL'] > 0).mean(), 2))
col3.metric("Total Trades", len(filtered))

# PnL Distribution
st.subheader("PnL Distribution")

fig, ax = plt.subplots()
sns.histplot(filtered['Closed PnL'], bins=50, ax=ax)
st.pyplot(fig)

# Trade Size vs Win Rate Scatter
st.subheader("Trade Size vs PnL")

fig2, ax2 = plt.subplots()
sns.scatterplot(
    x=filtered['Size USD'],
    y=filtered['Closed PnL'],
    ax=ax2
)
st.pyplot(fig2)

st.markdown("---")
st.markdown("This dashboard allows interactive exploration of sentiment-based performance patterns.")
