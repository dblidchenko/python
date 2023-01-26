import pytest
import requests


@pytest.mark.http
def test_first_request():
   r = requests.get('https://api.github.com/zen')
   print(f"Value of the attribute is {r.text}")

@pytest.mark.http
def test_second_request():
   r = requests.get('https://api.github.com/users/defunkt')
   body = r.json()                                        #text, json - формат передачі даних
   headers = r.headers

   assert body['name'] == 'Chris Wanstrath'
   assert r.status_code == 200
   assert headers['Server'] == 'GitHub.com'
   
@pytest.mark.http
def test_status_code_request():
   r = requests.get('https://api.github.com/users/d_blidchenko')

   assert r.status_code == 404