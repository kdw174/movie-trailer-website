import webbrowser

#This class will store information about movies and provide a function to view the trailer.
class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #constructor to set title, storyline, image, and trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date, director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.director = director
    #function to display trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
