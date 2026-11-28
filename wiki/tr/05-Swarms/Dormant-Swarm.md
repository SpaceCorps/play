<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Dormant sürüsü -->
# Dormant sürüsü {#dormant-swarm}

Dormant sürüsü, bir **Dormant Force** ve onun **Dormant Pulse** gemileridir: hiçbir zaman kavgayı başlatmayan ama uyandırıldıklarında çok sert vuran bir gemi grubu. Her dünyanın Tehlike Sektörleri’nde yalnızca bir tane vardır ([Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) için günde bir kez gelen ayrı bir ziyaret vardır). Bir Tehlike Sektörü’nden diğerine dolaşır; sürüler arasındaki en zor savaş ve en zengin ganimettir: en güçlü gemilerden oluşan büyük bir grup için bir savaş. Sezonun 11. gününden itibaren `DS-4` sektöründeki [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) bölgesinde başlar, daha çabuk geri gelir ve iki kat daha fazla öder (bkz. *Bir bakışta* listesi).

## Bir bakışta {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Tehlike Sektörleri `DS-1`, `DS-2`, `DS-3`, `DS-4`; sürü birinden diğerine uçar
- **Kaç tane**: Her dünyada bir tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar (Beta ve Gamma: sezonun 1. gününden itibaren)
- **Lider**: Dormant Force
- **Takipçiler**: 2 × Dormant Pulse, lider ile birlikte uçar
- **Takipçiler şu mesafede kalır**: liderden en fazla 700 birim
- **Lider yok edilince**: Bir Dormant Pulse liderliği devralır
- **Lider yok edilince**: Takipçiler, saldırıyor olsalar bile, lider yok edildikten 30 sn sonra ayrılır
- **Seyahat**: Bir haritada 8–15 dk kalır, sonra başka bir Tehlike Sektörü geçidine uçar. Tehlike Sektörleri dışındaki geçitleri asla kullanmaz ve kara deliğin halkasına asla girmez
- **Geri gelir**: Tüm sürü yok edildikten {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} sonra, rastgele bir Tehlike Sektörü’nde
- **Sezonun 11. gününden itibaren**: Rastgele bir Tehlike Sektörü yerine [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) bölgesinde (`DS-4`) belirir, tüm sürü yok edildikten 30 dk sonra geri gelir ve her gemi ×2 öder (kredi, Thulium, XP ve onur; ganimet aynı kalır)
- **Duyuru**: Tüm dünyadaki pilotlara sürünün ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Tehlike Sektörü haritalarında ve galaksi haritasında bir işaretle gösterilir. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- dormant-glance:end -->

## Üyeler {#the-members}

- **Dormant Force**: tam güçte bir Wraith; lazerleri tipik bir donanımınkinden üç kat sert vurur. Sürüye önderlik eder, vurulana kadar pasiftir ve ona ilk vuran pilota **düz roketler** fırlatır.
- **Dormant Pulse**: tam güçte bir Paragon; aynı türden ağır lazerleri vardır, her biri Dormant Force gemisinin lazerlerinden iki kat sert vurur ve kendi roketleri vardır. Bir Dormant Pulse gemisinin Dormant Force gemisinden daha az lazeri vardır, bu yüzden tüm salvosu Dormant Force gemisininkinden büyüktür ama iki kat değildir (değerler aşağıda). Pulse gemileri Force gemisinin yakınında uçar ve Force gemisi yok edildiğinde biri lider olarak devralır.

