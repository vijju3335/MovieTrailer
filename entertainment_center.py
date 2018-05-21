#!/usr/bin/env python
import media
import fresh_tomatoes


# Create Movie objects
race3 = media.Movie(
    "Race 3",
    "images/race3.jpeg",
    "https://www.youtube.com/watch?v=xBht9TG7ySw")
tare = media.Movie(
    "Tare Zamee Par",
    "images/tare.jpeg",
    "https://www.youtube.com/watch?v=NU2CGWplrD0")
dangal = media.Movie(
    "Dangal",
    "images/dangal.jpeg",
    "https://www.youtube.com/watch?v=x_7YlGv9u1g")
devadasu = media.Movie(
    "Devadasu",
    "images/devadas.jpg",
    "https://www.youtube.com/watch?v=nZCHsIegkaE")
mahanati = media.Movie(
    "Mahanati",
    "images/mahanati1.jpeg",
    "https://www.youtube.com/watch?v=njYYDSVVEm8")
maya = media.Movie(
    "Maya Bazaar",
    "images/maya.jpeg",
    "https://www.youtube.com/watch?v=9S8BJJYB79k")
kaala = media.Movie(
    "Kaala",
    "images/kaala.jpeg",
    "https://www.youtube.com/watch?v=Wm_vSSlVsV4")
lord = media.Movie(
    "Lord Of The Rings",
    "images/lord.jpeg",
    "https://www.youtube.com/watch?v=rCZ3SN65kIs")
frozen = media.Movie(
    "Frozen 2",
    "images/frozen.jpeg",
    "https://www.youtube.com/watch?v=FNZi0RoclBE")
padding2 = media.Movie(
    "Padding Ton2",
    "images/padding2.jpeg",
    "https://www.youtube.com/watch?v=5B6A0UrYJsk")
up = media.Movie(
    "Up",
    "images/up.jpeg",
    "https://www.youtube.com/watch?v=F2bk_9T482g")
# Create list of  movie objects
cinemas = [
    race3, tare, dangal, devadasu,
    mahanati, maya, kaala,
    lord, frozen, padding2, up]
# Create movie trailer page with above list passing
fresh_tomatoes.open_movies_page(cinemas)
