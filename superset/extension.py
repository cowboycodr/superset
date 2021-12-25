# Extension run input example:
# {"py": [["main.py"], ["secondary.py"]]}


class Extension:

  # return TERMINATE from "run" method to completely handle extension
  TERMINATE = "terminate"

  def __init__(self):
    pass

  def run(self, instructions: dict):
    pass