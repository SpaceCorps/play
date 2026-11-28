<!-- wiki-i18n source: b4ceac9f501a1ec2 -->
<!-- wiki-i18n title: Solo Geçitler -->
# Solo Geçitler {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; davidski's nightmare; nightmare; evil davidski; angry davidski; evil ships; golden ships; solo geçitler; solo geçit; galaksi geçitleri; geçit parçası; parça; parçalar; enerji maddeleştirici; çevirme; garanti; dalga; dalgalar; can; devam et; pes et; ölümsüz; meydan okuma; başarım; thulium sınırı; evil gemileri; altın gemiler; öfkeli davidski -->

**Solo geçitler**, Galaksi Geçitleri’nin tek başına uçtuğun beş geçididir: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** ve **Omega Vault**. Her biri kendine ait boş bir arenadır; orada uzaylı dalgaları sana birbiri ardına gelir ve sonda bir patron bekler. **Davidski's Nightmare** bu beşinden ayrı, altıncı bir geçittir: dalgaları uzaylılar değil, sana karşı uçan oyun gemileri olan **Evil gemileridir** ve inşa etmesi en pahalı geçittir. Bir geçidi **parçalarıyla** inşa edersin; parçaları Enerji Maddeleştirici’yi Thulium ile çevirerek bulursun, bir tamamlama da kredi, Thulium, deneyim, onur, cevher, plaka ve cephane öder.

Bir solo geçit bir [klan zindanı](/wiki/03-Mechanics/Dungeons.md) değildir. Zindan, bir klanın bir grup için açtığı, sonunda bir Savaş Lordu bulunan labirenttir; solo geçit ise yalnızca senin bulunduğun bir arenadır ve kimse seninle birlikte giremez. İkisinin kuralları, ödemeleri ve sınırları ayrıdır. Galaksi Geçitleri sayfasında ayrıca **Chrono-Gate** vardır; o uçulacak bir yer değil, sıfırlama için [Nakliye Deposu](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)’nu açan geçittir: parçaları aynı çevirmelerle bulunur.

## Bir bakışta {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Geçitler**: 7: Chrono-Gate ve 6 solo geçit, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault ve Davidski's Nightmare
- **Çevirme**: Her çevirme için 100 Thulium ve bir seferde 1, 5, 10, 100 ya da 1.000 çevirme
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

**Galaksi Geçitleri** sayfasını aç ve Enerji Maddeleştirici’yi çevir. Her çevirme Thulium ile ödenir ve en çok bir parça bulur. Önce bir **kategori** seç: **Chrono-Gate**, **Alpha–Gamma** (Alpha Rift, Beta Breach ve Gamma Foundry), **Delta–Omega** (Delta Siege ve Omega Vault) ya da kendine ait bir kategorisi olan **Davidski's Nightmare**. Parça bulma şansı her kategoride aynıdır ve parça, seçtiğin kategorinin geçitlerinden birine aittir; hepsi eşit olasılıklıdır. Bir geçidi inşa etmek için ondan belli sayıda parça gerekir ve parçalar sen kullanana kadar senindir. Parça bulmayan bir çevirme boşa gitmez: bir ödül öder ([aşağıda](#a-spin-without-a-part)). Her çevirme ücretlendirilir. Chrono-Gate tamamlandığında seçeneği kapanır, çünkü içinde bulunacak bir şey kalmaz; diğer iki kategori şansını korur, yani bir solo geçidin parçası Chrono-Gate varken de yokken de aynı maliyettedir.

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

Uzaylılar oyundakilerdir (Seeker, Phantasm, Bulwark, Goombah ve Crystalys), geçit tarafından daha sert ya da daha yumuşak yapılmıştır. **Davidski's Nightmare**’in dalgaları bunun yerine **Evil gemileridir**: bir pilotun uçabileceği her gövde için bir tane, Dormant sürüsünün rengiyle. Önce küçük gövdeler gelir ve her dalga bunlardan daha fazlasını ve daha büyüklerini getirir; patrondan önceki son dalgaya kadar böyle sürer. Bir Evil gemisi, bir pilotun gemisinin taşıdığını taşır: lazerler, sana birkaç saniyede bir attığı bir **roket** ve hiçbir şey ona vurmazken gövdesini onaran bir **onarım dronu**; yani rahat bıraktığın bir gemi iyileşir. Planlanan süre, geçidin Lazer teknolojisi başlangıç seviyesindeki bir pilotu ne kadar uğraştıracak biçimde kurulduğudur ([Pilot Becerileri](/wiki/03-Mechanics/Pilot-Skills.md)); Lazer teknolojisini geliştirmiş bir pilot daha erken bitirir.

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

