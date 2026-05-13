from django.test import SimpleTestCase


class HomeViewTests(SimpleTestCase):
    def test_home_returns_api_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
