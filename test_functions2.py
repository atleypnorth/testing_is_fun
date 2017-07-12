import unittest
from unittest.mock import patch

from functions2 import name_and_user_id


class TestFunctions2(unittest.TestCase):

    @patch('os.getlogin')
    def test_username(self, mock_getlogin):
        mock_getlogin.return_value = 'username FOO'
        self.assertEqual(name_and_user_id(), 'username FOO')


if __name__ == '__main__':
    unittest.main()
