import fresh_tomatoes
import media


# Begin movie-specific data list
wall_e = media.Movie("Wall-E",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=ZisWjdjs-gM")

up = media.Movie("Up",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=qas5lWp7_R0")

pokemon = media.Movie("Pokemon",
                      "https://www.movieposter.com/posters/archive/main/176/MPW-88471",  # NOQA
                      "https://www.youtube.com/watch?v=JBXGVw_RU3c")

finding_nemo = media.Movie("Finding Nemo",
                           "http://img.moviepostershop.com/finding-nemo-movie-poster-2003-1010399134.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=AXoZdTe9YFs")

toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

frozen = media.Movie("Frozen",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
# End movie-specific data list

# Specify movies to be shown in HTML output
movies = [wall_e, up, pokemon, finding_nemo, toy_story, frozen]
fresh_tomatoes.open_movies_page(movies)
