import fresh_tomatoes
import media

#Movies to be displayed
big_lebowski = media.Movie("The Big Lebowski",
                           "A 60's burnout gets into shennanigans.",
                           "http://www.circlecinema.com/wp-content/uploads/2011/06/The-Big-Lebowski-Movie-poster.jpeg",
                           "https://youtu.be/cd-go0oBF4Y",
                           "Abides")

lego_movie = media.Movie("The Lego Movie",
                             "Everything you want it to be",
                             "http://www.tribute.ca/tribute_objects/images/movies/The_LEGO_Movie/LefilmLEGO.jpg",
                             "https://youtu.be/fZ_JOBCLF-I",
                             "SPACESHIP!")

primer = media.Movie("Primer",
                     "Umm? Time? Something?",
                     "http://images.moviepostershop.com/primer-movie-poster-2004-1020240454.jpg",
                     "https://youtu.be/4CC60HJvZRE",
                     "Huh?")

waynes_world = media.Movie("Wayne's World",
                           "Remember when Mike Meyers was still funny?",
                           "http://images.moviepostershop.com/waynes-world-movie-poster-1992-1020190501.jpg",
                           "https://youtu.be/OIuhsHpcNAU",
                           "Worthy")

kick_ass = media.Movie("Kick-Ass",
                       "Some undeserving twerp gets Nick Cage killed",
                       "http://www.comicbookmovie.com/images/users/uploads/8558/kickass-poster_lglkjkj.jpg",
                       "https://youtu.be/rFpWpkxsVI8",
                       "Ass-Kick")

the_matrix = media.Movie("The Matrix",
                         'Introduced the concept of "Bullet time"',
                         "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                         "https://youtu.be/m8e-FF8MsqU",
                         "Woah")


#Movies must be in the movies array in order to display on the page.
movies = [big_lebowski, lego_movie, primer, waynes_world, kick_ass, the_matrix]

fresh_tomatoes.open_movies_page(movies)
