<!-- wiki-i18n source: 8df4cadc9772c73c -->
<!-- wiki-i18n title: Kalkanlar -->
# Kalkan mekaniği {#shield-mechanics}

Kalkanlar gelen hasarın büyük kısmını soğurur ve geminin gövdesini doğrudan hasardan korur.

## Kalkan hesaplamaları {#shield-calculations}

Geminin nihai kalkan değerleri şöyle hesaplanır:

\[\text{Nihai Kalkan Kapasitesi} = \text{Toplam Temel Kapasite} \times (1,0 + \text{Toplam Kalkan Bonusu Yüzdesi})\]
\[\text{Nihai Kalkan Dolum Hızı} = \text{Toplam Temel Dolum} \times (1,0 + \text{Toplam Kalkan Bonusu Yüzdesi})\]

### 1. Yuva verimi ve azalan getiri {#1-slot-efficiency-diminishing-returns}

Motorlara benzer şekilde, takılı kalkanlar (ve hibrit jeneratörler) en iyiden başlayarak sıralanır ve yuva verimine (çekirdek: %100, destek: %75, yardımcı: %50, bir dronun yuvası: %100, çekirdek yuvası gibi) ve sıralarına bağlı bir azalan getiri eğrisine tabi tutulur. Bir kalkan, kendisinden sayılan kısma göre sıralanır: kapasitesi çarpı yuvasının payı. Dolumun kendi sırası vardır (değeri çarpı yuvanın payı) ve **en iyi dört** kalkan bonusu sayılır. [Dronlarından](/wiki/03-Mechanics/Drones.md) birindeki kalkan, geminin kendi kalkanlarıyla birlikte sıralanır:

- **1. ila 4. kalkan**: **%100** (1,0) marjinal verim.
- **5. kalkan**: **%85** (0,85) marjinal verim.
- **6. kalkan**: **%70** (0,70) marjinal verim.
- **7. kalkan**: **%55** (0,55) marjinal verim.
- **8. ve sonrası**: **%50** (0,50) marjinal verim. (0.4.7 sürümüne kadar bu %25’ti, motorlarla aynı; motorlar hâlâ %25 kullanır, bkz. [Hız](/wiki/03-Mechanics/Speed.md).)

**Daha fazla takmak kalkanını asla düşürmez.** Bir kalkan ya da kalkan hücresi eklemek kalkan kapasiteni ya da dolumunu asla düşürmez: her sayı, sayılana göre en iyiden başlayarak sıralanır, bu yüzden yeni bir parça hak ettiği yeri alır. Soğurma kalkanlarının ortalamasıdır; bu yüzden ortalamandan daha zayıf yeni bir kalkan onu düşürür, bir hücre ise asla.

**Hangar bunu gösterir.** Tüm gücünden daha azı sayılan bir kalkan, motor ya da Uyarlanabilir Çekirdek, yuvasında küçük bir yüzde taşır (örneğin `64%`: destek yuvasında, %75’te, %85’teki 5. kalkan) ve üzerine gelince döküm gösterilir. Eşyalarını yere göre ve bir tanesinin daha neye sayılacağını görmek için savaş özelliklerindeki Kalkanlar ve Hız kutucuklarının üzerine gel. Uçuştaki Gemi penceresi, kalkan çubuğunun ve hızının üzerine geldiğinde aynı listeleri gösterir.

### 2. Kalkan soğurması (hasar paylaşımı) {#2-shield-absorbance-damage-split-}

