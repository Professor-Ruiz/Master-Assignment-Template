# Checklist

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
        - Ex: ["Snickerdoodle Cupcake","Biscoff Lava","Pumpkin Chocolate Chip"]
    - The outputs on line [16](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L16) & [19](https://github.com/RuizTheRuler/Assignment-Template-2/blob/d73b8c2c9ad5e3d4435f6096b9fc1a76c3080002/tests/test_exercise.py#L19) should be in string form, and include \\n characters when needed.
        - Ex: "\nBiscoff Lava\nPumpkin Chocolate Chip\nSnickerdoodle Cupcake\n"
    - Make sure the rubric at the bottom of the [README.md](README.md) file lists these two tests as the test cases.
        
4. Delete this TEACHER_README.md file
