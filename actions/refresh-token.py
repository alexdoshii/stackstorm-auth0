from lib.auth0-mgmt import Auth0Mgmt

__all__ = [
    'RefreshTokenAction'
]

class RefreshTokenAction(Auth0Mgmt):
    def run(self):
        return self.refreshAccessToken()