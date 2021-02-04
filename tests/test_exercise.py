'''
-- How to customize --
For each new assignment template made from this repo,
the only changes needed to test_exercise.py
are the input/output pairs: inp_1, out_1, inp_2, out_2

-- How to format your inputs --
A list of strings
    - even if only 1 value
    - even if numbers
    - Exclude any input() function prompts.
    - Exclude newline characters (\n)
Example inputs:
inp_1 = ['5']
inp_2 = ['Jane','Doe']

-- How to format your outputs --
A list of strings
    - Each string should correspond to a line of output on the console
    - Exclude any input() function prompts
    - Exclude any blank lines (newline characters, \n)

(Professor Bianca Ruiz)
References:
- https://docs.pytest.org/en/stable/parametrize.html
- https://docs.pytest.org/en/stable/capture.html
'''
import pytest
import src.exercise

inp_1 = []
out_1 = ['Hello']

# run the test function for each input/output pair
@pytest.mark.parametrize("test_input, expected", [(inp_1, out_1)])
def test_capture_stdout(capsys, test_input, expected):

    # Load the test input for the program execution:
    def mock_input(s):
        return test_input.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()
    
    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding all newline characters.
    out = out.strip().split('\n')
    out = [i for i in out if i]
    
    # Test the actual program output against the anticipated program output:
    assert out == expected
