import time
import sys
from scraper import Scraper
from nlp import NLP

samples_mix = [
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
samples_IT = [
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
]
samples_EN = [
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
]
samples_FR = [
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
]
samples_ES = [
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
]
samples_DE = [
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
]
samples_PT = [
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
]
samples_NL = [
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
]
samples_RU = [
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
]
samples_ZH = [
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
]
samples_JA = [
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
]
samples_AR = [
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
]

sample_words_IT = [
    ("gatto", "IT"),
    ("cane", "IT"),
    ("mare", "IT"),
    ("montagna", "IT"),
    ("città", "IT"),
    ("libro", "IT"),
    ("scuola", "IT"),
    ("strada", "IT"),
    ("sole", "IT"),
    ("luna", "IT"),
    ("albero", "IT"),
    ("fiore", "IT"),
    ("vino", "IT"),
    ("pane", "IT"),
    ("caffè", "IT"),
    ("tempo", "IT"),
    ("musica", "IT"),
    ("stella", "IT"),
    ("amore", "IT"),
    ("notte", "IT"),
]
sample_words_EN = [
    ("dog", "EN"),
    ("cat", "EN"),
    ("tree", "EN"),
    ("flower", "EN"),
    ("river", "EN"),
    ("mountain", "EN"),
    ("book", "EN"),
    ("school", "EN"),
    ("city", "EN"),
    ("village", "EN"),
    ("music", "EN"),
    ("star", "EN"),
    ("love", "EN"),
    ("night", "EN"),
    ("day", "EN"),
    ("house", "EN"),
    ("car", "EN"),
    ("computer", "EN"),
    ("window", "EN"),
    ("sun", "EN"),
]
sample_words_FR = [
    ("chien", "FR"),
    ("chat", "FR"),
    ("arbre", "FR"),
    ("fleur", "FR"),
    ("rivière", "FR"),
    ("montagne", "FR"),
    ("livre", "FR"),
    ("école", "FR"),
    ("ville", "FR"),
    ("village", "FR"),
    ("musique", "FR"),
    ("étoile", "FR"),
    ("amour", "FR"),
    ("nuit", "FR"),
    ("jour", "FR"),
    ("maison", "FR"),
    ("voiture", "FR"),
    ("ordinateur", "FR"),
    ("fenêtre", "FR"),
    ("soleil", "FR"),
]
sample_words_ES = [
    ("perro", "ES"),
    ("gato", "ES"),
    ("árbol", "ES"),
    ("flor", "ES"),
    ("río", "ES"),
    ("montaña", "ES"),
    ("libro", "ES"),
    ("escuela", "ES"),
    ("ciudad", "ES"),
    ("pueblo", "ES"),
    ("música", "ES"),
    ("estrella", "ES"),
    ("amor", "ES"),
    ("noche", "ES"),
    ("día", "ES"),
    ("casa", "ES"),
    ("coche", "ES"),
    ("computadora", "ES"),
    ("ventana", "ES"),
    ("sol", "ES"),
]
sample_words_DE = [
    ("Hund", "DE"),
    ("Katze", "DE"),
    ("Baum", "DE"),
    ("Blume", "DE"),
    ("Fluss", "DE"),
    ("Berg", "DE"),
    ("Buch", "DE"),
    ("Schule", "DE"),
    ("Stadt", "DE"),
    ("Dorf", "DE"),
    ("Musik", "DE"),
    ("Stern", "DE"),
    ("Liebe", "DE"),
    ("Nacht", "DE"),
    ("Tag", "DE"),
    ("Haus", "DE"),
    ("Auto", "DE"),
    ("Computer", "DE"),
    ("Fenster", "DE"),
    ("Sonne", "DE"),
]

sample_words_wikisearch_IT = [
    "gatto",
    "cane",
    "scienza",
    "università",
    "Italia",
    "politica",
    "arte",
    "musica",
    "letteratura",
    "storia",
]
sample_words_wikisearch_EN = [
    "cat",
    "dog",
    "science",
    "university",
    "Italy",
    "politics",
    "art",
    "music",
    "literature",
    "history",
]

samples_periods_wikisearch_IT = [
    "Oggi il sole splende e molti turisti passeggiano nel centro storico, fermandosi spesso nei caffè e nei negozi di souvenir.",
    "La biblioteca comunale è stata rinnovata di recente. Ora offre spazi digitali, sale studio moderne e una collezione di manoscritti antichi che attirano ricercatori da tutta Europa.",
    "Il calcio è lo sport più seguito in Italia. Le squadre locali hanno un forte legame con i tifosi, che partecipano con entusiasmo a ogni partita.",
    "Ho comprato un nuovo libro di storia dell’arte. È molto interessante e ben illustrato, con spiegazioni che rendono comprensibili anche i concetti più complessi.",
    "Il treno ad alta velocità collega Milano e Roma in poche ore, trasformando radicalmente il modo di viaggiare tra le due città.",
    "La cucina italiana è famosa per la pasta, la pizza e il vino. Ogni regione ha specialità diverse e tradizioni culinarie tramandate da generazioni.",
    "Molti studenti si preparano agli esami universitari nelle biblioteche cittadine, spesso lavorando in gruppo fino a tarda sera.",
    "Il mare Mediterraneo ospita una grande varietà di pesci e specie marine, ma è anche minacciato dall’inquinamento e dalla pesca intensiva.",
    "La tecnologia sta cambiando il modo in cui lavoriamo e comunichiamo, creando nuove opportunità ma anche nuove sfide per la società.",
    "Le Dolomiti sono considerate tra le montagne più belle del mondo, meta preferita di escursionisti, fotografi e amanti della natura.",
]
samples_periods_wikisearch_EN = [
    "The quick brown fox jumps over the lazy dog.",
    "Technology is evolving rapidly. Artificial intelligence and machine learning are now part of daily life, shaping industries and redefining how people interact with information.",
    "I love reading books in the evening. They help me relax after work and often inspire new ideas for my own writing projects.",
    "The city has built new parks and playgrounds for children, creating safer spaces and greener areas for the community.",
    "Traveling by train is fast and convenient in many European countries, and it is also more environmentally friendly than flying.",
    "Music has the power to inspire and connect people. It is a universal language that transcends borders, cultures, and generations.",
    "The library downtown is a peaceful place where many students gather, especially during exam season when every desk is full.",
    "Climate change is one of the biggest challenges humanity faces today, demanding urgent solutions and cooperation between nations.",
    "Modern art often surprises viewers with unusual shapes and colors, provoking debates about what art really means in contemporary society.",
    "The new museum exhibition explores ancient civilizations and their cultures, presenting artifacts that reveal the complexity of early human societies.",
]
samples_periods_wikisearch_FR = [
    "Le soleil brille aujourd’hui et la place principale est pleine de visiteurs.",
    "La bibliothèque nationale a ouvert une nouvelle section. Elle contient des manuscrits rares et précieux, étudiés par des spécialistes venus du monde entier.",
    "Le football est un sport très populaire en France. Les supporters suivent chaque match avec passion et remplissent les stades de chants et de drapeaux.",
    "J’aime écouter de la musique classique le soir. Cela me détend et me donne de l’énergie, surtout après une longue journée de travail.",
    "Le train à grande vitesse relie Paris et Lyon en moins de deux heures, facilitant les voyages d’affaires et le tourisme.",
    "La cuisine française est célèbre pour ses fromages, ses vins et ses desserts raffinés, qui varient considérablement d’une région à l’autre.",
    "De nombreux étudiants fréquentent les cafés pour étudier ensemble, discuter de leurs projets et profiter d’une ambiance conviviale.",
    "La Méditerranée est une mer riche en histoire et en commerce, mais elle est aujourd’hui confrontée à de sérieux problèmes écologiques.",
    "La technologie change nos habitudes quotidiennes et nos relations sociales, créant parfois plus de dépendance que de liberté.",
    "Les Alpes françaises offrent des paysages magnifiques et des stations de ski réputées, attirant touristes et sportifs du monde entier.",
]
samples_periods_wikisearch_ES = [
    "Hoy hace sol y la ciudad está llena de turistas, que pasean por las calles antiguas y disfrutan de la gastronomía local.",
    "La biblioteca central fue renovada recientemente. Ahora tiene áreas digitales y espacios de estudio modernos que facilitan la investigación.",
    "El fútbol es el deporte más seguido en España. Los aficionados apoyan a sus equipos con entusiasmo y llenan los estadios en cada temporada.",
    "Compré un nuevo libro de literatura contemporánea. Es muy interesante y profundo, con personajes que reflejan la sociedad actual.",
    "El tren de alta velocidad conecta Madrid y Barcelona en pocas horas, ofreciendo comodidad y eficiencia a miles de viajeros cada día.",
    "La cocina española es famosa por la paella, el jamón y las tapas. Cada región tiene su estilo propio y sus tradiciones culinarias.",
    "Muchos estudiantes preparan sus exámenes en las bibliotecas universitarias, donde encuentran un ambiente tranquilo y concentrado.",
    "El mar Mediterráneo es hogar de una gran diversidad de especies, pero enfrenta amenazas relacionadas con el cambio climático.",
    "La tecnología influye cada día más en la forma en que trabajamos y nos comunicamos, transformando también la educación y el ocio.",
    "Los Pirineos son montañas hermosas con paisajes impresionantes y una gran variedad de actividades deportivas durante todo el año.",
]
samples_periods_wikisearch_DE = [
    "Heute scheint die Sonne und viele Menschen spazieren durch die Altstadt.",
    "Die Stadtbibliothek wurde kürzlich renoviert. Sie bietet jetzt digitale Bereiche und moderne Lesesäle, die besonders bei Studenten beliebt sind.",
    "Fußball ist der beliebteste Sport in Deutschland. Die Fans sind sehr engagiert und folgen ihren Mannschaften durch das ganze Land.",
    "Ich habe ein neues Buch über Philosophie gekauft. Es ist spannend und gut geschrieben, mit Argumenten, die zum Nachdenken anregen.",
    "Der Hochgeschwindigkeitszug verbindet Berlin und München in wenigen Stunden, was Geschäftsreisen deutlich erleichtert.",
    "Die deutsche Küche ist bekannt für Brot, Wurst und Bier. Jede Region hat ihre Spezialitäten, die oft mit langen Traditionen verbunden sind.",
    "Viele Studenten bereiten sich in Bibliotheken auf ihre Prüfungen vor, manchmal bis spät in die Nacht.",
    "Die Nordsee ist bekannt für ihre raue Küste und starken Winde, aber auch für ihre malerischen Inseln.",
    "Technologie verändert die Art, wie wir leben und arbeiten, jeden Tag, und eröffnet neue Möglichkeiten für Innovation.",
    "Die Alpen bieten wunderschöne Landschaften und beliebte Skigebiete, die im Winter Tausende von Touristen anziehen.",
]


def lang_detection_accuracy(samples, lang : str, nlp : NLP):
    start_time = time.time()

    n_words = 0
    n_phrases = 0
    n_correct_words = 0
    n_correct_phrases = 0
    for sample in samples:
        query = nlp.compose_query(sample[0])
        if len(sample[0].split()) == 1:
            n_words += 1
        else:
            n_phrases += 1
        if query.lang == sample[1]:
            if len(sample[0].split()) == 1:
                n_correct_words += 1
            else:
                n_correct_phrases += 1
    
    elapsed_time = time.time() - start_time

    # Compute accuracies
    global_accuracy = (n_correct_words + n_correct_phrases) / (n_words + n_phrases)
    words_accuracy = (n_correct_words / n_words) if n_words != 0 else None
    phrases_accuracy = (n_correct_phrases / n_phrases) if n_phrases != 0 else None
    print(f"Computed language detection accuracy on {lang}:")
    print(f"    - Words accuracy: {words_accuracy}")
    print(f"    - Phrases accuracy: {phrases_accuracy}")
    print(f"    - Global accuracy: {global_accuracy}")
    time_for_input = elapsed_time / len(samples_mix)
    print(f"Execution time: {elapsed_time} s")
    print(f"Average detection time for single input: {time_for_input * 100000} μs")
    print("")
    return n_words, n_phrases, n_correct_phrases, n_correct_words, elapsed_time

if __name__ == "__main__":
    start_time = time.time()
    nlp : NLP = NLP()
    print(f"NLP configured in: {time.time() - start_time} s")
    print("")

    if "--lang-detect" in sys.argv:
        print("TEST MODULE: Language detection accuracy:")
        print("")
        print("Language detection on PERIODS:")
        print("")
        lang_detection_accuracy(samples_EN, "ENGLISH", nlp)
        lang_detection_accuracy(samples_IT, "ITALIAN", nlp)
        lang_detection_accuracy(samples_ES, "SPANISH", nlp)
        lang_detection_accuracy(samples_DE, "DEUTUSCH", nlp)
        lang_detection_accuracy(samples_AR, "ARABIC", nlp)
        lang_detection_accuracy(samples_RU, "RUSSIAN", nlp)
        lang_detection_accuracy(samples_mix, "MULTIPLE LANGUAGE", nlp)
        print("Language detection on WORDS:")
        print("")
        lang_detection_accuracy(sample_words_DE, "DEUTUSCH", nlp)
        lang_detection_accuracy(sample_words_EN, "ENGLISH", nlp)
        lang_detection_accuracy(sample_words_IT, "ITALIAN", nlp)
        lang_detection_accuracy(sample_words_FR, "FRENCH", nlp)
        lang_detection_accuracy(sample_words_ES, "SPANISH", nlp)
    if "--wiki-search" in sys.argv:
        print("TEST MODULE: Ability to search on Wikipedia")
        print("")
        scraper = Scraper(debug=True)
        print("Testing WORDS:")
        print("")
        for word in sample_words_wikisearch_IT:
            scraper.search(nlp.compose_query(word))
        for word in sample_words_wikisearch_EN:
            scraper.search(nlp.compose_query(word))
        print("")
        print("Testing PERIODS:")
        print("")
        for period in samples_periods_wikisearch_IT:
            scraper.search(nlp.compose_query(period))
        for period in samples_periods_wikisearch_EN:
            scraper.search(nlp.compose_query(period))
        for period in samples_periods_wikisearch_DE:
            scraper.search(nlp.compose_query(period))
        for period in samples_periods_wikisearch_ES:
            scraper.search(nlp.compose_query(period))
        for period in samples_periods_wikisearch_FR:
            scraper.search(nlp.compose_query(period))
    if "--wiki-scrape" in sys.argv:
        print("TEST MODULE: Ability to scrape information from Wikipedia")
        print("")
        scraper = Scraper(debug=True)
        print("Testing WORDS:")
        print("")
        for word in sample_words_wikisearch_IT:
            scraper.scrape(nlp.compose_query(word))
        for word in sample_words_wikisearch_EN:
            scraper.scrape(nlp.compose_query(word))
        print("")
        print("Testing PERIODS:")
        print("")
        for period in samples_periods_wikisearch_IT:
            scraper.scrape(nlp.compose_query(period))
        for period in samples_periods_wikisearch_EN:
            scraper.scrape(nlp.compose_query(period))
        for period in samples_periods_wikisearch_DE:
            scraper.scrape(nlp.compose_query(period))
        for period in samples_periods_wikisearch_ES:
            scraper.scrape(nlp.compose_query(period))
        for period in samples_periods_wikisearch_FR:
            scraper.scrape(nlp.compose_query(period))