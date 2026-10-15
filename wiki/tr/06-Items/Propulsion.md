<!-- wiki-i18n source: 526e241c3b279356 -->
<!-- wiki-i18n title: Tahrik -->
# Tahrik ve hız {#propulsion-speed}

Tahrik sistemleri geminin hareket hızını ve manevra kabiliyetini belirler.

## Bir dakikada {#in-one-minute}

- **Motorlar hız üretir, iticiler onların içinde durur ve ona katkı yapar.** Bir motor bir ila üç itici alır (Engine I bir, Engine II iki, Engine III üç); Uyarlanabilir Çekirdek de öyle (kaç tane olduğunu kademesi belirler).
- **İki aile, her birinde dört kademe.** Impulse Thruster ailesi en çok sabit hızı ekler. Momentum Thruster ailesi daha az sabit hız ekler ve hızı daha çok çarpar. İki ailede de her kademe bir altındakinden iki sayıda da daha iyidir.
- **Hangisi nereye.** Kural olarak her yere Impulse Thruster tak: yalnızca tam dolu bir Engine III motorunda (üç itici) I. ve II. kademe Momentum Thruster öne geçer. [Aşağıdaki tablo](#which-thruster-where) sayıları verir. En hızlı Engine III motoru üç Impulse Thruster IV taşır ve 52,5 hız yapar.
- **Nasıl edinilir.** Her ailenin I. kademesi 20.000 krediye mal olur. II. ila IV. kademeler Montaj’da, her biri bir alt kademeden üretilir; bir itici asla aile değiştirmez.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Eşya ağacı {#item-tree}

Her Montaj ürünü önce kendi teknolojisini ister; araştırmanın ne kadar sürdüğünü görmek için bir eşyanın üzerine gel. Teknoloji ağacı, yakıt ve hızlandırma: [Araştırma](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motorlar {#engines}

Motorlar geminin ana itki kaynağıdır. Bir **yetenek yuvasındaki** motor ise bunun yerine sana özel etki sütunundaki **Afterburner** yeteneğini verir: on saniyelik bir hız patlaması (daha fazla motorla daha uzun) ve kendi başına itki eklemez (bkz. [Yetenekler](/wiki/03-Mechanics/Abilities.md)).

| Ad | Nadirlik | Temel hız | Hız bonusu % | Kalkan bonusu % | Yuvalar | Özel etki | Maliyet |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Kalitesiz | +2 | +%2 | -%2 | 1 | Afterburner I | 20.000 kredi |
| **Engine II** | Sıradan | +4 | +%4 | -%8 | 2 | Afterburner II | Yalnızca üretilebilir |
| **Engine III** | Nadir | +6 | +%5 | -%15 | 3 | Afterburner III | Yalnızca üretilebilir |

**Engine II**, [Montaj’da](/wiki/06-Items/Overview.md#upgrading-modules) bir Engine I eşyasından üretilir: 2.000 Thulium, 60 Ship Fragment, 1 Power Core ve 4 Velkonite Reinforced Plate gerekir. **Engine III** orada bir Engine II eşyasından üretilir: 4.000 Thulium, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit ve 4 Dark Matter Plate gerekir ([Dark Matter ve Dark Matter plakaları](/wiki/03-Mechanics/Dark-Matter.md)). Her biri harcadığı motorun büyüleme kademesini korur ve bonusları yeniden belirlenir ([Modül yükseltmeleri](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Önce harcayacağın motoru gemiden çıkar (iticilerini de içinden al): takılı olan ya da itici barındıran bir motor harcanmaz.

Motorların kalkan bonusu eşya verisinde yer alır, ama oyun onu hiç uygulamadı: motorlar kalkanlarını zayıflatmaz ve eşya kartları onu göstermez.

---

## İticiler {#thrusters}

İticiler, hız çıktısını artırmak için motorların ya da Uyarlanabilir Çekirdeklerin içine yerleştirilir. Her biri dört kademeli iki aile vardır: **Impulse Thruster** ailesi en çok sabit hızı ekler ve içinde durduğu motorun hızını biraz çarpar; **Momentum Thruster** ailesi daha az sabit hız ekler ve onu daha çok çarpar. İki ailede de her kademe bir altındakinden hem sabit hızda hem çarpanda daha iyidir. İticili bir motorun (ya da Uyarlanabilir Çekirdeğin) yaptığı hız **kendi temel hızı artı iticilerin sabit hız artışlarıdır; bunun tamamı da iticilerin hız çarpanlarının çarpımıyla çarpılır** ([hız nasıl hesaplanır](/wiki/03-Mechanics/Speed.md)): üç Momentum Thruster IV taşıyan bir Engine III (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, üç Impulse Thruster IV ile (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5 yapar; iki Impulse Thruster IV taşıyan bir Adaptive Core II ise (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 yapar (iki Momentum Thruster IV ile 26,6).

| Ad | Nadirlik | Sabit hız artışı | Hız çarpanı | Maliyet |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Kalitesiz | +4,25 | x1,017 | 20.000 kredi |
| **Impulse Thruster II** | Sıradan | +8,5 | x1,02125 | Yalnızca üretilebilir |
| **Impulse Thruster III** | Nadir | +12,75 | x1,0255 | Yalnızca üretilebilir |
| **Impulse Thruster IV** | Destansı | +14,025 | x1,02975 | Yalnızca üretilebilir |
| **Momentum Thruster I** | Kalitesiz | +3,825 | x1,051 | 20.000 kredi |
| **Momentum Thruster II** | Sıradan | +7,65 | x1,0595 | Yalnızca üretilebilir |
| **Momentum Thruster III** | Nadir | +10,625 | x1,0765 | Yalnızca üretilebilir |
| **Momentum Thruster IV** | Destansı | +11,135 | x1,0935 | Yalnızca üretilebilir |

### Hangi itici nereye {#which-thruster-where}

Impulse daha çok sabit hız ekler, Momentum daha çok çarpar; bu yüzden hangisinin daha hızlı olduğu motorun zaten ne kadar hız yaptığına bağlıdır. Sabit hız, çarpılacak az hızın olduğu yerde en çok işe yarar: bir Uyarlanabilir Çekirdekte (kendi hızı yoktur) ve bir ya da iki iticili motorda. Çarpan, çarpılacak çok hızın olduğu tam dolu bir Engine III motorunda en çok işe yarar, ama orada yalnızca I. ve II. kademe Momentum Thruster kazanır. Her yuvada IV. kademe iticileriyle her birinin yaptığı hız:

| İticilerin yeri | Impulse Thruster IV ile | Momentum Thruster IV ile | Hangisi hızlı |
| :--- | :---: | :---: | :--- |
| Engine I, bir itici | 16,5 | 14,4 | Impulse |
| Engine II, iki itici | 34,0 | 31,4 | Impulse |
| Engine III, bir itici | 20,6 | 18,7 | Impulse |
| Engine III, iki itici | 36,1 | 33,8 | Impulse |
| Engine III, üç itici | 52,5 | 51,5 | Impulse |
| Adaptive Core II, iki itici | 29,7 | 26,6 | Impulse |

- **Düşük kademeler.** Düşük kademeler de aynı yöne gider; iki başa baş durum ve bir istisna vardır. Bir Engine II motorunda iki iticiyle aileler I. ve II. kademede başa baştır (Impulse 0,06 ve 0,24 önde), bir Engine III motorunda iki iticiyle de başa baştırlar (0,1 içinde). III. kademeden itibaren Impulse ikisinde de 1,5 ila 2,6 farkla öndedir. İstisna tam dolu Engine III: orada Momentum I. ve II. kademede 0,6 ve 0,9 farkla, Impulse ise III. ve IV. kademede 0,5 ve 1,0 farkla öndedir.
- **En hızlı Engine III.** Üç Impulse Thruster IV taşır: 52,5; bu, bir Impulse ve iki Momentum Thruster IV ile yapılan 52,1’in ya da üç Momentum Thruster IV ile yapılan 51,5’in biraz üstündedir.

Bir iticinin [Demirhane’den](/wiki/06-Items/Forge.md) gelen hız çarpanı bonusu 1’in üstündeki kısmı büyütür (x1,0935 üzerindeki +%15 bonus x1,1075 yapar) ve Demirhane, x1,05 ya da daha düşük bir çarpana bonus vermez: Impulse ailesinin x1,017 ila x1,02975 değerinde 0,005’ten azını ekler (x1,02975 üzerindeki +%15, x1,034 yapar). Bir Impulse Thruster bir bonus taşır (sabit hızı), bir Momentum Thruster iki.

Her ailenin I. kademesi 20.000 krediye satılır. II. ila IV. kademeler [Montaj’da](/wiki/06-Items/Overview.md#upgrading-modules), her biri aynı ailenin bir alt kademedeki iticisinden üretilir (her kademe bir öncekinden: I’den II, II’den III, III’ten IV), Thulium, ganimet ve plakalarla: II. ya da III. kademe için Skylab’ından 4 Velkonite Reinforced Plate, IV. kademe için 4 Dark Matter Plate ve bir Ancient Control Unit. Bir itici asla aile değiştirmez: I. kademeyi satın alırken Impulse ya da Momentum ailesini seçersin. Her biri harcadığı iticinin büyüleme kademesini korur ve bonusları yeniden belirlenir ([Modül yükseltmeleri](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). İticiler bir [yetenek yuvasına](/wiki/03-Mechanics/Abilities.md) takılmaz; motorların ve Uyarlanabilir Çekirdeklerin içine aittirler.

### Uzaylıları geride bırakmak {#outrunning-aliens}

Uzaylılar 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) ve 230 (Crystalys) hızla uçar. Bir Engine II ve iki iticili bir Ostirion gemisi, Impulse Thruster I ile 221,4 hızla uçar: hâlâ Crystalys hızının altındadır, bu yüzden onu geride bırakmak için Montaj’da üretilmiş bir itici gerekir (Impulse Thruster II ile 230,8, III ile 240,3, IV ile 243,3). Momentum ailesi o gemide aynı ya da biraz daha düşük hızla uçar (Momentum Thruster I ile 221,4; II ila IV ile sırasıyla 230,5, 238,4 ve 240,7): iki ailenin de I. kademesi Crystalys hızının altında, Montaj’da üretilen her kademe ise üstündedir; II. kademe yalnızca 0,8 ve 0,5 farkla.
