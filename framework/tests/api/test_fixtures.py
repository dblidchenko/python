import pytest

class User:

   def __init__(self) -> None:
      self.name = None
      self.second_name = None
   
   def create(self):
      self.name = 'Dimas'
      self.second_name = 'Dimasik'

   def remove(self):
      self.name = ''
      self.second_name = ''

   def test_change_name():
      user = User()
      user.create()

      assert user.name == 'Dimas'
      user.remove()

   def test_change_second_name():
      user = User()
      user.create()

      assert user.name == 'Dimasik'
      user.remove()