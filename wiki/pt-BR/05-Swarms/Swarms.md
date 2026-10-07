<!-- wiki-i18n source: 2e7e76790e2b0906 -->
<!-- wiki-i18n title: Enxames -->
# Enxames {#swarms}

Um **enxame** é um grupo de alienígenas que percorre uma parte da galáxia sob um **líder**: um chefe muito mais forte do que qualquer alienígena ao seu redor, com **seguidores** que o protegem e, em dois dos enxames, o curam. São três, e cada um tem um artigo próprio:

- [Enxame Seeker](/wiki/05-Swarms/Seeker-Swarm.md): o Boss Seeker e seus Seeker Slaves, o menor enxame, nos setores onde os pilotos novos voam.
- [Enxame Pirate](/wiki/05-Swarms/Pirate-Swarm.md): o Pirate Boss e seus Pirate Scouts, uma luta longa para um grupo.
- [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md): a Dormant Force e suas Dormant Pulses, o enxame mais forte, com o saque mais rico.

As naves deles são **alienígenas de tipos próprios**: têm nomes próprios e contagens de abates próprias, e nenhuma conta como um Seeker, um Phantasm ou qualquer outro alienígena. Uma nave de enxame tem a forma da nave em que se baseia, com uma tonalidade própria e o nome por cima; o Boss Seeker é um Seeker bem maior.

Os **Guardiões do clã** não são enxames públicos. Um clã invoca o seu próprio Guardião para a última etapa da sua linha diária, e só esse clã pode feri-lo: nenhum piloto encontra um deles vagando por um setor, e as tabelas abaixo não os listam. Um Guardião é pago por dano, como o chefe de um enxame, mas o saque dele não é uma caixa para quem causou mais dano: cada piloto que causou 5% do dano ou mais recebe uma [caixa privada](/wiki/03-Mechanics/Cargo.md#private-boxes) só dele. Veja [Clãs](/wiki/03-Mechanics/Clans.md#clan-wardens).

## Os três enxames {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Enxame | Onde | Quantos | Líder | Seguidores | Volta |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Enxame Pirate**](/wiki/05-Swarms/Pirate-Swarm.md) | Os setores `x-2` e `x-3` de cada corporação | Um em cada um desses setores, 6 em cada mundo | **Pirate Boss** | Até 5 × Pirate Scout, um novo a cada 10 s | 2 min depois que o líder é destruído, no mesmo setor |
| [**Enxame Dormant**](/wiki/05-Swarms/Dormant-Swarm.md) | Os setores de perigo `DS-1`, `DS-2`, `DS-3`, `DS-4`, voando de um para outro | Um em cada mundo | **Dormant Force** | 2 × Dormant Pulse, voando com o líder | 1 h depois que o enxame inteiro é destruído, num setor de perigo aleatório |
| [**Enxame Seeker**](/wiki/05-Swarms/Seeker-Swarm.md) | Os setores `x-1` e `x-2` de cada corporação | Um em cada um desses setores, 6 em cada mundo | **Boss Seeker** | Até 4 × Seeker Slave, um novo a cada 10 s | 2 min depois que o líder é destruído, no mesmo setor |

<!-- swarms-list:end -->

## Quando e onde {#when-and-where}

Os enxames começam a aparecer no **Primeiro Contato** e ficam até o reset (veja a [Linha do tempo do reset](/wiki/03-Mechanics/Wipe-Timeline.md); o dia é a primeira linha das regras abaixo). **Cada mundo tem os seus próprios enxames** nos mesmos lugares, então o Pirate Boss de Alpha e o de Beta são duas naves diferentes, e um enxame que você destrói no seu mundo não é destruído em outro. Um enxame destruído volta depois do tempo da tabela acima.

## As regras de todo enxame {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Os enxames aparecem a partir do dia 4 da temporada até o reset.
- Quando uma nave de enxame é acertada, as naves do seu enxame a até 1.500 unidades dela entram na luta contra o primeiro piloto que a acertou.
- Um líder aparece a pelo menos 2.500 unidades da borda de cada anel de estação e de portão.
- Um piloto que causou pelo menos 5% do dano feito a um chefe é pago pelo abate dele.

<!-- swarms-rules:end -->

## Os mundos {#the-worlds}

O mundo escala um enxame como escala todo alienígena ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): o casco, o escudo, a recarga do escudo, o dano dos lasers, o dano dos foguetes e a cura de uma nave de enxame são os números de Alpha vezes a força abaixo, e um abate paga a recompensa abaixo. Velocidade, alcance e saque são iguais em todos os mundos. Os artigos dão os números de cada nave nos três mundos.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Mundo | Força | Pagamento |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## O que os pilotos ficam sabendo {#what-the-pilots-are-told}

Os enxames Seeker e Pirate avisam os pilotos do seu próprio setor quando um chefe aparece e quando é destruído. O enxame Dormant avisa o mundo inteiro e é marcado nos mapas dos setores de perigo e no mapa da galáxia, para que os pilotos possam encontrá-lo. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O abate de um chefe também ganha uma linha no registro de baixas, que nomeia o piloto a quem ele é creditado. A lista *Resumo rápido* de cada artigo diz quem é avisado.

