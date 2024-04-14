from flask import Blueprint, jsonify

budget_routes = Blueprint('budget_routes', __name__)

@budget_routes.route('/get_budgets')
def get_budgets():
    return jsonify({'message': 'This is a placeholder response for get_budgets'})

@budget_routes.route('/save_budget', methods=['POST'])
def save_budget():
    return jsonify({'message': 'This is a placeholder response for save_budget'})
