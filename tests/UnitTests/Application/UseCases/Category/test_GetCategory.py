from unittest.mock import patch, MagicMock
import pytest

from src.Application.UseCases.Category.GetCategory import GetCategory

def test_GetCategory():
    mock_connection = MagicMock()
    mock_cursor = mock_connection.cursor.return_value
    mock_category = ('id1', 'Category 1', 'Description 1')
    
    mock_cursor.fetchone.return_value = mock_category
    
    with patch('psycopg2.connect', return_value=mock_connection):
        id = 'id1'
        getCategory = GetCategory()
        category = getCategory.execute(id)
        
        mock_cursor.execute.assert_called_once_with("SELECT * FROM CATEGORY WHERE id = %s",(id,))
        assert category == mock_category

if __name__ == "__main__":
    pytest.main([__file__])
