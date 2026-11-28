<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Özel yetenekler -->
# Özel yetenekler {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; özel yetenekler; yenilenme; kalkan patlaması; sertleştirilmiş zırh; öfke; takviye çağırma; klonlar; kaçış ve dönüş; can emme; nova darbesi; roket yaylımı; perde; mayın döşeme -->

Bazı uzaylılar bir **özel yetenek** taşır: gövdelerinin yarısı gittiğinde hayatlarında yalnızca bir kez yaptıkları bir şey. Yenilenme, bir kalkan patlaması, bir kaçış, bir yardım çağrısı. Başlamadan önce hiçbir şey görünmez, bu yüzden her av bir sürprizle bitebilir. Bu sayfa her yeteneğin ne yaptığını ve ona nasıl karşılık verileceğini anlatır. Patronlar farklı çalışır: gövdeleri azaldıkça dövüş biçimlerini üç aşamada değiştirirler; son kademenin küçük uzaylıları ise çok hızlı yok edilirse parçalara ayrılabilir.

## Nasıl çalışır {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Bir kez.** Yetenek taşıyan bir uzaylı, onu ömründe yalnızca bir kez kullanır: bir savaşta gövdesi (kalkanı değil) azami değerinin %50 altına düştüğünde. Onu bu çizginin üstünden yok eden bir vuruş ateş etmesine asla izin vermez, savaşta olmayan bir uzaylı da bir savaş başlayana kadar bekler.
- **Önce bir uyarı.** Yetenek bir uyarıyla başlar: geminin üzerine kapanan bir halka ve üstünde bir sözcük. Aşağıdaki girdisinde hemen başladığı yazan bir yeteneğin uyarısı yoktur. Uyarı sırasında uzaylı hâlâ yok edilebilir; o zaman hiçbir şey olmaz ve her zamanki gibi ödeme yapar. Hafif türler (Seeker ve Phantasm) daha çabuktur: uyarıları ve etkileri normalin %50 kadar sürer.
- **Öncesinde hiçbir şey görünmez.** Yetenek taşıyan bir uzaylı, uyarısı başlayana kadar her ayrıntısıyla diğerleri gibi görünür. Oyunda hiçbir şey hangisinin olduğunu söylemez, [Gezgin Rehberi](/wiki/03-Mechanics/Travelers-Guide.md) bile.
- **Kim taşır.** Şirket sektörlerindeki ve Tehlike Sektörlerindeki uzaylıların küçük bir kısmı: kademe ne kadar güçlüyse pay o kadar büyüktür ve sürülerin liderleri (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah ve Boss Crystalys) diğerlerinden daha olası taşıyıcılardır. Deep Void'in, klan zindanlarının ve solo geçitlerin uzaylıları asla taşımaz; bir sürünün takipçileri, bir Warden'ın dalgaları, Dormant Force ve Tesseract da taşımaz.
- **Her uzaylının ödediğini öder.** Yetenek kullanan bir uzaylı, kullanmayanla tamamen aynı şekilde öder, düşürür ve sayılır: yetenek öldürmeye hiçbir şey katmaz, ondan zaman alır. Öldürme, onu elinde tutan pilotta kalır: uzaylı kaçarken, onarılırken ya da saklanırken hak düşmez.
- **Çağrılan gemiler ve kopyalar öldürme sayılmaz.** Bir uzaylının çağırdığı gemiler ve yaptığı kopyalar hiçbir şey ödemez, hiçbir şey düşürmez ve hiçbir görev, istatistik ya da sıralamada sayılmaz. Çağıran başına en fazla 6, bir haritada en fazla 24 yaşar; haritanın kendi uzaylıları ise zamanında geri gelmeye devam eder.
- **Haritadaki herkes görür.** Haritadaki pilotlara bir yeteneğin ne zaman başladığı bildirilir: oyun halkayı, sözcüğü ve etkiyi çizer ve bir ses çalar.

<!-- mob-rules:end -->

## On iki yetenek {#the-twelve-abilities}

