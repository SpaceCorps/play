<!-- wiki-i18n source: 4d2749864875137f -->
<!-- wiki-i18n title: Portões solo -->
# Portões solo {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; portões solo; portão solo; portões galácticos; peça; peças; materializador de energia; giro; garantia; onda; ondas; vidas; retomar; abandonar; sem morrer; desafio; conquista; limite de thulium -->

Os **portões solo** são cinco portões dos Portões Galácticos que você pilota sozinho: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** e **Omega Vault**. Cada um é uma arena vazia própria onde ondas de alienígenas vêm até você uma após a outra e um chefe espera no fim. Você constrói um portão com as suas **peças**, que encontra girando o Materializador de Energia com Thulium, e uma vitória paga Créditos, Thulium, experiência, honra, minério, placas e munição.

Um portão solo não é uma [masmorra de clã](/wiki/03-Mechanics/Dungeons.md). Uma masmorra é um labirinto que um clã abre para um grupo, com um Senhor da guerra no fim; um portão solo é uma arena em que só você está, e ninguém mais pode entrar com você. Os dois têm regras, pagamentos e limites separados. A página dos Portões Galácticos também tem o **Chrono-Gate**, que não é um lugar para voar, mas o portão que abre o seu [Cache de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) para o reset: as peças dele se encontram com os mesmos giros.

## Em resumo {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Portões**: 6: o Chrono-Gate e 5 portões solo, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege e Omega Vault
- **Giro**: 100 Thulium por giro, e 1, 5, 10 ou 100 giros por vez
- **Chance de uma peça**: 13% por giro. O portão a que a peça pertence é escolhido ao acaso, e cada portão recebe 2,17% dos giros. Quando o Chrono-Gate está completo, a parte dele sai da roda, e os portões solo ficam com 2,17% cada um
- **Garantia**: Depois de 24 giros seguidos sem peça, a chance sobe a cada giro, e depois de 47 o giro seguinte sempre encontra uma. Uma peça de qualquer portão reinicia a contagem
- **Vidas**: 3 por tentativa; cada morte custa uma
- **Contagem regressiva**: 5 s antes de cada onda, também a primeira e a do chefe. Uma onda não tem cronômetro, nem uma partida
- **Arena**: Espaço aberto de 8.000 × 6.000 unidades sem rochas, e você está sozinho nele. Um mundo tem 16 delas, e quando todas estão ocupadas você não pode entrar
- **Alienígenas ao mesmo tempo**: No máximo 60 de uma onda estão vivos ao mesmo tempo, e 250 em uma onda opcional. O resto espera espaço
- **Chefes**: Um chefe não pode ser ferido por 3 s quando muda de fase
- **Limite de Thulium**: Um portão devolve no máximo 50% do Thulium que você gastou em giros. O resto é cortado, e o resultado diz quanto

<!-- solo-glance:end -->

## Encontrar peças de portão {#finding-gate-parts}

