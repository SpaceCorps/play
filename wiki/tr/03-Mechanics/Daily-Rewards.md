<!-- wiki-i18n source: c6cf04f6e8e99425 -->
<!-- wiki-i18n title: Günlük ödüller -->
# Günlük ödüller {#daily-rewards}

<!-- wiki-search: daily reward; daily rewards; daily login; login bonus; login reward; calendar; advent calendar; chest; chests; season prize; souvenir; blueprint; streak; günlük ödül; günlük ödüller; günlük giriş; takvim; sandık; sezon ödülü; hatıra; plan; seri -->

Her sezonun bir **günlük ödül takvimi** vardır: sezonun her günü için küçük bir hediye. İstasyonda **Ödülü al** düğmesine bas, günün hediyesi senin olsun. Ne kadar çok gün toplarsan o kadar çok şey kazanırsın: dört **sandık** 7, 14, 21 ve 28 toplanan günde gelir, sezonun son üç gününde de **sezon ödülü**nü alabilirsin. Kaçırdığın bir gün sana yalnızca o günün hediyesine mal olur, başka bir şeye değil. Takvimi **Gösterge Paneli**nde (**Günlük ödüller** kartı) ve **Sezon ve Profil › Takvim** altında bulursun.

## Bir dakikada {#in-one-minute}

- **29 kutucuk.** Sezonun her UTC günü için bir tane. Bir sezon 30 gündür, ama 30. gün [sıfırlamanın](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule) 5 dakikalık geri sayımıdır, bu yüzden o gün toplanacak bir şey yoktur.
- **Ödülü al düğmesine sen basarsın.** Bir basış bir kutucuğu toplar, pilot başına bir kez. Senin yerine hiçbir şey toplanmaz.
- **6 saatlik ek süre.** Bir kutucuk, günü bittikten sonra 6 saat daha açık kalır.
- **Seri yok.** Kaçırılan bir gün yalnızca o günün kutucuğunu kaybettirir, başka bir şeyi değil. Önemli olan kaç gün topladığındır, art arda olup olmadığı değil.
- **4 sandık**, 7, 14, 21 ve 28 toplanan günde.
- **Bir sezon ödülü** sezonun son üç gününde: 10 toplanan günde bir hatıra görünümü, 20 günde bir gemi tasarımının planı.
- **Her sıfırlamada yeni bir takvim.** Sezonun her hediyesini 1. günden itibaren görürsün.
- **Bilerek küçük.** 29 günün tümü, bir sezona yayılmış birkaç saatlik avın değeri kadardır.

## Gün {#the-day}

