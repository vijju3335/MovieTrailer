#!/usr/bin/env python
import webbrowser


class Movie():
    '''class Movie():
    create an object with 3 attributes and function
    Attributes:
        movie_title(str): name of movie
        poster_image_url(str): poster of movie
        trailer_youtube_url(str): trailer of movie
    '''
    def __init__(self, title, poster_img, trailer_link):
        #  movie title
        self.movie_title = title
        #  movie poster
        self.poster_image_url = poster_img
        #  movie trailer
        self.trailer_youtube_url = trailer_link

    def show_trailer(self):
        '''show youtube trailer in web browser'''
        webbrowser.open(self.trailer_youtube_id)