**Evil Davidski**, Davidski's Nightmare’in patronudur; Davidski’nin kendi Ironclad’ını daha koyu bir altın renkte uçurur. Uzun bir mesafe boyunca seni izleyen güdümlü roketler olan Dormant Lance atar ve meteorlar, bir halka ve çağırdığı Evil gemileriyle savaşır. Gövdesi üçte bire indiğinde **Öfkeli Davidski** olur: teması çalar, daha sert vurur ve çevresinde **oyundaki her geminin altın bir gemisi** belirir. Altın gemilerden biri bile hayattayken ona hiçbir şekilde zarar verilemez: lazerlerin ve roketlerin ona kilitlenemez ve yaptığın hiçbir şey gövdesine ya da kalkanına dokunmaz, bu yüzden önce onları aşarsın. Sonuncusu düştüğünde koruma kalıcı olarak kalkar. Her dalganın başında kendi penceresinden seninle alay eder. Onu öldürmek, bir Davidski öldürmesi isteyen görevler için, Tehlike Sektörleri’nde olduğu gibi bir geçitte de sayılır. Güncel olmayan bir oyun geçidi göstermez.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Patron | Geçit | Gövde | Kalkan | Lazer salvosu |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | {{guide:vitals.hull@Enhanced Phantasm}} | {{guide:vitals.shield@Enhanced Phantasm}} | {{guide:vitals.dps*0.9007633587786259~1.099236641221374@Enhanced Phantasm}} |
| **Enhanced Bulwark** | Beta Breach | {{guide:vitals.hull@Enhanced Bulwark}} | {{guide:vitals.shield@Enhanced Bulwark}} | {{guide:vitals.dps*0.9019607843137255~1.0980392156862746@Enhanced Bulwark}} |
| **Elite Crystalys** | Gamma Foundry | {{guide:vitals.hull@Elite Crystalys}} | {{guide:vitals.shield@Elite Crystalys}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Elite Crystalys}} |
| **Siege Construct** | Delta Siege | {{guide:vitals.hull@Siege Construct}} | {{guide:vitals.shield@Siege Construct}} | {{guide:vitals.dps*0.8974358974358975~1.1025641025641026@Siege Construct}} |
| **Omega Guardian** | Omega Vault | {{guide:vitals.hull@Omega Guardian}} | {{guide:vitals.shield@Omega Guardian}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Omega Guardian}} |
| **Evil Davidski** | Davidski's Nightmare | {{guide:vitals.hull@Evil Davidski}} | {{guide:vitals.shield@Evil Davidski}} | {{guide:vitals.dps*0.896551724137931~1.103448275862069@Evil Davidski}} |

