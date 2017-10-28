from Spotify import Spotify


if __name__ == '__main__':
    sp = Spotify()
    sp.get_playlists()
    sp.add_tracks_to_playlist('The native boat', ['Papa Roach', 'Help'])
