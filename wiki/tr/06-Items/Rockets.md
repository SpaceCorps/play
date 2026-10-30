<!-- wiki-i18n source: ad50226a5328bd83 -->
<!-- wiki-i18n title: Roketler -->
# Roketler {#rockets}

Roketler, lazerlerinin yanında ikinci bir silahtır: birkaç saniyede bir yapılan ve bir lazer salvosundan çok daha sert vuran tek bir atış. Dört türde, her türde üç kademe olmak üzere on iki roket vardır; bunlara yalnızca Montaj’ın ürettiği iki roket daha eklenir. Hangisini fırlatırsan fırlat hepsi **3 saniyelik tek bir ortak dolum sayacını** paylaşır (yalnızca Montaj’ın ürettiği iki roket, uzun uçuşları yüzünden biraz daha uzun bekler). Sıradan ve Nadir roketler **kredi** ile, dört Destansı roket **Thulium** ile satın alınır. Bir [dron formasyonu](/wiki/03-Mechanics/Formations.md) bir roketin hasarını artırabilir ve bu sayacı uzatabilir ya da kısaltabilir: bkz. [Dron formasyonları ve roketler](#drone-formations-and-rockets).

## Bir dakikada {#in-one-minute}

- **Satın alınacak on iki roket.** Dört tür (Lancet, Rivet, Ember, Scatter), her birinde üç kademe. Sıradan ve Nadir olanlar kredi, Destansı olanlar Thulium tutar. İki roket daha, N.U.K.E. ve N.I.K.E., Montaj’da üretilir.
- **Her roket hasarını rastgele belirler.** Fırlattığında oyun, roketin en düşük ve en yüksek hasarı arasından bir sayı seçer (bir Lancet I için 1.700 ile 2.100 arası). Gemin, lazerlerin, amfilerin ve boosterların hiçbir şeyi değiştirmez, yalnızca bir dron formasyonu değiştirir. Uzaylıların attığı roketler rastgele hasar vermez: sabit bir sayı verirler ([Uzaylılara karşı](#against-the-aliens)).
- **Patlamalar ortada en güçlüdür.** Ember ve Scatter roketleri patlar ve halkanın içindeki her gemiye zarar verir: merkezde sayının tamamı, kenarda yarısı.
- **Hepsi için tek sayaç.** Hangi roket olursa olsun, her fırlatmadan sonra bir sonrakine kadar 3 saniye beklersin. Yalnızca N.U.K.E. ve N.I.K.E. daha uzun bekletir (4,1 ve 4,6 saniye), çünkü havada o kadar kalırlar.
- **Güdümlü ya da düz.** Güdümlü bir roket (Lancet, Ember) seçtiğin bir hedef ister. Düz olan (Rivet, Scatter) imlecinin gösterdiği yere uçar.
- **Daha fazlası roket gibi taşınır.** **EMP Charge** bir sarf malzemesidir: envanterinde bir yığın olarak durur, kısayol çubuğundan kullanılır ve hiçbir yuvaya takılmaz ([EMP Charge](#emp-charge)). İki **Energetic Wall** da öyledir ([Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall)).

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Eşya ağacı {#item-tree}

Her Montaj ürünü önce kendi teknolojisini ister; araştırmanın ne kadar sürdüğünü görmek için bir eşyanın üzerine gel. Teknoloji ağacı, yakıt ve hızlandırma: [Araştırma](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
Energetic Wall I | consumable, uncommon | buy 250 Thulium | /wiki/06-Items/Extras.md#energetic-wall
EMP Charge | consumable, uncommon | buy 500 Thulium | /wiki/06-Items/Rockets.md#emp-charge
Energetic Wall II | consumable, rare | craft 600 Thulium, 120 s | research 21600 s, 21600 science | 5 Ship Fragment, 1 Power Core | /wiki/06-Items/Extras.md#energetic-wall

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
Energetic Wall I -> Energetic Wall II
```
<!-- item-tree:end -->

## Dört tür {#the-four-kinds}

| | Tek hedef: tek bir gemiye vurur | Alan hasarı: patlar, yakındaki her şeye zarar verir |
| :--- | :--- | :--- |
| **Güdümlü**: seçtiğin hedefe kilitlenir ve peşinden gider | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Düz**: imlecine doğru uçar | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Her tür, Sıradan roketinin adını taşıyan bir **ailedir** ve kademe bir Roma rakamıdır: **Lancet I**, **Lancet II** ve **Lancet III** sırasıyla Sıradan, Nadir ve Destansı güdümlü tek hedefli roketlerdir; Rivet, Ember ve Scatter aileleri de aynı şekilde ilerler. Bir roketin Roketler seçicisindeki ve hangardaki kutucuğunda yazan kodu, ailesinin üç harfi ile rakamıdır (LNC II, RVT III, EMB I, SCT II); yalnızca üretimle gelen iki roket adlarını ve kodlarını korur (N.U.K.E., NUK; N.I.K.E., NIK).

- **Güdümlü** roketler, ayrılırken **kilitlenme menzili** içinde seçili bir hedef ister. Sınırlı bir dönüş hızıyla hedefin peşinden giderler; bu yüzden uzaktaki hızlı bir gemi ucuz bir roketten kaçabilir. Hedef ölür, ayrılır ya da güvenli bölgeye ulaşırsa roket düz uçmaya devam eder ve başka bir hedef seçmez.
- **Düz** roketler hedef istemez ve seçili hedefi yok sayar: her zaman uçuş görünümünde **imlecinin** altındaki noktaya doğru uçarlar. **Düz bir roketi kurmak için yuvasına tıkla** (yuva beyaz bir çerçeve ve bir nişangâh alır, fare imlecin de uzayın üzerinde nişangâha dönüşür), sonra **uzayda bir yere tıkla**: roket tıkladığın noktaya doğru uçar ve gemin olduğu yerde kalır. Esc, sağ tık veya aynı yuvaya yeniden tıklamak kurmayı iptal eder. Roketler hâlâ yeniden doluyorsa tıklama yalnızca bunu söyler ve roket kurulu kalır. Sayı tuşları ve **Roket fırlat** tuşu, imlecin uçuş görünümünde en son bulunduğu noktaya doğru hemen ateşler; imleç henüz oraya gelmediyse geminin **baktığı** yöne uçarlar. Düz uçtukları için hızla yandan geçen bir gemi onlardan kaçabilir.
- **Tek hedefli** bir roket, vurabileceği ilk gemiye vurur (güdümlü olan yalnızca hedefine). **Alan hasarlı** bir roket, karşılaştığı ilk geminin yanında, nişan aldığın noktada ya da uçuşunun bittiği yerde patlar ve **patlama yarıçapı** içindeki her gemiye zarar verir: merkezde hasarın tamamı, kenarda yarısı. Patlamanın haritada çizdiği halka, erişiminin tam sınırıdır.
- **Asteroitler.** Bir [asteroite](/wiki/03-Mechanics/Asteroid-Mining.md) ateşlenen güdümlü roket ona doğru uçar; düz bir roket her hedefte olduğu gibi imlecine uçar ve imleç asteroitin üzerindeyse asteroiti kırar. Herhangi bir roketin yoluna çıkan ilk asteroit onu durdurur, arkasındaki gemi yerine vuruşu kendisi alır ([Siper](/wiki/03-Mechanics/Asteroid-Mining.md#cover)). Bir [Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall) bir roketi aynı şekilde durdurur; N.I.K.E. onun üzerinden uçar. Mağaza’daki on iki roket ve N.U.K.E. bir asteroiti kırabilir; N.I.K.E. bir asteroite ateşlenemez ve asteroitlerin üzerinden uçar. Lazerler de asteroitlere zarar verir, ama bir gemiye verdiklerinin yalnızca %5’i kadar: bu iş için araç roketlerdir.

## On iki roket {#the-twelve-rockets}

Her roketin **kendine ait, fırlattığında belirlenen bir hasarı** vardır: en düşük sayısından en yüksek sayısına kadar herhangi bir değer; tablo ikisini ve ortalamayı gösterir. Hasar geminden, lazerlerinden ve amfilerinden, boosterlarından, cephanenden ya da dronlarından etkilenmez ve bir roket asla kritik vurmaz. Yalnızca bir **dron formasyonu** onu değiştirir: buradaki tablo formasyonsuz hasarı verir (bkz. [Dron formasyonları ve roketler](#drone-formations-and-rockets)). Tek hedefli bir roket, belirlediği hasarı vurduğu gemiye verir; bir patlama bir kez belirler ve bunu **içindeki her gemiye** verir: merkezde sayının tamamını, kenarda yarısını. *Kalkan delme*, o vuruş için hedefinin soğurmasından düşülür (bir geminin soğurması, kalkanlarının bir vuruştan aldığı paydır; bkz. [Kalkan mekaniği](/wiki/03-Mechanics/Shields.md#shield-penetration)): bir Lancet III roketinin %35’i, %80 soğurmalı bir geminin kalkanlarına vuruşun %45’ini bırakır ve geri kalan %55’i gövdeye gönderir. Patlamanın kalkan delmesi yoktur.

| Ad | Tür | Nadirlik | Hasar | Ortalama | Kalkan delme | Patlama yarıçapı | Kilitlenme menzili | Menzil | Hız | Fiyat | Taşıma sınırı |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Güdümlü, tek hedef | Sıradan | 1.700–2.100 | 1.900 | %10 | – | 700 | 1.040 | 520 | 500 kredi | 5.000 |
| **Lancet II** | Güdümlü, tek hedef | Nadir | 3.500–4.200 | 3.850 | %25 | – | 1.000 | 1.584 | 660 | 800 kredi | 2.000 |
| **Lancet III** | Güdümlü, tek hedef | Destansı | 5.200–6.200 | 5.700 | %35 | – | 1.300 | 2.296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Düz, tek hedef | Sıradan | 2.200–2.700 | 2.450 | %5 | – | – | 1.080 | 900 | 500 kredi | 5.000 |
| **Rivet II** | Düz, tek hedef | Nadir | 4.500–5.250 | 4.875 | %25 | – | – | 1.120 | 700 | 800 kredi | 2.000 |
| **Rivet III** | Düz, tek hedef | Destansı | 7.000–8.000 | 7.500 | %35 | – | – | 1.100 | 500 | 5 Thulium | 500 |
| **Ember I** | Güdümlü, alan hasarı | Sıradan | 1.200–1.400 | 1.300 | – | 170 | 700 | 1.000 | 500 | 500 kredi | 5.000 |
| **Ember II** | Güdümlü, alan hasarı | Nadir | 2.400–2.900 | 2.650 | – | 230 | 920 | 1.500 | 600 | 800 kredi | 2.000 |
| **Ember III** | Güdümlü, alan hasarı | Destansı | 3.500–4.500 | 4.000 | – | 300 | 1.150 | 2.030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Düz, alan hasarı | Sıradan | 1.500–1.750 | 1.625 | – | 210 | – | 1.088 | 640 | 500 kredi | 5.000 |
| **Scatter II** | Düz, alan hasarı | Nadir | 3.000–3.500 | 3.250 | – | 290 | – | 1.080 | 540 | 800 kredi | 2.000 |
| **Scatter III** | Düz, alan hasarı | Destansı | 4.500–5.500 | 5.000 | – | 400 | – | 1.092 | 420 | 5 Thulium | 500 |

Kademe ne kadar pahalıysa roket o kadar sert vurur, o kadar uzağa erişir, kalkan delmesi o kadar yüksektir ve o kadar az taşıyabilirsin; pahalı olanlar, tuttukları bedele göre en çok hasarı da verir. Düz bir roket, aynı fiyata, kendi kademesi ve türündeki güdümlü rokete göre dörtte bir ile üçte bir arası fazla hasar verir (ortalamada %23 ile %32), çünkü onu nişanlamak zorundasın. Bir patlama, kendi kademesi ve türündeki tek hedefli roketin yaklaşık üçte ikisi kadar hasar verir (ortalamada %66 ile %70: Ember ile Lancet ailesi, Scatter ile Rivet ailesi arasında), ama kapsadığı her gemiye. Patlamadaki hasar merkezde tamdır ve düz bir çizgide **kenarda yarısına** düşer: gövdesi yarı yolda olan bir gemi %75 alır, gövdesi halkanın dışında kalan bir gemi hiç hasar almaz. Ortalamada bir fırlatma, aralığının ortasını, yani en yüksek sayısının %89 ile %94’ünü verir ve aşağıda roketleri sayan tablo bunu kullanır.

## Ne kadara mal olurlar {#what-they-cost}

Her türde Sıradan bir roket 500 kredi, Nadir bir roket 800 kredi, Destansı bir roket 5 Thulium tutar. Her sayaç dolduğunda ateşlenirse bu, Sıradan bir roket için dakikada 10.000 kredi, Nadir bir roket için 16.000, Destansı bir roket için 100 Thulium eder; Ostirion gemisinin üç lazerinin x1 cephanede dakikada yaktığı 900 kredinin karşısında. Dolu bir yığın: 5.000 Sıradan roket (2.500.000 kredi), 2.000 Nadir roket (1.600.000 kredi) veya 500 Destansı roket (2.500 Thulium). Bu sınıra kadar dilediğin kadar satın alabilirsin; bir roketin *taşıma sınırı*, kaç tane tutabileceğinin tek sınırıdır. Sıfırlamada on iki roketin her birinden en fazla 1.000 tanesini hiçbir şey yapmadan korursun; bunun üstündeki kısım ile her N.U.K.E. ve N.I.K.E. yalnızca Nakliye Deposu’nda hayatta kalır; orada bir roket 1 kg, bir N.U.K.E. ya da N.I.K.E. 250 kg gelir: bkz. [sıfırlama](/wiki/03-Mechanics/Wipe-Timeline.md#ammo-and-rockets). 3 saniyede bir roket, dakikada yalnızca yirmi eder; bu yüzden roket, lazerlerinin üstüne eklenen bir darbedir: ucuzlar zayıf uzaylılar için, pahalılar büyük çatışmalar için. Bir roket satın alırken ya da ona teklif verirken, [pazarda](/wiki/03-Mechanics/Auction.md#limits) listelediklerin ve orada önde olduğun lotlar bu sınıra dahildir. Bunlar temel sayılardır: Pilot araştırması Sealed Backdoor ([Araştırma](/wiki/03-Mechanics/Research.md#pilot-technologies)) her roketin sınırını senin için toplamda %25, %50, %100, %150 ya da %200 artırır, aşağı yuvarlanarak; böylece 5.000, I. seviyede 6.250, V. seviyede 15.000 olur.

Mağaza roketleri tür tür listeler, her tür kendi adının altında: önce Sıradan roket, en sonda Destansı olan; hangar, Nakliye Deposu ve Roketler seçicisi aynı sırayı kullanır.

## Uzaylılara karşı {#against-the-aliens}

Bir uzaylıyı öldürmek için gereken roket sayısı, tür tür ve her roketin hasar aralığının ortasını verdiği varsayılarak hesaplanır (Alpha Dünyası; Beta ve Gamma dünyalarındaki uzaylılar 1,5 ve 2 kat güçlüdür). Bir patlama, yanında patladığı geminin aldığı kadar sayılır, yani merkezin biraz altında (merkez hasarının %87 ile %93’ü). Bir uzaylının kalkanı bir vuruşun %80’ini alır, roketin kalkan delmesi düşülür. En düşük hasarda bir öldürme, tablonun söylediğinden en fazla %15 daha fazla roket ister (Goombah için Lancet I 43 değil 48 roket gerektirir), en yüksek hasarda en fazla %13 daha az (39). Rivet II, Lancet III ve Rivet III, bir Phantasm uzaylısını hangi hasar çıkarsa çıksın tek vuruşta öldürür; Rivet I, 2.600 ve üzeri çıkan hasarda iki, altında üç roket ister.

| Öldürmek için gereken roket | Seeker (1.600) | Phantasm (5.200) | Bulwark (26.000) | Goombah (80.000) | Crystalys (416.000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 14 | 43 | 219 |
| **Lancet II** | 1 | 2 | 7 | 19 | 109 |
| **Lancet III** | 1 | 1 | 5 | 11 | 73 |
| **Rivet I** | 1 | 3 | 11 | 33 | 170 |
| **Rivet II** | 1 | 1 | 6 | 15 | 86 |
| **Rivet III** | 1 | 1 | 4 | 8 | 56 |
| **Ember I** | 2 | 5 | 24 | 71 | 369 |
| **Ember II** | 1 | 3 | 12 | 34 | 177 |
| **Ember III** | 1 | 2 | 8 | 23 | 116 |
| **Scatter I** | 2 | 4 | 18 | 56 | 287 |
| **Scatter II** | 1 | 2 | 9 | 27 | 141 |
| **Scatter III** | 1 | 2 | 6 | 18 | 90 |

- **Sıradan** tek hedefli roketler, Seeker uzaylısını hangi hasar çıkarsa çıksın tek vuruşta, Phantasm uzaylısını üç vuruşta öldürür (bir Lancet I, en düşük hasarda dördüncüye ihtiyaç duyar); ilk sektörlerin gündelik roketleridir. **Nadir** olanlar Bulwark ve Goombah içindir: yedi Lancet II roketi bir Bulwark uzaylısını yaklaşık 20 saniyelik sayaçta devirir. **Destansı** tek hedefliler bir Goombah uzaylısını sekiz (Rivet III) ile on bir (Lancet III) roketle öldürür. Birkaç uzaylı birbirine yakınken patlamalar bedelini çıkarır: beş Phantasm uzaylısından oluşan bir kümenin (hepsi nişan aldığın uzaylıya 250 birim içinde) üzerinde patlayan bir Scatter III, tek atışta kümeye toplam yaklaşık 21.000 hasar verir.
- Yalnızca roketlerle öldürmek gerçek bir harcamadır, zengin olmanın yolu değil: tek hedefli bir roketin bedeli, öldürmenin ödediği tutarın (kredi ve tanesi 200 kredi olan Thulium) %15’i (Phantasm uzaylısına karşı Rivet II) ile %95’i (Crystalys uzaylısına karşı Lancet I) arasındadır; güçlü uzaylılara karşı zayıf patlamalar ise öldürmenin ödediğinden fazlasına mal olur (Bulwark uzaylısına karşı Ember I: %120). **Crystalys** uzaylısını tek bir türle öldürmek 56 ile 369 roket ve yaklaşık üç dakikalık sayaç ister; 500 adetlik dolu bir Destansı yığını dört ile sekiz Crystalys uzaylısını öldürmeye yeter. En güçlü uzaylı için bir plan gerekir: lazerlerin x2 cephaneyle, ilk saniyeden itibaren 3 saniyede bir orta kademe bir roket ve ani darbe olarak aşağıdaki büyük roketler.
- Bir öldürmenin ödemesi, nasıl yapılmış olursa olsun aynıdır (en büyüğü için bkz. [Crystalys](/wiki/04-Aliens/Crystalys.md)); bu yüzden roketle öldürmek, sana zaman kazandırıyor ve ödediğinden az tutuyorsa değer.
- **Uzaylılar da roket fırlatır.** [Sürülerin](/wiki/05-Swarms/Swarms.md) Pirate Boss, Dormant Force ve Dormant Pulse gemileri ile [klanların](/wiki/03-Mechanics/Clans.md#clan-wardens) Siege Warden uzaylıları, kendilerine saldıran pilota, formasyonunun değiştirmediği kendi sayaçlarıyla (sürüler için 5 saniye, Siege Warden uzaylıları için 8 ile 24) düz Rivet roketleri atar. **Bir uzaylının roketi rastgele hasar vermez ve yukarıdaki aralıkları kullanmaz**: sabit 2.500 (Rivet I), 5.000 (Rivet II) veya 7.500 (Rivet III) hasar verir; uzaylıların 1,5 ve 2 kat güçlü olduğu Beta ve Gamma dünyalarında daha fazla (bir Clan Warden roketi her dünyada aynıdır). Hareket etmeye devam eden bir gemi onlardan kaçar. Sürülerin patronları kutularında roket de bırakır.

## Yalnızca üretilen roketler {#the-craft-only-rockets}

İki roket Mağaza’da yoktur. Onları **Montaj** üretir ve aşağıdaki her kurala uyarlar (ortak sayaç, güvenli bölgeler, şirketin). En yüksek sayılarının **%90 ile %100’ü** arasında bir hasar belirlerler; bu, on ikisininkinden daha dar bir banttır, bu yüzden aşağıda tek vuruşta yok ettikleri şeyler en düşük hasarda da geçerlidir. İkisi de düz roketlerdir: her düz roket gibi imlecinin altındaki noktaya doğru uçarlar (oyun, ne seçili olursa olsun imlecin yönünü gönderir; yalnızca yön göndermeyen eski bir 0.4.3 istemcisinde sunucu onları seçili hedefe, o yoksa imlecinin altındaki noktaya, o da yoksa geminin baktığı yöne uçurur).

| Ad | Tür | Nadirlik | Hasar | Kalkan delme | Patlama yarıçapı | Menzil | Hız | Taşıma sınırı | Üretim malzemeleri |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Düz, alan hasarı | Efsanevi | 45.000–50.000 | – | 900 | 1.200 | 300 | 10 | Her üretimde 1 N.U.K.E.: 150.000 kredi, 3.000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Düz, tek hedef | Mitik | 67.500–75.000 | %35 | – | 4.050 | 900 | 20 | Her üretimde 5 N.I.K.E.: 100.000 kredi, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: oyundaki en büyük patlama. 900 birimlik bir patlama; Scatter III roketinin 400’ünün iki katı erişim ve beş katı alan: içindeki her gemiye merkezde 45.000 ile 50.000, kenarda bunun yarısı, yani 22.500 ile 25.000 hasar verir. Yavaştır (havada dört saniye). Tek bir N.U.K.E., patlamasının tamamındaki her Seeker ve Phantasm uzaylısını yok eder; patlama noktasının 830 birim (en yüksek hasarda 934) yakınındaki, yani neredeyse tüm alandaki her Bulwark uzaylısını da yok eder; bir Goombah uzaylısının yarısından fazlasını, bir Crystalys uzaylısının dokuzda birini götürür. Pilotlara karşı eldeki en büyük vuruştur: bkz. aşağıdaki kurallar. Haritadaki halka tam erişimidir.
- **N.I.K.E.**: bir Rivet I gibi tek hedefli bir roket; 67.500 ile 75.000 hasar ve %35 kalkan delmesi: **dokunduğu ilk gemiye vurur ve onda harcanır.** Aynı zamanda [Dark Matter](/wiki/03-Mechanics/Black-Hole.md) üreten roket de odur: Tehlike Sektörü 4’ün ortasındaki kara deliğe ateşlenirse olay ufkunu geçerken yutulur ve delik karşılığında Dark Matter verir. 4.050 birimi 4,5 saniyede uçar: onu radyasyonun kenarı ile merkezden 4.380 birim arasındaki herhangi bir yerden ateşle. Daha uzaktan ateşlenirse kısa kalır ve boşa gider. Beş N.I.K.E. yaklaşık on Dark Matter üretir.
- **Tuzak.** Yolunda bir gemiyle, hattın üzerinde bekleyen bir rakiple ya da zarar verebileceği başka bir şeyle karşılaşan bir N.I.K.E. ona 67.500 ile 75.000 hasar verir ve harcanır: kara delik hiçbir şey almaz, sen de almazsın. Deliğin halkasının içinde yanlışlıkla vurabileceği başka bir şey dolaşmaz (uzaylılar ve şirket pilotları oradan uzak durur): yalnızca Dark Matter için içeri girmiş ya da seni kenarda bekleyen pilotlar. Kendi şirketinin gemilerinin, güvenli bölgedeki gemilerin ve henüz zarar veremeyeceğin gemilerin içinden geçer. Ateşledikten sonra haritadan çıkarsan, kimseye zarar vermeden uçmaya devam eder ve yine de Dark Matter üretir.
- Montaj, kuyruğa aldıkların dahil elindeki sayıyı bir roketin *taşıma sınırının* üstüne çıkaracak bir üretimi başlatmaz. Sealed Backdoor bunların sınırlarını da artırır (I. seviyede 10, 12 olur ve 20, 25 olur; V. seviyede 30 ve 60).

## Fırlatma {#firing}

1. Roketleri Mağaza’dan (**Roketler** kategorisi) her birinin *taşıma sınırına* kadar satın al: Sıradan ve Nadir olanlar için kredi, Destansı olanlar için Thulium.
2. Kısayol çubuğunun üstündeki **Roketler** düğmesini aç ve istediklerini yuvalara sürükle. Seçici her tür için bir sütun, her kademe için bir satır gösterir, her birinde taşıdığın miktarla. Altlarında kendilerine ait bir satır vardır: N.U.K.E. ve N.I.K.E. için **Özel · yalnızca üretim** (hiç taşımadığın olanı küçük bir çekiç işaretler).
3. Yuvanın tuşuna bas. **Güdümlü** bir roketin yuvasına tıklamak onu seçili hedefe ateşler; **düz** bir roketin yuvasına tıklamak onu kurar ve uzayda bir sonraki tıklaman onu oraya ateşler. **Roket fırlat** tuşu (varsayılan `R`, Ayarlar › Kontroller’den değiştirilebilir) en son fırlattığın roketi ya da çubuktaki ilkini ateşler.
4. Bir sonraki fırlatmaya kadarki 3 saniye boyunca (N.U.K.E. sonrası 4,1, N.I.K.E. sonrası 4,6) **her** roket yuvasının üzerinde dairesel bir sayaç döner, ortasında kalan saniyeyle. O sırada basmak yalnızca roketlerin yeniden dolduğunu söyler (son saniyenin onda birinde basmak yine ateşler). Bir dron formasyonu beklemeyi 2,19 ile 4,05 saniye arasında herhangi bir değere getirebilir (aşağıya bak).

Sayılarını görmek için bir roket yuvasının üzerine gel (en düşük ve en yüksek hasarını; Mağaza ve hangar da aynısını söyler) ve uçuş görünümünde kilitlenme halkasını (seçili hedef menzildeyken yeşil) ya da çizgisini ve patlama dairesini gör. **Sana** kilitlenmiş bir roket ekranının kenarını kırmızı yakıp söndürür.

**N.U.K.E.**, ateşlemeden önce patlamasını haritada çizer (nişan aldığın noktada 900 birimlik daire) ve patladığında görünümün üzerinde beyaz bir parlama, yaklaşık bir saniyede tam erişimine kadar yayılan ve iki saniye daha kalan bir halka, mantar gibi yükselen bir bulut ve ne kadar yakınsan o kadar güçlü bir kamera sarsıntısı verir. **Ekran sarsıntısını azalt** sarsıntıyı kaldırır, **Hareketi azalt** ise parlamayı ışığının yarısından azıyla saniyenin üçte birine kısaltır (ikisi de Ayarlar’daki Grafik bölümündedir); düşük parçacık kalitesi bulutu inceltir ve kıvılcımları bırakır, parlamayı ya da halkayı asla. **N.I.K.E.**, bir Rivet I gibi, geminden imlecine uzanan çizgiyle nişanlanır ve oyun onu kara delikten uzak olduğu ya da deliği olmayan bir haritada olduğu için asla reddetmez: nereye gideceğine sen karar verirsin. Kartında hasarının yanında **Kara delik: Dark Matter üretir** yazar. Etrafında kıvrılan kıvılcımlarla mor bir iz bırakır; karşılaştığı bir gemi vuruşu her roket gibi alır, bunun yerine ufku geçerse delik parlar.

## Dron formasyonları ve roketler {#drone-formations-and-rockets}

Kuşandığın bir [dron formasyonu](/wiki/03-Mechanics/Formations.md), bir roketi değiştiren tek şeydir. Bu sayfadaki her hasar rakamı formasyonsuz bir gemi içindir.

- **Hasar.** Ballista (+%55), Bodkin (+%29) ve Asterism (+%24) formasyonlarının roket bonusu, N.U.K.E. ve N.I.K.E. dahil 14 roketin tamamının hasarını çarpar. Testudo formasyonunun tüm hasar bedeli roketlerde de geçerlidir, Culler formasyonunun uzaylılara hasarı ise bir uzaylıya isabet eden rokette geçerlidir. Bir roket üzerindeki tüm çarpanlar birlikte ×1,59’da durur. Bonus, bir gemiye olduğu gibi bir [asteroite](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one) karşı da geçerlidir ve asteroitin zırhı ondan sonra düşülür.
- **Yeniden doldurma.** Asterism ortak sayacı %35 uzatır (4,05 saniye), Cordon %11 uzatır (3,33), Redoubt %27 kısaltır (2,19); ama asla roketin uçuş süresine kısa bir an eklenmiş değerin altına inmez. Redoubt altında hızlı roketler (Lancet I, Rivet I ve II, Ember I, Scatter I ve II) 2,19 saniye bekler, bir Rivet III 2,3, bir Lancet III 2,9 ve bir Ember III tam 3 saniye; N.U.K.E. ve N.I.K.E., ne kuşanırsan kuşan 4,1 ve 4,6 saniye bekler. Bekleme ateşlediğin anda belirlenir, bu yüzden sonradan formasyon değiştirmek onu kısaltmaz ve roket yuvalarının üzerindeki sayaç onu izler.
- **Büyük ikilinin sınırları korunur.** En iyi formasyonla bir N.I.K.E. en çok 116.250 vurur; bunu tam gövdeli bir Paragon gemisi (128.000) atlatır. Bir N.U.K.E. ise en çok 77.500 vurur; bunu da bir Goombah uzaylısı (80.000) atlatır.
- **Kaçınma.** Asterism formasyonunun %7 kaçınması, sana isabet eden doğrudan bir roketin hiç hasar vermeme şansını %7 yapar ve geminin üzerinde yüzen bir “Iska” görünür; alan hasarlı bir patlamanın nişanı yoktur ve asla savuşturulmaz.
- **Kalkan delme.** Gemini 15 puanını, Stiletto da 35 puanlık roket delmesini doğrudan bir roketin kalkan delmesine ekler (patlamanın delmesi yoktur), sınır olmadan: Stiletto ile bir Lancet III %70, Gemini ile %50’dir. Bir lazer vuruşu Gemini’ninkini cephanesininkine ve amfilerininkine aynı şekilde ekler, Stiletto’nunkinden ise hiçbir şey almaz ([Lazerler ve cephane](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

## Kurallar {#rules}

- Bir roket fırlatmak için **takılı lazer gerekmez** ve lazerlerin onun verdiği hasarı ya da erişimini değiştirmez: güdümlü bir roket kendi kilitlenme menzilindeki bir hedefe kilitlenir, düz bir roket kendi mesafesini uçar. Takılı lazer yokken hangardaki Menzil göstergesi bir çizgi gösterir ve yalnızca roketlerini ateşleyebilirsin.
- Her fırlatmada bir roket harcanır, isabet etsin etmesin.
- Roketler lazerlerin kurallarına uyar: **güvenli bölge** içindeki hiçbir şeye zarar verilmez, **Barış Protokolü** bitmeden ya da bir sektörün PvP’yi yasakladığı yerde hiçbir pilota zarar verilmez ve **kendi şirketin ile kendi grubun**, doğrudan ya da patlama olsun, roketlerinden asla zarar görmez.
- Bir roket fırlatmak kendi güvenli bölge korumanı hemen bitirir. Bu bir atıştır: kendi **gizlenmeni** de bitirir ve Cloaking CPU, bir gizlenmenin her bitişinden sonra olduğu gibi bir dakika boyunca yeniden dolar. Gizli olsan da olmasan da fırlatma, ardından gelen 10 saniye boyunca gizlenmeni engeller (bkz. [Ekstralar](/wiki/06-Items/Extras.md)).
- **Gizlenmiş** ya da **3 saniyelik EMP süresi** içinde olan bir gemiye kilitlenilemez: güdümlü bir roket reddedilir, ona doğru uçmakta olan bir roket de kilidini kaybeder ve düz uçmaya devam eder. Düz tek hedefli bir roket böyle bir geminin içinden geçer. **Alan hasarlı bir patlama** kilit gerektirmez; bu yüzden kapsadığı gemilere, gizli olsun olmasın zarar verir ve bir gizlenmeyi bitirir (bkz. [Ekstralar](/wiki/06-Items/Extras.md)).
- **Bir roketin bir pilota yaptığı hasarı hiçbir şey sınırlamaz.** Başka bir pilotun gemisi hasarın tamamını alır: önce kalkan (soğurması eksi roketin kalkan delmesi), sonra gövde. Küçük gemiler dayanmaz. Standart kalkan çekirdeklerinde (Light, %45 soğurma) bir N.I.K.E., yeni bir Protos, Kitefin ya da Ostirion gemisini hangi hasar çıkarsa çıksın tek vuruşta yok eder (bir Paragon gemisi gövdesinin %47 ile %53’ünü, bir Wraith gemisi yaklaşık beşte birini kaybeder) ve bir N.U.K.E., bir Protos gemisini patlamasının her yerinde, bir Kitefin gemisini patlama noktasının yaklaşık 50 birim (en yüksek hasarda 220) yakınında yok eder, daha büyük hiçbir gemiyi tek patlamada yok etmez. İki Lancet III ya da iki Rivet III roketi bir Protos gemisini hangi hasar çıkarsa çıksın yok eder; bir Wraith gemisi için 45 ile 70 tanesi gerekir. Bir pilot ile bir roket arasında duran şeyler Barış Protokolü, güvenli bölgeler ve şirketindir. Bu rakamlar formasyonsuz bir gemi içindir; bir roket formasyonu bunları en fazla %55 artırır (bkz. [Dron formasyonları ve roketler](#drone-formations-and-rockets)).
- Bir uzaylıyı yalnızca bir roketin **doğrudan isabeti** sahiplenir (bkz. [Savaş](/wiki/03-Mechanics/Combat.md)); bir patlamanın kenarı, sahiplenilmiş bir uzaylıya onu çalmadan zarar verebilir. Bir patlamanın zarar verdiği her uzaylı, uyuyan da dahil, tıpkı lazer vuruşunda olduğu gibi sana döner (yalnızca karşılık veren Seeker ve Goombah dahil); patlamanın ıskaladığı uzaylı uyumaya devam eder.
- Sayaç senindir: bir sıçramadan, yeniden bağlanmadan, gemi değiştirmeden ve yok edilen bir gemiden sağ çıkar.

İlk tablodaki on iki roket satın alınır (Sıradan ve Nadir olanlar kredi, Destansı olanlar Thulium ile); N.U.K.E. ve N.I.K.E. üretilir.

Ayrıca bkz.: [Lazerler ve cephane](/wiki/06-Items/Lasers.md), [Savaş](/wiki/03-Mechanics/Combat.md), [Kara delik](/wiki/03-Mechanics/Black-Hole.md).

## EMP Charge

**EMP Charge** bir roket gibi taşınır ama roket değildir: bir **sarf malzemesidir**. Mağaza’dan tanesi **500 Thulium** karşılığında satın alırsın ve tek bir yığında en fazla **20** tane taşırsın ([Açık Artırma](/wiki/03-Mechanics/Auction.md)’da listelediklerin de sayılır); kısayol çubuğunun **Sarf Malzemeleri** seçicisi onu taşıdığın sayıyla gösterir. Hiçbir gemide **yuva kaplamaz**; 0.4.21’e kadar bir [ekstra](/wiki/06-Items/Extras.md) eşyaydı ve her adet bir ekstra yuvayı doldururdu. Tanesi Nakliye Deposu’nda 250 ağırlığındadır.

Bir çatışmada EMP yuvasına bas. **3 saniye** boyunca kimse sana kilitlenemez ve sana kilitlenmiş olan **herkes kilidini hemen kaybeder**, nerede olurlarsa olsunlar: pilotlar, uzaylılar ve şirket pilotları. Kilidi kopan bir pilota “Kilitlenme kayboldu: hedef EMP kullandı” denir. Bu 3 saniyede kilitlenmeye çalışan biri reddedilir.

- **Dokunulmazlık değildir.** Kilit gerektiren şeyleri durdurur: lazerler, güdümlü roketler ve içinden geçip giden düz bir tek hedefli roketin dokunuşu. **Alan hasarlı bir patlama** kilit gerektirmez; bu yüzden içindeysen yine de sana zarar verir ve kara delik hiç de bir atış değildir.
- **Yine de hareket edebilirsin.** Ateş etmek onu bitirmez. Gizlenebilir (gizlenmenin kendi kuralları izin veriyorsa), roket fırlatabilir ve ekstraları kullanabilirsin.
- **Yakınındaki gizlenmeleri bitirir.** Darbe patladığında sana **1.500 birim** içinde gizlenmiş her gemi hemen görünür olur ve CPU’sunun 60 saniyelik yeniden dolumu başlar; hangi şirkete ait olursa olsun, seninki de dahil; kendi [grubunun](/wiki/03-Mechanics/Groups.md) gemileri istisnadır: gizlenmelerini korurlar. Pilota “Gizlenme bozuldu: yakınlarda bir EMP patladı.” denir, geminin her gizlenme bitişindeki dalgalanmayla yeniden belirdiğini görür ve yuva yeniden dolmaya başlar. Kendin gizliyken EMP kullanamazsın.
- **Hiçbir şeyi gizlemez.** Herkes seni yine görür; 3 saniye boyunca çevrende çıtırdayan elektrikli bir kabukla.
- Bir güvenli bölge seni korurken, gizliyken ya da sonuncusundan sonraki **30 saniye** içinde **kullanamazsın**. Başka her yerde çalışır; bir sezonun ilk günleri de dahil (Barış Protokolü): uzaylılar o zaman da avlanır.
- Bu 3 saniye içinde vurduğun bir uzaylı, süre bitene kadar sana dönmez. Öldürme sahiplenmelerin ve ilk vuruş kuralları değişmez.
- **Ne görürsün.** Bükülmüş uzaydan bir darbe, darbenin gizlenmeleri bitirdiği mesafeye kadar (1.500 birim) pilotun etrafından yayılır, menzildeki herkes onu görür ve 3 saniye boyunca etrafını çıtırdayan elektrikli bir kabuk sarar; kendi geminin çevresinde bir halka ve ekranın üstünde süreyi sayan bir gösterge vardır. Seni seçmiş olan herkesin hedef halkası kısa bir elektrik çarpmasıyla dağılır. EMP yuvası taşıdığın adedi gösterir, kabuk dururken mavi yanar ve yeniden dolarken kararır.
- **Bir basış, bir adet.** Bir basış yığınından bir adet harcar; hiç kalmadıysa reddedilir (“EMP Charge kalmadı.”). Nakliye Deposu’ndaki adetler sonraki sezonun adetleridir ve kullanılamaz. Kendiliğinden aktarılan on iki roketin (her birinden 1.000) aksine, taşıdığın adetler sezonla birlikte kaybolur; onları Nakliye Deposu’na koymadıkça. **30 saniyelik** yeniden dolum kaydedilmez: oyundan çıkmak ya da bir portaldan sıçramak onu sıfırlar ve sonraki darbe bir adede mal olur.
