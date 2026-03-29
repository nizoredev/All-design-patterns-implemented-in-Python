from typing import (
    Any,
    Union,
    Self,
    Optional
)
from abc import ABC, abstractmethod
from collections import deque

class AbsCommand(ABC): 
    def __init__(self, app, editor, *args, **kwargs) -> None:
        self.app =  app
        self.editor = editor
        self.backup = None
    
    @abstractmethod
    def execute(self) -> Any: ...

    def undo(self) -> None:
        self.editor.text = self.backup

    def save_backup(self) -> None:
        self.backup = self.editor.text

class Editor:
    def __init__(self) -> None:
        self.text = ""

    def get_selection(self) -> Optional[str]:
        return self.text
    
    def replace_selection(self, text: str) -> None:
        self.text = text

class CommandHistory:
    def __init__(self) -> None:
        self.history = deque()

    def pop(self) -> AbsCommand:
        return self.history.pop()

    def push(self, command: AbsCommand) -> AbsCommand:
        self.history.append(command)
        return self.history[-1]
    
class CopyCommand(AbsCommand):
    def execute(self) -> None:
        self.app.clipboard = self.editor.get_selection()
        return False # Returns False so command is not saved to history stack

class UndoCommand(AbsCommand):
    def execute(self) -> None:
        self.app.undo()
        return False

class CutCommand(AbsCommand):
    def execute(self) -> None:
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True
    
class PasteCommand(AbsCommand): 
    def execute(self) -> None:
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True
    
class SetCommand(AbsCommand):
    def execute(self, text: str) -> None:
        self.save_backup()
        self.editor.replace_selection(text)
        return True

class App:
    def __init__(self) -> None:
        self.clipboard = ""
        self.editor = Editor()
        self.history = CommandHistory()

    def create(self) -> None:
        self.copy_cmd = lambda: self.execute(CopyCommand(self, self.editor))
        self.undo_cmd = lambda: self.execute(UndoCommand(self, self.editor))
        self.cut_cmd = lambda: self.execute(CutCommand(self, self.editor))
        self.paste_cmd = lambda: self.execute(PasteCommand(self, self.editor))

    def set_text(self, text: str) -> None:
        self.execute(SetCommand(self, self.editor), text)

    def get_text(self) -> str:
        return self.editor.get_selection()

    def execute(self, command: AbsCommand, *args, **kwargs) -> None:
        if command.execute(*args, **kwargs):
            self.history.push(command)
        
    def undo(self) -> None:
        command = self.history.pop()
        command.undo()

def main() -> None:
    app = App()
    app.create()
    
    app.set_text("Text") # Set text to "Text"
    print(app.get_text()) # Output the editor text ("Text")

    app.copy_cmd() # Copy text to clipboard
    app.undo() # Undo the previous command (set)
    print(app.get_text()) # Output the editor text (empty)
    app.paste_cmd() # Paste the text from clipboard ("Text")
    print(app.get_text()) # Outputs the editor text ("Text")
    
if __name__ == "__main__":
    main()

# ydoieiseie
# itbm
# wgi