from posixpath import commonpath
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