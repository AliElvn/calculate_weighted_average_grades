def get_grade_and_coefficient():
    try:
        grade = float(input("Enter a grade (or type 'done' to finish): "))
        coefficient = float(input("Enter the coefficient for this grade: "))
        return grade, coefficient
    except ValueError:
        return None, None

def calculate_weighted_average():
    total_grade = 0
    total_coefficient = 0
    
    while True:
        grade, coefficient = get_grade_and_coefficient()
        if grade is None or coefficient is None:
            break
        
        total_grade += grade * coefficient
        total_coefficient += coefficient
    
    if total_coefficient == 0:
        print("No valid grades or coefficients were entered.")
    else:
        weighted_average = total_grade / total_coefficient
        print(f"The weighted average is: {weighted_average:.2f}")

calculate_weighted_average()