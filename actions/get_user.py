from lib.auth0_mgmt import Auth0Mgmt

__all__ = [
    'GetUser'
]


class GetUser(Auth0Mgmt):
    def run(self, user_id: str):
        return self.getUser(user_id)
