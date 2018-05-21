# MovieTrailer
Udacity Full Stack Nano Degree Project1

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube. The project also includes some CSS and jQuery involved in the display of the webpage.

This Movie Trailer Website Project#1 consists of Python version 2.7.9 files that store a list of movies titles, along with its respective box art imagery and movie trailer website.

The Movie Class in the media.py module creates a data structure to store your favorite movies, including movie title, poster URL and a YouTube link to the movie trailer.

The entertainment_center.py file creates multiple instances of that Movie Class to represent your favorite movies and groups all the instances together in a list.

The Python module called fresh_tomatoes.py has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.

## Table of contents

- [Demo](#demo)
- [Download](#download)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Running Documents Locally](#running-documents-locally)
- [Bug And Feature Requests](#bug-and-feature-requests)

## Demo

For a demo, check out <https://github.com/vijju3335/MovieTrailer/blob/master/fresh_tomatoes.html>!

## Download

The files for the project, may be [downloaded here](https://github.com/vijju3335/MovieTrailer/archive/master.zip).

## Quick Start

After downloading the project files, a movie trailer page can be created by importing [media.py]  (https://github.com/vijju3335/MovieTrailer/blob/master/media.py) and [fresh_tomatoes.py]  (https://github.com/vijju3335/MovieTrailer/blob/master/fresh_tomatoes.py) at the start of your Python script. Then create idividual Movie objects by calling media.Movie() and supplying it with 3 arguments -- title, poster_url, and trailer_url. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an list of the movie objects you created.

```
import media
import fresh_tomatoes

#information for object arguments
title = "movie title"
poster_url = "image link"
trailer = "https://www.youtube.com/watch?v=njYYDSVVEm8"

# Create Movie object
movie_obj = media.Movie(title, poster_url, trailer_url)

# Create movie trailer page with list of objects
fresh_tomatoes.open_movies_page([movie_obj])

```
A more detailed example with multiple movie objects, which is used for the [demo](https://github.com/vijju3335/MovieTrailer/blob/master/fresh_tomatoes.py), can be found in [entertainment_center.py](https://github.com/vijju3335/MovieTrailer/blob/master/entertainment_center.py) 

### What's included

Within the download you'll find the following directories and files:

```
MovieTrailer-master.zip/
├── css/
│   └── custom.css
│   └── modal.css
├── images/
│   └── tare.jpeg
│   └── kaala.jpeg
│   └── mahanati.jpeg
│   └── up.jpeg
│   └── .....
├── js/
│   └── main.js
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py](https://github.com/edwardbryant/udacity-movie-trailer-project/blob/master/media.py). 

##### constructor method

The constructor method is called when a new Movie object is created and must include 3 arguments -- [title](#movietitle), [poster_url](#movieposter_url), and [trailer_url](#movietrailer_url). Each of these arguments is discussed further below.

```
import media
import fresh_tomatoes

#information for object arguments
title = "movie title"
poster_url = "image link"
trailer = "https://www.youtube.com/watch?v=njYYDSVVEm8"

# Create Movie object
movie_obj = media.Movie(title, poster_url, trailer_url)

```

###### movie.title

movie.title is any string used to identify the movie object.

###### movie.poster_url

movie.poster_url is a string containing a URL linking to an image which will be used to represent the Movie object, such as a movie poster or DVD box cover. The movie trailer page portion of this project displays these images with a width of 300px and a height of 400px.

###### movie.trailer_url

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/vijju3335/MovieTrailer/blob/master/fresh_tomatoes.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

#### open_movies_page function

To create the static movie trailers page the open_movies_page function must be called and supplied with one required argument (an array of Movie class objects)

```
# Create movie trailer page with array of Movie class objects
fresh_tomatoes.open_movies_page([movie1, movie2, movie3])

``` 

The newly generated page will be placed in the same directory and named fresh_tomatoes.html. This new page relies on three files for its background image (img/curtains.jpg), CSS style settings (css/custom.css,css/modal.css), and jQuery effects (js/main.js).

#### create_movie_tiles_content

The create_movie_tiles_content function is called by the open_movies_page function. It takes the array of Movie class objects as an argument and iterates through each Movie object and applies the object's data to the portion of the HTML template for each movie. While iterating through each object's class variables, it extracts the YouTube id from movie.trailer_url using regular expressions.

## Running Documents Locally
- Open and Edit entertainment_center.py
- Add your custom movies titles,poster url's,trailer url's
- Add to list to pass to fresh_tomatoes.open_movies_page([])
- Save file.

In a Terminal window type:
```bash
$ python entertainment_center.py
```
To run above command, you have to download & install python [downloaded here](https://www.python.org/downloads/)
This creates a html page fresh_tomatoes.html
Your default browser will open with the html page that was rendered by python.

---

## Bug And Feature Requests
Have a bug or a feature request? Please feel free to open an [issue](https://github.com/vijju3335/MovieTrailer/issues/new).
