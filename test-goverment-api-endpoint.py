import unittest
import requests

URL_GOV = "https://flamxby.herokuapp.com/"

class TestGovermentAPIEndpoint(unittest.TestCase) :
    
    def test_get_exist_user(self):
        endpoint = URL_GOV + "user/1155448765415"
        res = requests.get(endpoint)
        res_dict = res.json()
        self.assertEqual(res_dict["user_id"], 3)


    def test_get_unexist_user(self):
        endpoint = URL_GOV + "user/0155448765415"
        res = requests.get(endpoint)
        self.assertEqual(res.status_code, 404)


    def test_valid_login(self):
        endpoint = URL_GOV + "login/"
        bodys = {
            "username" : "1155448765415",
            "password": "password1234"
        }
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        res = requests.post(endpoint, data=bodys, headers=headers)
        self.assertEqual(res.status_code, 200)


    def test_invalid_password_login(self):
        endpoint = URL_GOV + "login/"
        bodys = {
            "username" : "1155448765415",
            "password": "password"
        }
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        res = requests.post(endpoint, data=bodys, headers=headers)
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()