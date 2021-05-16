import requests

wvideo = ('hxech2o4ig',
'mi8fwpevxo',
'ht7phhdnwl',
'si8nkul0nm',
'2wgcxgv3id',
'q56vbraapp',
'zf8k53lioy',
'lntnfm08z8',
'o9fn6a4q2y',
'8a849fltzg',
'kh0o3c2o10',
'r3u069dl2c',
'11gjoknsac',
'xirlafh5ok')
for c in range(0, len(wvideo)):
    aula = ('2.5 - Executando SEO como produto _ 1. O que é SEO - parte 1.mp4',
'2.5 - Executando SEO como produto _ 2. O que é SEO - parte 2.mp4',
'2.5 - Executando SEO como produto _ 3. SEO on-page - parte 1.mp4',
'2.5 - Executando SEO como produto _ 4. SEO on-page - parte 2.mp4',
'2.5 - Executando SEO como produto _ 5. Link Building.mp4',
'2.5 - Executando SEO como produto _ 6. SEO para Youtube.mp4',
'2.6 - Executando App Store Optimization (ASO) _ 1. O que é ASO e qual seu modelo de Growth.mp4',
'2.6 - Executando App Store Optimization (ASO) _ 2. Quais são os fatores de influência.mp4',
'2.6 - Executando App Store Optimization (ASO) _ 3. Aplicando melhores práticas de ASO.mp4',
'2.6 - Executando App Store Optimization (ASO) _ 4. Mensuração e ferramentas.mp4',
'2.7 - Aprofundando viral loops _ 1. Growth Loops x Funis.mp4',
'2.7 - Aprofundando viral loops _ 2. Mensuração e coeficiente viral.mp4',
'2.7 - Aprofundando viral loops _ 3. Os diversos tipos de growth loops.mp4',
'2.7 - Aprofundando viral loops _ 4. Encontrando o melhor modelo para o seu produto.mp4')
    request = requests.get(f'http://fast.wistia.net/embed/iframe/{wvideo[c]}')
    texto = request.text
    final = texto.find("bin")
    inicio = texto.find("http://embed")
    url = (texto[inicio:final]) + 'mp4'
    r = requests.get(url)
    f = open(aula[c], 'wb')
    for chunk in r.iter_content(chunk_size=255):
        if chunk:
            f.write(chunk)
    f.close()


'''
wvideo = '3z0lxlu9p3'
for c in wvideo:

    request = requests.get(f'http://fast.wistia.net/embed/iframe/{wvideo}')

    print(request.content)
'''


# http://fast.wistia.net/embed/iframe/3z0lxlu9p3




