"def test_api_status():  response = type('Response', (), {'status_code': 404})()  assert response.status_code == 999" 
