from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

import json


URLS = {
    "create_user": "/chains/create_user/"
}


class AccountTestCase(APITestCase):
    def setUp(self):
        self.example_account = {
            "username": "testUser",
            "email": "testUser@email.com",
            "password1": "password",
            "password2": "password"
        }

    def test_create_user(self):
        response = self.client.post(
            URLS["create_user"], self.example_account)
        data = response.data
        self.assertEqual(data["error"], False)

    def test_duplicate_user_errors(self):
        self.client.post(URLS["create_user"], self.example_account)
        response = self.client.post(URLS["create_user"], self.example_account)
        data = response.data
        errors = json.loads(data["data"]["errors"])
        self.assertTrue(data["error"])
        self.assertEqual(
            errors["username"][0]["message"],
            "The username testUser already exists.")
        self.assertEqual(errors["email"][0]["message"],
                         "The email testUser@email.com has already been used")

    def test_miss_matching_passwords(self):
        self.example_account["password2"] = "Password2"
        response = self.client.post(
            URLS["create_user"], self.example_account)
        data = response.data
        errors = json.loads(data["data"]["errors"])
        self.assertTrue(data["error"])
        self.assertEqual(
            errors["password1"][0]["message"],
            "Passwords did not match"
        )
