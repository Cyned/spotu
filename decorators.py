def get_tracks(func):
    """
        decorator to modify the output of the Spotify.get_paylist() function

        :return
        a string object {artist} -- {song}
    """

    def function_wrapper(*args, **kwargs):
        tracks = func(*args, **kwargs)
        s = ''
        print(tracks)
        # for item in tracks:
        #     s += '{artist} -- {song}'.format(artist=item.artist, song=item.track)

        return s

    return function_wrapper






