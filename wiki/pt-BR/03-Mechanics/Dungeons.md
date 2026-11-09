<!-- wiki-i18n source: 9421722a69e53475 -->
<!-- wiki-i18n title: Masmorras -->
# Masmorras {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; masmorra; masmorras; portão; portões; senhor da guerra; labirinto; fase; zona de saque; carta; portal; portal do clã; booster; névoa; guardiões; sala inicial; sala trancada; apoio do enxame; zona do caos; alertas de portão do clã; masmorra do clã; alertas de masmorra do clã; três quartos; 75 por cento -->

Uma **masmorra** é um labirinto fechado com um **Senhor da guerra** no fim (antes da 0.5.2 o jogo a chamava de portão). Um vice-líder ou o líder de um [clã](/wiki/03-Mechanics/Clans.md) abre uma e a paga com o banco do clã, e os membros do clã voam juntos para dentro como um único [grupo](/wiki/03-Mechanics/Groups.md). Eles abrem caminho entre os alienígenas do labirinto, abrem zonas de saque para escolher uma carta em cada uma e derrubam o Senhor da guerra. Todo piloto que participou da luta é pago quando o Senhor da guerra cai, dentro dos limites mais abaixo. As masmorras ficam na aba **Masmorras** da página do clã.

Uma masmorra é uma luta só contra os alienígenas: ninguém pode atacar dentro dele um colega de clã nem qualquer outra pessoa. Os alienígenas não pagam nada. O pagamento é só do Senhor da guerra, então a única maneira de ser pago é estar na luta quando ele cai.

## Em resumo {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Abre**: A partir do dia 1 da temporada
- **Quem abre uma masmorra**: Um vice-líder ou o líder, que paga o preço com o banco do clã
- **Grupo**: De 4 a 10 membros do clã, em um só grupo
- **Masmorras por dia**: 3 por clã em um dia UTC, um aberto por vez
- **Masmorras ao mesmo tempo**: 6 em um mundo
- **Mapas**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirintos**: 8; uma é sorteada quando uma masmorra é aberta
- **Sala do chefe**: Abre quando 75% dos Crystalys e de seus Twins são destruídos, arredondado para cima
- **Reunião**: 10 min para reunir e iniciar. Uma masmorra que ninguém inicia se fecha, e o preço volta ao banco do clã
- **Limite de tempo**: Fase 1: 95 min, Fase 2: 130 min, Fase 3: 165 min a partir do início. Quando esgota, a masmorra falha e não paga nada
- **Vazio**: Uma masmorra sem ninguém dentro por 3 min falha
- **Depois que o Senhor da guerra cai**: A masmorra fica aberta por 2 min, para os pilotos que estão dentro
- **Voltar**: Um piloto que saiu ou foi destruído pode voltar a entrar voando 3 vezes, com 20 s entre elas

<!-- dungeons-glance:end -->

## Como é uma partida {#how-a-run-goes}

