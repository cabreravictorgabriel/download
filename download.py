import requests
request = requests.get('http://fast.wistia.net/embed/iframe/ldvcdu9sj6')
texto = request.text
ocorrencia = texto.find("bin")
ocorrencia2 = texto.find("http://embed")
url = (texto[ocorrencia2:(ocorrencia)]) + 'mp4'
print (url)





'''
wvideo = '3z0lxlu9p3'
for c in wvideo:
    request = requests.get(f'http://fast.wistia.net/embed/iframe/{wvideo}')
    print(request.content)'''

# http://fast.wistia.net/embed/iframe/3z0lxlu9p3
