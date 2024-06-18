import streamlit as st

from src.backend.phising_detector import data_processing, predict_phishing

def phising_url_view(data):
    
  # Title and description
  st.title("Phishing Website Detection App")
  st.write("Enter a website URL to check if it's likely phishing.")

  # Form elements
  url = st.text_input("Enter URL:")
  prediction_select = st.selectbox("Prediction Model:", ("All", "RF", "GBC", "ABC"))

  # Prediction logic based on selection
  if st.button("Predict"):
    if url:
      st.markdown("***Phishing Prediction Result***")
      data, Scaler = data_processing(data)
      if prediction_select == "All":
        model_number = 0
        for prediction_name in ["RF", "GBC", "ABC"]:
          prediction = predict_phishing(prediction_name, url, data, Scaler)
          st.text(f"{prediction_name}: {display_prediction(prediction)}\n")
          model_number += 1
      else:
        prediction = predict_phishing(prediction_select, url, data, Scaler)
        st.text(f"{prediction_select}: {display_prediction(prediction)}\n")
        
def display_prediction(prediction):
    if prediction == 0:
        return "Benign!"
    elif prediction == 1:
        return "Phishing!"
    else:
        return "Incorrect Format!"
