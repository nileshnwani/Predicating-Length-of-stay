# 🏥 Predicting Length of Stay

This project aims to assist healthcare providers in estimating the **length of a patient's hospital stay** based on various factors. By leveraging **machine learning techniques**, the model helps in **better resource allocation** and **hospital planning**.

## 🚀 Features
- Accepts input details like **Location, Time, MRI Units, CT Scanners, and Hospital Beds**.
- Preprocesses the data using **one-hot encoding** and **feature scaling**.
- Trains a **Random Forest Regressor** to predict the **length of stay**.
- Interactive web application built using **Flask**.
- User-friendly **UI for input and result display**.

## 🛠 Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Database:** CSV File (Healthcare Investments & Hospital Stay Data)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nileshnwani/Predicating-Length-of-stay.git
   ```
   
2. Navigate to the project directory:
  ```bash
  cd predict-hospital-stay
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Run the Flask app:
  ```bash
  python app.py
  ```
5. Open http://127.0.0.1:5000/ in your browser.
 
## 📊 Model Details
-**Preprocessing:** One-hot encoding for categorical variables, StandardScaler for numerical features.<br>
-**Algorithm:** Random Forest Regressor<br>
-**Training Data:** Healthcare Investments & Hospital Stay Data.<br>

## 🎯 Usage
Enter **Location, Time, MRI Units, CT Scanners, and Hospital Beds**<br>
Click **Predict** to estimate the **length of hospital stay**<br>
The model will output the predicted stay duration in **days**<br>


<b>**Happy coding! 🚀**<b>


