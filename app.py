import streamlit as st
import pandas as pd
import joblib

st.title('Olympic Medals Predictor')

# Create input form
st.write('Enter team information:')

team = st.text_input('Team Code (e.g., USA, GBR)', '')
country = st.text_input('Country Name', '')
year = st.number_input('Year', 2024, 2040, 2024)
events = st.number_input('Number of Events', 0, 100, 0)
athletes = st.number_input('Number of Athletes', 0, 1000, 0)
age = st.number_input('Average Age', 0.0, 50.0, 0.0)
height = st.number_input('Average Height (cm)', 0.0, 250.0, 0.0)
weight = st.number_input('Average Weight (kg)', 0.0, 150.0, 0.0)
prev_medals = st.number_input('Previous Olympics Medals', 0.0, 1000.0, 0.0)
prev_3_medals = st.number_input('Average Medals (Last 3 Olympics)', 0.0, 1000.0, 0.0)

if st.button('Predict Medals'):
    try:
        # Load the model
        model = joblib.load('model.joblib')
        
        # Create input data
        input_data = pd.DataFrame([{
            'team': team,
            'country': country,
            'year': year,
            'events': events,
            'athletes': athletes,
            'age': age,
            'height': height,
            'weight': weight,
            'prev_medals': prev_medals,
            'prev_3_medals': prev_3_medals
        }])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        st.success(f'Predicted Medals: {prediction:.2f}')
    except Exception as e:
        st.error(f'Error: {e}') 