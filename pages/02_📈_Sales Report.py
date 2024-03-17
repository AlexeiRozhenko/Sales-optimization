import streamlit as st 
import pandas as pd
import plotly.express as px
import openpyxl, datetime
from datetime import date

st.set_page_config(page_title="Sales report", page_icon="📈")
st.header("Sales report")

def sales_chart(df, title):
  df_new = df.groupby([df['date']]).sum().reset_index()
  filter = (df_new["date"] >= d[0]) or (df_new["date"] <= d[1])
  df_new = df_new[filter]
  x_axis, y_axis = "date", "sales"
  fig = px.line(df_new, x=x_axis, y=y_axis, 
                title=title, height=350)
  st.plotly_chart(fig, use_container_width=True)

def pie_chart(df, values, names, title):
  colors=["#84A59D", "#F7EDE2", "#F6BD60", "#E0B498", "#BAC78E"]
  filter = (df["date"] >= d[0]) or (df["date"] <= d[1])
  df_new = df[filter]
  fig = px.pie(df_new, values=values, names=names, title=title, color_discrete_sequence=colors)
  fig.update_layout(showlegend=False,
    width=350,
    height=350,
    # legend=dict(
    # font=dict(size=10), 
    # entrywidth=70,
    # orientation="h",
    # y=-1,
    # x=0
    )
  fig.update_traces(textposition='inside')
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

  # choosing the suitable time interval
  min_date = datetime.date(2023, 1, 1)
  d = st.date_input(
  "Select the intervals",
  (min_date, date.today()),
  format="DD.MM.YYYY"
   )
  d = [i.strftime("%Y-%m-%d") for i in d]
  d = pd.to_datetime(d)
   
  # first row of graphs
  sales_chart(df, "Sales changes")

  # second row of graphs
  col1, col2, col3 = st.columns(3)
  with col1:
     pie_chart(df, "sales", "city", "Sales by city")
  
  with col2:
     pie_chart(df, "sales", "customer_type", "Sales by customers")
  
  with col3:
     pie_chart(df, "sales", "product_line", "Sales by product lines")


