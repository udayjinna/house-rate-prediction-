import streamlit as st
import pickle
import numpy as np
import json

# Load model and columns
model = pickle.load(open('model.pkl', 'rb'))
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]

# UI
st.title("🏡 Bangalore House Price Prediction")

location = st.selectbox("Location", sorted(locations))
total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
bath = st.slider("Number of Bathrooms", 1, 10, 2)
bhk = st.slider("BHK", 1, 10, 2)

# Predict function
def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location.lower() in data_columns:
        loc_index = data_columns.index(location.lower())
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)

# Button
if st.button("Predict"):
    price = predict_price(location, total_sqft, bath, bhk)
    st.success(f"💰 Estimated Price: ₹ {price} Lakhs")
