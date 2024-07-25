# Weighted Average Calculator

This project contains a Python script to calculate the weighted average of grades based on user input. The script repeatedly prompts the user to enter grades and their corresponding coefficients until the user decides to finish. It then calculates and prints the weighted average of the entered grades.

## How It Works

1. The script prompts the user to enter a grade and its corresponding coefficient.
2. The user can continue entering grades and coefficients.
3. If the user types 'done' for the grade input, the script stops asking for more inputs.
4. The script calculates the weighted average of the entered grades.
5. The weighted average is printed to the console.

## Functions

### `get_grade_and_coefficient()`

This function prompts the user to enter a grade and its coefficient. If the user inputs 'done', the function returns `None` for both values, signaling the end of input. If the user inputs invalid values, the function also returns `None` for both values.

```python
def get_grade_and_coefficient():
    try:
        grade = float(input("Enter a grade (or type 'done' to finish): "))
        coefficient = float(input("Enter the coefficient for this grade: "))
        return grade, coefficient
    except ValueError:
        return None, None
