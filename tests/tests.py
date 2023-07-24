from unittest import TestCase, main
import json
import requests

class TestCases(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_new_user(self):

        url = "http://127.0.0.1:8000/newUser"

        payload = json.dumps({
                            "name": "Raja",
                            "email": "raja@gmail.com",
                            "balance": 1000
                            })
        headers = {
                    'Content-Type': 'application/json'
                    }

        response = requests.request("POST", url, headers=headers, data=payload).json()
        
        self.assertEqual(response["status"], "success")
        
    def test_new_merchant(self):
        url = "http://127.0.0.1:8000/newMerchant"

        payload = json.dumps({
        "name": "Spice Factory",
        "email": "spice@gmail.com",
        "fee": 8
        })

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST",url, headers = headers,data = payload).json()
        self.assertEqual(response["status"],"success")

    def test_new_transact(self):
        url = "http://127.0.0.1:8000/transact"

        payload = json.dumps({
        "u_id": 3,
        "m_id": 3,
        "amount": 500
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_getMerchant_id(self):
        url = "http://127.0.0.1:8000/getMerchant/9"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_update_merchant_fee(self):
        url = "http://127.0.0.1:8000/updateFee?mid=7&fee=7"

        payload = ""
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_repay(self):
        url = "http://127.0.0.1:8000/repay?name=Abi&amount=100"

        payload = {}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_fee(self):
        url = "http://127.0.0.1:8000/fee/KFC"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_dues(self):
        url = "http://127.0.0.1:8000/dues/Naren"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_use_limit(self):
        url = "http://127.0.0.1:8000/usersAtLimit"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_total_dues(self):
        url = "http://127.0.0.1:8000/totalDues"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"],"success")

    def test_some_test_Case(self):
        pass
        """
        1. When user limit exceedds should "Return insuffcient funds!" as messasge
        """
        
if __name__ == '__main__':
    main()
    