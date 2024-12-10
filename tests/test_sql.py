
import pytest
from src.database import session
from src.models import InvestmentFund

@pytest.fixture
def setup_db():
    """
    This fixture sets up and tears down the database for each test.
    It creates and deletes a fund for testing.
    """
    # Create a new fund for testing
    fund = InvestmentFund(
        name="Test Fund",
        manager="Test Manager",
        nav=1000.0,
        performance=5.0
    )
    session.add(fund)
    session.commit()  # Commit the transaction to save to the database
    yield fund  # Yield the fund for testing
    # Cleanup after test
    session.delete(fund)
    session.commit()

def test_create_fund_db(setup_db):
    """
    Test that a fund is correctly inserted into the database.
    """
    fund = setup_db
    assert fund.id is not None  # Ensure that the fund has been assigned an ID
    assert fund.name == "Test Fund"  # Verify the fund name
    assert fund.manager == "Test Manager"  # Verify the fund manager

def test_update_fund_performance(setup_db):
    """
    Test that the performance of a fund is correctly updated.
    """
    fund = setup_db
    new_performance = 6.0
    fund.performance = new_performance
    session.commit()  # Commit the updated performance
    updated_fund = session.query(InvestmentFund).get(fund.id)
    assert updated_fund.performance == new_performance  # Verify performance update

def test_delete_fund_db(setup_db):
    """
    Test that a fund can be deleted from the database.
    """
    fund = setup_db
    session.delete(fund)
    session.commit()  # Commit the deletion
    deleted_fund = session.query(InvestmentFund).get(fund.id)
    assert deleted_fund is None  # Ensure the fund no longer exists
