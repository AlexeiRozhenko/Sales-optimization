import streamlit as st 
import pandas as pd
import plotly.express as px
import openpyxl
import os

st.set_page_config(page_title="Sales report", page_icon="📈")
st.header("Sales report")

def sales_chart(df, title):
  df_new = df.groupby([df['date']]).sum()
  df_new = df_new.reset_index()
  x_axis, y_axis = "date", "sales"
  fig = px.line(df_new, x=x_axis, y=y_axis, 
                title=title, height=350)
  st.plotly_chart(fig, use_container_width=True)

def pie_chart(df, values, names, title):
  colors=["#84A59D", "#F7EDE2", "#F6BD60", "#575761", "#CF8BA9"]
  fig = px.pie(df, values=values, names=names, title=title, color_discrete_sequence=colors)
  fig.update_layout(
    width=280,
    height=280
  )
  st.plotly_chart(fig, use_container_width=True)
  
with st.sidebar:
  with open('sample_table.xlsx','rb') as file:
    st.download_button(label= 'Download Sample File',
              file_name='sample_table.xlsx',
              data=file,
              use_container_width=False)
  uploaded_file = st.file_uploader("Choose an XLSX file", accept_multiple_files=False)
  
if uploaded_file is not None:
  
  df = pd.read_excel(uploaded_file)
  df['date'] = pd.to_datetime(df['date'])
  df.sort_values(by='date')
  df = df.astype({"sales": float, "unit_price": float, "quantity": int})
  
  with st.expander("Data preview"):
    st.dataframe(df.head())

  #first row of graphs
  sales_chart(df, "Sales changes")

  #second row of graphs
  col1, col2, col3 = st.columns(3)
  with col1:
     pie_chart(df, "sales", "city", "Sales by city")
  
  with col2:
     pie_chart(df, "sales", "customer_type", "Sales by customers")
  
  with col3:
     pie_chart(df, "sales", "product_line", "Sales by product lines")


