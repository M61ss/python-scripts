from query import Query
import time

samples = [
    # Italiano
    ("Oggi il sole splende e il cielo è sereno.", "IT"),
    ("Domani andrò al mercato per comprare frutta.", "IT"),
    ("La biblioteca è chiusa durante il weekend.", "IT"),
    ("Mi piace leggere libri nel tempo libero.", "IT"),
    ("Il gatto dorme sul divano accanto alla finestra.", "IT"),
    ("gatto", "IT"),
    ("cane", "IT"),
    ("libro", "IT"),
    ("mare", "IT"),
    ("fiore", "IT"),

    # Inglese
    ("The quick brown fox jumps over the lazy dog.", "EN"),
    ("She loves reading books in the evening.", "EN"),
    ("Tomorrow we will visit the museum in the city.", "EN"),
    ("The children are playing football in the park.", "EN"),
    ("He enjoys listening to classical music.", "EN"),
    ("dog", "EN"),
    ("book", "EN"),
    ("sun", "EN"),
    ("flower", "EN"),
    ("computer", "EN"),

    # Francese
    ("Demain, il fera beau et nous irons au marché.", "FR"),
    ("Le chat dort sur le canapé près de la fenêtre.", "FR"),
    ("J'aime lire des livres pendant mon temps libre.", "FR"),
    ("La bibliothèque est fermée le week-end.", "FR"),
    ("Elle écoute de la musique classique chaque soir.", "FR"),
    ("chien", "FR"),
    ("livre", "FR"),
    ("soleil", "FR"),
    ("fleur", "FR"),
    ("ordinateur", "FR"),

    # Spagnolo
    ("La biblioteca está cerrada durante el fin de semana.", "ES"),
    ("Mañana iremos al mercado a comprar frutas.", "ES"),
    ("El gato duerme en el sofá cerca de la ventana.", "ES"),
    ("Me gusta leer libros en mi tiempo libre.", "ES"),
    ("Los niños juegan fútbol en el parque.", "ES"),
    ("perro", "ES"),
    ("libro", "ES"),
    ("sol", "ES"),
    ("flor", "ES"),
    ("computadora", "ES"),

    # Tedesco
    ("Der Winter ist kalt, aber auch sehr schön.", "DE"),
    ("Die Kinder spielen im Park jeden Nachmittag.", "DE"),
    ("Ich liebe es, Bücher in meiner Freizeit zu lesen.", "DE"),
    ("Der Zug fährt um acht Uhr morgens ab.", "DE"),
    ("Die Katze schläft auf dem Sofa neben dem Fenster.", "DE"),
    ("Hund", "DE"),
    ("Buch", "DE"),
    ("Sonne", "DE"),
    ("Blume", "DE"),
    ("Computer", "DE"),

    # Portoghese
    ("O café da manhã foi delicioso hoje.", "PT"),
    ("A biblioteca está fechada durante o fim de semana.", "PT"),
    ("O gato dorme no sofá perto da janela.", "PT"),
    ("Eu gosto de ler livros no meu tempo livre.", "PT"),
    ("As crianças brincam no parque todas as tardes.", "PT"),
    ("gato", "PT"),
    ("cão", "PT"),
    ("livro", "PT"),
    ("sol", "PT"),
    ("flor", "PT"),

    # Olandese
    ("De kinderen spelen buiten in de tuin.", "NL"),
    ("De kat slaapt op de bank naast het raam.", "NL"),
    ("Ik lees graag boeken in mijn vrije tijd.", "NL"),
    ("De bibliotheek is in het weekend gesloten.", "NL"),
    ("Morgen ga ik naar de markt om fruit te kopen.", "NL"),
    ("kat", "NL"),
    ("hond", "NL"),
    ("boek", "NL"),
    ("zon", "NL"),
    ("bloem", "NL"),

    # Russo
    ("Сегодня вечером будет очень холодно.", "RU"),
    ("Кошка спит на диване рядом с окном.", "RU"),
    ("Я люблю читать книги в свободное время.", "RU"),
    ("Библиотека закрыта на выходных.", "RU"),
    ("Дети играют в парке каждый день.", "RU"),
    ("кот", "RU"),
    ("собака", "RU"),
    ("книга", "RU"),
    ("солнце", "RU"),
    ("цветок", "RU"),

    # Cinese (semplificato)
    ("今天的天气非常好。", "ZH"),
    ("猫在窗边的沙发上睡觉。", "ZH"),
    ("我喜欢在空闲时间阅读书籍。", "ZH"),
    ("图书馆在周末关闭。", "ZH"),
    ("孩子们每天在公园玩耍。", "ZH"),
    ("猫", "ZH"),
    ("狗", "ZH"),
    ("书", "ZH"),
    ("太阳", "ZH"),
    ("花", "ZH"),

    # Giapponese
    ("今日は学校に行きます。", "JA"),
    ("猫は窓のそばのソファで寝ています。", "JA"),
    ("私は自由時間に本を読むのが好きです。", "JA"),
    ("図書館は週末閉館です。", "JA"),
    ("子供たちは毎日公園で遊んでいます。", "JA"),
    ("猫", "JA"),
    ("犬", "JA"),
    ("本", "JA"),
    ("太陽", "JA"),
    ("花", "JA"),

    # Arabo
    ("السماء صافية اليوم والشمس مشرقة.", "AR"),
    ("القط ينام على الأريكة بجانب النافذة.", "AR"),
    ("أحب قراءة الكتب في وقت فراغي.", "AR"),
    ("المكتبة مغلقة في عطلة نهاية الأسبوع.", "AR"),
    ("الأطفال يلعبون في الحديقة كل يوم.", "AR"),
    ("قط", "AR"),
    ("كلب", "AR"),
    ("كتاب", "AR"),
    ("شمس", "AR"),
    ("زهرة", "AR"),

    # Svedese
    ("Idag skiner solen och himlen är klar.", "SV"),
    ("Katten sover på soffan bredvid fönstret.", "SV"),
    ("Jag gillar att läsa böcker på fritiden.", "SV"),
    ("Biblioteket är stängt under helgen.", "SV"),
    ("Imorgon går jag till marknaden för att köpa frukt.", "SV"),
    ("katt", "SV"),
    ("hund", "SV"),
    ("bok", "SV"),
    ("blomma", "SV"),
    ("dator", "SV"),

    # Danese
    ("I dag skinner solen, og himlen er klar.", "DA"),
    ("Katten sover på sofaen ved siden af vinduet.", "DA"),
    ("Jeg kan godt lide at læse bøger i min fritid.", "DA"),
    ("Biblioteket er lukket i weekenden.", "DA"),
    ("I morgen går jeg til markedet for at købe frugt.", "DA"),
    ("kat", "DA"),
    ("hund", "DA"),
    ("bog", "DA"),
    ("blomst", "DA"),
    ("computer", "DA"),

    # Norvegese
    ("I dag skinner solen og himmelen er klar.", "NO"),
    ("Katten sover på sofaen ved vinduet.", "NO"),
    ("Jeg liker å lese bøker på fritiden.", "NO"),
    ("Biblioteket er stengt i helgen.", "NO"),
    ("I morgen går jeg til markedet for å kjøpe frukt.", "NO"),
    ("katt", "NO"),
    ("hund", "NO"),
    ("bok", "NO"),
    ("blomst", "NO"),
    ("datamaskin", "NO"),

    # Finlandese
    ("Tänään aurinko paistaa ja taivas on selkeä.", "FI"),
    ("Kissa nukkuu sohvan vieressä ikkunan luona.", "FI"),
    ("Pidän kirjojen lukemisesta vapaa-aikana.", "FI"),
    ("Kirjasto on suljettu viikonloppuna.", "FI"),
    ("Huomenna menen torille ostamaan hedelmiä.", "FI"),
    ("kissa", "FI"),
    ("koira", "FI"),
    ("kirja", "FI"),
    ("kukka", "FI"),
    ("tietokone", "FI"),

    # Ceco
    ("Dnes svítí slunce a obloha je jasná.", "CS"),
    ("Kočka spí na pohovce vedle okna.", "CS"),
    ("Rád čtu knihy ve svém volném čase.", "CS"),
    ("Knihovna je o víkendu zavřená.", "CS"),
    ("Zítra půjdu na trh koupit ovoce.", "CS"),
    ("kočka", "CS"),
    ("pes", "CS"),
    ("kniha", "CS"),
    ("květina", "CS"),
    ("počítač", "CS"),

    # Polacco
    ("Dziś świeci słońce i niebo jest bezchmurne.", "PL"),
    ("Kot śpi na kanapie obok okna.", "PL"),
    ("Lubię czytać książki w wolnym czasie.", "PL"),
    ("Biblioteka jest zamknięta w weekend.", "PL"),
    ("Jutro pójdę na targ kupić owoce.", "PL"),
    ("kot", "PL"),
    ("pies", "PL"),
    ("książka", "PL"),
    ("kwiat", "PL"),
    ("komputer", "PL"),

    # Turco
    ("Bugün hava çok güzel ve gökyüzü açık.", "TR"),
    ("Kedi pencerenin yanındaki kanepede uyuyor.", "TR"),
    ("Boş zamanlarımda kitap okumayı seviyorum.", "TR"),
    ("Kütüphane hafta sonları kapalıdır.", "TR"),
    ("Yarın meyve almak için pazara gideceğim.", "TR"),
    ("kedi", "TR"),
    ("köpek", "TR"),
    ("kitap", "TR"),
    ("çiçek", "TR"),
    ("bilgisayar", "TR"),

    # Greco
    ("Σήμερα ο ήλιος λάμπει και ο ουρανός είναι καθαρός.", "EL"),
    ("Η γάτα κοιμάται στον καναπέ δίπλα στο παράθυρο.", "EL"),
    ("Μου αρέσει να διαβάζω βιβλία στον ελεύθερο χρόνο μου.", "EL"),
    ("Η βιβλιοθήκη είναι κλειστή τα Σαββατοκύριακα.", "EL"),
    ("Αύριο θα πάω στη αγορά για να αγοράσω φρούτα.", "EL"),
    ("γάτα", "EL"),
    ("σκύλος", "EL"),
    ("βιβλίο", "EL"),
    ("λουλούδι", "EL"),
    ("υπολογιστής", "EL"),

    # Ungherese
    ("Ma süt a nap és az ég tiszta.", "HU"),
    ("A macska alszik a kanapén az ablak mellett.", "HU"),
    ("Szeretek könyveket olvasni a szabadidőmben.", "HU"),
    ("A könyvtár hétvégén zárva tart.", "HU"),
    ("Holnap elmegyek a piacra gyümölcsöt venni.", "HU"),
    ("macska", "HU"),
    ("kutya", "HU"),
    ("könyv", "HU"),
    ("virág", "HU"),
    ("számítógép", "HU"),

    # Coreano
    ("오늘 날씨가 매우 좋습니다.", "KO"),
    ("고양이가 창가 소파에서 자고 있습니다.", "KO"),
    ("나는 자유 시간에 책 읽기를 좋아합니다.", "KO"),
    ("도서관은 주말에 닫습니다.", "KO"),
    ("내일 시장에 가서 과일을 살 거예요.", "KO"),
    ("고양이", "KO"),
    ("개", "KO"),
    ("책", "KO"),
    ("꽃", "KO"),
    ("컴퓨터", "KO"),

    # Vietnamita
    ("Hôm nay trời nắng và bầu trời trong xanh.", "VI"),
    ("Con mèo đang ngủ trên ghế gần cửa sổ.", "VI"),
    ("Tôi thích đọc sách vào thời gian rảnh.", "VI"),
    ("Thư viện đóng cửa vào cuối tuần.", "VI"),
    ("Ngày mai tôi sẽ đi chợ mua hoa quả.", "VI"),
    ("mèo", "VI"),
    ("chó", "VI"),
    ("sách", "VI"),
    ("hoa", "VI"),
    ("máy tính", "VI"),

    # Tailandese
    ("วันนี้อากาศดีและท้องฟ้าแจ่มใส", "TH"),
    ("แมวกำลังนอนบนโซฟาข้างหน้าต่าง", "TH"),
    ("ฉันชอบอ่านหนังสือในเวลาว่าง", "TH"),
    ("ห้องสมุดปิดในวันหยุดสุดสัปดาห์", "TH"),
    ("พรุ่งนี้ฉันจะไปตลาดเพื่อซื้อผลไม้", "TH"),
    ("แมว", "TH"),
    ("สุนัข", "TH"),
    ("หนังสือ", "TH"),
    ("ดอกไม้", "TH"),
    ("คอมพิวเตอร์", "TH"),
]

def lang_detection_accuracy():
    n_correct = 0
    for i, sample in enumerate(samples):
        query = Query(sample[0])
        if query.lang == sample[1]:
            n_correct += 1
    return n_correct / len(samples)

if __name__ == "__main__":
    print("Language detection accuracy:")
    start_time = time.time()
    print(f"Computed global language detection accuracy: {lang_detection_accuracy()}")
    elapsed_time = time.time() - start_time
    time_for_phrase = elapsed_time / len(samples)
    print(f"Execution time: {elapsed_time} s")
    print(f"Average detection time for single phrase: {time_for_phrase} s")