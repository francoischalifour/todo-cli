# Todo CLI

> Command-line tool to manage the To-Do lists of your projects

![Todo workflow](https://cloud.githubusercontent.com/assets/6137112/15577881/94d72140-235e-11e6-9f6d-68393c515a33.gif)

*Built with Python3.*

## Elevator Pitch

*Todo* exists to bring all the needed functionalities for simple project management to the terminal. No graphical interface is needed; this tool is easy enough to use to improve your workflow.

![Todo screenshot](https://cloud.githubusercontent.com/assets/6137112/15577612/8a2cac98-235d-11e6-9e62-520a1210f14d.png)

## Usage

### Clone the repo

```console
$ git clone https://github.com/francoischalifour/todo-cli
```

### Create a virtual environment (optional)

If you use several Python versions on your computer, create a virtual environment with the Python 3 interpreter:

```console
$ virtualenv -p python3 venv
```

Activate the new environment:

```console
$ source venv/bin/activate
```

### Install with [*pip*](https://github.com/pypa/pip)

```console
$ pip install <path to the todo-cli folder>
```

### Init a Todo project

```console
$ todo init
Project name: (moody-app) Moody
The project Moody has been created.
```

## Commands

### Create a new project

```console
$ todo init
```

### Delete an existing project

```console
$ todo delete
```

### Rename a project

```console
$ todo rename "New name"
```

### Add a task

```console
$ todo add "Name of the task"
```

You can add several tasks and don't need to add quotes:

```console
$ todo add "Task 1", Task 2, "Task 3"
```

### Remove a task

To remove a specific task by name:

```console
$ todo remove "Name of the task"
```

To remove a task with an interactive menu (Unix only):

```console
$ todo remove
```

### Check a task

```console
$ todo check "Name of the task"
```

### Uncheck a task

```console
$ todo uncheck "Name of the task"
```

### Toggle a task

To toggle a specific task by name:

```console
$ todo toggle "Name of the task"
```

To toggle a task with an interactive menu (Unix only):

```console
$ todo toggle
```

### List all tasks

```console
$ todo list
```

### Search tasks

```console
$ todo search "keyword"
```

## License

MIT © [François Chalifour](http://francoischalifour.com)