| Patron | Faz | Kalan gövde | Ne yapar |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | %100 ile %66 | Yalnızca ateş eder. |
|  | Reinforced | %66 ile %33 | Kalkanı, patronun kendi kalkanının ×1 katına ayarlanır. 10 dk aralıkla 4 Phantasm çağırır, en çok 4 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
|  | Second attack | %33 ile %0 | Salvosu ×1,3. 30 sn aralıkla {{guide:behaviour.ability:phases.ringBlast@Enhanced Phantasm}} vuran bir patlama patronun 500 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. |
| **Enhanced Bulwark** | Shielded | %100 ile %66 | Kalkanı, patronun kendi kalkanının ×4 katına ayarlanır. |
|  | Rocket barrage | %66 ile %33 | Sana 4 adet Dormant Lance roketi atar, her biri {{guide:behaviour.ability:phases.rocketBarrage@Enhanced Bulwark}}, 0,5 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. |
|  | Second attack | %33 ile %0 | Salvosu ×1,3. 10 dk aralıkla 4 Phantasm çağırır, en çok 4 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
| **Elite Crystalys** | Elite | %100 ile %66 | Yalnızca ateş eder. |
|  | Renewed shield | %66 ile %33 | Kalkanı, patronun kendi kalkanının ×1 katına ayarlanır. |
|  | Reinforced | %33 ile %0 | Kalkanı, patronun kendi kalkanının ×2 katına ayarlanır. 10 dk aralıkla 10 Goombah çağırır, en çok 10 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
| **Siege Construct** | Siege Construct | %100 ile %66 | 1 dk aralıkla 3 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 420 birim çevresindeki her şeye {{guide:behaviour.ability:phases.meteors@Siege Construct}} vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. |
|  | Rocket barrage | %66 ile %33 | 1 dk aralıkla 3 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 420 birim çevresindeki her şeye {{guide:behaviour.ability:phases.meteors2@Siege Construct}} vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. Sana 6 adet Dormant Lance roketi atar, her biri {{guide:behaviour.ability:phases.rocketBarrage@Siege Construct}}, 0,5 sn arayla; yaylım ateşi 1 dk aralıkla tekrarlanır. |
|  | Frenzy | %33 ile %0 | 30 sn aralıkla 3 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 420 birim çevresindeki her şeye {{guide:behaviour.ability:phases.meteors3@Siege Construct}} vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. Sana 6 adet Dormant Lance roketi atar, her biri {{guide:behaviour.ability:phases.rocketBarrage2@Siege Construct}}, 0,5 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. |
| **Omega Guardian** | Shield Fortress | %100 ile %66 | Kalkanı, patronun kendi kalkanının ×1,5 katına ayarlanır. 40 sn aralıkla 6 Bulwark çağırır, en çok 12 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
|  | Swarm Protocol | %66 ile %33 | 25 sn aralıkla 12 Phantasm çağırır, en çok 24 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. 30 sn aralıkla {{guide:behaviour.ability:phases.ringBlast@Omega Guardian}} vuran bir patlama patronun 700 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. |
|  | Overload | %33 ile %0 | Kalkanı, patronun kendi kalkanının ×0,1 katına ayarlanır. Tüm hasarı ×2,5. Fazda 2 dk geçince tüm hasarı bir ×2 daha olur. 25 sn aralıkla {{guide:behaviour.ability:phases.ringBlast2@Omega Guardian}} vuran bir patlama patronun 700 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. |
| **Evil Davidski** | Evil Davidski | %100 ile %66 | Yalnızca ateş eder. |
|  | Davidski attacks | %66 ile %33 | Sana 6 adet Dormant Lance roketi atar, her biri {{guide:behaviour.ability:phases.rocketBarrage@Evil Davidski}}, 0,5 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. 1 dk aralıkla 2 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 400 birim çevresindeki her şeye {{guide:behaviour.ability:phases.meteors@Evil Davidski}} vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. 40 sn aralıkla 5 Evil Protos çağırır, en çok 10 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |
|  | Angry | %33 ile %0 | Kalkanı, patronun kendi kalkanının ×0,5 katına ayarlanır. Tüm hasarı ×1,5. Fazda 8 dk geçince tüm hasarı bir ×2 daha olur. Sana 6 adet Dormant Lance roketi atar, her biri {{guide:behaviour.ability:phases.rocketBarrage2@Evil Davidski}}, 0,4 sn arayla; yaylım ateşi 30 sn aralıkla tekrarlanır. 1 dk aralıkla 3 kez, her seferinde 8 meteor bırakır; her biri düştüğü yerin 420 birim çevresindeki her şeye {{guide:behaviour.ability:phases.meteors2@Evil Davidski}} vurur, bunların %50 kadarı sana nişanlıdır; her daire düşmeden 3 sn önce görünür. 45 sn aralıkla {{guide:behaviour.ability:phases.ringBlast@Evil Davidski}} vuran bir patlama patronun 700 birim çevresindeki her şeye isabet eder; halka düşmeden 2 sn önce görünür. 40 sn aralıkla 3 Evil Kitefin çağırır, en çok 6 tanesi canlı; bir şey ödemezler ve bir şey düşürmezler. |

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
| **Seeker** | {{guide:spoils.pay.credits@Seeker#1}} | {{guide:spoils.pay.thulium@Seeker#1}} | {{guide:spoils.pay.experience@Seeker#1}} | {{guide:spoils.pay.honor@Seeker#1}} |
| **Phantasm** | {{guide:spoils.pay.credits@Phantasm#1}} | {{guide:spoils.pay.thulium@Phantasm#1}} | {{guide:spoils.pay.experience@Phantasm#1}} | {{guide:spoils.pay.honor@Phantasm#1}} |
| **Bulwark** | {{guide:spoils.pay.credits@Bulwark#1}} | {{guide:spoils.pay.thulium@Bulwark#1}} | {{guide:spoils.pay.experience@Bulwark#1}} | {{guide:spoils.pay.honor@Bulwark#1}} |
| **Goombah** | {{guide:spoils.pay.credits@Goombah#1}} | {{guide:spoils.pay.thulium@Goombah#1}} | {{guide:spoils.pay.experience@Goombah#1}} | {{guide:spoils.pay.honor@Goombah#1}} |
| **Crystalys** | {{guide:spoils.pay.credits@Crystalys#1}} | {{guide:spoils.pay.thulium@Crystalys#1}} | {{guide:spoils.pay.experience@Crystalys#1}} | {{guide:spoils.pay.honor@Crystalys#1}} |
| **Boss Seeker** | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#1}} |
| **Seeker Slave** | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#1}} |
| **Boss Phantasm** | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#1}} |
| **Phantasm Guard** | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#1}} |
| **Boss Goombah** | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#1}} |
| **Goombah Guard** | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#1}} |
| **Boss Crystalys** | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#1}} |
| **Crystalys Guard** | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#1}} |
| **Evil Protos** | {{guide:spoils.pay.credits@Evil Protos}} | {{guide:spoils.pay.thulium@Evil Protos}} | {{guide:spoils.pay.experience@Evil Protos}} | {{guide:spoils.pay.honor@Evil Protos}} |
| **Evil Kitefin** | {{guide:spoils.pay.credits@Evil Kitefin}} | {{guide:spoils.pay.thulium@Evil Kitefin}} | {{guide:spoils.pay.experience@Evil Kitefin}} | {{guide:spoils.pay.honor@Evil Kitefin}} |
| **Evil Ostirion** | {{guide:spoils.pay.credits@Evil Ostirion}} | {{guide:spoils.pay.thulium@Evil Ostirion}} | {{guide:spoils.pay.experience@Evil Ostirion}} | {{guide:spoils.pay.honor@Evil Ostirion}} |
| **Evil Nomad** | {{guide:spoils.pay.credits@Evil Nomad}} | {{guide:spoils.pay.thulium@Evil Nomad}} | {{guide:spoils.pay.experience@Evil Nomad}} | {{guide:spoils.pay.honor@Evil Nomad}} |
| **Evil Paragon** | {{guide:spoils.pay.credits@Evil Paragon}} | {{guide:spoils.pay.thulium@Evil Paragon}} | {{guide:spoils.pay.experience@Evil Paragon}} | {{guide:spoils.pay.honor@Evil Paragon}} |
| **Evil Storm** | {{guide:spoils.pay.credits@Evil Storm}} | {{guide:spoils.pay.thulium@Evil Storm}} | {{guide:spoils.pay.experience@Evil Storm}} | {{guide:spoils.pay.honor@Evil Storm}} |
| **Evil Wraith** | {{guide:spoils.pay.credits@Evil Wraith}} | {{guide:spoils.pay.thulium@Evil Wraith}} | {{guide:spoils.pay.experience@Evil Wraith}} | {{guide:spoils.pay.honor@Evil Wraith}} |
| **Evil Ironclad** | {{guide:spoils.pay.credits@Evil Ironclad}} | {{guide:spoils.pay.thulium@Evil Ironclad}} | {{guide:spoils.pay.experience@Evil Ironclad}} | {{guide:spoils.pay.honor@Evil Ironclad}} |

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
