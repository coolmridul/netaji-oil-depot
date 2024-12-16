import streamlit as st
import pandas as pd
import numpy as np
from app import *


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

df9 = df1[df1['Broker'] == option].reset_index()

st.write("Email: ")
st.code(df9['Email'].iloc[0], language="markdown")
st.write("Number: ")
st.code(df9['Number'].iloc[0], language="markdown")

if st.button("Submit",type="primary"):
    data = pd.DataFrame([{"Broker":option,"Party":option1,"Amount":option2}])
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