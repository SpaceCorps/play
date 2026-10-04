<!-- wiki-i18n source: 1fb27e9af6058c8b -->
<!-- wiki-i18n title: Combate -->
# Mecânica de combate {#combat-mechanics}

Esta seção detalha como o dano é calculado, aplicado e reparado durante os combates em SpaceCorps.

## Cálculo do dano {#damage-calculation}

Quando uma nave dispara os lasers, o servidor calcula o dano causado na sequência a seguir:

### 1. Dano base e variação aleatória {#1-base-damage-random-variance}

O dano base de todos os lasers equipados (incluindo os lasers dos drones) e dos amplificadores de laser encaixados neles é somado.
- **Sorteio aleatório**: o dano real de uma rajada é sorteado entre **80%** e **100%** do dano base total.
  - Fórmula: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Acertos críticos {#2-critical-hits}

Toda rajada tem uma chance de ser um acerto crítico.
- **Chance de crítico**: a chance de crítico média dos lasers equipados mais a soma das chances de crítico de todos os amplificadores de laser equipados.
- **Multiplicador de crítico**: se um disparo é crítico, o sorteio de dano é multiplicado por **1,5x**. O número de dano de uma rajada crítica aparece em ciano gelo, maior, com um “!”.
- Os Quantum Laser 1 e 2 não têm chance de crítico própria: quem a dá são os amplificadores deles.
- **Dano crítico fixo**: qualquer dano crítico fixo dos amplificadores de laser é somado depois do multiplicador.
  - Fórmula: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Multiplicadores globais {#3-global-multipliers}

Por fim, os multiplicadores globais (como boosters ativos ou multiplicadores de munição de laser como x2, x3, x4) são aplicados para obter o dano final:
- Fórmula: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- A munição **Siphon Battery** tem o multiplicador x1, mas um alvo diferente: o dano dela sai só do escudo do alvo (nunca do casco, seja qual for a absorção) e vai para o seu próprio escudo, até o seu máximo. Veja [Lasers e munição](/wiki/06-Items/Lasers.md).

### 3b. Foguetes {#3b-rockets}

Um [foguete](/wiki/06-Items/Rockets.md) tem o seu próprio dano (um Lancet I causa de 1.600 a 2.000, um Lancet III de 4.800 a 6.000, uma N.U.K.E. de 45.000 a 50.000), sorteado uma vez ao ser disparado e igual para todas as naves: os seus lasers, amplificadores, boosters e munição não o alteram, e ele não causa acerto crítico. Todos os foguetes compartilham um único temporizador de **5 segundos**. Um foguete de alvo único tem uma **penetração de escudo**: ela é descontada da absorção do seu alvo (veja Sofrer dano, abaixo); uma explosão atinge todas as naves dentro do seu raio, menos perto da borda. Nada limita o que um foguete tira da nave de um piloto: primeiro o escudo, depois o casco. Os foguetes nunca machucam a sua própria corporação nem o seu próprio [grupo](/wiki/03-Mechanics/Groups.md), sejam quais forem as corporações dos membros.

### 4. Ficar de frente para o alvo {#4-facing-the-target}

Uma nave ou um alienígena que está com o alvo travado e atirando gira para ficar de frente para o alvo, seja qual for o rumo em que está voando (circulando, recuando ou parado), e volta ao seu curso quando para de atirar.

### 5. Alcance {#5-range}

Uma nave dispara uma rajada por segundo enquanto o alvo está dentro do seu **alcance**, e segura o fogo enquanto o alvo está mais longe: o fogo deixa de gastar munição até o alvo chegar perto o bastante de novo, e o painel do alvo mostra “Fora de alcance”. O alcance é **a média dos alcances de todos os seus lasers** (os lasers dos drones também), arredondada para a unidade mais próxima, e é um único número para a nave inteira: dentro dele todo laser dispara, fora dele nenhum dispara. Um laser de longo alcance ao lado de lasers curtos, portanto, não amplia o seu alcance: um Starfire-3 (850) e dois Quantum Laser 2 (700) dão 750. Um bônus de alcance da Forja conta no próprio laser antes da média. Uma nave sem laser não pode disparar os lasers, e o hangar não mostra alcance para ela (um traço); os foguetes dela ainda disparam, cada um com o seu próprio alcance (veja [Foguetes](/wiki/06-Items/Rockets.md)). Veja [Lasers e munição](/wiki/06-Items/Lasers.md) para o alcance de cada laser.

---

## Recompensas de abate: o primeiro acerto reivindica {#kill-rewards-first-hit-claims}

As recompensas de um alienígena vão para o piloto que atirou nele primeiro, não para quem dá o último golpe.

- **Reivindicar**: o primeiro piloto cujo tiro causa dano a um alienígena o reivindica. Cada acerto seu renova a sua reivindicação.
- **Perder a reivindicação**: se você não acerta o alienígena por **10 segundos**, a sua reivindicação expira e o próximo piloto a acertá-lo a reivindica. A sua reivindicação também termina quando a sua nave é destruída ou você sai do mapa (por um portal ou desconectando), e voltar dentro dos 10 segundos não a recupera.
- **O abate**: quando o alienígena é destruído, o piloto que detém a reivindicação dele recebe tudo: créditos, Thulium, XP, honra, o abate para missões e pontos de reset, e a caixa de [carga](/wiki/03-Mechanics/Cargo.md). Um piloto que termina um alienígena reivindicado por outro não recebe nada, e o Registro do jogo avisa. Quando a sua reivindicação paga e outro piloto dá o último golpe, o Registro do jogo cita esse piloto e diz que a sua reivindicação paga a você.
- **Pontos de ranking**: o abate também soma pontos PvE ao ranking do piloto que detém a reivindicação, mais quanto mais resistente é o alienígena: 1 por um Seeker, 2 por um Phantasm, 4 por um Bulwark, 7 por um Goombah e 16 por um Crystalys (o artigo de cada alienígena traz o seu). Eles são só de quem fez o abate: a divisão das recompensas de um grupo não os inclui.
- **Ver a reivindicação**: quando você seleciona um alienígena que outro piloto reivindicou, a janela do alvo mostra *Reivindicado por* esse piloto e *Sem recompensa*.
- Os [pilotos de corporação](/wiki/03-Mechanics/Company-Pilots.md) nunca reivindicam um alienígena, e um alienígena que eles terminam ainda paga ao piloto que detém a reivindicação dele.
- Um piloto em um [grupo](/wiki/03-Mechanics/Groups.md) divide o que a sua reivindicação paga com os colegas de grupo que estão por perto e atirando; a reivindicação em si é só do piloto.
- **Os líderes dos [enxames](/wiki/05-Swarms/Swarms.md) e as Dormant Pulses são a exceção**: um chefe de enxame e cada Dormant Pulse pagam pelo dano que cada piloto causou a eles, não pelo primeiro acerto, e a caixa de carga deles vai para o piloto que mais causou dano ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Os demais seguidores, os Pirate Scouts e os Seeker Slaves, pagam pela reivindicação, como qualquer alienígena. Os pontos PvE de uma nave de enxame estão na página Enxames.

---

## Alienígenas que só revidam {#aliens-that-only-fight-back}

O Seeker e o Goombah nunca começam uma luta. Cada um se volta contra um piloto que o acerta (um acerto que causa dano; o fogo de outro alienígena nunca o provoca), luta contra o piloto indicado em [Contra quem um alienígena luta](#who-an-alien-fights) e desiste **10 segundos** depois de qualquer um o ter acertado pela última vez. Deixado em paz por **30 segundos**, o casco dele se recupera 2% do máximo por segundo. Os outros alienígenas (Phantasm, Bulwark, Crystalys) vão atrás de qualquer piloto desprotegido que chegue ao raio de agressão deles (700, 700 e 900 unidades) e nunca recuperam o casco; o escudo de todo alienígena volta a recarregar 15 segundos depois do último acerto dele.

---

## Contra quem um alienígena luta {#who-an-alien-fights}

Um alienígena continua lutando contra **o primeiro piloto que atirou nele**, enquanto ainda puder perseguir esse piloto: o piloto está no mapa, fora de uma zona segura, não está camuflado nem dentro da janela do próprio EMP, está vivo e o acertou nos últimos **10 segundos** (cada acerto reinicia os 10 segundos: uma rajada de laser, um foguete ou a borda de uma explosão, tanto faz). Enquanto isso vale, os tiros de outros pilotos nunca o desviam, por mais perto que estejam ou por mais vezes que acertem, de modo que um piloto pode segurar um alienígena enquanto outros atiram nele.

Quando o primeiro piloto sai da luta (sai do mapa, chega a uma zona segura, se camufla ou dispara um EMP, é destruído ou deixa de acertar o alienígena por 10 segundos), o alienígena se volta contra o **próximo** piloto que entrou na luta, na ordem em que atiraram nele pela primeira vez, e não contra o que o acertou por último. Um piloto que saiu da luta e atira nele de novo entra no fim da fila. Um alienígena acompanha os primeiros **32** pilotos que atiraram nele; um 33º atirador não faz parte da fila até que um deles saia da luta e, em uma multidão de qualquer tamanho, o alienígena continua no primeiro.

Os [pilotos de corporação](/wiki/03-Mechanics/Company-Pilots.md) contam depois de todos os jogadores: um alienígena só luta contra um piloto de corporação enquanto nenhum jogador que ele ainda possa perseguir tiver atirado nele, um jogador que atira em um alienígena que um piloto de corporação está combatendo toma o lugar desse piloto, e um piloto de corporação nunca desvia um alienígena de um jogador. Nada disso muda quem recebe as recompensas do alienígena: isso cabe à reivindicação ([Recompensas de abate](#kill-rewards-first-hit-claims)).

---

## Alienígenas perdem o interesse {#aliens-lose-interest}

Nenhum alienígena segue você pelo mapa inteiro. Mas um alienígena que você está **acertando** não está perdendo o interesse, ele está lutando contra você: por **10 segundos** depois do seu último acerto (cada acerto reinicia os 10 segundos, seja uma rajada de laser, um foguete ou a borda de uma explosão), ele voa na sua direção, na velocidade dele, sempre que você está além do seu alcance de ataque (Seeker 600, Phantasm e Bulwark 700, Goombah 800, Crystalys 900), e continua se aproximando e atirando até você estar ao alcance. Não há limite para a distância que ele percorre enquanto você continuar a acertá-lo. Um laser que alcança mais longe que a arma do alienígena (um Starfire-3 alcança 850 unidades, um Helios Beam 900) não deixa você acertá-lo de onde ele não pode responder, e uma nave mais rápida só o mantém atrás de você enquanto você continuar atirando. Ele ainda desiste de você na hora se você chega a uma zona segura, se camufla ou sai do mapa.

Quando vários pilotos acertam o mesmo alienígena, ele continua no primeiro que atirou nele (veja [Contra quem um alienígena luta](#who-an-alien-fights)): ele se aproxima desse piloto e atira, de modo que um grupo parado ao redor dele, logo fora do alcance, não consegue mantê-lo correndo de um para o outro sem nunca responder.

Um alienígena que escolheu você como alvo (um Phantasm, Bulwark ou Crystalys de que você se aproximou, ou qualquer alienígena em que você atirou) e que você não acerta há 10 segundos desiste assim que uma destas condições é verdadeira:

- **Você nunca atirou nele:** você está a mais de **1.200 unidades** dele, ou ele voou **2.000 unidades** a partir de onde a perseguição começou.
- **Você atirou nele no último minuto:** você está a mais de **2.500 unidades** dele, ou ele voou **3.000 unidades** a partir de onde a perseguição começou. Uma luta que você começou continua justa.

Um alienígena que desiste passa a vagar de onde está, nunca indo para onde viu você pela última vez (nem quando você se camufla ou dispara um EMP), e não escolhe você como alvo de novo por **8 segundos**, a menos que você atire nele. Cada alienígena decide por si, então um bando misto vai se desfazendo conforme você se afasta voando. Os alienígenas nunca seguem você para dentro de uma zona segura nem por um portal, e os que perderam você perto de um se afastam dele, cada um para o seu lado, para não ficarem esperando amontoados. O interesse de um alienígena nunca fica abaixo do alcance de ataque e do raio de agressão dele, mais 100 unidades.

Os alienígenas não se amontoam: um bando atrás de um piloto mantém algum espaço entre as suas naves enquanto se aproxima (150 unidades entre os cascos, de modo que um bando de Phantasms voa a 250 unidades de distância uns dos outros, em vez de casco a casco), e um alienígena que segue o seu caminho com outros por perto voa para longe deles, de modo que um bando que perdeu o seu piloto se desfaz em todas as direções.

Voar mais rápido só ajuda até certo ponto: uma Protos (150) é mais lenta do que todos os alienígenas que caçam (Phantasm 160, Bulwark 175, Crystalys 230), então o limite de distância, e não a sua velocidade, encerra a perseguição.

---

## Sofrer dano e zonas seguras {#taking-damage-safe-zones}

Quando a sua nave é atingida por um inimigo ou NPC, o dano é processado assim:

### 1. Absorção do escudo {#1-shield-absorption}

O dano recebido é dividido entre os escudos e os pontos de vida pela **Absorção média** da sua nave: a média da absorção dos seus escudos, cada um contado com as suas células de escudo, mais o Shield Absorbance Boost da Loja de PR (veja [Mecânica dos escudos](/wiki/03-Mechanics/Shields.md)). Ela **não tem teto de 100%**: o que os escudos recebem de um impacto é a sua absorção **menos a penetração de escudo de quem ataca**, entre 0% e 100%.
- **A absorção** (por exemplo, 80% para o melhor escudo com as melhores células, 56% para um Basic Shield Core com duas Absorption Shield Cell I) de cada impacto é recebida pelos escudos, menos a penetração do impacto: os 35% de um Lancet III deixam 45% nos escudos de uma nave de 80%, e o resto (55% nesse caso) atinge os HP diretamente.
- A **penetração de escudo** vem dos foguetes de alvo único (10 a 35%) e da munição de laser x3 e x4 (5% e 10%); os alienígenas não têm nenhuma. Uma nave acima de 100% (112%, por exemplo) segura um impacto inteiro contra uma penetração de até a diferença (12% nesse caso).
- Um escudo baixo demais para a sua parte passa a diferença para os HP; se os escudos estão totalmente esgotados, **100%** de todo o dano restante atinge os HP.
- Os alienígenas não têm atributo de absorção: os escudos deles recebem 80% de cada impacto (menos a penetração do impacto), e o casco, o resto.

### 2. Imunidade na zona segura {#2-safe-zone-immunity}

A base de origem de cada corporação (mapas X-1) tem zonas seguras.
- Entrar em uma zona segura deixa a sua nave completamente imune a dano.
- **Quebra de agressão**: atacar um inimigo remove imediatamente a sua imunidade de zona segura, mesmo que você esteja fisicamente dentro de uma.
- Um anel ao redor de cada estação e de cada portal protege você depois que se passaram 5 segundos desde que você foi atingido e 15 desde que você atirou. Enquanto ele protege você e você está fora de combate, a janela do hangar permite trocar de nave sem sair do jogo: veja [O hangar em voo](/wiki/03-Mechanics/Hangar.md).
- As estações existem só nas bases de origem (`x-1`). Os setores de perigo (`DS-1` a `DS-4`) não têm nenhuma: ali, os anéis ao redor dos portais são as únicas zonas seguras.

### 3. Sob ataque em um setor de perigo {#3-under-attack-in-a-danger-sector}

Um salto por um portal leva 3 segundos (veja [Viagem pelo mapa espacial](/wiki/01-General/Spacemap%20Travel.md)). Nos setores de perigo (`DS-1` a `DS-4`), um piloto cuja nave foi atingida por outro piloto ou por um alienígena nos últimos **10 segundos** não pode iniciar um, e um acerto cancela um salto em andamento. Em todos os outros lugares, os ataques nunca interrompem um salto, e nada interrompe a coleta de uma caixa de [carga](/wiki/03-Mechanics/Cargo.md).

---

## Recuperação e reparo {#recovery-repair}

Para se recuperar do combate, os pilotos podem contar com a regeneração passiva e com bots utilitários ativos:

### 1. Regeneração passiva do escudo {#1-shield-passive-regeneration}

- **Funcionamento**: restaura pontos de escudo iguais à taxa de recarga do seu escudo por segundo.
- **Atraso**: interrompida pelo combate; a regeneração passiva só volta depois de **15 segundos** sem receber dano.

### 1b. Siphon Battery {#1b-siphon-battery}

A munição [Siphon Battery](/wiki/06-Items/Lasers.md) soma na hora ao seu escudo o escudo que drena de um alvo, até o seu máximo. Ganhar escudo não é sofrer dano, então isso não atrasa a sua regeneração passiva.

### 2. Drones de reparo (reparo do casco) {#2-repair-drones-hull-repair-}

- **Funcionamento**: se você equipa um Repair Drone (nos extras do hangar), você o liga na barra de atalhos (arraste-o do seletor de Extras para um slot) e ele repara o seu casco (HP). Qualquer acerto o desliga, e ele para quando o casco está cheio. Com uma [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) equipada, você não precisa ligá-lo de novo: a CPU o lança sozinha assim que o atraso indicado abaixo passa, a menos que você o tenha parado à mão.
- **Taxa de reparo**: restaura uma porcentagem dos seus pontos de vida máximos por segundo (só conta o melhor drone equipado, eles não se somam):
  - **Repair Drone I**: 1,5% dos HP máx. / s
  - **Repair Drone II**: 2,25% dos HP máx. / s
  - **Repair Drone III**: 3,5% dos HP máx. / s
  - **Repair Drone IV**: 5% dos HP máx. / s
- **Atraso**: os drones de reparo só começam a remendar o casco depois de **10 segundos** sem receber dano.
- **Em um slot de habilidade**, um Repair Drone não repara sozinho: ele dá a você o **Emergency Repair**, um botão que cura uma parte dos seus pontos de vida máximos ao longo de dez segundos, mesmo sob fogo (veja [Habilidades](/wiki/03-Mechanics/Abilities.md)).

---

## Camuflagem e o EMP {#cloaking-and-the-emp}

Um tiro precisa de uma trava. Dois [extras](/wiki/06-Items/Extras.md) tiram a sua:

- **Cloaking CPU**: enquanto você está camuflado (não há limite de tempo), os pilotos de outras corporações, os alienígenas e os pilotos de corporação não veem a sua nave e não conseguem travar nela; eles veem um simples ponto vermelho no minimapa onde você está. A sua primeira rajada encerra a camuflagem, e você não pode se camuflar de novo por um minuto, nem dentro de 10 segundos depois de um acerto ou de um tiro.
- **EMP Charge**: por 3 segundos ninguém pode travar em você, e toda trava que já está em você se rompe na hora. Ele encerra toda camuflagem a até 1.500 unidades do piloto que o dispara, exceto as do próprio grupo do piloto. Ele não esconde você, e não é invulnerabilidade: ele impede o que precisa de trava.

Um foguete também é um tiro: ele encerra a sua própria camuflagem, e a explosão em área do foguete de outra pessoa ainda machuca uma nave camuflada e encerra a camuflagem dela, porque uma explosão não precisa de trava (veja [Foguetes](/wiki/06-Items/Rockets.md)). O EMP detém lasers travados e foguetes guiados, não uma explosão.

Nenhum dos dois altera uma reivindicação de abate: uma reivindicação é o histórico de quem acertou um alienígena, não uma trava, e a camuflagem libera a sua.
