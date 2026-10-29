<!-- wiki-i18n source: 9cb279aeecb3bbc8 -->
<!-- wiki-i18n title: Konteynerler -->
# Konteynerler {#containers}

<!-- wiki-search: konteyner; konteynerler; sandık; kutu; lootbox; loot box; şanslar; olasılık; garanti; pity; makara; açılış; kasa; pota; arşiv; silindir; raf; container; case; crate; odds; drop rate; vault; crucible; archive; canister; rack -->

Bir **konteyner**, Mission Control’ün mühürlü bir buluntusudur. Birini açtığında sunucu bir tablodan bir ödül çeker ve o tablodaki her ödülün şansı bu sayfada yazılıdır. Oyunun Konteynerler sayfası aynı tabloyu gösterir.

> [!NOTE]
> **Konteynerler oyunda kazanılan rastgele ödüllerdir. Asla satılmazlar ve şanslar burada yayımlanır.** Hiçbir konteyner satın alınamaz, takas edilemez ya da hediye edilemez.

## Konteyner nedir {#what-a-container-is}

- **Kazanılır.** Konteynerleri oyunda kazanırsın. Fiyatı ve anahtarı yoktur: Mağaza onları satmaz, başka kimse de satmaz.
- **Yalnızca senin.** Konteyner hesabına bağlıdır. Onu takas edemez, bir arkadaşına veremez ve [Açık Artırma](/wiki/03-Mechanics/Auction.md)’ya koyamazsın; bir konteynerin verdiği hiçbir şey de oraya konamaz.
- **Her pilot için aynı.** Premium hiçbir şeyi değiştirmez: fazladan açılış ya da daha iyi şans vermez.
- **Sıfırlama boyunca kalır.** Açmadığın bir konteyner, [sıfırlama](/wiki/03-Mechanics/Wipe-Timeline.md) geldiğinde hesabında kalır. Sıfırlamanın ödüllere ne yaptığı [Sıfırlama](#the-wipe) bölümünde yazılıdır.
- **İstasyonda açılır.** Konteyneri istasyona kenetliyken, Konteynerler sayfasında açarsın. Ödülü sunucu sen Aç’a bastığında çeker ve basmanın kendisi hiçbir şeyi değiştirmez. Neyin sayıldığı [Bir ödül nasıl seçilir](#how-a-prize-is-chosen) bölümündedir.

## Konteynerler nereden gelir {#where-containers-come-from}

<!-- containers-sources:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

Konteynerler sana şu yollarla ulaşır:

- Oyunun yöneticilerinden
- Sıfırlamada rütben için ödül olarak
- Giriş takviminde
- Başarımlar için

<!-- containers-sources:end -->

## Beş konteyner {#the-five-containers}

<!-- containers-glance:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Konteyner | İçindekiler | Uygun olan | Sıfırlamada kapanır | Garanti | En nadir ödül |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Numune Kasası (Specimen Vault)** | Her şeyden biraz: kredi, Thulium, mühimmat, roketler, ekipman, plakalar, Dark Matter, boosterlar ve renkler | Her pilot | Sezonun 30. gününden itibaren | 10 açılış içinde Nadir sınıfında veya daha iyi bir ödül | 60.000 Thulium; 12.000.000 kredi: her biri %0,100 |
| **Döküm Potası (Foundry Crucible)** | Mühimmat, roketler, lazerler, yükselticiler, kalkan hücreleri, iticiler ve ekipman; ayrıca 5 gemi | 5. seviye ve üstü | Sezonun 30. gününden itibaren | 8 açılış içinde Nadir sınıfında veya daha iyi bir ödül | gemi: Wraith: %0,020 |
| **Kroma Arşivi (Chroma Archive)** | Yalnızca görünümler: skinler, renkler, egzoz efektleri ve auralar | Her pilot | Açık kalır | 12 açılış içinde Destansı sınıfında veya daha iyi bir ödül | Crystal Ice; Comet; Halo: her biri %0,667 |
| **Keşif Silindiri (Survey Canister)** | Skylab cevheri, plakalar, Dark Matter, Cluster Chunks ve Thulium | Skylab çekirdeği 10 ve üstü | Sezonun 30. gününden itibaren | 8 açılış içinde Nadir sınıfında veya daha iyi bir ödül | 32 × Dark Matter Plate; 50.000 Thulium: her biri %0,150 |
| **Reaktif Rafı (Reagent Rack)** | Booster etkileri, EMP Charges, Energetic Walls ve mühimmat | 4. seviye ve üstü | Sezonun 30. gününden itibaren | 10 açılış içinde Nadir sınıfında veya daha iyi bir ödül | **Tam spektrum**; Cloaking CPU L: her biri %0,100 |

<!-- containers-glance:end -->

**Uygun** yalnızca bir tavsiyedir: oyun, her konteyneri her seviyede açmana izin verir.

## Sınıflar {#grades}

Her ödülün bir **sınıfı** vardır; oyunun nadirlik sözcüklerinden biridir. Çekilişin ilk karar verdiği şey sınıftır. Makarada, ödül kutucuğunun çerçevesidir; bir renk ve bir şekille gösterilir, böylece renk hiçbir zaman tek işaret olmaz.

| Sınıf | Renk | Şekil |
| :--- | :--- | :--- |
| Sıradan | Gri | Daire |
| Seyrek | Yeşil | Kare |
| Nadir | Mavi | Eşkenar dörtgen |
| Destansı | Mor | Altıgen |
| Mitik | Pembe | Yıldız |
| Efsanevi | Altın | Taç |

Her konteynerin her sınıf için kendi şansı vardır ve aşağıda yazılıdır. Sahip olduğun şeyler bir sınıfın şansını asla değiştirmez.

## Numune Kasası (Specimen Vault) {#specimen-vault}

*Mission Control’ün ksenoarşivcileri tek bir alana sığdıramadıkları her buluntuyu numaralı bir kasaya mühürler ve açılmadan gönderir. Bir pilot mührü kırana kadar istasyonda kimse kasanın içinde ne olduğunu bilmez.*

### Sınıfların şansları {#specimen-vault-grades}

<!-- containers-specimen-vault-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Şans | İçindeki ödüller |
| :--- | ---: | ---: |
| Sıradan | %38,000 | 9 |
| Seyrek | %38,000 | 8 |
| Nadir | %17,000 | 8 |
| Destansı | %5,500 | 5 |
| Mitik | %1,300 | 4 |
| Efsanevi | %0,200 | 2 |

<!-- containers-specimen-vault-grades:end -->

### Her ödül {#specimen-vault-prizes}

<!-- containers-specimen-vault-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Ödül | Şans |
| :--- | :--- | ---: |
| Sıradan | 50.000 kredi | %5,000 |
| Sıradan | 250 Thulium | %4,000 |
| Sıradan | 10.000 × Standard Battery | %4,000 |
| Sıradan | 500 × Advanced Plasma | %4,000 |
| Sıradan | 250 × Ultra Core | %3,000 |
| Sıradan | **Roket rafı I**: 4 taneden biri, 100 adet, eşit şans: Ember I, Lancet I, Rivet I, Scatter I | %6,000 |
| Sıradan | **Demirci tozu**: 1.500 × Daraxium + 1.500 × Nyxite | %3,000 |
| Sıradan | 4.000 × Ship Fragment | %3,000 |
| Sıradan | 1 sa Experience Booster | %6,000 |
| Seyrek | 150.000 kredi | %6,000 |
| Seyrek | 750 Thulium | %6,000 |
| Seyrek | 750 × Ultra Core | %4,500 |
| Seyrek | 340 × Experimental Fusion Core | %4,000 |
| Seyrek | **Roket rafı II**: 4 taneden biri, 190 adet, eşit şans: Ember II, Lancet II, Rivet II, Scatter II | %6,000 |
| Seyrek | 10 × Velkonite Reinforced Plate | %4,000 |
| Seyrek | 1 sa Laser Damage Booster I | %4,000 |
| Seyrek | **Renk örneği**: 11 taneden biri, eşit şans: Cobalt, Indigo, Violet, Magenta, Crimson, Ember, Sunset, Gold, Emerald, Jade, Teal | %3,500 |
| Nadir | 400.000 kredi | %2,500 |
| Nadir | 2.000 Thulium | %2,500 |
| Nadir | 10 × Dark Matter | %1,500 |
| Nadir | **Roket rafı III**: 4 taneden biri, 400 adet, eşit şans: Ember III, Lancet III, Rivet III, Scatter III | %2,000 |
| Nadir | 1.000 × Experimental Fusion Core | %1,500 |
| Nadir | 9 × Orvium Reinforced Plate | %1,500 |
| Nadir | 4 sa Laser Damage Booster I | %1,500 |
| Nadir | **II. kademe bir parça**: 4 taneden biri, eşit şans: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | %4,000 |
| Destansı | 1.200.000 kredi | %1,200 |
| Destansı | 6.000 Thulium | %1,200 |
| Destansı | 30 × Dark Matter | %0,900 |
| Destansı | 26 × Orvium Reinforced Plate | %0,900 |
| Destansı | **III. kademe bir parça**: 5 taneden biri, eşit şans: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III, Starfire-III | %1,300 |
| Mitik | 18.000 Thulium | %0,400 |
| Mitik | 12 × Dark Matter Plate | %0,300 |
| Mitik | Helios Beam | %0,300 |
| Mitik | **IV. kademe bir yükseltici**: 3 taneden biri, eşit şans: Damage Amp IV, Crit Amp IV, Penetration Amp IV | %0,300 |
| Efsanevi | 60.000 Thulium | %0,100 |
| Efsanevi | 12.000.000 kredi | %0,100 |

<!-- containers-specimen-vault-prizes:end -->

**Renk örneği**, sende henüz olmayan bir renk verir. Örnekteki tüm renkler sendeyse onun yerine geri dönüşüm Thulium’u öder ([Kopyalar ve geri dönüşüm](#duplicates-and-salvage)).

### Garanti {#specimen-vault-guarantee}

<!-- containers-specimen-vault-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garanti**: her 10 açılışta en az bir kez Nadir sınıfında veya daha iyi bir ödül
- **Garanti olmadan Nadir sınıfında veya daha iyi bir ödülün şansı**: %24,000
- **Garantiyle, çok sayıda açılışta**: %25,649
- **Garantinin zorladığı açılışlar**: %2,170
- **Böyle iki ödül arasındaki açılış sayısı, ortalama**: 3,899

<!-- containers-specimen-vault-guarantee:end -->

## Döküm Potası (Foundry Crucible) {#foundry-crucible}

*Dormant dökümhaneleri, son partileri hâlâ potadayken soğudu: mühimmat, takılı ekipman ve en derinlerde hiç bitirilmemiş bir gövde. Mission Control’ün mühendisleri potaları harabelerden kesip çıkardı ve pilotlara mühürlü olarak veriyor, çünkü hangisinde gövde olduğunu kimse söyleyemez.*

### Sınıfların şansları {#foundry-crucible-grades}

<!-- containers-foundry-crucible-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Şans | İçindeki ödüller |
| :--- | ---: | ---: |
| Sıradan | %45,000 | 6 |
| Seyrek | %30,000 | 7 |
| Nadir | %16,000 | 6 |
| Destansı | %6,500 | 6 |
| Mitik | %2,200 | 5 |
| Efsanevi | %0,300 | 2 |

<!-- containers-foundry-crucible-grades:end -->

### Her ödül {#foundry-crucible-prizes}

<!-- containers-foundry-crucible-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Ödül | Şans |
| :--- | :--- | ---: |
| Sıradan | 30.000 × Standard Battery | %7,000 |
| Sıradan | 1.500 × Advanced Plasma | %7,000 |
| Sıradan | 750 × Ultra Core | %7,000 |
| Sıradan | 340 × Experimental Fusion Core | %5,000 |
| Sıradan | **Roket rafı I**: 4 taneden biri, 300 adet, eşit şans: Ember I, Lancet I, Rivet I, Scatter I | %11,000 |
| Sıradan | **Lazer seti**: Quantum Laser II + Damage Amp I + Crit Amp I + Penetration Amp I | %8,000 |
| Seyrek | 2.250 × Ultra Core | %4,500 |
| Seyrek | 1.020 × Experimental Fusion Core | %4,500 |
| Seyrek | **Roket rafı II**: 4 taneden biri, 560 adet, eşit şans: Ember II, Lancet II, Rivet II, Scatter II | %8,500 |
| Seyrek | Basic Shield Core | %4,500 |
| Seyrek | **II. kademe yükseltici üçlüsü**: Damage Amp II + Crit Amp II + Penetration Amp II | %4,000 |
| Seyrek | Repair Drone IV | %3,900 |
| Seyrek | gemi: Nomad | %0,100 |
| Nadir | 1.800 × Experimental Fusion Core | %2,500 |
| Nadir | **Roket rafı III**: 4 taneden biri, 500 adet, eşit şans: Ember III, Lancet III, Rivet III, Scatter III | %3,000 |
| Nadir | Quantum Laser III | %2,400 |
| Nadir | **II. kademe bir parça**: 4 taneden biri, eşit şans: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | %4,500 |
| Nadir | **III. kademe bir yükseltici**: 3 taneden biri, eşit şans: Damage Amp III, Crit Amp III, Penetration Amp III | %3,500 |
| Nadir | gemi: Paragon | %0,100 |
| Destansı | **III. kademe bir hücre veya itici**: 4 taneden biri, eşit şans: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III | %3,000 |
| Destansı | Starfire-III | %1,200 |
| Destansı | Heavy Shield Core | %1,200 |
| Destansı | Cloaking CPU M | %1,000 |
| Destansı | gemi: Storm | %0,050 |
| Destansı | gemi: Ironclad | %0,050 |
| Mitik | Helios Beam | %0,600 |
| Mitik | **IV. kademe bir hücre veya itici**: 4 taneden biri, eşit şans: Absorption Shield Cell IV, Capacity Shield Cell IV, Impulse Thruster IV, Momentum Thruster IV | %0,700 |
| Mitik | **IV. kademe bir yükseltici**: 3 taneden biri, eşit şans: Damage Amp IV, Crit Amp IV, Penetration Amp IV | %0,480 |
| Mitik | Cloaking CPU L | %0,400 |
| Mitik | gemi: Wraith | %0,020 |
| Efsanevi | **Helios cephaneliği**: Helios Beam + Damage Amp IV + Crit Amp IV + Penetration Amp IV | %0,150 |
| Efsanevi | 50.000 Thulium | %0,150 |

<!-- containers-foundry-crucible-prizes:end -->

Gemiler temel şanslarıyla listelenir. Sende zaten olan bir gemi hiç çıkmaz, bu yüzden kendi şansların bu tablodan biraz farklı olabilir: bkz. [Gemiler](#the-ships).

### Garanti {#foundry-crucible-guarantee}

<!-- containers-foundry-crucible-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garanti**: her 8 açılışta en az bir kez Nadir sınıfında veya daha iyi bir ödül
- **Garanti olmadan Nadir sınıfında veya daha iyi bir ödülün şansı**: %25,000
- **Garantiyle, çok sayıda açılışta**: %27,781
- **Garantinin zorladığı açılışlar**: %3,708
- **Böyle iki ödül arasındaki açılış sayısı, ortalama**: 3,600

<!-- containers-foundry-crucible-guarantee:end -->

## Kroma Arşivi (Chroma Archive) {#chroma-archive}

*Dormant mor-siyah kristalden, mor damarlarla inşa ederdi; arşivcileri rengi, üzerine bastırılan her şeyi yeniden boyayan ince cam plakalarda saklardı. Her Kroma Arşivi, Mission Control’ün renkçileri tarafından dizinlenmiş ve bir pilot açana kadar hiç kimse tarafından okunmamış, mühürlü bir plaka yığınıdır.*

Kroma Arşivi önce sınıfı, sonra o sınıftan sende henüz olmayan bir görünümü çeker; her görünümün şansı eşittir. Bir koleksiyon tek bir ödüldür: sende olmayan tüm skinlerini verir. Tablodaki şans, sınıfın görünümlerinden hiçbirine sahip olmayan bir pilot içindir. Topladıkça yükselir, çünkü çekilişte daha az görünüm kalır. Görünümlerin kendisi [Kozmetikler](/wiki/06-Items/Cosmetics.md) sayfasındadır.

### Sınıfların şansları {#chroma-archive-grades}

<!-- containers-chroma-archive-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Şans | İçindeki görünümler |
| :--- | ---: | ---: |
| Sıradan | %6,000 | 1 |
| Seyrek | %50,000 | 14 |
| Nadir | %30,000 | 8 |
| Destansı | %12,000 | 12 |
| Mitik | %2,000 | 3 |
| Efsanevi | %0,000 | – |

<!-- containers-chroma-archive-grades:end -->

### Her ödül {#chroma-archive-prizes}

<!-- containers-chroma-archive-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Görünüm | Sınıfından hiçbirine sahip değilsen şans |
| :--- | :--- | ---: |
| Sıradan | Glow (aura) | %6,000 |
| Seyrek | Company Supporter (koleksiyon) | %3,571 |
| Seyrek | Cobalt (renk) | %3,571 |
| Seyrek | Indigo (renk) | %3,571 |
| Seyrek | Violet (renk) | %3,571 |
| Seyrek | Magenta (renk) | %3,571 |
| Seyrek | Crimson (renk) | %3,571 |
| Seyrek | Ember (renk) | %3,571 |
| Seyrek | Sunset (renk) | %3,571 |
| Seyrek | Gold (renk) | %3,571 |
| Seyrek | Emerald (renk) | %3,571 |
| Seyrek | Jade (renk) | %3,571 |
| Seyrek | Teal (renk) | %3,571 |
| Seyrek | Twin (egzoz efekti) | %3,571 |
| Seyrek | Breath (aura) | %3,571 |
| Nadir | Nature White (koleksiyon) | %3,750 |
| Nadir | Sunrise Orbit (koleksiyon) | %3,750 |
| Nadir | Seeker Burnt (renk) | %3,750 |
| Nadir | Pirate Brick (renk) | %3,750 |
| Nadir | Pulse (egzoz efekti) | %3,750 |
| Nadir | Helix (egzoz efekti) | %3,750 |
| Nadir | Motes (aura) | %3,750 |
| Nadir | Shimmer (aura) | %3,750 |
| Destansı | Midnight Gala (koleksiyon) | %1,000 |
| Destansı | Blue Marble (koleksiyon) | %1,000 |
| Destansı | Mimosa (koleksiyon) | %1,000 |
| Destansı | Olive Branch (koleksiyon) | %1,000 |
| Destansı | Steady Pulse (koleksiyon) | %1,000 |
| Destansı | Hollow Night (koleksiyon) | %1,000 |
| Destansı | Dormant Void (renk) | %1,000 |
| Destansı | Ancient Amethyst (renk) | %1,000 |
| Destansı | Embers (egzoz efekti) | %1,000 |
| Destansı | Gradient (egzoz efekti) | %1,000 |
| Destansı | Sparkle (aura) | %1,000 |
| Destansı | Wreath (aura) | %1,000 |
| Mitik | Crystal Ice (renk) | %0,667 |
| Mitik | Comet (egzoz efekti) | %0,667 |
| Mitik | Halo (aura) | %0,667 |

<!-- containers-chroma-archive-prizes:end -->

### Garanti {#chroma-archive-guarantee}

<!-- containers-chroma-archive-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garanti**: her 12 açılışta en az bir kez Destansı sınıfında veya daha iyi bir ödül
- **Garanti olmadan Destansı sınıfında veya daha iyi bir ödülün şansı**: %14,000
- **Garantiyle, çok sayıda açılışta**: %16,740
- **Garantinin zorladığı açılışlar**: %3,186
- **Böyle iki ödül arasındaki açılış sayısı, ortalama**: 5,974

<!-- containers-chroma-archive-guarantee:end -->

## Keşif Silindiri (Survey Canister) {#survey-canister}

*Keşif sondaları Skylab’lardan evren haritasının sisine uçar ve her biri mühürlü bir karot numunesi silindiri olarak döner. Kimsenin haritalamadığı bir damardan cevher, anomaliler ve ara sıra haritadan da eski bir şeyin parçası: Mission Control silindiri hücreye göre dosyalar, okumayı Skylab’ın sahibine bırakır.*

### Sınıfların şansları {#survey-canister-grades}

<!-- containers-survey-canister-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Şans | İçindeki ödüller |
| :--- | ---: | ---: |
| Sıradan | %45,000 | 8 |
| Seyrek | %30,000 | 7 |
| Nadir | %16,000 | 6 |
| Destansı | %6,500 | 5 |
| Mitik | %2,200 | 3 |
| Efsanevi | %0,300 | 2 |

<!-- containers-survey-canister-grades:end -->

### Her ödül {#survey-canister-prizes}

<!-- containers-survey-canister-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Ödül | Şans |
| :--- | :--- | ---: |
| Sıradan | 240 × Velkonite (Skylab’a) | %7,000 |
| Sıradan | 160 × Orvium (Skylab’a) | %7,000 |
| Sıradan | 1.300 × Reinforced Hull Plate | %5,000 |
| Sıradan | 9.000 × Ship Fragment | %6,000 |
| Sıradan | **Demirci kristalleri**: 4.000 × Cataclysite + 3.000 × Quorvium | %5,000 |
| Sıradan | 450 × Power Core | %5,000 |
| Sıradan | 450 Thulium | %5,000 |
| Sıradan | 4 × Regular Cluster Chunk | %5,000 |
| Seyrek | 780 × Velkonite (Skylab’a) | %5,000 |
| Seyrek | 510 × Orvium (Skylab’a) | %5,000 |
| Seyrek | 19 × Velkonite Reinforced Plate | %4,000 |
| Seyrek | 7 × Dark Matter | %5,000 |
| Seyrek | 8 × Ancient Control Unit | %3,000 |
| Seyrek | 1.450 Thulium | %4,000 |
| Seyrek | 3 × Mythical Cluster Chunk | %4,000 |
| Nadir | 17 × Dark Matter | %3,500 |
| Nadir | 15 × Orvium Reinforced Plate | %3,000 |
| Nadir | 1.900 × Velkonite (Skylab’a) | %2,500 |
| Nadir | 1.230 × Orvium (Skylab’a) | %2,500 |
| Nadir | 2 × Legendary Cluster Chunk | %1,500 |
| Nadir | 3.500 Thulium | %3,000 |
| Destansı | 45 × Dark Matter | %1,500 |
| Destansı | 39 × Orvium Reinforced Plate | %1,200 |
| Destansı | **Karışık plaka sandığı**: 60 × Velkonite Reinforced Plate + 20 × Orvium Reinforced Plate | %1,200 |
| Destansı | 9.000 Thulium | %1,500 |
| Destansı | 6 × Dark Matter Plate | %1,100 |
| Mitik | 13 × Dark Matter Plate | %0,900 |
| Mitik | 20.000 Thulium | %0,800 |
| Mitik | 100 × Dark Matter | %0,500 |
| Efsanevi | 32 × Dark Matter Plate | %0,150 |
| Efsanevi | 50.000 Thulium | %0,150 |

<!-- containers-survey-canister-prizes:end -->

*(Skylab’a)* işaretli cevher, Kaynak Deposu’nun izin verdiği kadarıyla Skylab’ının cevher bankasına girer. Geri kalanı aynı cevher olarak envanterine gelir. Bkz. [Skylab](/wiki/03-Mechanics/Skylab.md).

### Garanti {#survey-canister-guarantee}

<!-- containers-survey-canister-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garanti**: her 8 açılışta en az bir kez Nadir sınıfında veya daha iyi bir ödül
- **Garanti olmadan Nadir sınıfında veya daha iyi bir ödülün şansı**: %25,000
- **Garantiyle, çok sayıda açılışta**: %27,781
- **Garantinin zorladığı açılışlar**: %3,708
- **Böyle iki ödül arasındaki açılış sayısı, ortalama**: 3,600

<!-- containers-survey-canister-guarantee:end -->

## Reaktif Rafı (Reagent Rack) {#reagent-rack}

*Skylab’ın Araştırma Merkezi, uçarken kullandığın booster etkilerini reaktif ampullerinden damıtır; raf ise bir parti yarıda kesildiğinde geriye kalandır: her reaktifin kendi mühürlü ampulünde ölçülü bir dozu. Dozlar yalnızca gemi uçarken eskir, bu yüzden raf istediğin kadar rafta durabilir.*

### Sınıfların şansları {#reagent-rack-grades}

<!-- containers-reagent-rack-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Şans | İçindeki ödüller |
| :--- | ---: | ---: |
| Sıradan | %45,000 | 5 |
| Seyrek | %33,000 | 8 |
| Nadir | %15,000 | 8 |
| Destansı | %5,500 | 6 |
| Mitik | %1,300 | 2 |
| Efsanevi | %0,200 | 2 |

<!-- containers-reagent-rack-grades:end -->

### Her ödül {#reagent-rack-prizes}

<!-- containers-reagent-rack-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Ödül | Şans |
| :--- | :--- | ---: |
| Sıradan | 1 sa Experience Booster | %11,000 |
| Sıradan | 1 sa Honor Booster | %11,000 |
| Sıradan | 1 sa Shield Regen Booster | %9,000 |
| Sıradan | Energetic Wall I | %8,000 |
| Sıradan | 500 × Advanced Plasma | %6,000 |
| Seyrek | 1 sa Laser Damage Booster I | %5,000 |
| Seyrek | 1 sa Shield Wall Booster I | %5,000 |
| Seyrek | 1 sa Hull Plating Booster I | %5,000 |
| Seyrek | 1 sa Resource Magnet Booster | %3,500 |
| Seyrek | 2 sa Experience Booster | %4,500 |
| Seyrek | 2 sa Honor Booster | %3,500 |
| Seyrek | EMP Charge | %3,500 |
| Seyrek | 3 × Energetic Wall I | %3,000 |
| Nadir | 2 sa Laser Damage Booster I | %2,500 |
| Nadir | 2 sa Shield Wall Booster I | %2,000 |
| Nadir | 2 sa Hull Plating Booster I | %2,000 |
| Nadir | 4 sa Experience Booster | %2,000 |
| Nadir | 4 sa Honor Booster | %2,000 |
| Nadir | 2 sa Loot Luck Booster | %1,500 |
| Nadir | 3 × EMP Charge | %2,000 |
| Nadir | 2 sa Resource Magnet Booster | %1,000 |
| Destansı | 4 sa Laser Damage Booster I | %1,200 |
| Destansı | 4 sa Shield Wall Booster I | %1,000 |
| Destansı | 4 sa Hull Plating Booster I | %1,000 |
| Destansı | 4 sa Resource Magnet Booster | %0,700 |
| Destansı | 4 sa Loot Luck Booster | %0,900 |
| Destansı | 8 × EMP Charge | %0,700 |
| Mitik | **Savaş rafı**: 4 sa Laser Damage Booster I + 4 sa Shield Wall Booster I + 4 sa Hull Plating Booster I | %0,700 |
| Mitik | **Âlim rafı**: 4 sa Experience Booster + 4 sa Honor Booster + 4 sa Resource Magnet Booster + 4 sa Loot Luck Booster | %0,600 |
| Efsanevi | **Tam spektrum**: 4 sa Laser Damage Booster I + 4 sa Shield Wall Booster I + 4 sa Hull Plating Booster I + 4 sa Shield Regen Booster + 4 sa Experience Booster + 4 sa Honor Booster + 4 sa Resource Magnet Booster + 4 sa Loot Luck Booster | %0,100 |
| Efsanevi | Cloaking CPU L | %0,100 |

<!-- containers-reagent-rack-prizes:end -->

Booster süresi, zaten çalışıyorsa aynı booster’a eklenir ve yalnızca uçarken azalır. Bkz. [Boosterlar](/wiki/06-Items/Boosters.md).

### Garanti {#reagent-rack-guarantee}

<!-- containers-reagent-rack-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Garanti**: her 10 açılışta en az bir kez Nadir sınıfında veya daha iyi bir ödül
- **Garanti olmadan Nadir sınıfında veya daha iyi bir ödülün şansı**: %22,000
- **Garantiyle, çok sayıda açılışta**: %24,001
- **Garantinin zorladığı açılışlar**: %2,565
- **Böyle iki ödül arasındaki açılış sayısı, ortalama**: 4,167

<!-- containers-reagent-rack-guarantee:end -->

## Bir ödül nasıl seçilir {#how-a-prize-is-chosen}

Bir konteyner açtığında sunucu üç adımda seçer:

1. **Sınıf.** Bir rastgele sayı, sınıfların şanslarıyla eşleştirilir.
2. **Ödül.** İkinci bir sayı, o sınıftaki ödüllerin şanslarıyla eşleştirilir. Sende zaten olan bir gemi bunların arasında değildir (bkz. [Gemiler](#the-ships)).
3. **Eşitler arasından seçim.** *Birkaçından biri* diyen bir ödül, onlardan birini verir; her birinin şansı eşittir.

Sayılar sunucunun işletim sisteminin rastgele sayı üretecinden gelir ve konteynerin alındıktan sonra çekilir. Gönderdiğin hiçbir şey onları değiştiremez: ne düğme, ne saat.

Öncesinden iki şey yine de sayılır. Garanti sayacı bir açılıştan sonrakine taşınır; onu yukarıda her konteynerin garantisi anlatır. Ayrıca zaten sahip olduğun şeyler, önceki açılışlarda kazandıkların dahil, çekilişte hangi ödüllerin kaldığını değiştirir: sahip olduğun bir gemi bunların arasında değildir, sahip olduğun bir görünüm de sınıfında sahip olmadığın bir görünüm kaldığı sürece çekilmez (bkz. [Kopyalar ve geri dönüşüm](#duplicates-and-salvage) ve [Gemiler](#the-ships)). Sahip olduğun şeyler sınıfların şanslarını asla değiştirmez.

<!-- containers-draw:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- Her şans, 100.000 paydan tam sayıda paydır. Bir pay %0,001 eder.

<!-- containers-draw:end -->

**Her açılış kaydedilir**: sunucunun kullandığı tohum (rastgele sayı), çekilen sayılar, çekilen tablonun özeti ve sahip olduklarının çekilişten çıkardığı ödüller. Bunları Konteynerler sayfasındaki **Geçmiş** içinde **Ayrıntılar** altında okuyabilirsin.

**Birini kendin de kontrol edebilirsin.** Oyunun kaynak kodundaki `scripts/containers-verify.py` aracı tabloyu ve bir açılışın ayrıntılarını okur ve sınıfın, ödülün ve seçimin tohumdan çıkıp çıkmadığını söyler. Yöntem kısadır:

```text
stream(seed, id): value i, for i = 0, 1, 2, ...
  = the first 8 bytes (big endian) of HMAC-SHA256(
      key     = seed,
      message = "sc-container-v1|" + id + "|" + i )
  where i is written as 4 bytes, big endian
below(n): take values until one is under 2^64 - (2^64 mod n),
  then use it modulo n (no modulo bias)
grade:    roll = below(total of the grades in play);
  the grade is the first whose running sum is above the roll
prize:    sub = below(total of the prizes left in that grade);
  the prize is the first whose running sum is above sub
choice:   a prize that is "one of N" gives the alternative
  number below(N)
seed = the 32 bytes shown under Details; id = the container's id.
When the guarantee forces an opening, only the guaranteed grade
and better are in play.
```

## Kopyalar ve geri dönüşüm {#duplicates-and-salvage}

- Sahip olduğun bir **görünüm**, sınıfta sende olmayan bir görünüm kaldığı sürece çekilmez. Bir koleksiyon, tüm skinlerine sahip olduğunda sahip olunmuş sayılır.
- Sınıftaki her görünüme sahip olduğunda ödül onun yerine **geri dönüşüm** öder: sınıfa göre Thulium. Garanti için o sınıftan bir ödül sayılır.
- **Eşyalar** asla Thulium’a çevrilmez: üst üste yığılır ya da olduğu gibi gelir.
- **Gemiler** asla iki kez verilmez ve asla geri dönüşüm olarak ödenmez (bkz. [Gemiler](#the-ships)).

<!-- containers-salvage:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Sınıf | Thulium |
| :--- | ---: |
| Sıradan | 25 |
| Seyrek | 100 |
| Nadir | 400 |
| Destansı | 1.200 |
| Mitik | 4.000 |

<!-- containers-salvage:end -->

## Gemiler {#the-ships}

Döküm Potası konteyneri bir gemi tutabilir. Tablo gemileri **temel şanslarıyla** listeler; bunlar, hiçbirine sahip olmayan bir pilotun şanslarıdır. Yayımlanan şanslar bunlardır.

Sende zaten olan bir gemi hiçbir zaman çıkamaz. Çekilişten çıkarılır ve payı, aynı sınıftaki diğer ödüllere kendi şanslarıyla orantılı olarak gider. Yani sahip olduklarının kendi şanslarını değiştirir: o sınıfın diğer ödüllerinde biraz daha yüksek. Sınıfların şansları asla değişmez, garanti de değişmez. Bir gemiden yapılmış bir tasarım, o gemiye sahip olmak sayılır: bir Paragon THUNDER, Paragon’a sahip olmak sayılır.

<!-- containers-ships:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Gemi | Sınıf | Şans |
| :--- | :--- | ---: |
| Nomad | Seyrek | %0,100 |
| Paragon | Nadir | %0,100 |
| Storm | Destansı | %0,050 |
| Ironclad | Destansı | %0,050 |
| Wraith | Mitik | %0,020 |
| **Hepsi: 5** | | **%0,320** |

Örnek: Nomad adlı gemiye sahipsin. Seyrek sınıfı şansını korur, ancak sınıfın 30.000 payından o geminin (Nomad) 100 payı çekilişten çıkarılır; böylece Seyrek sınıfındaki her diğer ödül, tablonun söylediğinden 30.000 / 29.900 = 1,0033 kat daha olasıdır.

Sonraki tablo, sınıftaki her gemiye sahip olduğunda geçerlidir. Yalnızca bazılarına sahipsen, çekilişten yalnızca onların payları çıkarılır; bu yüzden çarpan daha küçüktür.

| Sınıf | Sınıfın payları | Tüm gemilerinin payları | Sınıfın her diğer ödülü bu kadar daha olası |
| :--- | ---: | ---: | ---: |
| Seyrek | 30.000 | 100 | ×1,0033 |
| Nadir | 16.000 | 100 | ×1,0063 |
| Destansı | 6.500 | 100 | ×1,0156 |
| Mitik | 2.200 | 20 | ×1,0092 |

Örnek: Destansı sınıfında 2 gemi var. Yalnızca Storm adlı gemiye sahipsen, sınıfın 6.500 payından yalnızca onun 50 payı çekilişten çıkarılır; böylece Destansı sınıfındaki her diğer ödül 6.500 / 6.450 = 1,0078 kat daha olasıdır, 1,0156 kat değil.

<!-- containers-ships:end -->

Oyunun Konteynerler sayfası, farklı olduklarında kendi şanslarını yayımlananların yanında gösterir. Sahip olduğun bir gemi listede soluk renkte kalır ve “Bu gemi sende var, bu yüzden bir konteynerden çıkamaz.” satırı yazar.

## Sıfırlama {#the-wipe}

- **Açılmamış konteynerler korunur.** Sıfırlama boyunca hesabında kalır.
- **Konteynerden çıkan eşyalar sıradan eşyalardır.** Sıfırlamada, Nakliye Deposu’nda taşımazsan kaybolur ([Sıfırlama zaman çizelgesi](/wiki/03-Mechanics/Wipe-Timeline.md)).
- **Görünümler ve gemiler sende kalır**, her görünüm ve her gemi gibi. Krediler, Thulium ve booster’ların kalan süresi sıfırlamada kendi kurallarına uyar.
- **Bir konteynerden çıkan hiçbir şey Açık Artırma’ya konamaz.**

<!-- containers-wipe:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Sezonun 30. gününden itibaren kapalı**: Numune Kasası, Döküm Potası, Keşif Silindiri, Reaktif Rafı. İçindekiler sıfırlamada kaybolacağı için, sıfırlama bitene kadar açılamazlar.
- **Uyarı bandı**: Konteynerler sayfası sezonun 28. gününden itibaren seni uyarır.
- **Açık kalır**: Kroma Arşivi. İçinde yalnızca görünümler vardır ve sıfırlama görünümleri korur.

<!-- containers-wipe:end -->

## Tablonun sürümü {#version-of-the-table}

Bu sayfadaki her şans, oyunun sunucusunun tablosudur. Bir şans değiştiğinde tablo yeni bir sürüm ve yeni bir özet alır; her açılış, çekildiği tablonun özetini kaydeder.

<!-- containers-version:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Tablonun sürümü**: 1
- **Tablonun özeti (ilk 12 karakter)**: `23aa20f1a5ad`

Ne değişti:

- Sürüm 1: Yayımlanan ilk tablo.

<!-- containers-version:end -->
