# Testing Options

<br>
<details>
  <summary>Two input/output tests (default)</summary>

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
    
- Example:
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
  <summary>One input/output test</summary>

> This test will execute your student's program once. You supply the input and expected output. It captures the program output in it's entirety. You'll need to remove the second input/output pair in the file by following the directions below:

<br>

- Assign the value of the program input to the variable ```inp_1``` on line 31
  - It should be a list of string(s) 
  - Exclude any input() function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the value to the expected program output to the variable ```out_1``` on line 32
  - It should be a list of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (\n).

- Example:
  ```Python
  31 inp_1 = ['1']
  32 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  ```

- Delete [lines 34-36](/tests/test_exercise.py#L34) of test_exercise.py:
  ```Python
  34 inp_2 = []
  35 out_2 = []
  36
  ```
  
- At (now) line 35, delete ```, (inp_2, out_2)``` from the decorator. It should now look like this:
  ```Python
  34 # run the test function for each input/output pair
  35 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1)])
  ```
  
<br>

</details>

<br>
<details>
  <summary>One test, no input</summary>

> If your student's program doesn't accept any user input, you should choose this option.
    
<br>

</details>



