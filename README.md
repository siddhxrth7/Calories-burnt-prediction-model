#  Calorie Burnt Prediction & Analytics Pipeline

### **Project Overview**
This is an end-to-end Machine Learning application designed to predict calories burned during physical activity based on physiological parameters.  the project demonstrates a complete data lifecycle—from exploratory analysis in Jupyter Notebooks to a live, interactive web application.



### **🚀 Key Features**
* **Predictive Modeling:** Utilizes an **XGBoost Regressor** for high-accuracy calorie estimation based on user features.
* **Live Data Logging:** Integrated with **SQLite** to automatically log every user prediction (Gender, Age, Heart Rate, etc.) in real-time.
* **Interactive Analytics:** A built-in dashboard within the app allows for the visualization of historical session data and user trends.
* **Streamlit Deployment:** Optimized for cloud hosting, providing a public URL for instant accessibility.

---

### **🛠️ Tech Stack**
* **Language:** Python 3.9
* **ML Libraries:** XGBoost, Scikit-Learn
* **Data Handling:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Web Framework:** Streamlit
* **Database:** SQLite3

---

### **📁 Repository Structure**
```text
├── data/               # Raw exercise and calorie datasets
├── models/             # Serialized XGBoost model (.pkl)
├── notebooks/          # Exploratory Data Analysis (EDA) & Training logic
├── src/                # Production source code
│   └── app.py          # Main Streamlit application & Database logic
└── requirements.txt    # Project dependencies
```
# ⚙️ Installation & Local Usage
- 1. Clone the repository:

```Bash
git clone https://github.com/siddhxrth7/Calories-burnt-prediction-model.git
cd Calories-burnt-prediction-model
```
- 2. Run the application:

```Bash
pip install -r requirements.txt
streamlit run src/app.py
```
# 📊 Data Engineering Highlights


A core component of this project is the Data Feedback Loop. By using SQLite, the application transforms a simple prediction tool into a data collection system. This architectural choice allows for:

Feature Monitoring: Tracking the range of inputs provided by real users.

Dataset Expansion: Gathering new, real-world data points for future model retraining (v2.0).

Audit Trails: Maintaining a transparent log of all model inferences with timestamps.


