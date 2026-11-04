
priorites_menu_option ={
    1: "high",
    2: "medium",
    3: "low"
}

tasks_high_priority = []
tasks_medium_priority = []
tasks_low_priority = []

tasks_by_priorities = {
    "high": tasks_high_priority,
    "medium": tasks_medium_priority,
    "low": tasks_low_priority
}

for task_position in range(1, 7):    
    while True:
        try:
            new_task = input(f"Please, register the {task_position}º "
                                "task: ").lower().strip()
            if not new_task:
                raise ValueError ("Please, the field can't be empty\n")
            break       

        except ValueError as e:
            print(f"\nERROR >>> {e}\n")  

    while True:
        try:
            priority_option = int(input(f"What priority "
                "should be assigned to this task?\n"
                f"1. {priorites_menu_option[1]}\n"
                f"2. {priorites_menu_option[2]}\n"
                f"3. {priorites_menu_option[3]}\n"
                "type the priority: "))
            print()

            priority = priorites_menu_option[priority_option]
            
            tasks_by_priorities[priority].append(new_task)
            break

        except ValueError:
            print("\nERROR >>> Please, enter only numbers")  

        except KeyError:
            print("\nERROR >>> Invalid priority. Choose 1, 2 or 3.\n")

print("\nRegistered tasks:")

for priority, tasks in tasks_by_priorities.items():
    print(f"\nPriority: {priority}")
    for task in tasks:
        print(f"- {task}")