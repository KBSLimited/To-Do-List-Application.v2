class TodoListCLI:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        """Display the menu of the To-Do List App."""
        print("""
        Welcome to the To-Do List App!
        Menu:
        1. Add a task
        2. View tasks
        3. View organized tasks
        4. Mark a task as complete
        5. Mark a task as incomplete
        6. Delete a task
        7. Save and Quit
        """)

    def add_task(self):
        """Add a new task to the list."""
        try:
            title = input("Enter the task title: ")
            priority = input("Enter the priority (High/Medium/Low): ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            self.tasks.append({"title": title, "status": "Incomplete", "priority": priority, "due_date": due_date})
            print("Task added successfully.")
        except Exception as e:
            print(f"An error occurred while adding the task: {e}")

    def view_tasks(self):
        """View all tasks with their details."""
        try:
            if not self.tasks:
                print("No tasks.")
            else:
                print("Tasks:")
                for index, task in enumerate(self.tasks, start=1):
                    status_color = "\033[92m" if task['status'] == "Complete" else "\033[91m"
                    print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status_color}{task['status']}\033[0m")
            input("Press Enter to return to the main menu.")
        except Exception as e:
            print(f"An error occurred while viewing tasks: {e}")

    def _print_task_list(self, tasks, status_color):
        """Print tasks based on their status."""
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status_color}{task['status']}\033[0m")

    def view_organized_tasks(self):
        """View tasks organized by status."""
        try:
            if not self.tasks:
                print("No tasks.")
                return
            incomplete_tasks = [task for task in self.tasks if task["status"] == "Incomplete"]
            complete_tasks = [task for task in self.tasks if task["status"] == "Complete"]
            print("Organized Tasks:")
            if incomplete_tasks:
                print("Incomplete Tasks:")
                self._print_task_list(incomplete_tasks, "\033[91m")
            else:
                print("No incomplete tasks.")
            if complete_tasks:
                print("Complete Tasks:")
                self._print_task_list(complete_tasks, "\033[92m")
            else:
                print("No complete tasks.")
            input("Press Enter to return to the main menu.")
        except Exception as e:
            print(f"An error occurred while viewing organized tasks: {e}")

    def mark_complete(self):
        """Mark a task as complete."""
        try:
            self.view_tasks()
            if not self.tasks:
                print("No tasks to mark as complete.")
                return
            index = int(input("Enter the index of the task to mark as complete: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["status"] = "Complete"
                print("Task marked as complete.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred while marking task as complete: {e}")
        finally:
            input("Press Enter to return to the main menu.")

    def mark_incomplete(self):
        """Mark a task as incomplete."""
        try:
            self.view_tasks()
            if not self.tasks:
                print("No tasks to mark as incomplete.")
                return
            index = int(input("Enter the index of the task to mark as incomplete: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["status"] = "Incomplete"
                print("Task marked as incomplete.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred while marking task as incomplete: {e}")
        finally:
            input("Press Enter to return to the main menu.")

    def delete_task(self):
        """Delete a task from the list."""
        try:
            self.view_tasks()
            if not self.tasks:
                print("No tasks to delete.")
                return
            index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                print("Task deleted successfully.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred while deleting task: {e}")
        finally:
            input("Press Enter to return to the main menu.")

    def save_tasks_to_file(self, filename):
        """Save tasks to a file."""
        try:
            with open(filename, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task['title']},{task['status']},{task['priority']},{task['due_date']}\n")
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving tasks to file: {e}")

    def get_user_choice(self):
        """Get user's choice from the menu."""
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print("Invalid choice. Please enter a number from 1 to 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self):
        """Main function to run the To-Do List application."""
        try:
            while True:
                self.display_menu()
                choice = self.get_user_choice()
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    self.view_organized_tasks()
                elif choice == 4:
                    self.mark_complete()
                elif choice == 5:
                    self.mark_incomplete()
                elif choice == 6:
                    self.delete_task()
                elif choice == 7:
                    self.save_tasks_to_file("tasks.txt")  # Save tasks to file before quitting
                    print("Tasks saved. Goodbye!")
                    break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    todo_cli = TodoListCLI()
    todo_cli.run()