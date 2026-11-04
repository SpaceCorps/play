<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Masmorras -->
# Masmorras {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; masmorra; masmorras; portão; portões; senhor da guerra; labirinto; fase; zona de saque; carta -->

Uma **masmorra** é o que o jogo chama de **portão**: um labirinto fechado com um **Senhor da guerra** no fim. Um vice-líder ou o líder de um [clã](/wiki/03-Mechanics/Clans.md) abre um e o paga com o banco do clã, e os membros do clã voam juntos para dentro como um único [grupo](/wiki/03-Mechanics/Groups.md). Eles abrem caminho entre os alienígenas do labirinto, abrem zonas de saque para escolher uma carta em cada uma e derrubam o Senhor da guerra. Todo piloto que participou da luta é pago quando o Senhor da guerra cai, dentro dos limites mais abaixo. Os portões ficam na aba **Portões** da página do clã.

Um portão é uma luta só contra os alienígenas: ninguém pode atacar dentro dele um colega de clã nem qualquer outra pessoa. Os alienígenas não pagam nada. O pagamento é só do Senhor da guerra, então a única maneira de ser pago é estar na luta quando ele cai.

## Em resumo {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Abre**: A partir do dia 4 da temporada
- **Quem abre um portão**: Um vice-líder ou o líder, que paga o preço com o banco do clã
- **Grupo**: De 4 a 10 membros do clã, em um só grupo
- **Portões por dia**: 3 por clã em um dia UTC, um aberto por vez
- **Portões ao mesmo tempo**: 6 em um mundo
- **Mapas**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labirintos**: 8; um é sorteado quando um portão é aberto
- **Reunião**: 10 min para reunir e iniciar. Um portão que ninguém inicia se fecha, e o preço volta ao banco do clã
- **Limite de tempo**: Fase 1: 80 min, Fase 2: 110 min, Fase 3: 150 min a partir do início. Quando esgota, o portão falha e não paga nada
- **Vazio**: Um portão sem ninguém dentro por 3 min falha
- **Depois que o Senhor da guerra cai**: O portão fica aberto por 2 min, para os pilotos que estão dentro
- **Voltar**: Um piloto que saiu ou foi destruído pode voltar a entrar voando 3 vezes, com 20 s entre elas

<!-- dungeons-glance:end -->

## Como é uma partida {#how-a-run-goes}

