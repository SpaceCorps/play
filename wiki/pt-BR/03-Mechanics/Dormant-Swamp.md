<!-- wiki-i18n source: a8a96edb9a5070f1 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; pântano; torre; torres; canhão; canhões -->

Há muito tempo, uma civilização avançada viveu no meio da galáxia. Ela construía em cristal preto arroxeado, com veios violeta que brilham, e por um motivo que ninguém conhece ruiu. O **Dormant Swamp** é o seu posto avançado, no canto superior esquerdo de `DS-4`. A partir do dia 11 da temporada ele se agita: canhões no centro atiram em toda nave que veem, as **Inert Masses** o guardam, e bem no meio dorme **o Unwakened**. É um lugar que os pilotos **ainda não devem visitar**. Sob camuflagem você pode voar até o Unwakened, e por enquanto nada mais pode ser feito lá: a base e seus canhões não podem ser danificados, nem entrados, nem abordados, nem usados para comerciar.

O pântano é também onde o [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md) aparece a partir do dia 11, e **Slumbering Voids** patrulham em volta dele. Os mesmos Voids vêm em ondas às [escavadeiras gigantes](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Os setores estão em [Setores de perigo](/wiki/01-General/Danger-Sectors.md).

## Em resumo {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Onde**: O canto superior esquerdo de `DS-4`: o meio fica em 5.000 / 5.000
- **Aparece**: Do dia 11 da temporada até o reset
- **A zona**: 4.300 unidades em volta do meio: o mais longe que os canhões alcançam, e o lugar que ninguém deve visitar ainda
- **O aviso**: Uma nave que cruza o anel a 4.800 unidades do meio recebe uma linha do Sistema
- **Camuflagem**: Nenhum canhão vê jamais uma nave camuflada, nem uma dentro da janela de um EMP
- **Os alienígenas**: 5 Inert Masses ficam a até 2.400 unidades do meio. O Unwakened dorme no meio. 2 Slumbering Voids patrulham entre 4.600 e 6.500 unidades do meio.
- **O Enxame Dormant**: Ele aparece em 9.417 / 6.606, a 4.700 unidades do meio e fora da zona
- **Rochas**: Nenhum asteroide fica a menos de 4.900 unidades do meio

<!-- swamp-glance:end -->

## Os canhões {#the-guns}

As torres do pântano atiram na **nave mais próxima que conseguem ver** dentro do seu alcance, e em nenhuma outra: a zona é o círculo que a mais distante delas alcança. Elas não são entidades de nenhum tipo: não têm pontos de vida, não podem ser alvo, e nada que você atire nelas faz efeito. Os tiros delas são reais, e o mundo escala o dano deles como escala a arma de qualquer alienígena.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Dano de um tiro, em cada mundo:

| Canhão | Local | Atira a cada | Alcance (unidades) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Torre de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 2 s | 3.640 | 75.000 | 112.500 | 150.000 |
| Torre de [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 5 s | 1.080 | 50.000 | 75.000 | 100.000 |
| Torre laser × 2 | 3.600 / 5.200; 6.400 / 5.200 | 1 s | 2.500 | 45.000–55.000 | 67.500–82.500 | 90.000–110.000 |

- Um foguete é disparado a 90% do seu alcance, para que chegue; uma torre laser atira uma vez por segundo, e o dano dela é sorteado na faixa mostrada.
- Um N.I.K.E. tem 35% de penetração de escudo, descontada da absorção de um escudo.
- Um N.U.K.E. explode num raio de 900 unidades, mais forte no centro.

<!-- swamp-guns:end -->

- **Nada alcança fora da zona,** e dentro dela uma nave é destruída em segundos: quanto mais perto do meio, mais canhões se juntam, e nem a Wraith com os melhores escudos aguenta.
- **Camuflagem deixa você entrar.** Nenhuma torre vê jamais uma nave camuflada, nem uma dentro da janela de um EMP, a nenhuma distância. Uma explosão mirada numa nave visível que estoura perto de uma camuflada ainda a fere e encerra a camuflagem dela.
- **Elas atiram só em pilotos,** nunca em alienígenas, pilotos de corporação ou no enxame, e a proteção de uma nave que acabou de voltar de uma destruição vale também contra elas.
- **O anel de aviso.** Uma nave que cruza o anel fora da zona recebe uma linha do Sistema: as torres atiram em toda nave que veem, e algo dorme no meio. Ela só é avisada de novo depois de sair do anel e voltar.
- **Sair.** Se você for destruído lá e voltar no local, ou entrar no jogo dentro da zona, é colocado fora. Um rumo que você clica é desviado em volta da zona, e um aviso alerta quando o lugar clicado fica dentro.

## Os alienígenas {#the-aliens}

Três alienígenas da civilização perdida vivem aqui, cada um com seus próprios números. Eles pagam como o chefe de um enxame: **pelo dano causado**, a todo piloto que fez pelo menos a parcela indicada em [Enxames](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), e a caixa vai para o piloto que causou mais dano. Os abates deles somam aos seus pontos PvE de patente como os de uma nave de enxame, em proporção ao pagamento ([Patentes](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). O escudo de cada um absorve 80% de cada acerto enquanto durar ([Escudos](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** O caçador esguio, o alienígena mais rápido do jogo (tão rápido quanto uma Storm com Afterburner III). Alguns patrulham sempre os arredores do pântano, e outros vêm em ondas às escavadeiras. É agressivo, caça o piloto mais próximo que consegue ver e nunca vê uma nave camuflada.
- **Inert Mass.** Um casco morto com rachaduras violeta, do tamanho de uma pequena estação. Elas ficam a uma distância fixa do meio do pântano e por enquanto não o deixam. Dispara **Dormant Lances**: foguetes guiados de alcance enorme que seguem uma nave até ela se camuflar, abrir uma janela de EMP, entrar num anel seguro, saltar ou morrer. É mais rápida que qualquer nave, então só essas interrupções ajudam.
- **O Unwakened.** Um monólito que dorme no meio do pântano, a maior coisa de qualquer mapa, tão lento que nunca alcança uma nave. Não dispara nada, mas toda nave dentro da sua aura queima, **camuflada ou não**. Ele é **imune**: tiros e foguetes acertam e não fazem nada, a janela de alvo mostra as barras cheias e a palavra Imune. Um evento futuro permitirá combatê-lo; as recompensas dele abaixo estão escritas e ainda não podem ser ganhas.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrulham entre 4.600 e 6.500 unidades do meio do pântano; um que é destruído volta 1 h depois. As ondas de uma escavadeira trazem mais do mesmo alienígena.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 25.000 | 37.500 | 50.000 |
| Escudo | 150.000 | 225.000 | 300.000 |
| Absorção do escudo | 80% | 80% | 80% |
| Dano dos lasers (uma salva por segundo) | 3.000 | 4.500 | 6.000 |
| Velocidade | 400 | 400 | 400 |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | 2.500 | 2.500 | 2.500 |
| Créditos | 23.000 | 46.000 | 69.000 |
| Thulium | 60 | 120 | 180 |
| Experiência (XP) | 3.600 | 7.200 | 10.800 |
| Honra | 16 | 32 | 48 |
| Pontos PvE por abate | 10 | 10 | 10 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Um entre Ultra Core e Experimental Fusion Core, escolhido ao acaso | 60% | 30–60 |
| Um dos 4 [foguetes](/wiki/06-Items/Rockets.md) Épicos, escolhido ao acaso | 40% | 1–3 |

### Inert Mass

5 Inert Masses ficam a até 2.400 unidades do meio; uma que é destruída volta 1 h depois. Dispara a cada 6 s uma [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) guiada na nave mais próxima que consegue ver: velocidade 750, voo de 5.250 unidades, 40% de penetração.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 250.000 | 375.000 | 500.000 |
| Escudo | 100.000 | 150.000 | 200.000 |
| Absorção do escudo | 80% | 80% | 80% |
| Dano de cada Dormant Lance | 5.000–8.000 | 7.500–12.000 | 10.000–16.000 |
| Velocidade | 60 | 60 | 60 |
| Alcance dos foguetes | 5.000 | 5.000 | 5.000 |
| Raio de agressão | 5.000 | 5.000 | 5.000 |
| Créditos | 125.000 | 250.000 | 375.000 |
| Thulium | 335 | 670 | 1.005 |
| Experiência (XP) | 20.200 | 40.400 | 60.600 |
| Honra | 88 | 176 | 264 |
| Pontos PvE por abate | 15 | 15 | 15 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Ultra Core e Experimental Fusion Core, divididos igualmente | 100% | 400–800 no total |
| Um dos 4 [foguetes](/wiki/06-Items/Rockets.md) Épicos, escolhido ao acaso | 100% | 20–40 |
| N.I.K.E. | 5% | 1–2 |
| Dark Matter | 5% | 1–3 |
| Ancient Control Unit | 10% | 1 |
| Power Core | 25% | 1–2 |

### The Unwakened

Há um, no meio do pântano e em nenhum outro lugar; ele volta 24 h depois de ser destruído. É **imune** até que uma missão futura desligue a marca: tiros e foguetes o acertam e não fazem nada. As recompensas dele estão escritas e ainda não podem ser ganhas.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 10.000.000 | 15.000.000 | 20.000.000 |
| Escudo | 10.000.000 | 15.000.000 | 20.000.000 |
| Absorção do escudo | 80% | 80% | 80% |
| Dano da aura por segundo, a toda nave dentro | 75.000 | 112.500 | 150.000 |
| Raio da aura | 700 | 700 | 700 |
| Velocidade | 10 | 10 | 10 |
| Raio de agressão | 3.000 | 3.000 | 3.000 |
| Créditos | 7.500.000 | 15.000.000 | 22.500.000 |
| Thulium | 20.000 | 40.000 | 60.000 |
| Experiência (XP) | 1.200.000 | 2.400.000 | 3.600.000 |
| Honra | 5.200 | 10.400 | 15.600 |
| Pontos PvE por abate | 112 | 112 | 112 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Ultra Core e Experimental Fusion Core, divididos igualmente | 100% | 10.000–15.000 no total |
| Um dos 4 [foguetes](/wiki/06-Items/Rockets.md) Épicos, escolhido ao acaso | 100% | 500–800 |
| N.I.K.E. | 100% | 20–30 |
| N.U.K.E. | 100% | 5–10 |
| Dark Matter | 100% | 40–60 |
| Ancient Control Unit | 100% | 10–20 |
| Power Core | 100% | 100–200 |

<!-- swamp-members:end -->

## O que fazer aqui {#what-to-do-here}

- **Olhe, não toque.** O pântano é para depois. O único conteúdo que você alcança sem camuflagem está fora da zona: os Voids de patrulha, num anel em volta da zona, são a primeira linha do pântano e o lugar onde um grupo pode lutar sem os canhões.
- **Combata os Voids com penetração.** O escudo grande de um Void absorve 80% de um acerto e quase não importa: o casco atrás dele é pequeno. Quanto mais penetração de escudo seus lasers tiverem, mais cedo ele cai ([Lasers e munição](/wiki/06-Items/Lasers.md)).
- **Fique longe das Lances.** Uma Inert Mass enxerga longe e de uma Lance não se escapa: quebre a prisão dela com uma camuflagem, um EMP, um anel seguro ou um salto, ou saia do alcance. Uma Mass é uma luta longa até para um grupo grande das naves mais fortes.
- **O Enxame Dormant** agora aparece logo fora da zona, então um grupo pode esperá-lo sem os canhões. Veja [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

## Onde ler mais {#where-to-read-more}

- [Setores de perigo](/wiki/01-General/Danger-Sectors.md): o que mudou no dia 11.
- [Escavadeira gigante](/wiki/03-Mechanics/Giant-Excavator.md): as ondas de Slumbering Voids e o que elas guardam.
- [Enxames](/wiki/05-Swarms/Swarms.md) e [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md): como paga o abate de um chefe.
- [Foguetes](/wiki/06-Items/Rockets.md#the-craft-only-rockets): o N.I.K.E. e o N.U.K.E. que a torre dispara.
- [Buraco negro](/wiki/03-Mechanics/Black-Hole.md): o outro perigo de `DS-4`.
- [Caixas de carga](/wiki/03-Mechanics/Cargo.md): as caixas que os alienígenas soltam.
