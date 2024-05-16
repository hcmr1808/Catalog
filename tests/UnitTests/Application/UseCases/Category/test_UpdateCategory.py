from src.Application.UseCases.Category.UpdateCategory import UpdateCategory
from unittest.mock import patch, MagicMock

def test_ValidUpdateCategory():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    with patch('psycopg2.connect', return_value=mock_conn):
        updateCategory = UpdateCategory()

        category_id = '1'
        name = "Updated Category"
        description = "Updated description"

        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('1', "Old category", "Old description", True)

        with patch.object(updateCategory, 'execute', return_value=(True, "Category updated successfully")) as mock_execute:
            sucess, message = updateCategory.execute(category_id, name, description)
            mock_execute.assert_called_once_with(category_id, name, description)

            assert sucess is True
            assert message == "Category updated successfully"

def test_InvalidUpdateCategory():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    with patch('psycopg2.connect', return_value=mock_conn):
        updateCategory = UpdateCategory()

        category_id = '1'
        name = ""
        description = "Updated description"

        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('1', "Old category", "Old description", True)

        with patch.object(updateCategory, 'execute', return_value=(False, "Category update failed")) as mock_execute:
            sucess, message = updateCategory.execute(category_id, name, description)
            mock_execute.assert_called_once_with(category_id, name, description)

            assert sucess is False
            assert message == "Category update failed"