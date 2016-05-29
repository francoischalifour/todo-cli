# Todo (CLI)

> Command-line tool to manage the Todo lists of your projects

![Todo workflow](https://cloud.githubusercontent.com/assets/6137112/15577881/94d72140-235e-11e6-9f6d-68393c515a33.gif)

*Built with Python3 with Unix systems in mind.*

## Elevator Pitch

*Todo* exists to bring all the needed functionalities for simple project management to the terminal. No graphical interface is needed; this tool is easy enough to use to improve your workflow.

![Todo screenshot](https://cloud.githubusercontent.com/assets/6137112/15632931/d48ba286-25a0-11e6-983b-46ef5188e91e.png)

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

### Install with [pip](https://github.com/pypa/pip)

```console
$ pip install <path to the todo-cli folder>
```

You should now be able to use the command `todo`.

### Create a Todo project

Before working on your Todo list, you need to create a project.

```console
$ todo init
Project name: (moody-app) Moody
The project Moody has been created.
```

You can now start adding tasks!

## Commands

* [Create a project](#create-a-project)
* [Delete a project](#delete-a-project)
* [Rename a project](#rename-a-project)
* [Add a task](#add-a-task)
* [Remove a task](#remove-a-task)
* [Check a task](#check-a-task)
* [Uncheck a task](#uncheck-a-task)
* [Toggle a task](#toggle-a-task)
* [List all tasks](#list-all-tasks)
* [Search tasks](#search-tasks)

### Create a project

```console
$ todo init
```

### Delete a project

```console
$ todo delete
```

*You can use `del` instead of `delete`.*

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

*You can use `rm` instead of `remove`.*

### Check a task

```console
$ todo check "Name of the task"
```

To check all the items:

```console
$ todo check --all
```

*You can use `-a` instead of `--all`.*

### Uncheck a task

```console
$ todo uncheck "Name of the task"
```

To uncheck all the items:

```console
$ todo uncheck --all
```

*You can use `-a` instead of `--all`.*

### Toggle a task

To toggle a specific task by name:

```console
$ todo toggle "Name of the task"
```

To toggle a task with an interactive menu (Unix only):

```console
$ todo toggle
```

*You can use `tg` instead of `toggle`.*

### List all tasks

```console
$ todo list
```

*You can use `ls` instead of `list`.*

### Search tasks

```console
$ todo search "keyword"
```

## License

MIT © [François Chalifour](http://francoischalifour.com)
