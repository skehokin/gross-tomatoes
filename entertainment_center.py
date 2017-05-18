# -*- coding: utf-8 -*-
"""
Created on Thu May 18 07:15:13 2017

@author: Siobhan
"""
import fresh_tomatoes
import media

# Here, we store the data in a Movie class object for use by fresh_tomatoes.py

guardians = media.Movie('Guardians of the Galaxy',
                        'Five idiots fight a zealot in space with great music',
                        'https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg',  # NOQA
                        'https://www.youtube.com/watch?v=B16Bo47KS2g')

star_wars = media.Movie('The Force Awakens',
                        'Star Wars revived',
                        'https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg',  # NOQA
                        'https://www.youtube.com/watch?v=sGbxmsDFVnE')

doctor_strange = media.Movie('Doctor Strange',
                             '''A genius brain surgeon is trained in magical
                             powers as he searches for some way to repare his
                             hands.''',
                             'https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg',  # NOQA
                             'https://www.youtube.com/watch?v=HSzx-zryEgM')

school_of_rock = media.Movie('School of Rock', 'Using rock music to learn',
                             'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',  # NOQA
                             'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

princess_bride = media.Movie('The Princess Bride', '''The classic adventure -
                             pirates, princesses, evil princes''',
                             'https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg',  # NOQA
                             'https://www.youtube.com/watch?v=njZBYfNpWoE')

iron_giant = media.Movie('The Iron Giant', '''The story of the friendship between
                         a boy and a giant robot.''',
                         'https://upload.wikimedia.org/wikipedia/en/d/d3/The_Iron_Giant_poster.JPG',  # NOQA
                         'https://www.youtube.com/watch?v=JgjmFBX34zc')

# create more movie instances here if desired

movies = [guardians, star_wars, doctor_strange,
          school_of_rock, princess_bride, iron_giant]


# create and open an html document with the movie information formatted.
fresh_tomatoes.open_movies_page(movies)
