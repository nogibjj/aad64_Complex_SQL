import unittest
from unittest.mock import patch
from mylib.data import general_query


class TestElectricityFunctionsPartOne(unittest.TestCase):
    @patch("mylib.data.sql.connect")
    def test_general_query(self, mock_connect):
        mock_cursor = (
            mock_connect.return_value.__enter__.return_value.cursor.return_value
        )
        mock_cursor.fetchall.return_value = [(1, "John", 25), (2, "Jane", 30)]
        query = "SELECT * FROM test_table"
        general_query(query)
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.fetchall.assert_called_once()


if __name__ == "__main__":
    unittest.main()
