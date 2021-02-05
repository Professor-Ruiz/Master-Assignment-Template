import pytest
import src.exercise

out_1 = ['hello']

def test_capture_stdout(capsys, out_1):
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()

    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == out_1
