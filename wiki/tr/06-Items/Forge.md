<!-- wiki-i18n source: a46d76b8a1130eb4 -->
<!-- wiki-i18n title: Demirhane -->
# Demirhane {#the-forge}

<!-- wiki-search: forge; demirhane; kademe yükselt; kademe yükseltme; kademe; kademeler; yuva; yuvalar; sockets; ayarla; ayar; yeniden düzenle; yeniden düzenleme; shard; shardlar; echo; echo shard; lattice; lattice shard; heartshard; bütünlük; çatlak; çatlaklar; onar; onarım; birleştirme; birleştir; füzyon; tainted; godly; rupturing; eternal; lekeli; ilahi; patlayan; ebedi; awakened; resonant; radiant; ascendant; uyanmış; rezonanslı; parlak; yücelmiş; tinkerer's badge -->

**Demirhane**, Montaj sayfasının (ve uçuştaki Montaj penceresinin) ikinci sekmesidir. Sahip olduğun ekipmanla üç şey yapar: kredi ve uzaylı ganimeti karşılığında **bir eşyayı bir kademe yükseltir**, Shard’larla **yuvalarını ayarlar** (bonusları buradan gelir) ve bir eşyanın **iki kopyasını**, ikisinin de en iyisini koruyan tek eşyada **birleştirir**. Bir kademe yükseltme asla başarısız olmaz ve Demirhane bir eşyaya yeni bir bonusu ancak sen onu bir tekliften seçtiğinde koyar. (0.5.7’den önce kademeler Lekeli, İlahi, Patlayan ve Ebedi diye anılırdı ve bir adım başarısız olabilirdi; artık Uyanmış, Rezonanslı, Parlak ve Yücelmiş diye anılıyor.) Beş özdeş eşya isteyen ve sonucu %25’lik bir şansa bırakan eski Füzyon Odası’nın yerini aldı.

## Neler dövülebilir {#what-can-be-forged}

Lazerler, lazer amfileri, kalkan çekirdekleri, kalkan hücreleri, motorlar, iticiler, Uyarlanabilir Çekirdekler, Repair Drone eşyaları ve [Gövde Kaplaması](/wiki/06-Items/Hull-Plating.md): [büyüleme bonusları](/wiki/06-Items/Overview.md) taşıyabilen her tek ekipman parçası. Envanterinde, bir gemide (orada kalır ve yeni kademesiyle hemen çalışır) ya da başka bir eşyaya takılı olabilir. Dronlar, gemiler, cephane, kaynaklar ve boosterlar dövülemez; Nakliye Deposu’ndaki ya da Skylab’ındaki Motor veya Savunma Modülü’ne takılı hiçbir şey de dövülemez: önce çıkar.

Ekipman listesinde, kademe ve tür filtrelerinin yanında bir **Tümü / Takılı / Envanterde** anahtarı vardır. **Takılı**, bir gemide ya da başka bir eşyaya takılı olanları, **Envanterde** boşta duranları gösterir; başlığın altındaki bir satır anahtarın kaç parçayı gizlediğini söyler. Bir birleştirmenin donörünü seçerken Takılı duraklatılır, çünkü donör boşta olmalıdır.

Tür filtresinin yanındaki **Gemi** açılır listesi yalnızca gemilerinden birindeki parçaları gösterir (başka bir eşyaya takılı parça, taşıyıcısının bulunduğu gemiye sayılır). “Envanterde” seçiliyken ve bir birleştirmenin donörünü seçerken duraklatılır. Parçanın üzerine gelince açılan kart, panelin başlığı ve birleştirmenin ana parçası nerede olduğunu söyler: *Kitefin gemisinde, konfigürasyon 1* (Hull Plating için iki konfigürasyon da) ve neye takılı olduğu. **Ctrl+F** (Mac’te Cmd+F) imleci Montaj’ın başlığındaki arama kutusuna koyar; açık sekmenin listesini daraltır (tarifler ürettiği ve istediği şeylere, ekipman ad, tür ve kademeye göre) ve Esc onu temizler. Panel, *Uyanık yuvalar* satırının altında parçanın bir özelliği bonus taşımak için çok düşükse bunu söyler; Impulse Thruster’ın bir, Momentum Thruster’ın iki bonus taşımasının sebebi budur.

## Kademe yükselt {#tier-up}

Bir eşya seç; panel eşyanın kademesini, ulaşacağı kademeyi, bunun neyi değiştirdiğini (kaç bonus taşıyabileceği ve bonusların ne kadar büyük olduğu) ve fiyatı, her parçadan elinde ne kadar olduğuyla birlikte gösterir: yeterliyse yeşil, değilse kırmızı ve kaç eksiğin olduğu. Hepsi elindeyse **Kademe yükselt** eşyayı tam bir kademe yükseltir. Atlama yoktur: Yücelmiş kademeye ulaşmak için bir eşya Uyanmış, Rezonanslı ve Parlak kademelerinden geçer, her birinin kendi fiyatı vardır.

