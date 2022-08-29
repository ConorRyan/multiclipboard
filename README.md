# multiclipboard

multiclipboard is a small python3 script allowing use of multiple clipboards at the same time.

`Ctrl + [NUMBER]` stores the selected content in a clipboard, and `Ctrl + Shift + [NUMBER]` pastes it, with number being any number from 1 to 9 via numpad or not. Use `Ctrl + 0` to exit.

`multiclip.py` can be ran from a terminal. `multiclip.pyw` can be used to run multiclipboard in the background.

The following pip dependencies are required:
- keyboard
- pyperclip
- pymsgbox (only for use in background mode)