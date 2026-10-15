<!-- wiki-i18n source: 74226336693d1ae9 -->
<!-- wiki-i18n title: Hız -->
# Hız hesabı {#speed-calculation}

Hız, geminin uzay haritasında ne kadar hızlı hareket ettiğini belirler; hedefleri kovalamana, çatışmadan kaçmana ya da bölgeler arasında geçiş yapmana olanak tanır.

## Hız formülü {#the-speed-formula}

Geminin nihai hızı, sunucuda aşağıdaki formülle hesaplanır:

\[\text{Nihai hız} = (\text{Geminin temel hızı} + \text{Toplam motor hızı}) \times (1,0 + \text{Toplam hız bonusu yüzdesi})\]

Bir [gemi tasarımı](/wiki/03-Mechanics/Ship-Designs.md) ilk terimi değiştirir (THUNDER tasarımında 40 fazla, DUMA tasarımında 20 eksik temel hız vardır); NOTSUM ve RECON ise nihai hızı bir faktörle daha çarpar: +%2 ve +%5.

### 1. Etkin motor hızı {#1-effective-engine-speed}

Takılı her motor hız üretir ve itici taşıyan her Uyarlanabilir Çekirdek de öyle. İticiler motorun içine takılıysa, motorun hızı değişir:

\[\text{Motor hızı} = (\text{Motorun temel hızı} + \text{İtici sabit bonusu}) \times \text{İtici çarpanı}\]

- **İtici sabit bonusu**: iticilerden gelen tüm sabit hız eklemelerinin toplamı (örneğin Impulse Thruster III `+12.75` hız verir).
- **İtici çarpanı**: o motora takılı tüm itici hız çarpanlarının çarpımı (örneğin Momentum Thruster III `1.0765` yani `+7.65%`, Impulse Thruster III `1.0255` yani `+2.55%` değerindedir). Motorun ürettiği her şeyi çarpar: kendi temel hızını ve iticilerin sabit bonuslarını. Bir Uyarlanabilir Çekirdeğin kendi temel hızı yoktur; iticilerinin sabit bonusları yine de aynı şekilde çarpılır.

Üç Momentum Thruster IV (`+11.135`, `1.0935`) takılı bir Engine III (temel hız 6) (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5 üretir; üç Impulse Thruster IV (`+14.025`, `1.02975`) ile (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5 üretir. Bir iticinin çarpanındaki Demirhane bonusu, 1’in üstündeki kısmı büyütür: `1.0935` üzerinde +%15, `1.1075` yapar.

### 2. Azalan getiri (marjinal verimlilik) {#2-diminishing-returns-marginal-efficiency-}

Oyuncuların sonsuz hız için sonsuz motor yığmasını önlemek amacıyla bir **azalan getiri (marjinal verimlilik)** eğrisi uygulanır. Tüm motorlar hıza katkılarına göre sıralanır ve sırayla işlenir. Uyarlanabilir Çekirdekler (hibritler) ve kalkan çekirdekleri de aynı şekilde sıralanır; her tür kendi grubundadır, bu yüzden hem motoru hem Uyarlanabilir Çekirdeği olan bir geminin her birinden ilk dördü vardır:

| Motor sırası | Verimlilik çarpanı |
| :---: | :--- |
| **1. ile 4. arası** | **%100** (1,0) |
| **5.** | **%85** (0,85) |
| **6.** | **%70** (0,70) |
| **7.** | **%55** (0,55) |
| **8. ve sonrası** | **%25** (0,25) |

Ayrıca motor hızı, yuvasının verimliliğiyle çarpılır (Çekirdek: %100, Destek: %75, Yardımcı: %50).

### 3. Hız bonusu yüzdesi ve kalkan cezaları {#3-speed-bonus-percent-shield-penalties}

Toplam hız bonusu yüzdesi, takılı motorlardan (ve hibritlerden) gelen tüm hız bonuslarının toplamından, takılı kalkanların cezalarının çıkarılmasıyla bulunur:

- **Motor hız bonusu**: motorlar olumlu hız yüzdeleri ekler (örneğin Engine III `+5%` ekler).
- **Kalkan hız cezası**: ağır kalkanlar geminin ağırlığını artırır ve olumsuz hız yüzdeleri ekler (örneğin Heavy Shield Core `-5%` hız ekler).
- **Yuva ölçeklemesi**: bu yüzde bonusları ve cezaları da eşyanın takıldığı yuvanın verimliliğiyle ölçeklenir. Dronlarından birindeki bir kalkan, seni bir çekirdek yuvasındaki kalkan gibi yavaşlatır.
- **Sıfırın altına inmez**: kaç kalkan taşırsan taşı, hızın 0’ın altına düşmez.
- **Dron formasyonları**: kuşanılmış bir [dron formasyonu](/wiki/03-Mechanics/Formations.md) nihai hızı bir kez daha, kendi faktörüyle değiştirir: Gyre +%10, Cordon −%3, Auger −%9, Culler −%10, Redoubt −%11, Rampart −%17. Afterburner bundan sonra sonucu çarpar.
