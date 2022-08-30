from django.test import TestCase
from unittest.mock import Mock, patch
from properties.controllers.properties import Properties

class TestProperties(TestCase):
    @patch("requests.get")
    def test_get_properties_response_has_content(self, mock_requests_get):
        mock_requests_get.return_value.ok = True
        response = Properties().getProperties()
        self.assertIsNotNone(response)

    @patch("requests.get")
    def test_get_properties_response_ok_is_false(self, mock_requests_get):
        mock_requests_get.return_value.ok = False
        response = Properties().getProperties()
        self.assertIsNone(response)

    @patch("requests.get")
    def test_get_properties_response_ok_is_true(self, mock_requests_get):
        properties = [
        {
            "pagination": {
            "limit": 1,
            "page": 2,
            "total": 826,
            "next_page": "https://api.stagingeb.com/v1/properties?limit=10&page=2"
            },
            "content": [
            {
                "public_id": "EB-C0111",
                "title": "Titulo",
                "title_image_full": "https://assets.images.com",
                "title_image_thumb": "https://assets.images.com",
                "location": "Ciudad ficticia",
                "operations": [
                    {
                        "type": "sale",
                        "amount": 100000.0,
                        "currency": "MXN",
                        "formatted_amount": "$100,100",
                        "commission": {
                            "type": "percentage"
                        },
                        "unit": "total"
                    }
                ],
                "bedrooms": 2,
                "bathrooms": 2,
                "parking_spaces": 1,
                "property_type": "Departamento",
                "lot_size": 250.0,
                "construction_size": 300.0,
                "updated_at": "2020-12-10T11:47:38-06:00",
                "agent": "Irais Aguirre Valente",
                "show_prices": True,
                "share_commission": True
            }
            ]
        }
        ]

        mock_requests_get.return_value = Mock(ok=True)
        mock_requests_get.return_value.json.return_value = properties

        response = Properties().getProperties()

        self.assertListEqual(response.json(), properties)