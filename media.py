# -*- coding: utf-8 -*-
"""
Created on Thu May 18 05:18:02 2017

@author: Siobhan
"""

import webbrowser


class Movie():
    """
    A class which provides a way to store movie data.

        Attributes:
        title(str): value is the movie title given as the first argument.
        storyline (str): value is the movie storyline given as the second
            argument.
        poster_image_url (str): value is the image url for the movie poster,
            which was given as the third argument.
        trailer_youtube_url (str): value is the youtube url for the movie
            trailer, which was given as the forth argument.
    """

    def __init__(self, movie_title, movie_storyline, movie_image,
                 movie_trailer):
        """Inits the Movie class, with variables (in argument order) - movie
        title, movie storyline, movie image and movie trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """is used by fresh_tomatoes.py to open the youtube trailer link"""
        webbrowser.open(self.trailer)
