# import libraries
import streamlit as st 
from joblib import load
# from sklearn.preprocessing import StandardScaler

 # load the model from disk
loaded_model = load('../MyModelTrained/titanic_survival.joblib')

#Create Streamlit Web App
st.title("Titanic Survival Prediction")

# Sildebar
menu = ['Home','Prediction']
st.sidebar.selectbox('',menu)


#Scaling input data 

# scaler = StandardScaler()

#Inpyt components 
age = st.slider('Age', 0.42,80.0,30.0)
sibsp = st.slider('SibSp',0,8,0)
parch = st.slider('Parch',0,9,0)
fare = st.slider('Fare',0.0,512.30,32.20)

# st.write(age , sibsp, parch, fare)
# add prediction button 
prediction_button = st.button('Predict')

# prediction logic 
if prediction_button:
    input_data = [[age,sibsp,parch,fare]]
    prediction = loaded_model.predict(input_data)

    st.write(input_data)
    st.subheader('Prediction: ')
    if prediction[0] == 1:
        st.write('Survived')
    else:
        st.write('Did not survive')

    # Display prediction probability
    # st.subheader('Prediction Probability')
    # st.write

