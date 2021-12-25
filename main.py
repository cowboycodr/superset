
from superset import Console
from superset import Extension

class NoteThis(Extension):
  def __init__(self):
    super().__init__()

  def run(self, instructions: dict):
    keyword, arguments = list(instructions.items())[0]

    if keyword.lower() != "notethis":
      return instructions

    print(arguments)

    return self.TERMINATE

if __name__ == '__main__':
  console = Console()

  console.use(NoteThis)

  console.start()