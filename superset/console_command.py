import os
from .superset_config import CONFIG

class ConsoleCommand:
  @staticmethod
  def build(instructions: list):
    result = ""
    
    first = True
    for command in instructions:
      for (keyword, subcommand) in command.items():
        if not first:
          result += " && "
          
        first_section = True
        for section in subcommand:
          if not first_section:
            result += " && "
            
          result += keyword
          
          for argument in section:
            string = argument['argument']
            value = argument['value']
            assigner = argument['assigner']
            
            if value:
              string = string + assigner + value
              
            result += " " + string
            
          if first_section: first_section = False
          
        if first: first = False
    
    return result
  
  def __init__(self, command: str) -> None:
    self.pre = command
    self.__command = command
  
  def __str__(self) -> str:
      return self.__command
    
  def __repr__(self) -> str:
      return self.__command  

  def _get_sections(self, split_command: list) -> list:
    divider: str = CONFIG["sectionDivider"]
    
    result = ' '.join(split_command[1:]).strip().split(divider)
    while ("" in result):
      result.remove("")
    return result
  
  def _parse(self):
    result = []
    
    commands = self.__command.split(CONFIG["commandDivider"])
    
    if self.__command.count(CONFIG["commandDivider"]) > 0:
      for command in commands:
        parsed_command = self._parse_command(command.strip())
        
        result.append({
          parsed_command['keyword']: parsed_command['arguments']
        })
    else:
      parsed_command = self._parse_command(self.__command)
      result.append({parsed_command['keyword']: parsed_command['arguments']})
      
    return result
  
  def _parse_command(self, command: str) -> dict:
    if command.count(" ") > 0:
      split_command = command.split(" ")
    
      keyword = split_command[0]
    
      arguments = []
      for section in self._get_sections(split_command):
        section_arguments = self._parse_arguments(section.split(" "))
          
        arguments.append(section_arguments)
      
      result = {
        "keyword": keyword,
        "arguments": arguments
      }
      
    else:
      result = {
        "keyword": command,
        "arguments": []
      }
    
    return result
  
  def _parse_arguments(self, arguments: list):
    parsed_arguments = []
    arguments = [a for a in arguments if a != ""]
    for argument in [a for a in arguments if a != ""]:
      identifier = ""
      assigner = ""
      value = None
      
      for _identifier in CONFIG["argumentIdentifiers"]:
        if argument.startswith(_identifier):
          identifier = _identifier
          argument = argument[len(_identifier):]
          break
      
      for _assigner in CONFIG["argumentAssigners"]:
        if _assigner in argument:
          assigner = _assigner
          split_argument = argument.split(_assigner)
          value = split_argument[1]
          argument = split_argument[0]
          break
      
      parsed_arguments.append({
        "argument": identifier + argument,
        "value": value,
        "assigner": assigner
      })
        
    return parsed_arguments
  
  def execute(self) -> None:
    instructions = self._parse()
    command = ConsoleCommand.build(instructions)
    
    message = self.pre + " -> " + command
    
    length = min(
      os.get_terminal_size()[0],
      len(message)
    )
    
    print("-" * length)
    print(message)
    print("-" * length)
    
    os.system(command)
  
  @property
  def command(self):
    return self._parse()