from lib.auth0_mgmt import Auth0Mgmt

__all__ = [
    'RefreshTokenAction'
]

class RefreshTokenAction(Auth0Mgmt):
    def run(self):
        return self.refreshAccessToken()