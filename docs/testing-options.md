# Testing Options

> Choose one of five autograding option below. I've already pre-written the the testing scripts and integrated them into the assignment so they're automatically > run with each student submission. I've also kept the required edits to a minimum and provided easy and explicit directions for you.
>
> HOT TIP: Put your solution code in [exercise.py](../src/exercise.py) before you begin updating the tests. That way, when you commit your changes to [exercise_test.py](../tests/test_exercise.py), you'll immediately see if it passes the pytest. Just make sure to delete the solution before you make an assignment!


<details>
  <summary><b>One input/output test</b></summary>

> This test will execute your student's program once. You supply the input and expected output. It captures the program output in it's entirety.

```Python
import pytest
import src.exercise

inp_1 = []
out_1 = []

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
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == expected
```
Paste the code above into [exercise_test.py](../tests/test_exercise.py), then update the following:

- The input (```inp_1```) should be a list of string(s):
    - Exclude any ```input()``` function prompts.
    - Exclude newline characters (```\n```).
    
- The output (```out_1```) should be a list of string(s):
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (```\n```).
    
- Example:
  ```Python
   4 inp_1 = ['1']
   5 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  ```

</details>


<br>
<details>
  <summary><b>Two input/output tests</b></summary>

> This test will execute your student's program twice. You supply the input and expected output for each execution. It captures the program output in it's entirety.

```Python
import pytest
import src.exercise

inp_1 = []
out_1 = []

inp_2 = []
out_2 = []

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

    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == expected
```
Paste the code above into [exercise_test.py](../tests/test_exercise.py), then update the following:

- The inputs (```inp_1```, ```inp_2```) should be lists of string(s):
    - Exclude any ```input()``` function prompts.
    - Exclude newline characters (```\n```).
    
- The outputs (```out_1```, ```out_2```) should be lists of string(s):
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (```\n```).
    
- Example:
  ```Python
   4 inp_1 = ['1']
   5 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  ```
</details>

<br>

<details>
  <summary><b>Three input/output tests</b></summary>

> This test will execute your student's program three times. You supply the input and expected output for each execution. It captures the program output in it's entirety. 

```Python
import pytest
import src.exercise

inp_1 = []
out_1 = []

inp_2 = []
out_2 = []

inp_3 = []
out_3 = []

# run the test function for each input/output pair
@pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2), (inp_3, out_3)])
def test_capture_stdout(capsys, test_input, expected):
    
    # Load the test input for the program execution:
    def mock_input(s):
        return test_input.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()

    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == expected
```
Paste the code above into [exercise_test.py](../tests/test_exercise.py), then update the following:

- The inputs (```inp_1```, ```inp_2```, ```inp_3```) should be lists of string(s):
    - Exclude any ```input()``` function prompts.
    - Exclude newline characters (```\n```).
    
- The outputs (```out_1```, ```out_2```, ```out_3```) should be lists of string(s):
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (```\n```).
    
- Example:
  ```Python
   4 inp_1 = ['1']
   5 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  ```

</details>

<br>
<details>
  <summary><b>One test, no input</b></summary>

> This test will execute your student's program once. You supply the expected output. It captures the program output in it's entirety. 

```Python
import pytest
import src.exercise

inp_1 = []
out_1 = []

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
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == expected
```
Paste the code above into [exercise_test.py](../tests/test_exercise.py), then update the following:

- The input (```inp_1```) should remain an empty list.
    
- The output (```out_1```) should be a list of string(s):
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (```\n```).
    
- Example:
  ```Python
   4 inp_1 = []
   5 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  ```

</details>

<br>
<details>
  <summary><b>Test for a specific string in the program output</b></summary>

> This test will execute your student's program twice. You supply the inputs and the test strings. The test captures the program output in it's entirety. Then it tests if the given string is in the program output.
    
```Python
import pytest
import src.exercise

inp_1 = []
out_1 = []

inp_2 = []
out_2 = []

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
    assert expected in out
```
Paste the code above into [exercise_test.py](../tests/test_exercise.py), then update the following:

- The inputs (```inp_1```, ```inp_2```) should be lists of string(s):
    - Exclude any ```input()``` function prompts.
    - Exclude newline characters (```\n```).
    
- The outputs (```out_1```, ```out_2```) should be the test strings:
    - They should be a single string, enclosed in quotes.
    
- Example:
  ```Python
   4 inp_1 = ['1']
   5 out_1 = 'One'
  ```

  <br>
</details>
<br><br>

*All tests created and shared by :purple_heart: Bianca Ruiz :purple_heart:*

*Github: @RuizTheRuler*
