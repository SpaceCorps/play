<!-- wiki-i18n source: a195d763558df440 -->
<!-- wiki-i18n title: Demirhane -->
# Demirhane {#the-forge}

**Demirhane**, Montaj sayfasının (ve uçuştaki Montaj penceresinin) ikinci sekmesidir. Sahip olduğun ekipmanla iki şey yapar: kredi ve uzaylı ganimeti karşılığında **bir eşyayı bir kademe yükseltir** ve bir eşyanın **iki kopyasını**, ikisinin de en iyisini koruyan tek eşyada **birleştirir**. Beş özdeş eşya isteyen ve sonucu %25’lik bir şansa bırakan eski Füzyon Odası’nın yerini aldı.

## Neler dövülebilir {#what-can-be-forged}

Lazerler, lazer amfileri, kalkan çekirdekleri, kalkan hücreleri, motorlar, iticiler, Uyarlanabilir Çekirdekler, Repair Drone eşyaları ve [Gövde Kaplaması](/wiki/06-Items/Hull-Plating.md): [büyüleme bonusları](/wiki/06-Items/Overview.md) taşıyabilen her tek ekipman parçası. Envanterinde, bir gemide (orada kalır ve yeni kademesiyle hemen çalışır) ya da başka bir eşyaya takılı olabilir. Dronlar, gemiler, cephane, kaynaklar ve boosterlar dövülemez; Nakliye Deposu’ndaki ya da Skylab’ındaki Motor veya Savunma Modülü’ne takılı hiçbir şey de dövülemez: önce çıkar.

Ekipman listesinde, kademe ve tür filtrelerinin yanında bir **Tümü / Takılı / Envanterde** anahtarı vardır. **Takılı**, bir gemide ya da başka bir eşyaya takılı olanları, **Envanterde** boşta duranları gösterir; başlığın altındaki bir satır anahtarın kaç parçayı gizlediğini söyler. Bir birleştirmenin donörünü seçerken Takılı duraklatılır, çünkü donör boşta olmalıdır.

Tür filtresinin yanındaki **Gemi** açılır listesi yalnızca gemilerinden birindeki parçaları gösterir (başka bir eşyaya takılı parça, taşıyıcısının bulunduğu gemiye sayılır). “Envanterde” seçiliyken ve bir birleştirmenin donörünü seçerken duraklatılır. Parçanın üzerine gelince açılan kart, panelin başlığı ve birleştirmenin ana parçası nerede olduğunu söyler: *Kitefin gemisinde, konfigürasyon 1* (Hull Plating için iki konfigürasyon da) ve neye takılı olduğu. **Ctrl+F** (Mac’te Cmd+F) imleci Montaj’ın başlığındaki arama kutusuna koyar; açık sekmenin listesini daraltır (tarifler ürettiği ve istediği şeylere, ekipman ad, tür ve kademeye göre) ve Esc onu temizler. Panel, *Bonus yuvaları* satırının altında parçanın bir özelliği bonus taşımak için çok düşükse bunu söyler; Impulse Thruster’ın bir, Momentum Thruster’ın iki bonus taşımasının sebebi budur.

## Kademe yükselt {#tier-up}

Bir eşya seç; panel eşyanın kademesini, ulaşacağı kademeyi, bunun neyi değiştirdiğini (kaç bonus taşıyabileceği ve bonusların ne kadar büyük olduğu) ve fiyatı, her parçadan elinde ne kadar olduğuyla birlikte gösterir: yeterliyse yeşil, değilse kırmızı ve kaç eksiğin olduğu. Hepsi elindeyse **Kademe yükselt** eşyayı tam bir kademe yükseltir. Atlama yoktur: Ebedi kademeye ulaşmak için bir eşya Lekeli, İlahi ve Patlayan kademelerinden geçer, her birinin kendi fiyatı vardır.

| Adım | Başarı | Kredi | Thulium | Malzemeler |
| :--- | :---: | :---: | :---: | :--- |
| Standart → Lekeli | %100 | 10.000 | – | 5 Ship Fragment, 15 Daraxium |
| Lekeli → İlahi | %90 | 50.000 | – | 30 Ship Fragment, 45 Nyxite |
| İlahi → Patlayan | %75 | 200.000 | – | 20 Reinforced Hull Plate, 120 Cataclysite, 2 Dark Matter Plate |
| Patlayan → Ebedi | %60 | 500.000 | 2.000 | 8 Power Core, 240 Quorvium, 2 Dark Matter Plate |