Bir yetenek, girdisi hemen başladığını söylemedikçe bir **uyarıyla** başlar: geminin üstüne kapanan bir halka ve onun üzerinde bir sözcük. Aşağıdaki süreler ve sayılar ağır türler içindir. Bir sayının birden çok değeri varsa, bunlar parantez içinde adı geçen kademelere, yani bir uzaylının adından önceki Yunan harfine aittir.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Yenilenme {#regenerate}

Yerinde durur ve 6 sn içinde gövdesinin ve kalkanının %15 / %20 / %25 / %30 (α / β / γ / δ) kadarını onarır, bu sırada hiçbir şey ateşlemez. Gövdesi ve kalkanı birlikte %10 tutan hasar onu böler ve o ana kadar onardığını korur.

- **Uyarı**: 1,5 sn
- **Geminin üzerindeki sözcük**: YENİLENİYOR
- **Taşıyan**: herhangi bir uzaylı
- **Karşılık**: Roketlerle ya da bir gemi kalabalığıyla hızla eritin veya uyarı sırasında yok edin.

### Kalkan patlaması {#shield-burst}

Kalkanının üzerine azami gövdesinin %15 / %20 / %30 / %40 (α / β / γ / δ) kadar yeni bir kalkan katmanı biner. Ayakta olduğu sürece bir vuruşun her puanını alır; tükendiğinde ya da 10 sn sonra gider.

- **Uyarı**: 1 sn
- **Geminin üzerindeki sözcük**: KALKAN
- **Taşıyan**: herhangi bir uzaylı
- **Karşılık**: Kalkanları delen mühimmat ve roketler ondan daha iyi geçer. Ya da gidene kadar başka bir uzaylıya ateş edin.

### Sertleştirilmiş zırh {#hardened-plating}

7 sn / 8 sn / 10 sn (β / γ / δ) boyunca gövde ve kalkan fark etmeksizin her vuruşun yalnızca %50 kadarını alır: iki kat dayanıklı. Savaşmaya devam eder ve vuruşlarınızın sayıları grileşir.

- **Uyarı**: 1,5 sn
- **Geminin üzerindeki sözcük**: ZIRH
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Pirate Boss ve Boss Phantasm), β ve üstü
- **Karşılık**: Bitmesini bekleyin, bu arada başka bir uzaylıya vurun ve ardışık vuruşlarınızı sonrası için saklayın.

### Öfke {#enrage}

10 sn boyunca hasarı ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) ile, hızı ×1,25 ile çarpılır.

- **Uyarı**: 1 sn
- **Geminin üzerindeki sözcük**: ÖFKELİ
- **Taşıyan**: herhangi bir uzaylı
- **Karşılık**: Kalkanınızı yukarıda tutun, hareket edin ve menzilinin dışında kalın.

### Takviye çağırma {#call-reinforcements}

4 / 6 (γ / δ) küçük uzaylı haritanın en yakın kenarından, 3 sn arayla 2 dalga hâlinde girer. Gelen tür: Phantasm (Bulwark ve Goombah çağırdı); Bulwark (Crystalys çağırdı). Birlikte gövdesinin ve kalkanının %45 / %60 (γ / δ) kadarına sahiptirler ve salvosunun %50 kadarını ateşlerler. Hiçbir şey ödemez, hiçbir şey düşürmez ve hiçbir şeyde sayılmazlar; 45 sn sonra ya da çağıran yok edilince giderler.

- **Uyarı**: 2 sn
- **Geminin üzerindeki sözcük**: TAKVİYE ÇAĞIRIYOR
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Boss Phantasm ve Boss Goombah), γ ve üstü
- **Karşılık**: Çağıranı yok edin: gemileri onunla birlikte gider. Alana vuran bir silah onları temizler.

### Klonlar {#clones}

Etrafında adı ve görünüşüyle 3 (γ / δ) kopyası belirir. Birlikte gövdesinin ve kalkanının %18 (γ / δ) kadarına sahiptirler; hiçbir şey ateşlemez ve hiçbir şey ödemezler, 15 sn ya da gerçeği yok edilene kadar dururlar. Kopyalar dışarıdayken gerçeği ince bir halka taşır ve Hedef penceresi bir kopyaya "Yem" der.

