import streamlit as st
import pandas as pd
import database
import chart

st.title('Abandonded Wells')
st.text('An interactive map that can used for geothermal energy')

st.sidebar.title('Select well parameters')

depth = st.sidebar.number_input("Minimum depth (m)", min_value=0, value=500)
gradient= st.sidebar.number_input('Minimum thermal gradient', min_value=0.0, value=0.05, format='%.03f', step=0.001)

data = database.get_wells(depth, gradient)
df = pd.DataFrame(data).dropna()
graph = chart.plot_wells(df)

st.altair_chart(graph)