- **Malzemeler** boştaki yığınlarından gelir: bir gemideki eşyalar ve Nakliye Deposu’ndaki yığınlar kullanılmaz. Eksik olanlar depodaysa panel bunu söyler.
- **Bir adım başarısız olabilir.** Eşya tıpatıp olduğu gibi kalır, krediler gider ve malzemelerin yarısı ile Thulium miktarının yarısı geri gelir (küsurat atılır; iki Dark Matter Plate varsa biri). Panel, basmadan önce şansı ve bunu söyler.
- **Başarılı olursa** eşyanın sahip olduğu her bonus yeni kademenin aralığında yeniden belirlenir ve daha iyi değeri korur. Hiç bonusu olmayan bir eşya her zaman ilkini alır; yeni kademenin açtığı her diğer yuva, **%50 şansla, her biri kendi zarıyla**, eşyanın diğer özelliklerinde dolar ve ıskalayan bir yuva sonraki kademe yükseltmede dolabilir (bkz. [Kademeye göre bonuslar](#buffs-by-tier)). Sonuç panelin üstünde gösterilir; eşya seçili kalır, böylece sonraki adımı zaten ekrandadır.
- Kademe yükseltme anlıktır.

### Dark Matter Plate {#dark-matter-plates}

Son iki adım, her şeyin üstüne her biri **2 Dark Matter Plate** ister. Bir plaka [Montaj](/wiki/06-Items/Overview.md)’da **5 Dark Matter, 1 Velkonite Reinforced Plate ve 1 Orvium Reinforced Plate** ile (250 Thulium, 2 dakika) preslenir; bu yüzden bir adım 10 Dark Matter, 2 Velkonite plakası ve 2 Orvium plakası ister. Dark Matter [kara delikten](/wiki/03-Mechanics/Black-Hole.md) gelir: yaklaşık beş N.I.K.E. roketi (bkz. [Roketler](/wiki/06-Items/Rockets.md)) on tane eder; yolunda bir gemiyle karşılaşan bir N.I.K.E. onun yerine o gemiye vurur ve hiç üretmez. Plakalar diğer malzemeler gibi boştaki yığınlarından kullanılır ve eksiğin varsa panel adlarını söyler. Her yükseltme zincirinin son kademesi de plaka ister, her biri için 3 ([Dark Matter ve Dark Matter plakaları](/wiki/03-Mechanics/Dark-Matter.md)).

### Kademeye göre bonuslar {#buffs-by-tier}

| Kademe | En fazla taşınan bonus | Her bonusun büyüklüğü |
| :--- | :---: | :---: |
| Lekeli | 1 | +%2 ile +%5 |
| İlahi | 2 | +%4 ile +%8 |
| Patlayan | 3 | +%6 ile +%11 |
| Ebedi | 4 | +%9 ile +%15 |

Demirhane’den önce üretilen ekipman, belirlendiği bonusları korur ve bunlar çoğu zaman tablodan küçüktür (o dönemden kalma İlahi bir parça +%2 taşıyabilir). Onları kendiliğinden hiçbir şey yükseltmez: bir kademe yükseltme her bonusu yeni kademenin aralığında yeniden belirler ve daha iyi değeri korur, bir birleştirme her özelliğin daha iyi değerini korur.

Bir eşya, özellik sayısından fazla bonus taşıyamaz: kalkan çekirdeği için dört, lazer için üç, motor ya da Uyarlanabilir Çekirdek için iki, Momentum Thruster için iki, Impulse Thruster için bir (1,017 ile 1,03 arasındaki çarpanı bir bonusa değmeyecek kadar küçüktür ve Demirhane 1,05 veya daha düşük bir çarpana bonus çıkarmaz; bu yüzden bonusu yalnızca sabit hızda olabilir), Crit Amp I, Repair Drone ya da Hull Plating için bir (gövdesi), daha yüksek kademeli Crit Amp eşyaları için iki, Damage Amp eşyaları ve kalkan hücreleri için üç. Sonraki kademe eşyanın taşıyabileceğinden fazla bonus taşımıyorsa panel bunu söyler: o zaman kademe yalnızca bonusları güçlendirir. Menzil bonusları +%5’i asla geçmez. Penetration Amp tek özellikli olduğundan tek bonus taşır.

**Bir kademe en fazla o kadar bonus taşır.** Bir kademe yükseltme eşyaya her zaman ilk bonusunu verir; yeni kademenin açtığı ve eşyanın bir özelliğinin bulunduğu her diğer yuva **%50 şansla, her biri kendi zarıyla** dolar ve ıskalayan bir yuva sonraki kademe yükseltmede yeniden denenir. Yani İlahi bir kalkan çekirdeğinin zamanın yarısında iki, diğer yarısında bir bonusu olur; Ebedi olanın zamanın yaklaşık üçte birinde dördü de olur (ortalamada 3,1 bonus), üç özellikli bir lazerin üçü de zamanın üçte ikisinde dolar ve bir motorun neredeyse her zaman ikisi de vardır. Panel, sonraki kademe için “en fazla” der ve yeni bir yuvanın ne sıklıkla dolduğunu söyler. Tek özellikli eşyalar ve Lekeli kademeye giden her adım bundan etkilenmez; bu kuraldan önce üretilmiş ekipman sahip olduğu bonusları korur. Bir **birleştirme**, bir kademe yükseltmenin ıskaladığı yuvayı doldurmanın yoludur: iki kopyanın her özelliğinin en iyi bonusunu, kademenin sınırına kadar korur. Şans yüzünden bir parça, sıradaki Soğurma bonusunu zamanın yalnızca bir kısmında taşır (Ebedi bir kalkan çekirdeği zamanın %78’inde, Ebedi bir kalkan hücresi %88’inde): oradaki rakamlar onu taşıyan parçalar içindir.

Bir **kalkanın Soğurma bonusu** (ve bir kalkan hücresinin Soğurma artışı) özelliği çarpar; bu yüzden [soğurmadan](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) ona orantılı puan değerindedir: bir Heavy Shield Core eşyasının %50’sinde +%5, +2,5 puandır ve en iyi setin her parçasında +%15 (bir Heavy Shield Core ve üç Absorption Shield Cell IV, toplam %80) +12 puandır. Ebedi bir set +7 ile +12 puan arası, ortalamada yaklaşık 10 puan kazandırır; Sezon Mağazası’nın Shield Absorbance Boost güçlendirmesiyle (sınırında +10 puan; tüm oyunun sıfırlama puanları 100 seviyesinin 44’ünü satın alır, +4,4 puan) bu bir gemiyi %95’e çıkarır ve %100’ün üstüne yalnızca bonusun sınırıyla ya da Pilot araştırması Field Theory ile (en fazla +5 puan) çıkar, ki özellik buna izin verir: saldıranın kalkan delmesi bundan düşülür. İlahi bir set 3 ile 6 puan arası kazandırır.

Motorlar, iticiler, Uyarlanabilir Çekirdekler ve Repair Drone eşyaları yüzdelik bir bonusla çok az değişir (bir Engine II 4 hız ekler, bu yüzden +%12 yarım puandır): özellikler için değil, kademeyi istiyorsan döv.

**Penetration Amp bonusu** delmesini çarpar: Ebedi bir bonus (+%9 ile +%15), bir Penetration Amp IV eşyasını yuva başına 12 yerine 13,1 ile 13,8 puan yapar. Bir vuruşun delmesini hiçbir şey sınırlamaz, bu yüzden her puan sayılır: en iyi lazerde (bir Fusion Core, bir Gemini ve her lazerde üç Penetration Amp IV) 10 + 15 + 36 toplamı %61 eder ve üç Ebedi bonus bunu %66,4’e kadar çıkarır ([Lazerler](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

### Malzemeler nereden düşer {#where-the-materials-drop}

| Malzeme | Düşüren |
| :--- | :--- |
| **Ship Fragment** | her uzaylı |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | hiçbir uzaylı düşürmez: Montaj onu Dark Matter ([kara delik](/wiki/03-Mechanics/Black-Hole.md)) ve Skylab’ın plakalarıyla preser |

Kristaller kademeleri izler: Daraxium Lekeli gibi mavi, Nyxite İlahi gibi sarı, Cataclysite Patlayan gibi turuncu ve Quorvium Ebedi gibi mor. Her kaynak, şansları ve miktarlarıyla birlikte [Kaynaklar](/wiki/06-Items/Resources.md) sayfasında ve her uzaylının sayfasındadır; Resource Magnet Booster bir kutunun içindekini %25 artırır. [Asteroitler](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds) parçalarında Dark Matter Plate dışında hepsini bırakır.

## Birleştirme {#merge}

Aynı eşyanın iki kopyası (iki Light Shield Core, iki Quantum Laser II) tek olur. **Birleştir**’e geç ve tutmak istediğin eşyaya (**temel**), sonra ikinci bir kopyaya (**donör**) tıkla. Panel, sen onaylamadan önce sonucu gösterir.

- **Temel korunur.** Yerini korur: bir gemide ya da başka bir eşyaya takılı olabilir ve içine takılı modüller kalır. **Donör harcanır.** Boşta olmalıdır (bir gemide değil, takılı değil) ve içine takılı modüller envanterine geri döner.
- **Sonuç iki kademenin yüksek olanını alır** ve her özellik için **iki değerin daha iyisini**.
- **Kademesinin izin verdiğinden fazla bonus taşımaz.** İki eşyanın bonusları birlikte sonucun kademesinin taşıyabileceğinden fazlaysa en iyileri korunur, gerisi elenir; tablo onları işaretler (üstü çizili, “sınırı aşıyor”). Daha fazla bonus taşımak için önce eşyanın kademesini yükselt. Bir birleştirme hiçbir şeyi rastgele belirlemez: önizlemenin gösterdiği, elde edeceğindir.
- **Bir birleştirme, ortaya çıkardığı kademeye göre kredi tutar**: Lekeli için 5.000, İlahi için 25.000, Patlayan için 100.000, Ebedi için 250.000. Malzeme yok.
- Hiçbir şeyi değiştirmeyecek bir birleştirme (sonuç temelden daha iyi değilse) reddedilir.
- Birleştirmeden sonra sonuç seçili kalır ve donör yuvası boştur: sonraki donörü koy ya da Kademe yükselt moduna geri dön.
- **Etiket**: birleştirilen parça, yalnızca temel ve donör ikisi de öyleyse **satılabilir** olur ([pazarda](/wiki/03-Mechanics/Auction.md#marketable-items) satışa çıkarılabilir). Önizleme bunu söyler.

Bir birleştirme bir eşyayı çoğaltmaz, ama bir kademe yükseltmenin ıskaladığı yuvaları doldurur: birleştirilmiş iki İlahi kalkan çekirdeği, ortalamada birinden yaklaşık üç buçuk puan fazla bonus eder. Kullanımı seçmektir: istediğin özelliklere sahip İlahi bir çekirdek ya da bir kademeyi, gemindeki eşyayı çıkarmadan ona taşımak.

## Montaj’da modül yükseltmeleri {#module-upgrades-in-the-assembly}

En üst üç lazer, lazer amfileri, II. ile IV. kademe kalkan hücreleri ve iticiler, II. ve III. kademe motorlar ve Uyarlanabilir Çekirdekler ile Heavy Shield Core satılmaz ve Montaj her birini yalnızca teknolojisini Skylab’da ([Araştırma](/wiki/03-Mechanics/Research.md)) araştırdıktan sonra üretir. Bunları Montaj’ın **Üretim** sekmesinde, bir adım aşağıdaki parçayı yükselterek üretirsin: Damage Amp III → **Damage Amp IV**, Crit Amp III → **Crit Amp IV**, Capacity Shield Cell I → **Capacity Shield Cell II** (III ve IV kademelerine kadar sürer; Absorption hücreleri, Impulse Thruster ve Momentum Thruster eşyaları da aynı şekilde yükselir), Basic Shield Core → **Heavy Shield Core**, Engine I → **Engine II** ve ardından **Engine III**, Adaptive Core I → **Adaptive Core II** ve ardından **Adaptive Core III**, Quantum Laser II → **Quantum Laser III**, Quantum Laser III → **Starfire-III** ve Starfire-III → **Helios Beam**. Demirhane’yi ilgilendiren kısım kademedir. Her amfi ailesinin ilk kademesi (Damage Amp I, Crit Amp I ve Penetration Amp I) Mağaza’da satılır; her ailenin II. ile IV. kademeleri bu şekilde üretilir.

- **Kademe kalır.** Bir yükseltme parçanın bir kopyasını harcar ve yeni eşya o kopyanın kademesini taşır: İlahi bir Damage Amp III harcanırsa İlahi bir Damage Amp IV olur, Standart olan Standart bir Damage Amp IV olur. Demirhane’ye ödediğin şey kaybolmaz. Yükseltme kendi başına kademe eklemez; bu yüzden Standart bir parça her zaman Standart bir sonuç verir.
- **Bonuslar korunur.** Yeni eşya, harcadığın parçanın bonuslarını korur: aynı özellikler aynı değerlerle, hiçbir şey yeniden belirlenmez (iki bonuslu İlahi bir Damage Amp III harcanırsa o iki bonusla İlahi bir Damage Amp IV olur, tek bonuslu olan o tek bonusla olur). Bir parçanın her özelliği, yükseltmesinin de özelliğidir; bu yüzden her bonus yerini bulur ve bir yükseltme Demirhane’nin ıskaladığı yuvaları doldurmaz, hiçbir bonusu da eksiltmez. Bonuslar işi kuyruğa aldığın anda sabitlenir ve topladığın şey sabitlenendir: toplamayı beklemek hiçbir şeyi değiştirmez; işi iptal edersen tıpatıp aynı parça, kademesi ve bonuslarıyla geri gelir. Bu kuraldan önce kuyruğa alınmış bir iş, belirlendiği bonusları korur. Pahalı olan, Demirhane’nin parçaya kattığıdır: Ebedi bir parça bir milyonun üzerinde kredilik Demirhane adımıdır ve yükseltme bunun hepsini korur.
- **Plakalar.** Thulium ve uzaylıların düşürdüklerinin yanında her modül yükseltmesi plaka ister. Son kademe **4 Dark Matter Plate** ve en az bir Ancient Control Unit ister: IV. kademe bir amfi, hücre ya da itici, Heavy Shield Core, Engine III, Adaptive Core III ve Helios Beam. Ondan önceki adımlar **Velkonite Reinforced Plate** ister: II. ya da III. kademe bir amfi için 2, II. ya da III. kademe bir hücre veya itici için 4, Quantum Laser III için 3, Engine II ya da Adaptive Core II için 4 ve Starfire-III için 8 (Helios Beam ayrıca 18 Orvium Reinforced Plate ister). Uzaylılar bunların hiçbirini düşürmez. [Skylab](/wiki/03-Mechanics/Skylab.md)’ındaki Dökümhane Velkonite ve Orvium plakalarını cevherden döker, Dökümhane 1. seviyedeyken plaka başına 40 Velkonite cevheri. 1. seviye bir Velkonite Toplayıcı saatte 10 cevher kazar; bu yüzden III. kademe bir amfinin plakaları 8 saatlik madencilik, III. kademe bir hücrenin ya da iticinin plakaları 16 saattir (5. seviye bir toplayıcıdan 4 ve 9 saat). Montaj, plakanın tarifini araştırdıktan sonra bir [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) preser: 5 Dark Matter, bir Velkonite Reinforced Plate, bir Orvium Reinforced Plate ve 250 Thulium ile. Her malzemenin nereden geldiği [Kaynaklar](/wiki/06-Items/Resources.md) sayfasındadır. Demirhane’nin kendi adımları ganimet ve kredi ister, en üst adımları ayrıca Dark Matter Plate ister (İlahi → Patlayan: 20 Reinforced Hull Plate ve 2 Dark Matter Plate; Patlayan → Ebedi: 2 Dark Matter Plate): bir modül yükseltmesinin son kademesiyle aynı plakalar.
- **Hangi kopya kullanılır.** Sen seçersin. Farklı kopyalar tuttuğunda (başka bir kademe ya da başka bonuslar), tarif kartı onları bir kutucuk sırası olarak gösterir: kullanılacak olana tıkla; kutucukların altındaki satır neye dönüşeceğini gösterir (“İlahi Damage Amp III”, sonra “Sonuç: İlahi Damage Amp IV”). Hiçbirini seçmezsen en sade olan gider: önce en düşük kademe, aynı kademedeki kopyalar arasında bonusları ne olursa olsun en eskisi. Daha sade bir kopya boştayken İlahi ya da daha iyi bir kopya asla kullanılmaz. Standart kademenin üstündeki bir kopyayı kullanmak önce sorar ve eşyanın adını söyler.
- **Hangi kopyalar kullanılabilir.** Boştakiler. Bir gemideki (bir yetenek yuvası da dahil), başka bir eşyaya takılı, Skylab’ındaki Motor ya da Savunma Modülü’ne takılı, kendi hücrelerini ya da iticilerini taşıyan ya da [Nakliye Deposu](/wiki/03-Mechanics/Cargo.md)’ndaki bir kopya kullanılamaz ve Montaj bunu söyler. Önce çıkar ya da depodan al. Birlikte başlatılan iki yükseltme aynı kopyayı kullanamaz.

- **Quantum Laser III de bir yükseltmedir.** Mağaza’nın lazeri olan bir **Quantum Laser II** kullanılarak yapılır (1.500 Thulium, 10 Ship Fragment ve 3 Velkonite Reinforced Plate ile: bkz. [Lazerler](/wiki/06-Items/Lasers.md)) ve yukarıdakilerin hepsi geçerlidir: İlahi bir Quantum Laser II harcanırsa aynı bonuslarla İlahi bir Quantum Laser III olur, kopyayı sen seçersin, kart Standart kademenin üstündekini kullanmadan önce sorar ve Quantum Laser II boşta olmalıdır: önce hangarda çıkar; çıkarana kadar Monte et düğmesi “Quantum Laser II parçanı çıkar” der. Kademe böylece yukarı doğru devam eder: İlahi bir Quantum Laser III harcanırsa İlahi bir Starfire-III olur.

- **Starfire-III de bir yükseltmedir.** Bir **Quantum Laser III** kullanılarak yapılır (1.500 Thulium, 100.000 kredi, ganimet ve 8 Velkonite Reinforced Plate ile: bkz. [Lazerler](/wiki/06-Items/Lasers.md)) ve yukarıdakilerin hepsi geçerlidir: İlahi bir Quantum Laser III harcanırsa aynı bonuslarla İlahi bir Starfire-III olur, kopyayı sen seçersin, kart Standart kademenin üstündekini kullanmadan önce sorar ve Quantum Laser III boşta olmalıdır: önce hangarda çıkar; çıkarana kadar Monte et düğmesi “Quantum Laser III parçanı çıkar” der. Kademe böylece yukarı doğru devam eder: İlahi bir Starfire-III harcanırsa İlahi bir Helios Beam olur.

- **Helios Beam de bir yükseltmedir.** Bir **Starfire-III** kullanılarak yapılır (2.000 Thulium, ganimet, 18 Orvium Reinforced Plate, 4 Dark Matter Plate ve bir Ancient Control Unit ile: bkz. [Lazerler](/wiki/06-Items/Lasers.md)) ve yukarıdakilerin hepsi geçerlidir: İlahi bir Starfire-III harcanırsa Starfire-III’ün bonuslarıyla İlahi bir Helios Beam olur, kopyayı sen seçersin, kart Standart kademenin üstündekini kullanmadan önce sorar ve Starfire-III boşta olmalıdır. Bir lazer bir gemiye takılıdır ve amfi taşır, bu yüzden çoğu zaman boşta değildir: önce hangarda çıkar (amfileri envanterine döner); çıkarana kadar Monte et düğmesi “Starfire-III parçanı çıkar” der.

Tarifler, maliyetleri ve kuralın arkasındaki sayılar [Eşyalara genel bakış](/wiki/06-Items/Overview.md#upgrading-modules) sayfasında; Quantum Laser III, Starfire-III ve Helios Beam için ise [Lazerler](/wiki/06-Items/Lasers.md) sayfasındadır.

## Eski sunucular {#old-servers}

Demirhane için güncellenmemiş bir oyun sunucusu, sekmenin yerinde “Demirhane bu sunucuda henüz yok” gösterir; Üretim eskisi gibi çalışır. Demirhane’den önceki bir oyun istemcisi, güncellenmiş bir sunucuda eski Füzyon sekmesini gösterir ve güncellemesi söylenir.
