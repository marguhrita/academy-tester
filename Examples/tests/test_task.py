import unittest
from academy_tester import OutputTester, ContentTester


class TestPrintStatements(unittest.TestCase):
    def setUp(self):
        self.OTester = OutputTester(self)
        self.CTester = ContentTester(self)
        self.cases = [
            ("81", "A"),
            ("40", "D"),
            ("55", "C"),
            ("41", "D"),
            ("1", "Fail")
        ]

    def testGradeOutput(self):
        
        for points, grade in self.cases:
            print(f"Grade:{grade}")
            print(f"points:{points}")
            self.OTester.test_output(grade, points)


if __name__ == '__main__':
    unittest.main()
