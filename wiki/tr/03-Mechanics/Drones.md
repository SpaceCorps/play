<!-- wiki-i18n source: ecb97ce5ddf9142a -->
<!-- wiki-i18n title: Dronlar -->
# Dron mekaniği {#drone-mechanics}

Dronlar, geminin yanında uçan otonom destek birimleridir. Ek ekipman yuvaları sağlar ve geminin savaş performansına doğrudan katkıda bulunurlar. Bir Slave Drone ayrıca gelişir: bir uzaylıyı her yok edişinde deneyim kazanır ve küçük, zırhlı bir küreden hilal kanatlı bir saldırı gemisine uzanan **sekiz seviyeden** geçer. Montaj’da bir Slave Drone, seviyeleri yeniden başlayan bir **Master Drone** hâline getirilebilir (aşağıdaki Master Drone bölümüne bak). Dronlar ayrıca bir **dron formasyonu** kuşanmanı sağlar: yalnızca sahip olduğun dronlar arasında en az bir tane varsa çalışır (bkz. [Dron formasyonları](/wiki/03-Mechanics/Formations.md)).

![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)

## Dron edinmek {#getting-drones}

Elindeki her dron (bir **Slave Drone** ya da bir Master Drone), kendi dron yuvalarını açar (Slave Drone için bir, Master Drone için iki), en fazla **8** dron. Mağaza kredi karşılığı Slave Drone satar; dördüncüden itibaren Thulium karşılığı da satar. Her biri bir öncekinden pahalıdır: fiyatlar [Dronlar](/wiki/06-Items/Drones.md) sayfasındadır.

## Uçuş düzeni ve hareket {#formation-movement}

Hiçbir [dron formasyonu](/wiki/03-Mechanics/Formations.md) kuşanılmadığında dronların standart **“Wingman” düzeninde (2-2-4)** uçar; bu **Standart** düzendir:

- Geminin yanında **2 dron**, her kanatta bir tane.
- Geminin yanında ve hemen gerisinde **2 dron**.
- Arkada iz süren **4 dron**.

Dronlar, konumlarını geminin hızına ve dönüşüne göre ayarlayan, keskin manevralarda düzeni sıkılaştıran yumuşak bir takip algoritması kullanır. Bu düzende hiçbiri önünde uçmaz.

Dronlar küçüktür ve yakında kalır: 8. seviye bir dron yaklaşık 19,5 birim genişliğindedir (bir Protos 50), 1. seviye bir dron ise yaklaşık 8 birimlik bir toptur; bu yüzden düzenin tamamı geminin her iki yanında ve arkasında yaklaşık 135 birim içine sığar. İlk aldığın dron en çok deneyime sahiptir ve bu düzende sol kanatta uçar, ikincisi sağda, en yenileri arkada iz sürer.

