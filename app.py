import pickle
import streamlit as st
import pandas as pd
import requests
import os
import zipfile

zip_path = "utils/similarity.zip"
extract_path = "utils/similarity.pkl"
if not os.path.exists(extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("utils")

movies_list = pickle.load(open('utils/movies.pkl','rb'))
similarity = pickle.load(open('utils/similarity.pkl','rb'))
movies = pd.DataFrame(movies_list)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=472928e765a79bd1196b861c20651dea&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_posters.append(fetch_poster(movie_id))
        recommended_names.append(movies.iloc[i[0]].title)
    return recommended_names,recommended_posters

st.title('MOVIE RECOMMEND SYSTEM')

selected_movie_name = st.selectbox(
    'What movie do you want to have a recommend?',
    movies.title
)

if st.button('Show Recommendation'):
    recommended_names, recommended_posters = recommend(selected_movie_name)

    st.image(
        recommended_posters,
        caption=recommended_names,
        width=140
    )