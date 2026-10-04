<!-- wiki-i18n source: 68b8f5293ad88b67 -->
<!-- wiki-i18n title: Propulsão -->
# Propulsão e velocidade {#propulsion-speed}

Os sistemas de propulsão determinam a velocidade de movimento e a manobrabilidade da sua nave.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

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

O **Engine III** é feito na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules) a partir de um Engine II, com 2.000 Thulium, 60 Ship Fragments, 3 Power Cores e 6 Velkonite Reinforced Plates do seu Skylab. Ele mantém o grau de encantamento do motor que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retire primeiro o Engine II da sua nave (e os propulsores de dentro dele): um motor que está encaixado ou que guarda propulsores não é consumido.

O bônus de escudo dos motores consta nos dados do item, mas o jogo nunca o aplicou: os motores não enfraquecem seus escudos, e os cartões dos itens o omitem.

---

## Propulsores {#thrusters}

Os propulsores se encaixam dentro de motores ou de núcleos adaptativos para aumentar a velocidade que eles geram. Há duas famílias de quatro níveis cada uma: os **Impulse Thrusters** dão mais velocidade fixa e multiplicam um pouco a velocidade do motor em que estão encaixados, os **Momentum Thrusters** menos velocidade fixa, mas multiplicam mais. Um motor (ou núcleo adaptativo) com propulsores gera **a própria velocidade base mais os aumentos fixos de velocidade dos propulsores, tudo isso vezes os multiplicadores de velocidade dos propulsores multiplicados entre si** ([como a velocidade é calculada](/wiki/03-Mechanics/Speed.md)): um Engine III com três Momentum Thruster IV gera (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, com três Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, e um Adaptive Core II com dois Impulse Thruster IV gera (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (31,2 com dois Momentum Thruster IV).

| Nome | Raridade | Velocidade extra fixa | Multiplicador de velocidade | Custo |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Inferior | +5 | 1,02x | 20.000 créditos |
| **Impulse Thruster II** | Comum | +10 | 1,02x | Só por criação |
| **Impulse Thruster III** | Raro | +15 | 1,03x | Só por criação |
| **Impulse Thruster IV** | Épico | +17 | 1,02x | Só por criação |
| **Momentum Thruster I** | Inferior | +4 | 1,08x | 20.000 créditos |
| **Momentum Thruster II** | Comum | +8 | 1,10x | Só por criação |
| **Momentum Thruster III** | Raro | +11 | 1,13x | Só por criação |
| **Momentum Thruster IV** | Épico | +12 | 1,14x | Só por criação |

Qual família é mais rápida depende de onde ela está. Os Impulse Thrusters geram mais num núcleo adaptativo e num motor com um ou dois propulsores; os Momentum Thrusters do mesmo nível geram mais num Engine III com os três slots ocupados (62,2 contra 60,5 no nível IV, e um Impulse Thruster IV com dois Momentum Thruster IV, 62,3, é o melhor que um Engine III pode ser).

O bônus de multiplicador de velocidade de um propulsor, vindo da [Forja](/wiki/06-Items/Forge.md), faz crescer a parte acima de 1 (um bônus de +15% sobre 1,14x dá 1,161x), e a Forja não sorteia bônus para um multiplicador de 1,05x ou menos: no 1,02x ou 1,03x de um Impulse Thruster, valeria um milésimo. Um Impulse Thruster comporta um bônus (a velocidade fixa), um Momentum Thruster dois.

O nível I de cada família é vendido por 20.000 créditos. Os níveis II a IV são feitos na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules), cada um a partir do propulsor da mesma família um nível abaixo (um Impulse Thruster II a partir de um Impulse Thruster I, um III a partir de um II, um IV a partir de um III), com Thulium, drops e Velkonite Reinforced Plates do seu Skylab (2, 4 e 6 placas). Um propulsor nunca muda de família: você escolhe Impulse ou Momentum ao comprar o nível I. Cada um mantém o grau de encantamento do propulsor que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Os propulsores não cabem em um [slot de habilidade](/wiki/03-Mechanics/Abilities.md); o lugar deles é dentro de motores e de núcleos adaptativos.

### Deixando os alienígenas para trás {#outrunning-aliens}

Os alienígenas voam a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) e 230 (Crystalys). Uma Ostirion com um Engine II e dois propulsores voa a 223,1 com Impulse Thruster I: ainda abaixo do Crystalys, então é preciso um propulsor feito na Montagem para deixá-lo para trás (234,0 com Impulse Thruster II, 245,5 com III, 249,1 com IV). Os Momentum Thrusters voam um pouco mais baixo nessa nave (222,6 com um Momentum Thruster I; 233,2, 242,5 e 245,8 com II a IV): o nível I das duas famílias fica abaixo de um Crystalys, e todo nível feito na Montagem fica acima.
