<!-- wiki-i18n source: 39eb60672313a89b -->
<!-- wiki-i18n title: Kalkanlar -->
# Kalkanlar ve savunma {#shields-defense}

Savunma modülleri kalkan kapasitesi sağlar, hasarı soğurur ve savunmalarını yeniden doldurur.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Eşya ağacı {#item-tree}

Her Montaj ürünü önce kendi teknolojisini ister; araştırmanın ne kadar sürdüğünü görmek için bir eşyanın üzerine gel. Teknoloji ağacı, yakıt ve hızlandırma: [Araştırma](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 50 Ship Fragment, 8 Reinforced Hull Plate, 20 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 50 Ship Fragment, 8 Reinforced Hull Plate, 20 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 50 Ship Fragment, 10 Reinforced Hull Plate, 2 Power Core, 25 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 50 Ship Fragment, 10 Reinforced Hull Plate, 2 Power Core, 25 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 5000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 5000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I => Adaptive Core II => Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Kalkan çekirdekleri {#shield-cores}

Aktif savunma bariyerleri oluşturmak için kalkan çekirdeklerini geminin jeneratör yuvalarına ya da [dronlarına](/wiki/03-Mechanics/Drones.md) tak (bir dronun yuvası çekirdek yuvası sayılır). Ağır kalkanların hızını düşürdüğünü unutma. Bir **yetenek yuvasındaki** kalkan çekirdeği ise bunun yerine sana özel etki sütunundaki **Shield Surge** yeteneğini verir: on saniye boyunca bir kalkan onarımı; kendi başına kalkan eklemez (bkz. [Yetenekler](/wiki/03-Mechanics/Abilities.md)).

| Ad | Nadirlik | Kapasite | Dolum hızı | Soğurma | Kalkan % | Hız % | Hücre yuvaları | Özel etki | Maliyet |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Kalitesiz | 10.000 | 333/sn | %45 | +%5 | -%1 | 1 | Shield Surge I | 20.000 kredi |
| **Basic Shield Core** | Sıradan | 15.000 | 500/sn | %48 | +%10 | -%3 | 2 | Shield Surge II | 2.000 Thulium |
| **Heavy Shield Core** | Nadir | 25.000 | 833/sn | %50 | +%20 | -%5 | 3 | Shield Surge III | Yalnızca üretilebilir |

**Heavy Shield Core**, [Montaj’da](/wiki/06-Items/Overview.md#upgrading-modules) bir Basic Shield Core eşyasından üretilir: 4.000 Thulium, 30 Cataclysite, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit ve 4 Dark Matter Plate gerekir ([Dark Matter ve Dark Matter plakaları](/wiki/03-Mechanics/Dark-Matter.md)). Harcadığı çekirdeğin büyüleme kademesini korur ve bonusları yeniden belirlenir ([Modül yükseltmeleri](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Önce Basic Shield Core eşyasını gemiden çıkar (hücrelerini de içinden al): takılı olan ya da hücre barındıran bir çekirdek harcanmaz.

**Soğurma**, kalkanlarının her vuruştan üstlendiği paydır; gerisini gövde alır. Tek başına bir kalkan **%45 ile %50 arasındadır**, gerisini hücreleri ekler: en iyi kalkan ile en iyi hücreler (üç Absorption Shield Cell IV taşıyan bir Heavy Shield Core) **%80** yapar; bu, bir geminin hiçbir ek güçlendirme olmadan sahip olabileceği en yüksek değerdir. Buna iki kalıcı güçlendirme eklenir: Sezon Mağazasındaki Shield Absorbance Boost güçlendirmesi (seviye başına +0,1 puan, 100 seviye, her biri 25 sıfırlama puanı) ve Demirhane’nin soğurma bonusları. Bugünkü sıfırlama puanı kaynakları (üst sınırlarında toplam 855, sıfırlamalar boyunca taşınır; daha fazla kaynak planlanıyor) bu 100 seviyeden 34’ünü (+3,4 puan) satın alır; bu, tamamen dövülmüş Ebedi bir setle yaklaşık **%95** eder. Yine de değer %100 ile sınırlı değildir: saldıranın *kalkan delmesi* ondan düşülür; yani bir geminin %100’ün üzerindeki kısmı, delmeye karşı güvenlik payıdır. Bkz. [Kalkan mekaniği](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Hibrit jeneratörler (Uyarlanabilir Çekirdekler) {#hybrid-generators-adaptive-cores-}

Uyarlanabilir çekirdekler, kalkan ve hız yeteneklerini birleştiren hibrit jeneratörler gibi çalışır. Yuvalarına hem iticileri hem kalkan hücrelerini kabul ederler (yuva başına bir modül, ikisinden biri). Kalkan ve hız bonusları bir kalkanınki ya da bir motorunki gibi sayılır (en iyi dördü, yuvanın payıyla çarpılarak). Soğurmaları yoktur: geminin soğurmasını değiştirmezler ve içlerindeki hücreler yalnızca kapasite ve dolum ekler. Bir vuruştan yalnızca kalkanlar pay alır; bu yüzden bir Uyarlanabilir Çekirdekteki hücreler için gemide bir kalkan da gerekir.

| Ad | Nadirlik | Kalkan bonusu % | Hız bonusu % | Yuvalar | Özel etki | Maliyet |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Kalitesiz | +%4 | +%2,4 | 1 | — | 100.000 kredi |
| **Adaptive Core II** | Sıradan | +%6,4 | +%3,2 | 2 | — | Yalnızca üretilebilir |
| **Adaptive Core III** | Nadir | +%8 | +%4 | 3 | — | Yalnızca üretilebilir |

**Adaptive Core II**, [Montaj’da](/wiki/06-Items/Overview.md#upgrading-modules) bir Adaptive Core I eşyasından üretilir: 2.000 Thulium, 60 Ship Fragment, 1 Power Core ve 4 Velkonite Reinforced Plate gerekir. **Adaptive Core III** orada bir Adaptive Core II eşyasından üretilir: 4.000 Thulium, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit ve 4 Dark Matter Plate gerekir ([Dark Matter ve Dark Matter plakaları](/wiki/03-Mechanics/Dark-Matter.md)). Her biri harcadığı çekirdeğin büyüleme kademesini korur ve bonusları yeniden belirlenir ([Modül yükseltmeleri](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Önce harcayacağın çekirdeği gemiden çıkar (iticilerini ve hücrelerini de içinden al): takılı olan ya da modül barındıran bir çekirdek harcanmaz.

---

## Kalkan hücreleri {#shield-cells}

Kalkan hücreleri, çekirdeği güçlendirmek için kalkan çekirdeklerinin ya da Uyarlanabilir Çekirdeklerin içine takılır (çekirdeğin yuvası kadar). Bir kalkan çekirdeğinde soğurmasını da puan olarak artırırlar; onunla birlikte kalkanlarının her vuruştan üstlendiği pay da artar. Dört kademeli iki aile vardır: **Capacity Shield Cell** ailesi en çok kalkan ve dolum, **Absorption Shield Cell** ailesi en çok soğurma ekler (her kademede, o kademedeki Capacity hücresinin iki katı soğurma ve yarısı kadar kalkan ile dolum). Capacity, dövüşü kalkanın bitirdiği bir gemiye, Absorption dövüşü gövdenin bitirdiği bir gemiye yarar. Yuvaları tek tür hücreyle dolu bir çekirdek: Light Shield Core (1 yuva) %47 ile %55, Basic Shield Core (2 yuva) %52 ile %68, Heavy Shield Core (3 yuva) %56 ile %80 arasındadır; I. kademe Capacity hücrelerinden IV. kademe Absorption hücrelerine kadar. Çekirdeği çıkarmak ya da bir [Demirhane](/wiki/06-Items/Forge.md) birleştirmesinde donör olarak harcamak, hücrelerini envantere geri verir.

| Ad | Nadirlik | Kapasite artışı | Dolum artışı | Soğurma artışı | Maliyet |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Kalitesiz | +3.000 | +250/sn | +%2 | 30.000 kredi |
| **Capacity Shield Cell II** | Sıradan | +6.000 | +500/sn | +%3 | Yalnızca üretilebilir |
| **Capacity Shield Cell III** | Nadir | +9.000 | +750/sn | +%4 | Yalnızca üretilebilir |
| **Capacity Shield Cell IV** | Destansı | +12.000 | +1.000/sn | +%5 | Yalnızca üretilebilir |
| **Absorption Shield Cell I** | Kalitesiz | +1.500 | +125/sn | +%4 | 30.000 kredi |
| **Absorption Shield Cell II** | Sıradan | +3.000 | +250/sn | +%6 | Yalnızca üretilebilir |
| **Absorption Shield Cell III** | Nadir | +4.500 | +375/sn | +%8 | Yalnızca üretilebilir |
| **Absorption Shield Cell IV** | Destansı | +6.000 | +500/sn | +%10 | Yalnızca üretilebilir |

Her ailenin I. kademesi 30.000 krediye satılır. II. ila IV. kademeler [Montaj’da](/wiki/06-Items/Overview.md#upgrading-modules), her biri aynı ailenin bir alt kademedeki hücresinden üretilir (her kademe bir öncekinden: I’den II, II’den III, III’ten IV), Thulium, ganimet ve plakalarla: II. ya da III. kademe için Skylab’ından 4 Velkonite Reinforced Plate, IV. kademe için 4 Dark Matter Plate ve bir Ancient Control Unit. Bir hücre asla aile değiştirmez: I. kademeyi satın alırken Capacity ya da Absorption ailesini seçersin. Yeni hücre harcadığı hücrenin büyüleme kademesini korur ve bonusları yeniden belirlenir ([Modül yükseltmeleri](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Hücreler bir [yetenek yuvasına](/wiki/03-Mechanics/Abilities.md) takılmaz; kalkanların ve Uyarlanabilir Çekirdeklerin içine aittirler.
