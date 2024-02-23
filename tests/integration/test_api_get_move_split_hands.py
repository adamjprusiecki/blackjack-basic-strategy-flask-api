import pytest
from app import app
from util.split_hand_combinations import split_hand_combinations

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    
    yield client

@pytest.mark.parametrize("dealer, card1, card2, expected_result", (
    split_hand_combinations
))
def test_split_hand_pass(dealer, card1, card2, expected_result, client):
    endpoint = f"/get-move?dealer={dealer}&hand={card1},{card2}"
    response = client.get(f"{endpoint}")
    
    recommended_move_key = response.json['recommended move key']
    basic_strategy_table_used = response.json['basic strategy table used']
    
    assert recommended_move_key == expected_result
    assert basic_strategy_table_used == 'split table'
    assert response.status_code == 200
    