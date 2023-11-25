from lib.auth0_mgmt import Auth0Mgmt

__all__ = [
    'UnblockUser'
]


class UnblockUser(Auth0Mgmt):
    def run(self, user_id: str):
        return self.unblockUser(user_id.strip())
