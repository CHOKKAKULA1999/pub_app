
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt



# Load the pub dataset
pub_data = pd.read_csv('E:\\INTERSHIP_TASKS\\PUB_APPLICATION\\open_pubs.csv', header=None)
pub_data.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

# Replace \N values with NaN
pub_data = pub_data.replace('\\N', np.nan)

# Drop rows with NaN values
pub_data = pub_data.dropna()

pub_data['longitude'] = pd.to_numeric(pub_data['longitude'], errors='coerce')
pub_data['latitude'] = pd.to_numeric(pub_data['latitude'], errors='coerce')




# Add some styling to the title and subtitle
st.markdown("<h1 style='text-align: center; color: #EB6864; font-weight: bold;'> 👯‍♂️ 💃 OPEN PUB APP BY SUNDAR  🍗</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #5243AA;'>WELCOME TO THE PUB APP THAT FINDS THE PUBS NEAR YOU 🕺 </h2>", unsafe_allow_html=True)

# Add an image of a pub
st.image('pub.jpg', use_column_width=True)

# Display some basic information about the dataset
st.write(f"The dataset contains **{len(pub_data)}** pub locations.")
st.write(f"The dataset covers **{len(pub_data['local_authority'].unique())}** local authorities.")
st.markdown("<h2 style='text-align: center; color: #7F45FA;'>PUB DATA 🕺 </h2>", unsafe_allow_html=True)
st.markdown("<style>div.stDataFrame div[data-testid='stHorizontalBlock'] div[data-testid='stDataFrameContainer'] {margin: 0 auto;}</style>", unsafe_allow_html=True)
st.write(pub_data)




# CREATING THE SCATTER PLOT OF THE PUB LOCATIONS WITH SIZE AND COLOR BASED ON THE NUMBER OF PUBS IN EACH LOCAL AUTHORITY 
pub_locations = pub_data[["latitude",'longitude', 'local_authority']].dropna()
local_authority_pubs = pub_locations['local_authority'].value_counts()
pub_locations['size'] = pub_locations['local_authority'].apply(lambda x:local_authority_pubs[x])
pub_locations['color'] = pub_locations['local_authority'].apply(lambda x:local_authority_pubs[x])
fig =px.scatter_mapbox(pub_locations ,lat = 'latitude' , lon = "longitude", color = 'color' , size = 'size' ,zoom= 10 , height =600)
fig.update_layout(
    mapbox_style ='carto-darkmatter',
    title = ' PUB LOCATIONS BY COLORED  AND SIZE BY LOCAL_AUTHORITY',
    margin = dict(l=0 , r =0 , t=40 , b=0),   
)
st.plotly_chart(fig)

#  Display some statistics about the dataset
st.write("Here are some statistics about the dataset:")
# st.write(pub_data.describe())
#stats = pub_data.describe().T
#stats['count'] = stats['count'].astype(int)
#stats = stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
#st.dataframe(stats.style.highlight_max(axis=0, color='#EB6864'))

#creating a bar plot of the 10 local authorities with the most  pubs
loacl_authority_pubs = pub_data['local_authority'].value_counts().nlargest(10)
fig = px.bar(loacl_authority_pubs , x =loacl_authority_pubs.index , y =loacl_authority_pubs.values)
fig.update_layout(
    xaxis_title = "LOCAL_AUTHORITY",
    yaxis_title = "NUMBER OF PUBS",
    title = "TOP 10 LOCAL_AUTHORITY WITH THE MOST PUBS",
    template = "plotly_dark"
)
st.plotly_chart(fig)



# Add a fun fact about pubs in the UK
#st.markdown("<br><br>", unsafe_allow_html=True)
#st.write("🤓 Fun fact: Did you know that the oldest pub in the UK, Ye Olde Fighting Cocks, is over 1,200 years old and located in St Albans, England? 🏰")


st.balloons()
# Add a footer with some information about the app
#st.markdown("<hr>", unsafe_allow_html=True)
#st.write("Data source: https://www.getthedata.com/open-pubs")
#st.sidebar.image('banner_top.png', use_column_width=True)
