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
from kafka_mgmt_client.model.kafka_request import KafkaRequest
from kafka_mgmt_client.model.kafka_request_list_all_of import KafkaRequestListAllOf
from kafka_mgmt_client.model.list import List
globals()['KafkaRequest'] = KafkaRequest
globals()['KafkaRequestListAllOf'] = KafkaRequestListAllOf
globals()['List'] = List
from kafka_mgmt_client.model.kafka_request_list import KafkaRequestList


class TestKafkaRequestList(unittest.TestCase):
    """KafkaRequestList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testKafkaRequestList(self):
        """Test KafkaRequestList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = KafkaRequestList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
