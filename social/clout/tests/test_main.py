import unittest

from clout.main import Clout


class TestClout(unittest.TestCase):
    """
    Test Clout() class and its methods
    """

    def test_follow(self):
        clout = Clout()
        clout.follow('nancy', 'ben')

        self.assertEqual(clout.people['ben'].score, 1)
        self.assertEqual(clout.people['nancy'].score, 0)

    def test_follow_accumulates(self):
        clout = Clout()
        clout.follow('alfred', 'nancy')
        clout.follow('nancy', 'andrew')
        clout.follow('andrew', 'alicia')

        self.assertEqual(clout.people['alicia'].score, 3)
        self.assertEqual(clout.people['andrew'].score, 2)
        self.assertEqual(clout.people['nancy'].score, 1)
        self.assertEqual(clout.people['alfred'].score, 0)

    def test_follow_accumulates_2(self):
        clout = Clout()
        clout.follow('alfred', 'nancy')
        clout.follow('andrew', 'nancy')

        self.assertEqual(clout.people['nancy'].score, 2)
        self.assertEqual(clout.people['alfred'].score, 0)
        self.assertEqual(clout.people['andrew'].score, 0)

    def test_follow_accumulates_3(self):
        clout = Clout()
        clout.follow('alfred', 'nancy')
        clout.follow('nancy', 'alfred')
        clout.follow('nancy', 'andrew')

        self.assertEqual(clout.people['nancy'].score, 1)
        self.assertEqual(clout.people['alfred'].score, 2)
        self.assertEqual(clout.people['andrew'].score, 2)

    def test_follow_follows_self(self):
        clout = Clout()
        follows = clout.follow('nancy', 'nancy')

        self.assertFalse(follows)
        self.assertEqual(clout.people['nancy'].score, 0)

    def test_follow_follows_twice(self):
        clout = Clout()
        follows_once = clout.follow('nancy', 'ben')
        follows_twice = clout.follow('nancy', 'ben')

        self.assertTrue(follows_once)
        self.assertFalse(follows_twice)
        self.assertEqual(clout.people['ben'].score, 1)

    def test_clout_default(self):
        # TODO: mock follow() method since that is not what we are testing.
        clout = Clout()
        clout.follow('nancy', 'ben')
        clout_string = clout.clout()
        expected_clout_string = "ben has 1 follower(s).\nnancy has 0 follower(s).\n"

        self.assertEqual(clout_string, expected_clout_string)

    def test_clout_person(self):
        # TODO: mock follow() method since that is not what we are testing.
        clout = Clout()
        clout.follow('nancy', 'ben')
        clout_string = clout.clout('ben')
        expected_clout_string = "ben has 1 follower(s).\n"

        self.assertEqual(clout_string, expected_clout_string)

    # TODO: Add more negative tests to try to break things.

    # TODO: Write tests for get_person_by_name() method.

    # TODO: Write tests for Person().

if __name__ == '__main__':
    unittest.main()