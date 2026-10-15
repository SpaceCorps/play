<!-- wiki-i18n source: 4a99637f071798ec -->
<!-- wiki-i18n title: Pirate sürüsü -->
# Pirate sürüsü {#pirate-swarm}

Pirate sürüsü, bir **Pirate Boss** ve onun **Pirate Scout** gemileridir: kimseye saldırmayan ve roketlerle karşılık veren kocaman, yavaş bir gemi ile onu koruyup gövdesini onaran, daha hızlı bir gemi sürüsü. Bir şirketin üssü ile sınırı arasındaki, oyunun orta seviyelerinin oynandığı sektörlerde yaşar ve bir grup pilot için hızlı bir öldürme değil, uzun bir savaştır.

## Bir bakışta {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Her şirketin `x-2` ve `x-3` sektörleri
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 6 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar
- **Lider**: Pirate Boss
- **Takipçiler**: En fazla 5 × Pirate Scout, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 900 birim
- **Onarım**: Liderin 600 birim yakınındaki her Pirate Scout, liderin gövdesini Alpha dünyasında saniyede 40 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 1 dk sonra ayrılır
- **Geri gelir**: Lider yok edildikten 2 dk sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- pirate-glance:end -->

## Üyeler {#the-members}

- **Pirate Boss**: Ironclad gemisini temel alan, onun gücünün bir kısmına sahip bir gemi (değerler aşağıda). Pasiftir ve **hiç lazer ateşlemez**: tek silahı bir **düz roket** ([Roketler](/wiki/06-Items/Rockets.md); hangisi olduğu sektöre bağlıdır, tabloya bak): onu kendisine saldıran pilota fırlatır ve ateş ederken dolaşmaya devam eder. Gövdesini kendi kendine asla onarmaz.
- **Pirate Scout**: Kitefin gemisini temel alan, onun gücünün bir kısmına sahip bir gemi. Pirate Scout gemileri yaklaşan her pilota saldırır, patronun yakınında kalır ve patronun yakınındaki her biri onun gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Patrona ateş et, Scout gemilerine değil.** Scout gemileri patronu onarır, ama onarım patronun gövdesinin yanında küçüktür ve *Bir bakışta* listesinin söylediği sıklıkta yeni bir Scout gelir: Scout gemilerini önce öldüren bir grup onların önüne asla geçemez; yalnızca çok büyük bir grup onları temizleyebilir ve yine de patronu bitirmesi, onları rahat bırakan bir gruptan daha uzun sürer. Scout gemileri sana zaman kaybettirir, savaşı belirlemez.
- **Scout gemilerini uzağa çek.** Bir Scout yalnızca patronun erişimi içindeyken onarır; bu yüzden seni erişim dışına kadar izleyen bir Scout hiçbir şeyi onarmaz ve bir Ostirion bir Scout gemisinden hızlıdır.
- **Hareket etmeye devam et.** Patronun roketi düzdür ve güdümsüzdür: hareket etmeye devam eden gemi ondan kaçar, olduğu yerde duran vurulur.
- **Bir grup getir.** x2 cephaneli Ostirion gemilerindeki üç pilot, darbeler paylaşıldığında bile `x-3` sektöründe bu savaşı kaybeder, `x-2` sektöründe de; dört pilot Alpha dünyasında onu yaklaşık dört dakikada indirir. x4 cephaneyle `x-3` sektöründe de üç pilot yeter (yaklaşık iki buçuk dakika). Beş pilot, darbeler paylaşıldığında yaklaşık üç dakikada, tüm ateşi tek pilot aldığında yaklaşık beş dakikada indirir; o durumda dört gemi kaybederler: tüm ateşi tek pilotun almasına izin veren bir grubun beş kişi olması gerekir. Beta dünyasında altı, Gamma dünyasında sekiz pilot gerekir; darbeler paylaşılmış olmalıdır (patron orada daha büyüktür ve Scout gemileri daha çok onarır). Tek bir Ostirion tek başına başaramaz, tek bir Paragon da başaramaz: iki Paragon başarır. Patron ona ilk vuran pilota karşılık verir, bu yüzden işe en sağlam gemi başlasın ve bu kadar uzun bir savaşta yeteneklerini (Emergency Repair, Shield Surge: [Yetenekler](/wiki/03-Mechanics/Abilities.md)) kullan. Hâlâ 2. ya da 3. seviyede olan pilotlar, uçtukları yerde bile, bunun için fazla zayıftır: daha güçlenene kadar uzak dur.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, aynı sektörde.

## Ödüller ve ganimet {#rewards-and-drops}

Pirate Boss, olduğu savaşın karşılığını öder: onunla bir dakikalık savaş, bir Goombah ile bir dakikalık savaştan daha çok öder. Ödeme, onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusu en çok hasar veren pilota aittir ve bir **Reinforced Hull Plate**, roketler ve cephane içerebilir. Kutunun değeri, öldürmenin kendi ödemesinin yaklaşık beşte ikisi kadardır. Scout gemileri az öder ve hiçbir şey düşürmez.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Ironclad temel alınarak, gövdesinin, kalkanının ve hasarının %50 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır. 5 sn aralıkla düz bir roket fırlatır: `x-2` sektöründe [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets), `x-3` sektöründe [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 300.000 | 450.000 | 600.000 |
| Kalkan | 50.100 | 75.150 | 100.200 |
| Lazer hasarı (saniyede bir salvo) | yok | yok | yok |
| Hız | 92 | 92 | 92 |
| Lazer menzili | – | – | – |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Roket hasarı, en fazla | 2.500 (Rivet I) / 5.000 (Rivet II) | 3.750 (Rivet I) / 7.500 (Rivet II) | 5.000 (Rivet I) / 10.000 (Rivet II) |
| Kredi | 145.000 | 290.000 | 435.000 |
| Thulium | 725 | 1.450 | 2.175 |
| Deneyim (XP) | 29.000 | 58.000 | 87.000 |
| Onur | 232 | 464 | 696 |
| Öldürme başına PvE puanı | 15 | 15 | 15 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya | Şans | Miktar |
| :--- | ---: | ---: |
| Reinforced Hull Plate | %50 | 1 |
| Kredi ile satın alınan 8 [roket](/wiki/06-Items/Rockets.md) arasından rastgele biri | %100 | 5–10 |
| Advanced Plasma ve Siphon Battery arasından rastgele biri | %100 | 1.000–2.000 |

### Pirate Scout

Kitefin temel alınarak, gövdesinin %50 kadarıyla ve lazer hasarının %113 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 12.000 | 18.000 | 24.000 |
| Kalkan | 9.818 | 14.727 | 19.636 |
| Lazer hasarı (saniyede bir salvo) | 221 | 332 | 442 |
| Hız | 175 | 175 | 175 |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | 700 | 700 | 700 |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 40 | 60 | 80 |
| Kredi | 1.000 | 2.000 | 3.000 |
| Thulium | 4 | 8 | 12 |
| Deneyim (XP) | 100 | 200 | 300 |
| Onur | 2 | 4 | 6 |
| Öldürme başına PvE puanı | 4 | 4 | 4 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- pirate-members:end -->
