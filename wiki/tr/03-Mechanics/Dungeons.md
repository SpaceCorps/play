<!-- wiki-i18n source: fe0e51ce5e04b430 -->
<!-- wiki-i18n title: Zindanlar -->
# Zindanlar {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; zindan; zindanlar; zindan; zindanlar; savaş lordu; labirent; aşama; ganimet bölgesi; kart; portal; klan portalı; booster; sis; muhafızlar; başlangıç odası; kilitli oda; sürü desteği; kaos bölgesi; klan zindanı uyarıları; klan zindanı; klan zindanı uyarıları; dörtte üç; yüzde 75 -->

**Zindan**, sonunda bir **Savaş Lordu** bulunan kapalı bir labirenttir (0.5.2'den önce oyunda geçit olarak adlandırılırdı). Bir [klanın](/wiki/03-Mechanics/Clans.md) yardımcı lideri ya da lideri bir zindan açar ve bedelini klan bankasından öder, klan üyeleri de tek bir [grup](/wiki/03-Mechanics/Groups.md) olarak birlikte içeri uçar. Labirentin uzaylılarının arasından yollarını açar, her birinden bir kart seçmek için ganimet bölgeleri açar ve Savaş Lordu'nu devirirler. Savaşa katılan her pilota, Savaş Lordu düştüğünde, aşağıdaki sınırlar içinde ödeme yapılır. Zindanlar, klan sayfasındaki **Zindanlar** sekmesindedir.

Zindan yalnızca uzaylılara karşı bir savaştır: içeride kimse bir klan arkadaşına ya da başka birine saldıramaz. Uzaylılar, örnek alındıkları oyundaki uzaylılar gibi, düştüklerinde ödeme yapar ([uzaylıların ödemesi](#what-the-aliens-pay)). Tamamlamanın ödemesi Savaş Lordu'na aittir, bu yüzden onu almanın tek yolu, o düşerken savaşın içinde olmaktır.

Zindan, bir [solo geçit](/wiki/03-Mechanics/Solo-Gates.md) değildir. Solo geçit, yalnızca senin uçtuğun bir arenadır ve Enerji Maddeleştirici ile bulduğun parçalarla açılır; ikisinin kuralları, ödemeleri ve sınırları ayrıdır.

## Bir bakışta {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Açılış**: Sezonun 1. gününden itibaren
- **Zindanı kim açar**: Bedeli klan bankasından ödeyen bir yardımcı lider ya da lider
- **Grup**: Klanın 4 ila 10 üyesi, tek bir grupta
- **Günlük zindan sayısı**: Klan başına UTC gününde 3, aynı anda yalnızca biri açık
- **Aynı anda zindan**: Bir dünyada 6
- **Haritalar**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirentler**: 8; zindan açılırken biri seçilir
- **Patron odası**: Crystalys’lerin ve Twin’lerin %75 kadarı yok edilince açılır, yukarı yuvarlanır
- **Toplanma**: Toplanıp başlamak için 10 dk. Kimsenin başlatmadığı bir zindan kapanır ve bedeli klan bankasına geri döner
- **Süre sınırı**: Başlangıçtan itibaren Aşama 1: 95 dk, Aşama 2: 130 dk, Aşama 3: 165 dk. Süre dolarsa zindan başarısız olur ve tamamlama hiçbir şey ödemez
- **Boş bırakılırsa**: 3 dk boyunca içinde kimse olmayan bir zindan başarısız olur
- **Savaş Lordu düştükten sonra**: Zindan, içerideki pilotlar için 2 dk açık kalır
- **Geri dönüş**: Ayrılan ya da yok edilen bir pilot, iki dönüş arasında en az 20 sn olması koşuluyla istediği kadar geri uçabilir

<!-- dungeons-glance:end -->

## Bir tur nasıl geçer {#how-a-run-goes}

1. **Çağır.** Zindanlar sekmesinde bir [yardımcı lider ya da lider](/wiki/03-Mechanics/Clans.md#hierarchy-roles) bir aşama seçer ve **Çağır**'a basar. Bedel [klan bankasından](/wiki/03-Mechanics/Clans.md#clan-economy-taxation) çıkar ve zindan yukarıda sıralanan haritalardan birini alır. Kimsenin başlatmadığı bir zindan kapanır ve bedel bankaya geri döner.
2. **Gir.** Klan üyeleri uçarken Klan penceresinde **Gir**'e basar, klan portalından sıçrar ya da uyarı kartındaki **Katıl**'a basar (bkz. Girmek). Herkes başlangıç odasına iner ve içerideki pilotlar zindanın grubudur.
3. **Başlat.** Başlangıç odası labirentin bir ucundaki küçük bir odadır ve zindan toplanırken kapısı kapalıdır. İçinde uzaylı yoktur, bu yüzden orada beklemek güvenlidir. Zindan, beklediği her pilot içeride olduğunda ve grup yeterince büyük olduğunda **kendiliğinden başlar**. Çevrimiçi olan, uzakta olmayan ve içeri girmiş bir pilotun grubunda bulunan klan üyelerini bekler, grup dolduğunda da hemen başlar. Zindanı açan pilot ya da bir subay, içeridekiler yeterince kalabalıksa onlarla daha erken başlamak için **Başlat**'a basabilir. Ayrılan bir pilot artık beklenmez. Zindan başladığında kapı bir daha kapanmamak üzere açılır ve bundan sonra yalnızca zaten içeride olan pilotlar geri dönebilir.
4. **Labirentten geç.** Labirente bir uçtan girersin, Savaş Lordu diğer uçta, kilitli bir odada bekler. Labirent karanlıktır: yalnızca grubun keşfettiği yerleri ve gemilerinin yakınındakileri görürsün. Uzaylılar koridorlarda sürüler halinde bekler ve bir sürü, bir pilot beklediği koridor bölümüne uçtuğu anda çıkar, sonra grubu labirent boyunca kovalar.
5. **Ganimet bölgelerini aç.** Labirentteki halkalar bölgeleri işaretler. Birini elinde tut, grup bir kart için oy versin; kart, Savaş Lordu'nun ödemesiyle birlikte ödenir.
6. **Patron odasının kilidini aç.** Labirentteki Crystalys’lerin ve Twin’lerinin dörtte üçünü yok et; Savaş Lordu'nun odasının kapısı açılır. O zamana kadar Savaş Lordu'na zarar verilemez. Diğer uzaylılar oldukları yerde kalır, onları da yok edebilirsin.
7. **Savaş Lordu'nu yen.** Kalkanını ve gövdesini kır, yeteneklerine karşılık ver. O düştüğünde zindan tamamlanır.
8. **Ödemeni al.** Ödeme, Savaş Lordu'nun düştüğü anda gelir. Zindan, içerideki pilotlar için biraz daha açık kalır, sonra kapanır.

## Girmek {#entering}

Bir zindana girmek için **uçuştaki bir gemiye** ihtiyacın var; önce kalk, sonra Klan penceresini aç; ayrıca içinde yeterince klan üyesi olan bir [grup](/wiki/03-Mechanics/Groups.md) gerekir. Aşamanın istediği **seviyeye** de sahip olmalısın ve başka bir zindanın içinde olmamalısın. Zindanın grubunun bir boyut sınırı vardır: dolduğunda kimse giremez.

Zindanı bir yardımcı lider ya da lider açar; klan için aynı anda yalnızca bir tane, günlük zindan sayısına kadar. Klan bankasında bedelin bulunması gerekir. Bir klan, bir aşamayı ancak ondan önceki aşamayı tamamladıktan sonra açabilir.

Bir zindanın içinde dünya değiştiremezsin ve Jump CPU ile Base CPU çalışmaz. Klan zindanı penceresindeki **Ayrıl** düğmesi seni dışarı çıkarır. Önce onay ister; Savaş Lordu zaten düşmüşse seni hemen çıkarır. Ayrılan ya da yok edilen bir pilot geri uçabilir; kaç kez uçabileceğini ve iki dönüş arasında ne kadar bekleyeceğini **Bir bakışta** altındaki liste söyler.

### Klan portalı ve uyarı {#the-clan-portal-and-the-call}

Bir zindan açıldığında klan, onun için her şirketin ana haritasında (`M-1`, `T-1` ve `G-1`), istasyonun güvenli bölgesinin biraz dışında bir **portal** alır. Portalı yalnızca klanın pilotları görür: diğer herkes için yoktur. Kendi güvenli bölgesi yoktur. Yanına uç ve başka herhangi bir portaldaki gibi sıçra; seni **Gir** kurallarına göre zindana götürür: uçuştaki bir gemi, yeterince klan üyesi olan bir grup, aşamanın seviyesi ve grupta yer. Zindan başladıktan sonra portalı yalnızca zaten içeride olan pilotlar kullanabilir. Zindan bitince portal kaybolur.

Klanının zindanı toplanırken ve sen başka bir yerde uçarken sana bir **uyarı** gelir: uçuş ekranının üstünde, sesli bir kart. Zindanı kimin açtığını, içeride kaç pilot olduğunu ve zindanın ne kadar daha açık kalacağını söyler. **Katıl** seni içeri uçurur, tıpkı Zindanlar sekmesindeki **Gir** gibi; zindandan çıktığında geminin eski yerine döner. Grubun çok küçük olduğu sürece Katıl soluk görünür. **Şimdi değil** o zindan için kartı gizler. Grubun zaten içerideyse ve zindan seni bekliyorsa kart bunu söyler. Kart, klanın uçmakta olan pilotlarına (istasyona yanaşmış olanlara değil) ve aşamanın istediği seviyeye sahip olanlara ulaşır. Kartı ve sesini Ayarlar › Genel › Gruplar altındaki **Klan zindanı uyarıları** ile kapatabilirsin.

### Klan zindanı penceresi {#the-clan-dungeon-window}

Bir zindanın içinde tura ait ayrı bir pencere vardır: **Klan zindanı**. Geçen süreyi ve kalanı, kaç uzaylının uçtuğunu ve kaçının yok edildiğini, grubun şimdi ne yapması gerektiğini (labirenti keşfetmek, bir bölgeyi tutmak, patronu bulmak, Crystalys’lerin ve Twin’lerinin dörtte üçünü yok etmek, Savaş Lordu'nu yenmek), bir bölgede dururken tutma çubuğunu, Savaş Lordu'nun yeteneğini geri sayımıyla ve **Ayrıl** düğmesini gösterir. Diğerleri gibi bir penceredir: başlık çubuğundan sürükle ve köşesindeki kırmızı ışıkla kapat. Bir zindana girdiğinde kendiliğinden açılır, her zindan için bir kez: kapatırsan bir sonraki zindana kadar kapalı kalır. Bir zindandayken araç çubuğunda onun için bir **Klan zindanı** düğmesi bulunur. Pencere kapalıyken, Savaş Lordu'nun başlamak üzere olan ya da etkin olan bir yeteneği, adı ve geri sayımıyla tek satırlık bir şerit olarak görünür. Pencereyi yeniden açmak için şeride tıkla. Bir ödül oylaması ya da booster seçimi açıkken ve penceresi kapalıyken, Klan zindanı penceresinde onun için geri sayımıyla birlikte bir satır ve onu yeniden açan bir **Seç** düğmesi bulunur.

## Aşamalar {#the-stages}

Bir zindanın bir aşaması vardır ve aşama onun zorluğudur. Daha yüksek bir aşamada uzaylılar daha dayanıklıdır, daha sert vurur ve daha çok ödeme yapar. Tablodaki çarpanlar uzaylılarındır. Hasar, onların lazerlerini ve roketlerini anlatır. Savaş Lordu tabloyu izlemez: her aşama için kendi sayıları vardır, aşağıda. Tablo ayrıca bir aşamanın birinciye kıyasla kaç uzaylı gönderdiğini de söyler. **Bedel**, zindan açılırken klan bankasından alınır.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aşama | Gereksinim | Uzaylıların gövdesi ve kalkanı | Uzaylı sayısı | Uzaylıların hasarı | Zindanın bedeli (kredi, klan bankasından) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Aşama 1** | 6. seviyeden itibaren | ×1 | ×1 | ×1 | 500.000 |
| **Aşama 2** | 7. seviyeden itibaren | ×1,5 | ×1 | ×1,5 | 1.000.000 |
| **Aşama 3** | 8. seviyeden itibaren | ×2 | ×1 | ×2 | 2.000.000 |

<!-- dungeons-stages:end -->

## Labirent {#the-maze}

Her zindan, kendi haritasında, yukarıdaki listedeki haritalardan birinde yer alan kapalı bir labirenttir ve labirent birkaç düzenden biridir. Labirent haritanın tamamını kenardan kenara doldurur: katı duvarlı odalar ve koridorlardan oluşan bir ızgara. Gemiler duvarı geçemez, duvar atışları da engeller; yani duvar siperdir. Meteor yukarıdan düşer ve bir duvar onu durdurmaz.

**Odalar ve kapılar.** İndiğin başlangıç odasının ve uzak uçtaki Savaş Lordu odasının birer kapısı vardır. Kapalı bir kapı gemiler, atışlar ve uzaylılar için aynı şekilde bir duvardır. Başlangıç kapısı zindan başladığında açılır. Savaş Lordu'nun kapısı, Crystalys’lerin ve Twin’lerinin dörtte üçü yok edilene kadar kilitli kalır ([Kilitli oda](#the-locked-room) bölümüne bak). Aralarında labirentin her ganimet bölgesi için bir ganimet odası vardır.

**Sis.** Labirent karanlıktır. Uçuşta duvarlarını ve uzaylılarını yalnızca grubun bulunduğu yerlerde ve grubun her gemisinin çevresinde kısa bir mesafede görürsün. Bir oda, içinde biriniz olur olmaz keşfedilmiş sayılır. Mini harita da aynıdır: grup keşfettikçe dolan, tüm katın bir haritasıdır; giriş, Savaş Lordu'nun kapısı, bulduğunuz bölgeler ve bulduktan sonra Savaş Lordu üzerinde gösterilir. Kendi grubunun pilotları her zaman gösterilir.

## Uzaylılar {#the-aliens}

Labirenti dört tür uzaylı korur. Koridorlarda sürüler halinde beklerler, asla bir odada değil, ve bir sürü, bir pilot beklediği koridor bölümüne uçtuğu anda çıkar. Hiçbir pilotun bulunmadığı yerde haritada hiçbir şey yoktur; bu yüzden sen oraya varmadan önce labirentin derinliklerinde, duvarların ardında hiçbir sürü durmaz. Bir sürü yer için beklemez: dışarıda zaten kaç uzaylı olursa olsun aynı anda haritadadır. Bir koridor bölümünde tek bir sürü bekler; bu yüzden uçtuğun bölümde karşına bir sürü çıkar, birkaç sürünün toplamı değil (on kişilik bir grupta bölümlerden daha çok sürü vardır ve orada bir bölümde iki sürü bekler, ikisi de çıkar). Çıkmış bir sürü seni beklemez: grubu labirent boyunca kovalar ve herkesi kaybeden bir sürü çıktığı yere geri döner ve iyileşir. Bir sürü yalnızca bir kez çıkar: yok ettiğin geri gelmez, uçup uzaklaştığın ise haritada kalır. Ganimet bölgelerinin dalgaları farklıdır: zindan havada aynı anda yalnızca belirli sayıda uzaylı tutar ve bu sayı grubun büyüklüğüyle artar; bu yüzden onu aşacak bir dalga yer için bekler, yok ettiğin bir sürü sıradaki dalgayı içeri alır. Daha büyük bir grup orantılı olarak daha çok uzaylıyla, daha küçük bir grup daha az uzaylıyla karşılaşır ve bir uzaylı türü asla birin altına düşmez.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Uzaylılar, 5 kişilik bir grup için | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Toplam | 235 | 235 | 235 |
| Patron odasını açmak için | 34 | 34 | 34 |
| Bir ganimet bölgesinin dalgası | 12 × Dungeon Goombah ve 1 × Dungeon Crystalys | 12 × Dungeon Goombah ve 1 × Dungeon Crystalys | 12 × Dungeon Goombah ve 1 × Dungeon Crystalys |

- **Bir ganimet bölgesinin dalgası yer için bekler**: Grubun her pilotu için 10, ya da toplamda 70 uzaylı hayattayken

<!-- dungeons-population:end -->

Her tür sırayla. Gövde ve kalkan, olağan değerlerin sütundaki aşamanın çarpanıyla çarpımıdır.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Görünüşü**: Goombah
- **Sürü büyüklüğü**: 6
- **Ödülü ve ganimeti şunun gibi**: Goombah

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 32.000 | 48.000 | 64.000 |
| Kalkan | 48.000 | 72.000 | 96.000 |
| Lazer hasarı (saniyede bir salvo) | 3.000 | 4.500 | 6.000 |
| Hız | 180 | 180 | 180 |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | 1.800 | 1.800 | 1.800 |
| Ödül ve ganimet, orijinalin katı | ×1 | ×1,5 | ×2 |
| Yok etme başına Kredi | 15.000 | 22.500 | 30.000 |
| Yok etme başına Thulium | 75 | 113 | 150 |
| Yok etme başına Deneyim | 3.000 | 4.500 | 6.000 |
| Yok etme başına Onur | 24 | 36 | 48 |

### Dungeon Pirate

- **Görünüşü**: Pirate Boss
- **Sürü büyüklüğü**: 2
- **Ödülü ve ganimeti şunun gibi**: Pirate Boss
- **Roket**: Her 5 sn bir düz roket, menzil 1.000 birim

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 250.000 | 375.000 | 500.000 |
| Kalkan | 50.100 | 75.150 | 100.200 |
| Lazer hasarı (saniyede bir salvo) | 200 | 300 | 400 |
| Roket hasarı | 5.000 | 7.500 | 10.000 |
| Hız | 100 | 100 | 100 |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | 1.800 | 1.800 | 1.800 |
| Ödül ve ganimet, orijinalin katı | ×1 | ×1,5 | ×2 |
| Yok etme başına Kredi | 145.000 | 217.500 | 290.000 |
| Yok etme başına Thulium | 725 | 1.088 | 1.450 |
| Yok etme başına Deneyim | 29.000 | 43.500 | 58.000 |
| Yok etme başına Onur | 232 | 348 | 464 |

### Dungeon Crystalys

- **Görünüşü**: Crystalys
- **Sürü büyüklüğü**: 2
- **Ödülü ve ganimeti şunun gibi**: Crystalys

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 256.000 | 384.000 | 512.000 |
| Kalkan | 160.000 | 240.000 | 320.000 |
| Lazer hasarı (saniyede bir salvo) | 10.000 | 15.000 | 20.000 |
| Hız | 230 | 230 | 230 |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | 2.400 | 2.400 | 2.400 |
| Ödül ve ganimet, orijinalin katı | ×1 | ×1,5 | ×2 |
| Yok etme başına Kredi | 75.000 | 112.500 | 150.000 |
| Yok etme başına Thulium | 200 | 300 | 400 |
| Yok etme başına Deneyim | 12.000 | 18.000 | 24.000 |
| Yok etme başına Onur | 52 | 78 | 104 |

### Dungeon Crystalys Twin

- **Görünüşü**: Crystalys, 1,4 kat büyük
- **Sürü büyüklüğü**: 1
- **Ödülü ve ganimeti şunun gibi**: Crystalys

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 512.000 | 768.000 | 1.024.000 |
| Kalkan | 320.000 | 480.000 | 640.000 |
| Lazer hasarı (saniyede bir salvo) | 20.000 | 30.000 | 40.000 |
| Hız | 230 | 230 | 230 |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | 2.400 | 2.400 | 2.400 |
| Ödül ve ganimet, orijinalin katı | ×2 | ×3 | ×4 |
| Yok etme başına Kredi | 150.000 | 225.000 | 300.000 |
| Yok etme başına Thulium | 400 | 600 | 800 |
| Yok etme başına Deneyim | 24.000 | 36.000 | 48.000 |
| Yok etme başına Onur | 104 | 156 | 208 |

<!-- dungeons-enemies:end -->

## Savaş Lordu {#the-warlord}

Savaş Lordu, labirentin uzak ucundaki odada bekler ve düşüşü tamamlamanın ödemesini yapar. Diğer uzaylılar gibi kendi yok edilişi için ayrıca ödeme yapmaz. Devasa büyümüş bir Crystalys'tir. Gövdesi ve kalkanı grubun büyüklüğüyle büyür: ne kadar çok pilot girerse, orantılı olarak o kadar dayanıklıdır. Kapı kapalı da olsa açık da olsa odasından asla çıkmaz: odanın duvarları içinde kalır ve koridorlarda avlanmaz. Dışarıdaki bir pilot onu ancak odanın kenarına kadar çekebilir; açık bir kapıdan yine de lazerinin yettiği her şeye ateş eder. Yeteneklerini tek tek, rastgele sırayla kullanır; her birinin kendi bekleme süresi vardır.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Görünüşü**: Crystalys, 3 kat büyük
- **Kalkan dolumu**: Saniyede 3.000, 15 sn hasarsız kaldıktan sonra

|  | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | ---: | ---: | ---: |
| Gövde | 10.000.000 | 15.000.000 | 25.000.000 |
| Kalkan | 8.000.000 | 12.000.000 | 20.000.000 |
| Lazer hasarı (saniyede bir salvo) | 12.500–15.000 | 15.000–17.500 | 20.000–25.000 |
| Hız | 120 | 120 | 120 |
| Lazer menzili | 1.100 | 1.100 | 1.100 |

Yukarıdaki gövde ve kalkan 5 kişilik bir grup içindir. Grupla birlikte büyürler: bunlar, zindan başladığında gruptaki pilot sayısına göre Savaş Lordu'nun gövdesi ve kalkanının toplamıdır.

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

### Kilitli oda {#the-locked-room}

Savaş Lordu'nun odasının kapısı, zindan açıldığı andan itibaren kapalıdır ve kapalıyken Savaş Lordu'na zarar verilemez: hiçbir lazer, roket ya da patlama ona değmez ve hiçbir yetenek kullanmaz. Zindanın yapıldığı **Crystalys’lerin ve Twin’lerinin dörtte üçü** yok edildiğinde (yukarı yuvarlanır; yukarıdaki uzaylı tablosu bunları 5 kişilik bir grup için sayar ve son satırı kaç tane gerektiğini söyler) kapı bir daha kapanmamak üzere açılır. Sayılanlar labirentin sürülerindeki Crystalys’ler ve Twin’lerdir, onları kim yok ederse etsin. Bir sürü ancak bir pilot koridor bölümüne uçtuğunda çıkar; bu yüzden kapıyı açmak için grubun yeterince sürü bulması gerekir. Diğer uzaylılar, ganimet bölgelerinin dalgaları, Savaş Lordu'nun çağırdığı Goombah'lar ve Savaş Lordu'nun kendisi kapı için sayılmaz.

Klan zindanı penceresi odayı açmak için bunlardan kaçının daha yok edilmesi gerektiğini sayar ve bir etiketle Savaş Lordu'na zarar verilemeyeceğini söyler; oda açıldığında bir mesaj sana haber verir. Henüz çıkmamış bir sürü tam sayılır, bu yüzden grubun labirentte Crystalys’leri ve Twin’lerini bulup koridor bölümlerine uçması gerekir. **Diğer uzaylılar kapı açılınca kaybolmaz.** Labirentte kalırlar, bir pilot koridor bölümlerine uçunca çıkarlar ve eskisi gibi yok edilebilirler; istiyorsa bir grup Savaş Lordu'yla dövüşmeden önce hepsini yok edebilir: penceredeki uzaylı sayacı zindanın yapıldığı tüm uzaylılara kadar sayar ve hiçbiri kalmadığında dolu görünür. Düştüklerinde ödeme yaparlar ([uzaylıların ödemesi](#what-the-aliens-pay)) ve Savaş Lordu düştüğünde hâlâ yaşayanlar zindanla birlikte gider. Mini haritada kapı, kilitliyken kırmızı bir çizgi, açıkken yeşil bir çizgidir. Bir zindan asla tuzak değildir: kapısı kapalı kalan bir zindanı yine de süre sınırı bitirir ve bir yönetici, takılıp kalmış bir zindanın odasının kilidini açabilir.

### Yetenekleri {#its-abilities}

- Can çalma aurasının **kırmızı halkası**, içindeki her pilota zarar verir ve bu hasarla Savaş Lordu'nu iyileştirir. Kalkan emiliminin de kırmızı bir halkası vardır: içindeki pilotların kalkanını boşaltır ve Savaş Lordu'nunkini doldurur. İkisinde de halkadan çık ya da bir duvarın arkasına geç.
- Meteor yağmurunun **kehribar halkaları**, meteorların bir an sonra nereye düşeceğini gösterir. Hareket etmeye devam et ve düşmeden önce halkadan çık.
- **En aranana odaklan** yeteneği, Savaş Lordu'na en çok hasar vermiş pilotu geminin üzerinde altın rengi bir ayraçla işaretler ve sürdüğü sürece Savaş Lordu ona her saniye bir fazladan atış yapar. Nişanı değişmez: görebildiği en yakın pilota ateş etmeye devam eder, bu yüzden aynı zamanda en yakın olan işaretli pilot ikisini de yer. Fazladan atış için açık bir görüş hattı ve Savaş Lordu'nun lazer menzili gerekir; bir duvar ya da biraz mesafe onu kurtarır. Kimse hasar vermediği sürece başlamaz.
- **Roket yağmuru**, rastgele pilotlara güdümlü roketler gönderir, ama yalnızca Savaş Lordu'nun görebildiği pilotlara; yoldaki bir duvar roketi durdurur. Bir halka, bir roketin hangi pilotu izlediğini gösterir. Bir EMP Charge ya da gizlenme onları atlatır.
- **Sürü desteği**, Savaş Lordu'nun Goombah'larını çağırmasıdır. Onlar yaşadığı sürece ona zarar verilemez ve ateş etmez, başka bir yetenek de kullanmaz. Hepsini yok et: afiş kaç tanesinin kaldığını sayar. Bir dakika geçerse Savaş Lordu'na yine zarar verilebilir ve kalan Goombah'lar yerinde kalıp savaşmaya devam eder. Patron odası için sayılmazlar ve hiçbir şey ödemezler.
- **Kaos Bölgesi**, Savaş Lordu'nun çevresinde, yerde duran mor bir halkadır ve sürdüğü müddetçe Savaş Lordu nereye giderse oraya gider. Halkanın içindeki hiç kimse lazerle ya da roketle saldıramaz; ama onarım, gizlenme ve uçuş çalışmaya devam eder, Savaş Lordu ve uzaylıları her zamanki gibi ateş eder. Halka etkisini göstermeden kısa bir an önce belirir: ondan çık ve dışarıda kal, çünkü Savaş Lordu'nu izler. Halkanın dışındaki bir pilot, silahları yettiği kadar ateş etmeye devam edebilir.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Yetenek | Hazırlık | Süre | Bekleme süresi | Halka yarıçapı (birim) | Savaş Lordu'nun geri kazandığı en çok |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Can çalma aurası** | 2 sn | 15 sn | 2 dk | 900 | Gövde ve kalkan: %8 |
| **Meteor yağmuru** | 1,5 sn | 3 salvo, aralarında 4 sn | 2 dk | 420 | – |
| **En aranana odaklan** | 1 sn | 20 sn | 2 dk | – | – |
| **Roket yağmuru** | 1,5 sn | 45 sn | 2 dk | – | – |
| **Kalkan emilimi** | 2 sn | 15 sn | 2 dk | 900 | Kalkan: %6 |
| **Sürü desteği** | 2 sn | En fazla 1 dk | 3 dk | – | – |
| **Kaos Bölgesi** | 2 sn | 15 sn | 2 dk | 900 | – |

| Yetenek | Aşama 1 | Aşama 2 | Aşama 3 |
| :--- | :--- | :--- | :--- |
| **Can çalma aurası** | Saniyede 8.000 | Saniyede 10.000 | Saniyede 12.000 |
| **Meteor yağmuru** | Salvo başına 6 meteor, her biri 40.000 | Salvo başına 8 meteor, her biri 50.000 | Salvo başına 10 meteor, her biri 60.000 |
| **En aranana odaklan** | En çok hasar veren pilota fazladan mermi başına 18.750–22.500, her 1 sn bir mermi | En çok hasar veren pilota fazladan mermi başına 22.500–26.250, her 1 sn bir mermi | En çok hasar veren pilota fazladan mermi başına 30.000–37.500, her 1 sn bir mermi |
| **Roket yağmuru** | Roket başına 26.000, her 15 sn bir roket | Roket başına 32.500, her 15 sn bir roket | Roket başına 39.000, her 15 sn bir roket |
| **Kalkan emilimi** | Saniyede 10.000 kalkan | Saniyede 12.500 kalkan | Saniyede 15.000 kalkan |
| **Sürü desteği** | 12 Goombah | 18 Goombah | 24 Goombah |
| **Kaos Bölgesi** | Halkanın içindeki pilotlar saldıramaz | Halkanın içindeki pilotlar saldıramaz | Halkanın içindeki pilotlar saldıramaz |

<!-- dungeons-abilities:end -->

## Ganimet bölgeleri {#loot-zones}

Labirentin zemindeki bir halka, grup bulur bulmaz her ganimet bölgesini işaretler. Bir süre içinde dur, bölge uyanır ve ona doğru bir uzaylı dalgası gelir. Sonra grubun bölgeyi **tutması** gerekir: çubuk dolana kadar içeride bir pilotu tut. Halkada ne kadar çok pilot varsa çubuk o kadar hızlı dolar: çubuğun yanındaki sayı kaç kat daha hızlı olduğunu söyler, aşağıdaki tablo da süreleri verir. Halkadaki yeterince uzaylı çubuğu durdurur (aşağıdaki liste kaç tane olduğunu söyler) ve içeride kimse yokken çubuk geri gider; bu yüzden önce dalgayı temizle. Bölge açıldığında grup üç farklı kart görür ve birine **oy verir**. Bir bölge yalnızca bir kez açılır ve dalgası bir daha gelmez. Oylama, ekranın sağ tarafında, her ödül için bir satır içeren ayrı küçük bir pencere: resmi, adı, kaç tane alacağın ve kaç oyu olduğu. Ne olduğunu ve kimin aldığını okumak için bir satırın üzerine gel, oy vermek için bir satıra bas (oyunu değiştirmek için başka bir satıra bas). Pencere her oylamada kendiliğinden açılır ve savaşı örtmez, böylece grup seçerken uçmaya devam edebilirsin. İstediğin yere sürükle ya da kırmızı ışıkla kapat; Klan zindanı penceresindeki **Seç** düğmesi onu yeniden açar. Pencere kapalıyken de oyun sayılır ve geri sayım işlemeye devam eder.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ganimet bölgeleri**: Her labirentte 6
- **Yarıçap**: 450 birim
- **Uyanma**: Halkanın içinde 2 sn dur
- **Tutma**: İçeride 30 sn boyunca bir pilot tut. Halkada 3 veya daha fazla uzaylı varken çubuk durur, içeride kimse yokken geri gider
- **Seçim**: Grubun oy vermek için 45 sn süresi var. Oy verme, orada bulunan her pilot oy verdiğinde ya da bir kart oyların yarısından fazlasını aldığında daha erken biter

Halkada ne kadar çok pilot varsa bölge o kadar hızlı tutulur. Bir bölgeyi tutmak ne kadar sürer:

| Halkadaki pilotlar | Bölgeyi tutma süresi |
| :--- | ---: |
| 1 | 30 sn |
| 2 | 20 sn |
| 3 | 15 sn |
| 4 | 12 sn |
| 5 veya daha fazla | 10 sn |

<!-- dungeons-zones:end -->

### Boosterlar {#boosters}

Aşama 2 ve 3'te grup, zindanın uzaylılarını yok ederek booster kazanır. Her onda birlerinde bir booster düşer: uzaylıların onda biri yok edildiğinde, sonra onda ikisi, ve böyle hepsine kadar, toplam on düşüş. Zindanın yapıldığı her uzaylı sayılır, kim yok ederse etsin (bu, Klan zindanı penceresindeki yok edilen uzaylı sayısıdır); ganimet bölgelerinin dalgaları ve Savaş Lordu'nun çağırdığı uzaylılar sayılmaz, bu yüzden bir bölge booster getirmez. Her düşüşte her pilot, oyunun beşten rastgele çektiği üç booster arasından kendisi için geçici bir booster seçmek üzere yarım dakikalık bir pencere alır: **Hasar** (lazerlerin daha sert vurur), **Gövde** (geminin daha çok gövde taşır), **Kalkan** (kalkanın daha çok dayanır), **Hız** (geminin daha hızlı uçar) ve **Kalkan dolumu** (kalkanın daha hızlı dolar). Seçmek için bir karta bas. Zamanında cevap vermezsen oyun senin yerine Gövde seçer; Gövde üçünün arasında değilse ilkini seçer. Bir seçim aşama 3'te %3, aşama 2'de %1,5 değerindedir, bu yüzden on seçim, hangi türler olursa olsun, aşama 3'te en çok yüzde otuza, aşama 2'de yüzde on beşe kadar birikir. Aşama 1'de booster yoktur. Üç booster, ödül oylamasındaki gibi ayrı küçük bir pencerenin satırlarıdır: her düşüşte ekranın sağ tarafında kendiliğinden açılır ve yarım dakika onun geri sayımıdır. Türün ne yaptığını ve ondan şimdiden ne kadar sahip olduğunu okumak için bir satırın üzerine gel. Pencereyi sürükle, kırmızı ışıkla kapat ya da Klan zindanı penceresindeki **Seç** düğmesiyle yeniden aç.

Onuncu düşüş son uzaylıyla gelir. Savaş Lordu ile savaşmadan önce her uzaylıyı yok eden grup on düşüşün hepsini alır; Savaş Lordu'nun odasını açıp yoluna devam eden grup, o ana kadar yok ettiği uzaylıların düşüşlerini alır ve geriye kalan uzaylılar kalır, yine de yok edilebilir. Savaş Lordu ile savaş başladıktan sonra artık hiç booster düşmez.

Bir booster, zindan tamamlanana kadar sürer. Zindandan ayrılırsan ya da yok edilirsen boosterlarını kaybedersin ve yeniden uçup girdiğinde onları geri alırsın. Klan zindanı penceresinin altındaki bir etiket sahip olduklarını listeler.

### Kartlar {#the-cards}

Kartlar, aşağıdaki havuzdan teker teker çekilir. Şans, bir kartın tek bir çekilişteki şansıdır. Her kart ödeme alan her pilota gider, ekipman kartları da: çok kopyalı bir kart her birine o kadar kopya verir, ekipman kartı ise her birine kendisi için dövülmüş kendi parçasını verir. Ödeme almayan bir pilot kart da almaz ve başarısız olan bir zindanda açılan bölge hiçbir şey ödemez.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Kart | Aşama 1 | Aşama 2 | Aşama 3 | Şans | Kime gider |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | %23,9 | Ödeme alan her pilot |
| Velkonite Reinforced Plate | 10 | 15 | 25 | %13,65 | Ödeme alan her pilot |
| Velkonite | 200 | 300 | 500 | %13,65 | Ödeme alan her pilot |
| Orvium | 200 | 300 | 500 | %13,65 | Ödeme alan her pilot |
| Ultra Core | 5.000 | 7.500 | 12.500 | %11,4 | Ödeme alan her pilot |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | %9,1 | Ödeme alan her pilot |
| Dark Matter | 10 | 16 | 24 | %9,1 | Ödeme alan her pilot |
| Dark Matter Plate | 1 | 1 | 2 | %4,55 | Ödeme alan her pilot |
| Starfire-III | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Helios Beam | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Engine III | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Adaptive Core III | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Heavy Shield Core | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Momentum Thruster IV | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Impulse Thruster IV | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Hull Plating II | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Hull Plating III | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Damage Amp IV | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Crit Amp IV | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Penetration Amp IV | – | – | 1 | %0,07 | Ödeme alan her pilot |
| Capacity Shield Cell IV | – | – | 1 | %0,08 | Ödeme alan her pilot |
| Absorption Shield Cell IV | – | – | 1 | %0,08 | Ödeme alan her pilot |

- **Ekipman**: Tek kopyalı kartlar ekipmandır: birlikte kartların %1 kadarı

<!-- dungeons-cards:end -->

Tek kopyalı kartlar **ekipmandır** ve yalnızca aşama 3 bir zindan bunları sunabilir. Bir ekipman parçası, ödeme alan her pilot için ödenirken dövülür: her biri Montaj'da yaptığın bir parçayla aynı şanslarla kendi [büyüleme kademesini](/wiki/06-Items/Overview.md#item-enchants) çeker; bu yüzden çoğu Standart çıkar ve Ebedi'ye kadar daha yüksek bir kademe, bonuslarıyla, nadir bir bulgudur.

## Ödeme {#pay}

Savaş Lordu düştüğünde, hak eden her pilota tamamlanan tur için bir kez ödeme yapılır. Grubun seçtiği kartlar, aşamanın ödemesinin üstüne gelir. Dünya çarpanı yoktur: ödeme her dünyada aynıdır.

**Orvium Reinforced Plates** oylamadaki bir kart değildir. Aşamanın ödemesinin parçasıdır ve ödeme alan her pilot onları tamamlama başına bir kez alır. Tamamlamanın ödediği eşyalar satılabilir değildir: onları [Açık Artırma'da satamazsın](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aşama | Onur | Deneyim | Kredi | Thulium | x4 cephane | Orvium Reinforced Plates | PvE sıralama puanı |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Aşama 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 5 | 600 |
| **Aşama 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 10 | 1.500 |
| **Aşama 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 15 | 2.400 |

<!-- dungeons-pay:end -->

### Kime ödeme yapılır {#who-is-paid}

Bu kurallar **tamamlama için** kime ödeme yapılacağını belirler. Bir tur, hiçbir şey ödemese bile sonuna kadar oynanır ve sonuç ekranı nedenini söyler. Bir aşama için zaten ödeme aldığın için giriş asla reddedilmez: tamamlama yalnızca hiçbir şey ödemez. Uzaylılar aynı kuralları, savaştaki pay hariç, yok ediş yok ediş okur ([uzaylıların ödemesi](#what-the-aliens-pay)).

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Bir gün**: Bir aşama, bir pilota UTC gününde bir kez öder: Savaş Lordu'nun düştüğü gün
- **Bir hafta**: Bir pilot, UTC haftasında (Pazartesi–Pazar) en çok 10 aşama tamamlama için ödeme alır
- **İçeride**: Toplamda en az 2 dk
- **Savaşa katkı**: Şunlardan en az biri: Savaş Lordu'nun gövdesine ve kalkanına toplam %2 oranında hasar verdi; zindanın 10 uzaylısını yok etti; Savaş Lordu'yla savaş sırasında diğer pilotları 50.000 iyileştirdi

<!-- dungeons-rules:end -->

### Bir günün ve bir haftanın değeri {#what-a-day-and-a-week-are-worth}

Bir pilotun bir günde ve sınırların izin verdiği en iyi haftada alabileceği ödeme. Son sütun, ödemenin [PvE puanlarına](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) ne kattığını gösterir.

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Her pilota ödeme | Onur | Deneyim | Kredi | Thulium | x4 cephane | Orvium Reinforced Plates | PvE sıralama puanı |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bir gün, her aşama bir kez | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 30 | 4.500 |
| En iyi hafta: 7 × Aşama 3 ve 3 × Aşama 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 135 | 21.300 |

Ödemesi yapılan bir tamamlamanın deneyimi PvE sıralama puanlarınıza sayılır: her 1.000 deneyim için bir puan.

<!-- dungeons-totals:end -->

### Uzaylıların ödemesi {#what-the-aliens-pay}

Bir zindanın her uzaylısı düştüğünde ödeme yapar ve ganimet bırakır; örnek alındığı oyundaki uzaylı gibi: bir Dungeon Goombah bir [Goombah](/wiki/04-Aliens/Goombah.md) gibi, bir Dungeon Crystalys ve Twin'i bir [Crystalys](/wiki/04-Aliens/Crystalys.md) gibi, bir Dungeon Pirate ise Pirate Boss gibi ([Pirate sürüsü](/wiki/05-Swarms/Pirate-Swarm.md)). Bir uzaylının yok edilmesinin ödediği ve bıraktığı şey, orijinalinkinin **ikisinin gövde ve kalkanının birlikte oranıyla çarpılmış** halidir: orijinali kadar dayanıklı bir uzaylı orijinalin ödediğini öder, iki kat dayanıklı olan iki kat öder ve her eşyadan iki kat bırakır, böyle devam eder. [Uzaylılar](#the-aliens) başlığı altındaki her uzaylı türünün bölümü, oranı ve her aşamada bir yok edişin ödemesini verir.

- **Kime ödenir.** Uzaylıya zarar veren pilotlara, verdikleri hasara göre, sürülerin uzaylılarında olduğu gibi: uzaylıya yalnızca sıyırıp geçen bir pilot ya da grup hiçbir şey almaz, bir grup tek kişi gibi ödenir ve bir grubun içinde enkaza yakın olan ve yakın zamanda ateş etmiş üyeler ödenen miktarı seviyeye göre paylaşır. Uzaylıya hasar vermemiş bir pilot, ne kadar yakından uçmuş olursa olsun, onun için hiçbir şey almaz; hiçbir pilotun zarar vermediği bir uzaylı ise kimseye ödeme yapmaz. Yalnızca yukarıdaki kuralların ödeme yaptığı pilotlar dahildir: ayrılan, yeterince uzun süre içeride kalmayan, bugün aşama için zaten ödeme alan ya da haftanın tüm ödemeli tamamlamalarını kullanan pilot uzaylılar için hiçbir şey almaz, payını diğerleri alır. Bir yok ediş savaştaki payı istemez: uzaylıya zarar vermek zaten paydır. Bir grubun en çok hasar veren üyesi yok edilmişse ya da haritada değilse, enkaza yakın olan ve yakın zamanda ateş etmiş üyeler ödemeyi onsuz paylaşır.
- **Ne ödenir.** Kredi, Thulium, deneyim ve onur, yok ediş başına bir kez. Ödeme, orijinalin Alpha'da ödediğidir ve her dünyada aynıdır: bir zindanın dünya çarpanı yoktur. Boosterların, Premium'un, formasyonun ve klanının bonusları herhangi bir yok edişte olduğu gibi geçerlidir; deneyim de tamamlamanın deneyimi gibi [PvE puanlarına](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) sayılır.
- **Ganimet.** Orijinalin şanslarıyla çekilir, sonra her miktar oranla çarpılır (bir birimin kesri, bir tane daha alma şansıdır). Enkazın yerinde bir kutu olarak düşer; önce en çok hasar veren pilot ve klanı için, sonra haritadaki herkes için, ardından kaybolur. Harita aynı anda yalnızca belirli sayıda kutu tutar, bu yüzden ilerlerken topla; zindan kapandığında haritada kalanlar zindanla birlikte gider. Tamamlamanın eşyalarından farklı olarak bunlar bir uzaylının olağan ganimetidir: eşya satılabilirse [Açık Artırma'da satılabilir](/wiki/03-Mechanics/Auction.md#marketable-items).
- **Ödeme yapmayanlar.** Savaş Lordu yok ediş için ödeme yapmaz, yalnızca tamamlama için yapar. Çağırdığı Goombah'lar hiçbir şey ödemez, çünkü çağrı, savaş sürdüğü sürece geri gelir.
- **Oyunun bir yok edişi değil.** Zindandaki bir yok ediş görevlere, başarımlara, yok etme sayaçlarına, sıfırlama puanlarına, bir yok edişin PvE puanlarına, dronlara ya da P.E.T.’lere sayılmaz: bir Dungeon Goombah, oyundaki bir Goombah değildir.
- **Sınırlar.** Yukarıdaki günlük ve haftalık sınırlar uzaylıların ödemesini de tamamlamanınki gibi tutar: bugün aşama için zaten ödeme alan ya da haftanın tüm ödemeli tamamlamalarını kullanan pilot, uzaylıları için de bir şey almaz ve bir yok edişin havuzu diğerlerine gider. Tamamlanmayan bir zindan, yok edişlerini kuralların ödeme yaptığı pilotlara öder, tamamlama için ise hiçbir şey ödemez.

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
- **Ödeme alan pilotlar**: Zindanda en az 3

<!-- dungeons-clan:end -->

## İpuçları {#tips}

- Bir bölgeyi tutmaya çalışmadan önce dalgasını temizle ve uzaylılar içeri girerse halkanın içinde savaş.
- Tüm grubu bir bölgeye getir: halkada ne kadar çok pilot varsa bölge o kadar hızlı tutulur.
- Labirentte Crystalys’leri ve Twin’lerini ara: Savaş Lordu'nun kapısı, onların dörtte üçü ölünce açılır, ondan önce değil. Diğer uzaylılar bekleyebilir ya da onlar da yok edilebilir.
- Duvarları kullan: lazerler onları geçmez, Savaş Lordu'nun aurasının kırmızı halkaları onlarda durur ve bir duvar Savaş Lordu'nun roketlerini de durdurur.
- Roket yağmuru için bir EMP Charge sakla.
- Savaş Lordu Goombah'larını çağırdığında önce onları yok et: onlar gidene kadar ona zarar verilemez. Kaos Bölgesi'nde ateş etmeden önce halkadan çık.
- Klan zindanı penceresindeki saate bak. Süre dolduğunda zindan başarısız olur ve tamamlama hiçbir şey ödemez.
