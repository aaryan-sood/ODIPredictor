import streamlit as st
import joblib
import pandas as pd

teams = ['India',
 'England',
 'New Zealand',
 'Australia',
 'Sri Lanka',
 'South Africa',
 'Bangladesh',
 'Pakistan',
 'Nepal',
 'Afghanistan',
 'West Indies',
 'Scotland',
 'United Arab Emirates',
 'Oman',
 'Netherlands',
 'Zimbabwe',
 'United States of America',
 'Ireland',
 'Canada',
 'Namibia',
 'Papua New Guinea',
 'Hong Kong',
 'Kenya']

cities = ["Aberdeen", "Abu Dhabi", "Ahmedabad", "Al Amarat", "Amstelveen", "Antigua",
"Auckland", "Ayr",  

"Belfast", "Bengaluru", "Birmingham", "Bready", "Brisbane", "Bristol", "Bulawayo", "Barbados",
"Benoni", 

"Cairns", "Cape Town", "Cardiff", "Centurion", "Chandigarh", "Chattogram", "Chester-le-Street", "Chennai", "Chittagong", "Christchurch",
"Colombo", "Cuttack", "Canberra", "Cape Town",

"Darwin", "Dehra Dun", "Delhi", "Dhaka", "Dharamsala", "Dharmasala", "Dubai", "Dublin", "Dunedin", "Durban",
"Deventer", "Dominica",  

"East London", "Edinburgh",

"Faisalabad", "Fatullah", "Glasgow", "Greater Noida", "Grenada", "Guyana", "Gwalior",
"Gros Islet", 

"Hamilton", "Hambantota", "Harare", "Hobart", "Hong Kong", "Hyderabad",

"Indore", "Jaipur", "Jamaica", "Johannesburg", "Kanpur", "Karachi", "Kandy", "Khulna", "Kimberley", "King City", "Kingston", "Kirtipur", "Kochi", "Kolkata",
"Kuala Lumpur",

"Lahore", "Lauderhill", "Leeds", "Lincoln", "London", "Lucknow",

"Manchester", "Margao", "Melbourne", "Mount Maunganui", "Multan", "Mirpur", "Mumbai",
"Nagpur", "Nairobi", "Napier", "Nelson", "North Sound", 

"Paarl", "Pearland", "Perth", "Port Elizabeth", "Port Moresby", "Port of Spain", "Potchefstroom", "Providence", "Pune",

"Rajkot", "Ranchi", "Rawalpindi", "Rotterdam", "Raipur",

"Sind", "Sharjah", "Southampton", "St Kitts", "St Lucia", "St Vincent", "St George's", "Sydney", "Sylhet",

"Taunton", "Tarouba", "Thiruvananthapuram", "Toronto", "Townsville", "Trinidad",

"Utrecht", 

"Vadodara", "Visakhapatnam",

"Wellington", "Whangarei", "Windhoek",


]

st.title('ODI Win Predictor')
col1,col2=st.columns(2)

pipe=joblib.load('pipe.joblib')


with col1:
    batting_team=st.selectbox('Select The batting Team',teams)
with col2:
    bowling_team=st.selectbox('Select the bowling team',teams)
if batting_team == bowling_team:
    st.warning("Teams should not be the same. Please enter different team.")
    butcon=1
else: 
    butcon=0
selected_city=st.selectbox('Select host City',cities)

target=st.number_input('target',value=1, step=1, min_value=1)

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('Score',value=0, step=1,max_value=target-1, min_value=0)

with col4:
    overs=st.number_input('Overs Completed',value=1, step=1, max_value=49, min_value=1)

with col5:
    wickets=st.number_input('Wickets Out',value=0, step=1, max_value=9, min_value=0)

if st.button('predict probability',disabled=butcon) : 
    runs_left=target-score
    balls_left=300-(overs*6)
    wickets_left=10-wickets
    crr=score/overs
    rrr=runs_left/(50-overs)
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})


    result=pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")