- **Uyarı**: 1 sn
- **Geminin üzerindeki sözcük**: KLONLUYOR
- **Taşıyan**: herhangi bir uzaylı, γ ve üstü
- **Karşılık**: Gerçeğinin halkasını ve hareket eden gövde çubuğunu izleyin ya da alana vuran bir silah kullanın.

### Kaçış ve dönüş {#flee-and-return}

5 sn / 6 sn / 7 sn / 8 sn (α / β / γ / δ) boyunca saldırganlarından ×2 hızla uzaklaşır, sonra ona ilk vuran pilota döner. Haritadan asla ayrılmaz, güvenli bölgeye girmez, her an vurulabilir ve öldürmeyi elinde tutan pilot onu korur.

- **Uyarı**: 0,5 sn
- **Geminin üzerindeki sözcük**: KAÇIYOR
- **Taşıyan**: herhangi bir uzaylı
- **Karşılık**: Kovalayın ya da uçarken roketle vurun.

### Can emme {#life-drain}

10 sn boyunca başka bir şey ateşlemez: saniyede bir menzilindeki her gemiyi hiçbir şeyin kaçınamadığı tam bir salvoyla emer ve verdiği hasarın %75 / %100 / %100 (β / γ / δ) kadarını onarır; toplamda gövdesinin en fazla %20 kadarını.

- **Uyarı**: 1 sn
- **Geminin üzerindeki sözcük**: EMİYOR
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Pirate Boss, Boss Phantasm, Boss Goombah ve Boss Crystalys), β ve üstü
- **Karşılık**: Hattın üzerine bir kaya ya da duvar koyun, gizlenin ya da menzilinden çıkın.

### Nova darbesi {#nova-pulse}

Uyarı sırasında etrafındaki zeminde bir halka büyür. Halka dolunca içindeki her gemiye bir kez, salvolarının 4 / 5 (γ / δ) kadarıyla vurur. Yarıçapı, birim cinsinden, 700 / 800 (γ / δ).

- **Uyarı**: 2,5 sn
- **Geminin üzerindeki sözcük**: NOVA
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Pirate Boss, Boss Phantasm ve Boss Goombah), γ ve üstü
- **Karşılık**: Halka dolmadan önce halkadan çıkın: kaçınabileceğiniz tek patlama bu.

### Roket yaylımı {#rocket-barrage}

3 sn içinde hedefine 4 / 6 / 8 (β / γ / δ) [Rivet roketi](/wiki/06-Items/Rockets.md#the-twelve-rockets) ateşler: Rivet I / II / II (β / γ / δ). Düz uçarlar ve güdümlü değildirler.

- **Uyarı**: 1,5 sn
- **Geminin üzerindeki sözcük**: YAYLIM
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Boss Phantasm ve Boss Goombah), β ve üstü
- **Karşılık**: Hareket edin: roketler düz gider. Yoldaki bir kaya onları durdurur.

### Perde {#veil}

6 sn / 8 sn (γ / δ) boyunca ondan 700 birimden uzaktaki bir gemi ona kilitlenemez ve elindeki kilit kaybolur. Bundan yakınsa her zamanki gibi görülür. Savaşmaya devam eder ve patlama yine ona zarar verir.

- **Uyarı**: yok, hemen başlar.
- **Geminin üzerindeki sözcük**: GİZLENİYOR
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Pirate Boss, Boss Phantasm, Boss Goombah ve Boss Crystalys), γ ve üstü
- **Karşılık**: 700 birim içine kadar yaklaşın.

### Mayın döşeme {#sow-mines}

Hedefinin durduğu yerin etrafında 500 birimlik bir halkaya 4 / 6 / 8 (β / γ / δ) mayın döşer. Bir mayın düştükten 3 sn sonra devreye girer, 30 sn kalır ve üzerinden geçen ilk pilot gemisinin altında bir kez patlar, uzaylının salvolarının 2 / 3 / 3 (β / γ / δ) kadarıyla. Bir mayın bir uzaylıya asla zarar vermez.

