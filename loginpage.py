import streamlit as st

# Hardcoded credentials (for demonstration purposes)
CREDENTIALS = {"user1": "password1", "user2": "password2"}


# Function to check login credentials
def login(username, password):
    if CREDENTIALS.get(username) == password:
        return True
    return False


# Logout function
def logout():
    st.session_state['logged_in'] = False


# If 'logged_in' key is not present in session_state, initialize it to False
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Show login page if user is not logged in
if not st.session_state['logged_in']:
    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if login(username, password):
            st.success("Logged in successfully!")
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid credentials, please try again.")

# Show the main app if the user is logged in
if st.session_state['logged_in']:
    # Create a simple navbar (as done earlier)
    st.markdown("""
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
      </div>
    </nav>
    """, unsafe_allow_html=True)

    # Add a logout button
    if st.button("Logout"):
        logout()
        st.success("Logged out successfully!")

    # Now you can place the rest of your app here, like the movie recommender system
    st.title("Welcome to the Movie Recommender System!")
    # (Your movie recommender code would go here)
else:
    st.write("Please log in to access the app.")
