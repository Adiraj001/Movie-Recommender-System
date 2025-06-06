## 🎬 Movie Recommender System
A content-based movie recommendation system built with Python, Pandas, Scikit-learn, and Streamlit. This project helps users discover new movies based on their favorite picks using similarity metrics and metadata features.



## 🔍 Features
-Content-based filtering using movie metadata

-Cosine similarity-based recommendations

-User-friendly web interface built with Streamlit



## 🧠 How It Works
The system uses metadata such as genres, cast, crew, and keywords to create a "tag" for each movie. These tags are vectorized and compared using cosine similarity to recommend movies that are similar to a user-selected title.

## 🛠 Tech Stack
-Python 🐍

-Pandas & NumPy for data processing

-Scikit-learn for vectorization and similarity computation

-Streamlit for the front-end interface


## 🚀 Getting Started
-1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/Adiraj001/Movie-Recommender-System.git
cd Movie-Recommender-System
-2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt



4. Run the App
bash
Copy
Edit
streamlit run app.py

## 📦 Dataset
The dataset used is a cleaned and merged version of movie metadata from Kaggle, including cast, crew, genres, keywords, etc.

## 🖼 Sample UI
Once launched, you'll see a dropdown to select a movie. The system then displays 5 similar movie recommendations with their posters.