## Lutando contra um enxame {#fighting-a-swarm}

- **Os líderes nunca começam uma luta.** Um líder vagueia até um piloto acertá-lo, então revida, e as naves do seu enxame perto dele entram na luta contra o primeiro piloto que o acertou (a distância está nas regras acima). Os Pirate Scouts são a exceção: atacam qualquer piloto que se aproxime. Um líder nunca conserta o próprio casco, então o dano que você causou fica nele, a menos que seus seguidores o curem; o escudo recarrega como o de qualquer alienígena.
- **Naves de enxame só lutam contra pilotos.** Elas não atiram em alienígenas e os alienígenas não atiram nelas, e os [pilotos de corporação](/wiki/03-Mechanics/Company-Pilots.md) as ignoram: não caçam uma nave de enxame nem vêm em seu auxílio contra uma.
- **Foguetes.** O Pirate Boss, a Dormant Force e as Pulses disparam foguetes **retos**, os [foguetes Rivet](/wiki/06-Items/Rockets.md), no piloto que os atacou. Uma nave que não para de se mover os esquiva; uma parada é atingida.
- **O tamanho das lutas.** O enxame Seeker é para dois pilotos, o Pirate para um grupo pequeno e o Dormant para um grupo grande das naves mais fortes; os mundos mais altos pedem mais pilotos, como com qualquer alienígena.

## O que levar {#what-to-bring}

- **Um grupo.** Voe em [grupo](/wiki/03-Mechanics/Groups.md): os enxames são equilibrados para grupos, um piloto sozinho de nível baixo é destruído rápido, e só as naves mais fortes conseguem derrotar um Pirate Boss sozinhas. Ninguém derrota o enxame Dormant sozinho. Um enxame luta contra o primeiro piloto que o acertou ([Contra quem um alienígena luta](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), então deixe a nave mais resistente do grupo começar.
- **Munição melhor.** Leve munição x2 ou melhor (veja [Lasers e munição](/wiki/06-Items/Lasers.md)). A cura dos seguidores de um enxame pode superar o que um grupo pequeno causa com munição x1.
- **Escudos e reparos** para uma luta longa: as habilidades da sua nave ([Habilidades](/wiki/03-Mechanics/Abilities.md)) importam mais na luta contra os piratas, que dura minutos.
- **Espaço para se mover.** Fique fora do alcance de uma arma que você supera em alcance e não pare de se mover diante de um foguete.

## Como o abate de um chefe paga {#how-a-boss-kill-pays}

Um alienígena comum paga o piloto que o acertou primeiro ([Combate](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). O líder de um enxame, e cada Dormant Pulse, pagam em vez disso **pelo dano causado**:

- **O pagamento é dividido pelo dano.** Todo piloto que causou pelo menos a parte indicada nas regras acima é pago, em proporção ao dano causado: os créditos, o Thulium, a XP e a honra do abate são divididos entre eles. Um piloto abaixo dessa parte não recebe nada.
- **A caixa de carga vai para o piloto que mais causou dano.** Ela é desse piloto (e do clã dele) por 30 segundos, como com qualquer alienígena, e depois qualquer um pode pegá-la ([Carga](/wiki/03-Mechanics/Cargo.md)). Cada nave Dormant tem a sua própria contagem de dano e a sua própria caixa.
- **Os seguidores pagam como de costume**: os Pirate Scouts e os Seeker Slaves pagam o piloto que os acertou primeiro, e o pagamento deles é pequeno perto do de um chefe.
- **O pagamento de um chefe é feito para superar os alienígenas ao redor.** Um minuto de luta contra um Pirate Boss paga mais do que um minuto de luta contra um Goombah, e o enxame Dormant paga ainda mais; o Boss Seeker paga exatamente dez Seekers.

Todo abate é contado com o nome próprio da nave nas suas estatísticas de abates e soma pontos PvE ao seu ranking:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Nave de enxame | Enxame | Pontos PvE por abate |
| :--- | :--- | ---: |
| **Pirate Boss** | Enxame Pirate | 15 |
| **Pirate Scout** | Enxame Pirate | 4 |
| **Dormant Force** | Enxame Dormant | 25 |
| **Dormant Pulse** | Enxame Dormant | 11 |
| **Boss Seeker** | Enxame Seeker | 5 |
| **Seeker Slave** | Enxame Seeker | 1 |

<!-- swarms-points:end -->

O abate de uma nave de enxame não conta como abate de nenhum outro alienígena: um Boss Seeker ou um Seeker Slave não é um Seeker para uma missão que pede Seekers, e os marcos dos pontos de reset ([Linha do tempo do reset](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) são só os dos cinco alienígenas. As missões que pedem naves de enxame estão listadas em [Missões de enxame](/wiki/03-Mechanics/Quests.md#swarm-missions).
