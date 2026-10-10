<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Propulsão -->
# Propulsão e velocidade {#propulsion-speed}

Os sistemas de propulsão determinam a velocidade de movimento e a manobrabilidade da sua nave.

## Em um minuto {#in-one-minute}

- **Os motores geram velocidade, os propulsores ficam dentro deles e a aumentam.** Um motor comporta de um a três propulsores (um Engine I um, um Engine II dois, um Engine III três), e um núcleo adaptativo também (o nível dele diz quantos).
- **Duas famílias de quatro níveis cada uma.** Os Impulse Thrusters dão mais velocidade fixa. Os Momentum Thrusters dão menos velocidade fixa e multiplicam mais a velocidade. Nas duas famílias, cada nível é melhor que o de baixo, nos dois valores.
- **Qual vai onde.** Como regra, ponha o Impulse em qualquer lugar: só num Engine III cheio (três propulsores) o Momentum dos níveis I e II sai na frente. [A tabela abaixo](#which-thruster-where) tem os números. O Engine III mais rápido leva três Impulse Thruster IV e dá 52,5.
- **Como conseguir.** O nível I de cada família custa 20.000 créditos. Os níveis II a IV são feitos na Montagem, cada um a partir do nível de baixo, e um propulsor nunca troca de família.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motores {#engines}

Os motores são a principal fonte de empuxo da sua nave. Um motor em um **slot de habilidade** dá a você, em vez disso, o **Afterburner** da coluna Efeito especial, um surto de velocidade por dez segundos (mais tempo com mais motores), e não acrescenta empuxo próprio (veja [Habilidades](/wiki/03-Mechanics/Abilities.md)).

| Nome | Raridade | Velocidade base | Bônus de velocidade % | Bônus de escudo % | Slots | Efeito especial | Custo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Inferior | +2 | +2% | -2% | 1 | Afterburner I | 20.000 créditos |
| **Engine II** | Comum | +4 | +4% | -8% | 2 | Afterburner II | Só por criação |
| **Engine III** | Raro | +6 | +5% | -15% | 3 | Afterburner III | Só por criação |

O **Engine II** é feito na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules) a partir de um Engine I, com 1.000 Thulium, 10 Ship Fragments, 1 Power Core e 2 Velkonite Reinforced Plates. O **Engine III** é feito lá a partir de um Engine II, com 2.000 Thulium, 60 Ship Fragments, 3 Power Cores e 3 Dark Matter Plates ([Dark Matter e Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Cada um mantém o grau de encantamento do motor que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retire primeiro da sua nave o motor que será consumido (e os propulsores de dentro dele): um motor que está encaixado ou que guarda propulsores não é consumido.

O bônus de escudo dos motores consta nos dados do item, mas o jogo nunca o aplicou: os motores não enfraquecem seus escudos, e os cartões dos itens o omitem.

---

## Propulsores {#thrusters}

Os propulsores se encaixam dentro de motores ou de núcleos adaptativos para aumentar a velocidade que eles geram. Há duas famílias de quatro níveis cada uma: os **Impulse Thrusters** dão mais velocidade fixa e multiplicam um pouco a velocidade do motor em que estão encaixados, os **Momentum Thrusters** menos velocidade fixa, mas multiplicam mais. Nas duas famílias, cada nível é melhor que o de baixo, tanto na velocidade fixa quanto no multiplicador. Um motor (ou núcleo adaptativo) com propulsores gera **a própria velocidade base mais os aumentos fixos de velocidade dos propulsores, tudo isso vezes os multiplicadores de velocidade dos propulsores multiplicados entre si** ([como a velocidade é calculada](/wiki/03-Mechanics/Speed.md)): um Engine III com três Momentum Thruster IV gera (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, com três Impulse Thruster IV (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5, e um Adaptive Core II com dois Impulse Thruster IV gera (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 com dois Momentum Thruster IV).

| Nome | Raridade | Velocidade extra fixa | Multiplicador de velocidade | Custo |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Inferior | +4,25 | 1,017x | 20.000 créditos |
| **Impulse Thruster II** | Comum | +8,5 | 1,02125x | Só por criação |
| **Impulse Thruster III** | Raro | +12,75 | 1,0255x | Só por criação |
| **Impulse Thruster IV** | Épico | +14,025 | 1,02975x | Só por criação |
| **Momentum Thruster I** | Inferior | +3,825 | 1,051x | 20.000 créditos |
| **Momentum Thruster II** | Comum | +7,65 | 1,0595x | Só por criação |
| **Momentum Thruster III** | Raro | +10,625 | 1,0765x | Só por criação |
| **Momentum Thruster IV** | Épico | +11,135 | 1,0935x | Só por criação |

### Qual propulsor vai onde {#which-thruster-where}

O Impulse dá mais velocidade fixa e o Momentum multiplica mais, então qual é mais rápido depende do que o motor já gera. A velocidade fixa conta mais onde há pouca velocidade para multiplicar: num núcleo adaptativo (ele não tem velocidade própria) e num motor com um ou dois propulsores. O multiplicador conta mais num Engine III cheio, onde há muita velocidade para multiplicar, mas ali só o Momentum dos níveis I e II vence. A velocidade que cada um gera com propulsores de nível IV em todos os slots:

| Onde ficam os propulsores | Com Impulse Thruster IV | Com Momentum Thruster IV | Mais rápido |
| :--- | :---: | :---: | :--- |
| Engine I, 1 propulsor | 16,5 | 14,4 | Impulse |
| Engine II, 2 propulsores | 34,0 | 31,4 | Impulse |
| Engine III, 1 propulsor | 20,6 | 18,7 | Impulse |
| Engine III, 2 propulsores | 36,1 | 33,8 | Impulse |
| Engine III, 3 propulsores | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 propulsores | 29,7 | 26,6 | Impulse |

- **Níveis mais baixos.** Os níveis mais baixos seguem o mesmo caminho, com dois casos apertados e uma exceção: com dois propulsores num Engine II, as famílias ficam empatadas nos níveis I e II (o Impulse fica à frente por 0,06 e 0,24), e com dois num Engine III também (dentro de 0,1). A partir do nível III o Impulse lidera nos dois, por 1,5 a 2,6. A exceção é o Engine III cheio: ali o Momentum lidera nos níveis I e II, por 0,6 e 0,9, e o Impulse nos níveis III e IV, por 0,5 e 1,0.
- **O Engine III mais rápido.** Leva três Impulse Thruster IV: 52,5, um pouco acima de um Impulse e dois Momentum Thruster IV (52,1) ou de três Momentum (51,5).

O bônus de multiplicador de velocidade de um propulsor, vindo da [Forja](/wiki/06-Items/Forge.md), faz crescer a parte acima de 1 (um bônus de +15% sobre 1,0935x dá 1,1075x), e a Forja não sorteia bônus para um multiplicador de 1,05x ou menos: no 1,017x a 1,02975x de um Impulse Thruster, ele acrescentaria menos de 0,005 (+15% sobre 1,02975x dá 1,034x). Um Impulse Thruster comporta um bônus (a velocidade fixa), um Momentum Thruster dois.

O nível I de cada família é vendido por 20.000 créditos. Os níveis II a IV são feitos na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules), cada um a partir do propulsor da mesma família um nível abaixo (um Impulse Thruster II a partir de um Impulse Thruster I, um III a partir de um II, um IV a partir de um III), com Thulium, drops e placas: 2 ou 4 Velkonite Reinforced Plates do seu Skylab para o nível II ou III, e 3 Dark Matter Plates para o nível IV. Um propulsor nunca muda de família: você escolhe Impulse ou Momentum ao comprar o nível I. Cada um mantém o grau de encantamento do propulsor que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Os propulsores não cabem em um [slot de habilidade](/wiki/03-Mechanics/Abilities.md); o lugar deles é dentro de motores e de núcleos adaptativos.

### Deixando os alienígenas para trás {#outrunning-aliens}

Os alienígenas voam a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) e 230 (Crystalys). Uma Ostirion com um Engine II e dois propulsores voa a 221,4 com Impulse Thruster I: ainda abaixo do Crystalys, então é preciso um propulsor feito na Montagem para deixá-lo para trás (230,8 com Impulse Thruster II, 240,3 com III, 243,3 com IV). Os Momentum Thrusters voam igual ou um pouco mais baixo nessa nave (221,4 com um Momentum Thruster I; depois 230,5, 238,4 e 240,7 com II a IV): o nível I das duas famílias fica abaixo de um Crystalys, e todo nível feito na Montagem fica acima, o nível II por apenas 0,8 e 0,5.
