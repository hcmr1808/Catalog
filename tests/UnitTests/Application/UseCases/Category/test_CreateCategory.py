from unittest.mock import patch, MagicMock
import pytest

from src.Application.UseCases.Category.CreateCategory import CreateCategory

def test_ValidCreateCategory():
    mock_connection = MagicMock()
    
    with patch('psycopg2.connect',return_value=mock_connection):
        createCategory = CreateCategory()

        name = "Test Category"
        description = "This is a test description"

        with patch.object(createCategory, 'execute', return_value=(True, "Category created successfully")) as mock_execute:
            success, message = createCategory.execute(name, description)

            mock_execute.assert_called_once_with(name, description)

            assert success is True
            assert message == "Category created successfully"

def test_InvalidCreateCategory():
    mock_connection = MagicMock()

    with patch('psycopg2.connect', return_value=mock_connection):

        createCategory = CreateCategory()

        name = ""
        description = "This is a test description"

        with patch.object(createCategory, 'execute', return_value=(False, "Error: Name cannot be empty")) as mock_execute:
            success, message = createCategory.execute(name, description)

            mock_execute.assert_called_once_with(name, description)

            assert success is False
            assert message == "Error: Name cannot be empty"

if __name__ == "__main__":
    pytest.main([__file__])
