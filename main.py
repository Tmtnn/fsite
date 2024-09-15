from flask import Flask
import random



app = Flask(__name__)

@app.route("/")
def buton():
   return f'''
    <html>
        <head>
            <title>Ana Sayfa</title>
        </head>
        <body>
            <a href="/facts"><button type="button">Gercekler</button></a>
            <a href="/yazitura"><button type="button">Yazi Tura</button></a>
            <a href="/sifreolusturucu"><button type="button">Şifre Oluşturucu</button></a>
            <a href="/resimg"><button type="button">Rastgele Resim Gosterici</button></a>
        </body>
    </html>
    '''

@app.route("/sifreolusturucu")
def sfrol():
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    uzunluk = random.randint(8, 72)

    parola = ''
    for _ in range(uzunluk):
        parola += random.choice(karakterler)

    return f'''
    <html>
        <head>
            <title>Şifre Oluşturucu</title>
        </head>
        <body>
            <p>Oluşturulan Şifre: {parola}</p>
            <a href="/"><button type="button">Ana Sayfa</button></a>
            <a href="/sifreolusturucu"><button type="button">Yeniden Oluştur</button></a>
        </body>
    </html>
    '''


@app.route("/facts")
def facts():
    facts_list=['''Teknolojik bağımlılıktan mustarip olan çoğu kişi,
                 kendilerini şebeke kapsama alanı dışında bulduklarında
                 veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.''', 
                 '''2018 yılında yapılan bir araştırmaya göre 18-34 yaş
                   arası kişilerin %50'den fazlası
                   kendilerini akıllı telefonlarına bağımlı olarak görüyor.''']
    return f'''
    <html>
        <head>
            <title>Rasgele Gercekler</title>
        </head>
        <body>
            <p>{random.choice(facts_list)}</p>
            <a href="/"><button type="button">Ana Sayfa</button></a>
            <a href="/facts"><button type="button">Rasgele Gercekler</button></a>
        </body>
    </html>
    '''

@app.route("/yazitura")
def yztr():
    yaztura = ['yazi', 'tura']
    result = random.choice(yaztura)
    return f'''
    <html>
        <head>
            <title>Yazi Tura</title>
        </head>
        <body>
            <p>{result.upper()}</p>
            <a href="/yazitura"><button type="button">Yeniden Oyna</button></a>
            <a href="/"><button type="button">Ana Sayfa</button></a>
        </body>
    </html>
    '''

@app.route("/resimg")
def resim():

    resim_url = 'https://picsum.photos/800/600'
    
    return f'''
    <html>
        <head>
            <title>Rastgele Resim</title>
        </head>
        <body>
            <img src="{resim_url}" alt="Rastgele Resim">
            <br>
            <a href="/resimg"><button type="button">Yeniden Göster</button></a>
            <a href="/"><button type="button">Ana Sayfa</button></a>
        </body>
    </html>
    '''




app.run(debug=True)