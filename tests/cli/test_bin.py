from unittest import TestCase
import logging

from dataflow.bin.cli import parse_cmd_args

logger = logging.getLogger(__name__)


class CliTest(TestCase):

    def test_command_parsing(self):
        logger.info("Sample")
        self.assertTrue(True, "Why would you do that")


class CliTest2(TestCase):

    def test_command_parsing(self):
        parse_cmd_args()
        self.assertTrue(True, "Why would you do that")
