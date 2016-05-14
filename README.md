# Todo CLI

> *Todo* is command line tool that manages the task lists of your projects.

![Todo screenshot](https://cloud.githubusercontent.com/assets/6137112/15250305/732b4056-1924-11e6-8609-d1918e902b4b.png)

## Elevator Pitch

*Todo* exists to bring all the needed functionalities to manage a simple project via a terminal. No graphical interface is needed; this tool is easy enough to work with to improve your workflow.

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

### Remove a task

To remove a specific task by name:

```sh
todo remove "Name of the task"
```

To remove a task in a list:

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

To toggle a task in a list:

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

```
pip install todo-cli
```

## Dev

To create a virtual environment:

```sh
virtualenv -p python3 venv
```

Activate the new environment:

```sh
source venv/bin/activate
```

## License

MIT © [François Chalifour](http://francoischalifour.com)
