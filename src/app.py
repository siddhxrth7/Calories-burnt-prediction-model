import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sqlite3
import datetime


conn = sqlite3.connect('calorie_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user_logs 
             (timestamp TEXT, gender TEXT, age INT, height REAL, weight REAL, 
              duration REAL, heart_rate REAL, prediction REAL)''')
conn.commit()
conn.close()

try:
    with open('calories_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("⚠️ Error: 'calories_model.pkl' not found. Please run your Notebook first!")
    st.stop()


st.title("Calorie Burnt Predictor & Analytics")
st.write("Enter your exercise details below to get a live prediction.")

# Input Form
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 10, 100, 25)
    height = st.number_input("Height (cm)", 100, 250, 175)
    weight = st.number_input("Weight (kg)", 30, 150, 75)
with col2:
    duration = st.slider("Duration (min)", 1, 120, 30)
    heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 100)
    body_temp = st.number_input("Body Temp (°C)", 36.0, 42.0, 39.0)

# Prediction Logic
if st.button("Predict"):
    g_val = 1 if gender == "Male" else 0 
    
    features = np.array([[g_val, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(features)[0]
    
    st.success(f"🔥 You burnt approximately **{prediction:.2f} Calories**!")
    conn = sqlite3.connect('calorie_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_logs VALUES (?,?,?,?,?,?,?,?)", 
              (datetime.datetime.now(), gender, age, height, weight, duration, heart_rate, float(prediction)))
    conn.commit()
    conn.close()

# --- 5. ADMIN/ANALYTICS SECTION ---
st.markdown("---")
st.header("📊 Live User Analytics")
if st.checkbox("Show Dashboard"):
    conn = sqlite3.connect('calorie_data.db')
    df = pd.read_sql("SELECT * FROM user_logs", conn)
    conn.close()
    
    if not df.empty:
        st.write(f"Total Predictions Made: {len(df)}")
        st.dataframe(df.tail(5)) 
        st.bar_chart(df['age']) # Simple chart of user ages
    else:
        st.write("No data yet. Make a prediction first!")