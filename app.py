# Save this as app.py and run with `streamlit run app.py`
import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv("meta_app_manager_large_dataset.csv")  # 🔁 Update path if file is elsewhere

# Page title
st.title("📱 App Usage Dashboard")

# Event Type Distribution
st.write("## Event Type Distribution")
event_counts = df['Event Type'].value_counts()
st.bar_chart(event_counts)

# Update Status by Network Type
st.write("## Update Status by Network Type")
update_status_by_network = df.groupby('Network Type')['Update Status'].value_counts().unstack().fillna(0)
st.bar_chart(update_status_by_network)
