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
      data = data_processing(data)
      if prediction_type == "All":
        for model_name in ["RF", "GBC", "ABC"]:
          prediction = predict_phishing(url, model_name, data)
          output.text += f"{model_name}: {prediction}\n"
      else:
        prediction = predict_phishing(url, model_name)
        output.text = prediction