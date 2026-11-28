<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Pirate sürüsü -->
# Pirate sürüsü {#pirate-swarm}

Pirate sürüsü, bir **Pirate Boss** ve onun **Pirate Scout** gemileridir: kimseye saldırmayan ve roketlerle karşılık veren kocaman, yavaş bir gemi ile onu koruyup gövdesini onaran, daha hızlı bir gemi sürüsü. Bir şirketin üssü ile sınırı arasındaki, oyunun orta seviyelerinin oynandığı sektörlerde yaşar ve bir grup pilot için hızlı bir öldürme değil, uzun bir savaştır.

## Bir bakışta {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Yer**: Her şirketin `x-2` ve `x-3` sektörleri
- **Kaç tane**: Bu sektörlerin her birinde bir tane, her dünyada 6 tane
- **Belirme**: Sezonun 4. gününden sıfırlamaya kadar (Beta ve Gamma: sezonun 1. gününden itibaren)
- **Lider**: Pirate Boss
- **Takipçiler**: En fazla 5 × Pirate Scout, 10 sn aralıkla yenisi çıkar
- **Takipçiler şu mesafede kalır**: liderden en fazla 900 birim
- **Onarım**: Liderin 600 birim yakınındaki her Pirate Scout, liderin gövdesini Alpha dünyasında saniyede 40 HP onarır
- **Lider yok edilince**: Takipçiler, saldırmıyorlarsa, lider yok edildikten 1 dk sonra ayrılır
- **Geri gelir**: Lider yok edildikten {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} sonra, aynı sektörde
- **Duyuru**: Sektördeki pilotlara liderin ne zaman belirdiği ve ne zaman yok edildiği bildirilir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Öldürme akışı, öldürmeyi alan pilotu adıyla gösterir.

<!-- pirate-glance:end -->

## Üyeler {#the-members}

