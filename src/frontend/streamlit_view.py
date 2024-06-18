import streamlit as st

from src.backend.phising_detector import data_processing, predict_phishing

def phising_url_view(data):
    
  # Title and description
  st.title("Phishing Website Detection App")
  st.write("Enter a website URL to check if it's likely phishing.")

  # Form elements
  url = st.text_input("Enter URL:")
  prediction_type = st.selectbox("Prediction Model:", ("All", "RF", "GBC", "ABC"))
  output = st.text_area("Phishing Prediction:", "", height=100, disabled=True)

  # Prediction logic based on selection
  if st.button("Predict"):
    if url:
      data, Scaler = data_processing(data)
      if prediction_type == "All":
        model_number = 0
        for model_name in ["RF", "GBC", "ABC"]:
          prediction = predict_phishing(url, model_name, data, Scaler)
          output.text += f"{model_name}: {display_prediction(prediction[model_number])}\n"
          model_number += 1
      else:
        prediction = predict_phishing(url, prediction_type, data, Scaler)
        output.text = f"{prediction_type}: {display_prediction(prediction)}\n"
        
def display_prediction(prediction):
    if prediction == 0:
        return "Benign!"
    elif prediction == 1:
        return "Phishing!"
    else:
        return "Incorrect Format!"
