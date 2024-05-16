from unittest.mock import patch, MagicMock
import pytest

from src.Application.UseCases.Category.DeleteCategory import DeleteCategory

def test_DeleteCategory():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    with patch('psycopg2.connect', return_value=mock_conn):
        delete_category = DeleteCategory()

        id = '1'

        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('1', "category", "description", True)

        with patch.object(delete_category, 'execute', return_value=(True, "Category deleted successfully")) as mock_execute:
            success, message = delete_category.execute(id)
            mock_execute.assert_called_once_with(id)

            assert success is True
            assert message is "Category deleted successfully"

def test_InvalidDeleteCategory():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    with patch('psycopg2.connect', return_value=mock_conn):
        delete_category = DeleteCategory()

        id = '2'

        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('1', "category", "description", True)

        with patch.object(delete_category, 'execute', return_value=(False, "Category delete failed")) as mock_execute:
            success, message = delete_category.execute(id)
            mock_execute.assert_called_once_with(id)

            assert success is False
            assert message is "Category delete failed"