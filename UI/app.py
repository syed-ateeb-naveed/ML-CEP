import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained pipeline model
model = joblib.load('model_pipeline.pkl')

# Title of the web app
st.title('Car Price Prediction')

# Form for user input
with st.form(key='prediction_form'):
    car_model = st.text_input('Car Model')
    brand = st.text_input('Brand')
    year = st.number_input('Year', min_value=1900, max_value=2024, step=1)
    km_driven = st.number_input('Kilometers Driven', min_value=0)
    fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
    
    submit_button = st.form_submit_button(label='Predict')

# Prediction and displaying the result
import pandas as pd

try:
  if submit_button:
    # Validate user input (replace with your specific validation logic)
    if not isinstance(car_model, str):
      raise ValueError("Car model must be a string.")
    if not isinstance(brand, str):
      raise ValueError("Brand must be a string.")
    if not isinstance(year, int) or year < 1900:
      raise ValueError("Year must be a valid integer greater than or equal to 1900.")
    if not isinstance(km_driven, (int, float)) or km_driven < 0:
      raise ValueError("Kilometers driven must be a non-negative number.")
    if not isinstance(fuel_type, str):
      raise ValueError("Fuel type must be a string.")

    # Create DataFrame with validated entries
    user_input = pd.DataFrame([[car_model, brand, year, km_driven, fuel_type]],
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    # Make prediction using your model
    prediction = model.predict(user_input)
    st.write(f'The predicted price of the car is: ${prediction[0]:,.2f}')

except (ValueError, Exception) as e:  # Catch both specific and general exceptions
  # Provide informative error message to the user
  st.error(f"Error: {str(e)}")
  st.write("Please ensure your entries are valid.")
