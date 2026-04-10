import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestSecurity(unittest.TestCase):
    def setUp(self):
        try:
            resp = requests.get(f"{BASE_URL}/health", timeout=2)
        except Exception:
            self.skipTest("Flask app is not running on 127.0.0.1:5000")
            return

        if resp.status_code != 200:
            self.skipTest("Flask app health check failed")

    def test_missing_field_a(self):
        resp = requests.post(f"{BASE_URL}/add", json={"b": 2}, timeout=2)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_missing_field_b(self):
        resp = requests.post(f"{BASE_URL}/add", json={"a": 1}, timeout=2)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_invalid_data_type(self):
        resp = requests.post(f"{BASE_URL}/add", json={"a": "abc", "b": 2}, timeout=2)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_empty_string_value(self):
        resp = requests.post(f"{BASE_URL}/add", json={"a": "", "b": 2}, timeout=2)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_very_large_number(self):
        resp = requests.post(
            f"{BASE_URL}/add",
            json={"a": 10**20, "b": 1},
            timeout=2,
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_malformed_json(self):
        resp = requests.post(
            f"{BASE_URL}/add",
            data='{"a": 1, "b":',
            headers={"Content-Type": "application/json"},
            timeout=2,
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_division_by_zero_returns_safe_error(self):
        resp = requests.post(f"{BASE_URL}/divide", json={"a": 1, "b": 0}, timeout=2)
        self.assertEqual(resp.status_code, 400)
        payload = resp.json()
        self.assertIn("error", payload)
        self.assertNotIn("Traceback", str(payload))


if __name__ == "__main__":
    unittest.main()
