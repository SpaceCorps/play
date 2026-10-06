<!-- wiki-i18n source: 7ed6ed3056da695a -->
<!-- wiki-i18n title: Drones -->
# Mecânica dos drones {#drone-mechanics}

Os drones são unidades de apoio autônomas que voam ao lado da sua nave. Eles oferecem slots de equipamento adicionais e contribuem diretamente para o desempenho de combate da sua nave. Um Slave Drone também cresce: ele ganha experiência toda vez que você destrói um alienígena e sobe por **oito níveis**, de uma pequena esfera blindada a uma canhoneira de asas em crescente. Na Montagem, um Slave Drone pode ser melhorado para **Master Drone**, que recomeça os níveis (veja Master Drone abaixo). Os drones também permitem que você use uma **formação de drones**: ela só funciona se você tiver pelo menos um drone na sua frota (veja [Formações de drones](/wiki/03-Mechanics/Formations.md)).

![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)

## Como obter drones {#getting-drones}

Cada drone que você possui, um **Slave Drone** ou um Master Drone, abre os seus slots de drone (um para um Slave Drone, dois para um Master Drone), até **8** drones. A Loja vende Slave Drones por créditos e, a partir do quarto, também por Thulium. Cada um custa mais do que o anterior: os preços estão em [Drones](/wiki/06-Items/Drones.md).

## Disposição de voo e movimento {#formation-movement}

Sem uma [formação de drones](/wiki/03-Mechanics/Formations.md) em uso, seus drones voam na **disposição “Wingman” (2-2-4)** padrão, a disposição **Padrão**:

- **2 drones** ao lado da nave, um em cada flanco.
- **2 drones** ao lado e um pouco atrás dela.
- **4 drones** seguindo atrás.

Eles usam um algoritmo de seguimento suave que ajusta a posição deles conforme a velocidade e a rotação da sua nave, fechando a disposição em manobras bruscas. Nesta disposição ninguém voa à sua frente.

Os drones são pequenos e ficam por perto: um drone de nível 8 tem cerca de 19,5 unidades de largura (uma Protos tem 50) e um drone de nível 1 é uma bola de cerca de 8, de modo que a disposição inteira cabe em cerca de 135 unidades de cada lado da sua nave e atrás dela. O drone que você comprou primeiro tem mais experiência e voa nesta disposição no seu flanco esquerdo, o segundo no direito, e os mais novos seguem atrás.

