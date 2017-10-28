class SpotifyException(Exception):

    def __init__(self, http_status, code, msg, headers=None):
        self.http_status = http_status
        self.code = code
        self.msg = msg
        if headers is None:
            headers = {}
        self.headers = headers

    def __str__(self):
        return 'http status {0}, code: {1} - {2}'.format(self.http_status, self.code, self.msg)
