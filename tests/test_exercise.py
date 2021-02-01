'''
For each new assignment template made from this repo,
the only changes needed to test_exercise.py
are the input/output pairs below on lines 12 - 19
Inputs should be entered as a list, even if only 1 value.
Outputs should be a string.
(Professor Bianca Ruiz)
References:
- https://docs.pytest.org/en/stable/parametrize.html
- https://docs.pytest.org/en/stable/capture.html
'''
import pytest
import src.exercise

inp_1 = []
out_1 = ""

inp_2 = []
out_2 = ""

# run the test function for each input/output pair
@pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2)])
def test_capture_stdout(capsys, test_input, expected):

    # Load the test input for the program execution:
    def mock_input(s):
        return test_input.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()
    
    # Test the actual program output against the anticipated program output:
    assert out == expected
