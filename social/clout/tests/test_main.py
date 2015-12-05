import unittest

from clout.main import Clout


class TestClout(unittest.TestCase):
    """
    Test Clout() class and its methods
    """

    def test_follow(self):
        clout = Clout()
        clout.follow('nancy', 'ben')

        self.assertEqual(clout.get_person_by_name('ben').score, 1)
        self.assertEqual(clout.get_person_by_name('nancy').score, 0)

    def test_follow_from_example(self):
        clout = Clout()
        clout.follow('neymar', 'xavi')
        # neymar = 0, xavi = 1
        clout.follow('neymar', 'messi')
        # neymar = 0, xavi = 0, messi = 1
        clout.follow('messi', 'messi')
        # neymar = 0, xavi = 0, messi = 1
        clout.follow('pique', 'victor')
        # neymar = 0, xavi = 0, messi = 1, pique = 0, victor = 1
        clout.follow('jordi', 'pique')
        # neymar = 0, xavi = 0, messi = 1, pique = 1, victor = 2, jordi = 0
        clout.follow('messi', 'victor')
        # neymar = 0, xavi = 0, messi = 1, pique = 0, victor = 4, jordi = 0

        self.assertEqual(clout.get_person_by_name('victor').score, 4)
        self.assertEqual(clout.get_person_by_name('messi').score, 1)
        self.assertEqual(clout.get_person_by_name('pique').score, 1)
        self.assertEqual(clout.get_person_by_name('jordi').score, 0)
        self.assertEqual(clout.get_person_by_name('neymar').score, 0)
        self.assertEqual(clout.get_person_by_name('xavi').score, 0)

    def test_follow_follows_self(self):
        clout = Clout()
        follows = clout.follow('nancy', 'nancy')

        self.assertFalse(follows)
        self.assertEqual(clout.get_person_by_name('nancy').score, 0)

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

    # TODO: Write tests for Person() and its methods.

if __name__ == '__main__':
    unittest.main()