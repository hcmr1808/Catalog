from unittest.mock import patch, MagicMock
import pytest

from src.Application.UseCases.Category.ListCategory import ListCategory

def test_ListCategory():
    mock_connection = MagicMock()
    mock_cursor = mock_connection.cursor.return_value
    mock_categories = [('id1', 'Category 1', 'Description 1'), ('id2', 'Category 2', 'Description 2')]

    mock_cursor.fetchall.return_value = mock_categories

    with patch('psycopg2.connect', return_value=mock_connection):
        listCategory = ListCategory()
        categories = listCategory.execute()

        mock_cursor.execute.assert_called_once_with("SELECT * FROM CATEGORY")
        assert categories == mock_categories

if __name__ == "__main__":
    pytest.main([__file__])
