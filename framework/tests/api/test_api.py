import pytest
class User:

   def __init__(self):
      self.name = 'Serhii'
      self.second_name = 'Butenko'

@pytest.fixture                  #декоратор фікстури
def user():                      #функція, що генерує окремий екземпляр класу для кожного теста
   yield User()

#user = User()

def test_remove_name(user):       #видаляємо імʼя користувача
   user.name = ''
   assert user.name == ''

def test_name(user):
   assert user.name == 'Serhii'

def test_second_name(user):
   assert user.second_name == 'Butenko'