# Phishing Website Detection App

This Streamlit application allows you to check if a website is likely phishing by analyzing its URL. 

**Features:**

* Enter a website URL.
* Select a prediction model (All, Random Forest, Gradient Boosting, AdaBoost).
* Get a prediction on whether the website is classified as "Phishing" or "Benign".
* Optionally, see predictions from all three models.

**Requirements:**

* Python
* Streamlit library (`pip install streamlit`)
* Scikit-learn library (`pip install scikit-learn`)
* Pre-trained phishing website detection models (replace placeholders in code)
* Pandas library (likely already installed)

**Instructions:**

1. Clone or download this repository.
2. Install required libraries using `pip install -r requirements.txt` (if requirements.txt exists).
3. Replace the placeholder functions (`load_model` and `predict_phishing`) in `main.py` with your actual model loading and prediction logic. 
    * Ensure your models are saved in a format compatible with scikit-learn.
    * The `predict_phishing` function should take the URL and a loaded model as input and return a prediction ("Phishing" or "Benign").
4. Run the app using `streamlit run main.py`.

**Note:**

* This is a basic example for educational purposes only. 
* Train your own phishing detection models on a relevant dataset before deployment in a real-world setting.
* This app should not be solely relied upon for real-world phishing detection.
