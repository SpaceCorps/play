<!-- wiki-i18n source: fff5cfd69e987468 -->
<!-- wiki-i18n title: Seeker sürüsü -->
# Seeker sürüsü {#seeker-swarm}

Seeker sürüsü, [sürülerin](/wiki/05-Swarms/Swarms.md) en küçüğüdür: bir **Boss Seeker** ve onu koruyup gövdesini onaran **Seeker Slave** gemileri. Yeni pilotların uçmaya başladığı sektörlerde yaşar, bu yüzden çoğu pilotun karşılaştığı ilk sürüdür. Boss Seeker hiçbir zaman kavgayı başlatmaz, ama ona ateş ettiğinde, temel aldığı [Seeker](/wiki/04-Aliens/Seeker.md) gemisinden çok daha tehlikeli olur.

## Bir bakışta {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Her şirketin `x-1` ve `x-2` sektörleri
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 6 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar
- **Lider**: Boss Seeker
- **Takipçiler**: En fazla 4 × Seeker Slave, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 500 birim
- **Onarım**: Liderin 600 birim yakınındaki her Seeker Slave, liderin gövdesini Alpha dünyasında saniyede 50 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 30 sn sonra ayrılır
- **Geri gelir**: Lider yok edildikten 2 dk sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- seeker-glance:end -->

## Üyeler {#the-members}

- **Boss Seeker**: çok daha büyük bir Seeker; sürünün tonunda ve üzerinde adıyla görünür; gövdesi, kalkanı ve hasarı bir Seeker gemisinin birçok katıdır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra olduğu yerde durur ve o pilota ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Seeker gemisininki gibidir ve gövdesini kendi kendine asla onarmaz.
- **Seeker Slave**: sürünün tonunda sade bir Seeker. Seeker Slave gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Seeker Slave, bir Seeker gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Gemin dayanabilecek hâle gelene kadar ona dokunma.** Bir Boss Seeker, bir pilotun ilk gemisinin kaldırabileceğinden sert vurur: henüz kalkanı olmayan yeni bir pilotun Protos gemisi, patron ve Seeker Slave gemileri üzerine geldiğinde saniyeler içinde yok edilir.
- **Menzilinin dışında kal.** Patron ve Seeker Slave gemileri bir Protos gemisinden yavaştır ve silahlarının menzili bir Quantum Laser II lazerinin menzilinden kısadır (bkz. [Lazerler ve cephane](/wiki/06-Items/Lasers.md)): bu lazerlere sahip olup menzillerinin dışında kalan bir pilot, onlar ateş ederken hiç hasar almaz. Quantum Laser I taşıyan bir pilot menzil dışında kalamaz.
- **Seeker Slave gemileri, yalnız bir yeni pilotun vurduğundan hızlı onarır.** Hep birlikte, tek bir pilotun lazerlerinin x1 cephaneyle verdiğinden fazlasını onarırlar; bu yüzden bir partner ve x2 cephane getir. Mesafesini koruyan, Quantum Laser II taşıyan iki pilot, Alpha dünyasında patronu yaklaşık bir dakikada indirir; x2 cephaneyle çok daha hızlı.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Seeker Slave gemileri de birbiri ardına gelir.

## Ödüller ve ganimet {#rewards-and-drops}

Boss Seeker **tam olarak on Seeker** öder: bir Seeker öldürmesinin kredisinin, Thulium’unun, XP’sinin ve onurunun on katı; onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusunda on Seeker ganimeti ve bunun üstüne Destansı nadirliğin altında cephane ve roketler bulunur; kutu en çok hasar veren pilota aittir. Seeker Slave gemileri az öder ve hiçbir şey düşürmez; onları öldürmek farm yapmanın yolu değildir, çünkü patronla birlikte geri gelirler.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Seeker temel alınarak, gövdesinin, kalkanının ve hasarının %400 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 3.200 | 4.800 | 6.400 |
| Kalkan | 3.200 | 4.800 | 6.400 |
| Lazer hasarı (saniyede bir salvo) | 720 | 1.080 | 1.440 |
| Hız | 120 | 120 | 120 |
| Lazer menzili | 600 | 600 | 600 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | 10.000 | 20.000 | 30.000 |
| Thulium | 40 | 80 | 120 |
| Deneyim (XP) | 1.000 | 2.000 | 3.000 |
| Onur | 20 | 40 | 60 |
| Öldürme başına PvE puanı | 5 | 5 | 5 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya | Şans | Miktar |
| :--- | ---: | ---: |
| Ship Fragment | 10 çekilişin her birinde %20 | 1 |
| Daraxium | 10 çekilişin her birinde %50 | 1–2 |
| Standard Battery | %100 | 200–400 |
| Advanced Plasma | %100 | 10–20 |
| Ultra Core | %100 | 2–4 |
| Kredi ile satın alınan 8 [roket](/wiki/06-Items/Rockets.md) arasından rastgele biri | %100 | 2–3 |

### Seeker Slave

Seeker temel alınarak, gövdesinin, kalkanının ve hasarının %100 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 800 | 1.200 | 1.600 |
| Kalkan | 800 | 1.200 | 1.600 |
| Lazer hasarı (saniyede bir salvo) | 180 | 270 | 360 |
| Hız | 120 | 120 | 120 |
| Lazer menzili | 600 | 600 | 600 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 50 | 75 | 100 |
| Kredi | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Deneyim (XP) | 12 | 24 | 36 |
| Onur | 1 | 2 | 3 |
| Öldürme başına PvE puanı | 1 | 1 | 1 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- seeker-members:end -->
