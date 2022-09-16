import pickle
import streamlit as st
pickle_in=open('Iris.pkl','rb')
model=pickle.load(pickle_in)
a=st.number_input('Enter sepal width')
b=st.number_input('Enter sepal length')
c=st.number_input('Enter petal width')
d=st.number_input('Enter petal length')
result=''

if st.predict('PREDICT'):
   result=st.predict([[a,b,c,d]])
   st.success(result)


