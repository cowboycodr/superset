from superset.extension import Extension
from superset.superset_config import CONFIG
from superset.console_command import ConsoleCommand as Command

class Console:
  def __init__(self) -> None:
    self.__config = CONFIG
  
  @staticmethod
  def command(command: str):
    command = Command(command)
    
    command.execute()
  
  @staticmethod
  def start() -> None:
    while (prompt := input(">>> ")) != "exit":
      Command(prompt).execute()

class Console:
  def __init__(self) -> None:
    self.__used = []

  def use(self, ext: Extension):
    self.__used.append(ext)

  def command(self, command: str):
    command = Command(command)

    for extension in self.__used:
      command.apply(extension)

    command.execute()

  def start(self):
    while (prompt := input(">>> ")) != "exit":
      self.command(prompt)