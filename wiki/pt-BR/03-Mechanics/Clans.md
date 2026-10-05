<!-- wiki-i18n source: b98e7995bde4597b -->
<!-- wiki-i18n title: Clãs -->
# Clãs {#clans}

Fundar um clã ou entrar em um permite reunir recursos, melhorar o banco compartilhado, definir taxas de imposto, coordenar-se com os membros da sua facção e gerenciar a diplomacia. Um clã também tem trabalho a fazer em conjunto: todo dia ele recebe uma **linha diária** de missões que termina com um chefe que só o clã pode ferir, e os pontos que ele ganha compram **bônus permanentes** para todos os membros. (Na página Clã do jogo, um clã se chama *frota*; seus pontos e bônus aparecem lá como pontos da frota e bônus da frota.)

**Em um minuto**

- A cada dia de temporada, seu clã recebe uma [linha diária](#daily-line): quatro missões feitas em ordem (abater alienígenas, voar uma distância, em alguns dias derrubar chefes de enxame) e depois um [Guardião do clã](#clan-wardens), um chefe que você invoca e que só o seu clã pode ferir.
- Cada etapa concluída paga pontos do clã na hora: 15, 15, 20, 20 e 30, ou seja, **100 pontos** por uma linha inteira.
- O Líder e os Vice-líderes gastam os pontos em três [bônus](#clan-points-and-boosts) de dez níveis cada: **Dano** (até +5%), **Thulium** (até +10%) e **Créditos** (até +10%).
- Um clã que conclui todas as linhas comprou todos os níveis no **dia 12 da temporada**. Os pontos e os níveis recomeçam a cada reset.
- É preciso ter pelo menos **três membros** que tenham feito a sua parte e cerca de cinco pilotos para a luta contra o Guardião.
- A linha e os bônus exigem um jogo da versão 0.4.10 ou mais recente.

![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Progressão do clã {#clan-progression}

Os clãs começam no nível 1 e podem ser melhorados até o nível 5. Melhorar o clã exige créditos pagos com o **Banco do clã**. As melhorias aumentam a capacidade de membros e os limites diários de pagamento.

| Nível do clã | Limite de membros | Limite diário de pagamentos (por membro) | Custo da melhoria (créditos) |
| :---: | :---: | :---: | :--- |
| **Nível 1** | 10 | 1.000.000 Cr | — |
| **Nível 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Nível 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Nível 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Nível 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Economia e impostos do clã {#clan-economy-taxation}

Os clãs funcionam com um sistema financeiro baseado em impostos:

### 1. Imposto diário {#1-daily-taxation}

- **Taxa de imposto**: o Líder ou os Vice-líderes podem definir uma taxa de imposto diária entre **0% e 5%**.
- **Cobrança automática**: uma vez por dia (UTC), o servidor cobra automaticamente o imposto de todos os membros do clã.
- **Fórmula**: o imposto é calculado como `ClanTaxRate` do saldo de créditos atual de cada membro.
  - *Exemplo*: se você tem 10.000.000 de créditos e o imposto do clã é 2%, 200.000 créditos serão descontados da sua conta e depositados no Banco do clã.
  - Também é possível fazer doações voluntárias de créditos, até o limite descrito na próxima seção.

### 2. Doações {#2-donations}

- **Doar**: qualquer membro pode enviar créditos ao Banco do clã pela página Clã. A janela mostra quanto você ainda pode enviar.
- **Limite de doações**: um piloto pode enviar no máximo **1.000.000 de créditos a clãs em qualquer período de 24 horas**, somando todos os clãs em que o piloto já esteve. Sair de um clã e entrar em outro não dá um novo limite.
- **Sem reinício diário**: as 24 horas são deslizantes. Cada doação deixa de contar exatamente 24 horas depois de feita, e a janela informa quando a mais antiga deixa de contar e quanto volta a ficar disponível. Uma doação acima do que resta é recusada por inteiro.
- O imposto diário não é uma doação e não consome o seu limite.

### 3. Pagamentos do banco {#3-bank-payouts}

- **Limites de pagamento**: os líderes e oficiais do clã podem distribuir créditos do Banco do clã a membros individuais.
- **Limite diário**: um membro não pode receber mais de `1,000,000 * ClanLevel` créditos em pagamentos em um único dia civil (UTC).

---

## Hierarquia e funções {#hierarchy-roles}

Os clãs usam uma estrutura de patentes baseada em funções para gerenciar as permissões:

- **Líder (função 3)**: tem acesso administrativo completo, incluindo melhorar o clã, definir impostos, diplomacia, promoções, expulsões e dissolver o clã.
- **Vice-líder (função 2)**: pode definir taxas de imposto, pagar créditos, gerenciar a diplomacia e promover ou rebaixar patentes inferiores.
- **Ancião (função 1)**: membro de confiança que pode aceitar novas candidaturas ao clã.
- **Membro (função 0)**: jogador comum, sem permissões administrativas.

### Tabela de permissões {#permissions-table}

| Ação | Líder | Vice-líder | Ancião | Membro |
| :--- | :---: | :---: | :---: | :---: |
| **Dissolver o clã** | ✅ | ❌ | ❌ | ❌ |
| **Melhorar o clã** | ✅ | ❌ | ❌ | ❌ |
| **Definir a taxa de imposto** | ✅ | ✅ | ❌ | ❌ |
| **Pagar créditos** | ✅ | ✅ | ❌ | ❌ |
| **Gerenciar a diplomacia** | ✅ | ✅ | ❌ | ❌ |
| **Comprar bônus do clã** | ✅ | ✅ | ❌ | ❌ |
| **Invocar o Guardião do clã** | ✅ | ✅ | ❌ | ❌ |
| **Promover / Expulsar** | ✅ | ✅* | ❌ | ❌ |
| **Aceitar candidaturas** | ✅ | ✅ | ✅ | ❌ |

*\*Os Vice-líderes só podem promover, rebaixar ou expulsar membros de patente inferior à sua.*

### Quando o Líder sai {#when-the-leader-leaves}

Um Líder não pode sair de um clã que ainda tem outros membros: primeiro promova um Vice-líder a Líder (o Líder passa a Vice-líder) ou saia por último, o que dissolve o clã. Se o Líder excluir a conta (Configurações › Conta), a liderança passa ao membro de patente mais alta e, em caso de empate, ao mais antigo no clã; um Líder sozinho no clã o dissolve, junto com o banco.

---

## Linha diária {#daily-line}

Todo clã recebe uma **linha diária** por dia: cinco etapas, feitas **em ordem**, pelo clã inteiro junto. As quatro primeiras são missões: abater tantos alienígenas, voar tanta distância ou, em alguns dias, derrubar chefes de enxame. A quinta é um **Guardião do clã**, um chefe que você invoca e destrói. Abra **Comunidade › Clã** e a aba **Operações** para ver a linha de hoje, a etapa aberta com a sua barra, a sua parte e o tempo que falta.

### As cinco etapas {#the-five-steps}

| Etapa | O quê | Pontos do clã |
| :---: | :--- | ---: |
| 1 | Primeira missão | 15 |
| 2 | Segunda missão | 15 |
| 3 | Terceira missão | 20 |
| 4 | Quarta missão | 20 |
| 5 | O Guardião do clã do dia | 30 |
| | **Uma linha concluída** | **100** |

- Só conta a **etapa aberta**. Um abate feito enquanto a etapa 1 está aberta conta para a etapa 1 e para mais nada. Quando a etapa 1 termina, a etapa 2 abre do zero. O que você abate além da meta de uma etapa não é guardado para a seguinte.
- Uma etapa paga os seus pontos **no momento em que termina**. Um clã que conclui as quatro missões e depois não consegue reunir uma tripulação para o Guardião ainda fica com **70 pontos**.
- O trabalho de todos vai para **uma contagem compartilhada**: os abates do alienígena da etapa aberta e a distância voada por todos os seus membros se somam, então ninguém precisa fazer uma etapa sozinho.

### O dia {#the-day}

- O dia de um clã é um **dia de temporada**: 24 horas contadas a partir do início da temporada ([Linha do tempo do reset](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). Uma linha nova começa à mesma hora todo dia, que não é meia-noite UTC (o imposto diário do clã continua sendo cobrado à meia-noite UTC). A aba Operações faz a contagem regressiva até a virada.
- Uma linha que não é concluída **expira** quando o dia acaba. As etapas já feitas mantêm os seus pontos, o progresso da etapa aberta se perde e não dá para compensar depois. As linhas rodam nos dias de temporada 1 a 29.
- Os pilotos do clã que estão online recebem uma linha do Sistema quando a linha nova começa, quando uma etapa termina e **uma hora antes da virada** se a linha não estiver concluída.

### Níveis de dificuldade {#difficulty-tiers}

Todo dia o jogo pega o **nível médio dos cinco pilotos de maior nível** do clã (todos, se tiver menos de cinco) e define com ele a categoria do dia:

| Categoria | Nível médio | Guardião |
| :--- | :--- | :---: |
| Recruta | menos de 4 | I |
| Veterano | de 4 a menos de 7 | II |
| Elite | 7 ou mais | III |

A categoria decide quantos alienígenas as missões pedem, qual alienígena a etapa «pesada» pede e quão forte é o Guardião. **Os pontos são os mesmos em todas as categorias.** Pilotos novos de nível baixo não puxam a categoria para baixo: só contam os cinco melhores.

### Quem conta {#who-counts}

- **O total do clã conta.** As barras da aba Operações são as do clã inteiro.
- **O seu mínimo.** Para dividir a recompensa do dia, você precisa fazer **5% do trabalho do dia**, uns oito minutos de caça de verdade. A aba mostra isso como «Seu trabalho de hoje: 312 de 469 unidades». Uma unidade de trabalho é um segundo de jogo: um abate conta o tempo que leva para achar e destruir aquele alienígena, e um trecho de voo o tempo que leva para voar. Para um clã Veterano, um Seeker vale cerca de 12 unidades, um Phantasm 22, um Bulwark 123 e 1.000 unidades voadas cerca de 5; o mínimo é de 446 a 480 unidades, qualquer que seja o dia e a categoria.
- **Pelo menos três membros** precisam ter atingido o mínimo antes que uma etapa possa terminar. Se uma etapa está cheia e menos membros chegaram lá, ela **espera** («A etapa 3 está cheia, mas só 2 membros atingiram o mínimo»), e os abates do alienígena dessa etapa continuam somando ao trabalho dos membros que os fizeram até o terceiro chegar. Um clã com menos de três pilotos não consegue concluir nenhuma etapa.
- **Quem fica com um abate.** O piloto que recebe o pagamento pelo abate e os colegas de grupo dele a até 4.000 unidades que atiraram nos últimos 15 segundos ([Grupos](/wiki/03-Mechanics/Groups.md#sharing-kills)). Um clã conta um abate **uma só vez**, não importa quantos pilotos dele estivessem no grupo, e o trabalho do abate é dividido igualmente entre eles. Dois clãs em um grupo contam uma vez cada.
- **Quais abates.** Só o alienígena da etapa aberta: o Seeker, Phantasm, Bulwark ou Goombah comum. Naves de enxame, outros pilotos e os ajudantes de um Guardião não contam como esses alienígenas. Qualquer mundo conta, e um abate vale mais em um mundo mais forte: **1 em Alpha, 1,5 em Beta, 2 em Gamma** ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Uma etapa de chefes conta os chefes dos [enxames](/wiki/05-Swarms/Swarms.md), um para cada clã que tenha um piloto que causou pelo menos 5% do dano.
- **Voar.** Uma etapa de patrulha conta a distância que cada piloto voa fora das zonas seguras; cinco pilotos voando juntos somam cinco vezes a distância.
- **Entrar e sair.** O que você fez continua contando se você sair. Um piloto que entra conta a partir desse momento.

### As sete linhas {#the-seven-lines}

As linhas seguem um ciclo de sete: a linha do dia de temporada *d* é a de número 1 + ((*d* − 1) mod 7), então cada uma volta a cada sete dias. Os números são para um clã **Recruta / Veterano / Elite**. As duas linhas **Swarm Break** pedem chefes de enxame e só vêm a partir do dia 4, quando os [enxames](/wiki/05-Swarms/Swarms.md) aparecem. Todos os números são feitos para cerca de **2,6 horas de jogo no total**, meia hora cada um com cinco pilotos (uma estimativa, não uma medição).

| Linha | Dias de temporada | Etapa 1 | Etapa 2 | Etapa 3 | Etapa 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115.000 / 155.000 / 185.000 unidades | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175.000 / 230.000 / 275.000 unidades | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290.000 / 385.000 / 460.000 unidades | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175.000 / 230.000 / 275.000 unidades | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350.000 / 460.000 / 550.000 unidades |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230.000 / 305.000 / 365.000 unidades |

### A sua recompensa {#the-reward-for-you}

Quando a linha é concluída, cada membro que atingiu o mínimo e ainda está no clã recebe um pagamento, mesmo que esteja offline. O pagamento é fixo: bônus, boosters e o mundo não o alteram.

| Categoria | Créditos | Thulium |
| :--- | ---: | ---: |
| Recruta | 5.000 | 20 |
| Veterano | 15.000 | 60 |
| Elite | 22.000 | 90 |

---

## Guardiões do clã {#clan-wardens}

Um **Guardião do clã** é o chefe do fim da linha diária. Ele não é um dos [enxames](/wiki/05-Swarms/Swarms.md) públicos que vagam por um setor: o seu clã **o invoca** e **só o seu clã pode feri-lo**. Três Guardiões se revezam, um por dia: dia 1 **Brood**, dia 2 **Siege**, dia 3 **Wrath**, dia 4 Brood de novo, e assim por diante (o dia 15 é um dia de Wrath). Cada um vem em três forças, **I, II e III**, definidas pela categoria do clã. Um Guardião é um alienígena de um tipo próprio, como as naves de um enxame: ele não conta como Seeker, Phantasm nem qualquer outro alienígena.

| Guardião | Dias de temporada | Papel | Como luta |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Guardião da colmeia: divida seu fogo | Quatro pequenos **Brood Drones** curam o casco dele, e chega um novo a cada 8 segundos enquanto menos de quatro estiverem vivos. Atire primeiro nos drones, depois no Guardião. |
| **Siege Warden** | 2, 5, 8, 11 … | Quebra-cercos: não pare de se mover | Ele vagueia e dispara um [foguete Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) reto no primeiro piloto que o acertou, e se conserta sozinho. Dois **Siege Escorts** acrescentam fogo de laser. Não pare de se mover e revezem-se como alvo. |
| **Wrath Warden** | 3, 6, 9, 12 … | Senhor da guerra: vença a fúria | Ele luta parado e se conserta sozinho. Com menos da metade do casco, seus lasers acertam **uma vez e meia mais forte**. Dois **Wrath Guards** acrescentam fogo de laser. Derrube-o rápido e mantenha os escudos de pé. |

### Invocar um Guardião {#calling-a-warden}

- **Quando.** Depois que a etapa 4 termina. Um clã tem **duas invocações por dia**, só um Guardião fora por vez, e o dia precisa ter **pelo menos 30 minutos** restantes.
- **Quem.** O Líder ou um Vice-líder.
- **Como.** Em voo: o botão **Invocar aqui** aparece na tela de voo assim que a etapa 4 termina e pede a sua confirmação. Fique fora das zonas seguras, em um setor de corporação **x-2, x-3 ou x-4** (de qualquer corporação) do seu mundo. A aba Operações mostra o Guardião do dia, as invocações restantes e por que o botão está esmaecido, mas um Guardião é invocado a partir da nave.
- **Onde ele aparece.** De 3.000 a 4.500 unidades da sua nave, no seu mundo: só os pilotos desse mundo conseguem chegar até ele. A aba recomenda **x-2 para um clã Recruta, x-3 para Veterano e x-4 para Elite**. As [regras de PvP](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) de sempre do setor escolhido continuam valendo.
- **Aquecimento.** Ele fica **90 segundos** blindado e passivo («carregando») e todo piloto do clã que está online é avisado de onde. Voe até lá enquanto ele carrega: passados os 90 segundos, ele está ativo.
- **Só o seu clã.** Os tiros de pilotos de qualquer outro clã são ignorados e não o fazem reagir.
- **Como termina.** Quando ele é destruído. Ele **se retira** 40 minutos depois de ativado, quando o dia acaba, quando nenhum piloto do seu clã está em voo no mapa dele há 2 minutos ou quando o servidor reinicia (essa invocação é devolvida). Um Guardião que se retira custa uma invocação, e a chamada seguinte é o mesmo Guardião com força total.

### Lutar contra um Guardião {#fighting-a-warden}

- **Um Guardião luta contra o primeiro piloto que o acertou**, como qualquer chefe: deixe a nave mais resistente da tripulação começar e use [Shield Surge e Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Leve munição x2** ([Lasers](/wiki/06-Items/Lasers.md#laser-ammunition)). Uma tripulação de cinco vence até com munição x1, mais devagar; uma de três, não.
- **Brood:** os drones curam o casco dele, e uma tripulação de três que os ignora perde. Atire neles primeiro: um morre em um segundo ou menos sob o fogo de cinco pilotos, e o seguinte chega depois de 8 segundos.
- **Siege:** os foguetes dele são retos e sem guia, então uma nave que não para de se mover desvia da maioria. Não pare de se mover e revezem-se como alvo.
- **Wrath:** quando o casco dele cai abaixo da metade, cada rajada acerta uma vez e meia mais forte, então a segunda metade da luta é a perigosa. Derrube a primeira metade rápido, mantenha os escudos de pé e guarde o Emergency Repair para a fúria.

### Que tripulação é preciso {#how-big-a-crew}

> [!NOTE]
> Estes tempos são **calculados** a partir dos números abaixo, não medidos no jogo: uma tripulação nas naves e no equipamento para os quais a categoria foi feita, todos atirando no Guardião. Um traço significa que não calculamos.

| Tripulação | Com munição x2 | Com munição x1 |
| :--- | :--- | :--- |
| 2 pilotos | perdem para Brood e Siege; vencem Wrath em cerca de 17 minutos | – |
| 3 pilotos | vencem em 9 a 10 minutos, por pouco: o casco do tanque termina baixo e um piloto pode cair | perdem |
| 5 pilotos | vencem em cerca de 5 minutos | vencem em 12 a 14 minutos |
| 7 pilotos | vencem em cerca de 3,4 minutos | – |
| 10 pilotos | vencem em cerca de 2,3 minutos | – |

Uma tripulação de categoria inferior à do Guardião perde: uma tripulação Recruta de cinco não consegue matar um Guardião Veterano, nem uma Veterana um Guardião Elite. O Guardião do **seu** clã sempre combina com a **sua** categoria.

### Os números dos Guardiões {#warden-numbers}

Os Guardiões têm os mesmos números em todos os mundos (os de Alpha), e o pagamento deles também. Cada drone, escolta ou guarda tem os números da segunda tabela e fica junto do Guardião: um Brood Drone cura o casco do Guardião, um Siege Escort ou um Wrath Guard atira com lasers.

| Guardião | Casco | Escudo | Dano dos lasers (uma salva por segundo) | Velocidade | Alcance dos lasers | Se conserta sozinho (casco por segundo) | Foguete e segundos entre os tiros |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166.000 | 136.000 | 43 | 90 | 600 | – | – |
| Brood Warden II | 288.000 | 236.000 | 259 | 90 | 700 | – | – |
| Brood Warden III | 1.060.000 | 870.000 | 1.030 | 90 | 800 | – | – |
| Siege Warden I | 143.000 | 117.000 | 16 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248.000 | 203.000 | 97 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915.000 | 745.000 | 615 | 110 | 800 | 1.385 | Rivet III: 8 |
| Wrath Warden I | 163.000 | 133.000 | 32 | 90 | 700 | 215 | – |
| Wrath Warden II | 282.000 | 231.000 | 194 | 90 | 800 | 375 | – |
| Wrath Warden III | 1.040.000 | 850.000 | 820 | 90 | 900 | 1.385 | – |

| Ajudante | Quantos | Casco | Escudo | Dano dos lasers (uma salva por segundo) | Velocidade | Cura o Guardião (casco por segundo) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 4 | 170 | 120 |
| Brood Drone II | 4 | 1.200 | 900 | 26 | 170 | 210 |
| Brood Drone III | 4 | 4.000 | 3.500 | 105 | 170 | 770 |
| Siege Escort I | 2 | 4.300 | 3.500 | 2 | 175 | – |
| Siege Escort II | 2 | 7.400 | 6.100 | 15 | 175 | – |
| Siege Escort III | 2 | 27.500 | 22.500 | 95 | 175 | – |
| Wrath Guard I | 2 | 4.900 | 4.000 | 6 | 180 | – |
| Wrath Guard II | 2 | 8.500 | 6.900 | 39 | 180 | – |
| Wrath Guard III | 2 | 31.000 | 25.500 | 165 | 180 | – |

### Pagamento e saque {#warden-pay-and-loot}

Um Guardião paga o mesmo que uma pilha do alienígena pesado da categoria: **30 Phantasms** para um Guardião I, **24 Bulwarks** para um II e **16 Goombahs** para um III. É um bolo só, dividido por dano entre os pilotos que causaram pelo menos 5% do dano, do mesmo jeito que com o líder de um [enxame](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Seus [bônus do clã](#what-the-boosts-apply-to) valem para a sua parte. Pela nossa conta, os créditos cobrem a munição x1 que uma tripulação de cinco queima, e a munição x2 custa mais Thulium do que o Guardião paga: é uma luta pelos pontos e pela caixa.

| Força do Guardião | Créditos | Thulium | Experiência (XP) | Honra |
| :--- | ---: | ---: | ---: | ---: |
| I | 90.000 | 360 | 9.000 | 180 |
| II | 120.000 | 600 | 19.200 | 240 |
| III | 240.000 | 1.200 | 48.000 | 384 |

O Guardião solta **uma caixa** para o piloto que causou mais dano; ela é dele e do clã dele por 30 segundos ([Carga](/wiki/03-Mechanics/Cargo.md)). Uma chance entre parênteses vale para cada uma das rolagens indicadas: (5 × 50%) são cinco rolagens com 50% de chance cada.

| Guardião | Item | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50%) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50%) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60%) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1.200 |
| Siege Warden | Foguete comprado com créditos (um tipo, aleatório) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30%) | – |
| Siege Warden | Foguete épico (um tipo, aleatório) | – | – | 1–2 (50%) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25%) | 1 (50%) | 1–2 (70%) |
| Wrath Warden | Power Core | – | 1 (15%) | 1 (35%) |
| Wrath Warden | Quorvium | – | – | 5–10 (70%) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8%) |

Um Guardião conta com o próprio nome nas suas estatísticas de abates e soma pontos PvE à sua [patente](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **10, 15 ou 25** pelo líder de um Guardião I, II ou III, e 1 por cada ajudante.

---

## Pontos e bônus do clã {#clan-points-and-boosts}

Os pontos do clã pertencem ao clã. Cada etapa que o clã conclui soma ao seu saldo. O **Líder e os Vice-líderes** o gastam no cartão **Bônus da frota** da aba Operações: três bônus de dez níveis cada, e todos os membros os recebem na hora. Uma compra é definitiva: não há reembolso nem redistribuição.

### Os três bônus {#the-three-boosts}

| Bônus | Níveis | Por nível | Nível máximo | Vale para |
| :--- | :---: | :---: | :---: | :--- |
| **Dano da frota** | 10 | +0,5% | +5% | Dano de laser em alienígenas e pilotos |
| **Thulium da frota** | 10 | +1% | +10% | Thulium de abates e recompensas de missões |
| **Créditos da frota** | 10 | +1% | +10% | Créditos de abates e recompensas de missões |

### Preços {#boost-prices}

O preço de um nível é **22 pontos do clã mais 4 por cada nível anterior**, e é o mesmo para os três bônus: 400 pontos por um bônus, **1.200 pelos três**, o que dá doze linhas concluídas.

| Nível | Preço | Total para este bônus | Dano da frota | Thulium da frota | Créditos da frota |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5% | +1% | +1% |
| 2 | 26 | 48 | +1% | +2% | +2% |
| 3 | 30 | 78 | +1,5% | +3% | +3% |
| 4 | 34 | 112 | +2% | +4% | +4% |
| 5 | 38 | 150 | +2,5% | +5% | +5% |
| 6 | 42 | 192 | +3% | +6% | +6% |
| 7 | 46 | 238 | +3,5% | +7% | +7% |
| 8 | 50 | 288 | +4% | +8% | +8% |
| 9 | 54 | 342 | +4,5% | +9% | +9% |
| 10 | 58 | 400 | +5% | +10% | +10% |

### Em que os bônus valem {#what-the-boosts-apply-to}

- **Dano da frota** soma a todo o dano de laser que a sua nave causa: em alienígenas, naves de enxame, Guardiões e outros pilotos. Ele **não vale para foguetes**, de nenhum tipo.
- **Thulium da frota e Créditos da frota** somam ao pagamento dos abates de alienígenas (os seus, a sua parte de um chefe e a sua parte de um abate em grupo) e à recompensa de cada missão que você resgata, de nível, da estação ou Desafio ([Missões](/wiki/03-Mechanics/Quests.md#rewards)). Eles **não valem para** as fazendas do [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm), os pagamentos do banco, os códigos de bônus nem a recompensa da linha diária.
- **Eles se somam aos seus outros bônus** (boosters como o Damage Amp, os bônus da [loja de bônus permanentes](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): as porcentagens se somam. Os amplificadores de laser (Amps) não estão entre eles: somam dano fixo, e as porcentagens valem para o total. Cinco pontos de Dano da frota ao lado de 50 de outras fontes dão 55, que é 3,3% mais dano do que antes.
- **Uma fração não se perde.** Um bônus muitas vezes soma menos de uma unidade a um abate: 10% dos 4 Thulium de um Seeker são 0,4. O jogo guarda a fração e a paga junto com as unidades dos seus próximos abates, de modo que dez Seekers pagam os 4 que lhe são devidos. A fração que você tem na mão se perde quando você sai do jogo.
- **Entrar e sair.** Um piloto tem os bônus a partir do momento em que entra no clã e os perde no momento em que sai, é expulso ou o clã é dissolvido. O clã mantém os seus níveis.

### Quanto tempo leva {#how-long-it-takes}

Um clã que conclui todas as linhas ganha 100 pontos por dia. Se os oficiais compram igualmente nos três bônus, ele tem **4 níveis depois da primeira linha, 10 depois da terceira, 16 depois da quinta e todos os 30 no dia de temporada 12**. Quatorze linhas já acabaram quando o dia 15 começa, então um clã assim tem duas linhas de folga. Um dia que não é concluído ainda paga as etapas feitas. Depois do último nível, a linha continua rodando e continua pagando a sua recompensa; os pontos continuam somando ao que o clã ganhou nesta temporada, o que a dica dos pontos do clã no cartão Bônus da frota mostra.

### Pontos e o reset {#clan-points-and-the-wipe}

A cada reset, os **pontos, os níveis dos bônus e as linhas do clã recomeçam do zero**, então cada temporada é uma nova corrida pelos bônus completos. O clã em si, os seus membros, o seu banco e o seu imposto ficam como estão.

---

## Diplomacia {#diplomacy}

Os clãs podem estabelecer relações diplomáticas formais com outras organizações informando a tag do clã-alvo:

- **Aliança**: clãs formalmente aliados. O status amistoso aparece no mapa.
- **NAP (Pacto de não agressão)**: acordo para não entrar em hostilidades.
- **Guerra**: declaração formal de guerra. Alvos de guerra podem ser atacados em qualquer lugar, sem penalidade.

---

## Convidando um amigo {#bringing-a-friend}

Um amigo que é novo no jogo pode entrar com o seu código de convite pessoal e recebe um pacote inicial; veja [Convidar amigos](/wiki/03-Mechanics/Invite-Friends.md). Já dentro do jogo, ele pode se candidatar ao seu clã como qualquer piloto.
