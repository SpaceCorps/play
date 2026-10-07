<!-- wiki-i18n source: 201734b1f19e2346 -->
<!-- wiki-i18n title: Propulsão -->
# Propulsão e velocidade {#propulsion-speed}

Os sistemas de propulsão determinam a velocidade de movimento e a manobrabilidade da sua nave.

## Em um minuto {#in-one-minute}

- **Os motores geram velocidade, os propulsores ficam dentro deles e a aumentam.** Um motor comporta de um a três propulsores (um Engine I um, um Engine II dois, um Engine III três), e um núcleo adaptativo também (o nível dele diz quantos).
- **Duas famílias de quatro níveis cada uma.** Os Impulse Thrusters dão mais velocidade fixa. Os Momentum Thrusters dão menos velocidade fixa e multiplicam mais a velocidade. Nas duas famílias, cada nível é melhor que o de baixo, nos dois valores.
- **Qual vai onde.** Como regra, o Momentum vai num Engine III cheio (três propulsores) e o Impulse em qualquer outro lugar: [a tabela abaixo](#which-thruster-where) tem os números. O Engine III mais rápido mistura os dois: um Impulse Thruster IV e dois Momentum Thruster IV dão 62,1.
- **Como conseguir.** O nível I de cada família custa 20.000 créditos. Os níveis II a IV são feitos na Montagem, cada um a partir do nível de baixo, e um propulsor nunca troca de família.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motores {#engines}

Os motores são a principal fonte de empuxo da sua nave. Um motor em um **slot de habilidade** dá a você, em vez disso, o **Afterburner** da coluna Efeito especial, um surto de velocidade por dez segundos (mais tempo com mais motores), e não acrescenta empuxo próprio (veja [Habilidades](/wiki/03-Mechanics/Abilities.md)).

| Nome | Raridade | Velocidade base | Bônus de velocidade % | Bônus de escudo % | Slots | Efeito especial | Custo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Inferior | +2 | +2% | -2% | 1 | Afterburner I | 20.000 créditos |
| **Engine II** | Comum | +4 | +4% | -8% | 2 | Afterburner II | 2.000 Thulium |
| **Engine III** | Raro | +6 | +5% | -15% | 3 | Afterburner III | Só por criação |

O **Engine III** é feito na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules) a partir de um Engine II, com 2.000 Thulium, 60 Ship Fragments, 3 Power Cores e 3 Dark Matter Plates ([Dark Matter e Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Ele mantém o grau de encantamento do motor que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retire primeiro o Engine II da sua nave (e os propulsores de dentro dele): um motor que está encaixado ou que guarda propulsores não é consumido.

O bônus de escudo dos motores consta nos dados do item, mas o jogo nunca o aplicou: os motores não enfraquecem seus escudos, e os cartões dos itens o omitem.

---

## Propulsores {#thrusters}

Os propulsores se encaixam dentro de motores ou de núcleos adaptativos para aumentar a velocidade que eles geram. Há duas famílias de quatro níveis cada uma: os **Impulse Thrusters** dão mais velocidade fixa e multiplicam um pouco a velocidade do motor em que estão encaixados, os **Momentum Thrusters** menos velocidade fixa, mas multiplicam mais. Nas duas famílias, cada nível é melhor que o de baixo, tanto na velocidade fixa quanto no multiplicador. Um motor (ou núcleo adaptativo) com propulsores gera **a própria velocidade base mais os aumentos fixos de velocidade dos propulsores, tudo isso vezes os multiplicadores de velocidade dos propulsores multiplicados entre si** ([como a velocidade é calculada](/wiki/03-Mechanics/Speed.md)): um Engine III com três Momentum Thruster IV gera (6 + 3 x 13,1) x 1,11 x 1,11 x 1,11 = 62,0, com três Impulse Thruster IV (6 + 3 x 16,5) x 1,035 x 1,035 x 1,035 = 61,5, e um Adaptive Core II com dois Impulse Thruster IV gera (0 + 2 x 16,5) x 1,035 x 1,035 = 35,4 (32,3 com dois Momentum Thruster IV).

| Nome | Raridade | Velocidade extra fixa | Multiplicador de velocidade | Custo |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Inferior | +5 | 1,02x | 20.000 créditos |
| **Impulse Thruster II** | Comum | +10 | 1,025x | Só por criação |
| **Impulse Thruster III** | Raro | +15 | 1,03x | Só por criação |
| **Impulse Thruster IV** | Épico | +16,5 | 1,035x | Só por criação |
| **Momentum Thruster I** | Inferior | +4,5 | 1,06x | 20.000 créditos |
| **Momentum Thruster II** | Comum | +9 | 1,07x | Só por criação |
| **Momentum Thruster III** | Raro | +12,5 | 1,09x | Só por criação |
| **Momentum Thruster IV** | Épico | +13,1 | 1,11x | Só por criação |

### Qual propulsor vai onde {#which-thruster-where}

O Impulse dá mais velocidade fixa e o Momentum multiplica mais, então qual é mais rápido depende do que o motor já gera. A velocidade fixa conta mais onde há pouca velocidade para multiplicar: num núcleo adaptativo (ele não tem velocidade própria) e num motor com um ou dois propulsores. O multiplicador conta mais num Engine III cheio, onde há muita velocidade para multiplicar. A velocidade que cada um gera com propulsores de nível IV em todos os slots:

| Onde ficam os propulsores | Com Impulse Thruster IV | Com Momentum Thruster IV | Mais rápido |
| :--- | :---: | :---: | :--- |
| Engine I, 1 propulsor | 19,1 | 16,8 | Impulse |
| Engine II, 2 propulsores | 39,6 | 37,2 | Impulse |
| Engine III, 1 propulsor | 23,3 | 21,2 | Impulse |
| Engine III, 2 propulsores | 41,8 | 39,7 | Impulse |
| Engine III, 3 propulsores | 61,5 | 62,0 | Momentum |
| Adaptive Core II, 2 propulsores | 35,4 | 32,3 | Impulse |

- **Níveis mais baixos.** Os níveis I a III seguem o mesmo caminho, com dois casos apertados: com dois propulsores num Engine II, as famílias ficam empatadas nos níveis I e II (dentro de 0,05), e com dois num Engine III o Momentum fica à frente por cerca de 0,2 nos níveis I e II. A partir do nível III o Impulse lidera nos dois, por 1,4 a 2,4. Num Engine III cheio o Momentum lidera em todos os níveis, por 0,4 a 1,7.
- **Misture-os num Engine III.** O Engine III mais rápido leva um Impulse Thruster IV e dois Momentum Thruster IV: (6 + 16,5 + 2 x 13,1) x 1,035 x 1,11 x 1,11 = 62,1, um pouco acima de três Momentum (62,0) ou três Impulse (61,5).

O bônus de multiplicador de velocidade de um propulsor, vindo da [Forja](/wiki/06-Items/Forge.md), faz crescer a parte acima de 1 (um bônus de +15% sobre 1,11x dá 1,1265x), e a Forja não sorteia bônus para um multiplicador de 1,05x ou menos: no 1,02x a 1,035x de um Impulse Thruster, ele acrescentaria menos de 0,006 (+15% sobre 1,035x dá 1,040x). Um Impulse Thruster comporta um bônus (a velocidade fixa), um Momentum Thruster dois.

O nível I de cada família é vendido por 20.000 créditos. Os níveis II a IV são feitos na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules), cada um a partir do propulsor da mesma família um nível abaixo (um Impulse Thruster II a partir de um Impulse Thruster I, um III a partir de um II, um IV a partir de um III), com Thulium, drops e placas: 2 ou 4 Velkonite Reinforced Plates do seu Skylab para o nível II ou III, e 3 Dark Matter Plates para o nível IV. Um propulsor nunca muda de família: você escolhe Impulse ou Momentum ao comprar o nível I. Cada um mantém o grau de encantamento do propulsor que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Os propulsores não cabem em um [slot de habilidade](/wiki/03-Mechanics/Abilities.md); o lugar deles é dentro de motores e de núcleos adaptativos.

### Deixando os alienígenas para trás {#outrunning-aliens}

Os alienígenas voam a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) e 230 (Crystalys). Uma Ostirion com um Engine II e dois propulsores voa a 223,1 com Impulse Thruster I: ainda abaixo do Crystalys, então é preciso um propulsor feito na Montagem para deixá-lo para trás (234,2 com Impulse Thruster II, 245,5 com III, 249,2 com IV). Os Momentum Thrusters voam igual ou um pouco mais baixo nessa nave (223,2 com um Momentum Thruster I; depois 234,2, 243,8 e 246,7 com II a IV): o nível I das duas famílias fica abaixo de um Crystalys, e todo nível feito na Montagem fica acima.
