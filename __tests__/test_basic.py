from __tests__.base import BaseTestCase

class TravelerTestCase(BaseTestCase):

    def test_index(self):
        self.assertEqual(199 + 1, 200)

if __name__ == '__main__':
    BaseTestCase.TestCase.run()