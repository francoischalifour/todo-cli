# Todo CLI

> *Todo* is a command-line tool to manage the To-Do lists of your projects.

![Todo workflow](https://cloud.githubusercontent.com/assets/6137112/15512100/8da8cc10-21de-11e6-9d16-3d41654aaa7d.gif)

*Built with Python3.*

## Elevator Pitch

*Todo* exists to bring all the needed functionalities for simple project management to a terminal. No graphical interface is needed; this tool is easy enough to work with to improve your workflow.

![Todo screenshot](https://cloud.githubusercontent.com/assets/6137112/15250305/732b4056-1924-11e6-8609-d1918e902b4b.png)

## Commands

### Create a new project

```sh
todo init
```

### Delete an existing project

```sh
todo delete
```

### Rename a project

```sh
todo rename "New name"
```

### Add a task

```sh
todo add "Name of the task"
```

You can add several tasks and don't need to add quotes:

```sh
todo add "Task 1", Task 2, "Task 3"
```

### Remove a task

To remove a specific task by name:

```sh
todo remove "Name of the task"
```

To remove a task with an interactive menu:

```sh
todo remove
```

### Check a task

```sh
todo check "Name of the task"
```

### Uncheck a task

```sh
todo uncheck "Name of the task"
```

### Toggle a task

To toggle a specific task by name:

```sh
todo toggle "Name of the task"
```

To toggle a task with an interactive menu:

```sh
todo toggle
```

### List all tasks

```sh
todo list
```

### Search tasks

```sh
todo search "keyword"
```

## Install

### 1. Clone the repo

```sh
git clone https://github.com/francoischalifour/todo-cli
```

### 2. Install with [*pip*](https://github.com/pypa/pip)

Install the program:

```sh
pip install -e [path to the TODO folder]
```

### 3. Optional: *if you use several Python versions*

Create a virtual environment with the Python 3 interpreter:

```sh
virtualenv -p python3 venv
```

Activate the new environment:

```sh
source venv/bin/activate
```

Install the program in your project environment:

```sh
pip install -e [path to the TODO folder]
```

You're ready to go!

## License

MIT © [François Chalifour](http://francoischalifour.com)
