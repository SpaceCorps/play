<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Zindanlar -->
# Zindanlar {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; zindan; zindanlar; geçit; geçitler; savaş lordu; labirent; aşama; ganimet bölgesi; kart -->

**Zindan**, oyunda **geçit** olarak adlandırılır: sonunda bir **Savaş Lordu** bulunan kapalı bir labirent. Bir [klanın](/wiki/03-Mechanics/Clans.md) yardımcı lideri ya da lideri bir geçit açar ve bedelini klan bankasından öder, klan üyeleri de tek bir [grup](/wiki/03-Mechanics/Groups.md) olarak birlikte içeri uçar. Labirentin uzaylılarının arasından yollarını açar, her birinden bir kart seçmek için ganimet bölgeleri açar ve Savaş Lordu'nu devirirler. Savaşa katılan her pilota, Savaş Lordu düştüğünde, aşağıdaki sınırlar içinde ödeme yapılır. Geçitler, klan sayfasındaki **Geçitler** sekmesindedir.

Geçit yalnızca uzaylılara karşı bir savaştır: içeride kimse bir klan arkadaşına ya da başka birine saldıramaz. Uzaylılar hiçbir şey ödemez. Ödeme yalnızca Savaş Lordu'ndan gelir, bu yüzden ödeme almanın tek yolu, o düşerken savaşın içinde olmaktır.

## Bir bakışta {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Açılış**: Sezonun 4. gününden itibaren
- **Geçidi kim açar**: Bedeli klan bankasından ödeyen bir yardımcı lider ya da lider
- **Grup**: Klanın 4 ila 10 üyesi, tek bir grupta
- **Günlük geçit sayısı**: Klan başına UTC gününde 3, aynı anda yalnızca biri açık
- **Aynı anda geçit**: Bir dünyada 6
- **Haritalar**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirentler**: 8; geçit açılırken biri seçilir
- **Toplanma**: Toplanıp başlamak için 10 dk. Kimsenin başlatmadığı bir geçit kapanır ve bedeli klan bankasına geri döner
- **Süre sınırı**: Başlangıçtan itibaren Aşama 1: 80 dk, Aşama 2: 110 dk, Aşama 3: 150 dk. Süre dolarsa geçit başarısız olur ve hiçbir şey ödemez
- **Boş bırakılırsa**: 3 dk boyunca içinde kimse olmayan bir geçit başarısız olur
- **Savaş Lordu düştükten sonra**: Geçit, içerideki pilotlar için 2 dk açık kalır
- **Geri dönüş**: Ayrılan ya da yok edilen bir pilot, aralarında 20 sn olacak şekilde 3 kez geri uçabilir

<!-- dungeons-glance:end -->

## Bir tur nasıl geçer {#how-a-run-goes}

