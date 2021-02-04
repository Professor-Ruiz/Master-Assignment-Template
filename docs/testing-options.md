# Testing Options

<br>
<details>
  <summary><b>DEFAULT:</b> Two input/output tests</summary>

> This test will execute your student's program twice. You supply the input and expected output for each execution. It captures the program output in it's entirety.
    
<br>

Update [lines 31-35](/tests/test_exercise.py#L31) of test_exercise.py

- The inputs should be a list of strings.
    - Even if it's only one input.
    - Even if it is a numeric value.
    - Exclude any input() function prompts.
    - Exclude newline characters (\n).
    
- The outputs should be a list of strings.
    - Each string in the list should correspond to a complete line of output on the console.
    - Exclude any ```input()``` function prompts (only include ```print()``` function output)
    - Exclude newline characters and blank lines (\n).
    
- Example:
  ```Python
  inp_1 = ['1']
  out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']

  inp_2 = ['2']
  out_2 = ['2 plus 1 is 3', '2 plus 2 is 4', '2 plus 3 is 5']
  ```
</details>

<br>
<details>
  <summary>One test, no input</summary>

> If your student's program doesn't accept any user input, you should choose this option.
    
<br>

</details>



