import webbrowser

class Movie():
""" Class for creating instances of movies containing information about the movie """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_review):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.review = movie_review

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)