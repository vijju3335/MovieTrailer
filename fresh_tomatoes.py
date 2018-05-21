#!/usr/bin/env python
import webbrowser
import os
import re


#  Styles and scripting for the start page
start_page_content = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head;
    any other head content must come *after* these tags -->

    <title>Movie Trailer</title>

    <!-- Bootstrap Core CSS -->
    <link rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

    <link rel="stylesheet" href="css/custom.css">
    <link rel="stylesheet" href="css/modal.css">

    <!-- Custom CSS: You can use this stylesheet to override
    any Bootstrap styles and/or apply your own styles -->
</head>

<body style="padding-top:0px;">
    <!-- Content -->
    <div class="container">
        <!-- Heading -->
        <div class="row">
            <div class="col-lg-10">
                <h1 class="page-header">Movie Trailer</h1>
            </div>
        </div>
        <div>
            <!-- The Modal -->
            <div id="myModal" class="modal">
            <!-- Modal content -->
                <div class="modal-content">
                    <span class="close"> &times;</span>
                    <iframe width="500px" height="350px"
                    src="" frameborder="0"
                    allow="autoplay; encrypted-media" allowfullscreen></iframe>
                </div>
            </div>
        </div>
        <!-- Projects Row -->
        <div class="row">
'''

''' The end page layout and title bar'''
end_page_content = '''
</div>
    </div>
    <!-- /.container -->

    <footer>
        <div class="copyright">
            <div class="container">
                <p style="background-color: skyblue;">
                Copyright &copy; &nbsp vijju3335 &nbsp #2018</p>
            </div>
        </div>
    </footer>

</body>

<script src="js/main.js"></script>
</html>
'''

''' A single movie main entry html template middle page'''
movie_tile_content = '''
<div class="col-md-4 portfolio-item" onclick="onc('{trailer_youtube_url}')">
    <img class="img-responsive" src="{poster_image_url}" alt="{movie_title}">
    <h3 ><b>{movie_title}</b></h3>
</div>
'''


def create_movie_tiles_content(movies):
    #  The HTML content for this section of the page
    content = ''
    for movie in movies:
        #  Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        #  Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.movie_title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_url=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    #  Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    #  Replace the movie tiles placeholder generated content
    rendered_content = create_movie_tiles_content(movies)

    #  Output the file
    output_file.write(start_page_content + rendered_content + end_page_content)
    output_file.close()

    #  open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
