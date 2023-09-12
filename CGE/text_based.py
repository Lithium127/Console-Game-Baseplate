
import os
import contextlib

from random import choice



class World:
  data:dict
  _name:str
  _desc:str|list
  _areas:list
  
  def __init__(self,data:dict[str,any]):
    self.data = data

    self._name = "< MISSING >"
    with contextlib.suppress(KeyError):
      self._name = self.data["name"]
    
    self._desc = "No desc..."
    with contextlib.suppress(KeyError):
      self._desc = self.data["desc"]
    
    self._areas = []
    with contextlib.suppress(KeyError):
      self._areas = self.data["areas"]


  @property
  def name(self):
    return self._name
  @name.setter
  def name(self,value):
    pass

  @property
  def desc(self):
    if str(type(self._desc)) == "<class 'list'>":
      return choice(self._desc)
    else:
      return self._desc
  @desc.setter
  def desc(self,value):
    pass


    
    
    