Hepsi pasiftir: hiçbir pilotun peşine düşmezler. Birine vurursan, ona yakın olan diğerleri ona ilk vuran pilota karşı savaşa katılır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Onu bul.** Belirdiğinde tüm dünyaya haber verilir ve bir işaret onu Tehlike Sektörü haritalarında ve galaksi haritasında gösterir. *Bir bakışta* listesindeki süre boyunca bir haritada kalır, sonra başka bir Tehlike Sektörü’nün geçidine uçar ve sıçrar; Tehlike Sektörleri dışına açılan bir geçidi asla kullanmaz ve kara deliğin halkasına asla girmez. En yavaş gemisinin hızıyla uçar ve bir pilot gibi ateş altındayken sıçramayı ne başlatır ne bitirir. Sezonun 11. gününden itibaren önce [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) bölgesinin hemen dışında belirir; orada bir grup onu bataklığın toplarından uzakta bekleyebilir; sonra `DS-4` sektörünün bir geçidinden uçarak çıkar.
- **Tek başına ya da birkaç kişiyle yenilemez.** x2 ya da x4 cephaneli Paragon gemileriyle uçan 8. seviye sekiz pilot onu Alpha dünyasında yaklaşık bir dakikada yok eder ve en fazla bir gemi kaybeder; tek bir Paragon yok edilir, x2 cephaneli üç ya da dört Paragon da yok edilir. Beta ve Gamma dünyalarının sürüleri daha güçlüdür ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)), bu yüzden o dünyalar daha büyük gruplar ister.
- **Savaşı lazerleri belirler.** Hep birlikte bir Paragon gemisini bir dakikadan kısa sürede, en iyi kalkanlara sahip olanı bile iki dakikadan kısa sürede yok edebilirler, roket olsun olmasın: hasarını hızlı getir ve elindeki en iyi kalkanları kullan.
- **Gemi gemi.** Her geminin kendi gövdesi ve kendi ödemesi vardır; bu yüzden önce Force ya da bir Pulse yok edilebilir. Sürü, ancak tamamı yok edildiğinde ve *Bir bakışta* listesindeki süre geçtikten sonra yenilenir.

## Liderin üç aşaması {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Bu savaşın üç aşaması vardır ([nasıl işlediği](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); her biri bir kez gerçekleşir.

- **Başlangıçta**: Dormant Pulses içinden biri yaşadığı sürece her vuruşun yalnızca %70 kadarını alır.
- **Üçte ikinin altında**: Dormant Pulses 15 sn boyunca her 2,5 sn bir roket ateşler.
- **Üçte birin altında**: Dormant Pulses hepsi yaşadığı sürece 6 sn boyunca saniyede gövdesinin %5 kadarını onarır.

<!-- mob-ladder:end -->

## Ödüller ve ganimet {#rewards-and-drops}

Her gemi kendi başına, ona verilen hasara göre öder ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)) ve her biri, ona en çok hasar veren pilot için bir kutu düşürür. Asıl ödül **Force kutusudur**: bolca x3 ve x4 cephane, tek türden Destansı roketler ve ara sıra bir N.I.K.E. ya da N.U.K.E. **Pulse** gemileri bir Ancient Control Unit, bir Power Core ya da Dark Matter düşürebilir. Sürüyle bir dakikalık savaş, en çok ödeyen uzaylı olan Crystalys ile bir dakikalık savaştan daha çok öder. Sezonun 11. gününden itibaren her gemi iki kat öder (*Bir bakışta* listesi); kutular aynıdır.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)). Tablolardaki kredi, Thulium, XP ve onur, sezonun 11. gününden önceki ödemedir; o günden itibaren bir öldürme iki kat öder.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Wraith temel alınarak, gövdesinin %100 kadarıyla ve lazer hasarının %300 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır. 5 sn aralıkla düz bir roket fırlatır: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Kalkan | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Hız | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Roket hasarı, en fazla | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Kredi | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Onur | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| Öldürme başına PvE puanı | 25 | 25 | 25 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Paragon temel alınarak, gövdesinin %100 kadarıyla ve lazer hasarının %600 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır. 5 sn aralıkla düz bir roket fırlatır: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Kalkan | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Hız | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Lazer menzili | 800 | 800 | 800 |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Roket hasarı, en fazla | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Kredi | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Onur | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| Öldürme başına PvE puanı | 11 | 11 | 11 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
