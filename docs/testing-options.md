# Testing Options

<br>
<details>
  <summary><b>Two input/output tests (default)</b></summary>

> This test will execute your student's program twice. You supply the input and expected output for each execution. It captures the program output in it's entirety.
    
<br>

Update [lines 31-35](/tests/test_exercise.py#L31) of test_exercise.py

- The inputs should be a list of strings.
    - Exclude any input() function prompts.
    - Exclude newline characters (```\n```).
    
- The outputs should be a list of strings.
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (```\n```).
    
- Finished Example:
  ```Python
  31 inp_1 = ['1']
  32 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  33 
  34 inp_2 = ['2']
  35 out_2 = ['2 plus 1 is 3', '2 plus 2 is 4', '2 plus 3 is 5']
  ```
</details>

<br>
<details>
  <summary><b>One input/output test</b></summary>

> This test will execute your student's program once. You supply the input and expected output. It captures the program output in it's entirety. You'll need to remove the second input/output pair in the file by following the directions below:

<br>

- Assign the value of the program input to the variable ```inp_1``` on [line 31]() of test_exercise.py
  - It should be a list of string(s) 
  - Exclude any input() function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the value to the expected program output to the variable ```out_1``` on line 32
  - It should be a list of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (\n).

- Delete lines 34-36: ```inp_2``` and ```inp_3```
  
- At (now) line 35, delete ```, (inp_2, out_2)``` from the decorator.
  
- Finished Example:
  ```Python
  31 inp_1 = ['1']
  32 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  33   
  34 # run the test function for each input/output pair
  35 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1)])
  ```

</details>

<br>
<details>
  <summary><b>Three input/output tests</b></summary>

> This test will execute your student's program three times. You supply the input and expected output for each execution. It captures the program output in it's entirety. You'll need to add a third input/output pair in the file by following the directions below:
    
<br>

- Move the code on [line 37](./tests/test_exercise.py) down two lines to line 40

- Insert ```inp_3 = []``` on line 37, and ```out_3 = []``` on line 38

- Assign the value of the program inputs to ```inp_1```, ```inp_2```, and ```inp_3```:
  - They should be a lists of string(s) 
  - Exclude any input() function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the value to the expected program output to ```out_1```, ```out_2```, ```out_3```:
  - They should be a lists of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (\n).
  
- At (now) line 40, add ```, (inp_3, out_3)``` to the decorator.
  
- Finished Example:
  ```Python
  31 inp_1 = ['1']
  32 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  33 
  34 inp_2 = ['2']
  35 out_2 = ['2 plus 1 is 3', '2 plus 2 is 4', '2 plus 3 is 5']
  36
  37 inp_3 = ['3']
  38 out_3 = ['3 plus 1 is 4', '3 plus 2 is 5', '3 plus 3 is 6']
  39
  40 # run the test function for each input/output pair
  41 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2), (inp_3, out_3)])
  ```

</details>

<br>
<details>
  <summary><b>One test, no input</b></summary>

> This test will execute your student's program once. You supply the expected output. It captures the program output in it's entirety. You'll need to remove the second input/output pair in the file by following the directions below:
    
<br>

- Leave the value of ```inp_1``` on [line 31](./tests/test_exercise.py) as an empty list
    
- Assign the value to the expected program output to ```out_1``` on line 32
  - It should be a list of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (\n).

- Delete lines 34-36: ```inp_2``` and ```inp_3```
  
- At (now) line 35, delete ```, (inp_2, out_2)``` from the decorator.
  
- Finished Example:
  ```Python
  31 inp_1 = []
  32 out_1 = ['hello']
  33   
  34 # run the test function for each input/output pair
  35 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1)])
  ```

</details>

<br>
<br>
<details>
  <summary><b>Test for a single string in the output</b></summary>

> If your student's program doesn't accept any user input, you should choose this option.
    
<br>

import pytest
import src.exercise

inp_1 = [5,6]
out_1 = "The sum of both numbers is 11"

inp_2 = [1,1]
out_2 = "The sum of both numbers is 2"

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
    # Each line of output will be a list element, excluding all newline characters.
    out = out.strip().split('\n')
    out = [i for i in out if i]
    
    # Test the actual program output against the anticipated program output:
    assert expected in out

</details>

<br>
<br>
<details>
  <summary>Testing a student-defined function</summary>

> If your student's program doesn't accept any user input, you should choose this option.
    
<br>

blah

</details>
