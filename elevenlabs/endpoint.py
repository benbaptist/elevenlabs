class Endpoint(object):
    def __init__(self, main):
        self.main = main
        
        self._request = main._request
        self._throttle = main._throttle
