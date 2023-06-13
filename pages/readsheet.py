import streamlit as st
import pandas

url='https://docs.google.com/spreadsheets/d/1t1Eux_WcHefWBrlfa_J-xqkyedjRNs_1FO_LonvOiAM/gviz/tq?tqx=out:csv&sheet=2013';

st.markdown("# Read Google spreadsheet 🎉")
st.sidebar.markdown("# Read Google sheet 🎉")

data = pandas.read_csv(url)
st.write(data)

