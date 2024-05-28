import pickle
import streamlit as st
import requests

# Set page config with title and icon
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎥"  # Film camera emoji
)

# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"

# Load movies and similarity data with error handling
try:
    movies = pickle.load(open('C:/Users/Pavan/Desktop/Recommender/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('C:/Users/Pavan/Desktop/Recommender/similarity.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()  # Stop execution if data loading fails

# Recommendation function considering user preferences
def recommend(movie, selected_genres):
    if movie == "None" or movie is None:
        if not selected_genres:
            return [], [], []  # Return empty lists if no movie or genres are selected
        
        # Initialize recommended movies list for selected genres
        recommended_movie_names = []
        recommended_movie_posters = []
        recommended_movie_ratings = []
        
        # Iterate over movies to find top rated movies within selected genres
        for idx, row in movies.iterrows():
            if set(selected_genres).intersection(set(row['genres'])):
                movie_id = row['movie_id']
                recommended_movie_posters.append(fetch_poster(movie_id))
                recommended_movie_names.append(row['title'])
                recommended_movie_ratings.append(row['vote_average'])
                if len(recommended_movie_names) == 10:  # Recommend top 10 rated movies for selected genre
                    break
        return recommended_movie_names, recommended_movie_posters, recommended_movie_ratings

    else:
        index = movies[movies['title'] == movie].index
        if len(index) == 0:
            return [], [], []  # Return empty lists if selected movie is not found

        index = index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        recommended_movie_ratings = []
        for i in distances[1:]:
            movie_id = movies.iloc[i[0]].movie_id
            if not selected_genres or set(selected_genres).intersection(set(movies.iloc[i[0]].genres)):
                recommended_movie_posters.append(fetch_poster(movie_id))
                recommended_movie_names.append(movies.iloc[i[0]].title)
                recommended_movie_ratings.append(movies.iloc[i[0]].vote_average)
            if len(recommended_movie_names) == 10:  # Recommend top 10 rated movies for selected genre
                break
        return recommended_movie_names, recommended_movie_posters, recommended_movie_ratings

# Custom CSS styling for the title
st.markdown(
    """
    <style>
    .custom-title {
        font-size: 46px;
        text-align: left;
        font-weight: bold;
        font-family: Open Sans;
        background: -webkit-linear-gradient(rgb(188, 12, 241), rgb(212, 4, 4));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-left: 10px;
    }
    .icon {
        vertical-align: middle;
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add an icon (movie emoji) at the beginning of the title
st.markdown("<p class='custom-title'><span class='icon'>🎥</span>Movie Recommender System</p>", unsafe_allow_html=True)

# Input widget for selecting preferred genres and movie selection dropdown side by side
col1, col2 = st.columns([1, 3])

with col1:
    selected_genres = st.multiselect("Select preferred genres", movies['genres'].explode().unique())

with col2:
    movie_list = ['None'] + list(movies['title'].values)
    selected_movie = st.selectbox("Type or select a movie", movie_list)

# Show recommendations on button click
if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_ratings = recommend(selected_movie, selected_genres)
        st.markdown("### Recommended Movies")
        cols = st.columns(5)
        for col, movie_name, movie_poster, movie_rating in zip(cols, recommended_movie_names, recommended_movie_posters, recommended_movie_ratings):
            with col:
                st.image(movie_poster)
                st.markdown(f"<p style='text-align: center;'>{movie_name}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center;'>Rating: {movie_rating}/10</p>", unsafe_allow_html=True)
