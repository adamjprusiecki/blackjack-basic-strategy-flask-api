import pytest
import pandas as pd
from app import get_hard_total_df, get_soft_total_df, get_splilt_df
from util.hard_total_combinations import hard_total_combinations
from util.soft_hand_combinations import soft_hand_combinations
from util.split_hand_combinations import split_hand_combinations

hard_df_csv = pd.read_csv("config/hard.csv")
soft_df_csv = pd.read_csv("config/soft.csv")
split_df_csv = pd.read_csv("config/split.csv")

hard_df_func = get_hard_total_df()
soft_df_func = get_soft_total_df()
split_df_func = get_splilt_df()

is_ten = ['10','T','J','Q','K']
def convert_to_key_if_is_ten_or_ace(card: str) -> str:
    if card == 'A':
        return '11'
    elif card in is_ten:
        return '10'
    else:
        return card

@pytest.mark.parametrize("dealer, player, expected_result", (
    hard_total_combinations
))
def test_hard_table(dealer, player, expected_result):
    csv_ser = hard_df_csv.loc[hard_df_csv['player'] == int(player)][dealer]
    csv_move = csv_ser[csv_ser.index[0]]
    
    func_ser = hard_df_func.loc[hard_df_func['player'] == player][dealer]
    func_move = func_ser[func_ser.index[0]]
    
    assert csv_move == expected_result
    assert func_move == csv_move

@pytest.mark.parametrize("dealer, card1, card2, expected_result", (
    soft_hand_combinations
))
def test_soft_table(dealer, card1, card2, expected_result):
    if dealer != 'A':
        dealer = convert_to_key_if_is_ten_or_ace(dealer)
    
    c1 = convert_to_key_if_is_ten_or_ace(card1)
    c2 = convert_to_key_if_is_ten_or_ace(card2)
    
    csum = int(c1) + int(c2)
    
    csv_ser = soft_df_csv.loc[soft_df_csv['player'] == csum][dealer]
    csv_move = csv_ser[csv_ser.index[0]]
    
    func_ser = soft_df_func.loc[soft_df_func['player'] == str(csum)][dealer]
    func_move = func_ser[func_ser.index[0]]
    
    assert csv_move == expected_result
    assert func_move == csv_move

@pytest.mark.parametrize("dealer, card1, card2, expected_result", (
    split_hand_combinations
))
def test_split_table(dealer, card1, card2, expected_result):
    if dealer != 'A':
        dealer = convert_to_key_if_is_ten_or_ace(dealer)
    
    if card1 != 'A':
        c1 = convert_to_key_if_is_ten_or_ace(card1)
    else:
        c1 = card1
        
    if card2 != 'A':
        c2 = convert_to_key_if_is_ten_or_ace(card2)
    else:
        c2 = card2
    
    csv_ser = split_df_csv.loc[split_df_csv['player'] == c1][dealer]
    csv_move = csv_ser[csv_ser.index[0]]
    
    func_ser = split_df_func.loc[split_df_func['player'] == c2][dealer]
    func_move = func_ser[func_ser.index[0]]
    
    assert csv_move == expected_result
    assert func_move == csv_move
    