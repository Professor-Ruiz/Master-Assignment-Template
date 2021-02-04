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

- Delete lines 34-36: ```inp_2``` and ```out_2```
  
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

- Leave the value of ```inp_1``` on [line 31](./tests/test_exercise.py) as an empty string
    
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
  <summary><b>Test for a single string in the program output</b></summary>

> This test will execute your student's program twice. You supply the input and the test string. The test captures the program output in it's entirety. Then it tests if the given string is in the program output.
    
<br>

- Assign the program inputs to ```inp_1``` and ```inp_2```:
  - They should be lists of string(s) 
  - Exclude any input() function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the test strings to ```out_1``` and ```out_2```
    - They should each be a single string enclosed in quotes.
    
- Delete lines 50 - 54. This code reformats the captured program output, we don't need it.

- change the assert statement to ```assert expected in out```
    
- Finished Example:
  ```Python
  31 inp_1 = ['1', '1']
  32 out_1 = '2'
  33
  34 inp_1 = ['2', '3']
  35 out_1 = '5'
  ..
  ..
  48 out, err = capsys.readouterr()
  49
  50 # Test if the expected output was in the actual output:
  51 assert expected in out
  ```
  <br>
</details>

<br>
<br>
<details>
  <summary>Testing a student-defined function</summary>

> If your student's program doesn't accept any user input, you should choose this option.
    
<br>

blah

</details>
