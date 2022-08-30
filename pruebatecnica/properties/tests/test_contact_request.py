from django.test import TestCase
from unittest.mock import Mock, patch
from properties.controllers.contact_requests import ContactRequests

class TestProperty(TestCase):    
    @patch("requests.post")
    def test_post_contact_request_response_is_success(self, mock_requests_post):
        my_mock_response = Mock(status_code=200)     
        mock_requests_post.return_value = my_mock_response         

        response = ContactRequests().postContactRequest(
            payload={
                "name": "Maricela Arenas",
                "phone": "2721670898",
                "email": "correoprueba@example.com",
                "property_id": "EB-C6484",
                "message": "I'm interested in this property. Please contact me.",
                "source": "pruebatecnica-irais.com"
            }
        )

        self.assertEqual(response.status_code, 200)

    @patch("requests.post")
    def test_post_contact_request_response_is_fail(self, mock_requests_post):
        my_mock_response = Mock(status_code=422)     
        mock_requests_post.return_value = my_mock_response         

        response = ContactRequests().postContactRequest(
            payload={
                "name": "Maricela Arenas",
                "phone": "2721670898",
                "email": "correoprueba@example.com",
                "property_id": "EB-C6484",
                "message": "I'm interested in this property. Please contact me."
            }
        )

        self.assertEqual(response.status_code, 422)

    @patch("requests.post")
    def test_post_contact_request_response_return_status_successful(self, mock_requests_post):
        my_mock_response = Mock(status_code=200)     
        my_mock_response.json.return_value = { "status": "successful" }
        mock_requests_post.return_value = my_mock_response         

        response = ContactRequests().postContactRequest(
            payload={
                "name": "Maricela Arenas",
                "phone": "2721670898",
                "email": "correoprueba@example.com",
                "property_id": "EB-C6484",
                "message": "I'm interested in this property. Please contact me.",
                "source": "pruebatecnica-irais.com"
            }
        )

        data = response.json()
        self.assertEqual(data['status'], "successful")

    @patch("requests.post")
    def test_post_contact_request_response_return_status_need_contact(self, mock_requests_post):
        my_mock_response = Mock(status_code=422)     
        my_mock_response.json.return_value = { "error": "Debes especificar una fuente de contacto." }
        mock_requests_post.return_value = my_mock_response         

        response = ContactRequests().postContactRequest(
            payload={
                "name": "Maricela Arenas",
                "phone": "2721670898",
                "email": "correoprueba@example.com",
                "property_id": "EB-C6484",
                "message": "I'm interested in this property. Please contact me."
            }
        )

        data = response.json()
        self.assertEqual(data['error'], "Debes especificar una fuente de contacto.")