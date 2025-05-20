# Python Todo App

A simple desktop to-do list application built with Python and Tkinter.

## Features

- Add new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Data persistence using JSON
- Clean, modern interface

## Screenshots

![Todo App Screenshot](screenshot.png)

## Requirements

- Python 3.x (no additional packages needed)

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/AdamFan9311/python-todo-app.git
   ```

2. Navigate to the project directory:
   ```
   cd python-todo-app
   ```

3. Run the application:
   ```
   python todo_app.py
   ```

## Usage

- Enter a task in the input field and press Enter or click "Add Task"
- Select a task and click "Mark Complete" to toggle its completion status
- Select a task and click "Delete Task" to remove it
- Tasks are automatically saved between sessions

## How It Works

The app uses Tkinter for the GUI and stores tasks in a JSON file (todo_data.json) in the same directory as the script. This allows the tasks to persist between application restarts.

## License

This project is open source and available under the MIT License.
