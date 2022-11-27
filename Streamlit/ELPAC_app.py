#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ELPAC_APP
import streamlit as st
import pandas as pd
import joblib
import sklearn
from sklearn import preprocessing
import numpy as np


st.write("""

# PREDICTION OF ELPAC LEVELS APP

This app predicts the ELPAC scores level for the students. 
In addtion, the app will also generate the probability of the predicted Level.

""")



# Dropdown input
School_deID = st.selectbox("Select Your School ID", ('0','1','2','3','4','5','6','7','8','9'))

GradeLevel = st.selectbox('Select Grade Level',('0','1','2','3','4','5','6'))

StudentGender = st.selectbox('Select Student Gender',('Female','Male'))

StudentEthnicity = st.selectbox('Select Student Ethnicity', ('Am Indian/Alskn Nat','Asian','Black/African Am','Filipino','Hispanic',
                                      'Missing','Multiple','Nat Hwiin/Othr Pac Islndr','White'))


Special_Education = st.selectbox('Select If Student Needs Special Education',('Yes','No'))

Homeless = st.selectbox('Select If Student Is Homelessness',('Yes','No'))

SocioEconomically = st.selectbox('Select If Student Is SocioEconomically',('Yes','No'))

TestDayName = st.selectbox('Select Test Day',('Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'))

OverallScore = st.number_input('Enter OverallScore')

ExpectedAttendanceDays = st.number_input('Enter Expected Attendance Days')

DaysAttended = st.number_input('Enter Days Attended')



# If button is pressed
if st.button("Predict"):
    
    model = joblib.load('ELPAC_model.pkl')
    
    #Store inputs into dataframe
    X = pd.DataFrame([[School_deID, GradeLevel, StudentGender, StudentEthnicity, Special_Education, Homeless,
                       SocioEconomically, TestDayName, OverallScore, ExpectedAttendanceDays, DaysAttended]],
                     columns = ['School_deID', 'GradeLevel', 'StudentGender', 'StudentEthnicity', 'Special_Education', 'Homeless', 'SocioEconomically',
                                'TestDayName', 'OverallScore', 'ExpectedAttendanceDays', 'DaysAttended'])
    
    #Yes: 1, No: 0 
    X = X.replace(['Male','Female'],[1, 0])    #label encoding of StudentGender and TeacherEthnicity
    X = X.replace(['Am Indian/Alskn Nat','Asian','Black/African Am','Filipino','Hispanic','Missing','Multiple',
                   'Nat Hwiin/Othr Pac Islndr','White'],
                  [0,1,2,3,4,5,6,7,8])
    X = X.replace(['No','Yes'], [0,1])
    X = X.replace(['Friday','Monday','Saturday','Sunday','Thursday','Tuesday','Wednesday'],
                  [0,1,2,3,4,5,6])

  
    # Get prediction
    prediction = model.predict(X)[0]
    prediction_prob = model.predict_proba(X)
    
        

    df = pd.DataFrame({
                    'PREDICTED LEVEL': prediction,
                    'PROBABILITY': [round(np.max(prediction_prob[0])*100,2)]
                    })
    st.write(df)

    


# In[ ]:




