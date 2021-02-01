# Using this template
    > This is a master template for creating autograded assignments. To use this template for your GitHub assignments, follow these steps in order:

1. [Clone this master-assignment-template](#clone-this-master-assignment-template)
2. [Create an assignment repository](#create-custom-assignment-repositories)
3. [Update and edit your assignment repository](#update-your-assignment-repositories)
3. [Create an assignment in GitHub Classroom](#create-assignments-in-github-classroom)

## Clone this maste-assignment-template
    > You only need to complete this step one time. This will give you your own copy of the master template. You will use it as a template when creating your own assignment repositories.

1. Click the ***Code*** button in the upper right corner of this repository's [code directory](https://github.com/Professor-Ruiz/master-assignment-template)

2. Copy the Clone URL that appears in the pop-up text box
    - Example: https://github.com/Professor-Ruiz/master-assignment-template.git
    
3. Create a clone repository
    - Navigate to https://github.com/new/import
    - Paste the clone URL in the text box
    - Make sure your organization is the repository owner (not your GitHub username)
    - Name your repository ***master-assignment-template**, then click ***Begin Import***
    
4. Make ***master-assignment-template*** a template
    - Open your ***master-assignment-template*** repository
    - Click the ***Settings*** menu in the upper right corner
    - Click the ***Template repository*** option
    - A green check mark to the right indicates success
     
4. Now you have your own copy of ***master-assignment-template***!
    - You'll use this as a template each time you make a new assignment repository
    - Don't make changes to your copy of ***master-assignment-template***

## Create custom assignment repositories
    > For each assignment you'd like to create in GitHub classroom, create a new repository using your master-assignment-template as it's template.

1. Navigate to https://github.com/new

2. In the pull-down menu with the text ***No Template***, find your ***master-assignment-template*** repository

3. Make sure your organization is the repository owner (not your personal GitHub username) 

4. Name your assignment repository, then click ***Create repository***

## Update and edit your assignment repository

1. Update [README.md](README.md) file. It's the directions the students will see when they accept the assignment.

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
        
## Create assignments in GitHub Classroom

1. Select the assignment repository you made specifically for the new assignment.
    - Example: ```Professor-Ruiz/CS1030-Lesson-10```

2. If your students will use Repl.it for this assignment, enter this Repl.it configuration when creating the assignment:
    ```
    Run command:    python3 src/exercise.py
    Language:       Python 3
    ```
    
3. Do not add tests

Delete this TEACHER_README.md file
