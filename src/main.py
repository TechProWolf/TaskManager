def main():
    task_manager = TaskManager()
    task_manager.load_tasks()  # Load tasks from a file or database (if applicable)

    # Example usage
    task_manager.create_task("Finish report", "2023-06-15", priority=2)
    task_manager.create_task("Attend meeting", "2023-06-10", priority=1)

    task_manager.display_tasks()  # Display all tasks

    # Update a task
    task_manager.update_task(0, title="Finish report", due_date="2023-06-17")

    # Mark a task as complete
    task_manager.complete_task(0)

    task_manager.display_tasks()  # Display updated task list

    task_manager.save_tasks()  # Save tasks to a file or database (if applicable)


if __name__ == "__main__":
    main()
