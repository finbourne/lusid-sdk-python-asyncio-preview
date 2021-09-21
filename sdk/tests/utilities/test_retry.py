import unittest

import asynctest
import lusid_asyncio.api
from lusid_asyncio import ApiException
from lusid_asyncio.utilities import ApiClientFactory

from tests.utilities import CredentialsSource


class MockApi:
    invocations = 0

    def __init__(self, api_client):
        pass

    def execute_retryable_call(self, *args, **kwargs):

        if self.invocations < 2:
            self.invocations += 1

            # include Retry-After header
            failed_response = type("FailedHttpResponse", (object,), {
                "getheaders": lambda: {"Retry-After": 0.1},
                "status": 429,
                "reason": "retryable",
                "data": None
            })

            raise ApiException(429, http_resp=failed_response)
        else:
            self.invocations += 1
            return self.invocations

    def execute_non_retryable_call(self):

        self.invocations += 1

        # no Retry-After header
        failed_response = type("FailedHttpResponse", (object,), {
            "getheaders": lambda: {},
            "status": 404,
            "reason": "non-retryable",
            "data": None
        })

        raise ApiException(404, http_resp=failed_response)

    def execute_failing_retryable(self, *args, **kwargs):
        self.invocations += 1

        # include Retry-After header
        failed_response = type("FailedHttpResponse", (object,), {
            "getheaders": lambda: {"Retry-After": 0.1},
            "status": 404,
            "reason": "non-retryable",
            "data": None
        })

        raise ApiException(404, http_resp=failed_response)


class RetryTests(asynctest.TestCase):
    factory = None

    def setUp(self):
        # add mock to the module
        lusid_asyncio.api.MockApi = MockApi
        self.factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())

    async def test_non_retryable_is_not_retried(self):
        api = self.factory.build(MockApi)

        with self.assertRaises(ApiException) as ex:
            api.execute_non_retryable_call()

        self.assertEqual(ex.exception.status, 404)
        self.assertEqual(api.invocations, 1)

    async def test_retry_when_lusid_response_contains_retry_header(self):
        api = self.factory.build(MockApi)

        api.execute_retryable_call()

        self.assertEqual(api.invocations, 3)

    async def test_retry_after_max_attempts_fails(self):
        api = self.factory.build(MockApi)

        with self.assertRaises(ApiException) as ex:
            api.execute_failing_retryable()

        self.assertEqual(ex.exception.status, 404)
        self.assertEqual(api.invocations, 3)

    async def test_providing_positional_arguments_success(self):
        api = self.factory.build(MockApi)

        api.execute_retryable_call("Portfolio")

        self.assertEqual(api.invocations, 3)

    async def test_providing_keyword_arguments_success(self):
        api = self.factory.build(MockApi)

        api.execute_retryable_call(name="Portfolio")

        self.assertEqual(api.invocations, 3)

    async def test_providing_positional_keyword_arguments_success(self):
        api = self.factory.build(MockApi)

        api.execute_retryable_call("Portfolio", name="Portfolio")

        self.assertEqual(api.invocations, 3)

    async def test_providing_retry_override_argument_success(self):
        api = self.factory.build(MockApi)

        with self.assertRaises(ApiException) as ex:
            api.execute_failing_retryable("Portfolio", name="Portfolio", lusid_retries=10)

        self.assertEqual(ex.exception.status, 404)
        self.assertEqual(api.invocations, 10)

    async def test_providing_retry_override_argument_not_int_uses_default(self):
        api = self.factory.build(MockApi)

        with self.assertRaises(ApiException) as ex:
            api.execute_failing_retryable("Portfolio", name="Portfolio", lusid_retries="ThisWontWork")

        self.assertEqual(ex.exception.status, 404)
        self.assertEqual(api.invocations, 3)

    async def test_providing_retry_override_with_no_retry_invokes_call(self):
        api = self.factory.build(MockApi)

        api.execute_retryable_call("Portfolio", name="Portfolio", lusid_retries=0)

        self.assertEqual(api.invocations, 1)

    async def test_providing_retry_invokes_call(self):
        with self.assertRaises(ApiException) as ex:
            self.factory.build(lusid_asyncio.InstrumentsApi).get_instrument(
                identifier_type="doesnt_exist",
                identifier="blah",
                lusid_retries=1
            )

        self.assertEqual(ex.exception.status, 400)
