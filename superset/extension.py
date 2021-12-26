# Extension run input example:
# {"py": [["main.py"], ["secondary.py"]]}


class Extension:

  TERMINATE   = "terminate" # return from method to stop the handling of command
  CANCEL      = "cancel"    # return from method to stop the extension process
  TRIGGER     = None        # trigger or keyword to activate extension | if none always activates

  def __init__(self):
    pass

  def set_trigger(self, new: str) -> None:
    self.TRIGGER = new

  def run(self, keyword: str, instructions: list) -> "str | list":
    return instructions