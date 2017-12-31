import webbrowser


# Defining attributes available for each movie
class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Defining method to open the YouTube trailer on click
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
