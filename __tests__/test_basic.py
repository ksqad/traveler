from __tests__.base import BaseTestCase

class TravelerTestCase(BaseTestCase):

    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    BaseTestCase.TestCase.run()