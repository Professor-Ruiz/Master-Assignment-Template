import pytest
import src.exercise

inp_1 = ['bianca']
out_1 = ['bianca']

def test_capture_stdout(capsys):
    
    # Load the test input for the program execution:
    def mock_input(s):
        return inp_1.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()

    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == out_1
