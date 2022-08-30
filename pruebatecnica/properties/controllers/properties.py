import requests

class Properties():

    def __init__(self):
        self.HEADERS = { 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9' }
        self.BASE_URL = 'https://api.stagingeb.com/v1/'

    def getProperties(self, page = 1):

        payload = {
            'page': page,
            'search[statuses]': 'published',
        }

        try:
            response = requests.get(self.BASE_URL+'properties?page='+str(page)+'&limit=15&statuses=published', params=payload, headers= self.HEADERS)
            if response.ok:
                return response
            else:
                return None
        except requests.exceptions.Timeout:
            return 'Bad Response'

    def getProperty(self, property_id):
        try:
            response = requests.get(self.BASE_URL+'properties/'+str(property_id), headers=self.HEADERS)
            if response.ok:
                return response
            else:
                return None
        except requests.exceptions.Timeout:
            return 'Bad Response'