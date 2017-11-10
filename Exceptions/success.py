from colorama import Fore

from .base import SpotifyException


class SpotifySuccess(SpotifyException):

    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        print(Fore.GREEN, end='')
        result = super().__str__()

        return result

    def __del__(self):
        print(Fore.WHITE)
