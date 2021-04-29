import requests
request = requests.get('http://fast.wistia.net/embed/iframe/ldvcdu9sj6')
texto = request.text
final = texto.find("bin")
inicio = texto.find("http://embed")
url = (texto[inicio:final]) + 'mp4'
r = requests.get(url)
f = open('video1.mp4', 'wb')
for chunk in r.iter_content(chunk_size=255):
    if chunk:
        f.write(chunk)
f.close()


'''
wvideo = '3z0lxlu9p3'
for c in wvideo:
    request = requests.get(f'http://fast.wistia.net/embed/iframe/{wvideo}')
    print(request.content)'''

# http://fast.wistia.net/embed/iframe/3z0lxlu9p3
