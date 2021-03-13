from requests import get, post, delete

print(post('http://localhost:5000/api/v2/users', json={'name': 'Anya', 'position': 'baker',
                                                       'surname': 'S', 'age': 22, 'address': 'module_3',
                                                       'speciality': 'PK',
                                                       'hashed_password': '1234', 'email': 'an@gmail.com'}).json())
print(get('http://localhost:5000/api/v2/users/1'))
print(delete('http://localhost:5000/api/v2/users/6'))