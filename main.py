from superset import (
  Console,
  ConsoleCommand as Command,
  Extension,
)

# extension imports
import os

class SingleCommand(Extension):
  """
  Determines if command has no arguments 
  and executes it
  """

  def __init__(self):
    super().__init__()

  def run(self, keyword: str, arguments: list):
    if arguments != []:
      return self.CANCEL

    os.system(keyword)

    return self.TERMINATE

class Eval(Extension):
  """
  Quick access to eval'ing pythonic statements
  in the command-line
  """
  def __init__(self):
    super().__init__()

    self.set_trigger("eval")

  def run(self, keyword: str, instructions: list) -> "str | list":
    result = ""
    for command in instructions:
      for argument in command:
        result += argument['argument'] + " "

    result = result.replace("; ", "\n")

    print(exec(result))

    return self.TERMINATE

class Comment(Extension):
  def __init__(self):
    super().__init__()

    self.set_trigger("#")

  def run(self, keyword: str, instructions: list) -> "str | list":
    return self.TERMINATE

if __name__ == '__main__':
  console = Console()

  console.use(Comment)
  console.use(SingleCommand)
  console.use(Eval)

  console.start()