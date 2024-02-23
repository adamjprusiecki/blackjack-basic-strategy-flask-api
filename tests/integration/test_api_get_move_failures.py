import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    
    yield client

@pytest.mark.parametrize("dealer, card1, card2, expected_result", (
    ('1','A','A','y'),
    ('1,','A','A','y'),
    ('1,1','A','A','y'),
    ('x','A','A','y'),
    ('x,','A','A','y'),
    ('x,x','A','A','y'),
    ('!','A','A','y'),
    ('!,','A','A','y'),
    ('!,!','A','A','y'),
))
def test_get_move_dealer_input_fails(dealer, card1, card2, expected_result, client):
    endpoint = f"/get-move?dealer={dealer}&hand={card1},{card2}"
    response = client.get(f"{endpoint}")
    error = response.json['error']
    
    assert error == f"[{dealer}] is not an allowed character. Allowed characters are [2, 3, 4, 5, 6, 7, 8, 9, 10, T, J, Q, K, A, 11]"
    assert response.status_code == 400


@pytest.mark.parametrize("dealer, card1, card2, expected_result", (
    ('A','1','A','y'),
    ('A','A','1','y'),
    ('A','1','1','y'),
    ('A','x','A','y'),
    ('A','A','X','y'),
    ('A','x','x','y'),
    ('A','!','A','y'),
    ('A','A','!','y'),
    ('A','!','!','y'),
))
def test_get_move_user_input_fails_unallowed_characters(dealer, card1, card2, expected_result, client):
    endpoint = f"/get-move?dealer={dealer}&hand={card1},{card2}"
    response = client.get(f"{endpoint}")
    error = response.json['error']
    
    assert "is not an allowed character. Allowed characters are [2, 3, 4, 5, 6, 7, 8, 9, 10, T, J, Q, K, A, 11]" in error
    assert response.status_code == 400

@pytest.mark.parametrize("dealer, card1, card2, expected_result", (
    ('A','A','','y'),
))
def test_get_move_user_input_fails_with_no_comma(dealer, card1, card2, expected_result, client):
    endpoint = f"/get-move?dealer={dealer}&hand={card1}"
    response = client.get(f"{endpoint}")
    error = response.json['error']
    
    assert error == "Character [,] must exist at least once in hand input [A]" 
    assert response.status_code == 400
