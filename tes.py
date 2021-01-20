import requests
import json

tz = {'tz': 'Europe/Prague'}
data = json.dumps({'start': {"date": '12.20.2020 22:26:05'},
                   'end': {"date": '12.20.2020 22:23:05'},
                   })

print('ex1:')
url = 'http://localhost:8080/'
post = requests.get(url)
print(post.text)

print('ex2:')
url = 'http://localhost:8080/Europe/Prague'
post = requests.get(url)
print(post.text)

print('ex3-test1:')
url = 'http://localhost:8080/api/v1/time'
post = requests.post(url)
print(post.text)

print('ex3-test2:')
url = 'http://localhost:8080/api/v1/time'
data = json.dumps({'tz': 'Europe/Prague'})
post = requests.post(url, data)
print(post.text)

print('ex3-test3:')
url = 'http://localhost:8080/api/v1/time'
data = json.dumps({'tz': 'Wrong/Tz'})
post = requests.post(url, data)
print(post.text)

print('ex4-test1:')
url = 'http://localhost:8080/api/v1/date'
post = requests.post(url)
print(post.text)

print('ex4-test2:')
url = 'http://localhost:8080/api/v1/date'
data = json.dumps({'tz': 'Europe/Prague'})
post = requests.post(url, data)
print(post.text)

print('ex4-test3:')
url = 'http://localhost:8080/api/v1/date'
data = json.dumps({'tz': 'Wrong/Tz'})
post = requests.post(url, data)
print(post.text)

print('ex5-test:')
url = 'http://localhost:8080/api/v1/datediff'
data = json.dumps({'start': {"date": '12.20.2020 22:26:05'},
                   'end': {"date": '12.20.2020 22:23:05'},
                   })
post = requests.post(url, data)
print(post.text)

print('ex5-test2:')
url = 'http://localhost:8080/api/v1/datediff'
data = json.dumps({'start': {"date": '12.20.2020 22:26:05', 'tz': 'Asia/Tomsk'},
                   'end': {"date": '12.20.2020 22:26:05', 'tz': 'Europe/Prague'},
                   })
post = requests.post(url, data)
print(post.text)

print('ex5-test3:')
url = 'http://localhost:8080/api/v1/datediff'
data = json.dumps({'start': {"date": 'WITHOUT START TIME', 'tz': 'Asia/Tomsk'},
                   'end': {"date": '12.20.2020 22:26:05', 'tz': 'Europe/Prague'},
                   })
post = requests.post(url, data)
print(post.text)