- **Uyarı**: 1,5 sn
- **Geminin üzerindeki sözcük**: MAYIN DÖŞÜYOR
- **Taşıyan**: ağır türler (Bulwark, Goombah ve Crystalys) ve ağır sürü liderleri (Pirate Boss, Boss Phantasm, Boss Goombah ve Boss Crystalys), β ve üstü
- **Karşılık**: Etraflarından uçun: yere çizilidirler ve geç devreye girerler.


<!-- mob-abilities:end -->

## Parçalanma {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Son kademedeki küçük uzaylılar çok hızlı yok edilirlerse bölünebilir. Bu yalnızca δ kademesinin Seeker, Phantasm, Bulwark, Goombah ve Crystalys türlerine özgüdür, başka hiçbir uzaylıda yoktur ve yukarıdaki yeteneklerden biri değildir: bir uzaylı ikisine de sahip olabilir.

- **Ne zaman**: bir pilot onu aldığı ilk hasardan sonra 5 sn içinde yok eder. O kadar hızlı ölen her uzaylı bölünmez.
- **Ne çıkar**: aynı tür ve kademeden 3 uzaylı, boyutunun %70 kadarı; her biri gövdesinin ve kalkanının %25 kadarına ve tam bir salvoya sahip olarak yok edildiği yerin etrafında belirir. Onu yok eden pilota giderler ve 180 sn sonra ayrılırlar.
- **Sıradan uzaylılardır**: her biri türünün ödediğini öder, düşürdüğünü düşürür ve görevlerde ve istatistiklerde sayılır. Yetenek taşımazlar ve asla bölünmezler.
- **Sınırlar**: bir haritada en fazla 60 parça yaşar ve haritanın kendi uzaylılarını geri tutmazlar.
- **Ne anlama gelir**: uzaylılarını yeterince hızlı yok eden bir mürettebat tek bir uzaylıdan en fazla 4 öldürme alabilir. Yapamayan hiçbir şey alamaz.

<!-- mob-split:end -->

## Patronların üç aşaması {#the-bosses-three-steps}

Her patron dövüş biçimini üç aşamada değiştirir: dövüş başladığında, gövdesi üçte ikinin altına düştüğünde ve üçte birin altına düştüğünde. Bir aşama bir kez olur ve asla geri dönmez, ancak patron aşağıda anlatıldığı gibi baştan başlarsa durum değişir.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Her aşamada bir duraklama.** İlkinden sonra yapacak işi olan bir aşama başladığında patron 1,5 sn boyunca yaralanamaz (Dungeon Warlord ve solo geçit patronları için 3 sn).
- **Bir de özel yetenek.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah ve Boss Crystalys özel bir yetenek de taşıyabilir (Dormant Force ve Tesseract asla taşımaz): ikinci ve üçüncü aşama arasında gelir; ikisi birlikte başlayacaksa sonraki en fazla 3 sn bekler. Liderin kendi aşamalarının kullandığı bir yetenek asla olmaz.
- **Baştan başlama.** Tesseract tamamen onarıldığında aşamalarına baştan başlar.

### Sürü liderleri {#the-swarm-leaders}

