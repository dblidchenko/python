import pytest

@pytest.mark.check
def test_name(user):
   assert user.name == 'Dimas'

@pytest.mark.check
def test_change_second_name(user):
   assert user.second_name == 'Dimasik'
