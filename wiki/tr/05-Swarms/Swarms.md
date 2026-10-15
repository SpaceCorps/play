<!-- wiki-i18n source: 0c56fb69c3771892 -->
<!-- wiki-i18n title: Sürüler -->
# Sürüler {#swarms}

**Sürü**, galaksinin bir bölümünde bir **lider** önderliğinde dolaşan uzaylı grubudur: çevresindeki her uzaylıdan çok daha güçlü bir patron ve onu koruyan, sürülerden ikisinde ise gövdesini de onaran **takipçiler**. Üç sürü vardır ve her birinin kendi makalesi bulunur:

- [Seeker sürüsü](/wiki/05-Swarms/Seeker-Swarm.md): Boss Seeker ve Seeker Slave gemileri; yeni pilotların uçtuğu sektörlerdeki en küçük sürü.
- [Pirate sürüsü](/wiki/05-Swarms/Pirate-Swarm.md): Pirate Boss ve Pirate Scout gemileri; bir grup için uzun bir savaş.
- [Dormant sürüsü](/wiki/05-Swarms/Dormant-Swarm.md): Dormant Force ve Dormant Pulse gemileri; en güçlü sürü ve en zengin ganimet.

Gemileri **kendi türlerinden uzaylılardır**: kendi adları ve kendi öldürme sayaçları vardır ve hiçbiri Seeker, Phantasm ya da başka bir uzaylı olarak sayılmaz. Bir sürü gemisi, temel aldığı geminin biçimindedir; kendine özgü bir tonda ve üzerinde adıyla görünür; Boss Seeker, çok daha büyük bir Seeker gibidir.