| Lider | Başlangıçta | Üçte ikinin altında | Üçte birin altında |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Ona ilk vuran pilota, aralarında 12 derece olan 3 roketlik bir yelpaze ateşler. | Bir kerede 5 Pirate Scouts daha çağırır, en fazla 10 canlı. Hiçbir şey ödemezler ve 45 sn sonra giderler. | 10 sn boyunca ×1,8 hızla en yakın geçide uçar, sonra pilotlara döner. |
| **Boss Seeker** | Seeker Slaves onu 8 sn boyunca ×2 hızla onarır. | Kopyalarından 2 tanesi belirir ve gerçeği bir halka taşır. | 4 sn boyunca pilotlardan kaçar, sonra döner. |
| **Boss Phantasm** | Phantasm Guards her biri kendi gövdesinin %10 kadar bir kalkan katmanı kurar. | Kopyalarından 3 tanesi belirir ve gerçeği bir halka taşır. | Pilotlardan yaklaşık 2.500 birim uzağa ışınlanır ve Phantasm Guards sapasağlam etrafına döner. |
| **Boss Goombah** | 6 sn boyunca her vuruşun yalnızca %50 kadarını alır. | 10 sn boyunca hasarı ×1,5 ile, hızı ×1,25 ile çarpılır. | Gövdesinin ve kalkanının %25 kadarını onarır (bir hasar patlaması onu böler) ve bu sırada Goombah Guards onu ×2 hızla onarır. |
| **Boss Crystalys** | 8 sn boyunca her vuruşun yalnızca %50 kadarını alır. | 700 birimlik bir halka içindeki her gemiye salvolarının 4 kadarıyla vurur ve 4 roket ateşler. | Gövdesinin ve kalkanının %20 kadarını onarır (bir hasar patlaması onu böler) ve 3 Crystalys Guards daha gelir, en fazla 6 canlı. |
| **Dormant Force** | Dormant Pulses içinden biri yaşadığı sürece her vuruşun yalnızca %70 kadarını alır. | Dormant Pulses 15 sn boyunca her 2,5 sn bir roket ateşler. | Dormant Pulses hepsi yaşadığı sürece 6 sn boyunca saniyede gövdesinin %5 kadarını onarır. |
| **Tesseract** | – | Olağan sayılarının üzerinde 20 Facets daha bir kerede gelir. | – |

### Klan Warden'ları {#the-clan-wardens}

| Warden | Başlangıçta | Üçte ikinin altında | Üçte birin altında |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | 4 dronun hepsi bir kerede yanına gelir. | Dronları onu 15 sn boyunca ×1,5 hızla onarır. | Olağan sayının üzerinde 2 dron daha 30 sn boyunca gelir. Hiçbir şey ödemezler. |
| **Siege Warden** (I, II, III) | – | 20 sn boyunca roketini ×2 sıklıkla ateşler. | Gövdesinin ve kalkanının %15 kadarını onarır (bir hasar patlaması onu böler). |
| **Wrath Warden** (I, II, III) | – | Lazerleri ×1,25 güçle vurur. | Lazerleri toplamda ×1,5 güçle vurur, önceki aşamanın üzerine eklenmez. |

### Dungeon Warlord {#the-dungeon-warlord}

- **Üçte ikinin altında**: Yetenekleri arasındaki boşluk 4 sn değerine, bekleme süreleri ×0,75 değerine düşer.
- **Üçte birin altında**: Boşluk 2 sn değerine, bekleme süreleri ×0,5 değerine düşer ve hasarı ×1,25 değerine yükselir; bir bedava Meteor salvosu atar ve Swarm yeteneği her 120 sn aralıktan daha sık geri gelmez.
- **Her aşamada bir duraklama.** Bir aşama başladığında Warlord 3 sn boyunca yaralanamaz.

### Solo geçit patronları {#the-solo-gate-bosses}

Solo geçitlerin altı patronunun da üç aşaması, yani evreleri vardır: Solo Geçitler makalesindeki [patronlar](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) tablosunda yer alırlar.

<!-- mob-ladders:end -->

## Daha fazlası {#where-to-read-more}

- [Savaş](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): bir uzaylı kimle savaşır ve yok edilmesini kim alır.
- [Sürüler](/wiki/05-Swarms/Swarms.md): liderler ve aşamaları, her sürü için ayrı bir makale.
- [Klan Warden'ları](/wiki/03-Mechanics/Clans.md#fighting-a-warden), [Zindan Warlord'u](/wiki/03-Mechanics/Dungeons.md#the-warlord) ve [solo geçitlerin patronları](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Gezgin Rehberi](/wiki/03-Mechanics/Travelers-Guide.md): bir uzaylı hakkında öğrendiklerin. Hangisinin yetenek taşıdığını asla söylemez.
