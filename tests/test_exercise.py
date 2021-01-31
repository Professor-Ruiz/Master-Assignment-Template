import pytest
import src.exercise

def test_case_1(capsys):
    ''' Captures the output of the program, and verifies it is alphabetized '''
    
    # Test input and output:
    input_values = ["Snickerdoodle Cupcake","Biscoff Lava","Pumpkin Chocolate Chip"]
    assert_out =   '\nBiscoff Lava\nPumpkin Chocolate Chip\nSnickerdoodle Cupcake\n'
    
    # Cycle the sample input through the student program:
    def mock_input(s):
        return input_values.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print stateements):
    src.exercise.main()
    out, err = capsys.readouterr()
    
    # Test the actual program output against the anticipated program output:
    assert out == assert_out
    assert err == ''

def test_case_2(capsys):
    ''' Captures the output of the program, and verifies it is alphabetized '''
    
    # Test input and output:
    input_values = ["Lemon Glaze","Confetti Cake","Reese's Peanut Butter Chip"]
    assert_out =   "\nConfetti Cake\nLemon Glaze\nReese's Peanut Butter Chip\n"    
    
    # Cycle the sample input through the student program:
    def mock_input(s):
        return input_values.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print stateements):
    src.exercise.main()
    out, err = capsys.readouterr()
    
    # Test the actual program output against the anticipated program output:
    assert out == assert_out
    assert err == ''  