Soğurma, kalkanlarının her vuruştan aldığı paydır; geri kalanı doğrudan gövde puanına (HP) gider.
- **Kalkan başına**: bir kalkanın soğurması artı ona takılı Kalkan Hücrelerinin soğurması. Tek başına bir kalkanın soğurması **%45 ila %55** olur (Light %45, Basic %50, Heavy %55); hücreler her biri 3 ila 12 puan ekler (Capacity Shield Cell I ila IV +%3, +%4, +%5, +%6; Absorption Shield Cell I ila IV +%6, +%8, +%10, +%12).
- **Ortalama soğurma**: geminin soğurması, çekirdek, destek ve yardımcı yuvalardaki ve dronlarındaki kalkanların basit ortalamasıdır. Uyarlanabilir Çekirdeklerin kendi soğurması yoktur ve ortalamaya girmez (bir Uyarlanabilir Çekirdekteki hücreler yalnızca kapasite ve dolum ekler). Takılı kalkan yokken soğurman %0’dır: gövde her vuruşu alır ve bir Uyarlanabilir Çekirdekteki hücrelerin kalkan puanları kullanılmaz, bu yüzden yanına bir kalkan tak.
- **Bonussuz en fazla %91’tir**: en iyi kalkan en iyi hücrelerle, yani her yuvada üç Absorption Shield Cell IV bulunan bir Heavy Shield Core. Daha zayıf kalkanları karıştırmak ortalamayı düşürür. Hiçbir Sezon Mağazası güçlendirmesi ve hiçbir Demirhane bonusu bu sayının parçası değildir.
- **Örnek**: iki Absorption Shield Cell I takılı bir Basic Shield Core (%50) %62’dir; bir Light Shield Core (%45) ekle, ortalama %53,5 olur.
- **Bu özellik %100 ile sınırlı değildir.** Saldıranın *kalkan delmesi* düşülmeden önce, kalkanlarının bir vuruştan alacağı paydır; bu yüzden bir gemi bir vuruşun tamamından fazlasını taşıyabilir: %112, %12’ye kadar delmesi olan bir saldıranın vuruşunun tamamını yine alır.

#### Kalkan delme {#shield-penetration}

Bazı saldırıların bir **kalkan delmesi** vardır: o vuruş için soğurmandan düşülen puanlar. Kalkanlarının aldığı pay:

\[\text{Kalkan Payı} = \text{sınırla}(\text{Soğurma} - \text{Delme},\ 0,\ \%100)\]

