import urbanairship
from google.appengine.api import urlfetch


class Airship(urbanairship.Airship):
    def __init__(self, *args, **kwargs):
        self.request_deadline = kwargs.pop('request_deadline', 60)
        self.request_validate_certificate = kwargs.pop(
            'request_validate_certificate', True)
        super(Airship, self).__init__(*args, **kwargs)

    def _request(self, method, body, url, content_type=None):
        headers = dict()
        headers['Authorization'] = 'Basic %s' % self.auth_string
        if content_type:
            headers['Content-Type'] = content_type

        resp = urlfetch.fetch(
            url,
            payload=body,
            method=method,
            headers=headers,
            deadline=self.request_deadline,
            validate_certificate=self.request_validate_certificate)
        if resp.status_code == 401:
            raise urbanairship.Unauthorized

        return resp.status_code, resp.content
