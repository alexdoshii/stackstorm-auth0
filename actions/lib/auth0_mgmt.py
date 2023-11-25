from auth0.authentication import GetToken
from auth0.management import Auth0
from auth0.exceptions import Auth0Error
from st2common.runners.base_action import Action
import logging

__all__ = [
    'Auth0Mgmt'
]


class Auth0Mgmt(Action):
    def __init__(self, config):
        super(Auth0Mgmt, self).__init__(config=config)
        self._clientId = self.config.get('management_api_client_id')
        self._clientSecret = self.config.get('management_api_client_secret')
        self._domain = self.config.get('auth0_domain')

    def _getAccessToken(self) -> str:
        getToken = GetToken(self._domain, self._clientId, self._clientSecret)
        try:
            token = getToken.client_credentials(
                'https://{}/api/v2/'.format(self._domain))
        except Auth0Error as e:
            print(str(e))
            return None
        return token['access_token']

    def _getAccessTokenFromStore(self) -> str:
        return self.action_service.get_value(
            name='auth0_mgmt_access_token',
            local=False,
            decrypt=True)

    def _getAuth0(self) -> Auth0:
        token = self._getAccessTokenFromStore()
        auth0 = Auth0(self.domain, token)
        return auth0

    def refreshAccessToken(self) -> bool:
        token = self._getAccessToken()

        if token is not None:
            try:
                self.action_service.set_value(
                    name='auth0_mgmt_access_token',
                    local=False,
                    encrypt=True,
                    value=token)
            except:
                logger.exception('An error occurred trying to set value.')
                return False
            return True
        else:
            logger.error('Token not obtained. Cannot continue.')
            return False

    def getUser(self, userId: str) -> dict:
        auth0 = self._getAuth0()
        try:
            data = auth0.users.get(id="auth0|{}".format(userId))
            return data
        except Auth0Error as e:
            logger.exception(str(e))
            return {"error": str(e)}