1. **Invocar.** Na aba Portões, um [vice-líder ou o líder](/wiki/03-Mechanics/Clans.md#hierarchy-roles) escolhe uma fase e aperta **Invocar**. O preço sai do [banco do clã](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), e o portão recebe um dos mapas listados acima. Um portão que ninguém inicia se fecha, e o preço volta ao banco.
2. **Entrar.** Os membros do clã apertam **Entrar** na janela do Clã enquanto estão voando. Os pilotos lá dentro formam o grupo do portão.
3. **Iniciar.** O piloto que abriu o portão, ou um oficial, aperta **Iniciar** quando há pilotos suficientes lá dentro. Depois disso, só podem voltar os pilotos que já estavam dentro.
4. **Abrir caminho pelo labirinto.** Você entra por uma ponta do labirinto e o Senhor da guerra espera na outra. Os alienígenas dormem em suas salas e acordam em bandos quando o grupo se aproxima.
5. **Abrir as zonas de saque.** Anéis no labirinto marcam as zonas. Segure uma e o grupo vota numa carta, que é paga junto com o pagamento do Senhor da guerra.
6. **Derrotar o Senhor da guerra.** Quebre seu escudo e seu casco e responda às suas habilidades. Quando ele cai, o portão está concluído.
7. **Ser pago.** O pagamento vem no momento em que o Senhor da guerra cai. O portão continua aberto um pouco mais para os pilotos lá dentro e depois se fecha.

## Entrar {#entering}

Para entrar em um portão você precisa de uma **nave em voo**, então decole primeiro e depois abra a janela do Clã, e de um [grupo](/wiki/03-Mechanics/Groups.md) com membros suficientes do clã. Você também precisa do **nível** que a fase pede, e não pode já estar dentro de outro portão. O grupo de um portão tem um limite de tamanho: quando está cheio, ninguém mais entra.

Um vice-líder ou o líder abre um portão, um de cada vez para o clã, e só até o número de portões por dia. O banco do clã precisa ter o preço. Um clã só pode abrir uma fase depois de concluir a anterior.

Dentro de um portão você não pode trocar de mundo, e a Jump CPU e a Base CPU não funcionam. O botão **Sair** da barra do portão leva você para fora depois de confirmar. Um piloto que saiu, ou que foi destruído, pode voltar algumas vezes, com uma curta espera entre elas.

## As fases {#the-stages}

Um portão tem uma fase, e a fase é a sua dificuldade. Uma fase mais alta tem alienígenas mais resistentes que batem mais forte, e paga mais. Os multiplicadores da tabela valem para todo alienígena e para o Senhor da guerra. Dano significa lasers, foguetes e as habilidades do Senhor da guerra. A tabela também diz quantos alienígenas uma fase manda em comparação com a primeira. O **preço** é tirado do banco do clã quando o portão é aberto.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Requisito | Casco e escudo dos alienígenas | Número de alienígenas | Dano dos alienígenas | Preço do portão (créditos, do banco do clã) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | A partir do nível 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | A partir do nível 7 | ×1,5 | ×1 | ×1,25 | 1.000.000 |
| **Fase 3** | A partir do nível 8 | ×2,5 | ×1 | ×1,5 | 2.000.000 |

<!-- dungeons-stages:end -->

## O labirinto {#the-maze}

Cada portão é um labirinto fechado em um mapa próprio, um dos mapas da lista acima, e o labirinto é um de vários desenhos. Um labirinto é uma grade de salas e corredores com paredes sólidas. As naves não atravessam uma parede, e uma parede bloqueia os tiros, então serve de abrigo. Um meteoro cai de cima, e uma parede não o detém.

## Os alienígenas {#the-aliens}

Quatro tipos de alienígenas guardam o labirinto. Eles dormem em suas salas e acordam quando um piloto se aproxima. O portão mantém no ar só um certo número de alienígenas ao mesmo tempo, e esse número cresce com o tamanho do grupo, então um bando que você destrói deixa o próximo entrar. Um grupo maior enfrenta mais alienígenas em proporção, um menor enfrenta menos, e um tipo de alienígena nunca fica abaixo de um.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alienígenas, para um grupo de 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Total | 195 | 195 | 195 |
| A onda de uma zona de saque | 10 × Gate Goombah e 1 × Gate Crystalys | 10 × Gate Goombah e 1 × Gate Crystalys | 10 × Gate Goombah e 1 × Gate Crystalys |

- **Vivos ao mesmo tempo**: No máximo 10 por piloto do grupo, e 70 no total

<!-- dungeons-population:end -->

Cada tipo por vez. O casco e o escudo são os valores de sempre vezes o multiplicador da fase da coluna.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Parece com**: Goombah
- **Voa em bandos de**: 6

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 32.000 | 48.000 | 80.000 |
| Escudo | 48.000 | 72.000 | 120.000 |
| Dano dos lasers (uma salva por segundo) | 3.000 | 3.750 | 4.500 |
| Velocidade | 180 | 180 | 180 |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | 1.800 | 1.800 | 1.800 |

### Gate Pirate

- **Parece com**: Pirate Boss
- **Voa em bandos de**: 2
- **Foguete**: Um foguete reto a cada 5 s, alcance de 970 unidades

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 300.000 | 450.000 | 750.000 |
| Escudo | 50.100 | 75.150 | 125.250 |
| Dano dos lasers (uma salva por segundo) | 200 | 250 | 300 |
| Dano do foguete | 5.000 | 6.250 | 7.500 |
| Velocidade | 92 | 92 | 92 |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | 1.800 | 1.800 | 1.800 |

### Gate Crystalys

- **Parece com**: Crystalys
- **Voa em bandos de**: 2

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 256.000 | 384.000 | 640.000 |
| Escudo | 160.000 | 240.000 | 400.000 |
| Dano dos lasers (uma salva por segundo) | 10.000 | 12.500 | 15.000 |
| Velocidade | 230 | 230 | 230 |
| Alcance dos lasers | 900 | 900 | 900 |
| Raio de agressão | 2.400 | 2.400 | 2.400 |

### Gate Crystalys Twin

- **Parece com**: Crystalys, 1,4 vezes maior
- **Voa em bandos de**: 1

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 512.000 | 768.000 | 1.280.000 |
| Escudo | 320.000 | 480.000 | 800.000 |
| Dano dos lasers (uma salva por segundo) | 20.000 | 25.000 | 30.000 |
| Velocidade | 230 | 230 | 230 |
| Alcance dos lasers | 900 | 900 | 900 |
| Raio de agressão | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## O Senhor da guerra {#the-warlord}

O Senhor da guerra espera na sala da ponta oposta do labirinto, e é a única coisa de um portão que paga. É um Crystalys que cresceu até ficar enorme. Seu casco e seu escudo crescem com o tamanho do grupo: quanto mais pilotos entram, mais resistente ele é, em proporção. Ele fica em sua sala e usa suas habilidades uma de cada vez, em ordem aleatória, cada uma com a sua própria recarga.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Parece com**: Crystalys, 3 vezes maior
- **Recarga do escudo**: 3.000 por segundo, após 15 s sem dano

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 10.000.000 | 15.000.000 | 25.000.000 |
| Escudo | 8.000.000 | 12.000.000 | 20.000.000 |
| Dano dos lasers (uma salva por segundo) | 8.000 | 10.000 | 12.000 |
| Velocidade | 120 | 120 | 120 |
| Alcance dos lasers | 1.100 | 1.100 | 1.100 |

O casco e o escudo acima são para um grupo de 5. Eles crescem com o grupo: são o casco e o escudo do Senhor da guerra juntos, conforme o número de pilotos no grupo quando o portão começa.

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

### Suas habilidades {#its-abilities}

- **O anel vermelho** da Aura de roubo de vida fere todo piloto dentro dele e cura o Senhor da guerra com esse dano. A Absorção de escudo também tem um anel vermelho: ele drena os escudos dos pilotos lá dentro e carrega o do Senhor da guerra. Nos dois casos, saia do anel ou fique atrás de uma parede.
- **Os anéis âmbar** da Queda de meteoros mostram onde os meteoros vão cair um instante depois. Continue se movendo e saia do anel antes que ele caia.
- **Foco nos curandeiros** volta o Senhor da guerra contra quem cura outro piloto, e ele bate mais forte nesse piloto. Espalhe a cura.
- **A Barragem de foguetes** manda foguetes teleguiados contra pilotos aleatórios. Uma EMP Charge ou uma camuflagem os despista.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Habilidade | Preparação | Duração | Recarga | Raio do anel (unidades) | O Senhor da guerra recupera, no máximo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de roubo de vida** | 2 s | 15 s | 2 min | 900 | 8% do casco e do escudo |
| **Queda de meteoros** | 1,5 s | 3 salvas, com 4 s entre elas | 2 min | 420 | – |
| **Foco nos curandeiros** | 1 s | 45 s | 2 min | – | – |
| **Barragem de foguetes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorção de escudo** | 2 s | 15 s | 2 min | 900 | 6% do escudo |

| Habilidade | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura de roubo de vida** | 8.000 por segundo | 10.000 por segundo | 12.000 por segundo |
| **Queda de meteoros** | 6 meteoros por salva, 40.000 cada | 8 meteoros por salva, 50.000 cada | 10 meteoros por salva, 60.000 cada |
| **Foco nos curandeiros** | O laser dele atinge ×1,5 mais forte o piloto em quem ele se volta | O laser dele atinge ×1,5 mais forte o piloto em quem ele se volta | O laser dele atinge ×1,5 mais forte o piloto em quem ele se volta |
| **Barragem de foguetes** | 6.500 por foguete, um a cada 15 s | 8.125 por foguete, um a cada 15 s | 9.750 por foguete, um a cada 15 s |
| **Absorção de escudo** | 10.000 de escudo por segundo | 12.500 de escudo por segundo | 15.000 de escudo por segundo |

<!-- dungeons-abilities:end -->

## Zonas de saque {#loot-zones}

Um anel no chão do labirinto marca cada zona de saque assim que o grupo a encontra. Fique um instante lá dentro e a zona acorda, e uma onda de alienígenas vai atrás dela. Então o grupo tem de **segurar** a zona: manter um piloto lá dentro até a barra encher. Alienígenas no anel param a barra, e ela recua enquanto não há ninguém dentro, então elimine a onda primeiro. Quando a zona se abre, o grupo vê três cartas diferentes e **vota** em uma. Uma zona se abre uma vez só, e a sua onda não volta.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zonas de saque**: 4 em cada labirinto
- **Raio**: 450 unidades
- **Despertar**: Fique dentro do anel por 2 s
- **Manter**: Mantenha um piloto dentro por 30 s. A barra para enquanto houver 3 ou mais alienígenas no anel e recua enquanto não houver ninguém
- **Escolher**: O grupo tem 45 s para votar. A votação termina mais cedo se todos os pilotos presentes votaram ou se uma carta tem mais da metade dos votos

<!-- dungeons-zones:end -->

### As cartas {#the-cards}

As cartas são sorteadas uma a uma do conjunto abaixo. A chance é a de uma carta em um sorteio. Uma carta com muitas cópias vai para todo piloto que é pago, e uma carta de equipamento, com uma só cópia, vai para um piloto do grupo. Um piloto que não é pago também não recebe carta, e uma zona aberta em um portão que fracassa não paga nada.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Chance | Vai para |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 21% | Todo piloto pago |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12% | Todo piloto pago |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12% | Todo piloto pago |
| Velkonite | 200 | 300 | 500 | 12% | Todo piloto pago |
| Orvium | 200 | 300 | 500 | 12% | Todo piloto pago |
| Ultra Core | 5.000 | 7.500 | 12.500 | 10% | Todo piloto pago |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 8% | Todo piloto pago |
| Dark Matter | 5 | 8 | 12 | 8% | Todo piloto pago |
| Dark Matter Plate | 1 | 1 | 2 | 4% | Todo piloto pago |
| Engine III | 1 | 1 | 1 | 0,25% | Um piloto do grupo |
| Heavy Shield Core | 1 | 1 | 1 | 0,25% | Um piloto do grupo |
| Adaptive Core III | 1 | 1 | 1 | 0,25% | Um piloto do grupo |
| Starfire-III | 1 | 1 | 1 | 0,25% | Um piloto do grupo |

- **Equipamento**: As cartas com uma só cópia são equipamento: juntas, 1% das cartas

<!-- dungeons-cards:end -->

## Pagamento {#pay}

Quando o Senhor da guerra cai, todo piloto que mereceu é pago, uma vez por partida. As cartas escolhidas pelo grupo vêm além do pagamento da fase. Não há multiplicador de mundo: o pagamento é o mesmo em todos os mundos.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Honra | Experiência | Créditos | Thulium | Munição x4 | Pontos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 600 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 1.500 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 2.400 |

<!-- dungeons-pay:end -->

### Quem é pago {#who-is-paid}

Os alienígenas nunca pagam. Uma partida é jogada por inteiro mesmo quando não paga nada, e a tela de resultado diz por quê. A entrada nunca é recusada porque você já foi pago por uma fase: essa partida simplesmente não paga.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Um dia**: Uma fase paga um piloto uma vez por dia UTC: o dia em que o Senhor da guerra cai
- **Uma semana**: Um piloto recebe por no máximo 10 fases concluídas por semana UTC, de segunda a domingo
- **Dentro**: Pelo menos 2 min no total
- **Parte na luta**: Pelo menos uma destas: causou 2% do casco e do escudo do Senhor da guerra; destruiu 10 alienígenas do portão; curou outros pilotos em 50.000 durante a luta contra o Senhor da guerra

<!-- dungeons-rules:end -->

### Quanto valem um dia e uma semana {#what-a-day-and-a-week-are-worth}

O que um piloto pode receber em um dia e na melhor semana que os limites permitem. A última coluna é o que o pagamento soma aos seus [pontos PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Pagamento por piloto | Honra | Experiência | Créditos | Thulium | Munição x4 | Pontos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Um dia, cada fase uma vez | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 4.500 |
| A melhor semana: 7 × Fase 3 e 3 × Fase 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 21.300 |

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
- **Pilotos pagos**: Pelo menos 3 no portão

<!-- dungeons-clan:end -->

## Dicas {#tips}

- Elimine a onda de uma zona antes de tentar segurá-la, e lute dentro do anel se os alienígenas entrarem.
- Use as paredes: os lasers não as atravessam, e os anéis do Senhor da guerra param nelas.
- Guarde uma EMP Charge para a Barragem de foguetes.
- Fique de olho no relógio da barra do portão. Quando o tempo acaba, o portão fracassa e não paga nada.