- **Pirate Boss**: Ironclad gemisini temel alan, onun gücünün bir kısmına sahip bir gemi (değerler aşağıda). Pasiftir ve **hiç lazer ateşlemez**: tek silahı bir **düz roket** ([Roketler](/wiki/06-Items/Rockets.md); hangisi olduğu sektöre bağlıdır, tabloya bak): onu kendisine saldıran pilota fırlatır ve ateş ederken dolaşmaya devam eder. Gövdesini kendi kendine asla onarmaz. [Üç aşaması](#the-leaders-three-steps) ve bir [özel yetenek](/wiki/03-Mechanics/Special-Abilities.md) bunu değiştirebilir.
- **Pirate Scout**: Kitefin gemisini temel alan, onun gücünün bir kısmına sahip bir gemi. Pirate Scout gemileri yaklaşan her pilota saldırır, patronun yakınında kalır ve patronun yakınındaki her biri onun gövdesini onarır.

## Savaş nasıl geçer {#how-the-fight-goes}

- **Patrona ateş et, Scout gemilerine değil.** Scout gemileri patronu onarır, ama onarım patronun gövdesinin yanında küçüktür ve *Bir bakışta* listesinin söylediği sıklıkta yeni bir Scout gelir: Scout gemilerini önce öldüren bir grup onların önüne asla geçemez; yalnızca çok büyük bir grup onları temizleyebilir ve yine de patronu bitirmesi, onları rahat bırakan bir gruptan daha uzun sürer. Scout gemileri sana zaman kaybettirir, savaşı belirlemez.
- **Scout gemilerini uzağa çek.** Bir Scout yalnızca patronun erişimi içindeyken onarır; bu yüzden seni erişim dışına kadar izleyen bir Scout hiçbir şeyi onarmaz ve bir Ostirion bir Scout gemisinden hızlıdır.
- **Hareket etmeye devam et.** Patronun roketi düzdür ve güdümsüzdür: hareket etmeye devam eden gemi ondan kaçar, olduğu yerde duran vurulur.
- **Bir grup getir.** x2 cephaneli Ostirion gemilerindeki üç pilot, `x-2` sektöründe tek gemi kaybetmeden onu indirir, ama ancak zar zor; `x-3` sektöründe ise darbeler paylaşıldığı sürece bile yok edilir; dört pilot Alpha dünyasında onu yaklaşık üç dakikada indirir. x4 cephaneyle `x-3` sektöründe üç pilot onu yaklaşık iki dakikada indirir. Beş pilot, darbeler paylaşıldığında yaklaşık iki buçuk dakikada, tüm ateşi tek pilot aldığında yaklaşık üç dakikada indirir; o durumda iki gemi kaybederler: tüm ateşi tek pilotun almasına izin veren bir grubun beş kişi olması gerekir. Beta dünyasında beş, Gamma dünyasında yedi pilot gerekir; darbeler paylaşılmış olmalıdır (patron orada daha büyüktür ve Scout gemileri daha çok onarır). Alpha dünyasında `x-3` sektöründe x2 cephaneyle tek bir Ostirion tek başına başaramaz, tek bir Paragon da başaramaz, iki Paragon güvenle başarır. Beta ve Gamma dünyalarında `x-3` sektöründe tek bir Paragon x2 cephaneyle de x4 cephaneyle de tek başına yok edilir. Patron ona ilk vuran pilota karşılık verir, bu yüzden işe en sağlam gemi başlasın ve bu kadar uzun bir savaşta yeteneklerini (Emergency Repair, Shield Surge: [Yetenekler](/wiki/03-Mechanics/Abilities.md)) kullan. Hâlâ 2. ya da 3. seviyede olan pilotlar, uçtukları yerde bile, bunun için fazla zayıftır: daha güçlenene kadar uzak dur.
- **Patron geri gelir**: *Bir bakışta* listesindeki süreden sonra, aynı sektörde.

## Liderin üç aşaması {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Bu savaşın üç aşaması vardır ([nasıl işlediği](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); her biri bir kez gerçekleşir.

- **Başlangıçta**: Ona ilk vuran pilota, aralarında 12 derece olan 3 roketlik bir yelpaze ateşler.
- **Üçte ikinin altında**: Bir kerede 5 Pirate Scouts daha çağırır, en fazla 10 canlı. Hiçbir şey ödemezler ve 45 sn sonra giderler.
- **Üçte birin altında**: 10 sn boyunca ×1,8 hızla en yakın geçide uçar, sonra pilotlara döner.

<!-- mob-ladder:end -->

## Ödüller ve ganimet {#rewards-and-drops}

Pirate Boss, olduğu savaşın karşılığını öder: onunla bir dakikalık savaş, bir Goombah ile bir dakikalık savaştan daha çok öder. Ödeme, onunla savaşan pilotlar arasında hasara göre bölüşülür ([patron öldürmesi nasıl öder](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Kutusu en çok hasar veren pilota aittir ve bir **Reinforced Hull Plate**, roketler ve cephane içerebilir. Kutunun değeri, öldürmenin kendi ödemesinin yarısından biraz azdır. Scout gemileri az öder ve hiçbir şey düşürmez.

## Değerler {#the-numbers}

Sürünün gemilerinin üç dünyadaki değerleri ([Dünyalar](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Ironclad temel alınarak, gövdesinin, kalkanının ve hasarının %50 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır. 5 sn aralıkla düz bir roket fırlatır: `x-2` sektöründe [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets), `x-3` sektöründe [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Kalkan | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Lazer hasarı (saniyede bir salvo) | yok | yok | yok |
| Hız | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Lazer menzili | – | – | – |
| Aggro yarıçapı | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca | yalnızca saldırıya uğrayınca |
| Roket hasarı, en fazla | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Kredi | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Onur | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| Öldürme başına PvE puanı | 15 | 15 | 15 |

**Ganimet**: tek bir kutu, en çok hasar veren pilota ait.

| Eşya |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Kitefin temel alınarak, gövdesinin %50 kadarıyla ve lazer hasarının %113 kadarıyla yapılmıştır; hızı ve menzili kaynağıyla aynıdır.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Gövde | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Kalkan | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Lazer hasarı (saniyede bir salvo) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Hız | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Lazer menzili | 700 | 700 | 700 |
| Aggro yarıçapı | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Lideri onarır (her biri, saniyede; yalnızca gövde) | 40 | 60 | 80 |
| Kredi | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Deneyim (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Onur | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| Öldürme başına PvE puanı | 4 | 4 | 4 |

**Ganimet**: yok. Öldürme yalnızca kredi, Thulium, XP ve onur öder.

<!-- pirate-members:end -->
