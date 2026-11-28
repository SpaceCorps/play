<!-- wiki-i18n source: 2eff9c368449da99 -->
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
- **Geri gelir**: Lider yok edildikten {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- phantasm-glance:end -->

## Üyeler {#the-members}

- **Boss Phantasm**: sürünün tonunda ve üzerinde adıyla görünen, daha büyük bir Phantasm; kendine ait gövdesi, kalkanı ve lazer yaylım ateşi vardır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra o pilotun peşine düşüp ona ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Phantasm gemisininkiyle aynıdır ve gövdesini kendi kendine asla onarmaz. [Üç aşaması](#the-leaders-three-steps) ve bir [özel yetenek](/wiki/03-Mechanics/Special-Abilities.md) bunu değiştirebilir.
- **Phantasm Guard**: sürünün tonunda daha küçük bir Phantasm. Guard gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Guard, bir Phantasm gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Bir grup getir.** x2 cephaneli, 4–5. seviyeden üç pilot onu Alpha’da yaklaşık bir buçuk dakikada yok eder ve en fazla bir gemi kaybeder; bu seviyeden tek bir pilot yok edilir, iki pilot ise ancak zar zor kazanır, o da yalnızca darbeler paylaşıldığında. Daha iyi gemiler ve x4 cephane işi çok hızlandırır.
- **Patrona ateş et, Guard gemilerine değil.** Bir Guard saniyeler içinde düşer, ama *Bir bakışta* listesinin söylediği sıklıkta yenisi gelir; Guard gemilerinin onardığı da bir grubun verdiği hasarın küçük bir kısmıdır: onları rahat bırakmak biraz zamana mal olur, peşlerine düşmek daha çoğuna.
- **Beta ve Gamma daha zordur.** O dünyaların sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)); bu yüzden daha çok pilot ya da daha iyi cephane gerekir.
- **Sektörü gözle.** `x-4` Alpha’da bir PvP sektörüdür; Beta ve Gamma’da ise `x-3` ve `x-4` öyledir ([Dünyalar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): bir rakip savaşa katılabilir ya da kutuyu bekleyebilir. Grubun bir gemisini gözcü olarak bırak.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Guard gemileri de birbiri ardına gelir.

## Liderin üç aşaması {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Bu savaşın üç aşaması vardır ([nasıl işlediği](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); her biri bir kez gerçekleşir.

- **Başlangıçta**: Phantasm Guards her biri kendi gövdesinin %10 kadar bir kalkan katmanı kurar.
- **Üçte ikinin altında**: Kopyalarından 3 tanesi belirir ve gerçeği bir halka taşır.
- **Üçte birin altında**: Pilotlardan yaklaşık 2.500 birim uzağa ışınlanır ve Phantasm Guards sapasağlam etrafına döner.

<!-- mob-ladder:end -->

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
| Gövde | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Kalkan | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Hız | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Onur | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| Öldürme başına PvE puanı | 8 | 8 | 8 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Phantasm temel alınarak, gövdesinin, kalkanının ve hasarının %50 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Kalkan | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Hız | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 30 | 45 | 60 |
| Kredi | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Onur | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| Öldürme başına PvE puanı | 1 | 1 | 1 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- phantasm-members:end -->
