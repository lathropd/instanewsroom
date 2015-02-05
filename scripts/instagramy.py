from instagram.client import InstagramAPI
from pprint import pprint


test_access_token = "1890268.7c3f1ab.e1c64ca8df38410099d98bff8a868bb6"
api = InstagramAPI(access_token=test_access_token)

pprint( api.user_recent_media())
