<!-- wiki-i18n source: a5842e3fb46a29a0 -->
<!-- wiki-i18n title: Envanter -->
# Envanter ve ekipman {#inventory-equipment}

Hangar, gemilerini ve ekipmanını yönetmeni sağlar. Eşyaları etkili biçimde takmak, hayatta kalmanın ve üstünlük kurmanın anahtarıdır. Bunu istasyonda yapabilirsin, uçuşta da güvenli bir bölgenin içinden: [Uçuşta Hangar](/wiki/03-Mechanics/Hangar.md) sayfasına bak.

![The Hangar's inventory: the category chips are one glyph each (the name is the tooltip) with the count of what you hold](../../img/wiki-img/shots/inventory-chips.jpg)
![Dragging a rectangle over the empty space of the inventory: every tile it touches is selected and the title row counts them](../../img/wiki-img/shots/inventory-marquee.jpg)

## Ekipman yuvaları ve özellik verimleri {#equipment-slots-stat-efficiencies}

Geleneksel uzay oyunlarının aksine SpaceCorps’ta, takılan modüllerin etkisini ölçekleyen, dinamik kademeli ekipman yuvaları bulunur.

- **Lazer yuvaları**: Saldırı silahları (lazerler) içindir. Bunlar her zaman **%100 hasar ve menzille** çalışır.
- **Jeneratör yuvaları**: Kalkanlar, motorlar ve Uyarlanabilir Çekirdekler için ortak yuvalardır. Üç verim bandına ayrılırlar ve bir eşyanın temel değerlerinin ne kadarının sayılacağını bant belirler. Hangarda her bandın adının yanında, onu açıklayan bir (i) vardır:
  - **Çekirdek yuvaları**: Buraya konan eşyalar temel değerlerinin **%100**’ünü alır. Her gemide vardır: en güçlü kalkanlarını ve motorlarını buraya koy.
  - **Destek yuvaları**: Buraya konan eşyalar temel değerlerinin **%75**’ini alır (örneğin %75 hız veya kalkan kapasitesi). Her gemide vardır.
  - **Yardımcı yuvalar**: Buraya konan eşyalar temel değerlerinin **%50**’sini alır. Yalnızca bazı gemilerde vardır (Nomad gemisinde 1, Paragon ve Storm gemilerinde 2, Ironclad gemisinde 3, Wraith gemisinde 4; Protos, Kitefin ve Ostirion gemilerinde hiç yoktur). Fazladan, daha zayıf kalkanlar ve motorlar için idealdir; en güçlülerini ise çekirdek yuvalarına koy.
  - **Dron yuvaları**: Dronlarından birindeki bir kalkan, çekirdek yuvasındaki gibi sayılır: değerlerinin **%100**’ünü alır ([Dron mekanikleri](/wiki/03-Mechanics/Drones.md)).
  - **Atanmamış/eski yuvalar**: Buraya konan eşyalar özelliklere katkı yapmaz.
  - **Yığılma da azalır**: kalkanlar ve motorlar en güçlüden başlayarak sıralanır (her birinin yuvasının payı uygulandıktan sonra saydığı değere göre), ardından bandın payı sıralarının payıyla çarpılır: 1–4. sıradakiler tam sayılır, 5–7. sıradakiler sırasıyla %85, %70 ve %55 sayılır; 8. ve sonrası kalkanlarda %50, motorlarda %25 sayılır. [Kalkanlar](/wiki/03-Mechanics/Shields.md) ve [Hız](/wiki/03-Mechanics/Speed.md) sayfalarına bak.
- **Ekstra yuvalar**: Repair Drone gibi özel yardımcı eşyalar içindir. Protos, Kitefin, Ostirion ve Nomad gemilerinde iki, ürettiğin Paragon, Ironclad, Wraith ve Storm gemilerinde üç tane vardır. Extra Slots CPU eşyaları ([Ekstralar](/wiki/06-Items/Extras.md#extra-slots-cpus)) 3, 5 veya 7 yuva daha ekler.
- **Gövde plakası yuvaları**: Gövde ekleyen [Gövde Kaplaması](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) içindir. Yalnızca ürettiğin dört gemide bulunur (Paragon gemisinde 5, Storm gemisinde 7, Ironclad gemisinde 15 ve Wraith gemisinde 9); her biri Skylab’da araştırana kadar kilitlidir ve iki konfigürasyonda da aynıdır.

## Envanter sırası {#inventory-order}

Envanter, eşyalarını Mağaza’yla aynı sırayla listeler; onları hangi sırayla satın aldığın, ürettiğin ya da bulduğun fark etmez. Birbirine ait türler yan yana durur: lazerler, lazer amfileri ve lazer cephanesi; kalkanlar ve kalkan hücreleri; motorlar ve iticiler; Uyarlanabilir Çekirdekler; ekstralar (Repair Drone); dronlar ve dron formasyonları; ardından kaynaklar. Bir türün içinde en ucuz olan başa gelir (önce kredi, sonra Thulium), ardından fiyatı olmayanlar gelir: yalnızca üretilebilen ekipman ve düşen eşyalar, en zayıf nadirlikten başlayarak (aynı nadirlikteki lazerlerde en zayıf hasar önce). Lazer cephanesi x1’den x4’e sıralanır, ardından Siphon Battery gelir. Roketler türüne göre (tek hedefliler alan hasarlılardan, güdümlüler düz gidenlerden önce), sonra kademesine göre sıralanır; bu yüzden Thulium’a mal olan Destansı roket kendi türünde en sona kalır. Bir eşyanın kopyaları büyüleme kademesine göre dizilir. Izgaranın üstünde, her tür için bir düğme aynı sırayı izler; her biri aramanın o türde bulduğu eşya sayısını gösterir. Her düğme kendi başına açılıp kapanır; böylece lazerler, kalkanlar ve motorlarla uğraşırken cephaneyi ve Repair Drone eşyalarını gizleyebilirsin: bir türü göstermek veya gizlemek için düğmesine tıkla, yalnızca o tür açık kalsın diye Shift+tıkla (veya çift tıkla), diğerlerini geri getirmek için tekrar tıkla. **Tümü** her türü gösterir, **Hiçbiri** hepsini gizler; böylece yalnızca istediklerini açabilirsin. Üstü çizili düğme kapalı, onay işaretli düğme açıktır. Arama açık olan türlerde çalışır ve seçimin pilotunla birlikte hatırlanır. Her şey gizliyse ızgara bunu söyler ve **Tüm kategorileri göster** düğmesini sunar.

## Satılabilir eşyalar {#marketable-items}

Kazandığın eşyalar (düşenler, görev ödülleri ve Montaj ile Demirhane’nin ürettikleri) kutucuğunda küçük bir **Satılabilir** etiketi taşır; eşya kartında da “Satılabilir” yazar, yalnızca bazı adetleri satılabilen bir yığında ise “Satılabilir (5 adetten 3 tanesi)”. Kategori düğmelerinin yanındaki **Yalnız satılabilir** düğmesi yalnızca bu eşyaları gösterir. Etiketli bir eşyanın çöp kutusunun yanındaki **tokmak**, [Açık Artırma](/wiki/03-Mechanics/Auction.md) sayfasının satış penceresini açar (uçuşta görünmez: satış istasyonun bir sayfasıdır). Satın aldığın, lotta kazandığın ya da sana hediye edilen eşyaların etiketi yoktur ve tekrar satılamaz.

## Birden çok eşya seçme {#select-several-items}

Envanterin boş bir yerine bas (kutucukların yanındaki boşluk, iki kutucuk arasındaki aralık ya da son satırın altındaki alan) ve sürükle: yarı saydam bir dikdörtgen işaretçiyi izler ve dokunduğu her kutucuk sen sürüklerken seçilir. Bırak, seçim kalır; başlık satırı onu sayar (“3 seçili”). Seçime eklemek için sürüklerken **Shift**, **Ctrl** veya **Cmd** tuşunu basılı tut: seçimde zaten olup dikdörtgenin dokunduğu kutucuklar bunun yerine seçimden çıkar. Düz bir sürükleme yeni bir seçim başlatır. **Esc**, boş bir yere tıklamak ya da başlık satırında çöp kutusunun yanındaki düğme seçimi temizler; sürüklemenin ortasında **Esc** sürüklemeyi iptal eder. Uzun bir envanterin üst veya alt kenarında liste kendiliğinden kayar. Bir kutucuğa basmak yine kutucuğun kendi işidir: takmak için tıkla, yuvaya sürükle. Başlık satırındaki çöp kutusu düğmesi, seçili eşyaları onları listeleyen bir onay sorusundan sonra siler (aynı ekstralardan oluşan bir yığın bütün olarak gider); uçuştaki hangar kilitliyken sunulmaz. Skylab’da takılı bir eşya seçilemez; yalnızca arama ve kategori düğmelerinin ızgarada bıraktıkları seçilebilir. Seçim dikdörtgeni seçime bir kutucuk daha kattığında hafif bir tık sesi gelir (Ayarlar’daki Düğme sesleri anahtarını izler).

## Eşyadan eşyaya takma (alt yuvalar) {#item-to-item-equipping-sub-sockets-}

Bazı ana eşyalar, parametrelerini güçlendirmek için ikincil destek eşyalarını “takabilir” (buna alt yuvaya takma denir). Alt yuvaya takmak için destek eşyasını hangar envanterinde doğrudan ana eşyanın üzerine sürükle.

### Uyumluluk tablosu {#compatibility-table}

| Ana eşya | Kabul edilen alt yuva eşyaları | Sonuç |
| :--- | :--- | :--- |
| **Lazer** | Lazer amfisi (Amp) | Temel hasarı ve kritik vuruş değerlerini artırır ya da hedefin soğurmasından puan düşer (Penetration Amp) |
| **Kalkan çekirdeği** | Kalkan hücresi | Kalkan kapasitesini ve dolum hızını artırır |
| **Motor** | İtici | Motor hızını ve çarpanları artırır |
| **Hibrit jeneratör** | Kalkan hücresi VEYA itici | Kalkan kapasitesini, dolum hızını veya hızı artırır |
| **Dron** | Her yuvasında bir lazer veya kalkan (Master Drone eşyasında iki yuva vardır) | Lazer, hasarını salvona ekler; kalkan, çekirdek yuvasındaki gibi sayılır (değerlerinin %100’ü) |

---

## Cephane yönetimi {#ammo-management}

Lazer cephanesi tüketilen bir kaynaktır.
- Cephane envanterinde yığın olarak birikir.
- Aktif lazer cephanesini HUD kısayol çubuğundan değiştirebilirsin.
- Daha kaliteli cephane hasar çarpanları sağlar (örneğin standart x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). Siphon Battery yalnızca kalkanlara x1 hasar verir ve verdiği hasarı senin kalkanına aktarır.
