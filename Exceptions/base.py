class SpotifyException(object):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return '{:20}'.format(self.msg)