1. **Çağır.** Geçitler sekmesinde bir [yardımcı lider ya da lider](/wiki/03-Mechanics/Clans.md#hierarchy-roles) bir aşama seçer ve **Çağır**'a basar. Bedel [klan bankasından](/wiki/03-Mechanics/Clans.md#clan-economy-taxation) çıkar ve geçit yukarıda sıralanan haritalardan birini alır. Kimsenin başlatmadığı bir geçit kapanır ve bedel bankaya geri döner.
2. **Gir.** Klan üyeleri uçarken Klan penceresinde **Gir**'e basar. İçerideki pilotlar geçidin grubudur.
3. **Başlat.** Geçidi açan pilot ya da bir subay, içeride yeterince pilot olduğunda **Başlat**'a basar. Bundan sonra yalnızca zaten içeride olan pilotlar geri dönebilir.
4. **Labirentten geç.** Labirente bir uçtan girersin, Savaş Lordu diğer uçta bekler. Uzaylılar odalarında uyur ve grup yaklaştıkça sürüler halinde uyanır.
5. **Ganimet bölgelerini aç.** Labirentteki halkalar bölgeleri işaretler. Birini elinde tut, grup bir kart için oy versin; kart, Savaş Lordu'nun ödemesiyle birlikte ödenir.
6. **Savaş Lordu'nu yen.** Kalkanını ve gövdesini kır, yeteneklerine karşılık ver. O düştüğünde geçit tamamlanır.
7. **Ödemeni al.** Ödeme, Savaş Lordu'nun düştüğü anda gelir. Geçit, içerideki pilotlar için biraz daha açık kalır, sonra kapanır.

## Girmek {#entering}

Bir geçide girmek için **uçuştaki bir gemiye** ihtiyacın var; önce kalk, sonra Klan penceresini aç; ayrıca içinde yeterince klan üyesi olan bir [grup](/wiki/03-Mechanics/Groups.md) gerekir. Aşamanın istediği **seviyeye** de sahip olmalısın ve başka bir geçidin içinde olmamalısın. Geçidin grubunun bir boyut sınırı vardır: dolduğunda kimse giremez.

Geçidi bir yardımcı lider ya da lider açar; klan için aynı anda yalnızca bir tane, günlük geçit sayısına kadar. Klan bankasında bedelin bulunması gerekir. Bir klan, bir aşamayı ancak ondan önceki aşamayı tamamladıktan sonra açabilir.

Bir geçidin içinde dünya değiştiremezsin ve Jump CPU ile Base CPU çalışmaz. Geçidin çubuğundaki **Ayrıl** düğmesi, onayladıktan sonra seni dışarı çıkarır. Ayrılan ya da yok edilen bir pilot, aralarda kısa bir beklemeyle birkaç kez geri uçabilir.

## Aşamalar {#the-stages}

Bir geçidin bir aşaması vardır ve aşama onun zorluğudur. Daha yüksek bir aşamada uzaylılar daha dayanıklıdır ve daha sert vurur, ödeme de daha yüksektir. Tablodaki çarpanlar her uzaylı için ve Savaş Lordu için geçerlidir. Hasar; lazerleri, roketleri ve Savaş Lordu'nun yeteneklerini kapsar. Tablo ayrıca bir aşamanın birinciye kıyasla kaç uzaylı gönderdiğini de gösterir. **Bedel**, geçit açılırken klan bankasından alınır.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aşama | Gereksinim | Uzaylıların gövdesi ve kalkanı | Uzaylı sayısı | Uzaylıların hasarı | Geçidin bedeli (kredi, klan bankasından) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Aşama 1** | 6. seviyeden itibaren | ×1 | ×1 | ×1 | 500.000 |
| **Aşama 2** | 7. seviyeden itibaren | ×1,5 | ×1 | ×1,25 | 1.000.000 |
| **Aşama 3** | 8. seviyeden itibaren | ×2,5 | ×1 | ×1,5 | 2.000.000 |

<!-- dungeons-stages:end -->

## Labirent {#the-maze}

Her geçit, kendi haritasında kapalı bir labirenttir; harita yukarıdaki listedeki haritalardan biridir, labirent ise birkaç yerleşimden biridir. Labirent, sağlam duvarlı odalar ve koridorlardan oluşan bir ızgaradır. Gemiler duvardan geçemez ve duvar atışları engeller, yani siper işi görür. Meteor yukarıdan düşer ve duvar onu durdurmaz.

## Uzaylılar {#the-aliens}

Labirenti dört tür uzaylı korur. Odalarında uyurlar ve bir pilot yaklaşınca uyanırlar. Geçit, havada aynı anda yalnızca belirli sayıda uzaylı tutar ve bu sayı grubun büyüklüğüyle artar; böylece yok ettiğin bir sürü, sıradakini içeri alır. Daha büyük bir grup orantılı olarak daha çok uzaylıyla karşılaşır, daha küçük bir grup daha azıyla; bir uzaylı türü de asla birin altına düşmez.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Uzaylılar, 5 kişilik bir grup için | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Toplam | 195 | 195 | 195 |
| Bir ganimet bölgesinin dalgası | 10 × Gate Goombah ve 1 × Gate Crystalys | 10 × Gate Goombah ve 1 × Gate Crystalys | 10 × Gate Goombah ve 1 × Gate Crystalys |

- **Aynı anda canlı**: Grubun her pilotu için en çok 10, toplamda 70

<!-- dungeons-population:end -->

Her tür sırayla. Gövde ve kalkan, olağan değerlerin sütundaki aşamanın çarpanıyla çarpımıdır.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Görünüşü**: Goombah
- **Sürü büyüklüğü**: 6

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 32.000 | 48.000 | 80.000 |
| Kalkan | 48.000 | 72.000 | 120.000 |
| Lazer hasarı (saniyede bir salvo) | 3.000 | 3.750 | 4.500 |
| Hız | 180 | 180 | 180 |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | 1.800 | 1.800 | 1.800 |

### Gate Pirate

- **Görünüşü**: Pirate Boss
- **Sürü büyüklüğü**: 2
- **Roket**: Her 5 sn bir düz roket, menzil 970 birim

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 300.000 | 450.000 | 750.000 |
| Kalkan | 50.100 | 75.150 | 125.250 |
| Lazer hasarı (saniyede bir salvo) | 200 | 250 | 300 |
| Roket hasarı | 5.000 | 6.250 | 7.500 |
| Hız | 92 | 92 | 92 |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | 1.800 | 1.800 | 1.800 |

### Gate Crystalys

- **Görünüşü**: Crystalys
- **Sürü büyüklüğü**: 2

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 256.000 | 384.000 | 640.000 |
| Kalkan | 160.000 | 240.000 | 400.000 |
| Lazer hasarı (saniyede bir salvo) | 10.000 | 12.500 | 15.000 |
| Hız | 230 | 230 | 230 |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | 2.400 | 2.400 | 2.400 |

### Gate Crystalys Twin

- **Görünüşü**: Crystalys, 1,4 kat büyük
- **Sürü büyüklüğü**: 1

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 512.000 | 768.000 | 1.280.000 |
| Kalkan | 320.000 | 480.000 | 800.000 |
| Lazer hasarı (saniyede bir salvo) | 20.000 | 25.000 | 30.000 |
| Hız | 230 | 230 | 230 |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## Savaş Lordu {#the-warlord}

Savaş Lordu labirentin uzak ucundaki odada bekler ve bir geçitte ödeme yapan tek şey odur. Dev boyuta ulaşmış bir Crystalys'tir. Gövdesi ve kalkanı grubun büyüklüğüyle artar: ne kadar çok pilot girerse o kadar dayanıklı olur, orantılı olarak. Odasında kalır ve yeteneklerini rastgele sırayla, teker teker kullanır; her birinin kendi bekleme süresi vardır.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Görünüşü**: Crystalys, 3 kat büyük
- **Kalkan dolumu**: Saniyede 3.000, 15 sn hasarsız kaldıktan sonra

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 10.000.000 | 15.000.000 | 25.000.000 |
| Kalkan | 8.000.000 | 12.000.000 | 20.000.000 |
| Lazer hasarı (saniyede bir salvo) | 8.000 | 10.000 | 12.000 |
| Hız | 120 | 120 | 120 |
| Lazer menzili | 1.100 | 1.100 | 1.100 |

Yukarıdaki gövde ve kalkan 5 kişilik bir grup içindir. Grupla birlikte büyürler: bunlar, geçit başladığında gruptaki pilot sayısına göre Savaş Lordu'nun gövdesi ve kalkanının toplamıdır.

| Gruptaki pilotlar | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14.400.000 | 21.600.000 | 36.000.000 |
| 5 | 18.000.000 | 27.000.000 | 45.000.000 |
| 6 | 21.600.000 | 32.400.000 | 54.000.000 |
| 7 | 25.200.000 | 37.800.000 | 63.000.000 |
| 8 | 28.800.000 | 43.200.000 | 72.000.000 |
| 9 | 32.400.000 | 48.600.000 | 81.000.000 |
| 10 | 36.000.000 | 54.000.000 | 90.000.000 |

<!-- dungeons-boss:end -->

### Yetenekleri {#its-abilities}

- Can çalma aurasının **kırmızı halkası**, içindeki her pilota zarar verir ve bu hasarla Savaş Lordu'nu iyileştirir. Kalkan emiliminin de kırmızı bir halkası vardır: içindeki pilotların kalkanını boşaltır ve Savaş Lordu'nunkini doldurur. İkisinde de halkadan çık ya da bir duvarın arkasına geç.
- Meteor yağmurunun **kehribar halkaları**, meteorların bir an sonra nereye düşeceğini gösterir. Hareket etmeye devam et ve düşmeden önce halkadan çık.
- **İyileştiricilere odaklanma**, Savaş Lordu'nu başka bir pilotu iyileştirenin üzerine çevirir ve o pilota daha sert vurur. İyileştirmeyi dağıt.
- **Roket yağmuru**, rastgele pilotlara güdümlü roketler gönderir. Bir EMP Charge ya da gizlenme onları atlatır.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Yetenek | Hazırlık | Süre | Bekleme süresi | Halka yarıçapı (birim) | Savaş Lordu'nun geri kazandığı en çok |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Can çalma aurası** | 2 sn | 15 sn | 2 dk | 900 | Gövde ve kalkan: %8 |
| **Meteor yağmuru** | 1,5 sn | 3 salvo, aralarında 4 sn | 2 dk | 420 | – |
| **İyileştiricilere odaklanma** | 1 sn | 45 sn | 2 dk | – | – |
| **Roket yağmuru** | 1,5 sn | 45 sn | 2 dk | – | – |
| **Kalkan emilimi** | 2 sn | 15 sn | 2 dk | 900 | Kalkan: %6 |

| Yetenek | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | :--- | :--- | :--- |
| **Can çalma aurası** | Saniyede 8.000 | Saniyede 10.000 | Saniyede 12.000 |
| **Meteor yağmuru** | Salvo başına 6 meteor, her biri 40.000 | Salvo başına 8 meteor, her biri 50.000 | Salvo başına 10 meteor, her biri 60.000 |
| **İyileştiricilere odaklanma** | Lazeri, döndüğü pilota ×1,5 daha sert vurur | Lazeri, döndüğü pilota ×1,5 daha sert vurur | Lazeri, döndüğü pilota ×1,5 daha sert vurur |
| **Roket yağmuru** | Roket başına 6.500, her 15 sn bir roket | Roket başına 8.125, her 15 sn bir roket | Roket başına 9.750, her 15 sn bir roket |
| **Kalkan emilimi** | Saniyede 10.000 kalkan | Saniyede 12.500 kalkan | Saniyede 15.000 kalkan |

<!-- dungeons-abilities:end -->

## Ganimet bölgeleri {#loot-zones}

Grup bulduğunda, labirentin zeminindeki bir halka her ganimet bölgesini işaretler. İçinde kısa bir süre dur; bölge uyanır ve bir uzaylı dalgası ona doğru gelir. Sonra grubun bölgeyi **tutması** gerekir: çubuk dolana kadar içeride bir pilot bulundurmak. Halkadaki uzaylılar çubuğu durdurur, içeride kimse yokken de çubuk geri gider; bu yüzden önce dalgayı temizle. Bölge açıldığında grup üç farklı kart görür ve birine **oy verir**. Bir bölge yalnızca bir kez açılır ve dalgası bir daha gelmez.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ganimet bölgeleri**: Her labirentte 4
- **Yarıçap**: 450 birim
- **Uyanma**: Halkanın içinde 2 sn dur
- **Tutma**: İçeride 30 sn boyunca bir pilot tut. Halkada 3 veya daha fazla uzaylı varken çubuk durur, içeride kimse yokken geri gider
- **Seçim**: Grubun oy vermek için 45 sn süresi var. Oy verme, orada bulunan her pilot oy verdiğinde ya da bir kart oyların yarısından fazlasını aldığında daha erken biter

<!-- dungeons-zones:end -->

### Kartlar {#the-cards}

Kartlar, aşağıdaki havuzdan teker teker çekilir. Şans, bir kartın tek bir çekilişteki şansıdır. Çok kopyalı bir kart ödeme alan her pilota, tek kopyalı bir ekipman kartı ise grubun bir pilotuna gider. Ödeme almayan bir pilot kart da almaz ve başarısız olan bir geçitte açılan bölge hiçbir şey ödemez.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Kart | Aşama 1 | Aşama 2 | Aşama 3 | Şans | Kime gider |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | %21 | Ödeme alan her pilot |
| Velkonite Reinforced Plate | 10 | 15 | 25 | %12 | Ödeme alan her pilot |
| Orvium Reinforced Plate | 10 | 15 | 25 | %12 | Ödeme alan her pilot |
| Velkonite | 200 | 300 | 500 | %12 | Ödeme alan her pilot |
| Orvium | 200 | 300 | 500 | %12 | Ödeme alan her pilot |
| Ultra Core | 5.000 | 7.500 | 12.500 | %10 | Ödeme alan her pilot |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | %8 | Ödeme alan her pilot |
| Dark Matter | 5 | 8 | 12 | %8 | Ödeme alan her pilot |
| Dark Matter Plate | 1 | 1 | 2 | %4 | Ödeme alan her pilot |
| Engine III | 1 | 1 | 1 | %0,25 | Grubun bir pilotu |
| Heavy Shield Core | 1 | 1 | 1 | %0,25 | Grubun bir pilotu |
| Adaptive Core III | 1 | 1 | 1 | %0,25 | Grubun bir pilotu |
| Starfire-III | 1 | 1 | 1 | %0,25 | Grubun bir pilotu |

- **Ekipman**: Tek kopyalı kartlar ekipmandır: birlikte kartların %1 kadarı

<!-- dungeons-cards:end -->

## Ödeme {#pay}

Savaş Lordu düştüğünde, hak eden her pilota tamamlanan tur için bir kez ödeme yapılır. Grubun seçtiği kartlar, aşamanın ödemesinin üstüne gelir. Dünya çarpanı yoktur: ödeme her dünyada aynıdır.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aşama | Onur | Deneyim | Kredi | Thulium | x4 cephane | PvE sıralama puanı |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Aşama 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 600 |
| **Aşama 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 1.500 |
| **Aşama 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 2.400 |

<!-- dungeons-pay:end -->

### Kime ödeme yapılır {#who-is-paid}

Uzaylılar asla ödeme yapmaz. Bir tur, hiçbir şey ödemese bile sonuna kadar oynanır ve sonuç ekranı nedenini söyler. Bir aşama için zaten ödeme aldığın için giriş asla reddedilmez: o tur yalnızca hiçbir şey ödemez.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Bir gün**: Bir aşama, bir pilota UTC gününde bir kez öder: Savaş Lordu'nun düştüğü gün
- **Bir hafta**: Bir pilot, UTC haftasında (Pazartesi–Pazar) en çok 10 aşama tamamlama için ödeme alır
- **İçeride**: Toplamda en az 2 dk
- **Savaşa katkı**: Şunlardan en az biri: Savaş Lordu'nun gövdesine ve kalkanına toplam %2 oranında hasar verdi; geçidin 10 uzaylısını yok etti; Savaş Lordu'yla savaş sırasında diğer pilotları 50.000 iyileştirdi

<!-- dungeons-rules:end -->

### Bir günün ve bir haftanın değeri {#what-a-day-and-a-week-are-worth}

Bir pilotun bir günde ve sınırların izin verdiği en iyi haftada alabileceği ödeme. Son sütun, ödemenin [PvE puanlarına](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) ne kattığını gösterir.

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Her pilota ödeme | Onur | Deneyim | Kredi | Thulium | x4 cephane | PvE sıralama puanı |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Bir gün, her aşama bir kez | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 4.500 |
| En iyi hafta: 7 × Aşama 3 ve 3 × Aşama 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 21.300 |

Ödemesi yapılan bir tamamlamanın deneyimi PvE sıralama puanlarınıza sayılır: her 1.000 deneyim için bir puan.

<!-- dungeons-totals:end -->

## Klan bankasının ödülü {#clan-bank-reward}

Klan bir sezonda bir aşamayı ilk kez tamamladığında klan bankasına da ödeme yapılır; Thulium olarak değil, kredi olarak. Klanın yeterince eski olması ve o turun yeterince pilotuna ödeme yapılması gerekir. Banka, bir sezonda her aşama için bir kez ödeme alır.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aşama | Klan bankası için kredi |
| :--- | ---: |
| **Aşama 1** | 10.000.000 |
| **Aşama 2** | 20.000.000 |
| **Aşama 3** | 30.000.000 |

- **Klanın yaşı**: En az 3 gün
- **Ödeme alan pilotlar**: Geçitte en az 3

<!-- dungeons-clan:end -->

## İpuçları {#tips}

- Bir bölgeyi tutmaya çalışmadan önce dalgasını temizle ve uzaylılar içeri girerse halkanın içinde savaş.
- Duvarları kullan: lazerler onlardan geçmez ve Savaş Lordu'nun halkaları onlarda durur.
- Roket yağmuru için bir EMP Charge sakla.
- Geçidin çubuğundaki saate bak. Süre dolduğunda geçit başarısız olur ve hiçbir şey ödemez.
