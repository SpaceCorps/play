<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
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
- **Geri gelir**: Lider yok edildikten {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- goombah-glance:end -->

## Üyeler {#the-members}

- **Boss Goombah**: sürünün tonunda ve üzerinde adıyla görünen, daha büyük bir Goombah; kendine ait gövdesi, kalkanı ve lazer yaylım ateşi vardır (değerler aşağıda). Pasiftir: bir pilot ona vurana kadar dolaşır, sonra o pilotun peşine düşüp ona ateş eder; sürüsünün yakındaki gemileri de savaşa katılır. Silahının menzili ve hızı bir Goombah gemisininkiyle aynıdır ve gövdesini kendi kendine asla onarmaz. [Üç aşaması](#the-leaders-three-steps) ve bir [özel yetenek](/wiki/03-Mechanics/Special-Abilities.md) bunu değiştirebilir.
- **Goombah Guard**: sürünün tonunda daha küçük bir Goombah. Guard gemileri patronun yakınında kalır, yakınlarındaki bir sürü gemisi vurulduğunda savaşa katılır ve patronun yakınındaki her biri onun gövdesini onarır. Bir Guard, bir Goombah gibi, dinlendikten sonra kendi gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **En güçlü gemilerden oluşan bir grup getir.** x2 cephaneli, 8. seviyeden üç pilot onu Alpha’da yaklaşık 75 saniyede yok eder ve en fazla bir gemi kaybeder; bunlardan ikisinin x4 cephaneye ihtiyacı vardır, daha düşük seviyeli pilotlar ise kazanmaya yetecek hasarı veremez.
- **Patrona ateş et, Guard gemilerine değil.** Bir Guard saniyeler içinde düşer, ama *Bir bakışta* listesinin söylediği sıklıkta yenisi gelir; Guard gemilerinin onardığı da bir grubun verdiği hasarın küçük bir kısmıdır: onları rahat bırakmak biraz zamana mal olur, peşlerine düşmek daha çoğuna.
- **Beta ve Gamma daha zordur.** O dünyaların sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)); bu yüzden daha çok pilot ya da daha iyi cephane gerekir.
- **Sektörü gözle.** `x-4` Alpha’da bir PvP sektörüdür; Beta ve Gamma’da ise `x-3` ve `x-4` öyledir ([Dünyalar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): bir rakip savaşa katılabilir ya da kutuyu bekleyebilir. Grubun bir gemisini gözcü olarak bırak.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, tam güçte ve aynı sektörde; Guard gemileri de birbiri ardına gelir.

## Liderin üç aşaması {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Bu savaşın üç aşaması vardır ([nasıl işlediği](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); her biri bir kez gerçekleşir.

- **Başlangıçta**: 6 sn boyunca her vuruşun yalnızca %50 kadarını alır.
- **Üçte ikinin altında**: 10 sn boyunca hasarı ×1,5 ile, hızı ×1,25 ile çarpılır.
- **Üçte birin altında**: Gövdesinin ve kalkanının %25 kadarını onarır (bir hasar patlaması onu böler) ve bu sırada Goombah Guards onu ×2 hızla onarır.

<!-- mob-ladder:end -->

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
| Gövde | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Kalkan | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Hız | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Kredi | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Onur | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| Öldürme başına PvE puanı | 14 | 14 | 14 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Goombah temel alınarak, gövdesinin, kalkanının ve hasarının %20 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Kalkan | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Hız | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 110 | 165 | 220 |
| Kredi | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Onur | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| Öldürme başına PvE puanı | 3 | 3 | 3 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- goombah-members:end -->
