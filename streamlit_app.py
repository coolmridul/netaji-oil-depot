import streamlit as st
import pandas as pd
import numpy as np
from app import *
import requests
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")
hide_github_icon = """
<style>
#MainMenu {
  visibility: hidden;
}
<style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


st.title("PAYMENT TAKADA")

df1=pd.read_excel('list.xlsx')
df2=pd.read_excel('final.xlsx')


col1, col2, col3 = st.columns(3)

with col1:
    option = st.selectbox(
        "Broker",df1['Broker'].to_list(),
    )
with col2:
    option1 = st.text_input("Party Name")
    # option1 = st.selectbox(
    #     "Party",("D K ", "Home phone", "Mobile phone"),
    # )
with col3:
    option2 = st.text_input("Amount: ")

col6, col7, col8 = st.columns(3)

with col6:
    option4 = st.date_input("Invoice Date",format="DD/MM/YYYY")
with col7:
    option5 = st.text_input("Invoice Number")

df9 = df1[df1['Broker'] == option].reset_index()

st.write("Email: ")
st.code(df9['Email'].iloc[0], language="markdown")
st.write("Number: ")
st.code(df9['Number'].iloc[0], language="markdown")

if st.button("Submit",type="primary"):
    data = pd.DataFrame([{"Broker":option,"Party":option1,"Amount":option2,"IDate":option4,"INumber":option5}])
    with pd.ExcelWriter('final.xlsx', engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:
        data.to_excel(writer, sheet_name='Sheet1', index=False, header=None, startrow= writer.sheets['Sheet1'].max_row)
    
    df2=pd.read_excel('final.xlsx')
    # data.to_excel('final.xlsx',index = False, header= None,startrow=df2.shape[0]+1)



st.header("PENDING LIST")

df2['is_widget'] = False
# column_configuration = {
#     'Command': st.button('Send SMS')
# }
# st.data_editor(df2,column_config=column_configuration)

edited_df = st.data_editor(df2,disabled=("Amount","Party","Broker"),use_container_width=True)
# st.write(df2)

col4, col5 = st.columns(2)

with col5:
    if st.button("Send SMS",type="primary"):
        st.write("Not Enabled")
with col4:
    if st.button("Send Email",type="primary"):
        edited_df1=edited_df[edited_df['is_widget'] == True].reset_index()
        if edited_df1.shape[0]:
            for i in range(0,edited_df1.shape[0]):
                df10 = df1[df1['Broker'] == edited_df1['Broker'].iloc[i]].reset_index()
                send_email(subject,edited_df1['Amount'].iloc[i],edited_df1['Party'].iloc[i], sender, [df10['Email'].iloc[0]], password)
                st.write("Sent Mail")
        else:
            st.write("Select from above")

df2['Amount'] = df2['Amount'].astype('int')
df20 = df2.groupby('Broker')['Amount'].sum().reset_index().sort_values('Amount',ascending=False).reset_index(drop=True)
# df20['test'] = df20['Broker'] + " : " + df20['Amount'].astype(str)
# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = df20['Broker'].tolist()
# sizes = df20['Amount'].tolist()
# new_lendgent = df20['test'].tolist()


# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, startangle=180)
# ax1.legend(new_lendgent, loc='lower left', bbox_to_anchor=(-0.1, 1.),fontsize=8)

# st.pyplot(fig1)
st.dataframe(df20)