Bir [dron formasyonu](/wiki/03-Mechanics/Formations.md) kuşan, dronlar bu düzeni bırakır: **16 formasyonun her birinin kendi şekli vardır**: kanatların üstünde bir çatı, bir elmas, bir kalp, kanatlar, bir kılıç, bir matkap ve daha fazlası; dronlar saniyeden kısa sürede o şekle süzülür. Şekil, sahip olduğun dronlara göre yapılır (en fazla 8) ve geminle birlikte döner. Diğer pilotlar da onu görür. [Nasıl uçarlar](/wiki/03-Mechanics/Formations.md#how-they-fly) on altısının hepsini gösterir. **Standart** (kısayol çubuğunun Formasyonlar listesindeki, formasyon olmayan girdi) seçildiğinde dronlar yeniden Wingman düzeninde uçar.

Dronları Ayarlar › Arayüz bölümünde kapatabilirsin: kendi dronların için **Dronlarımı göster**, diğer pilotların dronları için **Düşman dronlarını göster**. Dronlar bir **kaplama** da giyer: onu hangarın Dronlar görünümünde seçersin ve **Diğer pilotların görünümlerini göster** ayarı, diğer pilotların dronlarının kaplamalarını görüp görmeyeceğini belirler ([Kozmetikler](/wiki/06-Items/Cosmetics.md#drone-liveries)).

## Ekipman ve özellikler {#equipment-stats}

Dronlar, gemin için genişleyen ekipman rafları gibi çalışır.

- Slave Drone **1 yuva**, Master Drone **2 yuva** sağlar; en fazla **8 dron**.
- Bu yuvalara **lazer** ve **kalkan** takabilirsin; iki yuvası olan Master Drone için her ikisine de. Başka hiçbir şey sığmaz: motor yok, Uyarlanabilir Çekirdek yok.
- **Lazerler tam sayılır.** Bir drondaki lazer, sen ateş ettiğinde ateş eder, hasarını salvona ekler ve diğer her lazer gibi cephane harcar (her lazer salvo başına bir birim cephane yakar). Master Drone üzerindeki iki lazer, iki lazer sayılır.
- **Kalkanlar da tam sayılır.** Bir drondaki kalkan, her iki yuvada da, çekirdek yuvasındaki bir kalkan gibi sayılır: hücreleriyle birlikte kapasitesi ve dolumu, geminin ortalamasındaki soğurması, kalkan bonusu ve hız cezası. Geminin kendi kalkanlarıyla birlikte, yuvanın payından sonra neyin saydığına göre sıralanır (bir dron yuvası %100 sayılır; en iyi dördü tam, beşinci ve sonrakiler daha az sayılır, bkz. [Kalkan mekaniği](/wiki/03-Mechanics/Shields.md)) ve Demirhane bonusları, Sezon Mağazası güçlendirmeleri ve saldıranın kalkan delmesi ona her kalkanda olduğu gibi işler. Dronun seviyesi yalnızca lazerini yükseltir, kalkanını asla. Bir dron yükseltilirken yuvaları çevrimdışıdır: kalkan da lazer de. 0.4.7’den önce bir drondaki kalkan hiçbir şey eklemezdi.
- **Lazer mi, kalkan mı?** Bir yuva birini ya da ötekini alır: lazer salvona bir lazer ekler, kalkan ise kalkan puanlarını ekler. İyi kalkanlı küçük bir gemide ek puanlar çok az şey katar, çünkü önce gövde biter; büyük bir gövdede ise çok daha fazlasına dayanmanı sağlar.
- **Formasyonlar bir dron ister, bir yuva değil.** Bir [dron formasyonu](/wiki/03-Mechanics/Formations.md), en az bir dronun olduğu sürece çalışır. Dron yuvası kullanmaz; dron sayısı, seviyeleri ve taşıdıkları onu değiştirmez.

## Seviyeler {#levels}

Her Slave Drone 1. seviyede başlar ve bir uzaylıyı yok ettiğin her seferde deneyim (XP) kazanır. Bir Master Drone da 1. seviyede, hiç XP’si olmadan başlar ve aynı şekilde seviye atlar. Her seviye bir öncekinden fazlasını ister ve görünüm de onunla değişir; böylece bir dronun ne kadar ilerlediğini görebilirsin. Tablo, her seviye için bir önceki seviyeden oraya çıkmak için gereken XP’yi ve bunun yalnızca tek bir uzaylı türünü öldürerek kaç öldürmeye denk geldiğini verir (Alpha dünyasında: Beta yaklaşık yarısını, Gamma yaklaşık üçte birini ister):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **1. seviye, Tohum:** tek bir camgöbeği merceği olan küçük, zırhlı bir küre.
- **2. seviye, Hale:** süzülen bir halkanın içindeki küre.
- **3. seviye, Disk:** cam bir kubbenin altında düz bir disk.
- **4. seviye, Uçan daire:** zırh plakaları ve hava girişleri olan bir uçan daire.
- **5. seviye, Saldırı gemisi:** uçan daireye bir pruva ve iki top eklenir.
- **6. seviye, Kanat tomurcukları:** pilonlar üzerinde toplar ve kısa kanat bıçakları.
- **7. seviye, Yarım kanatlar:** altın uçlu daha uzun kanat bıçakları.
- **8. seviye, Hilal:** tamamlanmış saldırı gemisi: camgöbeği ışık şeritli tam hilal kanatlar.

| Seviye | Ulaşmak için XP | Seviye için XP | Lazer hasarı | Seeker öldürme sayısı | Bulwark öldürme sayısı | Goombah öldürme sayısı |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +%1 | 550 | 69 | 23 |
| 4 | 2.000 | 1.100 | +%2 | 1.100 | 138 | 46 |
| 5 | 3.700 | 1.700 | +%3 | 1.700 | 213 | 71 |
| 6 | 6.000 | 2.300 | +%4 | 2.300 | 288 | 96 |
| 7 | 9.500 | 3.500 | +%5 | 3.500 | 438 | 146 |
| 8 | 14.000 | 4.500 | +%7 | 4.500 | 563 | 188 |

| Uzaylı | Dron başına XP |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Dronlar XP’yi nasıl kazanır {#how-drones-earn-xp}

- **Sahip olduğun her dron aynı XP’yi kazanır**: ödemesini aldığın her uzaylı öldürmesi için, ilk 8 dron, lazer taşısın taşımasın. Sonradan aldığın bir dron 1. seviyede, hiç XP’si olmadan başlar; bu yüzden ilk dronların her zaman en yüksek seviyedir.
- **Daha güçlü uzaylılar daha çok değer.** Bir uzaylının verdiği XP yukarıdaki ikinci tablodadır (bir Crystalys 72 Seeker değerindedir). Listede olmayan her uzaylı 1 verir.
- **Dünyalar daha çok öder.** Beta XP’yi ikiye katlar, Gamma üçe katlar (oradaki uzaylıların gövdesi de daha fazladır). Boosterlar ve Premium bunu değiştirmez.
- **Öldürmeler, sana ödeme yaptığında sayılır.** Başka bir pilot sahiplenmeyi elinde tutarken bitirdiğin bir uzaylı, sana hiçbir şey ödemediği gibi dronlarına da hiçbir şey ödemez. Oyuncu öldürmeleri, görevler ve şirket pilotlarının kendi öldürmeleri dron XP’si vermez.
- **8. seviye son seviyedir.** XP ondan sonra da sayılmaya devam eder.

### Bir seviyenin verdiği {#what-a-level-gives}

Bir **dronun yuvasına takılı lazer**, dronu seviye atladıkça daha çok temel hasar verir: 1. ve 2. seviyede hiçbir şey, sonra 3. seviyede +%1’den **8. seviyede +%7’ye** kadar. Bonus, o lazerin kendi hasarını çarpar (büyülemesinden sonra); içine takılan amfiler üstüne eklenir ve çarpılmaz. Hangar her dronun seviyesini, XP çubuğunu ve bir sonraki seviyenin istediği öldürmeleri gösterir; hasar rakamları bonusu zaten içerir. Bir dron seviye atladığında Oyun Günlüğü bunu söyler (“2. dron 4. seviyeye ulaştı.”) ve dron bir ışık halkasıyla parlar.

### Ne kadar sürer {#how-long-it-takes}

Eğri öyle ayarlanmıştır ki yeni bir dron normal oyunda (Bulwark ve Goombah avlayarak) yaklaşık bir saatte 2. seviyeye, yaklaşık 27 saatlik oyunda 8. seviyeye ulaşır. Bu saatler, ilk dronu yaklaşık 7. seviye görevlerinde alan bir pilot içindir; daha zayıf ekipmanla daha uzun sürer (2. seviye için yaklaşık 4 saate, 8. seviye için 150 saate kadar). Tek bir uzaylı türünü tek başına avlamak, normal bir karışıma göre en iyi ihtimalle yaklaşık bir buçuk kat hızlıdır. Dronlar seviyeleri ve deneyimleriyle sezon sıfırlamasından kalır; bu yüzden o saatler bir kez, gerektiği kadar sezon boyunca harcanır: günde yarım saat oynayan bir pilot oraya birkaç sezonda ulaşır.

### Master Drone

Master Drone teknolojisi araştırıldıktan sonra ([Araştırma](/wiki/03-Mechanics/Research.md)), Montaj’da yükselttiğin bir Slave Drone **Master Drone** hâline gelir. Tarif 1.000.000 kredi, 50.000 Thulium, 250 Ship Fragment, 10 Dark Matter plakası, 5 Orvium Reinforced Plate, 5 Velkonite Reinforced Plate ve 2 Ancient Control Unit tutar, 60 saniye sürer ve bir dronu tüketmez: **hangi Slave Drone olacağını sen seçersin** (seçici her birinin seviyesini ve XP’sini gösterir) ve aynı dron, numarası, dron yuvası ve içine takılı her şeyle, iş bittiğinde boş bir ikinci yuvayla birlikte Master Drone hâline gelir. Envanterine hiçbir şey girmez ve toplanacak bir şey yoktur: bittiğinde Oyun Günlüğü bunu söyler; sen yokken biten bir yükseltme için de.

**Seviyesi ve XP’si, yükseltme bittiğinde 0’a sıfırlanır.** Bir Master Drone yeniden 1. seviyeden, hiç XP’si olmadan başlar ve bir Slave Drone gibi seviye atlar (yukarıdaki tablo); sahip olduğu seviyenin lazer bonusu da onunla gider. Montaj bunu sen başlamadan önce söyler ve dronun XP’si varsa, dronun adını vererek onay ister. Varsayılan seçim en az XP’si olan drondur.

Yükseltme sürerken dron kilitlidir: onu yeniden yükseltemez ya da silemezsin ve yuvası **çevrimdışıdır**, bu yüzden içindeki lazer iş bitene kadar ateş etmez (o zamana kadar hâlâ tek yuvalı bir Slave Drone olarak sayılır). Her üretim gibi, diğer işlerinin arkasında kuyruğa girer.

Bir Master Drone, 8 dronundan biridir: dron sınırına ve bir sonraki Slave Drone fiyatına sayılır, bu yüzden yükseltme ikisini de değiştirmez; seviyesi ve XP’siyle sezon sıfırlamasından kalır. Uçuşta altın renkli, tamamlanmış saldırı gemisidir. **İki ekipman yuvası** olması, Master Drone ile Slave Drone arasındaki farktır: Slave Drone bir yuva taşır; her yuva bir lazer ya da kalkan alır ve seviye bonusu ikisindeki lazere de uygulanır. Bunun dışında bir Slave Drone gibidir: aynı sekiz seviye ve aynı lazer bonusu. İkinci yuva eklenmeden önce yapmış olduğun Master Drone eşyaları artık ona sahiptir; taşıdıkları şey eski yerinde durur. Yerinde yükseltme olmadan önce üretilen Master Drone eşyaları envanterindeki sıradan eşyalardır ve uçmaz.

## Savaş davranışı {#combat-behavior}

- **Lazerler**: Dronlar, takılı lazerlerini kilitlendiğin hedefe ateşler.
- **Hasar**: Dronlar hasar alabilir (ayrı bir varlık mantığı varsa; şu an çoğunlukla geminin havuzunu paylaşır ama görsel olarak ayrıdır). _Not: Şu an dronlar geminin yok edilemez uzantılarıdır._
- **Repair Drone**: Repair Drone eşyaları (I–IV) filonun dronları değil, [ekstralardır](/wiki/06-Items/Extras.md#repair-drones). Biri gövdeni onarırken gemiden küçük onarım dronları çıkar, geminin çevresinde döner ve ona ışın tutar; yakınındaki pilotlar onları görür.
