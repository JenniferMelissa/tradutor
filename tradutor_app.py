#instalar biblioteca de tradicao, prompt de comando: pip install deep_translator
#bilbioteca
from deep_translator import GoogleTranslator 

tradutor = GoogleTranslator(source='auto',target='pt')

while True:
    try:
        texto = input('Texto a ser traduzido: ')
        texto_traduzido = tradutor.translate(texto)

        print(f'Texto traduzido: "{texto_traduzido}".')
        
        repetir = input('Deseja traduzir outro texto (s/n)?').lower()
        
        if repetir == 's':
            continue
        else:
            break
    except:
        print('Não foi possível traduzir.')    


#usar  pip freeze > requirements.txt
#pois como é preciso instalar a extensao na minha maquina, e quando voce abrir na sua maquina o projeto ele e for criar o ambiente virtual, ele vai baixar as extensoes atraves desse
#novo arquivo gerado requirements.txt
#se voce fizer mais algum import e ja fez o requirements.txt, precisa refazer esse arquivo
    