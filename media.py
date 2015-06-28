"""
Defines Movie, a class that describes a movie and
can show the trailer in a web browser.
"""

import webbrowser

class Movie():

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        Displays the defined movie trailer in a web browser.
        """
        webbrowser.open(self.trailer_youtube_url)
