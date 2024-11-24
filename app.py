import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import requests

# Custom CSS for out-of-this-world styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
        color: white;
        font-family: 'Courier New', Courier, monospace;
    }
    .css-18e3th9 {
        background-color: rgba(0, 0, 0, 0.5) !important;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        border-radius: 12px;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: white; 
        color: black;
        border: 2px solid #4CAF50;
    }
    img {
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    }
    .stSelectbox {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load pickled data
newdf = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetchposter(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=73ea8b3ecf4e69a185157298d93f8b48'
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = newdf[newdf['title'] == movie].index[0]
    similar = similarity[movie_index]
    movies_list = sorted(list(enumerate(similar)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_posters = []
    for el in movies_list:
        recommend_movies.append(newdf.iloc[el[0]].title)
        recommend_posters.append(fetchposter(newdf.iloc[el[0]].movie_id))
    return recommend_movies, recommend_posters


# Sidebar menu
with st.sidebar:
    selectedmenu = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contacts"],
        default_index=0,
        orientation="horizontal",
    )

if selectedmenu == 'Home':
    # Page title
    st.title('Movie Recommendation System 🌌')

    # Movie selection box
    movie_selected = st.selectbox('🔍 Select a movie:', newdf['title'].values)

    # Recommend button with animation effect
    if st.button('✨ Recommend Me Movies ✨'):
        recommend_movies, recommend_posters = recommend(movie_selected)

        # Display the recommendations in an elegant layout
        st.markdown("<h3 style='text-align: center; color: #FFA500;'>Recommended Movies for You</h3>",
                    unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(recommend_posters[0], use_container_width=True)
            st.write(f"🎬 **{recommend_movies[0]}**")
        with col2:
            st.image(recommend_posters[1], use_container_width=True)
            st.write(f"🎬 **{recommend_movies[1]}**")
        with col3:
            st.image(recommend_posters[2], use_container_width=True)
            st.write(f"🎬 **{recommend_movies[2]}**")

        col4, col5 = st.columns(2)
        with col4:
            st.image(recommend_posters[3], use_container_width=True)
            st.write(f"🎬 **{recommend_movies[3]}**")
        with col5:
            st.image(recommend_posters[4], use_container_width=True)
            st.write(f"🎬 **{recommend_movies[4]}**")

if selectedmenu == 'Projects':
    st.title("🌟 Explore Your Projects Here")
    st.markdown("<p style='text-align: center;'>Coming Soon... Stay Tuned! 🎥</p>", unsafe_allow_html=True)

if selectedmenu == 'Contacts':
    st.title("📞 Contact Us")
    st.markdown("<p style='text-align: center;'>We'd love to hear from you! 🌟</p>", unsafe_allow_html=True)
