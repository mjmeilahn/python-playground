
from requests import Session

"""
EXAMPLE:
from api import Api
req = Api('base-url-goes-here', {'header-key':'header-value'})
res = req.get('/user/1')
"""

class Api(Session):
    def __init__(self, base_url=None, headers=None):
        super().__init__()
        self.base_url = base_url
        self.headers = headers

    def request(self, method, url, *args, **kwargs):
        joined_url = self.base_url + url
        return super().request(method, joined_url, headers=self.headers, *args, **kwargs)