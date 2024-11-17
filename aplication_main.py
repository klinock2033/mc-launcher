import asyncio
from colorama import Fore, Style
from PyQt5.QtCore import QObject, pyqtSignal
import time

class ApplicationLogic(QObject):
    # Definește un semnal personalizat care trimite un text
    update_text_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def start_button(self):
        self.dev_Tool("Launcher Start", "done")
    def Run_launcher(self):
        # Emetere semnal pentru textul funcției
        try:
            loop = asyncio.get_event_loop()

            print(str(loop))
            if loop.is_running():
                # Folosește ensure_future pentru a adăuga task-ul în ciclul de evenimente curent
                loop.run_until_complete(self.dev_Tool("Launcher Start2", "done"))
            else:
                # Rulează pentru prima dată cu asyncio.run() doar dacă nu există un ciclu activ
                #asyncio.run(self.dev_Tool("Launcher Start1", "done"))
                asyncio.run(self.test1())
        except Exception as e:
            #There is no current event loop in thread 'MainThread'.
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")

     async def test1(self):
        numar = 1

        while True:
            print(numar)
            numar += 1
            time.sleep(1)  # Așteaptă 1 secundă înainte de a continua

    async def dev_Tool(self, text, msgType):
        ToolVersion = f"{Fore.CYAN}[Dev-tool-v1.0]:{Style.RESET_ALL}"
        ToolVersionHtml = "<font color='cyan'>[Dev-tool-v1.0]:</font>"
        color_map_console = {
            "simple": Style.RESET_ALL,
            "done": Fore.GREEN,
            "warn": Fore.YELLOW,
            "error": Fore.RED
        }
        if msgType == "simple":
            message = f"{ToolVersionHtml} <font color='white'>{text}</font>"
        elif msgType == "done":
            message = f"{ToolVersionHtml} <font color='green'>{text}</font>"
        elif msgType == "warn":
            message = f"{ToolVersionHtml} <font color='yellow'>{text}</font>"
        elif msgType == "error":
            message = f"{ToolVersionHtml} <font color='red'>{text}</font>"
        else:
            message = f"{ToolVersionHtml} <font color='red'>Dev tool error!</font>"

        colorConsole = color_map_console.get(msgType, Fore.RED)
        msg = message
        msgConsole = f"{ToolVersion} {colorConsole}{text}{Style.RESET_ALL}"
        print(msgConsole)
        self.update_text_signal.emit(msg)  # Emitere mesaj către interfață



