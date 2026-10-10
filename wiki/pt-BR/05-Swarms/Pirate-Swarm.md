<!-- wiki-i18n source: 1591c57b813b2ba9 -->
<!-- wiki-i18n title: Enxame Pirate -->
# Enxame Pirate {#pirate-swarm}

O enxame Pirate é um **Pirate Boss** com seus **Pirate Scouts**: uma nave enorme e lenta que não ataca ninguém e responde com foguetes, e um bando de naves mais rápidas que a protegem e a curam. Vive nos setores entre a base de uma corporação e a sua fronteira, onde se jogam os níveis intermediários do jogo, e é uma luta longa para um grupo de pilotos, não um abate rápido.

## Resumo rápido {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores `x-2` e `x-3` de cada corporação
- **Quantos**: Um em cada um desses setores, 6 em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset
- **Líder**: Pirate Boss
- **Seguidores**: Até 5 × Pirate Scout, um novo a cada 10 s
- **Os seguidores ficam a**: até 900 unidades do líder
- **Cura**: Cada Pirate Scout a até 600 unidades do líder cura o casco dele, 40 HP por segundo em Alpha
- **Líder destruído**: Os seguidores vão embora 1 min depois que o líder é destruído, a menos que estejam atacando
- **Volta**: 2 min depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- pirate-glance:end -->

## Os membros {#the-members}

- **Pirate Boss**: uma nave baseada na Ironclad, com uma parte da força dela (os números estão abaixo). É passivo e **não dispara lasers**: sua única arma é um **foguete reto** ([Foguetes](/wiki/06-Items/Rockets.md); qual deles depende do setor, veja a tabela), no piloto que o atacou, e ele continua vagueando enquanto dispara. Nunca conserta o próprio casco.
- **Pirate Scout**: uma nave baseada na Kitefin, com uma parte da força dela. Os Scouts atacam qualquer piloto que se aproxime, ficam perto do chefe, e cada um que está perto do chefe cura o casco dele.

## Como a luta transcorre {#how-the-fight-goes}

- **Atire no chefe, não nos Scouts.** Os Scouts curam o chefe, mas a cura é pequena perto do casco dele, e um novo Scout chega com a frequência que a lista *Resumo rápido* indica: um grupo que mata os Scouts primeiro nunca passa à frente deles, e só um grupo muito grande consegue eliminá-los e ainda assim leva mais tempo para acabar com o chefe do que um que os deixou em paz. Os Scouts custam tempo, não decidem a luta.
- **Afaste os Scouts.** Um Scout só cura enquanto está ao alcance do chefe, então um Scout que segue você para fora desse alcance não cura nada, e uma Ostirion é mais rápida que um Scout.
- **Não pare de se mover.** O foguete do chefe é reto e não guiado: uma nave que não para de se mover o esquiva, uma parada é atingida.
- **Leve um grupo.** Três pilotos em Ostirions com munição x2 perdem em `x-3` mesmo enquanto os acertos são divididos; quatro o derrubam em cerca de quatro minutos em Alpha, e três ainda conseguem em `x-2`, mas por pouco. Com munição x4, três bastam também em `x-3` (cerca de dois minutos e meio). Cinco o derrubam em cerca de três minutos quando os acertos são divididos e em pouco mais de quatro quando um piloto leva todo o fogo, e então perdem três naves: um grupo que deixa um piloto levar todo o fogo precisa de cinco. Em Beta são necessários seis pilotos e em Gamma sete, com os acertos divididos (o chefe é maior lá e seus Scouts curam mais). Uma Ostirion sozinha não consegue, uma Paragon sozinha consegue. O chefe responde ao primeiro piloto que o acertou, então deixe a nave mais resistente começar, e use suas habilidades (Emergency Repair, Shield Surge: [Habilidades](/wiki/03-Mechanics/Abilities.md)) numa luta tão longa. Pilotos que ainda são de nível 2 ou 3 são fracos demais para ele, mesmo onde voam: fique longe até estar mais forte.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, no mesmo setor.

## Recompensas e saque {#rewards-and-drops}

O Pirate Boss paga pela luta que ele é: um minuto de luta contra ele paga mais do que um minuto de luta contra um Goombah. O pagamento é dividido pelo dano entre os pilotos que lutaram contra ele ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A caixa dele é para o piloto que mais causou dano e pode conter uma **Reinforced Hull Plate**, foguetes e munição. A caixa dele vale cerca de dois quintos do que o próprio abate paga. Os Scouts pagam pouco e não largam nada.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Base: Ironclad, com 50% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem. Dispara um foguete reto a cada 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) em `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) em `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 300.000 | 450.000 | 600.000 |
| Escudo | 50.100 | 75.150 | 100.200 |
| Dano dos lasers (uma salva por segundo) | nenhum | nenhum | nenhum |
| Velocidade | 92 | 92 | 92 |
| Alcance dos lasers | – | – | – |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Dano dos foguetes, no máximo | 2.500 (Rivet I) / 5.000 (Rivet II) | 3.750 (Rivet I) / 7.500 (Rivet II) | 5.000 (Rivet I) / 10.000 (Rivet II) |
| Créditos | 145.000 | 290.000 | 435.000 |
| Thulium | 725 | 1.450 | 2.175 |
| Experiência (XP) | 29.000 | 58.000 | 87.000 |
| Honra | 232 | 464 | 696 |
| Pontos PvE por abate | 15 | 15 | 15 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50% | 1 |
| Um dos 8 [foguetes](/wiki/06-Items/Rockets.md) comprados com créditos, escolhido ao acaso | 100% | 5–10 |
| Um entre Advanced Plasma e Siphon Battery, escolhido ao acaso | 100% | 1.000–2.000 |

### Pirate Scout

Base: Kitefin, com 50% do casco e 113% do dano dos lasers; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 12.000 | 18.000 | 24.000 |
| Escudo | 9.818 | 14.727 | 19.636 |
| Dano dos lasers (uma salva por segundo) | 221 | 332 | 442 |
| Velocidade | 175 | 175 | 175 |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | 700 | 700 | 700 |
| Cura o líder, cada um, por segundo (só o casco) | 40 | 60 | 80 |
| Créditos | 1.000 | 2.000 | 3.000 |
| Thulium | 4 | 8 | 12 |
| Experiência (XP) | 100 | 200 | 300 |
| Honra | 2 | 4 | 6 |
| Pontos PvE por abate | 4 | 4 | 4 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- pirate-members:end -->
