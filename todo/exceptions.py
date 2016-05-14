class TodoError(Exception):
    """Base todo exception"""


class CommandError(TodoError):
    """Raised when there is an error in command-line arguments"""
