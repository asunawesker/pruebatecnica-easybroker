from django.test import TestCase
from unittest.mock import Mock, patch
from properties.controllers.properties import Properties

class TestProperty(TestCase):    
    @patch("requests.get")
    def test_get_property_response_has_content(self, mock_requests_get):
        mock_requests_get.return_value.ok = True
        response = Properties().getProperty('EB-B5357')
        self.assertIsNotNone(response)

    @patch("requests.get")
    def test_get_property_response_ok_is_false(self, mock_requests_get):
        mock_requests_get.return_value.ok = False
        response = Properties().getProperty('EB-B5357')
        self.assertIsNone(response)

    @patch("requests.get")
    def test_get_property_response_ok_is_true(self, mock_requests_get):
        property = {
            "public_id": "EB-B5357",
            "title": "Locales Comerciales en Venta Vasconcelos San Pedro Garza Garcia",
            "description": "- Edificio 100% comercial- 6 niveles de área comercial- 42 locales desde 31 m2 hasta 172 m2- 2 elevadores de circulación vertical- 2,856 m2 de área rentable- 8,992 m2 de construcción- 1,571 m2 de terreno. 154 cajones en 6 sótanosCARACTERÍSTICAS DE LOS LOCALES- Muros: perimetrales block aparente- Cielo: Losa concreto aligerada- Firme: de concreto- Frente: cristal con puerta de cristal templado- Peparaciones: eléctricas, hidrosanitarias, voz y datos, aire acondicionadoDISPONIBLENIVEL PB- Local 6 / 85.79 m2 / terraza 16.08 m2 / total 101.87 m2- Local 7 / 103.66 m2 / terraza 33.16 m2 / total 136.82 m2- Local 8 / 43.01 m2 / terraza 33.16 m2 / total 76.17 m2- Local 10 / 24.29 m2 / terraza 15.47 m2 / total 39.76 m2NIVEL 2- Local 14 / 35.65 M2- Local 15 / 90.1 m2- Local 16 / 105.12 m2 NIVEL 3- Local 19 / 36.62 m2- Local 22 / 30.62 m2- Local 23 / 77.74 m2- Local 24 / 79.08 m2- Local 25 / 30.73 m2NIVEL 4- Local 28 / 40.87 m2 / terraza 37.81 m2 / total 78.68 m2- Local 29 / 36.82 m2- Local 30 / 30.96 m2- Local 31 / 29.82 m2- Local 32 / 29.6 m2- Local 33 / 77.22 m2 - Local 34 / 131.07 m2 / terraza 48,8 m2 / total 179.87 m2NIVEL 5- Local 35 / 46.85 m2 / terraza 33.8 m2 / total 80.65- Local 36 / 44.43 m2 - Local 37 / 37.45 m2- Local 38 / 36.82 m2- Local 39 / 77.5 m2 / terraza 130.09 m2 / total 208.59 m2NIVEL 6- Local 41 / 47.52 m2- Local 42 / 35.15 m2 / terraza 41.61 m2 / total 76.76 m2* Precios y disponibilidad al 1 de Febrero del 2019 y sujeto a cambiosID-1408",
            "bedrooms": None,
            "bathrooms": None,
            "half_bathrooms": None,
            "parking_spaces": 154,
            "lot_size": 0.0,
            "construction_size": 36.0,
            "lot_length": 0.0,
            "lot_width": 0.0,
            "floors": None,
            "floor": None,
            "age": None,
            "internal_id": None,
            "expenses": None,
            "location": {
                "name": "Valle de Vasconcelos, San Pedro Garza García, Nuevo León",
                "latitude": 25.6645281,
                "longitude": -100.4154254,
                "street": "",
                "postal_code": "",
                "show_exact_location": True,
                "hide_exact_location": False,
                "exterior_number": "",
                "interior_number": ""
            },
            "property_type": "Local en centro comercial",
            "created_at": "2019-04-17T18:21:19-05:00",
            "updated_at": "2020-12-14T17:07:37-06:00",
            "published_at": "2020-12-14T17:07:37-06:00",
            "operations": [
                {
                    "type": "sale",
                    "amount": 2945600.0,
                    "currency": "MXN",
                    "formatted_amount": "$2,945,600",
                    "commission": {
                        "type": "percentage"
                    },
                    "unit": "total"
                }
            ],
            "property_files": [
                "https://assets.stagingeb.com/property_files/25357/326/Ana%CC%81lisis_comp..pdf"
            ],
            "videos": [],
            "virtual_tour": None,
            "collaboration_notes": None,
            "public_url": "https://www.stagingeb.com/mx/inmueble/locales-comerciales-en-venta-vasconcelos-san-pedro-garza-garcia-81b8365f-0c71-4806-bdc0-3eae76379b26",
            "tags": [],
            "show_prices": True,
            "share_commission": False,
            "property_images": [
                {
                    "title": "",
                    "url": "https://assets.stagingeb.com/property_images/25357/49606/EB-B5357.jpg?version=1601049752"
                }
            ],
            "agent": {
                "id": 2829,
                "name": "Alejandro Blanco Zivec",
                "full_name": "Alejandro Blanco Zivec",
                "mobile_phone": "5512123132",
                "profile_image_url": "https://assets.stagingeb.com/profile_images/2829/Alex__1___scaled_.jpg",
                "email": "ablanco+prueba5@easybroker.com"
            },
            "features": [
                {
                    "name": "Balcón",
                    "category": "Exterior"
                }
            ]
        }

        mock_requests_get.return_value = Mock()
        mock_requests_get.return_value.ok = True
        mock_requests_get.return_value.json.return_value = property
        response = Properties().getProperty('EB-B5357')
        
        self.assertEqual(response.json(), property)