Abra a página dos **Portões Galácticos** e gire o Materializador de Energia. Cada giro é pago em Thulium e encontra no máximo uma peça, e a peça pertence a um dos seis portões, escolhido ao acaso. Você precisa de um número de peças de um portão para construí-lo, e as peças são suas até você usá-las. Um giro que não encontra peça não se perde: ele paga um prêmio ([abaixo](#a-spin-without-a-part)). Todo giro é cobrado, mesmo com o Chrono-Gate completo. Quando o Chrono-Gate está completo, a parte dele nos giros não encontra nada, e os portões solo mantêm a própria chance, então uma peça de um portão solo custa o mesmo com ou sem ele.

A tabela dá o custo de cada portão em peças e o que elas custam em média **com a garantia** (um giro é uma loteria, então um piloto sortudo paga menos e um azarado mais, até a mais longa sequência de giros que a garantia permite).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Portão | Peças para completá-lo | Chance de uma peça por giro | Giros em média | Thulium em média |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17% | 91 | 9.093 |
| **Alpha Rift** | 11 | 2,17% | 500 | 50.011 |
| **Beta Breach** | 26 | 2,17% | 1.182 | 118.208 |
| **Gamma Foundry** | 54 | 2,17% | 2.455 | 245.508 |
| **Delta Siege** | 87 | 2,17% | 3.955 | 395.541 |
| **Omega Vault** | 108 | 2,17% | 4.910 | 491.017 |

<!-- solo-parts:end -->

As peças do Chrono-Gate voltam a zero no reset, e você as encontra de novo a cada temporada. **As peças dos portões solo ficam**, e também a contagem da garantia e o registro do que você gastou em giros e do que os portões devolveram; o reset não leva nenhum deles ([Portões e o reset](#gates-and-the-wipe)).

### Um giro sem peça {#a-spin-without-a-part}

A maioria dos giros não encontra peça. Cada um deles paga um prêmio, escolhido pelas chances abaixo: munição laser do segundo multiplicador ou melhor, um lote de foguetes do segundo ou terceiro nível e, de vez em quando, um [item especial](/wiki/06-Items/Special-Items.md) ou um [contêiner](/wiki/06-Items/Containers.md). Um prêmio que não pode ser dado (você já tem o máximo daquele item especial, por exemplo) vira um lote de munição ou de foguetes pelo mesmo sorteio, então um giro nunca paga menos que a sua tabela. O prêmio vale claramente menos do que o giro custa: os portões são um ralo de Thulium.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Prêmio | Chance por giro |
| :--- | ---: |
| Um contêiner: Chroma Archive | 0,01% |
| Um item especial: Magic Hammer | 0,2% |
| Um item especial: Schematics | 0,2% |
| Um item especial: Philosopher's Stone | 0,2% |
| Um item especial: Forger's Seal | 0,2% |
| Um item especial: Workforce Contract | 0,2% |
| Um item especial: Tinkerer's Badge | 0,1% |
| Munição laser: Advanced Plasma ×75 | 12,88% |
| Munição laser: Antimatter Battery I ×62 | 8,59% |
| Munição laser: Ultra Core ×40 | 8,59% |
| Munição laser: Antimatter Battery II ×29 | 4,29% |
| Munição laser: Dark Matter Ammo I ×31 | 4,29% |
| Munição laser: Experimental Fusion Core ×17 | 2,15% |
| Munição laser: Dark Matter Ammo II ×17 | 2,15% |
| Foguetes: Lancet II ×4 | 8,59% |
| Foguetes: Rivet II ×4 | 8,59% |
| Foguetes: Ember II ×4 | 8,59% |
| Foguetes: Scatter II ×4 | 8,59% |
| Foguetes: Lancet III ×1 | 2,15% |
| Foguetes: Rivet III ×1 | 2,15% |
| Foguetes: Ember III ×1 | 2,15% |
| Foguetes: Scatter III ×1 | 2,15% |

<!-- solo-prizes:end -->

## Entrar {#going-in}

Você **constrói** um portão na página dos Portões Galácticos e **salta** para dentro pelo portal dele. Construir é feito pela estação, com a nave atracada: você não precisa estar voando. É preciso:

- as peças do portão: elas são tiradas **uma só vez, quando você o constrói**, e uma construção recusada não tira nada;
- nenhuma outra partida solo aberta: você tem uma partida por vez, e uma partida que você deixou é retomada pelo portal dela ou abandonada antes de você construir outro portão;
- o servidor principal (os servidores regionais não têm portões).

O portão construído fica no seu **setor-base** (`M-1`, `T-1` ou `G-1`, conforme a sua corporação) como um portal com o nome dele, e a página dos Portões Galácticos diz onde ele está. **Decole, voe até o portal e salte** por ele como por qualquer portal. É preciso haver uma fenda livre no seu mundo quando você entrar: cada mundo tem um número delas, e quando todas estão ocupadas você espera.

Você pousa sozinho no meio de uma arena vazia. Ninguém pode atacar você nela, e a Jump CPU e a Base CPU não funcionam.

## Como uma partida transcorre {#how-a-run-goes}

1. **Antes de cada onda há uma contagem regressiva**, também antes da primeira e antes da do chefe. Uma onda não tem cronômetro, nem a partida: ela leva o tempo que você precisar.
2. **Uma onda** aparece em um anel ao seu redor e voa até você, no ritmo do portão. Só vivem ao mesmo tempo tantos dela, e o resto espera espaço. Ela termina quando o último alienígena morre.
3. **O seu progresso é salvo depois de cada onda.** Se você sair, uma onda em andamento recomeça inteira quando você voltar.
4. **Uma onda opcional** é uma onda enorme de Seekers, e o Delta Siege e o Omega Vault têm uma cada. Durante a contagem regressiva dela você pode pulá-la: ela passa a contar como feita, e **não paga nada**. Se você a combater, as baixas dela pagam como as de qualquer onda.
5. **A última onda é o chefe.** Ele muda de fase conforme o casco cai, e não pode ser ferido por um instante a cada mudança. Quando o chefe morre, a partida está vencida, e a vitória é paga na hora.

**Vidas.** Uma morte custa uma vida e manda você para a sua base como qualquer outra morte; a partida espera por você, sem relógio correndo. Enquanto a partida está aberta e você está fora da arena, **o portal do seu portão fica no seu setor-base**, e um salto por ele leva você de volta à onda salva com as vidas que restam, como **Retomar**; ele não pede peças novas. Quando a sua última vida acaba, a tentativa termina, mas a partida fica aberta na última onda vencida, e entrar de novo devolve as suas vidas. **Sair**, um logoff ou uma troca de mundo pausa a partida sem custar uma vida. Um reinício do servidor também mantém a sua partida aberta. **Abandonar** desiste da partida: as peças dela se perdem, e os alienígenas que você matou são pagos como estão. **Retomar** só funciona a partir de uma nave em voo: depois de uma morte, o botão dele na tela de resultado espera, com uma linha que diz por quê, até você reaparecer. Uma nave que reaparece volta com o casco limitado; por isso, quando o seu casco está abaixo da metade, a tela de resultado avisa, e **Retomar** ainda assim leva você de volta do jeito que está. As naves de reparo da sua base reparam você dentro da aura delas.

Todo mundo enfrenta o mesmo portão: a força e o pagamento dos alienígenas não dependem do mundo em que você voa.

### As ondas {#the-waves}

Os alienígenas são os do jogo (Seeker, Phantasm, Bulwark, Goombah e Crystalys), feitos mais duros ou mais moles pelo portão. O tempo previsto é o que o portão é construído para levar com um piloto no nível inicial de Tecnologia laser ([Perícias do piloto](/wiki/03-Mechanics/Pilot-Skills.md)); um piloto que subiu a Tecnologia laser termina antes.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Portão | Ondas, a do chefe incluída | Alienígenas nas ondas | Chefe | Tempo previsto |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 a 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 a 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 a 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 a 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 a 60 min |

- **Delta Siege**: a onda 18 (250 Seeker) é opcional: você pode pulá-la enquanto a contagem regressiva dela corre, e ela não paga nada
- **Omega Vault**: a onda 17 (250 Seeker) é opcional: você pode pulá-la enquanto a contagem regressiva dela corre, e ela não paga nada; as ondas 22 a 24 são de elite, com ×1,5 de casco, escudo e dano

<!-- solo-waves:end -->

### Os chefes {#the-bosses}

Um chefe é a nave de um alienígena aumentada, com um casco, um escudo e uma rajada próprios, que nenhuma configuração do portão ou do mundo muda. Uma fase começa quando o casco do chefe cai até o número da tabela: o escudo dele pode ser reajustado, a rajada ou todo o dano dele muda, e ele pode iniciar um movimento. Todo movimento é anunciado: um círculo, um anel ou uma marca na sua nave mostra um instante antes de cair. Os alienígenas que um chefe chama não pagam nem soltam nada.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Chefe | Portão | Casco | Escudo | Rajada de laser |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330.000 | 530.000 | 5.700–7.000 |
| **Enhanced Bulwark** | Beta Breach | 690.000 | 170.000 | 4.500–5.500 |
| **Elite Crystalys** | Gamma Foundry | 620.000 | 250.000 | 3.800–4.700 |
| **Siege Construct** | Delta Siege | 1.150.000 | 1.730.000 | 3.400–4.200 |
| **Omega Guardian** | Omega Vault | 1.340.000 | 840.000 | 2.600–3.200 |

| Chefe | Fase | Casco restante | O que faz |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100% a 0% | Só atira. |
| **Enhanced Bulwark** | Shielded | 100% a 50% | O escudo dele é ajustado para ×4 do próprio do chefe. |
|  | Second attack | 50% a 0% | A rajada dele é ×1,3. Ele dispara 4 foguetes Dormant Lance contra você, de 61.000 cada, um a cada 0,5 s, em uma saraivada a cada 30 s. |
| **Elite Crystalys** | Elite | 100% a 50% | Só atira. |
|  | Reinforced | 50% a 0% | O escudo dele é ajustado para ×2 do próprio do chefe. A cada 10 min ele chama 10 Goombah, no máximo 10 vivos; não pagam nem soltam nada. |
| **Siege Construct** | Siege Construct | 100% a 0% | A cada 1 min ele faz cair 3 saraivadas de 8 meteoros, de 5.500 cada sobre tudo a até 420 unidades de onde caem, 50% deles mirados em você; cada círculo aparece 3 s antes de cair. Ele dispara 6 foguetes Dormant Lance contra você, de 9.000 cada, um a cada 0,5 s, em uma saraivada a cada 1 min. |
| **Omega Guardian** | Shield Fortress | 100% a 70% | O escudo dele é ajustado para ×1,5 do próprio do chefe. A cada 40 s ele chama 6 Bulwark, no máximo 12 vivos; não pagam nem soltam nada. |
|  | Swarm Protocol | 70% a 35% | A cada 25 s ele chama 12 Phantasm, no máximo 24 vivos; não pagam nem soltam nada. A cada 30 s uma explosão de 140.000 atinge tudo a até 700 unidades do chefe; o anel aparece 2 s antes de cair. |
|  | Overload | 35% a 0% | O escudo dele é ajustado para ×0,1 do próprio do chefe. Todo o dano dele é ×2,5. Depois de 2 min na fase, todo o dano dele é mais ×2. A cada 25 s uma explosão de 28.000 atinge tudo a até 700 unidades do chefe; o anel aparece 2 s antes de cair. |

<!-- solo-bosses:end -->

## O que uma vitória paga {#what-a-clear-pays}

Uma vitória paga a sua tabela **uma vez**, de uma só vez, no momento em que o chefe morre: os Créditos, o Thulium, a experiência e a honra, o minério, as placas e os Power Cores, e a munição. A experiência conta para os seus pontos PvE, como a de uma masmorra.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Portão | Créditos | Thulium | XP | Honra |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450.000 | 5.000 | 70.000 | 1.000 |
| **Beta Breach** | 1.500.000 | 12.000 | 180.000 | 2.500 |
| **Gamma Foundry** | 4.000.000 | 25.000 | 400.000 | 5.500 |
| **Delta Siege** | 8.000.000 | 40.000 | 800.000 | 10.000 |
| **Omega Vault** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; munição: Advanced Plasma ×20.000, Ultra Core ×5.000, Experimental Fusion Core ×20.000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; munição: Advanced Plasma ×50.000, Ultra Core ×20.000, Experimental Fusion Core ×30.000
- **Gamma Foundry**: Ship Fragment ×1.150, Nyxite ×1.000, Cataclysite ×900, Quorvium ×400, Power Core ×15; munição: Advanced Plasma ×30.000, Ultra Core ×60.000, Experimental Fusion Core ×50.000
- **Delta Siege**: Ship Fragment ×2.000, Nyxite ×1.750, Cataclysite ×1.500, Quorvium ×1.000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; munição: Advanced Plasma ×40.000, Ultra Core ×90.000, Experimental Fusion Core ×75.000
- **Omega Vault**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; munição: Advanced Plasma ×50.000, Ultra Core ×100.000, Experimental Fusion Core ×100.000

<!-- solo-pay:end -->

**O Thulium é cortado em um limite.** Os portões não podem devolver mais que uma parte do Thulium que você gastou em giros, contada sobre todos os seus portões e todos os seus giros (a parte está na lista do topo). O que uma vitória e os alienígenas dela pagariam acima disso é cortado, e a tela de resultado diz quanto. Créditos, experiência, honra, minério, placas e munição nunca são cortados.

### Os alienígenas {#the-aliens}

Todo alienígena que você mata em um portão paga com os números que tem no Alpha, em qualquer mundo em que você voe: nenhum multiplicador de mundo, nenhum booster e nenhum bônus Premium os muda. Uma onda paga pelos seus alienígenas **uma vez** por partida, por mais vezes que você saia e volte. O pagamento chega no fim de cada trecho da partida: quando você sai, morre, fica sem vidas, abandona ou vence. As baixas de um trecho ficam sem pagamento apenas no reset e em um reinício do servidor enquanto você está dentro (a sua partida continua aberta, mas as baixas desse trecho se perdem). As baixas de um portão não contam para mais nada: nem para as missões, nem para as estatísticas de baixas, nem para os contadores das conquistas, nem para o registro de baixas, nem para a experiência dos seus drones e P.E.T.s. A experiência que elas pagam, porém, conta para os seus pontos PvE, como a de uma vitória. O saque dos alienígenas chega com o pagamento, direto no seu inventário.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alienígena | Créditos | Thulium | XP | Honra |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1.000 | 4 | 100 | 2 |
| **Phantasm** | 3.000 | 12 | 300 | 6 |
| **Bulwark** | 5.000 | 25 | 800 | 10 |
| **Goombah** | 15.000 | 75 | 3.000 | 24 |
| **Crystalys** | 75.000 | 200 | 12.000 | 52 |

| Portão | Créditos | Thulium | XP | Honra |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540.000 | 2.160 | 54.000 | 1.080 |
| **Beta Breach** | 1.320.000 | 5.980 | 186.000 | 2.520 |
| **Gamma Foundry** | 3.000.000 | 13.300 | 522.000 | 4.616 |
| **Delta Siege** | 4.975.000 | 21.400 | 829.000 | 7.640 |
| **Omega Vault** | 6.875.000 | 29.000 | 1.160.000 | 10.100 |

<!-- solo-kills:end -->

## Desafios e conquistas {#challenges-and-achievements}

Dois desafios opcionais podem ser vencidos em qualquer vitória, e cada um paga uma conquista e **nenhum Thulium**. Uma vitória **sem morrer** é uma sem nenhuma morte em toda a partida, somando todas as vezes em que você entrou. Um **speedrun** é uma vitória dentro do menor tempo previsto do portão, contado pelo tempo que você passa dentro da arena. As outras seis conquistas são por vencer cada portão, e os cinco:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Fenda fechada** (Comum): Complete o Alpha Rift sozinho.
- **Brecha selada** (Incomum): Complete o Beta Breach sozinho.
- **Fundição desativada** (Raro): Complete a Gamma Foundry sozinho.
- **Cerco rompido** (Raro): Rompa o Delta Siege sozinho.
- **Cofre arrombado** (Épico): Arrombe o Omega Vault sozinho.
- **Guardião dos portões** (Lendário): Complete os cinco portões solo: Alpha, Beta, Gamma, Delta e Omega.
- **Intocável** (Raro): Complete um portão solo sem perder uma vida.
- **Contra o relógio** (Raro): Complete um portão solo em seu menor tempo ou menos: 10, 15, 25, 35 ou 50 minutos, de Alpha a Omega.

<!-- solo-achievements:end -->

## Itens de um portão {#items-from-a-gate}

O que um portão dá a você é **negociável**: o minério, as placas, os Power Cores, a munição e o saque dos alienígenas podem ser anunciados no [Leilão](/wiki/03-Mechanics/Auction.md) como um drop ou uma recompensa de missão, com as mesmas exceções de qualquer item. Os prêmios de um giro sem peça não são: eles vêm de um giro, não de um portão.

## Portões e o reset {#gates-and-the-wipe}

- **O reset encerra qualquer partida aberta** e devolve as peças dela. Uma partida não continua na temporada seguinte.
- **Mantidos no reset:** as peças dos cinco portões solo, a contagem da garantia e o registro do que você gastou em giros e do que os portões devolveram, então o limite do Thulium continua de temporada em temporada. As conquistas são suas para sempre.
- **Perdidas no reset:** as peças do Chrono-Gate, como antes. Os seus giros as compram de novo.
- **Excluir uma conta** exclui as peças, a contagem e o registro.
