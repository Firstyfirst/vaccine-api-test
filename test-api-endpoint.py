import unittest
import requests

URL = "https://suchonsite-server.herokuapp.com/"

class TestAPIEndpoint(unittest.TestCase):
    """This class created for testing API endpoints of suchonsite at 23-10-2021"""
    

    def test_get_all_people(self):
        """The general test for test get_all_people API work correctly.
        so, when you enter this url, the web-site will respone status 200. 
        """

        endpoint = URL + "people/all"
        res = requests.get(endpoint)
        self.assertEqual(res.status_code, 200)
        

    def test_get_all_people_is_json_or_not(self):
        """This test is used for check get_all_people API that is in json from."""

        endpoint = URL + "people/all"
        res = requests.get(endpoint)
        self.assertEqual("application/json; charset=utf-8", res.headers["Content-Type"])


    def test_get_had_appointment(self):
        """The general test for get_people_by_date with correct date format
        so, it will get the json form. 
        """

        endpoint = URL + "people/by_date/20-10-2021"
        res = requests.get(endpoint)
        self.assertEqual("application/json; charset=utf-8", res.headers["Content-Type"])


    def test_get_not_had_appointment(self):
        """The test for get the result when user enter the correct date format
        but do not have the appointment in the queue. Thus it should return 
        empty string.
        """

        endpoint = URL + "people/by_date/23-10-2021"
        res = requests.get(endpoint)
        self.assertEqual(res.text, "")


    def test_get_inexisted_appointment(self):
        """Test the inexisted date (In this test, I use 32 because it does not
        have the 32th day in the month.) so, it should return 404 not found.
        """

        endpoint = URL + "people/by_date/32-10-2021"
        res = requests.get(endpoint)
        self.assertEqual(res.status_code, 404)


    def test_get_wrong_date_format(self):
        """Test the wrong date format. The correct format must be only the integer
        but, this case use the abbriviation of month instead. So that, it should
        return the 404 not found status. 
        """

        endpoint = URL + "people/by_date/20-Oct-2021"
        res = requests.get(endpoint)
        self.assertEqual(res.status_code, 404)


    def test_get_wrong_url_format(self):
        """Test wrong url format (In this test case, I cut the part of specific date
        to make it wrong) thus, it should return 404 not found status"""

        endpoint = URL + "people/by_date"
        res = requests.get(endpoint)
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()