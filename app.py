import streamlit as st
import pickle
import joblib
# import nltk
import sklearn
import pandas as pd

st.title("movies recommendation system")

# streamlit run app.py
with open("movies.pickle",'rb')as m:
  movies=pickle.load(m)


similarity=joblib.load('similarities.joblib')

movies_names=movies['title'].values

def recommend(name_movies):
    
    movie_index = movies[movies['title'] == name_movies].index[0]

    recommendations = similarity[movie_index]

    movies_list = sorted(
        enumerate(recommendations),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    recommended_movies=[]

    for i in movies_list:
         recommended_movies.append(movies.iloc[i[0]]['title'])
        
    return recommended_movies






name_movies=st.selectbox("enter the movies name:",movies_names)


if  st.button('recommend'):
  r=recommend(name_movies)
  st.write(" The Recommanded Movies Are :- ")

  for i in r:
     st.write(i)