Use uma [formação de drones](/wiki/03-Mechanics/Formations.md) e os drones saem dessa disposição: **cada uma das 16 formações tem uma forma própria**, um telhado sobre as asas, um losango, um coração, asas, uma espada, uma broca e mais, e os drones deslizam até ela em menos de um segundo. A forma é feita para os drones que você tem, até 8, e gira junto com a sua nave. Outros pilotos também a veem. [Como voam](/wiki/03-Mechanics/Formations.md#how-they-fly) mostra as dezesseis. Use **Padrão**, a entrada da lista de Formações que não é formação nenhuma, e os drones voltam a voar na disposição “Wingman”.

Você pode desligar os drones em Configurações › Interface: **Mostrar meus drones** para os seus e **Mostrar drones inimigos** para os de outros pilotos.

## Equipamento e atributos {#equipment-stats}

Os drones funcionam como suportes de equipamento que ampliam a sua nave.

- Um Slave Drone tem **1 slot** e um Master Drone **2**, até **8 drones**.
- Você pode equipar **lasers** e **escudos** nesses slots, em qualquer um dos dois slots de um Master Drone. Mais nada cabe: nem motores, nem núcleos adaptativos.
- **Os lasers contam por inteiro.** Um laser em um drone dispara quando você dispara, soma o dano dele à sua rajada e gasta munição como qualquer outro laser (cada laser queima uma unidade de munição por rajada). Os dois lasers de um Master Drone são dois lasers.
- **Os escudos também contam por inteiro.** Um escudo em um drone conta como um em um slot de núcleo, em qualquer um dos dois slots: a capacidade e a recarga dele, com as células de escudo encaixadas, a absorção dele na média da sua nave, o bônus de escudo e a penalidade de velocidade. Ele é ordenado junto com os escudos da própria nave pelo que conta depois da parcela do slot (o slot de um drone conta 100%; os quatro melhores contam por inteiro, o quinto e os seguintes valem menos, veja [Mecânica dos escudos](/wiki/03-Mechanics/Shields.md)), e os bônus da Forja, os bônus da Loja de PR e a penetração de escudo de quem ataca agem sobre ele como sobre qualquer escudo. O nível do drone aumenta só o laser dele, nunca o escudo. Enquanto um drone está sendo melhorado, os slots dele ficam desligados, tanto o escudo quanto o laser. Antes da versão 0.4.7, um escudo em um drone não somava nada.
- **Um laser ou um escudo?** Um slot guarda um ou outro: um laser soma um laser à sua rajada, um escudo soma os pontos de escudo dele. Em uma nave pequena com bons escudos, os pontos extras somam pouco, porque o casco acaba primeiro; em um casco grande, eles permitem aguentar muito mais.
- **As formações precisam de um drone, não de um slot.** Uma [formação de drones](/wiki/03-Mechanics/Formations.md) funciona enquanto você tiver pelo menos um drone. Ela não ocupa nenhum slot de drone, e o número de drones, os níveis deles e o que carregam não a alteram.

## Níveis {#levels}

Todo Slave Drone começa no nível 1 e ganha experiência (XP) sempre que você destrói um alienígena. Um Master Drone também começa no nível 1, sem XP, e sobe de nível do mesmo jeito. Cada nível exige mais do que o anterior, e o visual muda junto, para você ver até onde um drone chegou. A tabela dá, para cada nível, o XP necessário para subir até ele a partir do nível anterior e quantos abates de um único tipo de alienígena isso equivale, sozinho (no mundo Alpha: o Beta precisa de cerca de metade disso, o Gamma de cerca de um terço):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Nível 1, Semente:** uma pequena esfera blindada com uma lente ciano.
- **Nível 2, Halo:** a esfera dentro de um anel flutuante.
- **Nível 3, Disco:** um disco plano sob uma cúpula de vidro.
- **Nível 4, Disco voador:** um disco voador com placas de blindagem e entradas de ar.
- **Nível 5, Canhoneira:** uma proa e dois canhões se juntam ao disco voador.
- **Nível 6, Brotos de asa:** canhões e lâminas de asa curtas sobre pilares.
- **Nível 7, Meias-asas:** lâminas de asa mais longas com pontas douradas.
- **Nível 8, Crescente:** a canhoneira completa: asas em crescente inteiras com faixas de luz ciano.

| Nível | XP para chegar | XP do nível | Dano do laser | Abates de Seeker | Abates de Bulwark | Abates de Goombah |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1% | 550 | 69 | 23 |
| 4 | 2.000 | 1.100 | +2% | 1.100 | 138 | 46 |
| 5 | 3.700 | 1.700 | +3% | 1.700 | 213 | 71 |
| 6 | 6.000 | 2.300 | +4% | 2.300 | 288 | 96 |
| 7 | 9.500 | 3.500 | +5% | 3.500 | 438 | 146 |
| 8 | 14.000 | 4.500 | +7% | 4.500 | 563 | 188 |

| Alienígena | XP por drone |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Como os drones ganham XP {#how-drones-earn-xp}

- **Todo drone que você possui ganha o mesmo XP** por cada abate de alienígena pelo qual você é pago: os 8 primeiros drones, tenham ou não um laser. Um drone que você compra depois começa no nível 1, sem XP, então os seus primeiros drones sempre têm o nível mais alto.
- **Alienígenas mais fortes valem mais.** O XP que um alienígena dá está na segunda tabela acima (o Crystalys vale 72 Seekers). Qualquer outro alienígena dá 1.
- **Os mundos pagam mais.** O Beta dobra o XP, o Gamma o triplica (os alienígenas de lá também têm mais vida). Boosters e Premium não o alteram.
- **Os abates contam quando pagam a você.** Um alienígena que você termina enquanto outro piloto detém a reivindicação dele não paga nada aos seus drones, assim como não paga nada a você. Abates de pilotos, missões e abates dos próprios pilotos de corporação não dão XP aos drones.
- **O nível 8 é o último.** O XP continua sendo contado depois dele.

### O que um nível dá {#what-a-level-gives}

O **laser encaixado no slot de um drone** causa mais dano base conforme o drone sobe de nível: nada nos níveis 1 e 2, depois +1% no nível 3, até **+7% no nível 8**. O bônus multiplica o dano do próprio laser (depois do encantamento dele); os amplificadores encaixados nele são somados por cima e não são multiplicados. O hangar mostra o nível de cada drone, a barra de XP dele e os abates que o próximo nível exige, e os números de dano já incluem o bônus. Quando um drone sobe de nível, o Registro do jogo avisa (“O drone 2 chegou ao nível 4.”) e o drone solta um anel de luz.

### Quanto tempo leva {#how-long-it-takes}

A curva foi ajustada para que um drone novo chegue ao nível 2 em cerca de uma hora de jogo normal (caçando Bulwarks e Goombahs) e ao nível 8 em aproximadamente 27 horas de jogo. Essas horas valem para um piloto que compra o primeiro drone por volta das missões do nível 7; com equipamento mais fraco, leva mais (até cerca de 4 horas para o nível 2 e 150 horas para o nível 8). Caçar um único tipo de alienígena é, no melhor dos casos, cerca de 50% mais rápido do que uma mistura normal. Os drones permanecem no reset da temporada com os seus níveis e a sua experiência, então essas horas são gastas uma só vez, ao longo de quantas temporadas forem necessárias: um piloto que joga meia hora por dia chega lá em umas duas temporadas.

### Master Drone

Um Slave Drone vira um **Master Drone** quando você o melhora na Montagem, depois de pesquisada a tecnologia do Master Drone ([Pesquisa](/wiki/03-Mechanics/Research.md)). A receita custa 40.000 Thulium e 100 Ship Fragments, leva 60 segundos e não consome um drone: **você escolhe qual Slave Drone** será melhorado (o seletor mostra o nível e o XP de cada um), e esse mesmo drone, com o seu número, o seu slot de drone e tudo o que está encaixado nele, vira um Master Drone quando a tarefa termina, com um segundo slot vazio. Nada vai para o seu inventário e não há nada para coletar: o Registro do jogo avisa quando termina, inclusive no caso de uma melhoria que terminou enquanto você estava fora.

**O nível e o XP dele voltam a 0 quando a melhoria termina.** Um Master Drone recomeça no nível 1, sem XP, e sobe de nível como um Slave Drone (a tabela acima); o bônus de laser do nível que ele tinha vai embora junto. A Montagem avisa isso antes de você começar e pede que você confirme, citando o drone, quando ele tem algum XP. A escolha padrão é o drone com menos XP.

Enquanto a melhoria está em andamento, o drone fica bloqueado: você não pode melhorá-lo de novo nem excluí-lo, e o slot dele fica **offline**, então o laser nele não dispara até a tarefa terminar (até lá, ele continua sendo um Slave Drone com um slot). Ela entra na fila atrás das suas outras tarefas, como qualquer criação.

Um Master Drone é um dos seus 8 drones: ele conta para o limite de drones e para o preço do próximo Slave Drone, de modo que melhorar não muda nenhum dos dois, e ele permanece no reset da temporada com o nível e o XP. Em voo, ele é a canhoneira completa em dourado. Um Master Drone tem **dois slots de equipamento** onde um Slave Drone tem um: cada um aceita um laser ou um escudo, e o bônus de nível vale para o laser em qualquer um deles. No mais, é um Slave Drone: os mesmos oito níveis e o mesmo bônus de laser. Os Master Drones que você fez antes de ele ter o segundo slot agora o têm, e o que carregavam continua onde estava. Os Master Drones criados antes de existirem as melhorias no próprio drone são itens comuns no seu inventário e não voam.

## Comportamento em combate {#combat-behavior}

- **Lasers**: os drones disparam os lasers equipados no seu alvo travado.
- **Dano**: os drones podem sofrer dano (se existir lógica de entidade própria; hoje eles compartilham em sua maioria os pontos de vida da nave, mas são visualmente distintos). _Nota: atualmente, os drones são extensões indestrutíveis da nave._
- **Repair Drones**: os itens Repair Drone (I a IV) são [extras](/wiki/06-Items/Extras.md#repair-drones), não drones da sua frota. Enquanto um repara o seu casco, pequenos drones de reparo saem da nave, giram em volta dela e a atingem com feixes, e os pilotos por perto os veem.
