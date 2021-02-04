# Testing Options

> Choose one of five autograding option below. I've already pre-written the the testing scripts and integrated them into the assignment so they're automatically run with each student submission. I've also kept the required edits to a minimum and provided easy and explicit directions for you.
> 
> Hot Tip:
> Put your solution code in [exercise.py](../src/exercise.py) before you begin updating the tests. That way, when you commit your changes to [exercise_test.py](../tests/test_exercise.py), you'll immediately see if it passes the test. Just make sure to delete the solution before you make an assignment!


<br>
<details>
  <summary><b>Two input/output tests (default)</b></summary>

> This test will execute your student's program twice. You supply the input and expected output for each execution. It captures the program output in it's entirety.
    
<br>

Update [lines 9-13](../tests/test_exercise.py#L9) of test_exercise.py

- The inputs should be a list of strings.
    - Exclude any ```input()``` function prompts.
    - Exclude newline characters (```\n```).
    
- The outputs should be a list of strings.
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (```\n```).
    
- Finished Example:
  ```Python
   9 inp_1 = ['1']
  10 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  11 
  12 inp_2 = ['2']
  13 out_2 = ['2 plus 1 is 3', '2 plus 2 is 4', '2 plus 3 is 5']
  ```
</details>

<br>
<details>
  <summary><b>One input/output test</b></summary>

> This test will execute your student's program once. You supply the input and expected output. It captures the program output in it's entirety. You'll need to remove the second input/output pair in the file by following the directions below:

<br>

- Assign the value of the program input to the variable ```inp_1``` on [line 9](../tests/test_exercise.py#L9) of test_exercise.py
  - It should be a list of string(s) 
  - Exclude any ```input()``` function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the value to the expected program output to the variable ```out_1``` on line 10
  - It should be a list of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (\n).

- Delete lines 12-14: ```inp_2``` and ```out_2```
  
- At (now) line 13, delete ```, (inp_2, out_2)``` from the decorator.
  
- Finished Example:
  ```Python
  09 inp_1 = ['1']
  10 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  11   
  12 # run the test function for each input/output pair
  13 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1)])
  ```

</details>

<br>
<details>
  <summary><b>Three input/output tests</b></summary>

> This test will execute your student's program three times. You supply the input and expected output for each execution. It captures the program output in it's entirety. You'll need to add a third input/output pair in the file by following the directions below:
    
<br>

- Move the code on [line 15](../tests/test_exercise.py#L15) down three lines to line 18

- Insert ```inp_3 = []``` on line 15, and ```out_3 = []``` on line 16

- Assign the value of the program inputs to ```inp_1```, ```inp_2```, and ```inp_3```:
  - They should be a lists of string(s) 
  - Exclude any ```input()``` function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the value to the expected program output to ```out_1```, ```out_2```, ```out_3```:
  - They should be a lists of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (\n).
  
- At (now) line 19, add ```, (inp_3, out_3)``` to the decorator.
  
- Finished Example:
  ```Python
  09 inp_1 = ['1']
  10 out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']
  11 
  12 inp_2 = ['2']
  13 out_2 = ['2 plus 1 is 3', '2 plus 2 is 4', '2 plus 3 is 5']
  14
  15 inp_3 = ['3']
  16 out_3 = ['3 plus 1 is 4', '3 plus 2 is 5', '3 plus 3 is 6']
  17
  18 # run the test function for each input/output pair
  19 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2), (inp_3, out_3)])
  ```

</details>

<br>
<details>
  <summary><b>One test, no input</b></summary>

> This test will execute your student's program once. You supply the expected output. It captures the program output in it's entirety. You'll need to remove the second input/output pair in the file by following the directions below:
    
<br>

- Leave the value of ```inp_1``` on [line 9](../tests/test_exercise.py#L9) as an empty list
    
- Assign the value to the expected program output to ```out_1``` on line 10
  - It should be a list of string(s) 
  - Each string in the list should correspond to a complete line of output on the console.
  - Exclude any ```input()``` function prompts (only include ```print()``` function output)
  - Exclude newline characters and blank lines (```\n```).

- Delete lines 12-14: ```inp_2``` and ```out_2```
  
- At (now) line 13, delete ```, (inp_2, out_2)``` from the decorator.
  
- Finished Example:
  ```Python
   9 inp_1 = []
  10 out_1 = ['hello']
  11   
  12 # run the test function for each input/output pair
  13 @pytest.mark.parametrize("test_input, expected", [(inp_1, out_1)])
  ```

</details>

<br>
<details>
  <summary><b>Test for a single string in the program output</b></summary>

> This test will execute your student's program twice. You supply the input and the test string. The test captures the program output in it's entirety. Then it tests if the given string is in the program output.
    
<br>

Update [lines 9-13](../tests/test_exercise.py#L9) of test_exercise.py

- Assign the program inputs to ```inp_1``` and ```inp_2```:
  - They should be lists of string(s) 
  - Exclude any ```input()``` function prompts.
  - Exclude newline characters (```\n```).
    
- Assign the test strings to ```out_1``` and ```out_2```
    - They should each be a single string enclosed in quotes.
    
- Delete lines 28-32. This code reformats the captured program output, it will break our test.

- change the assert statement to ```assert expected in out```
    
- Finished Example:
  ```Python
  09 inp_1 = ['1', '1']
  10 out_1 = '2'
  11
  12 inp_1 = ['2', '3']
  13 out_1 = '5'
  ..
  ..
  26 out, err = capsys.readouterr()
  27
  28 # Test if the expected output was in the actual output:
  29 assert expected in out
  ```
  <br>
</details>
