import numpy as np
import pickle
import streamlit as st

model = pickle.load(open("minmaxscaler.pkl", "rb"))
ms = pickle.load(open("standscaler.pkl", "rb"))
sc = pickle.load(open("model.pkl", "rb"))

def crop_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    
    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        return f'{crop} is the best crop to be cultivated right there'
    else:
        return 'Sorry, we could not determine the best crop to be cultivated with the provided data.'

def main():
    st.title('Future Crop prediction')
    
    nitrogen = st.text_input('Value of N')
    phosphorus = st.text_input('Value of P')
    potassiumn = st.text_input('Value of K')
    temperature = st.text_input('Value of Temperature')
    humidity = st.text_input('Value of Humidity')
    ph = st.text_input('Value of pH')
    rainfall = st.text_input('Rainfall')
    
    detector = ''
    
    if st.button('The best crop to be cultivated'):
        detector = crop_prediction([nitrogen, phosphorus, potassiumn, temperature, humidity, ph, rainfall])
    
    st.success(detector)

if __name__ == '__main__':
    main()

    