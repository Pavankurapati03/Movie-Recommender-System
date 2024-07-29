# Movie Recommender System 🎥

## Overview
The Movie Recommender System(Content based filtering) is a web application built using Streamlit that suggests movies based on user-selected preferences and genres. Users can either choose a specific movie to get recommendations similar to it or select their preferred genres to receive top-rated movie suggestions.

## Features
- **Movie Recommendations**: Get movie recommendations based on a selected movie or preferred genres.
- **Genre Filtering**: Choose from various genres to filter movie suggestions.
- **Poster Display**: View movie posters alongside their titles and ratings.
- **Responsive Layout**: User-friendly interface with custom styling and layout.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommender.git
    ```
2. Change the directory:
    ```bash
    cd movie-recommender
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Launch the application:
    ```bash
    streamlit run app.py
    ```
2. Select your preferred genres from the multiselect dropdown on the left.
3. Type or select a movie from the dropdown on the right.
4. Click the "Show Recommendation" button to view the recommendations.
5. The recommended movies, along with their posters and ratings, will be displayed on the screen.

## Files

- **app.py**: Main application script containing the Streamlit app logic.
- **movie_list.pkl**: Pickle file containing the list of movies.
- **similarity.pkl**: Pickle file containing the movie similarity data.
- **requirements.txt**: List of dependencies required to run the application.

## API Used

- **The Movie Database (TMDB)**: Used to fetch movie posters.

## Custom CSS

The application uses custom CSS to style the title and other elements for a better user experience.

## Error Handling

- Handles errors during data loading and poster fetching gracefully.
- Displays error messages to the user when necessary.

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
