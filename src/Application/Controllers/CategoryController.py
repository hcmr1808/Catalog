from flask import Blueprint, jsonify, request # type: ignore
from src.Application.UseCases.Category.CreateCategory import CreateCategory
from src.Application.UseCases.Category.GetCategory import GetCategory
from src.Application.UseCases.Category.ListCategory import ListCategory
import psycopg2

category_controller = Blueprint('category_controller', __name__)

list_category = ListCategory()
get_category = GetCategory()


@category_controller.route('/categories', methods=['GET'])
def list_categories():
    categories = list_category.execute()
    return jsonify(categories), 200

@category_controller.route('/categories/<string:id>', methods=['GET'])
def get_category_by_id(id):
    category = get_category.execute(id)
    if category:
        return jsonify(category), 200
    else:
        return jsonify({"error": "Category not found"}), 404

@category_controller.route('/categories', methods=['POST'])
def create_category():
    create_category = CreateCategory()
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    category = create_category.execute(name, description)

    if category:
        return jsonify({"id": category, "name": name, "description": description}), 201
    else:
        return jsonify({"error": "Error creating category"}), 400

