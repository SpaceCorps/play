<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Crystalys sürüsü -->
# Crystalys sürüsü {#crystalys-swarm}

Crystalys sürüsü, bir **Boss Crystalys** ve **Crystalys Guard** gemilerinden oluşur: uzaylıların en sağlamı olan [Crystalys](/wiki/04-Aliens/Crystalys.md) gemisinin daha büyük hâli ve onun yakınında kalıp gövdesini onaran muhafızlar. [Tehlike Sektörleri](/wiki/01-General/Danger-Sectors.md) içinde `DS-1`, `DS-2` ve `DS-3` sektörlerinde, her birinde bir tane yaşar ve sektöründen hiç ayrılmaz. Tehlike Sektörleri PvP sektörleridir; bu yüzden savaş, en güçlü pilotlardan oluşan büyük bir grup içindir ve oradaki tek tehlike patron değildir.

## Bir bakışta {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Tehlike Sektörleri `DS-1`, `DS-2`, `DS-3`
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 3 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar (Beta ve Gamma: sezonun 1. gününden itibaren)
- **Lider**: Boss Crystalys
- **Takipçiler**: En fazla 3 × Crystalys Guard, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 500 birim
- **Onarım**: Liderin 600 birim yakınındaki her Crystalys Guard, liderin gövdesini Alpha dünyasında saniyede 250 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 30 sn sonra ayrılır
- **Geri gelir**: Lider yok edildikten {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- crystalys-glance:end -->

## Üyeler {#the-members}

- **Boss Crystalys**: sürünün tonunda ve üzerinde adıyla görünen, daha büyük bir Crystalys; kendine ait gövdesi, kalkanı ve lazer yaylım ateşi vardır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra o pilotun peşine düşüp ona ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Crystalys gemisininkiyle aynıdır ve gövdesini kendi kendine asla onarmaz. [Üç aşaması](#the-leaders-three-steps) ve bir [özel yetenek](/wiki/03-Mechanics/Special-Abilities.md) bunu değiştirebilir.
- **Crystalys Guard**: sürünün tonunda daha küçük bir Crystalys. Guard gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Guard, bir Crystalys gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Büyük bir grup getir.** Alpha’da x2 cephaneli, Paragon ile uçan 8. seviyeden altı pilot, ateşi aralarında dağılırsa yeter; tamamı tek pilota yönelirse dokuz pilot gerekir; x4 cephanede bu sayılar beş ve altıdır. Pilot sayısı arttıkça savaş daha erken biter ve daha az gemi kaybedilir; tek başına bir pilot ise yok edilir.
- **Patrona ateş et, Guard gemilerine değil.** Bir Guard saniyeler içinde düşer, ama *Bir bakışta* listesinin söylediği sıklıkta yenisi gelir; Guard gemilerinin onardığı da bir grubun verdiği hasarın küçük bir kısmıdır: onları rahat bırakmak biraz zamana mal olur, peşlerine düşmek daha çoğuna.
- **Beta ve Gamma daha zordur.** O dünyaların sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)); bu yüzden daha çok pilot ya da daha iyi cephane gerekir.
- **Tehlike Sektörleri PvP’dir.** Bir rakip savaşın ortasında gruba saldırıp kutuyu bekleyebilir: kutu 30 saniye boyunca en çok hasar veren pilotun (ve klanının) olur, sonra herkesin ([Kargo](/wiki/03-Mechanics/Cargo.md)). Yalnız gitme.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Guard gemileri de birbiri ardına gelir.

## Liderin üç aşaması {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Bu savaşın üç aşaması vardır ([nasıl işlediği](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); her biri bir kez gerçekleşir.

- **Başlangıçta**: 8 sn boyunca her vuruşun yalnızca %50 kadarını alır.
- **Üçte ikinin altında**: 700 birimlik bir halka içindeki her gemiye salvolarının 4 kadarıyla vurur ve 4 roket ateşler.
- **Üçte birin altında**: Gövdesinin ve kalkanının %20 kadarını onarır (bir hasar patlaması onu böler) ve 3 Crystalys Guards daha gelir, en fazla 6 canlı.

<!-- mob-ladder:end -->

## Ödüller ve ganimet {#rewards-and-drops}

Boss Crystalys, olduğu savaşın karşılığını öder: onunla bir dakikalık savaş, en çok ödeyen uzaylı olan bir Crystalys ile bir dakikalık savaştan daha çok öder. Ödeme, onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusu en çok hasar veren pilota aittir ve Cataclysite ile Quorvium içerir; ara sıra bir Power Core, bir Ancient Control Unit ya da Dark Matter, x3 ve x4 cephane ve Destansı roketler de çıkar. Guard gemileri az öder ve hiçbir şey düşürmez; onları öldürmek farm yapmanın yolu değildir, çünkü patronla birlikte geri gelirler.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Crystalys temel alınarak, gövdesinin %350 kadarıyla ve lazer hasarının %100 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Kalkan | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Hız | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Onur | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| Öldürme başına PvE puanı | 30 | 30 | 30 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Crystalys temel alınarak, gövdesinin, kalkanının ve hasarının %15 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Kalkan | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Hız | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Lazer menzili | 900 | 900 | 900 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 250 | 375 | 500 |
| Kredi | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Onur | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| Öldürme başına PvE puanı | 6 | 6 | 6 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- crystalys-members:end -->
