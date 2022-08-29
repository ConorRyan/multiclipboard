from time import sleep
import keyboard
import pyperclip

CLIPBOARD_IDX_START = 1
CLIPBOARD_IDX_END = 10

class MultiClipboard(object):
    def __init__(self):
        self.clipboards = ["" for _ in range(CLIPBOARD_IDX_START, CLIPBOARD_IDX_END)]

        for i in range(CLIPBOARD_IDX_START, CLIPBOARD_IDX_END):
            keyboard.add_hotkey(f"ctrl + {i}", self.save_clipboard, args=[i])
            keyboard.add_hotkey(
                f"ctrl + shift + {i}", self.paste_clipboard, args=[i], suppress=True
            )

    def save_clipboard(self, idx) -> None:
        assert idx >= CLIPBOARD_IDX_START and idx < CLIPBOARD_IDX_END
        keyboard.send("ctrl + c")
        sleep(0.1)  # Hack to leave time for clipboard to process
        self.clipboards[idx] = pyperclip.paste()

    def paste_clipboard(self, idx) -> None:
        assert idx >= CLIPBOARD_IDX_START and idx < CLIPBOARD_IDX_END
        pyperclip.copy(self.clipboards[idx])
        keyboard.send("ctrl + v")

MultiClipboard()
keyboard.wait("ctrl + 0")
