from Spotify import Spotify


class Adapter(object):
    def __init__(self):
        self.sp = Spotify()

    def get_tracks(self, *args, **kwargs):
        """
            function to modify the output of the Spotify.get_paylist() function

            :return
            a string object {artist} -- {song}
        """
        tracks = self.sp.get_tracks(*args, **kwargs)
        s = ''
        print(tracks)
        # for item in tracks:
        #     s += '{artist} -- {song}'.format(artist=item.artist, song=item.track)

        return s

    def get_playlist(self, *args, **kwargs):
        return self.sp.get_playlists()

    def add_track_to_playlist(self, *args, **kwargs):
        pass










