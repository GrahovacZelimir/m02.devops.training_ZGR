import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestEndToEnd(unittest.TestCase):
    
    def test_home_page(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome", response.text)

    def test_add_endpoint(self):
        response = requests.post(f"{BASE_URL}/add", json={"a": 5, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 8)

    def test_subtract_endpoint(self):
        response = requests.post(f"{BASE_URL}/subtract", json={"a": 10, "b": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 6)

    def test_multiply_endpoint(self):
        response = requests.post(f"{BASE_URL}/multiply", json={"a": 3, "b": 7})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 21)

    def test_divide_endpoint(self):
        response = requests.post(f"{BASE_URL}/divide", json={"a": 20, "b": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 5)

    def test_divide_by_zero(self):
        response = requests.post(f"{BASE_URL}/divide", json={"a": 10, "b": 0})
        self.assertEqual(response.status_code, 400)

    def test_health_endpoint(self):
        response = requests.get(f"{BASE_URL}/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
    

if __name__ == "__main__":
    unittest.main()