Takvimin günü bir **UTC günüdür**: tüm pilotlar için aynı anda, **00:00 UTC**’de değişir ve klanların günlük hattıyla aynı gün sayımıdır (“Gün *n*/29”, bkz. [Klanlar](/wiki/03-Mechanics/Clans.md#the-day)). Saat dilimini izlemez ve sezonun başladığı saatte değişen Sezon sayfasındaki sezon günü de değildir. Her şeye sunucunun saati karar verir: bilgisayarının saati hiçbir şeyi değiştirmez.

Kart da sekme de bir sonraki ödülün **kendi saat diliminde** ne zaman açılacağını söyler (“Yeni ödüller senin saatinle 02:00 itibarıyla açılır (00:00 UTC)”). Kendin hesaplamak için 00:00 UTC’yi çevir. Birkaç örnek:

| Nerede | UTC gece yarısı |
| :--- | :--- |
| Orta Avrupa | 01:00 (kış) veya 02:00 (yaz) |
| Moskova, İstanbul | 03:00 |
| Japonya, Kore | 09:00 |
| ABD Doğu Kıyısı | 19:00 (kış) veya 20:00 (yaz) |
| ABD Batı Kıyısı | 16:00 (kış) veya 17:00 (yaz) |

- **1. gün kısadır.** Sezon, bir UTC gününün ortasında, sıfırlamayla başlar; bu yüzden 1. kutucuk o andan o günün sonuna kadar ve ek süre boyunca açıktır.
- **29. gün uzundur.** Son kutucuk, sıfırlamanın geri sayımı başlayana kadar açık kalır; bu, açılışından 24 saatten fazla sonra olabilir. Geri sayım başladıktan sonra yeni sezon başlayana kadar hiçbir şey toplanamaz.
- **Yöneticiler sezon gününü kaydırabilir.** Takvim onu izler: atlanan günler herkes için kaçırılmış sayılır, senin zaten topladığın bir kutucuk ise toplanmış kalır.

## Kutucuklar {#the-tiles}

Takvim sekmesi her gün için bir kutucuğu olan bir ızgara gösterir: gün numarası, hediye ve sözcüklerle yazılmış bir durum. Sezonun her hediyesi ilk günden itibaren görünür, böylece neyin geleceğini görürsün. Sekme ayrıca günlerini sayar (örneğin “29 günden 11’i alındı”) ve bir sonraki sandığın ne zaman geleceğini söyler. Gösterge Panelindeki kart bugünün hediyesini ve tek bir **Ödülü al** düğmesini gösterir.

| Durum | Ne anlama gelir |
| :--- | :--- |
| **Bugün** | Şu an açık. **Ödülü al** düğmesine bas. |
| **Alındı** | Elinde. |
| **Dün** | Dünün kutucuğu, ek süre boyunca hâlâ açık. Ne kadar süre kaldığını gösterir ve kendi **Ödülü al** düğmesi vardır. |
| **Kaçırıldı** | Gün ve ek süresi bitti. Hediye gitti, başka hiçbir şey değişmedi. |
| **… sonra açılır** | Gelecek bir gün. Hediyesini görebilirsin ama henüz toplayamazsın. |
| **Katılmadan önce** | İlk girişinden önceki bir gün. Toplanamaz. |

Bir ödül beklerken kenar çubuğunda **Sezon ve Profil** satırında ve uçuşta **Üsse dön** düğmesinde küçük bir **(!)** görünür, girişte de bir mesaj sana haber verir (her gün için her bilgisayarda bir kez).

## Ek süre ve kaçırılan günler {#grace-and-missed-days}

Bir kutucuk gece yarısı kapanmaz: UTC günü bittikten sonra **6 saat** daha açık kalır. Bu 6 saatte iki kutucuk açıktır, dünün ve bugünün; her birini ayrı bir basışla toplarsın. Ek süreden sonra dünün kutucuğu kalıcı olarak **Kaçırıldı** olur ve bundan daha geriye gidemezsin.

Kaçırılan bir gün sana **o günün hediyesine mal olur, başka bir şeye değil**. Kopacak bir seri yoktur: topladığın gün sayın, sandıkların ve sezon ödülü devam eder. Ek süre içinde topladığın bir kutucuk, zamanında toplanmış biriyle tıpatıp aynı sayılır.

## Sandıklar {#chests}

Bir sandık, topladığın gün sayısını belli bir sayıya ulaştıran **Ödülü al** ile birlikte gelir, ondan önce değil: basılacak bir şey ve bulunacak bir anahtar yoktur. Önemli olan sayıdır, tarih değil: 7 günlük sandık, sezonun hangi günü olursa olsun 7. toplanan günle gelir.

| Sandık | Şu zaman gelir |
| :---: | :--- |
| **1.** | 7 toplanan gün |
| **2.** | 14 toplanan gün |
| **3.** | 21 toplanan gün |
| **4.** | 28 toplanan gün |

Her sandık bir **Specimen Vault** içerir; bu, her şeyden biraz barındıran konteynerdir. Sonraki sandıklara sıfırlamanın almadığı küçük bir ek eklenebilir. Takvim sekmesi her sandığın içinde ne olduğunu gösterir. Konteyner yalnızca senindir ve Konteynerler sayfasında açarsın. Açmadığın bir konteyner [sıfırlamadan](/wiki/03-Mechanics/Wipe-Timeline.md) sonra da hesabında kalır.

Oyun konteyneri veremiyorsa, örneğin konteynerler açık değilse, sandık onun yerine yaklaşık aynı değerde kredi, Thulium ve bir booster’dan oluşan bir **paket** öder. Bir sandık asla kaybolmaz ve ikisini birden almazsın.

## Sezon ödülü {#season-prize}

Sezon ödülünün iki basamağı vardır. Onları sezonun **son üç gününde** (27. günden 29. güne), sıfırlamanın geri sayımı başlayana kadar toplarsın. 27. günden önce, gerekli günlere zaten sahip olsan bile sekme **Son üç günde açılır** der. Her basamak bir kez, istediğin sırayla toplanır.

| Basamak | Gerekir | Ödül |
| :---: | :--- | :--- |
| **1** | 10 toplanan gün | Bir **sezon hatırası**: bir görünüm |
| **2** | 20 toplanan gün | Bir **tasarım planı**: bir gemi tasarımının teknolojisi |

- **Hatıra** bir skin, bir renk, bir egzoz efekti ya da bir auradır ([Kozmetikler](/wiki/06-Items/Cosmetics.md)); sezon için bu iş için ayrılmış kısa bir görünüm listesinden seçilir ve asla Destansı’nın üstüne çıkmaz. Her görünüm gibi yalnızca gösteriş içindir, hesabına aittir ve sıfırlamadan sonra da kalır. Zaten sahipsen sahip olmadığın bir sonraki hatırayı alırsın. Hepsine sahipsen 250 Thulium alırsın.
- **Plan**, bir gemi tasarımının araştırmasıdır ve senin yerine yapılmıştır: tasarımın teknolojisi ve onun gerektirdiği teknolojiler. Bir gemiyi tasarıma dönüştürmek yine Montaj’da yapılır ve yine [Gemi tasarımları](/wiki/03-Mechanics/Ship-Designs.md#getting-a-design) sayfasında yazan kadar tutar. Bir sezonun tasarımı 13’ten biridir, sabit bir sırayla alınır; bu yüzden bir tasarım 13 sezon boyunca geri gelmez. Zaten biliyorsan eksik olduğun bir sonraki tasarımı alırsın. 13’ünü de biliyorsan eşya olan 4 Dark Matter Plate alırsın: onları sıfırlamadan önce Nakliye Deposu’na koy.

## Hediyeler {#the-gifts}

Bir günün hediyesi küçüktür. Şunlardan biridir:

- **Cephane ve roketler**, mütevazı yığınlar halinde.
- **Malzemeler, plakalar ve sarf malzemeleri**; aralarında Forge kit’ler (Demirhane’nin bir adımının malzemeleri) de var.
- Birkaç saatlik **booster**’lar. Bir booster hediyesi saatlerini [booster’larına](/wiki/06-Items/Boosters.md#active-boosters) ekler.
- **Kredi ve Thulium**, küçük miktarlarda.
- **Birkaç özel eşya** (Workforce Contract, Forger’s Seal): bir sezonda hiçbir zaman 4 kutucuktan fazla değil.

Bu sayfa hiçbir sezonun hiçbir hediyesini anmaz, çünkü takvim her sıfırlamada farklıdır. Bu sezonun hediyelerini Takvim sekmesi gösterir. Hediye hediyedir: takvimden gelen eşyaların **Satılabilir** etiketi olmaz ([Satılabilir eşyalar](/wiki/03-Mechanics/Inventory.md#marketable-items)) ve [Açık Artırma](/wiki/03-Mechanics/Auction.md)’ya konamaz.

## Sıfırlama {#the-wipe}

Yeni bir sezon yeni bir takvimdir. [Sıfırlamada](/wiki/03-Mechanics/Wipe-Timeline.md) eskisi kapanır, yenisi kendi 29 hediyesiyle açılır ve sayacın yeniden 0’dan başlar. Sıfırlama, her eşyadan aldığı dışında topladığın hiçbir şeyi almaz:

- **Silinir:** eşya olan hediyeler (cephane, roketler, malzemeler, plakalar, sarf malzemeleri), [Nakliye Deposu](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)’nda değilse sıfırlamada silinir. Takvim böyle bir hediyeyi bir notla işaretler.
- **Kalır:** booster’lar, kredi, Thulium, özel eşyalar, görünümler, teknolojiler (bir plan) ve konteynerler.
- **Son dört gün (26’dan 29’a) yalnızca kalan hediyeler verir**, böylece son haftanın bir hediyesi sıfırlamada asla kaybolmaz.

## Geç katılanlar ve geç başlayan takvimler {#late-joiners-and-late-calendars}

**Bir sezonun ortasında katılırsan,** ilk girişinden önceki kutucuklar **Katılmadan önce** yazar ve toplanamaz. Sandıklar ve sezon ödülü herkesten aynı sayıda gün ister, bu yüzden geç gelen bir pilot bunların daha azına ulaşabilir. İlk kez 16. günde giriş yapan bir pilotun 14 kutucuğu kalır, yani toplayabileceği en çok gün 14’tür: ilk iki sandık ve sezon ödülünün 1. basamağı erişilebilir, 2. basamak (20 gün) değildir.

**Bir takvim de geç başlayabilir.** Genellikle sezonla birlikte açılır. Daha sonra da açılabilir, örneğin oyuna Günlük ödüller bir sezonun ortasında geldiğinde. Böyle bir takvimin yalnızca kalan günleri vardır ve her şey onunla birlikte ölçeklenir: 14. günde açılanın 16 kutucuğu (“16 günden”), 4, 8, 12 ve 15 toplanan günde sandıkları ve 6 ile 11’de sezon ödülü basamakları olur. Gösterge Panelindeki kart hangi günde açıldığını söyler. 10 günden az kaldıysa süren sezonun hiç takvimi olmaz (**Bu sezon takvim yok**) ve bir sonraki sıfırlamayla başlar.

## Sorular {#questions}

- **N. günü neden toplayamıyorum?** Dört neden var. Gün henüz gelmedi (**… sonra açılır**). Gün ve ek süresi bitti (**Kaçırıldı**). Gün ilk girişinden önceydi (**Katılmadan önce**). Ya da sıfırlamanın geri sayımı başladı. Takvimi olmayan bir sezonda ya da kapatılmış bir takvimde toplanacak bir şey yoktur.
- **Saat dilimimi izler mi?** Hayır. Gün bir UTC günüdür. Yalnızca gösterilen saatler saat dilimine çevrilir ([Gün](#the-day)).
- **Sunucu kapalıysa ne olur?** 6 saatlik ek süre gece yarısı civarındaki kısa bir kesintiyi karşılar. Daha uzunu için bir yönetici bir günü herkes için daha uzun açık tutabilir. O günün kutucuğu o zaman kendi geri sayımıyla **Dün** olarak görünür.
- **İki günü birden toplayabilir miyim?** Yalnızca iki kutucuk açıkken, bir UTC gece yarısından sonraki 6 saatte: dünün ve bugünün, her biri bir basışla. Bir kutucuk iki kez ya da önceden toplanamaz.
- **Her gün giriş yapmam gerekir mi?** Hayır. Seri yok: atladığın bir gün sana o günün hediyesine mal olur, sandıklar ve sezon ödülü yalnızca kaç gün topladığını sayar.
- **Premium bir şeyi değiştirir mi?** Hayır. Premium fazladan kutucuk ya da daha iyi hediye vermez, takvim de Premium günü vermez.
- **Klana ihtiyacım var mı?** Hayır. Takvim klanların günlük hattıyla aynı günü kullanır ama yalnızca senindir.
- **Seviye sınırı var mı?** Hayır. Her pilot 1. seviyeden itibaren toplayabilir.
- **Sıfırlamada ne olur?** Yeni bir takvim alırsın ve 0 günden yeniden başlarsın. Eşya olan hediyeler Nakliye Deposu’nda değilse silinir; gerisi kalır ([Sıfırlama](#the-wipe)).

## Bilmekte fayda var {#good-to-know}

- Hediyeler, sayılar ve ek süre oyun sunucusunda belirlenir ve bir güncellemeyle değişebilir; Takvim sekmesi her zaman geçerli olanları gösterir.
- Günlük ödüllerden önceki bir oyun sunucusunun takvimi yoktur ve kart ile sekme gizli kalır. Bir yönetici takvimi kapatabilir de; topladığın şey toplanmış kalır.
- Her yeni takvim sıfırlamadan önce hazırlanır, böylece oyunun yöneticileri başlamadan önce ona bakabilir ve yanlış bir hediyeyi değiştirebilir.
