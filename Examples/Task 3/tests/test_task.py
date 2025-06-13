import unittest
import subprocess
import os
from platform import system
from academy_tester import Tester


class TestPrintStatements(unittest.TestCase):
    def test_two_print_statements(self):

        t = Tester(self)

        if not t.test_count("print", 1):
            self.fail("You should have print in the output!")

        if not t.get_line_count() >= 2:
            self.fail("Make sure you have more than 2 lines of output!")

        test = t.test_output(["Hello there", "print"])
        if not test.result:
            self.fail(f"{test.output}")
        # self.assertGreaterEqual(
        #     len(output_lines),
        #     2,
        #     msg="You should print a message, and then your name!"
        # )
        #
        # # Optionally, check for errors in stderr
        # self.assertEqual(
        #     stderr,
        #     "",
        #     msg="The script should not produce any errors"
        # )


if __name__ == '__main__':
    unittest.main()