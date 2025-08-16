# import pickle
# import streamlit as st
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     data = requests.get(url).json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#     return recommended_movie_names, recommended_movie_posters
#
# st.header('Movie Recommender System')
#
# # Load data
# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)  # FIXED
# similarity = pickle.load(open('similarity.pkl','rb'))
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )
#
# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)  # FIXED
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])

import pickle
import streamlit as st
import pandas as pd
import requests
import os
import urllib.request

# --- Function to download files from Hugging Face ---
def download_file(url, filename):
    if not os.path.exists(filename):
        with st.spinner(f"Downloading {filename}..."):
            urllib.request.urlretrieve(url, filename)
        st.success(f"{filename} downloaded!")

# --- URLs of your files on Hugging Face ---
MOVIE_DICT_URL = "https://huggingface.co/datasets/Arifcourse25/my-movie-dataset/resolve/main/movie_dict.pkl"
SIMILARITY_URL = "https://huggingface.co/datasets/Arifcourse25/my-movie-dataset/resolve/main/similarity.pkl"

# --- Download the files (only if not already present) ---
download_file(MOVIE_DICT_URL, "movie_dict.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")

# --- Load Data ---
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# --- TMDB API poster fetch ---
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# --- Recommender ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# --- Streamlit UI ---
st.header('🎬 Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])

