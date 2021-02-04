# Testing Options

> I've included a few basic set-ups to test your student submissions. I've tried to make them very simple to select and implement. 

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
  ```python
  inp_1 = ['1']
  out_1 = ['1 plus 1 is 2', '1 plus 2 is 3', '1 plus 3 is 4']

  inp_2 = ['2']
  out_2 = ['2 plus 1 is 3', '2 plus 2 is 4', '2 plus 3 is 5']
  ```
    

    
4. <details><summary>Make your copy of <b>master-assignment-template</b> a template</summary>
    <ul><li>Open your copy of <b>master-assignment-template</b></li>
    <li>Click the <b>Settings</b> menu in the upper right corner</li>
    <li>Click the <b>Template repository</b> option</li>
    <li>A green check mark to the right indicates success</li></ul></details>
     
5. <details><summary>Now you have your own copy of <b>master-assignment-template</b>!</summary>
    <ul><li>You'll use this as a template each time you make a new assignment repository</li>
    <li>Don't make changes to your copy of <b>master-assignment-template</b></li></ul></details>
</details>






    - This pytest runs two input/output tests.
    - The inputs should be a list of strings:
        - even if only 1 value
        - even if numbers
        - Exclude any input() function prompts.
        - Exclude newline characters (\n)
    - The outputs should be a list of strings:
        - Each string should correspond to a line of output on the console
        - Exclude any input() function prompts
        - Exclude any blank lines (newline characters, \n)
    - Example:
        ```
        31 inp_1 = ['8', '3']
        32 out_1 = ['eight', 'three']
        33
        34 inp_2 = ['4', '1']
        35 out_2 = ['four', 'one']
        ```
    - Make sure the [rubric](/README.md#grading) in the README.md file lists these two tests as the test cases.
