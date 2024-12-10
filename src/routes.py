
# src/routes.py
from flask import Blueprint, request, jsonify
from src.database import session
from src.models import InvestmentFund

# Blueprint for modular routing
bp = Blueprint('funds', __name__)

@bp.route('/funds', methods=['GET'])
def get_funds():
    """
    Retrieve a list of all funds.
    """
    funds = session.query(InvestmentFund).all()
    # Convert ORM objects to dictionaries for JSON serialization
    return jsonify([fund.__dict__ for fund in funds])

@bp.route('/funds', methods=['POST'])
def create_fund():
    """
    Create a new fund.
    """
    data = request.json
    fund = InvestmentFund(**data)
    session.add(fund)
    session.commit()
    return jsonify(fund.__dict__), 201  # Return the created fund with status 201 (Created)

@bp.route('/funds/<int:fund_id>', methods=['GET'])
def get_fund(fund_id):
    """
    Retrieve details of a specific fund by its ID.
    """
    fund = session.query(InvestmentFund).get(fund_id)
    if not fund:
        # Return 404 if fund not found
        return jsonify({"error": "Fund not found"}), 404
    return jsonify(fund.__dict__)

@bp.route('/funds/<int:fund_id>/performance', methods=['PUT'])
def update_performance(fund_id):
    """
    Update the performance of a specific fund.
    """
    data = request.json
    fund = session.query(InvestmentFund).get(fund_id)
    if not fund:
        return jsonify({"error": "Fund not found"}), 404
    fund.performance = data.get('performance')
    session.commit()
    return jsonify(fund.__dict__)

@bp.route('/funds/<int:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    """
    Delete a fund by its ID.
    """
    fund = session.query(InvestmentFund).get(fund_id)
    if not fund:
        return jsonify({"error": "Fund not found"}), 404
    session.delete(fund)
    session.commit()
    return '', 204  # Return 204 (No Content) on successful deletion

@bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Fund Management System API"})


@bp.route('/favicon.ico')
def favicon():
    return '', 204  # No Content


