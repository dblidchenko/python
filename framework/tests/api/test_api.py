import pytest

@pytest.mark.change
def test_remove_name(user):       #видаляємо імʼя користувача
   user.name = ''
   assert user.name == ''

@pytest.mark.check
def test_name(user):
   assert user.name == 'Dimas'

@pytest.mark.check
def test_second_name(user):
   assert user.second_name == 'Dimasik'