from database import create_database, add_task


if __name__ == "__main__":

    title = input("Enter task title: ")
    category = input("Enter task category: ")
    due_date = input("When is the assignment due?  ")
    status = "Not Started"

    add_task(title, category, due_date, status)

    print("Task has been added!")