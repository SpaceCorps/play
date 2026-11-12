<!-- wiki-i18n source: 0d92c80e748fc9b8 -->
<!-- wiki-i18n title: Pilot Becerileri -->
# Pilot Becerileri {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; beceriler; pilot becerileri; beceri ağacı; deneyim; seviye atlama; değerler; nitelikler; kütle; dayanıklılık; refleks; içgüdü; lazer teknolojisi; roket teknolojisi; antimadde; nişancılık; sabotaj; kaçınma; taktik; radyasyon teknolojisi; itici teorisi; bilim; çıkarma; lojistik; imalat; ticaret; saatlik yumuşak sınır; kargo bölmesi -->

Pilotunun bir **beceri ağacı** var: yaptığın şeylere göre seviye atlayan değerler kümesi. Savaşırsan Lazer teknolojin ve Dayanıklılığın yükselir; Skylab’ından toplarsan Çıkarma yükselir. Her seviye zaten yaptığın bir şeye küçük, kalıcı bir buff verir ve hiçbir şey harcanmaz ya da seçilmez: dağıtılacak puan ve sıfırlanacak bir şey yoktur. Kullandığını geliştirirsin.

Ağaç bir gemiye değil **sana** aittir. Uçurduğun her geminin senin seviyelerin vardır, yarın alacağın geminin de, ve seviyeler her sıfırlamada korunur ([nelerin korunduğu](#what-is-kept)).

Yeni bir pilot tam güçte değildir. 1. seviyede bir lazer ve bir roket, eşya sayfalarında yazandan daha az hasar verir; Lazer teknolojisi ve Roket teknolojisi yükseldikçe onları yazılı sayıların üstüne çıkarır. Eşya sayfalarındaki her rakam eşyanın kendi rakamıdır, becerilerinden önceki hâliyle.

## Bir bakışta {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Değerler**: 19 değer: 5 grupta 4 nitelik ve 15 beceri
- **Seviyeler**: 1’den 100’e kadar. Her pilot her değere 1. seviyeden başlar ve harcanacak ya da sıfırlanacak bir şey yoktur
- **Bir seviyenin maliyeti**: 1. seviyeden 2’ye 40 XP, 50. seviyeden 51’e 875 XP, 99. seviyeden 100’e 19.157 XP; toplam 313.258 XP
- **Bir seviyenin verdiği**: Bir buff, 1. seviyedeki değerinden 100. seviyedeki değerine düz bir çizgide artar. Hiçbir şeyin sınırı yoktur
- **1. seviyede lazerin**: Hasarının %100 kadarını verir ve zamanın %80 kadarında isabet eder; yani eşya sayfalarında yazan hasarın %80 kadarı
- **1. seviyede roketin**: Hasarının %100 kadarını verir ve zamanın %10 kadarında ateşlenmez; yani eşya sayfalarında yazan hasarın %90 kadarı
- **Kaçınma**: Her pilotun gemisi, kaçınılabilir darbelerin %3 kadarını, herhangi bir beceri ya da diziliş eklemeden önce savuşturur
- **Gövde kademesi**: Geminin nadirliği belirler, aşağıdaki tablonun gösterdiği gibi. Kargo bölmesinin boyutu ve Kütle’nin XP’si buna uyar
- **Kargo bölmesi**: Fırlatmadan sonra topladığın kaynak birimlerini, gövde kademesinin verdiği boyuta kadar sayar. Bunun %90 kadarından itibaren doludur ve dolu bir kargo bölmesi Kütle’nin ×1,5 ödemesini sağlar. Hiçbir şey asla reddedilmez
- **Saatlik yumuşak sınır**: Çoğu değer tam XP’yi yalnızca saatte bir sınıra kadar öder; değerin kendi biriminde, UTC saatine göre bir saat boyunca sayılır. Üstünde bir olay XP’sinin %25 kadarını öder
- **Eğitim**: Bir becerinin XP’si, kendisinin %10 kadarını niteliğine de öder. 100. seviyedeki bir nitelik becerilerini 1. seviyedekinden %25 kadar daha hızlı eğitir

| Gövde kademesi | Geminin nadirliği | Kargo bölmesi boyutu |
| :--- | :--- | ---: |
| 1 | Kalitesiz / Sıradan | 60 |
| 2 | Seyrek | 120 |
| 3 | Nadir | 250 |
| 4 | Destansı | 500 |
| 5 | Mitik / Efsanevi / Ebedi | 1.000 |

<!-- skills-glance:end -->

## Değerler {#the-stats}

Değerler iki türdür. **Nitelikler** (Kütle, Dayanıklılık, Refleks ve İçgüdü) bir pilotun temelidir. **Beceriler** beş grupta yer alır ve her beceriyi tabloların parantez içinde andığı bir nitelik yönetir: bir becerinin XP’si niteliğini de besler, yüksek bir nitelik de becerilerini daha hızlı eğitir ([XP nasıl ödenir](#how-xp-is-paid)). Adlar, oyundaki Pilot Becerileri sayfasındaki adlardır.

Tablolar her buff’ı 1. seviyede ve son seviyede verir; arada buff düz bir çizgide artar. Bir **çarpan** bir sayıyı çarpar: 1’in üstündeki büyütür, 1’in altındaki küçültür. Çoğu buff geminin bir sayısını değiştirir ve bir becerinin oynattığı sayının ipucunda, ne kadarının becerilerinden geldiğini söyleyen bir satır bulunur.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Nitelikler {#attributes}

| Değer | Neyi değiştirir | Seviye 1 | Seviye 100 |
| :--- | :--- | ---: | ---: |
| **Kütle** | Gövde | +%0 | +%20 |
| **Dayanıklılık** | Alınan hasar | ×1 | ×0,92 |
| **Refleks** | Yeteneklerin dolum hızı | ×1 | ×1,1 |
| **İçgüdü** | Her ganimet satırının şansı | +0 puan | +7,5 puan |
|  | Toplayıcılardan Orvium ve Velkonite | ×1 | ×1,5 |

### Silahlar {#weapons}

| Değer | Neyi değiştirir | Seviye 1 | Seviye 100 |
| :--- | :--- | ---: | ---: |
| **Lazer teknolojisi** (Refleks) | Lazer hasarı | ×1 | ×1,3 |
|  | Bir lazer salvosunun isabet şansı | %80 | %89 |
| **Roket teknolojisi** (Refleks) | Roket hasarı | ×1 | ×1,3 |
|  | Bir roketin ateşlenmeme şansı | %10 | %1 |
| **Antimadde** (İçgüdü) | Toplamalardan Dark Matter | ×1 | ×1,25 |

### Savaş {#combat}

| Değer | Neyi değiştirir | Seviye 1 | Seviye 100 |
| :--- | :--- | ---: | ---: |
| **Nişancılık** (Refleks) | Bir Mine’ın fırlatılma mesafesi | ×1 | ×1,15 |
|  | Fırlatılan bir Mine’ın hızı | ×1 | ×1,15 |
| **Sabotaj** (Refleks) | Zehirlerin ve Mine’ların hasarı | ×1 | ×1,3 |
|  | Zehirlerin süresi | ×1 | ×1,2 |
| **Kaçınma** (Refleks) | Bir darbeden kaçınma şansı, geminin kendi şansına eklenir | %0 | %15 |
| **Taktik** (Refleks) | Yeteneklerin süresi | ×1 | ×1,2 |
| **Kalkan soğurması** (Dayanıklılık) | Kalkanlarının soğurması | +0 puan | +5 puan |

### Gemi kontrolü {#ship-control}

| Değer | Neyi değiştirir | Seviye 1 | Seviye 100 |
| :--- | :--- | ---: | ---: |
| **Radyasyon teknolojisi** (Dayanıklılık) | Radyasyon dozu | ×1 | ×0,4 |
| **İtici teorisi** (Kütle) | Hız | +%0 | +%10 |
| **Bilim** (İçgüdü) | Her yakıt birimi başına bilim | ×1 | ×1,25 |

### Skylab

| Değer | Neyi değiştirir | Seviye 1 | Seviye 100 |
| :--- | :--- | ---: | ---: |
| **Çıkarma** (İçgüdü) | Skylab’ın ürettiği | ×1 | ×1,3 |
| **Lojistik** (Kütle) | Kaynak Deposu’nun bankasının tuttuğu | ×1 | ×1,4 |
| **İmalat** (Refleks) | Bir üretimin süresi | ×1 | ×0,65 |

### Ticaret {#trading}

| Değer | Neyi değiştirir | Seviye 1 | Seviye 100 |
| :--- | :--- | ---: | ---: |
| **Ticaret** (İçgüdü) | Mağaza’daki fiyatlar | ×1 | ×0,85 |
|  | Mağaza’nın geri alırken ödediği | ×1 | ×1,1 |
|  | Bir Açık Artırma ilanının teminatı | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Nerede hissedersin {#where-you-feel-it}

- **Lazerler.** Lazer teknolojisi her salvonun hasarını ve isabet şansını değiştirir; ıskalayan bir salvo uçuşan bir “Miss” gösterir ve yine de cephanesini harcar ([Savaş](/wiki/03-Mechanics/Combat.md#laser-tech)). Lazerlerinin menzili geminin kendi menzilidir: Nişancılık, düz x1 dışındaki cephaneyle yaptığın isabetlerle seviye atlar, ancak yalnızca Mine’lara etki eder (aşağıda).
- **Roketler.** Roket teknolojisi her roketin hasarını ve bir roketin ateşlenmeme şansını değiştirir ([Roket teknolojisi](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Darbe almak.** Dayanıklılık aldığın her darbeden bir pay çıkarır, Kaçınma doğrudan bir darbenin hiçbir şey yapmama şansını artırır, Kalkan soğurması da bir vuruşun kalkanlarının aldığı payı artırır ([Savaş](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). Kütle gövdeni artırır.
- **Yetenekler.** Refleks yeteneklerinin bekleme süresini kısaltır, Taktik de onları daha uzun sürdürür ([Yetenekler](/wiki/03-Mechanics/Abilities.md#pilot-skills)). Sabotaj zehirleri güçlendirir.
- **Mine.** Sabotaj bir Mine’ın hasarını artırır, Nişancılık da onu daha hızlı ve daha uzağa fırlatır ([Ekstralar](/wiki/06-Items/Extras.md#mine)).
- **Hız.** İtici teorisi hızına, motorların ve bir Afterburner’ın üstüne ekler ([Hız](/wiki/03-Mechanics/Speed.md)).
- **Toplama.** İçgüdü her ganimet satırının şansını bir Loot Luck Booster gibi artırır ve ikisi toplanır; Antimadde topladığın Dark Matter’ı artırır ([Kargo](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Radyasyon.** Radyasyon teknolojisi kara deliğin, ekskavatörlerin dairelerinin, pulsarların ve Unwakened’in aurasının dozunu düşürür ([Kara delik](/wiki/03-Mechanics/Black-Hole.md)).
- **Ev.** Çıkarma ve Lojistik [Skylab](/wiki/03-Mechanics/Skylab.md)’ın ürettiğini ve tuttuğunu değiştirir, İçgüdü iki toplayıcısını artırır, İmalat Montaj’ın üretimlerini kısaltır, Bilim [Araştırma](/wiki/03-Mechanics/Research.md) Merkezi’ni daha hızlı doldurur, Ticaret de Mağaza’nın fiyatlarını düşürür, geri alırken ödediğini artırır ve bir [Açık Artırma](/wiki/03-Mechanics/Auction.md) ilanının teminatını düşürür.

## XP nasıl ödenir {#how-xp-is-paid}

Sunucu, nerede uçarsan uç, yaptıkların için XP öder, şu sırayla:

1. **Farm karşıtı kural.** Bir şirket arkadaşından ya da grup arkadaşından gelen veya ona giden bir darbe hiçbir şey ödemez; güvenli bölgedeki ya da yeniden doğuş korumasındaki bir gemiye yapılan ya da onun yaptığı hiçbir şey de ödemez. Kütle’nin, Dayanıklılık’ın düşük gövdesinin ve İtici teorisi’nin saniyeleri yalnızca geminin canlı olduğu, bir korumanın dışında bulunduğu ve son dakikada bir emir verdiğin sürece sayılır: açıkta park edilmiş bir gemi hiçbir şey kazanmaz.
2. **Saatlik yumuşak sınır.** Sınırı olan bir değer, sınıra kadar tam XP öder, üstünde ise bir payını; değerin kendi biriminde sayılır (attığın atışlar, verdiğin komutlar, kazandığı XP) ve UTC saatine göre bir saat boyunca. Yeni bir giriş pencereyi yeniden açmaz, sayılar yukarıdaki listede ve aşağıdaki tablodadır.
3. **Eğitim hızı.** Bir beceriyi yöneten nitelik, becerinin kazandığı XP’yi, niteliğin her seviyesinde biraz daha artırır (sınır bundan önce sayılır, yani sınır hızı değil etkinliği sınırlar).
4. **Niteliğin payı.** Beceri XP’yi alır, niteliği de ondan bir pay alır; bu pay hiçbir zaman sınırlanmaz ya da hızlandırılmaz.

Tablo, XP’yi neyin ödediğini değer değer sıralar. XP, ikinci sütunda adı geçen şeyin her birimi için ödenir.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Değer | XP’yi neyin ödediği | XP | Saatlik yumuşak sınır |
| :--- | :--- | ---: | ---: |
| **Kütle** | Son 1 dk içinde emir verilmiş her 10 sn uçuş için: geminin gövde kademesi, takılı her plaka için 0,2 ek, dolu kargo bölmesinde ×1,5 | 1 | Yok |
| **Dayanıklılık** | Bir düşman ya da tehlike yüzünden kaybedilen azami gövdenin her %1’i için | 1 | saatte 300 XP |
|  | Azami gövdenin %25 kadarının altındaki her 10 sn için | 5 |  |
| **Refleks** | Oyunun kabul ettiği her komut için: bir yetenek, bir ekstra, yeni bir hedef, bir toplama, bir üretim, bir diziliş değişimi, bir roket ya da bir sıçrama. Yeni bir hedef en çok 4 sn içinde bir kez, bir toplama en çok 1 sn içinde bir kez ve bir roket en çok 1 sn içinde bir kez öder | 1 | saatte 600 komut |
| **İçgüdü** | Elle ya da bir Retriever ile topladığın her kargo kutusu için | 2 | saatte 600 XP |
|  | Aldığın bir görev ödülünün her eşyası için | 10 |  |
|  | Nadir ya da daha iyi kalitede bir eşyayı ilk kez toplayışın için (her eşya için bir kez, sonsuza dek) | 25 |  |
| **Lazer teknolojisi** (Refleks) | Ateşlediğin her salvo için | 0,1 | saatte 1.800 atış |
|  | Bir gemiye isabet eden her salvo için | 0,1 |  |
| **Roket teknolojisi** (Refleks) | Fırlattığın her roket için | 0,15 | saatte 130 roket |
|  | Bir gemiye isabet eden her roket için (patlaması kaç gemiye zarar verirse versin roket başına bir kez) | 0,3 |  |
| **Antimadde** (İçgüdü) | Bir toplamada aldığın her Dark Matter birimi için | 2,2 | Yok |
| **Nişancılık** (Refleks) | Düz x1 dışındaki cephaneyle ateşlenen bir salvonun her isabeti için (bir saat içinde her cephane türünün ilk 10 dk süresinde ×1,5) | 0,1 | saatte 3.000 isabet |
|  | Bir Mine’ın her isabeti ve bir düşmanın Energetic Wall’unda geçirdiği her saniye için | 0,1 |  |
| **Sabotaj** (Refleks) | Bir Mine’ın her isabeti ve bir düşmanın Energetic Wall’unda geçirdiği her saniye için | 0,5 | saatte 1.200 XP |
|  | Senin bir zehrinin bir düşman üzerinde işlediği her saniye için | 0,05 |  |
| **Kaçınma** (Refleks) | Sana yönelik, ıskalayan ya da kaçınılan her düşman saldırısı için | 1 | saatte 600 XP |
| **Taktik** (Refleks) | Lazer menzilinde bir düşman varken bastığın her yetenek için | 2 | saatte 600 XP |
| **Kalkan soğurması** (Dayanıklılık) | Düşman vuruşlarının aldığı azami kalkanın her %1’i için | 0,1 | saatte 300 XP |
| **Radyasyon teknolojisi** (Dayanıklılık) | Bir radyasyon bandının içindeki her saniye için | 0,2 | Yok |
|  | Radyasyonun aldığı azami gövdenin her %1’i için | 1 |  |
| **İtici teorisi** (Kütle) | Geminin hızının %80 kadarını aşarak uçulan her saniye için, Afterburner altında iki katı | 0,1 | Yok |
| **Bilim** (İçgüdü) | Araştırma Merkezi’nin yaktığı her bilim birimi için | 0,1 | Yok |
|  | Bitirdiğin her teknoloji için | 50 |  |
| **Çıkarma** (İçgüdü) | Skylab’ının ürettiği her kaynak birimi için, topladığında ödenir | 0,1 | Yok |
| **Lojistik** (Kütle) | Skylab bankasına yatırdığın her kaynak birimi için | 0,05 | Yok |
| **İmalat** (Refleks) | Tamamladığın her saniyelik üretim süresi için, topladığında ödenir | 0,1 | Yok |
| **Ticaret** (İçgüdü) | Açık Artırma ya da Mağaza’daki her ticaret için; kredi cinsinden değerinin 1 fazlasının onluk logaritması olarak sayılır (bir Thulium, Açık Artırma’nın değerlendirdiği kadar eder) | 2 | saatte 600 XP |

<!-- skills-xp:end -->

Uçarken uçuş ekranı kazandığın XP’yi birkaç saniyede bir toplanan kısa satırlarla gösterir, bir bayrak da bir değer seviye atladığında ve ne değiştiğinde seni bilgilendirir (Oyun Günlüğü bunun için bir satır tutar). İlk XP’sini kazanan bir değer bir kez duyurulur. Becerilerin oynattığı sayıların ipuçları da bunu söyler, kendi Pilot satırında; hangarın Hasar karosu becerileri dışarıda bırakır ve bunu belirtir: onlar ateş ettiğinde uygulanır.

## Seviye atlama {#levelling-up}

Bir seviye, öncekinden sabit bir oranda daha fazla XP’ye mal olur; böylece ilk seviyeler hızlı gelir, sonuncular uzun sürer. Her değerin eğrisi aynıdır. Bir seviyede sahip olduğun buff her pilot için aynıdır: yalnızca ona ulaşma hızın yaptıklarına bağlıdır.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Seviye | Seviyenin XP’si | 1. seviyeden itibaren toplam XP | Her buff’ın payı |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | %1,01 |
| 10 | 66 | 468 | %9,09 |
| 25 | 170 | 2.174 | %24,24 |
| 50 | 822 | 12.851 | %49,49 |
| 75 | 3.968 | 64.397 | %74,75 |
| 100 | 19.157 | 313.258 | %100 |

<!-- skills-curve:end -->

## Pilot Becerileri sayfası {#the-pilot-skills-page}

**Pilot Becerileri** sayfası istasyonun bir sayfasıdır ve kenar çubuğunda kendi satırı vardır. Bütün ağacı tek bir derli toplu sayfada gösterir: nitelikler ve beceriler beş grup halinde sütunlar boyunca yan yana durur (geniş ekranda üç, dar ekranda daha az), her değer için bir satır vardır; seviyesi sağ kenardadır ve altında ince bir XP çubuğu bulunur. Henüz XP kazanmamış bir değer gridir, seviyesi yerinde bir çizgi görünür. Değerin ne yaptığını, hangi niteliğin yönettiğini ya da hangi becerileri eğittiğini, XP’sini ve neyle büyüdüğünü görmek için işaretçiyi bir satırın üzerinde beklet. Ayrıntılarını sütun sırasının altında açmak için bir satıra tıkla: aynı sözcükler, XP çubuğu ve 1’den sonuncuya kadar herhangi bir seviyeyi önizlemek için bir kaydırıcı; yanında değerin 1. seviyede, şimdiki seviyende, önizlediğin seviyede ve son seviyede neyi değiştirdiğini gösteren küçük bir tablo vardır. Aynı anda yalnızca bir değer açıktır; kapatmak için satıra yeniden tıkla, kapatma düğmesini kullan ya da Esc’ye bas. Sayfayı en son açtığından beri bir değer seviye atladıysa kenar çubuğundaki satır bir rozet alır, Boosterlar penceresindeki bir kart da becerilerinin neyi değiştirdiğini özetler.

Uçuşta aynı sayfa **Pilot Becerileri** penceresidir. Araç çubuğundaki Pilot Becerileri düğmesiyle (geniş bir ekranda) ya da varsayılanı K olan tuşuyla (Ayarlar, Kontroller) aç. Diğerleri gibi bir penceredir: taşıyabilir, boyutunu değiştirebilirsin; yerini ve açık olup olmadığını hatırlar. Yalnızca becerilerini gösterir: uçuşun XP satırları geldikçe seviyeler ilerler, bir satıra tıklamak da aynı ayrıntıları pencerenin içinde açar.

## Nelerin korunduğu {#what-is-kept}

- **Her sıfırlamada.** Ağaç hesabının bir parçasıdır: bir sıfırlama hiçbir seviyeyi ya da XP’yi değiştirmez ve Nakliye Deposu’nun bununla bir ilgisi yoktur ([Neleri korursun](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **Bölgesel sunucularda.** Singapore ya da US East’te uçarken kazandığın XP, eve döndüğünde becerilerine eklenir; orada ilk kez kullandığın değer de dahildir, orada tükettiğin saatlik sınır da seninle gelir. Orada uçan bir pilotun Pilot Becerileri sayfası bölgesel sunucunun sayılarını okur, gemisinin son kaydından beri kazandığı XP ile birlikte.
- **Hesap silinene kadar.** Bir hesabı silmek seviyelerini siler.

Buff’ların son seviyeden başka bir tavanı yoktur: her şeyi geliştirmiş bir pilot, tabloların söylediği kadar güçlüdür.
