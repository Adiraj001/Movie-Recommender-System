import pickle
import streamlit as st
import base64
import os
from sklearn.neighbors import NearestNeighbors

final_movies_path = 'artifacts/FinalMovies.pkl'
cv_path = 'artifacts/cv.pkl'

@st.cache_resource(show_spinner=False)
def load_data():
    with open(final_movies_path, 'rb') as f:
        movies = pickle.load(f)
    with open(cv_path, 'rb') as f:
        cv = pickle.load(f)
    vectors = cv.transform(movies['tag'])
    nn = NearestNeighbors(metric='cosine', algorithm='brute')
    nn.fit(vectors)
    return movies, cv, vectors, nn

movies, cv, vectors, nn = load_data()

def recommend(movie_title, n_recommendations=5):
    idx = movies[movies['title'].str.lower() == movie_title.lower()].index
    if len(idx) == 0:
        st.write("Movie not found in the dataset.")
        return []
    idx = idx[0]
    distances, indices = nn.kneighbors(vectors[idx], n_neighbors=n_recommendations+1)
    recommended_movies = []
    for i in range(1, n_recommendations+1):
        movie_idx = indices[0][i]
        recommended_movies.append(movies.iloc[movie_idx]['title'])
    return recommended_movies

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


img_path = 'assets/background.jpg'
if os.path.exists(img_path):
    img_base64 = get_base64_of_bin_file(img_path)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stHeader {{
        font-size: 2.5rem;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
        margin-bottom: 2rem;
    }}
    .stButton>button {{
        background-color: #FFD700;
        color: #232526;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.5rem;
        font-size: 1.1rem;
        transition: background 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #FFA500;
        color: #fff;
    }}
    .stSelectbox label {{
        color: #FFD700;
        font-weight: bold;
    }}
    .stBlackBox {{
        background: #111;
        color: #fff;
        padding: 1.2rem 1.5rem;
        border-radius: 10px;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('<div class="stHeader">🍿 Movie Recommendation System 🍿</div>', unsafe_allow_html=True)
st.write("Select a movie to get recommendations 💫")
movielist = movies['title'].values
selectedmovie = st.selectbox('Select a movie', movielist)

if st.button('Show Recommend'):
    recommended_movies = recommend(selectedmovie)
    st.markdown(
        '<div class="stBlackBox">Recommended Movies:</div>',
        unsafe_allow_html=True
    )
    for movie in recommended_movies:
        st.write(movie)