**Clan Warden** herkese açık bir sürü değildir. Bir klan, günlük hattının son adımı için kendine ait bir Clan Warden çağırır ve ona yalnızca o klan zarar verebilir: hiçbir pilot bir sektörde dolaşan bir Clan Warden ile karşılaşmaz ve aşağıdaki tablolar onları listelemez. Bir Clan Warden, sürü patronu gibi hasara göre ödeme yapar ama ganimeti en çok hasar verene giden tek bir kutu değildir: %5 veya daha fazlasını veren her pilot kendi [özel kutusunu](/wiki/03-Mechanics/Cargo.md#private-boxes) alır. Bkz. [Klanlar](/wiki/03-Mechanics/Clans.md#clan-wardens).

## Üç sürü {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Sürü | Yer | Kaç tane | Lider | Takipçiler | Geri gelir |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate sürüsü**](/wiki/05-Swarms/Pirate-Swarm.md) | Her şirketin `x-2` ve `x-3` sektörleri | Bu sektörlerin her birinde bir tane, her dünyada 6 tane | **Pirate Boss** | En fazla 5 × Pirate Scout, 10 sn aralıkla yenisi çıkar | Lider yok edildikten 2 dk sonra, aynı sektörde |
| [**Dormant sürüsü**](/wiki/05-Swarms/Dormant-Swarm.md) | Tehlike Sektörleri `DS-1`, `DS-2`, `DS-3`, `DS-4`; sürü birinden diğerine uçar | Her dünyada bir tane | **Dormant Force** | 2 × Dormant Pulse, lider ile birlikte uçar | Tüm sürü yok edildikten 1 sa sonra, rastgele bir Tehlike Sektörü’nde. Sezonun 11. gününden itibaren: 30 dk sonra, [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) bölgesinde; her gemi ×2 öder |
| [**Seeker sürüsü**](/wiki/05-Swarms/Seeker-Swarm.md) | Her şirketin `x-1` ve `x-2` sektörleri | Bu sektörlerin her birinde bir tane, her dünyada 6 tane | **Boss Seeker** | En fazla 4 × Seeker Slave, 10 sn aralıkla yenisi çıkar | Lider yok edildikten 2 dk sonra, aynı sektörde |

<!-- swarms-list:end -->

## Ne zaman ve nerede {#when-and-where}

Sürüler **İlk Temas** ile belirmeye başlar ve sıfırlamaya kadar kalır (bkz. [Sıfırlama zaman çizelgesi](/wiki/03-Mechanics/Wipe-Timeline.md); gün, aşağıdaki kuralların ilk satırındadır). **Her dünyanın kendi sürüleri** vardır ve aynı yerlerdedir; yani Alpha dünyasındaki Pirate Boss ile Beta dünyasındaki iki ayrı gemidir ve kendi dünyanda yok ettiğin bir sürü başka bir dünyada yok edilmiş olmaz. Yok edilen bir sürü, yukarıdaki tabloda yazan süre sonra geri gelir. Dormant sürüsü sezonun 11. gününde (2. etkinlik) değişir: [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) bölgesinde belirir, daha çabuk geri gelir ve iki kat daha fazla öder.

## Her sürünün kuralları {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Sürüler sezonun 4. gününden sıfırlamaya kadar görünür.
- Bir sürü gemisi vurulduğunda, sürüsünden ona 1.500 birim içinde olan gemiler, ona ilk vuran pilota karşı savaşa katılır.
- Bir lider, her istasyonun ve geçit halkasının kenarından en az 2.500 birim uzakta belirir.
- Bir patron öldürüldüğünde, ona verilen hasarın en az %5 kadarını veren pilot, öldürme ödülünü alır.

<!-- swarms-rules:end -->

## Dünyalar {#the-worlds}

Dünya, bir sürüyü her uzaylıyı ölçeklediği gibi ölçekler ([Dünyalar](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): bir sürü gemisinin gövdesi, kalkanı, kalkan dolumu, lazer hasarı, roket hasarı ve onarımı Alpha değerlerinin aşağıdaki güçle çarpımıdır; bir öldürme de aşağıdaki kazancı öder. Hız, menzil ve ganimet her dünyada aynıdır. Makaleler her geminin değerlerini üç dünyada da verir.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Dünya | Güç | Kazanç |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Pilotlara ne bildirilir {#what-the-pilots-are-told}

Seeker ve Pirate sürüleri, bir patron belirdiğinde ve yok edildiğinde kendi sektörlerindeki pilotlara haber verir. Dormant sürüsü tüm dünyasına haber verir ve pilotlar onu bulabilsin diye Tehlike Sektörü haritalarında ve galaksi haritasında işaretlenir. Bunlar Sistem satırlarıdır: sohbetin **Sistem** sekmesinde, okunmamış sayısıyla birlikte görünür; **Genel** ya da **Yerel** sekmesinde görünmez. Bir patron öldürmesi ayrıca öldürme akışında, öldürmeyi alan pilotu adıyla belirten bir satır alır. Her makalenin *Bir bakışta* listesi kimlere haber verildiğini söyler.

## Bir sürüyle savaşmak {#fighting-a-swarm}

- **Liderler hiçbir zaman kavgayı başlatmaz.** Bir lider, bir pilot ona vurana kadar dolaşır, sonra karşılık verir; sürüsünün ona yakın gemileri de ona ilk vuran pilota karşı savaşa katılır (mesafe yukarıdaki kurallarda verilir). Pirate Scout gemileri bunun istisnasıdır: yaklaşan her pilota saldırırlar. Bir lider gövdesini kendi kendine onarmaz; bu yüzden verdiğin hasar, takipçileri onu onarmadıkça üzerinde kalır; kalkanı her uzaylının kalkanı gibi dolar.
- **Sürü gemileri yalnızca pilotlarla savaşır.** Uzaylılara ateş etmezler, uzaylılar da onlara ateş etmez; [şirket pilotları](/wiki/03-Mechanics/Company-Pilots.md) da onları yok sayar: ne bir sürü gemisini avlarlar ne de ona karşı yardımına gelirler.
- **Roketler.** Pirate Boss ile Dormant Force ve Dormant Pulse gemileri, kendilerine saldıran pilota **düz** roketler, yani [Rivet roketleri](/wiki/06-Items/Rockets.md) fırlatır. Hareket etmeye devam eden bir gemi onlardan kaçar, olduğu yerde duran vurulur.
- **Savaşların ölçeği.** Seeker sürüsü iki pilot içindir, Pirate sürüsü küçük bir grup içindir, Dormant sürüsü en güçlü gemilerden oluşan büyük bir grup içindir; daha büyük dünyalar her uzaylıda olduğu gibi daha çok pilot ister.

## Neler getirmeli {#what-to-bring}

- **Bir grup.** Bir [grupla](/wiki/03-Mechanics/Groups.md) uç: sürüler gruplara göre dengelenmiştir, düşük seviyeli yalnız bir pilot hızla yok edilir ve bir Pirate Boss ile yalnızca en güçlü gemiler tek başına baş edebilir. Dormant sürüsünü kimse tek başına yenemez. Bir sürü ona ilk vuran pilotla savaşır ([Bir uzaylı kimle savaşır](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), bu yüzden işe grubun en sağlam gemisi başlasın.
- **Daha iyi cephane.** x2 cephane veya daha iyisini getir (bkz. [Lazerler ve cephane](/wiki/06-Items/Lasers.md)). Bir sürünün takipçilerinin onarımı, x1 cephaneyle küçük bir grubun verebildiği hasardan fazla olabilir.
- **Kalkan ve onarım**, uzun bir savaş için: geminin yetenekleri ([Yetenekler](/wiki/03-Mechanics/Abilities.md)) dakikalar süren Pirate savaşında en çok işe yarar.
- **Hareket alanı.** Menzilini aştığın bir silahın erişiminin dışında kal ve bir rokete karşı hareket etmeyi bırakma.

## Bir patron öldürmesi nasıl öder {#how-a-boss-kill-pays}

Sıradan bir uzaylı, ona ilk vuran pilota öder ([Savaş](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). Bir sürünün lideri ve her Dormant Pulse ise bunun yerine **verilen hasara göre** öder:

- **Ödeme hasara göre bölüşülür.** Yukarıdaki kurallarda belirtilen payı veya daha fazlasını veren her pilot, verdiği hasarla orantılı olarak ödenir: öldürmenin kredisi, Thulium’u, XP’si ve onuru aralarında bölüşülür. Payın altında kalan pilota hiçbir şey ödenmez.
- **Kargo kutusu en çok hasar veren pilota gider.** Her uzaylıda olduğu gibi 30 saniye boyunca o pilotun (ve klanının) olur, sonra herkes alabilir ([Kargo](/wiki/03-Mechanics/Cargo.md)). Her Dormant gemisinin kendi hasar sayımı ve kendi kutusu vardır.
- **Takipçiler olağan biçimde öder**: Pirate Scout ve Seeker Slave gemileri kendilerine ilk vuran pilota öder ve ödemeleri bir patronunkinin yanında küçüktür.
- **Bir patronun ödemesi, çevresindeki uzaylıları geçecek biçimde ayarlanmıştır.** Bir Pirate Boss ile bir dakikalık savaş, bir Goombah ile bir dakikalık savaştan daha çok öder; Dormant sürüsü ondan da fazla öder; Boss Seeker tam olarak on Seeker öder.
- **Dormant Swamp bölgesinin uzaylıları** (Slumbering Void, Inert Mass ve The Unwakened) bir patron gibi, hasara göre öder ve sıralamana PvE puanı ekler; değerleri [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-aliens) sayfasındadır.

Her öldürme, öldürme istatistiklerinde geminin kendi adı altında sayılır ve sıralamana PvE puanı ekler:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Sürü gemisi | Sürü | Öldürme başına PvE puanı |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate sürüsü | 15 |
| **Pirate Scout** | Pirate sürüsü | 4 |
| **Dormant Force** | Dormant sürüsü | 25 |
| **Dormant Pulse** | Dormant sürüsü | 11 |
| **Boss Seeker** | Seeker sürüsü | 5 |
| **Seeker Slave** | Seeker sürüsü | 1 |

<!-- swarms-points:end -->

Bir sürü öldürmesi başka hiçbir uzaylının öldürmesi sayılmaz: Boss Seeker ya da Seeker Slave, Seeker isteyen bir görev için Seeker değildir ve sıfırlama puanı kilometre taşları ([Sıfırlama zaman çizelgesi](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) yalnızca beş uzaylıya aittir. Sürü gemilerini isteyen görevler [Sürü görevleri](/wiki/03-Mechanics/Quests.md#swarm-missions) altında listelenir.