1. **Invocar.** Na aba Masmorras, um [vice-líder ou o líder](/wiki/03-Mechanics/Clans.md#hierarchy-roles) escolhe uma fase e aperta **Invocar**. O preço sai do [banco do clã](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), e a masmorra recebe um dos mapas listados acima. Uma masmorra que ninguém inicia se fecha, e o preço volta ao banco.
2. **Entrar.** Os membros do clã apertam **Entrar** na janela do Clã enquanto estão voando, saltam pelo portal do clã ou apertam **Entrar** no cartão de aviso (veja Entrar). Todos pousam na sala inicial, e os pilotos lá dentro formam o grupo da masmorra.
3. **Iniciar.** A sala inicial é uma sala pequena numa ponta do labirinto, e a porta dela fica fechada enquanto a masmorra se reúne. Não há alienígenas nela, então é seguro esperar ali. A masmorra **inicia sozinha** quando todos os pilotos que ela espera estão dentro e o grupo é grande o bastante. Ele espera os membros do clã que estão online, não ausentes e no grupo de um piloto que entrou, e inicia na hora quando o grupo está cheio. O piloto que abriu a masmorra, ou um oficial, pode apertar **Iniciar** para começar mais cedo com os pilotos que estiverem dentro, se forem o bastante. Um piloto que sai deixa de ser esperado. Quando a masmorra inicia, a porta se abre para sempre, e depois disso só podem voltar os pilotos que já estavam dentro.
4. **Abrir caminho pelo labirinto.** Você entra por uma ponta do labirinto e o Senhor da guerra espera na outra, numa sala trancada. O labirinto é escuro: você só vê o que o grupo explorou e o que está perto das naves dele. Os alienígenas dormem em bandos nos corredores, e um bando que acorda caça o grupo pelo labirinto.
5. **Abrir as zonas de saque.** Anéis no labirinto marcam as zonas. Segure uma e o grupo vota numa carta, que é paga junto com o pagamento do Senhor da guerra.
6. **Destrancar a sala do chefe.** Destrua três quartos dos Crystalys e de seus Twins do labirinto, e a porta da sala do Senhor da guerra se abre. Até lá, o Senhor da guerra não pode ser ferido. Os outros alienígenas ficam onde estão, e você também pode destruí-los.
7. **Derrotar o Senhor da guerra.** Quebre seu escudo e seu casco e responda às suas habilidades. Quando ele cai, a masmorra está concluída.
8. **Ser pago.** O pagamento vem no momento em que o Senhor da guerra cai. A masmorra continua aberta um pouco mais para os pilotos lá dentro e depois se fecha.

## Entrar {#entering}

Para entrar em uma masmorra você precisa de uma **nave em voo**, então decole primeiro e depois abra a janela do Clã, e de um [grupo](/wiki/03-Mechanics/Groups.md) com membros suficientes do clã. Você também precisa do **nível** que a fase pede, e não pode já estar dentro de outra masmorra. O grupo de uma masmorra tem um limite de tamanho: quando está cheio, ninguém mais entra.

Um vice-líder ou o líder abre uma masmorra, uma de cada vez para o clã, e só até o número de masmorras por dia. O banco do clã precisa ter o preço. Um clã só pode abrir uma fase depois de concluir a anterior.

Dentro de uma masmorra você não pode trocar de mundo, e a Jump CPU e a Base CPU não funcionam. O botão **Sair** da janela Masmorra do clã leva você para fora. Ele pede confirmação antes, a não ser que o Senhor da guerra já tenha caído: aí você sai na hora. Um piloto que saiu, ou que foi destruído, pode voltar algumas vezes, com uma curta espera entre elas.

### O portal do clã e o aviso {#the-clan-portal-and-the-call}

Quando uma masmorra é aberta, o clã ganha um **portal** para ela no mapa de origem de cada corporação (`M-1`, `T-1` e `G-1`), um pouco fora da zona segura da estação. Só os pilotos do clã o veem: para todos os outros ele não existe. Ele não tem zona segura própria. Voe até ele e salte como em qualquer outro portal, e ele leva você à masmorra com as regras de **Entrar**: uma nave em voo, um grupo com membros suficientes do clã, o nível da fase e vaga no grupo. Depois que a masmorra inicia, só os pilotos que já estavam dentro podem usá-lo. O portal some quando a masmorra termina.

Enquanto a masmorra do seu clã se reúne e você voa em outro lugar, um **aviso** chega a você: um cartão no alto da tela de voo, com um som. Ele diz quem abriu a masmorra, quantos pilotos estão dentro e por quanto tempo a masmorra fica aberta. O botão **Entrar** do cartão leva você para dentro, como **Entrar** na aba Masmorras, e quando você sai da masmorra sua nave volta para onde estava. Esse botão fica esmaecido enquanto o seu grupo é pequeno demais. **Agora não** esconde o cartão dessa masmorra. Se o seu grupo já está dentro e a masmorra espera por você, o cartão diz isso. O cartão chega aos pilotos do clã que estão voando (não aos que estão ancorados numa estação) e que têm o nível que a fase pede. Você pode desligar o cartão e o som dele em **Alertas de masmorra do clã**, em Configurações › Geral › Grupos.

### A janela Masmorra do clã {#the-clan-dungeon-window}

Dentro de uma masmorra a partida tem uma janela própria, **Masmorra do clã**. Ela mostra o tempo que passou e o que resta, quantos alienígenas voam e quantos foram destruídos, o que o grupo deve fazer agora (explorar o labirinto, segurar uma zona, achar o chefe, destruir três quartos dos Crystalys e de seus Twins, derrotar o Senhor da guerra), a barra de retenção enquanto você está numa zona, a habilidade do Senhor da guerra com a contagem regressiva e o botão **Sair**. É uma janela como as outras: arraste pela barra de título e feche com a luz vermelha no canto. Ela abre sozinha quando você entra numa masmorra, uma vez para cada masmorra: se você a fecha, ela fica fechada até a próxima masmorra. A barra de ferramentas tem um botão **Masmorra do clã** para ela enquanto você está numa masmorra. Com a janela fechada, uma habilidade do Senhor da guerra que está para começar ou em andamento aparece como uma faixa de uma linha com o nome e a contagem regressiva. Clique na faixa para abrir a janela de novo.

## As fases {#the-stages}

Uma masmorra tem uma fase, e a fase é a dificuldade dela. Uma fase mais alta tem alienígenas mais resistentes que batem mais forte, e paga mais. Os multiplicadores da tabela são os dos alienígenas. Dano quer dizer os lasers e foguetes deles. O Senhor da guerra não segue a tabela: ele tem números próprios para cada fase, mais abaixo. A tabela também diz quantos alienígenas uma fase envia em comparação com a primeira. O **preço** sai do banco do clã quando a masmorra é aberta.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Requisito | Casco e escudo dos alienígenas | Número de alienígenas | Dano dos alienígenas | Preço da masmorra (créditos, do banco do clã) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | A partir do nível 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | A partir do nível 7 | ×1,5 | ×1 | ×1,5 | 1.000.000 |
| **Fase 3** | A partir do nível 8 | ×2 | ×1 | ×2 | 2.000.000 |

<!-- dungeons-stages:end -->

## O labirinto {#the-maze}

Cada masmorra é um labirinto fechado num mapa próprio, um dos mapas da lista acima, e o labirinto é um de vários desenhos. O labirinto ocupa o mapa inteiro, de borda a borda: uma grade de salas e corredores com paredes sólidas. As naves não atravessam uma parede, e uma parede bloqueia os tiros, então é cobertura. Um meteoro cai de cima, e uma parede não o detém.

**Salas e portas.** A sala inicial, onde você pousa, e a sala do Senhor da guerra, na ponta oposta, têm cada uma uma porta. Uma porta fechada é uma parede para naves, tiros e alienígenas. A porta inicial abre quando a masmorra inicia. A do Senhor da guerra fica trancada até três quartos dos Crystalys e de seus Twins serem destruídos (veja [A sala trancada](#the-locked-room)). Entre as duas, o labirinto tem uma sala de saque para cada zona de saque.

**Névoa.** O labirinto é escuro. Em voo você vê as paredes e os alienígenas dele só onde o grupo esteve, e um trecho curto em volta de cada nave do grupo. Uma sala conta como explorada assim que um de vocês está nela. O minimapa é igual: uma carta do andar inteiro que se preenche conforme o grupo explora, com a entrada, a porta do Senhor da guerra, as zonas que vocês acharam e o Senhor da guerra depois de achado. Os pilotos do seu próprio grupo sempre aparecem.

## Os alienígenas {#the-aliens}

Quatro tipos de alienígenas guardam o labirinto. Eles dormem em bandos nos corredores, nunca numa sala, e um bando acorda quando um piloto se aproxima. Um bando acordado não espera por você: ele caça o grupo pelo labirinto, e um bando que perde todo mundo volta para onde dormia e se cura. Alguns bandos estão acordados desde o primeiro segundo, parados nos corredores longe da entrada, até um piloto se aproximar. A masmorra mantém só um certo número de alienígenas no ar de cada vez, e esse número cresce com o tamanho do grupo, então um bando que acorda pode ter de esperar vaga, e um bando que você destrói deixa o próximo entrar. Um grupo maior encontra mais alienígenas, em proporção, um menor encontra menos, e um tipo de alienígena nunca cai abaixo de um. Um bando que ainda espera vaga quando todos os pilotos se afastaram volta a dormir, e acorda de novo quando um piloto se aproxima.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alienígenas, para um grupo de 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Total | 235 | 235 | 235 |
| Para abrir a sala do chefe | 34 | 34 | 34 |
| A onda de uma zona de saque | 12 × Dungeon Goombah e 1 × Dungeon Crystalys | 12 × Dungeon Goombah e 1 × Dungeon Crystalys | 12 × Dungeon Goombah e 1 × Dungeon Crystalys |

- **Vivos ao mesmo tempo**: No máximo 10 por piloto do grupo, e 70 no total

<!-- dungeons-population:end -->

Cada tipo por vez. O casco e o escudo são os valores de sempre vezes o multiplicador da fase da coluna.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Parece com**: Goombah
- **Voa em bandos de**: 6

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 32.000 | 48.000 | 64.000 |
| Escudo | 48.000 | 72.000 | 96.000 |
| Dano dos lasers (uma salva por segundo) | 3.000 | 4.500 | 6.000 |
| Velocidade | 180 | 180 | 180 |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | 1.800 | 1.800 | 1.800 |

### Dungeon Pirate

- **Parece com**: Pirate Boss
- **Voa em bandos de**: 2
- **Foguete**: Um foguete reto a cada 5 s, alcance de 1.000 unidades

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 300.000 | 450.000 | 600.000 |
| Escudo | 50.100 | 75.150 | 100.200 |
| Dano dos lasers (uma salva por segundo) | 200 | 300 | 400 |
| Dano do foguete | 5.000 | 7.500 | 10.000 |
| Velocidade | 110 | 110 | 110 |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | 1.800 | 1.800 | 1.800 |

### Dungeon Crystalys

- **Parece com**: Crystalys
- **Voa em bandos de**: 2

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 256.000 | 384.000 | 512.000 |
| Escudo | 160.000 | 240.000 | 320.000 |
| Dano dos lasers (uma salva por segundo) | 10.000 | 15.000 | 20.000 |
| Velocidade | 230 | 230 | 230 |
| Alcance dos lasers | 900 | 900 | 900 |
| Raio de agressão | 2.400 | 2.400 | 2.400 |

### Dungeon Crystalys Twin

- **Parece com**: Crystalys, 1,4 vezes maior
- **Voa em bandos de**: 1

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 512.000 | 768.000 | 1.024.000 |
| Escudo | 320.000 | 480.000 | 640.000 |
| Dano dos lasers (uma salva por segundo) | 20.000 | 30.000 | 40.000 |
| Velocidade | 230 | 230 | 230 |
| Alcance dos lasers | 900 | 900 | 900 |
| Raio de agressão | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## O Senhor da guerra {#the-warlord}

O Senhor da guerra espera na sala do fim do labirinto, e é a única coisa numa masmorra que paga. É um Crystalys que cresceu enorme. O casco e o escudo dele crescem com o tamanho do grupo: quanto mais pilotos entram, mais resistente ele é, em proporção. Ele nunca sai da sala dele, com a porta fechada ou aberta: fica dentro das paredes da sala e não caça pelos corredores. Um piloto do lado de fora só consegue atraí-lo até a borda da sala, e por uma porta aberta ele ainda atira em tudo que o laser dele alcança. Ele usa as habilidades uma de cada vez, em ordem aleatória, cada uma com a sua própria recarga.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Parece com**: Crystalys, 3 vezes maior
- **Recarga do escudo**: 3.000 por segundo, após 15 s sem dano

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 10.000.000 | 15.000.000 | 25.000.000 |
| Escudo | 8.000.000 | 12.000.000 | 20.000.000 |
| Dano dos lasers (uma salva por segundo) | 12.500–15.000 | 15.000–17.500 | 20.000–25.000 |
| Velocidade | 120 | 120 | 120 |
| Alcance dos lasers | 1.100 | 1.100 | 1.100 |

O casco e o escudo acima são para um grupo de 5. Eles crescem com o grupo: são o casco e o escudo do Senhor da guerra juntos, conforme o número de pilotos no grupo quando a masmorra começa.

| Pilotos no grupo | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14.400.000 | 21.600.000 | 36.000.000 |
| 5 | 18.000.000 | 27.000.000 | 45.000.000 |
| 6 | 21.600.000 | 32.400.000 | 54.000.000 |
| 7 | 25.200.000 | 37.800.000 | 63.000.000 |
| 8 | 28.800.000 | 43.200.000 | 72.000.000 |
| 9 | 32.400.000 | 48.600.000 | 81.000.000 |
| 10 | 36.000.000 | 54.000.000 | 90.000.000 |

<!-- dungeons-boss:end -->

### A sala trancada {#the-locked-room}

A porta da sala do Senhor da guerra fica fechada desde o momento em que a masmorra é aberta, e enquanto está fechada o Senhor da guerra não pode ser ferido: nenhum laser, foguete ou explosão o atinge, e ele não usa habilidade nenhuma. A porta se abre para sempre quando **três quartos dos Crystalys e de seus Twins** com os quais a masmorra foi feita são destruídos, arredondados para cima (a tabela dos alienígenas acima os conta para um grupo de 5, e a última linha diz quantos são necessários). Contam os Crystalys e os Twins dos bandos do labirinto, inclusive os dos bandos que ficam nos corredores desde o primeiro segundo, e quem quer que os destrua. Para a porta não contam os outros alienígenas, as ondas das zonas de saque, os Goombahs que o Senhor da guerra chama nem o próprio Senhor da guerra.

A janela Masmorra do clã conta quantos deles ainda faltam destruir para abrir a sala e diz, numa etiqueta, que o Senhor da guerra não pode ser ferido, e uma mensagem avisa quando a sala é destrancada. Um bando que ainda dorme conta por inteiro, então o grupo precisa achar os Crystalys e seus Twins no labirinto. **Os outros alienígenas não somem quando a porta se abre.** Eles ficam no labirinto, acordam quando um piloto se aproxima e podem ser destruídos como antes, então um grupo que quiser pode destruir todos antes de enfrentar o Senhor da guerra: a contagem de alienígenas na janela vai até todos os alienígenas com que a masmorra foi feita e aparece cheia quando não sobra nenhum. Eles não pagam nada, e os que ainda estão vivos quando o Senhor da guerra cai vão embora com a masmorra. No minimapa a porta é uma linha vermelha enquanto está trancada e uma verde quando está aberta. Uma masmorra nunca é uma armadilha: o limite de tempo ainda encerra uma masmorra cuja porta continua fechada, e um administrador pode destrancar a sala de uma masmorra travada.

### Suas habilidades {#its-abilities}

- **O anel vermelho** da Aura de roubo de vida fere todo piloto dentro dele e cura o Senhor da guerra com esse dano. A Absorção de escudo também tem um anel vermelho: ele drena os escudos dos pilotos lá dentro e carrega o do Senhor da guerra. Nos dois casos, saia do anel ou fique atrás de uma parede.
- **Os anéis âmbar** da Queda de meteoros mostram onde os meteoros vão cair um instante depois. Continue se movendo e saia do anel antes que ele caia.
- **Foco no mais procurado** marca o piloto que causou mais dano ao Senhor da guerra, com um colchete dourado na nave dele, e o Senhor da guerra dispara nele um tiro extra a cada segundo enquanto dura. A mira dele não muda: ele continua atirando no piloto mais próximo que consegue ver, então um piloto marcado que também é o mais próximo leva os dois. O tiro extra precisa de linha livre e do alcance do laser do Senhor da guerra, então uma parede ou alguma distância o salva. Não começa enquanto ninguém causou dano.
- **A Barragem de foguetes** manda foguetes teleguiados contra pilotos aleatórios, mas só contra pilotos que o Senhor da guerra consegue ver, e uma parede no caminho detém um foguete. Um anel mostra qual piloto um foguete segue. Uma EMP Charge ou uma camuflagem os despista.
- **O Apoio do enxame** é o Senhor da guerra chamando seus Goombahs. Enquanto eles vivem, ele não pode ser ferido, e não atira nem usa outra habilidade. Destrua todos: o estandarte conta quantos restam. Se passar um minuto, o Senhor da guerra volta a poder ser ferido e os Goombahs que sobraram ficam e continuam lutando. Eles não contam para a sala do chefe e não pagam nada.
- **A Zona do Caos** é um anel violeta no chão, em volta do Senhor da guerra, e enquanto dura vai aonde o Senhor da guerra for. Ninguém dentro do anel pode atacar, nem com lasers nem com foguetes, mas reparos, camuflagem e voo continuam funcionando, e o Senhor da guerra e seus alienígenas atiram como sempre. O anel aparece um instante antes de fazer efeito: saia dele e fique fora, porque ele segue o Senhor da guerra. Um piloto fora do anel ainda pode atirar, até onde suas armas alcançarem.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Habilidade | Preparação | Duração | Recarga | Raio do anel (unidades) | O Senhor da guerra recupera, no máximo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de roubo de vida** | 2 s | 15 s | 2 min | 900 | 8% do casco e do escudo |
| **Queda de meteoros** | 1,5 s | 3 salvas, com 4 s entre elas | 2 min | 420 | – |
| **Foco no mais procurado** | 1 s | 20 s | 2 min | – | – |
| **Barragem de foguetes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorção de escudo** | 2 s | 15 s | 2 min | 900 | 6% do escudo |
| **Apoio do enxame** | 2 s | Até 1 min | 3 min | – | – |
| **Zona do Caos** | 2 s | 15 s | 2 min | 900 | – |

| Habilidade | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura de roubo de vida** | 8.000 por segundo | 10.000 por segundo | 12.000 por segundo |
| **Queda de meteoros** | 6 meteoros por salva, 40.000 cada | 8 meteoros por salva, 50.000 cada | 10 meteoros por salva, 60.000 cada |
| **Foco no mais procurado** | 18.750–22.500 por tiro extra no piloto que mais causou dano, um a cada 1 s | 22.500–26.250 por tiro extra no piloto que mais causou dano, um a cada 1 s | 30.000–37.500 por tiro extra no piloto que mais causou dano, um a cada 1 s |
| **Barragem de foguetes** | 26.000 por foguete, um a cada 15 s | 32.500 por foguete, um a cada 15 s | 39.000 por foguete, um a cada 15 s |
| **Absorção de escudo** | 10.000 de escudo por segundo | 12.500 de escudo por segundo | 15.000 de escudo por segundo |
| **Apoio do enxame** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zona do Caos** | Pilotos dentro do anel não podem atacar | Pilotos dentro do anel não podem atacar | Pilotos dentro do anel não podem atacar |

<!-- dungeons-abilities:end -->

## Zonas de saque {#loot-zones}

Um anel no chão do labirinto marca cada zona de saque assim que o grupo a encontra. Fique um instante dentro dele e a zona desperta, e uma onda de alienígenas vai até ela. Então o grupo tem de **segurar** a zona: manter um piloto dentro até a barra encher. Quanto mais pilotos no anel, mais rápido a barra enche: um número ao lado da barra diz quantas vezes mais rápido, e a tabela abaixo dá os tempos. Alienígenas suficientes no anel param a barra (a lista abaixo diz quantos), e ela recua enquanto ninguém está dentro, então limpe a onda primeiro. Quando a zona abre, o grupo vê três cartas diferentes e **vota** em uma. Uma zona abre uma vez só, e a onda dela não volta.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zonas de saque**: 6 em cada labirinto
- **Raio**: 450 unidades
- **Despertar**: Fique dentro do anel por 2 s
- **Manter**: Mantenha um piloto dentro por 30 s. A barra para enquanto houver 3 ou mais alienígenas no anel e recua enquanto não houver ninguém
- **Escolher**: O grupo tem 45 s para votar. A votação termina mais cedo se todos os pilotos presentes votaram ou se uma carta tem mais da metade dos votos

Mais pilotos no anel mantêm a zona mais rápido. Quanto tempo leva para manter uma zona:

| Pilotos no anel | Tempo para manter a zona |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 ou mais | 10 s |

<!-- dungeons-zones:end -->

### Boosters

Nas fases 2 e 3 o grupo ganha boosters destruindo os alienígenas da masmorra. Um booster cai a cada décimo deles: quando um décimo dos alienígenas é destruído, depois dois décimos, e assim por diante até todos, dez quedas no total. Conta cada alienígena com que a masmorra foi feita, não importa quem o destrua (é a contagem de alienígenas destruídos da janela Masmorra do clã); as ondas das zonas de saque e os alienígenas que o Senhor da guerra chama não contam, então uma zona não traz booster nenhum. A cada queda cada piloto ganha uma janela de meio minuto para escolher um booster temporário para si entre três que o jogo sorteia de cinco: **Dano** (seus lasers batem mais forte), **Pontos de vida** (sua nave aguenta mais casco), **Escudo** (seu escudo aguenta mais), **Velocidade** (sua nave voa mais rápido) e **Recarga do escudo** (seu escudo recarrega mais rápido). Aperte uma carta para escolhê-la. Se você não responder a tempo, o jogo escolhe Pontos de vida por você, ou o primeiro dos três se Pontos de vida não estiver entre eles. Uma escolha vale 3% na fase 3 e 1,5% na fase 2, então dez escolhas somam no máximo trinta por cento na fase 3 e quinze por cento na fase 2, sejam de que tipo forem. A fase 1 não tem boosters.

A décima queda vem com o último alienígena. Um grupo que destrói todos os alienígenas antes de lutar contra o Senhor da guerra ganha as dez quedas; um grupo que abre a sala do Senhor da guerra e segue em frente ganha as quedas dos alienígenas que destruiu até ali, e os que sobram ficam e ainda podem ser destruídos. Depois que a luta contra o Senhor da guerra começou, nenhum booster cai mais.

Um booster dura até a masmorra ser concluída. Se você sai da masmorra, ou é destruído, perde seus boosters, e os recebe de volta quando voa para dentro de novo. Uma etiqueta sob a janela Masmorra do clã lista o que você tem.

### As cartas {#the-cards}

As cartas são sorteadas uma a uma do conjunto abaixo. A chance é a de uma carta em um sorteio. Toda carta vai para todo piloto que é pago, as de equipamento também: uma carta com muitas cópias dá a cada um todas essas cópias, e uma carta de equipamento dá a cada um uma peça própria, forjada para ele. Um piloto que não é pago também não recebe carta, e uma zona aberta em uma masmorra que fracassa não paga nada.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Chance | Vai para |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 23,9% | Todo piloto pago |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65% | Todo piloto pago |
| Velkonite | 200 | 300 | 500 | 13,65% | Todo piloto pago |
| Orvium | 200 | 300 | 500 | 13,65% | Todo piloto pago |
| Ultra Core | 5.000 | 7.500 | 12.500 | 11,4% | Todo piloto pago |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 9,1% | Todo piloto pago |
| Dark Matter | 10 | 16 | 24 | 9,1% | Todo piloto pago |
| Dark Matter Plate | 1 | 1 | 2 | 4,55% | Todo piloto pago |
| Starfire-III | – | – | 1 | 0,07% | Todo piloto pago |
| Helios Beam | – | – | 1 | 0,07% | Todo piloto pago |
| Engine III | – | – | 1 | 0,07% | Todo piloto pago |
| Adaptive Core III | – | – | 1 | 0,07% | Todo piloto pago |
| Heavy Shield Core | – | – | 1 | 0,07% | Todo piloto pago |
| Momentum Thruster IV | – | – | 1 | 0,07% | Todo piloto pago |
| Impulse Thruster IV | – | – | 1 | 0,07% | Todo piloto pago |
| Hull Plating II | – | – | 1 | 0,07% | Todo piloto pago |
| Hull Plating III | – | – | 1 | 0,07% | Todo piloto pago |
| Damage Amp IV | – | – | 1 | 0,07% | Todo piloto pago |
| Crit Amp IV | – | – | 1 | 0,07% | Todo piloto pago |
| Penetration Amp IV | – | – | 1 | 0,07% | Todo piloto pago |
| Capacity Shield Cell IV | – | – | 1 | 0,08% | Todo piloto pago |
| Absorption Shield Cell IV | – | – | 1 | 0,08% | Todo piloto pago |

- **Equipamento**: As cartas com uma só cópia são equipamento: juntas, 1% das cartas

<!-- dungeons-cards:end -->

As cartas com uma única cópia são **equipamento**, e só uma masmorra de fase 3 pode oferecê-las. Uma peça de equipamento é forjada para cada piloto pago na hora do pagamento: cada um sorteia o seu [grau de encantamento](/wiki/06-Items/Overview.md#item-enchants) com as mesmas chances de uma peça que você constrói na Montagem, então a maioria sai Padrão, e um grau mais alto, até Eterno, com bônus, é um achado raro.

## Pagamento {#pay}

Quando o Senhor da guerra cai, todo piloto que mereceu é pago, uma vez por partida. As cartas escolhidas pelo grupo vêm além do pagamento da fase. Não há multiplicador de mundo: o pagamento é o mesmo em todos os mundos.

As **Orvium Reinforced Plates** não são uma carta da votação. Elas fazem parte do pagamento da fase, e cada piloto pago as recebe uma vez pela conclusão. Os itens que uma masmorra paga não são vendáveis: você não pode [vendê-los no Leilão](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Honra | Experiência | Créditos | Thulium | Munição x4 | Orvium Reinforced Plates | Pontos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 5 | 600 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 10 | 1.500 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 15 | 2.400 |

<!-- dungeons-pay:end -->

### Quem é pago {#who-is-paid}

Os alienígenas nunca pagam. Uma partida é jogada por inteiro mesmo quando não paga nada, e a tela de resultado diz por quê. A entrada nunca é recusada porque você já foi pago por uma fase: essa partida simplesmente não paga.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Um dia**: Uma fase paga um piloto uma vez por dia UTC: o dia em que o Senhor da guerra cai
- **Uma semana**: Um piloto recebe por no máximo 10 fases concluídas por semana UTC, de segunda a domingo
- **Dentro**: Pelo menos 2 min no total
- **Parte na luta**: Pelo menos uma destas: causou 2% do casco e do escudo do Senhor da guerra; destruiu 10 alienígenas da masmorra; curou outros pilotos em 50.000 durante a luta contra o Senhor da guerra

<!-- dungeons-rules:end -->

### Quanto valem um dia e uma semana {#what-a-day-and-a-week-are-worth}

O que um piloto pode receber em um dia e na melhor semana que os limites permitem. A última coluna é o que o pagamento soma aos seus [pontos PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Pagamento por piloto | Honra | Experiência | Créditos | Thulium | Munição x4 | Orvium Reinforced Plates | Pontos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Um dia, cada fase uma vez | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 30 | 4.500 |
| A melhor semana: 7 × Fase 3 e 3 × Fase 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 135 | 21.300 |

A experiência de uma fase concluída e paga conta para os seus pontos de ranking PvE: um ponto a cada 1.000 de experiência.

<!-- dungeons-totals:end -->

## A recompensa do banco do clã {#clan-bank-reward}

O banco do clã também é pago, em créditos e não em Thulium, na primeira vez que o clã conclui uma fase em uma temporada. O clã precisa ser antigo o bastante, e pilotos suficientes dessa partida precisam ser pagos. O banco é pago uma vez por fase em uma temporada.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Créditos para o banco do clã |
| :--- | ---: |
| **Fase 1** | 10.000.000 |
| **Fase 2** | 20.000.000 |
| **Fase 3** | 30.000.000 |

- **Idade do clã**: Pelo menos 3 d
- **Pilotos pagos**: Pelo menos 3 na masmorra

<!-- dungeons-clan:end -->

## Dicas {#tips}

- Elimine a onda de uma zona antes de tentar segurá-la, e lute dentro do anel se os alienígenas entrarem.
- Leve o grupo todo a uma zona: quanto mais pilotos no anel, mais rápido ela é segurada.
- Procure os Crystalys e seus Twins no labirinto: a porta do Senhor da guerra se abre quando três quartos deles estão mortos, e não antes. Os outros alienígenas podem esperar, ou ser destruídos também.
- Use as paredes: os lasers não as atravessam, os anéis vermelhos das auras do Senhor da guerra param nelas, e uma parede detém também os foguetes dele.
- Guarde uma EMP Charge para a Barragem de foguetes.
- Quando o Senhor da guerra chamar seus Goombahs, destrua-os primeiro: ele não pode ser ferido até eles sumirem. Na Zona do Caos, saia do anel antes de atirar.
- Fique de olho no relógio da janela Masmorra do clã. Quando o tempo acaba, a masmorra fracassa e não paga nada.
