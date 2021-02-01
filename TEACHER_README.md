# TODO

- [x] Clone this Master_Assignment_Template into your own repository.
- [x] Create a new assignment repository (from your copy of Master_Assignment_Template) for each new assignment you'd like to create for your students.
- [x] Create the assignments in GitHub Classroom using the new assignment repository you created.

## Clone this Master_Assignment_Template
- make it a template repository
- name it ***\<your username or organization>/Master-Assignment-Template***
- Don't alter this repository, you'll use it to create actual assignment repositories for your students

## Create Assignment Templates for each of your assignments

Clone your ***Master-Assignment-Template***, and begin editing it for the students 

1. Update [README.md](README.md) file for new assignment directions for the student.

2. Check [exercise.py](/src/exercise.py) to see if the student template needs to be updated for this new assignment.
    - Do you need to add a user-defined function stub?
    
3. Will students need to import any modules into this program?
    - Example:
        ```
        import sys
        import NumPy
        import Tkinter
        ```
    - Add these modules to [line 22](https://github.com/RuizTheRuler/Assignment-Template-2/blob/3d95062b925091355e3e1db65d6fe817bbcf28b3/.github/workflows/workflow.yml#L22) of the workflow.yml file
        ```
        pip install pytest flake8 sys NumPy Tkinter
        ```
    
3. Update [lines 15-19](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L15) of test_exercise.py to reflect the new assignment's test cases:

    - This pytest runs two input/output tests.
    - The inputs on lines [15](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L15) & [18](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L18) should be a list, even if it's just one element.
        - Example 1: ["Snickerdoodle Cupcake","Biscoff Lava","Pumpkin Chocolate Chip"]
        - Example 2: [5]
    - The outputs on line [16](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L16) & [19](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L19) should be in string form, and include \\n characters when needed.
        - Example 1: "\nBiscoff Lava\nPumpkin Chocolate Chip\nSnickerdoodle Cupcake\n"
        - Example 2: "6"
    - DO NOT include user prompts from any `input()` functions in the output string.
    - Make sure the rubric at the bottom of the [README.md](README.md) file lists these two tests as the test cases.
        
## When creating a new assignment in your GitHub Classroom:

1. Select the assignment repository you made specifically for the new assignment.
    - Example: ```Professor-Ruiz/CS1030-Lesson-10```

2. If your students will use Repl.it for this assignment, enter this Repl.it configuration when creating the assignment:
    ```
    Run command:    python3 src/exercise.py
    Language:       Python 3
    ```
    
3. Do not add tests

Delete this TEACHER_README.md file