- Kalkanlar vuruşun en fazla `round(damage x share)` kadarını alır; gövde geri kalanını alır. Payına göre çok düşük bir kalkan farkı gövde puanına geçirir ve kalkanlar 0’daysa tüm hasar doğrudan gövde puanına gider.
- **Delme nereden gelir**: doğrudan bir roketin *kalkan delmesi* (Lancet I %10, Lancet II %25, Lancet III %35, Rivet I %5, Rivet II %25, Rivet III %35, N.I.K.E. %35; alan patlamalarında yoktur, bkz. [Roketler](/wiki/06-Items/Rockets.md)) ve lazer cephanesinin (Ultra Core %5, Experimental Fusion Core %10; bkz. [Lazerler ve Cephane](/wiki/06-Items/Lasers.md)). Uzaylıların yoktur, x1 ve x2 cephanenin de yoktur. Bir lazer vuruşu ayrıca atıcının lazerlerindeki Penetration Amp bonusunu (yuva başına +%5 ila +%20, lazerleri üzerinden ortalama) ve bir dron formasyonunun delmesini (Gemini +%15; Stiletto yalnızca doğrudan bir roketin delmesine +%35 ekler) alır; doğrudan bir roket formasyonunkini kendisininkine ekler. **Toplamı hiçbir şey sınırlamaz**: kalkanlar, soğurmadan bunların hepsi düşülmüş hâlini alır; vuruşun hiçbirini almayacak noktaya kadar da düşebilir ([bir lazer vuruşunun nasıl toplandığı](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Örnekler**: %91 soğurma, bir Lancet III roketine (%35) karşı: kalkanlar vuruşun %56’sini, gövde %44’sini alır. %100 soğurma ona karşı: %65 ve %35. %112 soğurma, %12 delmeye karşı: vuruşun tamamı. %45 (tek başına bir Light Shield Core), %35’e karşı: kalkanda %10, geri kalanı gövdede. Bir roket tek başına hiçbir çekirdeği tamamen delmez, ama Stiletto formasyonlu bir Lancet III (%35 + %35 = %70), tek başına bir Light Shield Core (%45) için vuruştan kalkana hiç pay bırakmaz; en iyi lazer (%85) de öyle: o lazere karşı en iyi kalkan (%91) vuruşun %6’ünü, gövde %94’sını alır.
- Uzaylıların soğurma özelliği yoktur: her vuruş, vuruşun delmesi düşüldükten sonra %80 kalkana / %20 gövdeye bölünür.
- Siphon Battery cephanesinin hasarı yalnızca kalkandan düşer: soğurma ve delme buna karışmaz.

**Kalkanların hiçbir şey almadığı yerler.** Soğurmaya eşit ya da ondan yüksek bir delme, kalkanlara vuruştan hiçbir pay bırakmaz: gövde hepsini alır. Tablo, kalkanların en iyi lazerin (%85; Experimental Fusion Core yerine bir Antimatter Battery kullanırsan x3 hasarla %95) ve en iyi doğrudan roketin (Stiletto formasyonlu bir Lancet III ya da Rivet III, %70) tek bir vuruşundan ne aldığını gösterir:

| Kalkan | Soğurma | Kalkanların aldığı, en iyi lazer (%85) | Kalkanların aldığı, en iyi doğrudan roket (%70) |
| :--- | ---: | ---: | ---: |
| Light Shield Core | %45 | %0 | %0 |
| Basic Shield Core | %50 | %0 | %0 |
| Heavy Shield Core | %55 | %0 | %0 |
| Bonussuz en iyi kalkan | %91 | %6 | %21 |
| %100’lük bir kalkan | %100 | %15 | %30 |
| %120’lik bir kalkan | %120 | %35 | %50 |

#### %100’e ulaşmak ve aşmak {#reaching-and-passing-100-}

- **Bonussuz**: en fazla %91 (yukarıda).
- **Shield Absorbance Boost**: sıfırlama puanıyla satın alınan kalıcı bir Sezon Mağazası güçlendirmesi, **seviye başına +0,1 puan, en fazla +10 puan** (100 seviye, her biri 25 WP). Geminin soğurmasına sabit puan ekler, kalkanı olan her gemide aynıdır: %91, 4 seviyeyle (100 WP) %91,4 olur; Light Shield Core için %45 olan soğurma 12 seviyeyle (300 WP) %46,2 olur. Kalkan takılı olmayan bir gemi %0’da kalır. 100 seviye 2.500 WP tutar, birkaç sıfırlamalık bir hedeftir: sıfırlama puanı kaynakları (öldürme kilometre taşları, görevler ve beş Dormant Knowledge araştırması) bir sıfırlamada en fazla 1.105 WP öder ve her sıfırlamada yeniden başlar, rütben sıfırlamada 5 ile 400 arası ekler ve 1.105 WP 44 seviye, +4,4 puan alır. Bkz. [Sezon ve sıfırlama puanları](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Demirhane**: kalkanlar ve kalkan hücreleri, özelliği çarpan bir **Soğurma** bonusu alabilir: %55’lik bir kalkanda +%5, +2,75 puandır. Tam dövülmüş Ebedi bir en iyi set (bir çekirdek ve üç hücre, her bonus en üst değerde, +%15) 13,65 puana kadar ekler, ortalama yaklaşık 11 (bkz. [Demirhane](/wiki/06-Items/Forge.md)).
- **Field Theory**: Pilot araştırması Field Theory I, II ve III ([Araştırma](/wiki/03-Mechanics/Research.md#pilot-technologies)) bütün gemilerinin soğurmasına, her seviye bir öncekinin üstüne eklenmeden, toplamda **+4, +7 ve +10 puan** ekler; bedeli kredi, Thulium ve Dark Matter’dır. Sezon Mağazası güçlendirmesi gibi kalkanı olan her gemide sabit puandır ve sıfırlamadan sonra da kalır.
- **Kalkan soğurması**: [pilot becerisi](/wiki/03-Mechanics/Pilot-Skills.md#the-stats), geminin yukarıdaki her şeyden sahip olduğu soğurmaya 100. seviyede en fazla **+5 puan** ekler; toplam için bir üst sınır yoktur: %119’daki bir gemi %124’e çıkar, kalkan takılı olmayan bir gemi ise %0’da kalır. **Birlikte** maddesindeki rakamlara girmez.
- **Birlikte**: bonussuz %91, +4,4 puan güçlendirme (bir sıfırlamanın 1.105 sıfırlama puanı), en fazla +13,65 puan Demirhane bonusu ve Field Theory III’ten +10 puan bir sıfırlamadan sonra en fazla **%119,05** eder; bu, [tasarım](/wiki/03-Mechanics/Ship-Designs.md) ve [formasyon](/wiki/03-Mechanics/Formations.md) kullanmayan sade bir gemi için geçerlidir; güçlendirmenin 100 seviyesinin hepsiyle (+10 puan, 2.500 WP) %124,65 olurdu. %10 kalkan soğurması veren bir tasarım (Paragon BUCKY, Ironclad DUMA, Wraith ATARAXIS) ile Rampart formasyonu (%17), güçlendirmenin ve Field Theory’nin sabit puanları eklenmeden önce kalkanların soğurmasıyla çarpılır; ikisini de taşıyan aynı gemi bir sıfırlamadan sonra **%149,1** eder (100 seviyenin hepsiyle %154,7). Üçünün her biri tek başına %100’ü aşar: sınırındaki güçlendirme ve Field Theory III %101 yapar, en iyi değerleri alan tam bir Ebedi set %104,65; Ebedi bir set Field Theory III ile birlikte %109 ile %115 arasına ulaşır ve güçlendirmenin seviyeleri bunun üstüne gelir. Bu rakamların hepsi yalnızca sıfırlama puanı kaynaklarını sayar; rütbenin sıfırlamada ödediği 5 ile 400 sıfırlama puanını saymaz, bu puanlarla güçlendirmenin daha fazla seviyesi alınır.

### Kalkan güçlendirmeleri: kapasite, soğurma, dolum {#shield-boosts-capacity-absorbance-recharge}

Her kalkan güçlendirmesi üç özellikten birini yükseltir ve Boosterlar penceresinde kendi türünün altında listelenir:

- **Kapasite** (en yüksek kalkan puanı): Shield Wall Booster I ve II ile kalıcı kalkan kapasitesi güçlendirmesi.
- **Soğurma** (kalkanlarının aldığı vuruş payı): kalıcı kalkan soğurması güçlendirmesi (seviye başına +0,1 puan, en fazla +10 puan) ve Kalkan soğurması pilot becerisi (en fazla +5 puan).
- **Dolum** (saniyede geri gelen kalkan puanı): Shield Regen Booster.

Sayılar için [Boosterlar](/wiki/06-Items/Boosters.md) sayfasına bak.

---

## Kalkanın pasif yenilenmesi {#shield-passive-regeneration}

Kalkanlar, savaşa hazır kalman için zamanla pasif olarak yenilenir.

- **Saniyelik yenilenme**: Kalkanlar en yüksek kapasitenin altındaysa, saniyede dolum hızın kadar kalkan puanı geri gelir.
- **Savaşta kesinti (15 sn gecikme)**: Hasar alırken yenilenme durur ve yalnızca **15 saniye** hiç hasar alınmazsa yeniden başlar. [Dron formasyonlarından](/wiki/03-Mechanics/Formations.md) Adamant ve Redoubt bunun istisnasıdır: kalkanı her saniye geri verirler, savaşta bile.
