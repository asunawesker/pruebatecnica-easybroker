import requests


class ContactRequests():

    def __init__(self):
        self.HEADERS = { 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9' }
        self.BASE_URL = 'https://api.stagingeb.com/v1/'

    def postContactRequest(self, payload):

        return requests.post(self.BASE_URL+'/contact_requests', json=payload, headers=self.HEADERS)