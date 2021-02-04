# Using this template
    
> This is a master template for creating autograded Python assignments. To use this template for your GitHub assignments, follow these steps in order:

1. [Clone this master-assignment-template](#clone-this-master-assignment-template)
2. [Create an assignment repository](#create-an-assignment-repository)
    
    2.1. [Update and edit your assignment repository](#update-and-edit-your-assignment-repository)
3. [Create an assignment in GitHub Classroom](#create-an-assignment-in-github-classroom)

## Clone this master-assignment-template

> You only need to complete this step one time. This will give you your own copy of the master template. You will use it as a template each time you create your own assignment repositories.

1. Click the ***Code*** button in the upper right corner of this repository's [code directory](https://github.com/Professor-Ruiz/master-assignment-template) (to the left of the green "Use this template" button).

2. Copy the Clone URL that appears in the pop-up text box
    - Example: https://github.com/Professor-Ruiz/master-assignment-template.git
    
3. Create a clone repository
    - Navigate to https://github.com/new/import
    - Paste the clone URL in the text box
    - Make sure your organization is the repository owner (not your GitHub username)
    - Name your repository ***master-assignment-template***, then click ***Begin Import***
    
4. Make ***master-assignment-template*** a template
    - Open your ***master-assignment-template*** repository
    - Click the ***Settings*** menu in the upper right corner
    - Click the ***Template repository*** option
    - A green check mark to the right indicates success
     
4. Now you have your own copy of ***master-assignment-template***!
    - You'll use this as a template each time you make a new assignment repository
    - Don't make changes to your copy of ***master-assignment-template***

## Create an assignment repository
> For each assignment you'd like to create in GitHub classroom, create a new repository using your copy of master-assignment-template as it's template.

1. Navigate to https://github.com/new

2. In the pull-down menu with the text ***No Template***, find your ***master-assignment-template*** repository

3. Make sure your organization is the repository owner (not your personal GitHub username) 

4. Name your assignment repository, then click ***Create repository***

### Update and edit your assignment repository
> Once you've created an assignment repo using your copy of master-assignment-template as it's template, you'll want to update and edit some things. In this section, we'll check everything in the new assignment repo to make sure it reflects the assignment you want to create.

1. Make your repository a Template repository
    - Click the ***Settings*** menu in the upper right corner
    - Click the ***Template repository*** option
    - A green check mark to the right indicates success

1. Update the [README.md](/README.md) file. It is the directions the students will see when they accept the assignment.
    
2. Check [exercise.py](/src/exercise.py) to see if the student's boiler-plate code needs to be updated for this new assignment.
    - Do you need to add a user-defined function stub?
    
3. Will students need to import any modules into this program?
    - Example:
        ```
        import sys
        import NumPy
        import Tkinter
        ```
    - If yes, add these modules to [line 22](/.github/workflows/workflow.yml#L22) of the workflow.yml file
        ```
        pip install pytest flake8 sys NumPy Tkinter
        ```
    
4. Update [lines 31-35](/tests/test_exercise.py#L31) of test_exercise.py to reflect the new assignment's test cases:

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
        35 inp_2 = ['four', 'one']
        ```
    - Make sure the [rubric](/README.md#grading) in the README.md file lists these two tests as the test cases.
    
5. Delete the ***Docs*** folder from your assignment template. It includes this readme file intended for teachers only, and the pretty page theme you see :)
        
## Create an assignment in GitHub Classroom
> Once you've created an assignment repository template, you'll want to create an assignment.

1. Navigate to https://classroom.github.com/classrooms

2. Open the relevant Classroom.

3. Click the green ***New assignment** button.

4. Give the assignment a name, choose it's visibility, then click ***Continue***

5. In the ***Select a repository*** pull-down menu, select the assignment repository you just created:
    - Type in your organization name, followed by a forward slash /
    - Scroll until you find the repository

6. If you want your students to use Repl.it for this assignment, enter this Repl.it configuration:
    ```
    Run command:    python3 src/exercise.py
    Language:       Python 3
    ```
7. Repl.it's Free accounts do not allow students to import assignments (repositories) set to "Private" visibility. However, When assignments are set to "public" visibility, students will have access to each other's solutions. This may cause issues with plagiarism.
    - I made a quick three-point assignment for my students to claim their free "Hacker" level Repl.it accounts. I made [this video](https://youtu.be/ZqzVN47oVr0) to walk them through the process.
         
8. Click ***Continue***

9. DO NOT Add any tests on this page! Click ***Create assignment***
