<!-- wiki-i18n source: 6ff3251582e96a39 -->
<!-- wiki-i18n title: Tarif Kitabı -->
# Tarif Kitabı ve Build’ler {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; tarif; tarifler; tarif kitabı; maliyet; adımlar; şema; üretim ağacı; ne gerekiyor; build’ler; buildler; donanım düzeni; ön ayar; ön ayarlar; içe aktar; dışa aktar; build’lerim; buildlerim; build paylaş -->

**Tarif Kitabı**, oyundaki her eşya için “bu ne gerektirir?” sorusunu yanıtlar: neyden yapıldığını gösteren bir şema, sırayla adımlar, tam maliyet ve her ham eşyanın nereden geldiği. **Build’ler** aynısını bütün bir gemi için yapar: hangarındaki donanım düzenini ya da bir arkadaşının build’ini içe aktar, 15 ön ayardan birinden başla ya da kendi build’ini yap ve istatistiklerini ve tam maliyetini adım adım gör. İkisi de istasyonun **Kütüphane** bölümünde, Wiki’nin altındadır.

Tarif Kitabı’nın kendi fiyat listesi yoktur: sayılarını sen baktıkça, Mağaza’nın, [Montaj](/wiki/06-Items/Overview.md#upgrading-modules) ve [Araştırma](/wiki/03-Mechanics/Research.md) sayfalarının kullandığı tariflerden, fiyatlardan, teknolojilerden ve ganimet tablolarından hesaplar; bu yüzden bir fiyat ya da tarif değiştiğinde oyunu izler. Bu sayfanın hiçbir fiyatı ya da özelliği anmamasının nedeni budur: eşyayı ya da build’i aç.

![The Builds page: the presets from early to late, and a build with its lasers, generators, extras and drones laid out in slots](../../img/wiki-img/shots/builds.jpg)
![The Bill tab: what the item takes in Credits, Thulium and raw items, with what you have and what is missing](../../img/wiki-img/shots/recipe-book-bill.jpg)
![An item in the Recipe Book: its ways to get it, the switches for the bill and the chart of what it takes down to the raw items](../../img/wiki-img/shots/recipe-book-chart.jpg)

## Nasıl açılır {#open-it}

İstasyon menüsünü aç ve **Kütüphane › Tarif Kitabı** ya da **Kütüphane › Build’ler** seçeneğini seç. Tarif Kitabı, baktığın son eşyayı, filtrelerini ve yakınlaştırmasını yalnızca bu bilgisayarda hatırlar; build’lerin bunun parçası değildir ([Hesabına kaydedilir](#saved-on-your-account)). Oyun, konuştuğu sunucudan daha yeniyse sayfalar bunu söyler ve daha azını gösterir: Tarif Kitabı satın alınan, üretilen ya da yükseltilen her şeyi yine hesaplar ama dünyanın bir eşyayı nerede verdiğini söyleyemez (yalnızca “Elde et” yazar); Build’ler ise daha yeni sunucu gerektiren parçaları adıyla söyler: ön ayarlar, Build’lerim ve istatistikler.

## Bir eşya bul {#find-an-item}

Soldaki büyük liste oyunun her eşyasını tür bazında gruplayarak ve bir türün içinde oyunun kendi sırasıyla tutar: en zayıf kademe önce. Tek sarf malzemesi olan EMP Charge de içindedir.

- **Arama.** Sayfanın herhangi bir yerinde yazmaya başla, metin arama alanına gider. Liste, adın ne kadar iyi eşleştiğine göre sıralanan tek bir liste olur (adın tamamı, başlangıcı, bir sözcüğün başlangıcı, herhangi bir parçası, sonra tür). Büyük harf ve aksanlar önemli değildir ve adı değişmiş bir eşyanın eski adı da eşyayı bulur. `Esc` aramayı temizler.
- **Tür.** Listenin üstündeki açılır menü onu tek bir türe daraltır ve her türün kaç eşyası olduğunu söyler. Yanındaki anahtar her türün içinde A’dan Z’ye sıralar.
- **Satırlar.** Bir satır eşyanın resmini, adını, türünü ve nadirliğini, onu normalde nasıl edineceğini gösteren küçük bir simgeyi (Montaj’da üretilir, Mağaza’da satılır, düşer ya da bulunur, preslenir ya da kara delikte oluşturulur) ve sende varsa bir onay işaretini gösterir.
- **Tuşlar.** Ok tuşları, Page Up, Page Down, Home ve End listede gezinir, `Enter` şemaya geçer. `Alt+Left` ve `Alt+Right` açtığın eşyalar arasında geri ve ileri gider.

## Şema {#the-chart}

Bir eşyaya tıkla, sağ taraf onu gösterir. En üstte resmi, adı, nadirliği ve türü ile onu edinmenin her **yolu** için bir çip bulunur: **Üret** (Montaj’da, süresi ve maliyetiyle), **Satın al** (Mağaza’da, fiyatıyla), **Presle** (cevherden, Skylab’daki Dökümhane’de), **Ganimet** (dünya verir: uzaylılar, kayalar, ödüller) ve **Oluştur** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), kara deliğe atılan N.I.K.E. roketlerinden). Dolu çip, şemanın ve maliyetin izlediği yoldur; onun yerine başka bir yolu izlemek için başka bir çipe tıkla. Eşyayı üretmeni sağlayan şeyi araştırmadıysan, bir satır hangi teknolojinin gerektiğini ve ne kadar sürdüğünü söyler; yanında Araştırma sayfasını açan bir düğme bulunur.

**Şema**, eşyayı soldan sağa bir ağaç olarak çizer: eşya solda, neyden yapıldığı sağında, ham eşyalara kadar.

- Her kutu eşyayı, ondan kaç tane gerektiğini ve nasıl edinildiğine dair bir simgeyi gösterir (yukarıdaki yolun çipinin simgesi; sözcükleri görmek için kutunun üzerine gel, böylece renk hiçbir zaman tek işaret olmaz). Bir kilit, teknolojisinin henüz araştırılmadığını söyler; bir sayıyla birlikte yeşil bir onay işareti, ondan kaç tane olduğunu söyler.
- Dalları olan bir kutunun onları gizleyen küçük bir tutamacı vardır; büyük bir ağacın derin dalları kapalı başlar. **Hepsini genişlet**, **Hepsini daralt**, **Sığdır** ve yakınlaştırma düğmeleri şemanın üstündedir.
- Kartını şemanın altında okumak için bir kutuya tıkla: eşya, edinme yolları (o yolu izlemek için başka bir çipe tıkla), yolun gerektirdiği (bir üretimin kaç kez yapılacağı, süresi ve maliyeti ya da Mağaza’daki fiyatı), kaç tane olduğu ve kilitli bir kutu için gereken teknoloji. O eşyayı Tarif Kitabı’nda açmak için çift tıkla ya da `Enter` tuşuna bas. Ok tuşları kutudan kutuya gider, `Space` bir dalı daraltır, `0` şemayı sığdırır. Dolaşmak için kaydır; `Ctrl` ve tekerlek yakınlaştırır.
- Yalnızca satın alınan ya da bulunan bir eşya, “Üretilecek bir şey yok: satın alınır ya da bulunur. Edinme sekmesine bak.” yazan tek bir kutudur.

Geniş bir pencerede şema solu kaplar, diğer paneller sağında bir sütunda durur; dar bir pencerede **Şema**, **Adımlar**, **Maliyet**, **Edinme** ve **Kullanıldığı yerler** sekmeleri bir seferde bir panel gösterir.

## Adımlar ve maliyet {#steps-and-the-bill}

Başlığın altında, neyin sayılacağına üç denetim karar verir: kaç kopya istediğin (**Kaç tane**), **Sahip olduklarımı say** (açık: zaten sahip olduğun şeyler düşülür) ve **Takılı olanları da say** (kapalı: bir gemiye takılı parça sayılmaz, çünkü bir yükseltme üretmek bir parçayı harcar ve takılı bir parça yuvasından çıkmış olur).

- **Adımlar**, şemanın numaralı liste hâlidir; yapılma sırasıyla ve gruplar hâlinde: Araştırma, Elde et, Satın al, Presle ve üret ve Stoğundan. Araştırma ilk gelir çünkü Montaj, teknolojisi araştırılmadan hiçbir şey üretmez. Her adım neyin ve kaç tane olduğunu, neye mal olduğunu ve ne kadar sürdüğünü söyler; bir Elde et adımı nereden edinileceğini gösterebilir. **Adımları kopyala** listeyi metin olarak kopyalar.
- **Maliyet** hepsini toplar: gereken kredi ve Thulium, sahip olduklarınla karşılaştırılmış olarak; her ham eşya için **Gerekli**, **Sende** ve **Eksik** miktarları, araştırmanın gerektirdiği Dark Matter, üretme ve presleme süresi, araştırma süresi (teknolojiler teker teker) ve bir **Değer**. Değer, bir eşyayı edinmenin iki yolunu karşılaştırmanın bir yoludur; Thulium ve bulman gereken şeyler kredi olarak sayılır: bir fiyat değildir. **Maliyeti kopyala** maliyeti bir sohbete ya da nota yapıştırabileceğin bir tablo olarak kopyalar.

## Edinme ve Kullanıldığı yerler {#sources-and-used-in}

- **Edinme**, dünyanın eşyayı ve planın gerektirdiği her ham eşyayı nerede verdiğini türe göre söyler: uzaylılar, asteroitler ve kayalar, sürüler, Dormant Swamp, Clan Warden, [Davidski](/wiki/03-Mechanics/Davidski.md), Skylab seferleri, Dev ekskavatör, Skylab üretimi, görevler, Arkadaşları Davet Et ve başlangıç paketi. Bir satır onu kimin ve nerede verdiğini, şansı ve kaç tane olduğunu belirtir. “Ayrıca şurada” satırı [pazarı](/wiki/03-Mechanics/Auction.md), Davidski’nin stoğunu ve diğer pilotları listeler. Şans bir şanstır, saatlik bir oran değildir: bir öldürmenin ne kadar süreceği sana bağlıdır.
- **Kullanıldığı yerler**, bu eşyadan yapılan eşyaları listeler. Açmak için birine tıkla.

## Build’e ekle {#add-to-build}

Bir yuvaya oturan ya da taşınan bir eşyanın **Build’e ekle** düğmesi vardır: gemiler, gövde plakaları, lazerler, amfiler, kalkanlar, hücreler, motorlar, iticiler, Uyarlanabilir Çekirdekler, ekstralar, dronlar, formasyonlar, cephane, roketler ve EMP Charge. Eşyayı **Build’ler** sayfasında düzenlediğin build’e, uyduğu ilk yere koyar (hiç build yoksa “Yeni build” adlı yeni bir build oluşturulur) ve bir mesaj nereye gittiğini ya da neden sığmadığını söyler (“Önce bir gemi seç.”). Zaten gemisi olan bir build’e gemi eklemek, değiştirmek için tekrar tıklamanı ister. EMP Charge takılmaz, taşınır: build’in roketlerine girer.

## Build’ler {#builds}

Bir **build**, tek bir geminin donanım düzenidir ve her sunucuda aynı anlama gelmesi için eşya adlarıyla yazılır: gemi, amfileriyle lazerler, hücreleri ve iticileriyle kalkanlar, motorlar ve Uyarlanabilir Çekirdekler, ekstralar, yetenek yuvalarındaki parçalar, gövde plakaları, taşıdıklarıyla dronlar, bir formasyon ve taşınacak cephane ile roketler. Ayrıca bir adı, bir notu, bir aşaması (Erken, Orta ya da Geç) ve bir türü vardır.

Soldaki listede aşamaya göre **Ön ayarlar**, **Build’lerim**, **Yeni build** ve **İçe aktar** bulunur; dar bir pencerede bir sekme sırasıdır. Bir build seç, düzenini, istatistiklerini ve maliyetini görürsün.

### İçe aktar {#import}

**İçe aktar** üç kapılı bir sayfa açar:

- **Yapıştır**: bir build’in metnini yapıştır ya da **Panodan yapıştır** düğmesine bas.
- **Dosyadan**: oyunun veri klasörünün (ana klasöründeki `.spacecorps2027`) `exports` klasöründeki build dosyaları; **Dosyaya kaydet** düğmesinin yazdığı klasör.
- **Hangarımdan**: gemilerinden birini ve bir konfigürasyonu seç; oyun takılı olanları okur: lazerler ve amfiler, hücreleri ve iticileriyle jeneratörler, ekstralar, yetenek parçaları, gövde plakaları, taşıdıklarıyla dronlar ve Extra Slots CPU seviyen. Kısayol çubuğundaki formasyonu, cephaneyi ve roketleri de sunar; istediklerini işaretle.

Hiçbir şey kaydedilmeden önce neyin içe aktarılacağını görürsün ve oyun içe aktaramadığı şeyi tam olarak söyler: bu oyunda olmayan bir eşya, yerine uymayan bir parça, geminin yuvalarından fazla parça, daha yeni bir oyunla yapılmış bir build. **Değişiklik olmadan içe aktarıldı** her şeyin içeri girdiği anlamına gelir. Sonra **Build’lerime kaydet**, **Düzenleyicide aç** ya da sayfayı kapat. [Demirhane](/wiki/06-Items/Forge.md) kademelerin, büyüleme bonusların, dron seviyelerin, boosterların, P.E.T. birimin, geminin görünümü ve diğer [Hangar](/wiki/03-Mechanics/Hangar.md) konfigürasyonun bir build’in parçası değildir (diğer konfigürasyonu ikinci bir build olarak içe aktar).

### 15 ön ayar {#the-15-presets}

On beş build kullanıma hazırdır: oyunun üç aşaması, **Erken**, **Orta** ve **Geç**, her birinde beş tür. **Farm**, maliyetine göre en çok öldürmeyi sağlar, **Savunma** en büyük kalkana ve en hızlı yenilenmeye sahiptir, **Saldırı** en çok hasara ve kalkan delmeye, **Duruma göre** savaşlarını gizlenme, sıçrama ve hızla seçer, **Tank** ise gövde ve kalkan toplamı en yüksek olandır. Bir ön ayar değiştirilemez: **Kopyasını düzenle** onu kendi taslağın olarak açar, **Build’lerime ekle** ise olduğu gibi saklar. Her satır Değerini birkaç karakterle gösterir, sen baktıkça tariflerden hesaplanır; istatistikleri ve maliyeti için bir ön ayarı aç.

### Düzenle {#edit}

Bir build, Hangar gibi çizilir: lazerler, jeneratörler, ekstralar, yetenekler, plakalar ve dronlar, sonra Extra Slots CPU seviyesi, bir formasyon ve taşınacak cephane ile roketler. Boş bir yuvaya tıkla, bir liste yalnızca ona uyanları fiyatıyla ya da edinme yoluyla gösterir; bir parçaya tıkla ve onu **Değiştir**, ona **Modül ekle** ya da onu **Kaldır**. Bir dron bir lazer ya da bir kalkan çekirdeği taşır. Gemiyi değiştirirsen hâlâ uyan parçalar kalır, gerisi çıkarılanlar olarak listelenir. Build’e bir ad, bir aşama, bir tür ve bir not ver, sonra **Kaydet**, **Kopya olarak kaydet**, **Sil** ya da **Kapat** (Kapat, değişiklikler kaydedilmemişse önce sorar).

### İstatistikler {#stats}

Düzenin altında hangarın kendi özellik kartı bulunur: gövde puanı, hasar, menzil, kritik şans, kalkanlar ve dolumları, soğurma, hız, kalkan ve hız bonusları, kalkan delme ve gövde plakası yuvası olan bir gemide plakalarının eklediği gövde. Yeteneklere ait satır yoktur: yetenek yuvalarındaki parçalar düzendedir. Sunucu, hiçbir gemiye takılı olmayan bir build için sayıları hangarınla aynı kodla hesaplar. İki anahtar sayıların varsaydığı değerleri belirler: **Demirhane kademesi** ve **Dron seviyesi**. Bir formasyon uçuşta çalışır, bu yüzden metin olarak listelenir ve sayılara dahil edilmez; boosterlar ve kendi Demirhane kademelerin de dahil edilmez.

### Maliyet {#cost}

Maliyet dört bloktan oluşur:

- **Toplamlar**: kredi, Thulium, Dark Matter, her ham eşya için Gerekli, Sende ve Eksik, süreler ve Değer. **Hâlâ gerekenler**, sahip olduklarının düşülmesinden sonra kalandır.
- **Paranın gittiği yer**: her parça, en pahalısı önce.
- **Adımlar**: tüm build için araştırma, elde etme, satın alma, presleme ve üretme, sırayla. Dünyanın onu nerede verdiğini görmek için bir Elde et adımına tıkla ya da eşyayı Tarif Kitabı’nda aç.
- **Başlamadan önce**: parça olmayanlar; Extra Slots CPU seviyeleri, gövde plakası yuvalarının araştırması, hâlâ satın alman gereken dronlar ve Dökümhane’nin gerektirdiği Skylab Çekirdeği seviyesi gibi.

Üç anahtar: **Sahip olduklarımı say** (açık), **Takılı olanları da say** (kapalı) ve **Cephane ve roketleri de say** (kapalı: tekrar tekrar harcanırlar, bu yüzden build’in fiyatı değildirler).

## Hesabına kaydedilir {#saved-on-your-account}

**Build’lerin hesabına kaydedilir**, bu bilgisayarda değil sunucuda; bu yüzden hangi bilgisayarı kullanırsan kullan seninle olurlar. En fazla 50 tane tutabilirsin; liste kaç tanen olduğunu gösterir ve dolduğunda sayfa başka birini kaydetmek için birini silmeni ister. Bir build, sunucu öyle dediğinde kaydedilmiş sayılır: sayfa beklerken **Kaydediliyor…** gösterir; sunucu reddederse ya da ulaşılamazsa nedenini söyler ve build kaydedilmemiş kalır, değişikliklerin düzenleyicide durur. Kaydedilmiş bir build yalnızca eşya adlarından, birkaç etiketten ve yazdığın ad ile nottan oluşur ve başka hiçbir pilot onu göremez. Bir arkadaşına vermek için dışa aktar.

## Paylaş ve dışa aktar {#share-and-export}

Bir build üzerindeki **Dışa aktar**, build’i metin (JSON) olarak gösteren bir sayfa açar. Bir sohbete yapıştırmak için **Kopyala**, ya da `spacecorps-build-<name>.json` dosyasını `exports` klasörüne yazan ve daha eski bir dosyanın üzerine asla yazmayan **Dosyaya kaydet**. Bir arkadaşın metni **İçe aktar › Yapıştır** altına yapıştırır ya da dosyayı kendi `exports` klasörüne koyup **Dosyadan** altından seçer. Metin donanım düzeninin eşya adlarını, gemiyi ve build’in adı ile notunu içerir; hesabına ait hiçbir şey içermez.

## İpuçları {#tips}

1. **Farm yapmadan önce bak.** Gereken şey olmayan bir ganimet için bir günü harcamadan önce Tarif Kitabı’nda eşyayı aç, Edinme ve Adımlar sekmelerini oku.
2. **Sıfırdan say.** Bir eşyanın ya da build’in sıfırdan neye mal olduğunu görmek için **Sahip olduklarımı say** seçeneğini kapat; hâlâ neye ihtiyacın olduğunu görmek için açık bırak.
3. **Bir ön ayardan başla.** **Kopyasını düzenle**, bir parçayı değiştir; istatistikler ve maliyet arkasından gelir.
4. **Ağaçları da oku.** [Eşya ağaçları](/wiki/06-Items/Item-Trees.md) her eşya türünü yan yana gösterir; Tarif Kitabı bunlardan herhangi birinin fiyatını senin için hesaplar.
