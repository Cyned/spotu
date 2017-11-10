import os

import spotipy
import spotipy.util as util

from SpotifyBase import SpotifyBase
from Exceptions.success import SpotifySuccess as success_msg
from Exceptions.failed import SpotifyFailed as failed_msg
from Exceptions.info import SpotifyInfo as info_msg

from decorators import get_tracks


class Spotify(SpotifyBase):

    username = 'cynedenis'
    scope = 'user-library-modify playlist-modify-public user-modify-playback-state'
    # scope = ''

    def __init__(self):
        super(SpotifyBase, self).__init__()

        self.client_id, self.client_secret, self.redirect_url = self._get_const()

        self._rm_cache()
        self._authentication()

    def _authentication(self):
        """
            to authenticate user
        """
        try:
            token = util.prompt_for_user_token(username=self.username,
                                               scope=self.scope,
                                               client_id=self.client_id,
                                               client_secret=self.client_secret,
                                               redirect_uri=self.redirect_url)
        except spotipy.oauth2.SpotifyOauthError as e:
            token = None
            print(failed_msg('Something wrong with your Spotify Web. '
                             'Try to use another browser or set your browser to use protected content.'))

        if token:
            self.sp = spotipy.Spotify(auth=token)
            print(success_msg('Authentication was successful'))
        else:
            print(failed_msg('Authentication was failed. \n Check if all you input data was correct.'))

    @get_tracks
    def get_tracks(self):
        """
            :return:
            list of the tracks objects
        """
        tracks = self.sp.current_user_saved_tracks()
        return tracks

    def get_playlists(self):
        """
            :return: user's playlists object

            in the key 'items' there are a list of all the public playlists
        """

        playlists = self.sp.current_user_playlists(limit=50)

        if playlists:
            print(info_msg('get your playlists'))
            return playlists
        else:
            print(info_msg('You have no playlists'))

    def find_playlist(self, name):
        """
            to find playlist via its name

            :param name: the name of playlist that is being finding

            :return: playlist dict
        """

        playlists = self.get_playlists()
        pl = None

        for playlist in playlists['items']:

            if playlist['name'] == name:
                pl = playlist
                break

        if pl:
            print(info_msg('needed playlist was found'))
            return pl
        else:
            print(failed_msg('there is no playlist you wrote'))

    def add_tracks_to_playlist(self, pl_name, tracks):
        """
            to add tracks to the given playlist

            :param pl_name: name of the playlist
            :param tracks: list of the tracks:
                            [..., ['{artist}', '{name of the song}'], ...]
        """

        artist = tracks[0]
        song = tracks[1]
        urn = 'artist:{} track:{}'.format(artist, song)
        artist = self.sp.search(q=urn)

        track_id = artist['tracks']['items'][0]['id']
        pl_id = self.find_playlist(pl_name)['id']

        if pl_id and track_id:
            try:
                result = self.sp.user_playlist_add_tracks(self.username, pl_id, track_id)
                # result = self.sp.current_user_saved_tracks_add(track_id)
                print(success_msg('The songs was added successfully'))
            except spotipy.client.SpotifyException as e:
                print(failed_msg('The songs were not added. \n {}'.format(e)))

        else:
            print(failed_msg('Something is wrong: \n playlist_id: {} \n track_id: [}'.format(pl_id, track_id)))

    @staticmethod
    def _rm_cache():
        """
            remove .cache-* file
        """
        try:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.cache-cynedenis')
            os.remove(path)
        except FileNotFoundError:
            pass

    @staticmethod
    def _get_const(file_name='app_const'):
        """
            get constants to authenticate user
            :param file_name: name of the file where client_id, client_secret and redirect_url are located

            :return: client_id, client_secret, redirect_url
        """
        with open(file_name, 'r') as file:
            t = file.read().split('\n')

            client_id = t[0].split('=')[1]
            client_secret = t[1].split('=')[1]
            redirect_url = t[2].split('=')[1]

        return client_id, client_secret, redirect_url
