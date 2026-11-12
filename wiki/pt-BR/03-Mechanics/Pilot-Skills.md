<!-- wiki-i18n source: 0d92c80e748fc9b8 -->
<!-- wiki-i18n title: Perícias do piloto -->
# Perícias do piloto {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; perícias; perícias do piloto; árvore de perícias; experiência; subir de nível; estatísticas; atributos; massa; tenacidade; reflexos; instinto; tecnologia laser; tecnologia de foguetes; antimatéria; pontaria; sabotagem; evasão; tática; tecnologia de radiação; teoria de propulsores; ciência; extração; logística; fabricação; comércio; limite por hora; porão -->

O seu piloto tem uma **árvore de perícias**: um conjunto de estatísticas que sobem de nível pelo que você faz. Lute, e sua Tecnologia laser e sua Tenacidade sobem; colete do seu Skylab, e sua Extração sobe. Cada nível dá um pequeno bônus permanente a algo que você já faz, e nada é gasto nem escolhido: não há pontos para distribuir nem nada para refazer. Você sobe de nível o que usa.

A árvore é **sua**, não de uma nave. Toda nave que você pilota tem os seus níveis, uma nave que você comprar amanhã também, e os níveis se mantêm em todos os resets ([o que se mantém](#what-is-kept)).

Um piloto novo não está com força total. No nível 1, um laser e um foguete causam menos dano do que as páginas de itens indicam, e a Tecnologia laser e a Tecnologia de foguetes os levam além dos números indicados conforme sobem. Todo número das páginas de itens é o do próprio item, antes das suas perícias.

## Em resumo {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Estatísticas**: 19 estatísticas: 4 atributos e 15 perícias em 5 grupos
- **Níveis**: De 1 a 100. Todo piloto começa toda estatística no nível 1, e não há nada para gastar nem para refazer
- **Custo de um nível**: 40 XP do nível 1 ao 2, 875 XP do nível 50 ao 51, 19.157 XP do nível 99 ao 100; 313.258 XP no total
- **O que um nível dá**: Um bônus cresce em linha reta do valor dele no nível 1 ao valor dele no nível 100. Nada tem limite
- **O seu laser no nível 1**: Causa 100% do dano dele e acerta 80% das vezes, ou seja, 80% do dano que as páginas de itens indicam
- **O seu foguete no nível 1**: Causa 100% do dano dele e falha ao acender 10% das vezes, ou seja, 90% do dano que as páginas de itens indicam
- **Esquiva**: A nave de todo piloto esquiva 3% dos golpes que podem ser esquivados, antes de qualquer perícia ou formação somar
- **Nível de casco**: A raridade da sua nave o define, como mostra a tabela abaixo. O tamanho do seu porão e o XP da Massa o acompanham
- **Porão**: Conta as unidades de recursos que você coleta depois de decolar, até o tamanho que o seu nível de casco lhe dá. Está cheio a partir de 90% disso, e um porão cheio faz a Massa pagar ×1,5. Nada é recusado
- **Limite suave por hora**: A maioria das estatísticas paga o XP completo só até um limite por hora, contado na unidade própria da estatística ao longo da hora do relógio UTC. Acima dele, um evento paga 25% do XP dele
- **Treino**: O XP de uma perícia também paga 10% de si ao atributo dela. Um atributo no nível 100 treina as perícias dele 25% mais rápido que no nível 1

| Nível de casco | Raridade da nave | Tamanho do porão |
| :--- | :--- | ---: |
| 1 | Inferior / Comum | 60 |
| 2 | Incomum | 120 |
| 3 | Raro | 250 |
| 4 | Épico | 500 |
| 5 | Mítico / Lendário / Eterno | 1.000 |

<!-- skills-glance:end -->

## As estatísticas {#the-stats}

As estatísticas são de dois tipos. Os **atributos** (Massa, Tenacidade, Reflexos e Instinto) são o básico de um piloto. As **perícias** estão em cinco grupos, e cada uma é regida por um atributo, que as tabelas nomeiam entre parênteses: o XP de uma perícia também alimenta o seu atributo, e um atributo alto treina mais rápido as suas perícias ([como o XP é pago](#how-xp-is-paid)). Os nomes são os da página Perícias do piloto do jogo.

As tabelas dão cada bônus no nível 1 e no último nível; entre os dois, o bônus cresce em linha reta. Um **fator** multiplica um número: um acima de 1 o aumenta, um abaixo de 1 o diminui. A maioria dos bônus muda um número da sua nave, e a dica de um número que uma perícia mexeu tem uma linha que diz quanto dele vem das suas perícias.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Atributos {#attributes}

| Estatística | O que muda | Nível 1 | Nível 100 |
| :--- | :--- | ---: | ---: |
| **Massa** | Casco | +0% | +20% |
| **Tenacidade** | Dano sofrido | ×1 | ×0,92 |
| **Reflexos** | Velocidade de recarga das habilidades | ×1 | ×1,1 |
| **Instinto** | Chance de cada linha de saque | +0 pontos | +7,5 pontos |
|  | Orvium e Velkonite dos coletores | ×1 | ×1,5 |

### Armas {#weapons}

| Estatística | O que muda | Nível 1 | Nível 100 |
| :--- | :--- | ---: | ---: |
| **Tecnologia laser** (Reflexos) | Dano do laser | ×1 | ×1,3 |
|  | Chance de uma rajada de laser acertar | 80% | 89% |
| **Tecnologia de foguetes** (Reflexos) | Dano do foguete | ×1 | ×1,3 |
|  | Chance de um foguete falhar ao acender | 10% | 1% |
| **Antimatéria** (Instinto) | Dark Matter das coletas | ×1 | ×1,25 |

### Combate {#combat}

| Estatística | O que muda | Nível 1 | Nível 100 |
| :--- | :--- | ---: | ---: |
| **Pontaria** (Reflexos) | Alcance do lançamento de uma Mine | ×1 | ×1,15 |
|  | Velocidade de uma Mine lançada | ×1 | ×1,15 |
| **Sabotagem** (Reflexos) | Dano de venenos e Mines | ×1 | ×1,3 |
|  | Duração dos venenos | ×1 | ×1,2 |
| **Evasão** (Reflexos) | Chance de esquivar de um golpe, somada à da própria nave | 0% | 15% |
| **Tática** (Reflexos) | Duração das habilidades | ×1 | ×1,2 |
| **Absorção de escudo** (Tenacidade) | Absorção dos seus escudos | +0 pontos | +5 pontos |

### Controle da nave {#ship-control}

| Estatística | O que muda | Nível 1 | Nível 100 |
| :--- | :--- | ---: | ---: |
| **Tecnologia de radiação** (Tenacidade) | Dose de radiação | ×1 | ×0,4 |
| **Teoria de propulsores** (Massa) | Velocidade | +0% | +10% |
| **Ciência** (Instinto) | Ciência por unidade de combustível | ×1 | ×1,25 |

### Skylab

| Estatística | O que muda | Nível 1 | Nível 100 |
| :--- | :--- | ---: | ---: |
| **Extração** (Instinto) | O que o Skylab produz | ×1 | ×1,3 |
| **Logística** (Massa) | O que o banco do Depósito de recursos guarda | ×1 | ×1,4 |
| **Fabricação** (Reflexos) | Tempo de uma criação | ×1 | ×0,65 |

### Comércio {#trading}

| Estatística | O que muda | Nível 1 | Nível 100 |
| :--- | :--- | ---: | ---: |
| **Comércio** (Instinto) | Preços da Loja | ×1 | ×0,85 |
|  | O que a Loja paga na recompra | ×1 | ×1,1 |
|  | Depósito de um anúncio no Leilão | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Onde você sente {#where-you-feel-it}

- **Lasers.** A Tecnologia laser muda o dano de cada rajada e a chance de ela acertar; uma rajada que erra mostra um “Miss” flutuante e gasta a munição do mesmo jeito ([Combate](/wiki/03-Mechanics/Combat.md#laser-tech)). O alcance dos seus lasers é o da sua nave: a Pontaria sobe com os seus acertos com munição diferente da simples x1, mas só age sobre as Mines (abaixo).
- **Foguetes.** A Tecnologia de foguetes muda o dano de cada foguete e a chance de um falhar ao acender ([Tecnologia de foguetes](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Levar golpes.** A Tenacidade tira uma parte de cada golpe que você leva, a Evasão aumenta a chance de um acerto direto não fazer nada e a Absorção de escudo aumenta a parte de um acerto que os seus escudos recebem ([Combate](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). A Massa aumenta o seu casco.
- **Habilidades.** Os Reflexos encurtam o tempo de recarga das suas habilidades e a Tática as faz durar mais ([Habilidades](/wiki/03-Mechanics/Abilities.md#pilot-skills)). A Sabotagem fortalece os venenos.
- **Mines.** A Sabotagem aumenta o dano de uma Mine, e a Pontaria a lança mais rápido e mais longe ([Extras](/wiki/06-Items/Extras.md#mine)).
- **Velocidade.** A Teoria de propulsores soma à sua velocidade, além dos motores e de um Afterburner ([Velocidade](/wiki/03-Mechanics/Speed.md)).
- **Coletas.** O Instinto aumenta a chance de cada linha de saque, como faz um Loot Luck Booster, e os dois se somam; a Antimatéria aumenta a Dark Matter que você coleta ([Carga](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Radiação.** A Tecnologia de radiação reduz a dose do buraco negro, dos círculos das escavadeiras, dos pulsares e da aura dos Unwakened ([Buraco negro](/wiki/03-Mechanics/Black-Hole.md)).
- **Em casa.** A Extração e a Logística mudam o que o [Skylab](/wiki/03-Mechanics/Skylab.md) produz e guarda, o Instinto aumenta os seus dois coletores, a Fabricação encurta as criações da Montagem, a Ciência enche mais rápido o Centro de [Pesquisa](/wiki/03-Mechanics/Research.md), e o Comércio baixa os preços da Loja, aumenta o que ela paga na recompra e baixa o depósito de um anúncio no [Leilão](/wiki/03-Mechanics/Auction.md).

## Como o XP é pago {#how-xp-is-paid}

O servidor paga XP pelo que você faz, onde quer que você voe, nesta ordem:

1. **A regra antifarm.** Um acerto de ou em um colega de corporação ou de grupo não paga nada, e nada paga também o que é feito a uma nave em uma zona segura ou sob o abrigo de uma reaparição, ou por ela. Os segundos de Massa, do casco baixo da Tenacidade e da Teoria de propulsores só contam enquanto a sua nave está viva, fora de um abrigo, e você deu uma ordem no último minuto: uma nave estacionada ao ar livre não ganha nada.
2. **O limite suave por hora.** Uma estatística com limite paga o XP completo até ele e uma parte acima, contada na unidade própria da estatística (os tiros que você dá, os comandos que você manda, o XP que ela ganhou) ao longo da hora do relógio UTC. Um novo login não reabre a janela, e os números estão na lista acima e na tabela abaixo.
3. **Velocidade de treino.** O atributo que rege uma perícia aumenta o XP que a perícia ganha, mais a cada nível do atributo (o limite é contado antes disso, então o limite restringe a atividade e não a velocidade).
4. **A parte do atributo.** A perícia recebe o XP, e o seu atributo recebe uma parte dele, que nunca é limitada nem acelerada.

A tabela lista o que paga XP, estatística por estatística. O XP é por cada unidade do que está nomeado na segunda coluna.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Estatística | O que paga XP | XP | Limite suave por hora |
| :--- | :--- | ---: | ---: |
| **Massa** | A cada 10 s de voo com uma ordem dada nos últimos 1 min: o nível de casco da nave, mais 0,2 por cada placa instalada, ×1,5 com o porão cheio | 1 | Nenhum |
| **Tenacidade** | A cada 1% do seu casco máximo perdido para um inimigo ou um perigo | 1 | 300 XP por hora |
|  | A cada 10 s abaixo de 25% do seu casco máximo | 5 |  |
| **Reflexos** | A cada comando que o jogo aceita: uma habilidade, um extra, um novo alvo, uma coleta, uma criação, uma troca de formação, um foguete ou um salto. Um novo alvo paga no máximo uma vez em 4 s, uma coleta no máximo uma vez em 1 s e um foguete no máximo uma vez em 1 s | 1 | 600 comandos por hora |
| **Instinto** | A cada caixa de carga que você coleta, à mão ou com um Retriever | 2 | 600 XP por hora |
|  | A cada item de uma recompensa de missão que você resgata | 10 |  |
|  | A primeira vez que você coleta um item de qualidade Raro ou melhor (uma vez por item, para sempre) | 25 |  |
| **Tecnologia laser** (Reflexos) | A cada rajada que você dispara | 0,1 | 1.800 tiros por hora |
|  | A cada rajada que acerta uma nave | 0,1 |  |
| **Tecnologia de foguetes** (Reflexos) | A cada foguete que você lança | 0,15 | 130 foguetes por hora |
|  | A cada foguete que acerta uma nave (uma vez por foguete, por mais naves que a explosão atinja) | 0,3 |  |
| **Antimatéria** (Instinto) | A cada unidade de Dark Matter que você recebe numa coleta | 2,2 | Nenhum |
| **Pontaria** (Reflexos) | A cada acerto de uma rajada disparada com munição diferente da simples x1 (×1,5 nos primeiros 10 min de cada tipo de munição em uma hora do relógio) | 0,1 | 3.000 acertos por hora |
|  | A cada acerto de uma Mine, e a cada segundo que um inimigo passa na sua Energetic Wall | 0,1 |  |
| **Sabotagem** (Reflexos) | A cada acerto de uma Mine, e a cada segundo que um inimigo passa na sua Energetic Wall | 0,5 | 1.200 XP por hora |
|  | A cada segundo em que um veneno seu age sobre um inimigo | 0,05 |  |
| **Evasão** (Reflexos) | A cada ataque hostil contra você que erra ou é esquivado | 1 | 600 XP por hora |
| **Tática** (Reflexos) | A cada habilidade que você aciona com um hostil ao alcance do laser | 2 | 600 XP por hora |
| **Absorção de escudo** (Tenacidade) | A cada 1% do seu escudo máximo consumido por acertos de inimigos | 0,1 | 300 XP por hora |
| **Tecnologia de radiação** (Tenacidade) | A cada segundo dentro de uma faixa de radiação | 0,2 | Nenhum |
|  | A cada 1% do seu casco máximo que a radiação tira | 1 |  |
| **Teoria de propulsores** (Massa) | A cada segundo voado acima de 80% da velocidade da sua nave, o dobro sob um Afterburner | 0,1 | Nenhum |
| **Ciência** (Instinto) | A cada unidade de ciência que o Centro de Pesquisa queima | 0,1 | Nenhum |
|  | A cada tecnologia que você conclui | 50 |  |
| **Extração** (Instinto) | A cada unidade de recurso que o seu Skylab produz, paga na coleta | 0,1 | Nenhum |
| **Logística** (Massa) | A cada unidade de recurso que você deposita no banco do Skylab | 0,05 | Nenhum |
| **Fabricação** (Reflexos) | A cada segundo de tempo de criação que você conclui, pago na coleta | 0,1 | Nenhum |
| **Comércio** (Instinto) | A cada negociação no Leilão ou na Loja, contada como o logaritmo decimal de 1 mais o valor dela em Créditos (um Thulium vale o que o Leilão o avalia) | 2 | 600 XP por hora |

<!-- skills-xp:end -->

Enquanto você voa, a tela de voo mostra o XP que você ganha em linhas curtas, reunidas a cada poucos segundos, e um banner avisa quando uma estatística sobe de nível e o que mudou (o Registro do jogo guarda uma linha). Uma estatística que ganha o seu primeiro XP é anunciada uma vez. As dicas dos números que as perícias mexeram também dizem isso, em uma linha de Piloto própria, e o bloco de Dano do hangar deixa as perícias de fora e diz isso: elas valem quando você atira.

## Subir de nível {#levelling-up}

Um nível custa mais XP que o anterior, por uma proporção fixa, então os primeiros níveis vêm rápido e os últimos demoram. Toda estatística tem a mesma curva. O bônus que você tem em um nível é o mesmo para todo piloto: só a velocidade com que você o alcança depende do que você faz.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Nível | XP do nível | XP no total desde o nível 1 | Parte de cada bônus |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01% |
| 10 | 66 | 468 | 9,09% |
| 25 | 170 | 2.174 | 24,24% |
| 50 | 822 | 12.851 | 49,49% |
| 75 | 3.968 | 64.397 | 74,75% |
| 100 | 19.157 | 313.258 | 100% |

<!-- skills-curve:end -->

## A página Perícias do piloto {#the-pilot-skills-page}

A página **Perícias do piloto** é uma página da estação, com uma linha própria na barra lateral. É uma folha compacta de toda a árvore: os atributos e os cinco grupos de perícias ficam lado a lado em colunas (três em uma tela larga, menos em uma estreita), com uma linha por estatística, o seu nível na borda direita e uma barra de XP fina embaixo. Uma estatística que ainda não ganhou XP fica cinza, com um traço no lugar do nível. Deixe o ponteiro sobre uma linha para ver o que a estatística faz, qual atributo a rege ou quais perícias ela treina, o seu XP e o que a faz crescer. Clique em uma linha para abrir os detalhes dela embaixo da sua fileira de colunas: as mesmas palavras, a barra de XP e um controle deslizante para pré-visualizar qualquer nível do 1 ao último, com uma pequena tabela do que a estatística muda no nível 1, no seu nível atual, no nível pré-visualizado e no último nível. Só uma estatística fica aberta por vez; clique de novo na linha, use o botão de fechar ou pressione Esc para guardá-la. A linha da barra lateral ganha um selo quando uma estatística subiu de nível desde a última vez que você abriu a página, e um cartão da janela de Boosters resume o que as suas perícias mudam.

Em voo, a mesma folha é a janela **Perícias do piloto**. Abra-a com o botão Perícias do piloto da barra de ferramentas (em uma tela larga) ou com a sua tecla, K por padrão (Configurações, Controles). É uma janela como as outras: mova-a, redimensione-a, e ela lembra o seu lugar e se estava aberta. Ela só mostra as suas perícias: os níveis avançam conforme chegam as linhas de XP do voo, e um clique em uma linha abre os mesmos detalhes dentro da janela.

## O que se mantém {#what-is-kept}

- **Em todos os resets.** A árvore faz parte da sua conta: um reset não muda nenhum nível nem XP, e o Cache de Transporte não tem nada a ver com ela ([O que você mantém](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **Nos servidores regionais.** O XP que você ganha voando em Singapore ou US East é somado às suas perícias quando você volta para casa, inclusive de uma estatística que você usou ali pela primeira vez, e o limite por hora que você gastou ali vai com você. A página Perícias do piloto de um piloto que está voando ali lê os números do servidor regional, com o XP que a nave dele ganhou desde o último salvamento.
- **Até a conta ser excluída.** Excluir uma conta exclui os seus níveis.

Os bônus não têm outro teto além do último nível: um piloto que subiu tudo é tão forte quanto as tabelas dizem.
