import pytest
import src.exercise

def test_case_1(capsys):
    input_values = ["Snickerdoodle Cupcake","Biscoff Lava","Pumpkin Chocolate Chip"]
    
    def mock_input(s):
        return input_values.pop(0)
    src.exercise.input = mock_input
    
    src.exercise.main()
    
    out, err = capsys.readouterr()
    
    assert out == '\nBiscoff Lava\nPumpkin Chocolate Chip\nSnickerdoodle Cupcake\n'
    assert err == ''

def test_case_2(capsys):
    input_values = ["Lemon Glaze","Confetti Cake","Reese's Peanut Butter Chip"]
    
    def mock_input(s):
        return input_values.pop(0)
    src.exercise.input = mock_input
    
    src.exercise.main()
    
    out, err = capsys.readouterr()
    
    assert out == "\nConfetti Cake\nLemon Glaze\nReese's Peanut Butter Chip\n"
    assert err == ''   
