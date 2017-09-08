import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Movie: creates a Movie object with show title, show storyline,
    # and a poster image
    def __init__(self, movie_title, movie_stroyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_stroyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

    # Video: creates a Television object with show title, show storyline,
    # and a poster image
    class Televison():

        def __init__(self, show_title, show_storyline, poster_image,
                     trailer_youtube):
            self.title = show_title
            self.storyline = show_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

        # Video: creates a Video object with title and duration
        class Video():

            def __init__(self, title, duration):
                self.title = title
                self.duration = duration
