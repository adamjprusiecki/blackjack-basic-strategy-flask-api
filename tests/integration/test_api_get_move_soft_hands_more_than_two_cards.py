import pytest
from app import app
from util.soft_hand_more_than_2_card_combinations import soft_hand_more_than_two_cards

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    
    yield client

@pytest.mark.parametrize("dealer, cards, expected_result", (
    soft_hand_more_than_two_cards
))
def test_soft_hand__more_than_two_pass(dealer, cards, expected_result, client):
    endpoint = f"/get-move?dealer={dealer}&hand=" 
    for card in cards:
        endpoint += f"{card},"
    endpoint = endpoint[:-1]
    
    response = client.get(f"{endpoint}")
    
    recommended_move_key = response.json['recommended move key']
    basic_strategy_table_used = response.json['basic strategy table used']
    
    assert recommended_move_key == expected_result
    assert basic_strategy_table_used == 'soft total table'
    assert response.status_code == 200
    