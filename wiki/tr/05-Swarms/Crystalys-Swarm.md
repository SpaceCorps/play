<!-- wiki-i18n source: 62896aebea81e95a -->
<!-- wiki-i18n title: Crystalys sürüsü -->
# Crystalys sürüsü {#crystalys-swarm}

Crystalys sürüsü, bir **Boss Crystalys** ve **Crystalys Guard** gemilerinden oluşur: uzaylıların en sağlamı olan [Crystalys](/wiki/04-Aliens/Crystalys.md) gemisinin daha büyük hâli ve onun yakınında kalıp gövdesini onaran muhafızlar. [Tehlike Sektörleri](/wiki/01-General/Danger-Sectors.md) içinde `DS-1`, `DS-2` ve `DS-3` sektörlerinde, her birinde bir tane yaşar ve sektöründen hiç ayrılmaz. Tehlike Sektörleri PvP sektörleridir; bu yüzden savaş, en güçlü pilotlardan oluşan büyük bir grup içindir ve oradaki tek tehlike patron değildir.

## Bir bakışta {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Tehlike Sektörleri `DS-1`, `DS-2`, `DS-3`
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 3 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar
- **Lider**: Boss Crystalys
- **Takipçiler**: En fazla 3 × Crystalys Guard, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 500 birim
- **Onarım**: Liderin 600 birim yakınındaki her Crystalys Guard, liderin gövdesini Alpha dünyasında saniyede 250 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 30 sn sonra ayrılır
- **Geri gelir**: Lider yok edildikten 30 dk sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- crystalys-glance:end -->

## Üyeler {#the-members}

- **Boss Crystalys**: sürünün tonunda ve üzerinde adıyla görünen, daha büyük bir Crystalys; kendine ait gövdesi, kalkanı ve lazer yaylım ateşi vardır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra o pilotun peşine düşüp ona ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Crystalys gemisininkiyle aynıdır ve gövdesini kendi kendine asla onarmaz.
- **Crystalys Guard**: sürünün tonunda daha küçük bir Crystalys. Guard gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Guard, bir Crystalys gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Büyük bir grup getir.** x2 cephaneli, Paragon ile uçan 8. seviyeden sekiz pilot onu Alpha’da yaklaşık bir dakikada yok eder ve en fazla bir gemi kaybeder; dördünün x4 cephaneye ihtiyacı vardır, tek başına bir pilot ise yok edilir.
- **Patrona ateş et, Guard gemilerine değil.** Bir Guard saniyeler içinde düşer, ama *Bir bakışta* listesinin söylediği sıklıkta yenisi gelir; Guard gemilerinin onardığı da bir grubun verdiği hasarın küçük bir kısmıdır: onları rahat bırakmak biraz zamana mal olur, peşlerine düşmek daha çoğuna.
- **Beta ve Gamma daha zordur.** O dünyaların sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)); bu yüzden daha çok pilot ya da daha iyi cephane gerekir.
- **Tehlike Sektörleri PvP’dir.** Bir rakip savaşın ortasında gruba saldırıp kutuyu bekleyebilir: kutu 30 saniye boyunca en çok hasar veren pilotun (ve klanının) olur, sonra herkesin ([Kargo](/wiki/03-Mechanics/Cargo.md)). Yalnız gitme.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Guard gemileri de birbiri ardına gelir.

## Ödüller ve ganimet {#rewards-and-drops}

Boss Crystalys, olduğu savaşın karşılığını öder: onunla bir dakikalık savaş, en çok ödeyen uzaylı olan bir Crystalys ile bir dakikalık savaştan daha çok öder. Ödeme, onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusu en çok hasar veren pilota aittir ve Cataclysite ile Quorvium içerir; ara sıra bir Power Core, bir Ancient Control Unit ya da Dark Matter, x3 ve x4 cephane ve Destansı roketler de çıkar. Guard gemileri az öder ve hiçbir şey düşürmez; onları öldürmek farm yapmanın yolu değildir, çünkü patronla birlikte geri gelirler.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Crystalys temel alınarak, gövdesinin %175 kadarıyla ve lazer hasarının %50 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 448.000 | 672.000 | 896.000 |
| Kalkan | 280.000 | 420.000 | 560.000 |
| Lazer hasarı (saniyede bir salvo) | 5.000 | 7.500 | 10.000 |
| Hız | 230 | 230 | 230 |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | 393.750 | 787.500 | 1.181.250 |
| Thulium | 1.050 | 2.100 | 3.150 |
| Deneyim (XP) | 63.000 | 126.000 | 189.000 |
| Onur | 273 | 546 | 819 |
| Öldürme başına PvE puanı | 21 | 21 | 21 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya | Şans | Miktar |
| :--- | ---: | ---: |
| Cataclysite | 2 çekilişin her birinde %100 | 8 |
| Quorvium | 2 çekilişin her birinde %100 | 6–10 |
| Power Core | %30 | 1 |
| Ancient Control Unit | %15 | 1 |
| Dark Matter | %4 | 1 |
| Ultra Core ve Experimental Fusion Core, eşit paylaşılır | %100 | toplam 600–1.000 |
| 4 Destansı [roket](/wiki/06-Items/Rockets.md) arasından rastgele biri | %100 | 8–15 |

### Crystalys Guard

Crystalys temel alınarak, gövdesinin, kalkanının ve hasarının %15 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | 38.400 | 57.600 | 76.800 |
| Kalkan | 24.000 | 36.000 | 48.000 |
| Lazer hasarı (saniyede bir salvo) | 1.500 | 2.250 | 3.000 |
| Hız | 230 | 230 | 230 |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 250 | 375 | 500 |
| Kredi | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Deneyim (XP) | 12 | 24 | 36 |
| Onur | 1 | 2 | 3 |
| Öldürme başına PvE puanı | 6 | 6 | 6 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- crystalys-members:end -->
