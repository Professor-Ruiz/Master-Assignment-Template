# Checklist

1. Update [README.md](README.md) file for new assignment directions for the student

2. Check [exercise.py](/src/exercise.py) to see if the student template needs to be updated for this new assignment
    - Do you need to add a user-defined function stub?
    
3. Update lines 15-19 of [test_exercise.py](tests/test_exercise.py) to reflect the new assignment's test cases

    - This pytest runs two input/output tests
    - The inputs on lines 15 & 18 should be a list, even if it's just one element
        - Ex: ["Snickerdoodle Cupcake","Biscoff Lava","Pumpkin Chocolate Chip"]
    - The outputs on line 16 & 19 should be in string form, and include \\n characters when needed.
        - Ex: "\nBiscoff Lava\nPumpkin Chocolate Chip\nSnickerdoodle Cupcake\n"
        
4. Delete this TEACHER_README.md file
