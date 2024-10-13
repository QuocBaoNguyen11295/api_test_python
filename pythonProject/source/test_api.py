import requests
import unittest


class TestAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    def test_get_user(self):
        response = requests.get(f"{self.BASE_URL}/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", response.json())

    def test_get_nonexistent_user(self):
        response = requests.get(f"{self.BASE_URL}/999")
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        new_user = {
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
        response = requests.post(self.BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], new_user["name"])


if __name__ == '__main__':
    unittest.main()
