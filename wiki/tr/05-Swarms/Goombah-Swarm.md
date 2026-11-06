<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Goombah sürüsü -->
# Goombah sürüsü {#goombah-swarm}

Goombah sürüsü, bir **Boss Goombah** ve **Goombah Guard** gemilerinden oluşur: hiçbir zaman kavgayı başlatmayan dev bir [Goombah](/wiki/04-Aliens/Goombah.md) ile onun yakınında kalıp gövdesini onaran daha küçük olanlar. [Phantasm sürüsü](/wiki/05-Swarms/Phantasm-Swarm.md) ile aynı sektörlerde, `x-3` ve `x-4` sektörlerinde yaşar ve şirket sektörlerinin en güçlü pilotlarından oluşan bir grup için bir savaştır.

## Bir bakışta {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Her şirketin `x-3` ve `x-4` sektörleri
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 6 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar (Beta ve Gamma: sezonun 1. gününden itibaren)
- **Lider**: Boss Goombah
- **Takipçiler**: En fazla 4 × Goombah Guard, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 500 birim
- **Onarım**: Liderin 600 birim yakınındaki her Goombah Guard, liderin gövdesini Alpha dünyasında saniyede 110 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 30 sn sonra ayrılır
- **Geri gelir**: Lider yok edildikten 5 dk sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- goombah-glance:end -->

## Üyeler {#the-members}

- **Boss Goombah**: sürünün tonunda ve üzerinde adıyla görünen, daha büyük bir Goombah; kendine ait gövdesi, kalkanı ve lazer yaylım ateşi vardır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra o pilotun peşine düşüp ona ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Goombah gemisininkiyle aynıdır ve gövdesini kendi kendine asla onarmaz.
- **Goombah Guard**: sürünün tonunda daha küçük bir Goombah. Guard gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Guard, bir Goombah gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **En güçlü gemilerden oluşan bir grup getir.** x2 cephaneli, 8. seviyeden üç pilot onu Alpha’da yaklaşık 75 saniyede yok eder ve en fazla bir gemi kaybeder; bunlardan ikisinin x4 cephaneye ihtiyacı vardır, daha düşük seviyeli pilotlar ise kazanmaya yetecek hasarı veremez.
- **Patrona ateş et, Guard gemilerine değil.** Bir Guard saniyeler içinde düşer, ama *Bir bakışta* listesinin söylediği sıklıkta yenisi gelir; Guard gemilerinin onardığı da bir grubun verdiği hasarın küçük bir kısmıdır: onları rahat bırakmak biraz zamana mal olur, peşlerine düşmek daha çoğuna.
- **Beta ve Gamma daha zordur.** O dünyaların sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)); bu yüzden daha çok pilot ya da daha iyi cephane gerekir.
- **Sektörü gözle.** `x-4` Alpha’da bir PvP sektörüdür; Beta ve Gamma’da ise `x-3` ve `x-4` öyledir ([Dünyalar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): bir rakip savaşa katılabilir ya da kutuyu bekleyebilir. Grubun bir gemisini gözcü olarak bırak.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Guard gemileri de birbiri ardına gelir.

## Ödüller ve ganimet {#rewards-and-drops}

Boss Goombah, olduğu savaşın karşılığını öder: onunla bir dakikalık savaş, bu sektörlerin en çok ödeyen uzaylısı olan bir Goombah ile bir dakikalık savaştan daha çok öder. Ödeme, onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusu en çok hasar veren pilota aittir ve bir Goombah’ın ganimetini birkaç kat içerir (Cataclysite, Quorvium, Power Core, Reinforced Hull Plate ve Ship Fragment); ayrıca cephane ve roketler bulunur. Guard gemileri az öder ve hiçbir şey düşürmez; onları öldürmek farm yapmanın yolu değildir, çünkü patronla birlikte geri gelirler.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Goombah temel alınarak, gövdesinin %400 kadarıyla ve lazer hasarının %100 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 128.000 | 192.000 | 256.000 |
| Kalkan | 192.000 | 288.000 | 384.000 |
| Lazer hasarı (saniyede bir salvo) | 3.000 | 4.500 | 6.000 |
| Hız | 180 | 180 | 180 |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | 120.000 | 240.000 | 360.000 |
| Thulium | 600 | 1.200 | 1.800 |
| Deneyim (XP) | 24.000 | 48.000 | 72.000 |
| Onur | 192 | 384 | 576 |
| Öldürme başına PvE puanı | 14 | 14 | 14 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya | Şans | Miktar |
| :--- | ---: | ---: |
| Ship Fragment | 8 çekilişin her birinde %100 | 3 |
| Reinforced Hull Plate | 8 çekilişin her birinde %60 | 1 |
| Power Core | 8 çekilişin her birinde %25 | 1 |
| Cataclysite | 8 çekilişin her birinde %100 | 4 |
| Quorvium | 8 çekilişin her birinde %100 | 2–4 |
| Advanced Plasma | %100 | 100–200 |
| Ultra Core | %100 | 100–200 |
| Kredi ile satın alınan 8 [roket](/wiki/06-Items/Rockets.md) arasından rastgele biri | %100 | 6–10 |

### Goombah Guard

Goombah temel alınarak, gövdesinin, kalkanının ve hasarının %20 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 6.400 | 9.600 | 12.800 |
| Kalkan | 9.600 | 14.400 | 19.200 |
| Lazer hasarı (saniyede bir salvo) | 600 | 900 | 1.200 |
| Hız | 180 | 180 | 180 |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 110 | 165 | 220 |
| Kredi | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Deneyim (XP) | 12 | 24 | 36 |
| Onur | 1 | 2 | 3 |
| Öldürme başına PvE puanı | 3 | 3 | 3 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- goombah-members:end -->
