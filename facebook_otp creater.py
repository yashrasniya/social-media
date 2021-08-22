import requests
import time
# r = requests.get('https://www.facebook.com/recover/password/?u=100010489384107&n=928250&fl=default_recover&sih=0')
r = requests.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
data =r.text.split('name="csrfmiddlewaretoken" value=')[1].split('"')[1]

url='http://127.0.0.1:8000/admin/login/?next='
myobj=f'{data}&username=yash&password=202020&next=%2Fadmin%2F'
x = requests.post(url, data = myobj)
print(x.status_code,x.text)
start_time = time.time()
# for a in range(100000,999999):
#     print(a)
# for a in r.text.split('retryDelays'):
#     print(a,"\n\n\n")
print("--- %s seconds ---" % (time.time() - start_time))
