<!-- wiki-i18n source: abb582fd63389ab9 -->
<!-- wiki-i18n title: Phantasm sürüsü -->
# Phantasm sürüsü {#phantasm-swarm}

Phantasm sürüsü, bir **Boss Phantasm** ve **Phantasm Guard** gemilerinden oluşur: hiçbir zaman kavgayı başlatmayan devasa bir [Phantasm](/wiki/04-Aliens/Phantasm.md) ile onun yakınında kalıp gövdesini onaran daha küçük olanlar. Şirketlerin dış sektörlerinde, `x-3` ve `x-4` sektörlerinde yaşar ve orta seviyeli pilotlardan oluşan bir grup için bir savaştır.

## Bir bakışta {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Her şirketin `x-3` ve `x-4` sektörleri
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 6 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar (Beta ve Gamma: sezonun 1. gününden itibaren)
- **Lider**: Boss Phantasm
- **Takipçiler**: En fazla 4 × Phantasm Guard, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 500 birim
- **Onarım**: Liderin 600 birim yakınındaki her Phantasm Guard, liderin gövdesini Alpha dünyasında saniyede 30 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 30 sn sonra ayrılır
- **Geri gelir**: Lider yok edildikten 2 dk sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- phantasm-glance:end -->

## Üyeler {#the-members}

- **Boss Phantasm**: sürünün tonunda ve üzerinde adıyla görünen, daha büyük bir Phantasm; kendine ait gövdesi, kalkanı ve lazer yaylım ateşi vardır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra o pilotun peşine düşüp ona ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Phantasm gemisininkiyle aynıdır ve gövdesini kendi kendine asla onarmaz.
- **Phantasm Guard**: sürünün tonunda daha küçük bir Phantasm. Guard gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Guard, bir Phantasm gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Bir grup getir.** x2 cephaneli, 4–5. seviyeden üç pilot onu Alpha’da yaklaşık bir buçuk dakikada yok eder ve en fazla bir gemi kaybeder; bu seviyeden tek bir pilot yok edilir, iki pilot ise ancak zar zor kazanır, o da yalnızca darbeler paylaşıldığında. Daha iyi gemiler ve x4 cephane işi çok hızlandırır.
- **Patrona ateş et, Guard gemilerine değil.** Bir Guard saniyeler içinde düşer, ama *Bir bakışta* listesinin söylediği sıklıkta yenisi gelir; Guard gemilerinin onardığı da bir grubun verdiği hasarın küçük bir kısmıdır: onları rahat bırakmak biraz zamana mal olur, peşlerine düşmek daha çoğuna.
- **Beta ve Gamma daha zordur.** O dünyaların sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)); bu yüzden daha çok pilot ya da daha iyi cephane gerekir.
- **Sektörü gözle.** `x-4` Alpha’da bir PvP sektörüdür; Beta ve Gamma’da ise `x-3` ve `x-4` öyledir ([Dünyalar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): bir rakip savaşa katılabilir ya da kutuyu bekleyebilir. Grubun bir gemisini gözcü olarak bırak.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Guard gemileri de birbiri ardına gelir.

## Ödüller ve ganimet {#rewards-and-drops}

Boss Phantasm, olduğu savaşın karşılığını öder: onunla bir dakikalık savaş, bu sektörlerin en çok ödeyen uzaylısı olan bir Goombah ile bir dakikalık savaştan daha çok öder. Ödeme, onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusu en çok hasar veren pilota aittir ve bir Phantasm’ın ganimetini katbekat içerir (Ship Fragment, Daraxium ve Nyxite); ayrıca cephane ve roketler bulunur. Guard gemileri az öder ve hiçbir şey düşürmez; onları öldürmek farm yapmanın yolu değildir, çünkü patronla birlikte geri gelirler.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Phantasm temel alınarak, gövdesinin %2.000 kadarıyla ve lazer hasarının %300 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 40.000 | 60.000 | 80.000 |
| Kalkan | 64.000 | 96.000 | 128.000 |
| Lazer hasarı (saniyede bir salvo) | 1.050 | 1.575 | 2.100 |
| Hız | 160 | 160 | 160 |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | 39.000 | 78.000 | 117.000 |
| Thulium | 195 | 390 | 585 |
| Deneyim (XP) | 7.800 | 15.600 | 23.400 |
| Onur | 62 | 124 | 186 |
| Öldürme başına PvE puanı | 8 | 8 | 8 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya | Şans | Miktar |
| :--- | ---: | ---: |
| Ship Fragment | 13 çekilişin her birinde %100 | 1 |
| Daraxium | 13 çekilişin her birinde %60 | 1–2 |
| Nyxite | 13 çekilişin her birinde %60 | 1–2 |
| Standard Battery | %100 | 600–1.200 |
| Advanced Plasma | %100 | 60–100 |
| Ultra Core | %100 | 10–20 |
| Kredi ile satın alınan 8 [roket](/wiki/06-Items/Rockets.md) arasından rastgele biri | %100 | 4–6 |

### Phantasm Guard

Phantasm temel alınarak, gövdesinin, kalkanının ve hasarının %50 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 1.000 | 1.500 | 2.000 |
| Kalkan | 1.600 | 2.400 | 3.200 |
| Lazer hasarı (saniyede bir salvo) | 175 | 263 | 350 |
| Hız | 160 | 160 | 160 |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 30 | 45 | 60 |
| Kredi | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Deneyim (XP) | 12 | 24 | 36 |
| Onur | 1 | 2 | 3 |
| Öldürme başına PvE puanı | 1 | 1 | 1 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- phantasm-members:end -->
