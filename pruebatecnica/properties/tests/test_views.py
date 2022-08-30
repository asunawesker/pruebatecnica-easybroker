from django.test import TestCase

class TestView(TestCase):
    def test_call_view_is_loading_correctly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')