"""
    Kafka Management API

    Kafka Management API is a REST API to manage Kafka instances  # noqa: E501

    The version of the OpenAPI document: 1.11.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_mgmt_client
from kafka_mgmt_client.model.instant_query import InstantQuery
from kafka_mgmt_client.model.metrics_instant_query_list_all_of import MetricsInstantQueryListAllOf
globals()['InstantQuery'] = InstantQuery
globals()['MetricsInstantQueryListAllOf'] = MetricsInstantQueryListAllOf
from kafka_mgmt_client.model.metrics_instant_query_list import MetricsInstantQueryList


class TestMetricsInstantQueryList(unittest.TestCase):
    """MetricsInstantQueryList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricsInstantQueryList(self):
        """Test MetricsInstantQueryList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricsInstantQueryList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
