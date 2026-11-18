<!-- wiki-i18n source: 0b67d55ade0b37c6 -->
<!-- wiki-i18n title: Solo Geçitler -->
# Solo Geçitler {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; solo geçitler; solo geçit; galaksi geçitleri; geçit parçası; parça; parçalar; enerji maddeleştirici; çevirme; garanti; dalga; dalgalar; can; devam et; pes et; ölümsüz; meydan okuma; başarım; thulium sınırı -->

**Solo geçitler**, Galaksi Geçitleri’nin tek başına uçtuğun beş geçididir: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** ve **Omega Vault**. Her biri kendine ait boş bir arenadır; orada uzaylı dalgaları sana birbiri ardına gelir ve sonda bir patron bekler. Bir geçidi **parçalarıyla** inşa edersin; parçaları Enerji Maddeleştirici’yi Thulium ile çevirerek bulursun, bir tamamlama da kredi, Thulium, deneyim, onur, cevher, plaka ve cephane öder.

Bir solo geçit bir [klan zindanı](/wiki/03-Mechanics/Dungeons.md) değildir. Zindan, bir klanın bir grup için açtığı, sonunda bir Savaş Lordu bulunan labirenttir; solo geçit ise yalnızca senin bulunduğun bir arenadır ve kimse seninle birlikte giremez. İkisinin kuralları, ödemeleri ve sınırları ayrıdır. Galaksi Geçitleri sayfasında ayrıca **Chrono-Gate** vardır; o uçulacak bir yer değil, sıfırlama için [Nakliye Deposu](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)’nu açan geçittir: parçaları aynı çevirmelerle bulunur.

## Bir bakışta {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Geçitler**: 7: Chrono-Gate ve 6 solo geçit, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault ve Davidski's Nightmare
- **Çevirme**: Her çevirme için 100 Thulium ve bir seferde 1, 5, 10 ya da 100 çevirme
- **Parça şansı**: Çevirme başına %13, hangi kategoriyi çevirirsen çevir. Parça o kategorinin geçitlerinden birine aittir, hepsi eşit olasılıklıdır: Chrono-Gate tek başına hepsini alır, Alpha Rift, Beta Breach ve Gamma Foundry her biri %4,33, Delta Siege ve Omega Vault her biri %6,5 alır. Chrono-Gate tamamlandığında kategorisinde çevrilecek bir şey kalmaz
- **Garanti**: Arka arkaya 24 parçasız çevirmeden sonra şans her çevirmede artar ve 47 sonra bir sonraki çevirme her zaman bir parça bulur. Herhangi bir geçidin bir parçası sayımı yeniden başlatır
- **Canlar**: Bir denemede 3; her ölüm bir tanesini götürür
- **Geri sayım**: Her dalgadan önce 5 sn, ilk dalgadan ve patronunkinden önce de. Bir dalganın zamanlayıcısı yoktur, turun da yoktur
- **Arena**: Kaya olmayan 8.000 × 6.000 birimlik açık alan ve içinde yalnızca sen varsın. Bir dünyada 16 tane vardır ve hepsi doluyken giremezsin
- **Aynı anda uzaylı**: Bir dalgadan aynı anda en çok 60 canlıdır, isteğe bağlı bir dalgada 250. Kalanı yer bekler
- **Patronlar**: Bir patron faz değiştirirken 3 sn boyunca hasar alamaz
- **Thulium sınırı**: Bir geçit, çevirmelere harcadığın Thulium’un en çok %50 kadarını geri öder. Kalanı kırpılır ve sonuç ne kadarını söyler

<!-- solo-glance:end -->

## Geçit parçalarını bulmak {#finding-gate-parts}

