<!-- wiki-i18n source: 35213e745899897b -->
<!-- wiki-i18n title: Boosterlar -->
# Boosterlar {#boosters}

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Boosterlar, geminin savaş, savunma, seviye atlama ve kaynak toplama gücünü artırmak için özelliklerini geçici olarak değiştirir.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Eşya ağacı {#item-tree}

Her Montaj ürünü önce kendi teknolojisini ister; araştırmanın ne kadar sürdüğünü görmek için bir eşyanın üzerine gel. Teknoloji ağacı, yakıt ve hızlandırma: [Araştırma](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster I | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster I -> Shield Wall Booster II
Hull Plating Booster I -> Hull Plating Booster II
Laser Damage Booster I -> Laser Damage Booster II
```
<!-- item-tree:end -->

## Üst üste binme kuralları {#stacking-rules}

Boosterlar toplamsal bir ölçekleme sistemi kullanır:
1. **Bonus yüzdeleri toplanır**: İkisi de %10 lazer hasarı veren iki farklı booster satın alırsan toplam bonusun **%20 lazer hasarı** olur.
2. **Süreler çarpımsal olarak birikir**: _Aynı_ booster birden çok kez satın alınırsa etkin süresi uzar. _Farklı_ boosterların sayaçları yan yana işler.
3. **Sayaç görünümü**: Aktif boosterlar HUD’daki Boosterlar penceresinde görünür; gruplanmış toplam aktif bonusları ve bir sonraki bitiş anını gösterir.
4. **Gösterilen değerler bunları içerir**: hangardaki hasar, kalkan, kalkan dolumu, soğurma, hız ve gövde değerleri ile Pilot penceren; çalışan boosterlarını, Sezon Mağazası güçlendirmelerini, klanının güçlendirmelerini ve yanaştırılmış [P.E.T. birimlerini](/wiki/03-Mechanics/Pets.md) hesaba katar; Savaş özellikleri kartındaki küçük bir *boosterlarla* etiketi bunu belirtir. Kalkan delme, kritik şansı ve menzil boosterlardan etkilenmez.

---

## Aktif boosterlar {#active-boosters}

Her booster temelde **10 saat** sürer ve satın alındığında, teslim alındığında ya da toplandığında hemen devreye girer. Üç **ikinci kademe** booster (Laser Damage Booster II, Shield Wall Booster II ve Hull Plating Booster II) satılmaz: teknolojilerini Skylab’da araştırırsın ([Araştırma](/wiki/03-Mechanics/Research.md)), sonra Montaj’da üretirsin; birini toplamak da satın almak gibi 10 saatini hemen başlatır.

| Ad | Nadirlik | Temel etki (10 saat) | Fiyat (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster I** | Nadir | +%10 lazer hasarı | 20.000 |
| **Laser Damage Booster II** | Nadir | +%10 lazer hasarı | Montaj: 20.000 |
| **Shield Wall Booster I** | Nadir | +%25 kalkan kapasitesi (maksimum kalkan puanı) | 15.000 |
| **Shield Wall Booster II** | Nadir | +%25 kalkan kapasitesi (maksimum kalkan puanı) | Montaj: 15.000 |
| **Hull Plating Booster I** | Nadir | +%10 maksimum gövde puanı | 15.000 |
| **Hull Plating Booster II** | Nadir | +%10 maksimum gövde puanı | Montaj: 15.000 |
| **Shield Regen Booster** | Nadir | +%25 kalkan dolum hızı (saniyede dolan kalkan puanı) | 10.000 |
| **Experience Booster** | Sıradan | +%20 deneyim kazancı | 8.000 |
| **Honor Booster** | Sıradan | +%20 onur puanı kazancı | 10.000 |
| **Resource Magnet Booster** | Nadir | +%25 kargo kutusu verimi | 18.000 |
| **Loot Luck Booster** | Efsanevi | +%5 NPC öldürmelerinde nadir ganimet şansı | 30.000 |

> [!NOTE]
> **Booster mı, amfi mi?** İkisi farklı şeyler. Her booster, adında **Booster** geçen bir eşyadır; sayaçla çalışır ve takılacak bir şeyi yoktur: **Laser Damage Booster I** ve **Laser Damage Booster II**, Mağaza’dan ya da Montaj’dan, 10 saat boyunca %10 lazer hasarı verir. **Damage Amp**, **Crit Amp** ve **Penetration Amp** (kademeler I–IV) ise lazer amfileridir: bir lazerin amfi yuvasına taktığın, sayacı olmayan modüllerdir ([Lazerler ve cephane](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). 0.4.12 öncesinde boosterların adları Damage Amp ve Damage Amp II, Shield Wall ve Shield Wall II, Hull Plating ve Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet ve Loot Luck idi; çalışmakta olan boosterlar yeni adlarıyla sürdü. Hull Plating **Booster**, geminin gövde plakası yuvalarına takılan **Hull Plating** zırhı değildir ([Gövde Kaplaması](/wiki/06-Items/Hull-Plating.md#hull-plating-or-booster)).

---

## Kalkan güçlendirmeleri: üç tür {#shield-boosts-three-kinds}

Kalkanların üç ayrı özelliği vardır ve her kalkan güçlendirmesi bunlardan tam olarak birini artırır. Boosterlar penceresi bunları ayrı tutar; her birinin bir simgesi ve bir toplamı vardır:

| Tür | Nedir | Onu artıran güçlendirmeler |
| :--- | :--- | :--- |
| **Kalkan kapasitesi** | Maksimum kalkan puanın | Shield Wall Booster I, Shield Wall Booster II, kalıcı **Shield Capacity Boost** güçlendirmesi (Sezon Mağazası), yanaştırılmış bir [P.E.T.](/wiki/03-Mechanics/Pets.md) biriminin kalkan güçlendirmesi |
| **Kalkan soğurması** | Her vuruşun kalkanlarının üstlendiği pay (gerisi gövdeye gider); %100’ü geçebilir | Kalıcı **Shield Absorbance Boost** güçlendirmesi (Sezon Mağazası): seviye başına +0,1 puan, 25 WP karşılığında, en fazla +10 puan. Hiçbir booster bunu artırmaz |
| **Kalkan dolumu** | Saniyede dolan kalkan puanı | Shield Regen Booster. Hiçbir kalıcı güçlendirme bunu artırmaz |

Aynı türdeki güçlendirmeler toplanır; başka bir türe asla sayılmaz. Kalıcı güçlendirmeler [Sezonlar arası ilerleme](/wiki/03-Mechanics/Wipe-Timeline.md) bölümünde, özelliklerin kendisi [Kalkan mekaniği](/wiki/03-Mechanics/Shields.md) sayfasında anlatılır.
