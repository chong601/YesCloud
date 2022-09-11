class User(object):
    _user = {}

    def setUser(self, key, name):
        self._user.update({key: name})

    def dumpUser(self):
        return self._user
