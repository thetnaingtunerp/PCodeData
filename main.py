import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

@st.cache_data
def load_data():
    v_df = pd.read_excel("VillageCode.xlsx")
    w_df = pd.read_excel("warddf.xlsx")
    return v_df, w_df

v_df, w_df = load_data()
#sidebar

state_name = st.sidebar.selectbox('Select Region', w_df['SR_Name_Eng'].unique())

township_name = st.sidebar.selectbox('Select Township', w_df[w_df['SR_Name_Eng'] == state_name]['Township_Name_Eng'].unique())



# metrics
total_villages = v_df[v_df['Township_Name_Eng'] == township_name]['Village_Name_Eng'].value_counts()
total_villages_tracts = v_df[v_df['Township_Name_Eng'] == township_name]['Village_Tract_Name_Eng'].nunique()
total_townships = w_df[w_df['SR_Name_Eng'] == state_name]['Township_Name_Eng'].nunique()
total_wards = w_df[w_df['Township_Name_Eng'] == township_name]['Ward_Name_Eng'].nunique()

# Township_Name_Eng
if township_name:
    total_wards = w_df[w_df['Township_Name_Eng'] == township_name]['Ward_Name_Eng'].nunique()
    total_villages_tracts = v_df[v_df['Township_Name_Eng'] == township_name]['Village_Tract_Name_Eng'].nunique()
    total_villages = v_df[v_df['Township_Name_Eng'] == township_name]['Village_Name_Eng'].nunique()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Townships", total_townships, border=True)
col2.metric("Total Wards", total_wards, border=True)
col3.metric("Total Villages", total_villages, border=True)
col4.metric("Total Village Tracts", total_villages_tracts, border=True)

#columns[1,3]
dt1, dt2, dt3 = st.columns(3)
with dt1:
    wards = w_df[w_df['Township_Name_Eng'] == township_name]['Ward_Name_MMR']
    st.write(wards.to_frame(name='ရပ်ကွက်ကြီးများ'))

with dt2:
    village_tracts = v_df[v_df['Township_Name_Eng'] == township_name]
    village_tracts = village_tracts['Village_Tract_Name_Eng'].drop_duplicates().reset_index(drop=True)
    st.write(village_tracts.to_frame(name='ကျေးရွာအုပ်စုများ'))

with dt3:
    villages = v_df[v_df['Township_Name_Eng'] == township_name]['Village_Name_MMR']
    villages = villages.drop_duplicates().reset_index(drop=True)
    st.write(villages.to_frame(name='ကျေးရွာများ'))