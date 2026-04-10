import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):

    @patch("weather_service.api_client.fetch_weather_data")
    def test_get_weather_success(self, mock_fetch):
        mock_fetch.return_value = {
            "city": "London",
            "temp": 25,
            "condition": "sunny",
            "humidity": 50,
        }

        result = weather_service.get_weather("London")
        self.assertEqual(result["temp"], 25)
        self.assertEqual(result["condition"], "sunny")

    @patch("weather_service.api_client.fetch_weather_data")
    def test_get_weather_api_error(self, mock_fetch):
        mock_fetch.side_effect = Exception("API failure")

        result = weather_service.get_weather("London")
        self.assertEqual(result["error"], "api failure")

    @patch("weather_service.api_client.fetch_weather_data")
    def test_get_weather_timeout(self, mock_fetch):
        mock_fetch.side_effect = TimeoutError()

        result = weather_service.get_weather("London")
        self.assertEqual(result["error"], "timeout")

    @patch("weather_service.api_client.fetch_forecast")
    def test_get_forecast_with_patch(self, mock_fetch):
        mock_fetch.return_value = [
            {"temp": 20, "condition": "sunny"},
            {"temp": 18, "condition": "cloudy"},
        ]

        result = weather_service.get_forecast("London", 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["temp"], 20)

    @patch("weather_service.api_client.get_current_hour")
    def test_greeting_morning(self, mock_hour):
        mock_hour.return_value = 8

        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good morning!")

    @patch("weather_service.api_client.get_current_hour")
    def test_greeting_afternoon(self, mock_hour):
        mock_hour.return_value = 14

        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good afternoon!")

    @patch("weather_service.api_client.get_current_hour") # extra test , not in CANVAS task for M02
    def test_get_current_time_mocked(self, mock_hour):
        mock_hour.return_value = 22  # simulate 10 PM

        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good evening!")


if __name__ == "__main__":
    unittest.main()
