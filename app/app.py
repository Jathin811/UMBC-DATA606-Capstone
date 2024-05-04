import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

DATA_URL = (
    r"C:\Users\jathi\Downloads\Motor_Vehicle_Collisions.csv"
)

st.title("Exploring Motor Vehicle Collisions in a Big City")
st.markdown("This app is a Streamlit dashboard for analyzing motor vehicle collisions in a big city")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH DATE', 'CRASH TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lower_case = lambda x: str(x).lower()
    data.rename(lower_case, axis='columns', inplace=True)
    data.rename(columns={'crash date_crash time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)
original_data = data

st.header("Where Do the Most People Expected Get Hurt in a Big City?")
injured_people = st.slider("Number of people injured in vehicle collisions", 0, 19)
filtered_data = data[data['number of persons injured'] >= injured_people]
st.map(filtered_data[["latitude", "longitude"]].dropna(how="any"))

st.header("How Many Collisions Are Expected to Occur During a Given Time of Day?")
hour = st.slider("Choose an hour", 0, 23)
data = data[data['date/time'].dt.hour == hour]

st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (np.average(data['latitude']), np.average(data['longitude']))
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state = {
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50
    },
    layers = [
        pdk.Layer(
            "HexagonLayer",
            data = data[['date/time', 'latitude', 'longitude']],
            get_position=['longitude', 'latitude'],
            radius=100,
            extruded=True,
            pickable=True,
            elevation_scale=4,
            elevation_range=[0, 1000],
        ),
    ],
))

st.subheader("Breakdown by Minute Between %i:00 and %i:00" % (hour, (hour + 1) % 24))
filtered = data[
    (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour + 1))
]
hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({'minute': range(60), 'collisions': hist})
fig = px.bar(chart_data, x='minute', y='collisions', hover_data=['minute', 'collisions'], height=400)
st.write(fig)

st.header("Top 5 Risky Streets by Types of Affected Categories")
select = st.selectbox('Affected categories', ['Pedestrians', 'Cyclists', 'Motorists'])

if select == 'Pedestrians':
    original_data['number of pedestrians injured'] = original_data['number of pedestrians injured'].astype(int)
    st.write(original_data[original_data['number of cyclist injured'] >= 1][["on street name", "number of pedestrians injured"]].sort_values(by=['number of pedestrians injured'], ascending=False).dropna(how='any')[:5])

elif select == 'Cyclists':
    original_data['number of cyclist injured'] = original_data['number of cyclist injured'].astype(int)
    st.write(original_data[original_data['number of cyclist injured'] >= 1][["on street name", "number of cyclist injured"]].sort_values(by=['number of cyclist injured'], ascending=False).dropna(how='any')[:5])

else:
    original_data['number of motorist injured'] = original_data['number of motorist injured'].astype(int)
    st.write(original_data[original_data['number of motorist injured'] >= 1][["on street name", "number of motorist injured"]].sort_values(by=['number of motorist injured'], ascending=False).dropna(how='any')[:5])

if st.checkbox("Show raw data", False):
    st.subheader('Raw data')
    st.write(data)