**Galaksi Geçitleri** sayfasını aç ve Enerji Maddeleştirici’yi çevir. Her çevirme Thulium ile ödenir ve en çok bir parça bulur. Önce bir **kategori** seç: **Chrono-Gate**, **Alpha–Gamma** (Alpha Rift, Beta Breach ve Gamma Foundry) ya da **Delta–Omega** (Delta Siege ve Omega Vault). Parça bulma şansı her kategoride aynıdır ve parça, seçtiğin kategorinin geçitlerinden birine aittir; hepsi eşit olasılıklıdır. Bir geçidi inşa etmek için ondan belli sayıda parça gerekir ve parçalar sen kullanana kadar senindir. Parça bulmayan bir çevirme boşa gitmez: bir ödül öder ([aşağıda](#a-spin-without-a-part)). Her çevirme ücretlendirilir. Chrono-Gate tamamlandığında seçeneği kapanır, çünkü içinde bulunacak bir şey kalmaz; diğer iki kategori şansını korur, yani bir solo geçidin parçası Chrono-Gate varken de yokken de aynı maliyettedir.

Tablo her geçidin parça olarak maliyetini ve geçidin içinde bulunduğu kategoriyi çevirdiğinde **garantiyle** ortalama neye mal olduklarını verir (bir çevirme piyangodur, bu yüzden şanslı bir pilot daha az, şanssız biri daha çok öder; garantinin izin verdiği en uzun çevirme dizisine kadar).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Geçit | Tamamlamak için parça | Çevirme başına parça şansı | Ortalama çevirme | Ortalama Thulium |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 13 | %13 | 99 | 9.851 |
| **Alpha Rift** | 14 | %4,33 | 318 | 31.825 |
| **Beta Breach** | 33 | %4,33 | 750 | 75.016 |
| **Gamma Foundry** | 68 | %4,33 | 1.546 | 154.579 |
| **Delta Siege** | 96 | %6,5 | 1.455 | 145.486 |
| **Omega Vault** | 119 | %6,5 | 1.803 | 180.343 |
| **Davidski's Nightmare** | 238 | %13 | 1.803 | 180.343 |

<!-- solo-parts:end -->

Chrono-Gate’in parçaları sıfırlamada sıfıra döner ve her sezon yeniden bulursun. **Solo geçitlerin parçaları kalır**, garantinin sayacı ile çevirmelere harcadığın ve geçitlerin geri ödediği tutarların kaydı da; sıfırlama bunların hiçbirini almaz ([Geçitler ve sıfırlama](#gates-and-the-wipe)).

### Parçasız bir çevirme {#a-spin-without-a-part}

Çevirmelerin çoğu parça bulmaz. Her biri, aşağıdaki şanslara göre seçilen bir ödül öder: ikinci çarpan ya da daha iyisinin lazer cephanesi, ikinci ya da üçüncü kademenin roket destesi ve ara sıra bir [özel eşya](/wiki/06-Items/Special-Items.md) ya da bir [konteyner](/wiki/06-Items/Containers.md). Verilemeyen bir ödül (örneğin özel eşyalar ya da konteynerler kapalıysa), aynı çekilişle bir cephane ya da roket destesine dönüşür; bu yüzden bir çevirme tablosundan asla daha az ödemez. Ödül, çevirmenin maliyetinden belirgin biçimde daha az değerlidir: geçitler bir Thulium lavabosudur.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Ödül | Çevirme başına şans |
| :--- | ---: |
| Bir konteyner: Chroma Archive | %0,01 |
| Bir özel eşya: Magic Hammer | %0,2 |
| Bir özel eşya: Schematics | %0,2 |
| Bir özel eşya: Philosopher's Stone | %0,2 |
| Bir özel eşya: Forger's Seal | %0,2 |
| Bir özel eşya: Workforce Contract | %0,2 |
| Bir özel eşya: Tinkerer's Badge | %0,1 |
| Lazer cephanesi: Advanced Plasma ×75 | %12,88 |
| Lazer cephanesi: Antimatter Battery I ×62 | %8,59 |
| Lazer cephanesi: Ultra Core ×40 | %8,59 |
| Lazer cephanesi: Antimatter Battery II ×29 | %4,29 |
| Lazer cephanesi: Dark Matter Ammo I ×31 | %4,29 |
| Lazer cephanesi: Experimental Fusion Core ×17 | %2,15 |
| Lazer cephanesi: Dark Matter Ammo II ×17 | %2,15 |
| Roketler: Lancet II ×4 | %8,59 |
| Roketler: Rivet II ×4 | %8,59 |
| Roketler: Ember II ×4 | %8,59 |
| Roketler: Scatter II ×4 | %8,59 |
| Roketler: Lancet III ×1 | %2,15 |
| Roketler: Rivet III ×1 | %2,15 |
| Roketler: Ember III ×1 | %2,15 |
| Roketler: Scatter III ×1 | %2,15 |

<!-- solo-prizes:end -->

## İçeri girmek {#going-in}

Bir geçidi Galaksi Geçitleri sayfasında **inşa edersin** ve portalından **sıçrayarak** girersin. İnşa istasyondan yapılır, gemin kenetliyken, uçuş sırasında da: araç çubuğundaki geçit düğmesinin açtığı **Galaksi Geçitleri penceresi** sayfa gibi çevirir, inşa eder ve hedefi seçer. Şunlar gerekir:

- geçidin parçaları: bunlar **inşa ederken bir kez** alınır ve reddedilen bir inşa hiçbir şey almaz;
- geçidin henüz inşa edilmemiş olması: **tüm** geçitleri aynı anda inşa edilmiş tutabilirsin, her birinin bir portalı olur ve aynı anda yalnızca birini oynarsın; inşa ettiğin bir geçide portalından yeniden girilir ya da geçit bırakılır, ancak sonra yeniden inşa edilebilir;
- ana sunucu (geçit yalnızca ana sunucuda inşa edilir: bölgesel bir sunucuda önce üsse dönersin).

İnşa edilen geçit, **ana sektöründe** (şirketine göre `M-1`, `T-1` ya da `G-1`) kendi adını taşıyan bir portal olarak durur ve Galaksi Geçitleri sayfası nerede olduğunu söyler. **Uçuşa çık, portala uç ve** diğer portallar gibi **sıçra**. İçeri girerken dünyanda boş bir yarık olmalı: her dünyada belli sayıda yarık vardır ve hepsi doluyken beklersin. Yalnızca **kendi** geçitlerini görürsün: aynı sektördeki diğer pilotların geçitlerinin portalları sana gösterilmez. Beş geçidin **hepsini aynı anda inşa edilmiş** tutabilirsin; her birinin kendi portalı vardır ve aynı anda yalnızca birini oynarsın: **bir arenadayken portallarından hiçbiri durmaz**, arenadan çıkınca geri gelirler.

**Bölgesel sunucularda (Singapore, US East).** İnşa edilmiş bir geçit orada da oynanır. Geçidinin portalı, ana sunucuda olduğu gibi bölgesel bir sunucuda da ana sektöründe durur ve vardığında sana haber verilir. **Ondan sıçra, o sunucunun bir arenasına girersin**; gecikme ana sunucunun değil, o sunucunun gecikmesidir. Bölgesel bir sunucuda her dünyada yalnızca **iki arena** vardır, ana sunucuda çok daha fazlası var; ikisi de doluysa, ana sunucuda boş bir yarık beklediğin gibi beklersin. Turunu, parçalarını ve ödemeni tutan tek yer yine ana sunucudur: ödeme, ana sunucu turu saydığında, yani bitişinden birkaç saniye sonra cüzdanına ulaşır ve **uçuş penceresindeki cüzdan yanaştığında yetişir**. Bir sonraki tura ancak son tur sayıldıktan sonra girersin. Arenada bıraktığın tura portaldan yeniden girilir; vazgeçmek istersen bunu arenada ya da istasyonda yaparsın. Bölgesel bir sunucunun arenası kapalıysa portalı seni bunun yerine ana sunucuya geri götürür; orada yukarıdaki gibi geçidine uçuşa çıkarsın. Bölgesel bir sunucuda başka nelerin çalıştığı [Sunucular](/wiki/03-Mechanics/Servers.md) sayfasında.

Boş bir arenanın ortasına tek başına inersin. İçeride kimse sana saldıramaz; Jump CPU ve Base CPU çalışmaz.

## Bir tur nasıl geçer {#how-a-run-goes}

1. **Her dalgadan önce bir geri sayım gelir**, ilk dalgadan ve patronunkinden önce de. Bir dalganın zamanlayıcısı yoktur, turun da yoktur: ihtiyacın olduğu kadar sürer.
2. **Bir dalga** çevrende bir halkada belirir ve geçidin temposunda sana uçar. Ondan aynı anda yalnızca bu kadarı canlıdır, kalanı yer bekler. Son uzaylısı öldüğünde biter.
3. **İlerlemen her dalgadan sonra kaydedilir.** Ayrılırsan, süren bir dalga döndüğünde baştan başlar.
4. **İsteğe bağlı bir dalga** devasa bir Seeker dalgasıdır; Delta Siege ve Omega Vault’un birer tane var. Geri sayımı sırasında atlayabilirsin: o zaman yapılmış sayılır ve **hiçbir şey** ödemez. Onunla savaşırsan öldürmeleri herhangi bir dalganınki gibi öder.
5. **Son dalga patrondur.** Gövdesi düştükçe faz değiştirir ve her değişimde bir an hasar alamaz. Patron öldüğünde tur tamamlanır ve tamamlama ödülü hemen ödenir.

**Canlar.** Bir ölüm bir can götürür ve seni, diğer ölümler gibi üssüne gönderir; tur sana saat işlemeden bekler. Tur açıkken ve sen arenanın dışındayken **inşa ettiğin her geçidin portalı ana sektöründe durur**; bunlardan birinden sıçramak, **Devam et** gibi seni kalan canlarınla kayıtlı dalgaya geri götürür ve yeni parça istemez. Son canın gittiğinde deneme biter ama tur son geçilen dalgada açık kalır ve yeniden girmek canlarını yeniler. **Ayrıl**, bir oturum kapatma ya da dünya değişimi turu can kaybetmeden duraklatır. Sunucunun yeniden başlatılması da turunu açık tutar. **Pes et**, turdan vazgeçmektir: parçaları gider ve öldürdüğün uzaylılar oldukları gibi ödenir. **Devam et** yalnızca uçan bir gemiyle çalışır: bir ölümden sonra sonuç ekranındaki düğmesi, nedenini söyleyen bir satırla birlikte, yeniden doğana kadar bekler. Yeniden doğan gemi sınırlı bir gövdeyle döner; gövden yarının altındaysa sonuç ekranı seni uyarır, **Devam et** yine de seni olduğun gibi geri götürür. Üssündeki onarım gemileri seni aurasının içinde onarır.

Her dünya aynı geçitle savaşır: uzaylıların gücü ve ödemesi uçtuğun dünyaya bağlı değildir.

### Dalgalar {#the-waves}

Uzaylılar oyundakilerdir (Seeker, Phantasm, Bulwark, Goombah ve Crystalys), geçit tarafından daha sert ya da daha yumuşak yapılmıştır. Planlanan süre, geçidin Lazer teknolojisi başlangıç seviyesindeki bir pilotu ne kadar uğraştıracak biçimde kurulduğudur ([Pilot Becerileri](/wiki/03-Mechanics/Pilot-Skills.md)); Lazer teknolojisini geliştirmiş bir pilot daha erken bitirir.

Bazı dalgalar bir **sürü** getirir: oyunun bir patron NPC'si (Boss Seeker, Boss Phantasm, Boss Goombah ya da Boss Crystalys) ve muhafızları, tek bir grup olarak saldırır. Bir sürünün her gemisi kendi dalgasının parçasıdır ve son gemi ölünce dalga biter. Dalganın diğer gemileri gibi öderler, [uzaylılar tablosundaki](#the-aliens) rakamlarla. **Bir patron NPC, oyunun sektörlerinde olduğu gibi ganimetini düşürür**: cevher, plaka, cephane ve roketler (her birinin ne düşürdüğü [sürülerin sayfalarında](/wiki/05-Swarms/Swarms.md) yazar). Bir geçitte toplanacak kutu yoktur: ganimet ödemeyle birlikte doğrudan envanterine gelir ve ödeme gibi tur başına yalnızca bir kez gelir. Muhafızları geçitte de sektörlerde de hiçbir şey düşürmez, patronlarını iyileştirmez ve geri gelmez. Aşağıdaki tablo, her geçidin hangi dalgalarının sürü getirdiğini söyler.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Geçit | Patronunki dahil dalgalar | Dalgalardaki uzaylılar | Patron NPC'ler ve sürüler | Patron | Planlanan süre |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | 5. dalga: 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10 ile 15 dk |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | 4. dalga: 2 Seeker Swarm; 9. dalga: 1 Phantasm Swarm | Enhanced Bulwark | 15 ile 25 dk |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | 4. dalga: 1 Phantasm Swarm; 9. dalga: 1 Goombah Swarm; 14. dalga: 1 Goombah Swarm | Elite Crystalys | 25 ile 35 dk |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | 5. dalga: 2 Phantasm Swarm; 10. dalga: 2 Goombah Swarm; 15. dalga: 1 Goombah Swarm; 20. dalga: 1 Crystalys Swarm | Siege Construct | 35 ile 45 dk |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | 6. dalga: 1 Goombah Swarm; 11. dalga: 2 Goombah Swarm; 16. dalga: 1 Crystalys Swarm; 22. dalga: 1 Phantasm Swarm | Omega Guardian | 50 ile 60 dk |
| **Davidski's Nightmare** | 13 | 50 Evil Protos, 66 Evil Kitefin, 31 Evil Ostirion, 19 Evil Nomad, 22 Evil Paragon, 7 Evil Storm, 8 Evil Wraith, 2 Evil Ironclad |  | Evil Davidski | 45 ile 60 dk |

- **Delta Siege**: 18. dalga (250 Seeker) isteğe bağlıdır: geri sayımı sürerken atlayabilirsin ve hiçbir şey ödemez
- **Omega Vault**: 17. dalga (250 Seeker) isteğe bağlıdır: geri sayımı sürerken atlayabilirsin ve hiçbir şey ödemez; 22. ile 24. dalgalar elittir; gövde, kalkan ve hasar ×1,5

<!-- solo-waves:end -->

### Patronlar {#the-bosses}

Bir patron, bir uzaylının büyütülmüş gemisidir; geçidin ya da dünyanın hiçbir ayarının değiştirmediği kendi gövdesi, kalkanı ve salvosu vardır. Patronun gövdesi tablodaki rakama düştüğünde bir faz başlar: kalkanı yeniden ayarlanabilir, salvosu ya da tüm hasarı değişir ve bir hamle başlatabilir. Her hamle duyurulur: bir daire, bir halka ya da geminin üstündeki bir işaret, düşmeden bir an önce gösterir. Bir patronun çağırdığı uzaylılar bir şey ödemez ve bir şey düşürmez.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Patron | Geçit | Gövde | Kalkan | Lazer salvosu |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330.000 | 530.000 | 5.700–7.000 |
| **Enhanced Bulwark** | Beta Breach | 690.000 | 170.000 | 4.500–5.500 |
| **Elite Crystalys** | Gamma Foundry | 620.000 | 250.000 | 3.800–4.700 |
| **Siege Construct** | Delta Siege | 1.150.000 | 1.730.000 | 3.400–4.200 |
| **Omega Guardian** | Omega Vault | 1.340.000 | 840.000 | 2.600–3.200 |
| **Evil Davidski** | Davidski's Nightmare | 550.000 | 660.000 | 2.600–3.200 |

| Patron | Faz | Kalan gövde | Ne yapar |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | %100 ile %0 | Yalnızca ateş eder. |
| **Enhanced Bulwark** | Shielded | %100 ile %50 | Kalkanı, patronun kendi kalkanının ×4 katına ayarlanır. |
|  | Second attack | %50 ile %0 | Salvosu ×1,3. Sana 4 adet Dormant Lance roketi atar, her biri 61.000, 0,5 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. |
| **Elite Crystalys** | Elite | %100 ile %50 | Yalnızca ateş eder. |
|  | Reinforced | %50 ile %0 | Kalkanı, patronun kendi kalkanının ×2 katına ayarlanır. 10 dk aralıkla 10 Goombah çağırır, en çok 10 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
| **Siege Construct** | Siege Construct | %100 ile %0 | 1 dk aralıkla 3 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 420 birim çevresindeki her şeye 5.500 vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. Sana 6 adet Dormant Lance roketi atar, her biri 9.000, 0,5 sn arayla; yaylım ateşi 1 dk aralıkla tekrarlanır. |
| **Omega Guardian** | Shield Fortress | %100 ile %70 | Kalkanı, patronun kendi kalkanının ×1,5 katına ayarlanır. 40 sn aralıkla 6 Bulwark çağırır, en çok 12 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
|  | Swarm Protocol | %70 ile %35 | 25 sn aralıkla 12 Phantasm çağırır, en çok 24 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. 30 sn aralıkla 140.000 vuran bir patlama patronun 700 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. |
|  | Overload | %35 ile %0 | Kalkanı, patronun kendi kalkanının ×0,1 katına ayarlanır. Tüm hasarı ×2,5. Fazda 2 dk geçince tüm hasarı bir ×2 daha olur. 25 sn aralıkla 28.000 vuran bir patlama patronun 700 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. |
| **Evil Davidski** | Evil Davidski | %100 ile %50 | Sana 6 adet Warden Rivet II roketi atar, her biri 4.900, 0,5 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. 1 dk aralıkla 2 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 400 birim çevresindeki her şeye 11.000 vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. 40 sn aralıkla 5 Evil Protos çağırır, en çok 10 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
|  | Angry | %50 ile %0 | Kalkanı, patronun kendi kalkanının ×0,5 katına ayarlanır. Tüm hasarı ×1,5. Fazda 8 dk geçince tüm hasarı bir ×2 daha olur. Sana 6 adet Warden Rivet III roketi atar, her biri 2.600, 0,4 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. 1 dk aralıkla 3 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 420 birim çevresindeki her şeye 3.400 vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. 45 sn aralıkla 35.000 vuran bir patlama patronun 700 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. 40 sn aralıkla 3 Evil Kitefin çağırır, en çok 6 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |

<!-- solo-bosses:end -->

## Bir tamamlama ne öder {#what-a-clear-pays}

Bir tamamlama tablosunu **bir kez**, patron öldüğü anda tek seferde öder: kredi, Thulium, deneyim ve onur, cevher, plakalar ve Power Core’lar, bir de cephane. Deneyim ve onur, bir zindanınkiler gibi PvE sıralama puanlarına sayılır.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Geçit | Kredi | Thulium | XP | Onur |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450.000 | 5.000 | 70.000 | 1.000 |
| **Beta Breach** | 1.500.000 | 12.000 | 180.000 | 2.500 |
| **Gamma Foundry** | 4.000.000 | 25.000 | 400.000 | 5.500 |
| **Delta Siege** | 8.000.000 | 40.000 | 800.000 | 10.000 |
| **Omega Vault** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |
| **Davidski's Nightmare** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400, Echo Shard ×4, Lattice Shard ×6; cephane: Advanced Plasma ×15.000, Ultra Core ×3.750, Experimental Fusion Core ×15.000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100, Echo Shard ×9, Lattice Shard ×13; cephane: Advanced Plasma ×37.500, Ultra Core ×15.000, Experimental Fusion Core ×22.500
- **Gamma Foundry**: Ship Fragment ×1.150, Nyxite ×1.000, Cataclysite ×900, Quorvium ×400, Power Core ×15, Echo Shard ×18, Lattice Shard ×27; cephane: Advanced Plasma ×22.500, Ultra Core ×45.000, Experimental Fusion Core ×37.500
- **Delta Siege**: Ship Fragment ×2.000, Nyxite ×1.750, Cataclysite ×1.500, Quorvium ×1.000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3, Echo Shard ×29, Lattice Shard ×44; cephane: Advanced Plasma ×30.000, Ultra Core ×67.500, Experimental Fusion Core ×56.250
- **Omega Vault**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; cephane: Advanced Plasma ×37.500, Ultra Core ×75.000, Experimental Fusion Core ×75.000
- **Davidski's Nightmare**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54; cephane: Advanced Plasma ×37.500, Ultra Core ×75.000, Experimental Fusion Core ×75.000
- **Heartshards**: Bir sezonda her geçidin ilk tamamlanmasında 1; ayrıca her tamamlamada %5 ihtimalle 1 tane daha.

<!-- solo-pay:end -->

**Thulium bir sınıra kırpılır.** Geçitler, çevirmelere harcadığın Thulium’un yalnızca bir payını geri ödeyebilir; bu pay tüm geçitlerin ve tüm çevirmelerin üzerinden sayılır (pay en üstteki listededir). Bir tamamlamanın ve uzaylılarının bunun üstünde ödeyeceği kısım kırpılır ve sonuç ekranı ne kadarını söyler. Kredi, deneyim, onur, cevher, plaka ve cephane asla kırpılmaz.

### Uzaylılar {#the-aliens}

Bir geçitte öldürdüğün her uzaylı, hangi dünyada uçarsan uç, Alpha’daki rakamlarıyla öder: hiçbir dünya çarpanı, booster ve Premium bonusu bunları değiştirmez. Bir dalga uzaylıları için bir tur boyunca **bir kez** öder, kaç kez çıkıp girersen gir. Ödeme, turun her kesiminin sonunda gelir: ayrıldığında, öldüğünde, canların bittiğinde, pes ettiğinde ya da tamamladığında. Bir kesimin öldürmeleri yalnızca sıfırlamada ve sen içerideyken sunucunun yeniden başlatılmasında ödenmeden kalır (turun açık kalır, ama o kesimin öldürmeleri kaybolur). Bir geçitteki öldürmeler, hiçbir sektör adlandırmayan [görevlere](/wiki/03-Mechanics/Quests.md#where-it-counts) (meydan okuma hattının büyük avları gibi) gerçekleştikleri anda sayılır (bir dalga bir tur boyunca onlara **bir kez** sayılır, tıpkı bir kez ödediği gibi) ve başka hiçbir şeye sayılmaz: öldürme istatistiklerine, başarımların sayaçlarına, öldürme akışına ya da dronelarının ve P.E.T.’lerinin deneyimine. Ama ödedikleri deneyim ve onur, bir tamamlamanın deneyimi ve onuru gibi PvE sıralama puanlarına sayılır. Uzaylıların ganimeti ödemeyle birlikte doğrudan envanterine gelir.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Uzaylı | Kredi | Thulium | XP | Onur |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1.000 | 4 | 100 | 2 |
| **Phantasm** | 3.000 | 12 | 300 | 6 |
| **Bulwark** | 5.000 | 25 | 800 | 10 |
| **Goombah** | 15.000 | 75 | 3.000 | 24 |
| **Crystalys** | 75.000 | 200 | 12.000 | 52 |
| **Boss Seeker** | 10.000 | 40 | 1.000 | 20 |
| **Seeker Slave** | 125 | 1 | 12 | 1 |
| **Boss Phantasm** | 39.000 | 195 | 7.800 | 62 |
| **Phantasm Guard** | 125 | 1 | 12 | 1 |
| **Boss Goombah** | 120.000 | 600 | 24.000 | 192 |
| **Goombah Guard** | 125 | 1 | 12 | 1 |
| **Boss Crystalys** | 393.750 | 1.050 | 63.000 | 273 |
| **Crystalys Guard** | 125 | 1 | 12 | 1 |
| **Evil Protos** | 4.250 | 17 | 725 | 6 |
| **Evil Kitefin** | 12.850 | 53 | 2.175 | 18 |
| **Evil Ostirion** | 34.350 | 141 | 5.800 | 48 |
| **Evil Nomad** | 59.600 | 245 | 10.060 | 84 |
| **Evil Paragon** | 68.700 | 283 | 11.600 | 97 |
| **Evil Storm** | 96.600 | 398 | 16.315 | 136 |
| **Evil Wraith** | 137.450 | 566 | 23.205 | 194 |
| **Evil Ironclad** | 268.450 | 1.105 | 45.330 | 379 |

| Geçit | Kredi | Thulium | XP | Onur |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514.000 | 2.099 | 55.296 | 1.018 |
| **Beta Breach** | 1.298.500 | 5.939 | 187.744 | 2.470 |
| **Gamma Foundry** | 3.064.500 | 13.693 | 541.944 | 4.696 |
| **Delta Siege** | 5.239.625 | 22.338 | 882.676 | 7.850 |
| **Omega Vault** | 7.088.125 | 29.196 | 1.196.828 | 10.022 |
| **Davidski's Nightmare** | 7.081.950 | 29.124 | 1.196.445 | 9.968 |

<!-- solo-kills:end -->

## Meydan okumalar ve başarımlar {#challenges-and-achievements}

İsteğe bağlı iki meydan okuma herhangi bir tamamlamada kazanılabilir ve her biri bir başarım öder, **Thulium ödemez**. **Ölümsüz** bir tamamlama, girdiğin tüm seferler boyunca bütün turda hiç ölmemiş olmandır. **Hız koşusu**, geçidin en kısa planlanan süresi içinde bir tamamlamadır ve arenanın içinde geçirdiğin süreyle sayılır. Diğer altı başarım her geçidi ve beşini birden tamamlamak içindir:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Yarık kapatıldı** (Sıradan): Alpha Rift’i tek başına tamamla.
- **Gedik mühürlendi** (Seyrek): Beta Breach’i tek başına tamamla.
- **Döküm hanesi durdu** (Nadir): Gamma Foundry’yi tek başına tamamla.
- **Kuşatma kırıldı** (Nadir): Delta Siege’i tek başına kır.
- **Kasa açıldı** (Destansı): Omega Vault’u tek başına aç.
- **Geçit Bekçisi** (Efsanevi): Beş solo geçidin hepsini tamamla: Alpha, Beta, Gamma, Delta ve Omega.
- **Dokunulmaz** (Nadir): Bir solo geçidi can kaybetmeden tamamla.
- **Zamana karşı** (Nadir): Bir solo geçidi en kısa süresi içinde ya da daha hızlı tamamla: Alpha’dan Omega’ya 10, 15, 25, 35 veya 50 dakika.

<!-- solo-achievements:end -->

## Bir geçitten eşyalar {#items-from-a-gate}

Bir geçidin sana verdiği her şey **satılabilir**: cevher, plakalar, Power Core’lar, cephane ve uzaylıların ganimeti, bir düşürme ya da görev ödülü gibi [Açık Artırma](/wiki/03-Mechanics/Auction.md)’da ilana konabilir; istisnalar da her eşyadakiyle aynıdır. Parçasız bir çevirmenin ödülleri öyle değildir: bir çevirmeden gelir, bir geçitten değil.

## Geçitler ve sıfırlama {#gates-and-the-wipe}

- **Sıfırlama açık her turu bitirir** ve parçalarını sana geri verir. Bir tur bir sonraki sezona devam etmez.
- **Sıfırlamada korunanlar:** beş solo geçidin parçaları, garantinin sayacı ve çevirmelere harcadığın ile geçitlerin geri ödediği tutarların kaydı; böylece Thulium sınırı sezonlar boyunca sürer. Başarımlar sonsuza dek senindir.
- **Sıfırlamada kaybedilenler:** Chrono-Gate’in parçaları, eskisi gibi. Çevirmelerin onları yeniden satın alır.
- **Bir hesabı silmek** parçaları, sayacı ve kaydı siler.