| Adım | Kredi | Thulium | Malzemeler |
| :--- | :---: | :---: | :--- |
| Standart → Uyanmış | 10.000 | – | 5 Ship Fragment, 15 Daraxium |
| Uyanmış → Rezonanslı | 56.000 | – | 32 Ship Fragment, 48 Nyxite |
| Rezonanslı → Parlak | 267.000 | – | 23 Reinforced Hull Plate, 140 Cataclysite, 2 Dark Matter Plate |
| Parlak → Yücelmiş | 833.000 | 2.667 | 11 Power Core, 320 Quorvium, 2 Dark Matter Plate |

- **Malzemeler** boştaki yığınlarından gelir: bir gemideki eşyalar ve Nakliye Deposu’ndaki yığınlar kullanılmaz. Eksik olanlar depodaysa panel bunu söyler.
- **Bir adım her zaman başarılı olur.** Maliyeti, Demirhane’de yuvalar yokken bir adımın ortalama maliyetidir ve eşyada bir yuvayı daha uyandırır ([Kademeye göre bonuslar](#buffs-by-tier) bölümüne bak).
- **Commerce becerin**, bir adımın kredisini ve Thulium’unu, ayrıca bir birleştirmenin kredisini 100. seviyede %15’e kadar düşürür ([Pilot Becerileri](/wiki/03-Mechanics/Pilot-Skills.md)). Tablo ilk seviyedeki fiyatı, panel ise senin ödediğin fiyatı gösterir; malzemeler değişmez.
- **Eşyanın sahip olduğu her bonus,** yeni kademenin aralığında yeniden belirlenir ve daha iyi değeri korur. Sonuç panelin üstünde gösterilir; eşya seçili kalır, böylece sonraki adımı zaten ekrandadır.
- Kademe yükseltme anlıktır.
- **Yuvalar adımın altındadır.** Kademe yükselt ve [Yuvalar](#sockets) tek bir görünümdür, **Geliştir**, önce Kademe yükselt gelir: bir adımın uyandırdığı yuva, listede düğmenin hemen altındadır ve Ayarla düğmesi de oradadır; onu kullanmak için başka yere geçmen gerekmez.
- **Bir Tinkerer’s Badge** (bir [özel eşya](/wiki/06-Items/Special-Items.md#tinkerers-badge)) bir parçayı kredisiz, Thulium’suz ve malzemesiz bir kademe yükseltir, Standart’tan itibaren. Hiçbir şeye mal olmayan bir adımdır: bir yuvayı uyandırır ve parçanın taşıdığı bonusları, ücretli bir adım gibi, yeniden çeker.

### Dark Matter Plate {#dark-matter-plates}

Son iki adım, her şeyin üstüne her biri **2 Dark Matter Plate** ister. Bir plaka [Montaj](/wiki/06-Items/Overview.md)’da **5 Dark Matter, 1 Velkonite Reinforced Plate ve 1 Orvium Reinforced Plate** ile (250 Thulium, 2 dakika) preslenir; bu yüzden bir adım 10 Dark Matter, 2 Velkonite plakası ve 2 Orvium plakası ister. Dark Matter [kara delikten](/wiki/03-Mechanics/Black-Hole.md) gelir: yaklaşık beş N.I.K.E. roketi (bkz. [Roketler](/wiki/06-Items/Rockets.md)) on tane eder; yolunda bir gemiyle karşılaşan bir N.I.K.E. onun yerine o gemiye vurur ve hiç üretmez. Plakalar diğer malzemeler gibi boştaki yığınlarından kullanılır ve eksiğin varsa panel adlarını söyler. Her yükseltme zincirinin son kademesi de plaka ister, her biri için 4 ([Dark Matter ve Dark Matter plakaları](/wiki/03-Mechanics/Dark-Matter.md)).

### Kademeye göre bonuslar {#buffs-by-tier}

| Kademe | En fazla taşınan bonus | Her bonusun büyüklüğü | Adımın kristali |
| :--- | :---: | :---: | :--- |
| Uyanmış | 1 | +%2 ile +%5 | Daraxium |
| Rezonanslı | 2 | +%4 ile +%8 | Nyxite |
| Parlak | 3 | +%6 ile +%11 | Cataclysite |
| Yücelmiş | 4 | +%9 ile +%15 | Quorvium |

Demirhane’den önce üretilen ekipman, belirlendiği bonusları korur ve bunlar çoğu zaman tablodan küçüktür (o dönemden kalma Rezonanslı bir parça +%2 taşıyabilir). Onları kendiliğinden hiçbir şey yükseltmez: bir kademe yükseltme her bonusu yeni kademenin aralığında yeniden belirler ve daha iyi değeri korur, bir birleştirme her özelliğin daha iyi değerini korur.

Bir eşya, özellik sayısından fazla bonus taşıyamaz: kalkan çekirdeği için dört, lazer için üç, motor ya da Uyarlanabilir Çekirdek için iki, Momentum Thruster için iki, Impulse Thruster için bir (1,017 ile 1,03 arasındaki çarpanı bir bonusa değmeyecek kadar küçüktür ve Demirhane 1,05 veya daha düşük bir çarpana bonus çıkarmaz; bu yüzden bonusu yalnızca sabit hızda olabilir), Crit Amp I, Repair Drone ya da Hull Plating için bir (gövdesi), daha yüksek kademeli Crit Amp eşyaları için iki, Damage Amp eşyaları ve kalkan hücreleri için üç. Sonraki kademe eşyanın taşıyabileceğinden fazla bonus taşımıyorsa panel bunu söyler: o zaman kademe yalnızca bonusları güçlendirir. Menzil bonusları +%5’i asla geçmez. Penetration Amp tek özellikli olduğundan tek bonus taşır.

**Bir kademe en fazla bu kadar bonus taşır.** Her kademe yükseltmesi eşyada bir yuvayı uyandırır, adımın kristaline karşılık gelen yuvayı: Daraxium birincisini, Nyxite ikincisini, Cataclysite üçüncüsünü, Quorvium dördüncüsünü uyandırır. Bir eşyanın, kademesinin taşıdığı ve eşyanın özelliği olduğu kadar yuvası vardır: Rezonanslı kademedeki bir kalkan çekirdeğinin ikisi, Yücelmiş kademedekinin dördü de vardır; iki özelliği olan bir motorun ise uyandırılacak üçüncü bir yuvası yoktur. Bir bonus, onu bir Echo Shard ile ayarladığında ve tekliften seçtiğinde yuvaya girer. Bir **birleştirme**, iki kopyanın her özelliğindeki en iyi bonusu kademenin sınırına kadar korur.

Bir **kalkanın Soğurma bonusu** (ve bir kalkan hücresinin Soğurma artışı) özelliği çarpar; bu yüzden [soğurmadan](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) ona orantılı puan değerindedir: bir Heavy Shield Core eşyasının %55’inde +%5, +2,75 puandır ve en iyi setin her parçasında +%15 (bir Heavy Shield Core ve üç Absorption Shield Cell IV, toplam %91) +13,65 puandır. Yücelmiş bir set +8,2 ile +13,65 puan arası, ortalamada yaklaşık 11 puan kazandırır; Sezon Mağazası’nın Shield Absorbance Boost güçlendirmesiyle (sınırında +10 puan; bir sıfırlamanın sıfırlama puanları 100 seviyesinin 44’ünü satın alır, +4,4 puan) bu bir gemiyi yaklaşık %106’e çıkarır, Pilot araştırması Field Theory ile (en fazla +10 puan) ise çok daha öteye taşır; özellik buna izin verir: saldıranın kalkan delmesi bundan düşülür. Rezonanslı bir set 3,6 ile 7,3 puan arası kazandırır. Bunlar, üzerinde hiç çatlak olmayan bonusların rakamlarıdır ([Bütünlük ve çatlaklar](#integrity-and-fractures)).

Motorlar, iticiler, Uyarlanabilir Çekirdekler ve Repair Drone eşyaları yüzdelik bir bonusla çok az değişir (bir Engine II 10 hız ekler, bu yüzden +%12, 1,2 puan eder): özellikler için değil, kademeyi istiyorsan döv.

**Penetration Amp bonusu** delmesini çarpar: Yücelmiş bir bonus (+%9 ile +%15), bir Penetration Amp IV eşyasını yuva başına 20 yerine 21,8 ile 23 puan yapar. Bir vuruşun delmesini hiçbir şey sınırlamaz, bu yüzden her puan sayılır: en iyi lazerde (bir Fusion Core, bir Gemini ve her lazerde üç Penetration Amp IV) 10 + 15 + 60 toplamı %85 eder ve üç Yücelmiş bonus bunu %94’e kadar çıkarır ([Lazerler](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

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

Kristaller kademeleri izler: Daraxium Uyanmış gibi mavi, Nyxite Rezonanslı gibi sarı, Cataclysite Parlak gibi turuncu ve Quorvium Yücelmiş gibi mor. Her kaynak, şansları ve miktarlarıyla birlikte [Kaynaklar](/wiki/06-Items/Resources.md) sayfasında ve her uzaylının sayfasındadır; Resource Magnet Booster bir kutunun içindekini %25 artırır. [Asteroitler](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds) parçalarında Dark Matter Plate dışında hepsini bırakır.

## Yuvalar {#sockets}

Demirhane’nin **Geliştir** görünümünde Kademe yükselt’in altındaki **Yuvalar** bölümü, bir bonusun eşyaya girdiği yerdir. Bir parça seç; bölüm onun yuvalarını, bütünlüğünü ve elindeki Shard’ları listeler. Bir yuva, bir kademe yükseltme onu uyandırana kadar **kilitlidir** (satırı hangi kademede ve hangi kristalin adımıyla uyanacağını söyler), uyanınca **boştur**, bir bonus taşıyorsa **ayarlanmıştır**. Kademe yükselt bölümü onları sayar: *Uyanık yuvalar 1 → 2 / 4*.

- Boş bir yuvayı **Echo Shard** ile **ayarla**: bir parçanın ilk yuvası için 10, sonra 20, 40 ve 80; yani fiyat ayarladığın her yuvayla artar (sonraki her boş yuvanın soluk fiyatı, ne kadara mal olacağını söyler). Shard’lar Ayarla’ya bastığında harcanır ve Demirhane sana bir **teklif** sunar: hâlâ boş olan özelliklerden rastgele çekilmiş ikisi, her biri vereceği bonusla birlikte. Birini **seç**: teklifin gösterdiğini alırsın. Yalnızca bir özellik boş kaldıysa iki satır da o özelliğin birer çekilişidir ve aynı çıkabilirler.
- Bir ayara ya da yeniden düzenlemeye bir **Heartshard** eklenebilir: önce *Sonraki ayarda ya da yeniden düzenlemede bir Heartshard kullan* seçeneğini aç; teklif bunun yerine parçanın boştaki her özelliğini listeler, her biri aralığının üst yarısında çekilmiş olarak; yani özelliği sen seçersin.
- Ayarlanmış bir yuvada başka bir özellik istediğinde onu **Lattice Shard** ile **yeniden düzenle**. Bir parçanın ilk yeniden düzenlemesi 2 Lattice Shard tutar, sonra 3, 4, 4, 5, 7 ve böyle sürer (2, önceki her yeniden düzenleme için bir kez 1,25 ile çarpılır, yukarı yuvarlanır) ve parçanın bütünlüğünden bir miktar: 6 puan, İmalat ile daha az ([Bütünlük ve çatlaklar](#integrity-and-fractures)). Önce bir pencere sorar, çünkü ne seçersen seç Shard’lar ve bütünlük harcanır. Teklif bir ayarınki gibi hazırlanır: boştaki özelliklerden ve yuvanın şimdi taşıdığı özellikten, her biri yeniden çekilerek; ve tüm genişlik boyunca bir **Mevcut olanı koru** düğmesi vardır; hiçbiri yuvadaki bonusu geçmiyorsa diye.
- **Sen seçene kadar parça bekler.** Açık bir teklif parçayı kilitler: üzerinde başka hiçbir şey çalışmaz ve panel bunu söyler. Oyunu kapatmak bir şey kaybettirmez, teklif döndüğünde yerinde durur. Kimsenin yanıtlamadığı teklif 7 gün sonra, Demirhane parçaya bir sonraki kez dokunduğunda (orada seçmek yeter) senin yerine çözülür: ayar teklifin ilk özelliğini alır, yeniden düzenleme mevcut bonusu korur. Açık Artırma ve Montaj’daki modül yükseltmeleri bir teklifi asla çözmez, Demirhane çözene kadar parçayı reddeder; bu yüzden parçayı önce Demirhane’de aç.
- **Onar**, bir sonraki yeniden düzenlemenin tutacağı Lattice Shard’ın iki katına 12 bütünlük geri verir. Yeniden düzenleme sayısını düşürmez, bu yüzden bir sonraki yeniden düzenlemenin fiyatı aynı kalır.
- **Gösterge**, bütünlüğü bir sonraki çatlağın açıldığı her noktada bir işaretle (ilki ilk puan kaybında açılır) gösterir; üzerine gelince her çatlağın hangi özelliği aldığını söyler. Bonusu bir çatlak yüzünden puan kaybeden ayarlı bir yuva iki sayıyı da gösterir (iki çatlaklı %9’luk bir bonus: *Çatlaklar yüzünden −%4 (çıkan: +%9)*), hiçbir şey kalmayan ise *Çatlaklarla yok oldu: bonus kalmadı* der. Yuva ayarlı kalır, bonusu +%0 olur.
- **Yalnızca boştaki yığınlar harcanır.** Nakliye Deposu’ndaki Shard’lar harcanmaz ve eksik olanlar oradaysa panel bunu söyler. Shard’lar satın alınamaz, satılamaz ve Açık Artırma’ya konamaz; şans da Resource Magnet Booster da onları artırmaz.

### Shard’lar nereden gelir {#where-the-shards-come-from}

Bir parçanın dört yuvasını da ayarlamak 150 Echo Shard tutar (10 + 20 + 40 + 80), ilk 16 yeniden düzenlemesi ise 283 Lattice Shard. Bunlar [Solo Geçitler](/wiki/03-Mechanics/Solo-Gates.md)’den ve [Zindanlar](/wiki/03-Mechanics/Dungeons.md)’dan gelir, bunların başka türlü ödediklerinin üstüne, ve uzaylılardan gelen birkaç Echo Shard’dan:

| Kaynak | Echo Shard’lar | Lattice Shard’lar |
| :--- | :---: | :---: |
| Solo geçit: Alpha Rift | 4 | 6 |
| Solo geçit: Beta Breach | 9 | 13 |
| Solo geçit: Gamma Foundry | 18 | 27 |
| Solo geçit: Delta Siege | 29 | 44 |
| Solo geçit: Omega Vault | 34 | 54 |
| Solo geçit: Davidski's Nightmare | 34 | 54 |
| Klan zindanı: 1. aşama | 12 | 5 |
| Klan zindanı: 2. aşama | 8 | 6 |
| Klan zindanı: 3. aşama | 8 | 7 |

- **Solo geçitler** Shard’larını her tamamlamada öder, **klan zindanları** bir aşamanın her ücretli tamamlanmasında.
- **Heartshard’lar** her geçidin ve her zindan aşamasının bir sezondaki ilk tamamlanmasıyla gelir (1) ve her tamamlamada %5 ihtimalle 1 tane daha. Nadir NPC’ler de onları düşürür: Davidski %10, Dormant Force ve Tesseract %5. Gerisi [Kaynaklar](/wiki/06-Items/Resources.md#heartshard) sayfasında.
- **Uzaylılar** yalnızca Echo Shard düşürür, o da az: bir Seeker için öldürme başına %0,8’ten bir Crystalys için %40’ye ([Echo Shard](/wiki/06-Items/Resources.md#echo-shard)).

## Birleştirme {#merge}

Aynı eşyanın iki kopyası (iki Light Shield Core, iki Quantum Laser II) tek olur. **Birleştir**’e geç ve tutmak istediğin eşyaya (**temel**), sonra ikinci bir kopyaya (**donör**) tıkla. Panel, sen onaylamadan önce sonucu gösterir.

- **Temel korunur.** Yerini korur: bir gemide ya da başka bir eşyaya takılı olabilir ve içine takılı modüller kalır. **Donör harcanır.** Boşta olmalıdır (bir gemide değil, takılı değil) ve içine takılı modüller envanterine geri döner.
- **Sonuç iki kademenin yüksek olanını alır** ve her özellik için **iki değerin daha iyisini**.
- **Kademesinin izin verdiğinden fazla bonus taşımaz.** İki eşyanın bonusları birlikte sonucun kademesinin taşıyabileceğinden fazlaysa en iyileri korunur, gerisi elenir; tablo onları işaretler (üstü çizili, “sınırı aşıyor”). Daha fazla bonus taşımak için önce eşyanın kademesini yükselt. Bir birleştirme hiçbir şeyi rastgele belirlemez: önizlemenin gösterdiği, elde edeceğindir.
- **Bir birleştirme, ortaya çıkardığı kademeye göre kredi tutar**: Uyanmış için 5.000, Rezonanslı için 25.000, Parlak için 100.000, Yücelmiş için 250.000. Malzeme yok. Commerce becerin bu krediyi de bir adımınki gibi düşürür.
- Hiçbir şeyi değiştirmeyecek bir birleştirme (sonuç temelden daha iyi değilse) reddedilir. Yalnızca daha iyi bir bütünlük sayılmaz: birleştirme bir onarım değildir.
- **Bütünlük.** Sonucun bütünlüğü, iki parçanın bütünlüğünün ortalamasının (aşağı yuvarlanmış) 6 eksiğidir, hiçbir zaman 0’ın altına inmez; yeniden düzenleme sayısı ise ikisinden yüksek olandır: iki sağlam parça 94 bütünlüklü tek bir parçada birleşir. Sonuç, tabanın çatlak sırasını korur: önce aynı özellik vurulur. Bkz. [Bütünlük ve çatlaklar](#integrity-and-fractures).
- Birleştirmeden sonra sonuç seçili kalır ve donör yuvası boştur: sonraki donörü koy ya da Geliştir moduna geri dön.
- **Etiket**: birleştirilen parça, yalnızca temel ve donör ikisi de öyleyse **satılabilir** olur ([pazarda](/wiki/03-Mechanics/Auction.md#marketable-items) satışa çıkarılabilir). Önizleme bunu söyler.

Bir birleştirme bir eşyayı çoğaltmaz. Faydası seçmektir: istediğin özelliklere sahip Rezonanslı bir çekirdek ya da gemindeki eşyanın üzerine, onu çıkarmadan taşınan bir kademe.

## Bütünlük ve çatlaklar {#integrity-and-fractures}

Her teçhizat parçasının 0 ile 100 arasında bir **bütünlüğü** vardır. Kimsenin üzerinde çalışmadığı bir parça 100’dedir. Montaj’da ürettiğin ya da ganimet olarak aldığın bir parça (bir uzaylının, bir sürünün ya da bir Warden’ın sandığından ya da bir klan zindanının teçhizat kartı olarak) 70 ile 100 arasında bir yerden başlar; satın aldıkların ya da hediye edilenler ve 0.5.7’den önce sahip olduğun her şey sağlamdır. Bir yuvayı yeniden düzenlemek (bir Lattice Shard gerekir) bütünlüğe mal olur: 6 puan, İmalat’ın 29. seviyesinden itibaren 5, 84. seviyeden itibaren 4 ([Pilot Becerileri](/wiki/03-Mechanics/Pilot-Skills.md)); geriye bundan fazlası kalmayan bir parça yeniden düzenlenemez. Bir onarım 12 puan geri verir (bkz. [Yuvalar](#sockets)).

100’ün altındaki her 12 puan bir **çatlaktır**, başlanmış 12 de sayılır: 99 ile 88 arasındaki bir parçada bir, 87 ile 76 arasında iki, böyle devam ederek en fazla 8 çatlak olur. Bir çatlak bir değerin bonusundan 2 puan alır: üzerinde iki çatlak olan +%9’luk bir bonus +%5 olur. Çatlaklar eşyanın değerlerine sırayla düşer, her parça için sabit bir sırayla: ilk çatlak bir değere, ikincisi bir sonrakine düşer ve her değer birer tane aldığında tur yeniden başlar. Bonusu olmayan bir değere de çatlak düşer: çatlakları bekler ve sen ona bir bonus ayarladığın anda sayılmaya başlar. Bir bonus hiçbir zaman +%0’ın altına inmez; yani bir çatlak parçayı hiçbir zaman sade eşyadan daha kötü yapmaz. Bonus verilecek tek bir değeri olan bir eşya (bir Hull Plating, bir Repair Drone, bir Crit Amp I, bir Penetration Amp, bir Impulse Thruster) bütün çatlakları o tek değerde alır: 8 çatlakta, 16 puanda, +%15’lik bir bonus bile kalmaz.

Envanterin, hangarın, açık artırmanın ve Demirhane’nin hasarlı bir parça için gösterdiği, parçanın **uçtuğu** değerdir: çatlaklar zaten düşülmüştür ve yanında çatlakların listesi durur. Kademe yükseltme ve modül yükseltmesi bütünlüğü olduğu gibi bırakır; bir [birleştirme](#merge) onu iki parçanın ortalamasının 6 eksiğine ayarlar.

## Sezon sıfırlaması {#the-season-wipe}

[Sıfırlamanın](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) koruduğu bir parça (ekipmanını koruyan gemiye takılı olan, Skylab’ına takılı olan ya da Nakliye Deposu’ndaki), Demirhane’nin ona yaptığı her şeyi korur: kademesini, ayarlanmış yuvalarını ve bonuslarını, bütünlüğünü, yeniden düzenleme sayısını ve hâlâ açık olan bir teklifi. Sıfırlama hiçbir şeyi onarmaz ve hiçbir şeyi kırmaz. Shard’lar cevherler gibi kaynaklardır: sıfırlama boştakileri yok eder, Nakliye Deposu’na koyduklarını ise korur (tanesi 1 kg).

## Montaj’da modül yükseltmeleri {#module-upgrades-in-the-assembly}

En üst üç lazer, lazer amfileri, II. ile IV. kademe kalkan hücreleri ve iticiler, II. ve III. kademe motorlar ve Uyarlanabilir Çekirdekler ile Heavy Shield Core satılmaz ve Montaj her birini yalnızca teknolojisini Skylab’da ([Araştırma](/wiki/03-Mechanics/Research.md)) araştırdıktan sonra üretir. Bunları Montaj’ın **Üretim** sekmesinde, bir adım aşağıdaki parçayı yükselterek üretirsin: Damage Amp III → **Damage Amp IV**, Crit Amp III → **Crit Amp IV**, Capacity Shield Cell I → **Capacity Shield Cell II** (III ve IV kademelerine kadar sürer; Absorption hücreleri, Impulse Thruster ve Momentum Thruster eşyaları da aynı şekilde yükselir), Basic Shield Core → **Heavy Shield Core**, Engine I → **Engine II** ve ardından **Engine III**, Adaptive Core I → **Adaptive Core II** ve ardından **Adaptive Core III**, Quantum Laser II → **Quantum Laser III**, Quantum Laser III → **Starfire-III** ve Starfire-III → **Helios Beam**. Demirhane’yi ilgilendiren kısım kademedir. Her amfi ailesinin ilk kademesi (Damage Amp I, Crit Amp I ve Penetration Amp I) Mağaza’da satılır; her ailenin II. ile IV. kademeleri bu şekilde üretilir.

- **Kademe kalır.** Bir yükseltme parçanın bir kopyasını harcar ve yeni eşya o kopyanın kademesini taşır: Rezonanslı bir Damage Amp III harcanırsa Rezonanslı bir Damage Amp IV olur, Standart olan Standart bir Damage Amp IV olur. Demirhane’ye ödediğin şey kaybolmaz. Yükseltme kendi başına kademe eklemez; bu yüzden Standart bir parça her zaman Standart bir sonuç verir.
- **Bonuslar korunur.** Yeni eşya, harcadığın parçanın bonuslarını korur: aynı özellikler aynı değerlerle, hiçbir şey yeniden belirlenmez (iki bonuslu Rezonanslı bir Damage Amp III harcanırsa o iki bonusla Rezonanslı bir Damage Amp IV olur, tek bonuslu olan o tek bonusla olur). Bir parçanın her özelliği, yükseltmesinin de özelliğidir; bu yüzden her bonus yerini bulur ve bir yükseltme boş bir yuvayı ayarlamaz, hiçbir bonusu da eksiltmez. Bonuslar işi kuyruğa aldığın anda sabitlenir ve topladığın şey sabitlenendir: toplamayı beklemek hiçbir şeyi değiştirmez; işi iptal edersen tıpatıp aynı parça, kademesi ve bonuslarıyla geri gelir. Bu kuraldan önce kuyruğa alınmış bir iş, belirlendiği bonusları korur. Pahalı olan, Demirhane’nin parçaya kattığıdır: Yücelmiş bir parça bir milyonun üzerinde kredilik Demirhane adımıdır ve yükseltme bunun hepsini korur. **Parçanın bütünlüğü ve yeniden düzenleme sayısı da onunla kalır**: bir yükseltme bir onarım değildir ve hiçbir çatlağı silmez.
- **Plakalar.** Thulium ve uzaylıların düşürdüklerinin yanında her modül yükseltmesi plaka ister. Son kademe **4 Dark Matter Plate** ve en az bir Ancient Control Unit ister: IV. kademe bir amfi, hücre ya da itici, Heavy Shield Core, Engine III, Adaptive Core III ve Helios Beam. Ondan önceki adımlar **Velkonite Reinforced Plate** ister: II. ya da III. kademe bir amfi için 2, II. ya da III. kademe bir hücre veya itici için 4, Quantum Laser III için 3, Engine II ya da Adaptive Core II için 4 ve Starfire-III için 8 (Helios Beam ayrıca 18 Orvium Reinforced Plate ister). Uzaylılar bunların hiçbirini düşürmez. [Skylab](/wiki/03-Mechanics/Skylab.md)’ındaki Dökümhane Velkonite ve Orvium plakalarını cevherden döker, Dökümhane 1. seviyedeyken plaka başına 40 Velkonite cevheri. 1. seviye bir Velkonite Toplayıcı saatte 10 cevher kazar; bu yüzden III. kademe bir amfinin plakaları 8 saatlik madencilik, III. kademe bir hücrenin ya da iticinin plakaları 16 saattir (5. seviye bir toplayıcıdan 4 ve 9 saat). Montaj, plakanın tarifini araştırdıktan sonra bir [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) preser: 5 Dark Matter, bir Velkonite Reinforced Plate, bir Orvium Reinforced Plate ve 250 Thulium ile. Her malzemenin nereden geldiği [Kaynaklar](/wiki/06-Items/Resources.md) sayfasındadır. Demirhane’nin kendi adımları ganimet ve kredi ister, en üst adımları ayrıca Dark Matter Plate ister (Rezonanslı → Parlak: 23 Reinforced Hull Plate ve 2 Dark Matter Plate; Parlak → Yücelmiş: 2 Dark Matter Plate): bir modül yükseltmesinin son kademesiyle aynı plakalar.
- **Hangi kopya kullanılır.** Sen seçersin. Farklı kopyalar tuttuğunda (başka bir kademe ya da başka bonuslar), tarif kartı onları bir kutucuk sırası olarak gösterir: kullanılacak olana tıkla; kutucukların altındaki satır neye dönüşeceğini gösterir (“Rezonanslı Damage Amp III”, sonra “Sonuç: Rezonanslı Damage Amp IV”). Hiçbirini seçmezsen en sade olan gider: önce en düşük kademe, aynı kademedeki kopyalar arasında bonusları ne olursa olsun en eskisi. Daha sade bir kopya boştayken Rezonanslı ya da daha iyi bir kopya asla kullanılmaz. Standart kademenin üstündeki bir kopyayı kullanmak önce sorar ve eşyanın adını söyler.
- **Hangi kopyalar kullanılabilir.** Boştakiler. Bir gemideki (bir yetenek yuvası da dahil), başka bir eşyaya takılı, Skylab’ındaki Motor ya da Savunma Modülü’ne takılı, kendi hücrelerini ya da iticilerini taşıyan ya da [Nakliye Deposu](/wiki/03-Mechanics/Cargo.md)’ndaki bir kopya kullanılamaz ve Montaj bunu söyler. Önce çıkar ya da depodan al. Birlikte başlatılan iki yükseltme aynı kopyayı kullanamaz.

- **Quantum Laser III de bir yükseltmedir.** Mağaza’nın lazeri olan bir **Quantum Laser II** kullanılarak yapılır (1.500 Thulium, 10 Ship Fragment ve 3 Velkonite Reinforced Plate ile: bkz. [Lazerler](/wiki/06-Items/Lasers.md)) ve yukarıdakilerin hepsi geçerlidir: Rezonanslı bir Quantum Laser II harcanırsa aynı bonuslarla Rezonanslı bir Quantum Laser III olur, kopyayı sen seçersin, kart Standart kademenin üstündekini kullanmadan önce sorar ve Quantum Laser II boşta olmalıdır: önce hangarda çıkar; çıkarana kadar Monte et düğmesi “Quantum Laser II parçanı çıkar” der. Kademe böylece yukarı doğru devam eder: Rezonanslı bir Quantum Laser III harcanırsa Rezonanslı bir Starfire-III olur.

- **Starfire-III de bir yükseltmedir.** Bir **Quantum Laser III** kullanılarak yapılır (1.500 Thulium, 100.000 kredi, ganimet ve 8 Velkonite Reinforced Plate ile: bkz. [Lazerler](/wiki/06-Items/Lasers.md)) ve yukarıdakilerin hepsi geçerlidir: Rezonanslı bir Quantum Laser III harcanırsa aynı bonuslarla Rezonanslı bir Starfire-III olur, kopyayı sen seçersin, kart Standart kademenin üstündekini kullanmadan önce sorar ve Quantum Laser III boşta olmalıdır: önce hangarda çıkar; çıkarana kadar Monte et düğmesi “Quantum Laser III parçanı çıkar” der. Kademe böylece yukarı doğru devam eder: Rezonanslı bir Starfire-III harcanırsa Rezonanslı bir Helios Beam olur.

- **Helios Beam de bir yükseltmedir.** Bir **Starfire-III** kullanılarak yapılır (2.000 Thulium, ganimet, 18 Orvium Reinforced Plate, 4 Dark Matter Plate ve bir Ancient Control Unit ile: bkz. [Lazerler](/wiki/06-Items/Lasers.md)) ve yukarıdakilerin hepsi geçerlidir: Rezonanslı bir Starfire-III harcanırsa Starfire-III’ün bonuslarıyla Rezonanslı bir Helios Beam olur, kopyayı sen seçersin, kart Standart kademenin üstündekini kullanmadan önce sorar ve Starfire-III boşta olmalıdır. Bir lazer bir gemiye takılıdır ve amfi taşır, bu yüzden çoğu zaman boşta değildir: önce hangarda çıkar (amfileri envanterine döner); çıkarana kadar Monte et düğmesi “Starfire-III parçanı çıkar” der.

Tarifler, maliyetleri ve kuralın arkasındaki sayılar [Eşyalara genel bakış](/wiki/06-Items/Overview.md#upgrading-modules) sayfasında; Quantum Laser III, Starfire-III ve Helios Beam için ise [Lazerler](/wiki/06-Items/Lasers.md) sayfasındadır.

## Eski sunucular {#old-servers}

Demirhane için güncellenmemiş bir oyun sunucusu, sekmenin yerinde “Demirhane bu sunucuda henüz yok” gösterir; Üretim eskisi gibi çalışır. Demirhane’den önceki bir oyun istemcisi, güncellenmiş bir sunucuda eski Füzyon sekmesini gösterir ve güncellemesi söylenir. 0.5.7’den önceki bir sunucuda Yuvalar bölümü yoktur ve 0.5.7’den önceki bir oyun Demirhane’yi hâlâ açıp okuyabilir, ama güncellenmiş bir sunucu istediği her değişikliği (bir kademe yükseltmeyi, bir birleştirmeyi, bir ayarı, bir yeniden düzenlemeyi, bir onarımı, bir Tinkerer's Badge’i) şu mesajla reddeder: “Bu özelliği kullanmak için oyunu güncelle.”
