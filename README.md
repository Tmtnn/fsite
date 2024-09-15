# Flask Web Uygulaması

Bu proje, Flask kullanarak basit bir web uygulaması oluşturur. Uygulama çeşitli işlevler sunar ve kullanıcıların çeşitli etkileşimlerde bulunmasına olanak tanır.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Yol ve Sayfalar](#yol-ve-sayfalar)
- [Gereksinimler](#gereksinimler)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Depoyu Klonlayın:**

   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   cd proje-adi


2. **Sanallaştırılmış Bir Ortam Oluşturun (Opsiyonel):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows için: venv\Scripts\activate
   ```

3. **Gerekli Kütüphaneleri Yükleyin:**

   ```bash
   pip install flask
   ```

4. **Uygulamayı Çalıştırın:**

   ```bash
   python app.py
   ```

   Uygulama varsayılan olarak `http://127.0.0.1:5000/` adresinde çalışacaktır.

## Kullanım

Uygulama, aşağıdaki sayfalara erişim sağlar:

- **Ana Sayfa (`/`)**
  - Uygulamanın ana sayfasını içerir ve diğer sayfalara bağlantılar sunar.

- **Şifre Oluşturucu (`/sifreolusturucu`)**
  - Rastgele bir şifre oluşturur ve kullanıcıya gösterir.

- **Rastgele Gerçekler (`/facts`)**
  - Kullanıcıya rastgele teknolojik gerçekler sunar.

- **Yazı Tura (`/yazitura`)**
  - Rastgele olarak "yazı" veya "tura" sonucunu gösterir.

- **Rastgele Resim Gösterici (`/resimg`)**
  - Rastgele bir resim gösterir.

## Yol ve Sayfalar

Uygulamanın yönlendirdiği URL'ler ve işlevler:

- `/` - Ana sayfa, uygulamanın diğer sayfalarına bağlantılar içerir.
- `/sifreolusturucu` - Rastgele şifre oluşturur ve gösterir.
- `/facts` - Teknolojik gerçekleri rastgele sunar.
- `/yazitura` - Yazı tura oyunu oynatır.
- `/resimg` - Rastgele bir resim gösterir.

## Gereksinimler

- Python 3.x
- Flask

