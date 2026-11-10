"""
Exercise 00

Goal:
Create s permance bonus calculator, allowing employees
to enter their salary and performance score. 
Based on the perfomance score, a pre-defined percentage
will be applied as a bonus, calculated on the basis 
of the employee's salary; the result shows the 
bonus amount and the total salary including bonus. 

Concepts Practiced:
- Input handling
- Input validation
- 
- 
- 
-  
-  

Tests:
✓ 
✓  
✓ 
✓ 
✓ 
✓ 

"""
while True:
    while True:
        try:
            worker_salary = input("Please enter your based salary: ").strip()

            if not worker_salary:
                raise ValueError("Please, this field must be completed.")
            elif "," in worker_salary and "." in worker_salary:
                clean_worker_salary = worker_salary.replace(".", "")
                clean_worker_salary = clean_worker_salary.replace(",", ".")
                salary = float(clean_worker_salary)
            elif worker_salary.replace(".", "", 1):
                salary = worker_salary.replace(".", "")
                salary = float(salary)
            else:
                raise ValueError("Please, enter a valid salary.")
            break

        except ValueError as error:
            print(error)

    while True:
        try:
            performance_score = input("Please, enter your performance score (score ranges from 0 to 10): ").strip()

            if "," in performance_score and "." in performance_score:
                raise ValueError("Please, enter a valid number.")
            elif not performance_score:
                raise ValueError("Please, enter a valid score.")
            elif "," in performance_score:
                clean_performance_score = performance_score.replace(",", ".")
                score = float(clean_performance_score)
            elif performance_score.replace(".", "", 1).isdigit():
                score = float(performance_score)
            else:
                raise ValueError("Please, enter numbers only.")

            score = float(performance_score)

            if score < 0 or score > 10:
                raise ValueError ("Please, enter a valid score (score ranges from 0 to 10).")
            break

        except ValueError as error:
            print(error)

    if score > 9:
        bonus = salary * 0.2
        salary_up_bonus = salary + bonus
    elif score <= 9 and score >= 7:
        bonus = salary * 0.1
        salary_up_bonus = salary + bonus
    elif score < 7: 
        bonus = salary * 0.05
        salary_up_bonus = salary + bonus

    print("\n>>> TOTAL SALARY <<<")

    print(f"Bonus amount: {bonus:.2f}€\n"
        f"Salary due: {salary_up_bonus:.2f}€\n")