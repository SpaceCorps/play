<!-- wiki-i18n source: 615b51aa98d6a27d -->
<!-- wiki-i18n title: Foguetes -->
# Foguetes {#rockets}

Os foguetes são uma segunda arma ao lado dos seus lasers: um disparo a cada poucos segundos que bate muito mais forte que uma rajada de laser. Doze foguetes em quatro tipos, três raridades cada, mais dois que só a Montagem fabrica, e **um único temporizador de recarga de 5 segundos que todos compartilham**, qualquer que você dispare. Os foguetes Comuns e Raros são comprados com **créditos**; os quatro foguetes Épicos são comprados com **Thulium**. Uma [formação de drones](/wiki/03-Mechanics/Formations.md) pode aumentar o dano de um foguete e alongar ou encurtar esse temporizador: veja [Formações de drones e foguetes](#drone-formations-and-rockets).

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## Os quatro tipos {#the-four-kinds}

| | Alvo único: atinge uma nave | Explosão em área: explode e fere tudo por perto |
| :--- | :--- | :--- |
| **Guiado**: trava no alvo que você selecionou e o persegue | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Reto**: voa em direção ao seu cursor | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Cada tipo é uma **família**, com o nome do seu foguete comum, e a raridade é um numeral romano: **Lancet I**, **Lancet II** e **Lancet III** são o foguete guiado de alvo único Comum, Raro e Épico, e as famílias Rivet, Ember e Scatter seguem o mesmo padrão. O código de um foguete no seu bloco do seletor de foguetes e no hangar é formado pelas três letras da família e pelo numeral (LNC II, RVT III, EMB I, SCT II); os dois foguetes que só a Montagem fabrica mantêm nome e código (N.U.K.E., NUK; N.I.K.E., NIK).

- Os foguetes **guiados** precisam de um alvo selecionado dentro do **alcance de travamento** quando saem. Eles o perseguem com uma taxa de curva limitada, então uma nave rápida e distante pode escapar de um foguete barato. Se o alvo morre, sai ou chega a uma zona segura, o foguete continua voando reto e não escolhe outro.
- Os foguetes **retos** não precisam de alvo e ignoram o que você selecionou: eles sempre voam em direção ao seu **cursor**, ao ponto sob ele na visão de voo. **Clique no slot de um foguete reto para armá-lo** (o slot ganha uma moldura branca e uma mira, e o cursor do mouse vira uma mira sobre o espaço), depois **clique no espaço**: o foguete voa em direção ao ponto em que você clicou e a sua nave fica onde está. Esc, um clique direito ou o mesmo slot de novo o solta. Se os foguetes ainda estão recarregando, o clique apenas avisa isso e o foguete continua armado. As teclas numéricas e **Disparar foguete** disparam na hora em direção ao último ponto que o cursor teve na visão de voo; antes de o cursor ter passado por ela, eles voam para onde a sua nave **aponta**. Eles voam reto, então uma nave que cruza em velocidade pode desviar deles.
- Um foguete de **alvo único** atinge a primeira nave que puder atingir (um guiado, só o alvo dele). Um foguete de **explosão em área** explode ao lado da primeira nave que encontra, no ponto para onde você o apontou, ou onde o voo dele termina, e fere toda nave dentro do seu **raio da explosão**: dano total no centro, menos em direção à borda. O anel que a explosão desenha no mapa é o alcance exato dela.

## Os doze foguetes {#the-twelve-rockets}

Cada foguete tem **o seu próprio dano, sorteado quando você o dispara**: entre **80% e 100%** do número máximo dele, e a tabela mostra o menor e o maior. Ele não depende da sua nave, dos seus lasers, dos seus Damage Amps, dos seus boosters, da sua munição nem dos seus drones, e um foguete nunca causa crítico. Só uma **formação de drones** o muda: a tabela aqui dá o dano sem formação (veja [Formações de drones e foguetes](#drone-formations-and-rockets)). Um foguete de alvo único causa o dano sorteado à nave que atinge; uma explosão sorteia uma vez só e o causa a **toda nave dentro dela**, o número inteiro no centro e menos em direção à borda. A *penetração de escudo* é descontada da absorção do seu alvo naquele acerto (a absorção de uma nave é a parte de um impacto que os escudos dela recebem, veja [Mecânica dos escudos](/wiki/03-Mechanics/Shields.md#shield-penetration)): os 35% de um Lancet III deixam os escudos de uma nave com 80% com 45% do impacto e mandam os outros 55% para o casco. Os foguetes de explosão em área não têm penetração.

| Nome | Tipo | Raridade | Dano | Penetração de escudo | Raio da explosão | Alcance de travamento | Alcance | Velocidade | Preço | Máximo que você carrega |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guiado, alvo único | Comum | 1.600–2.000 | 10% | – | 700 | 1.040 | 520 | 500 créditos | 5.000 |
| **Lancet II** | Guiado, alvo único | Raro | 3.200–4.000 | 25% | – | 1.000 | 1.584 | 660 | 800 créditos | 2.000 |
| **Lancet III** | Guiado, alvo único | Épico | 4.800–6.000 | 35% | – | 1.300 | 2.296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Reto, alvo único | Comum | 2.000–2.500 | 5% | – | – | 1.080 | 900 | 500 créditos | 5.000 |
| **Rivet II** | Reto, alvo único | Raro | 4.000–5.000 | 25% | – | – | 1.120 | 700 | 800 créditos | 2.000 |
| **Rivet III** | Reto, alvo único | Épico | 6.000–7.500 | 35% | – | – | 1.100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guiado, explosão em área | Comum | 1.120–1.400 | – | 170 | 700 | 1.000 | 500 | 500 créditos | 5.000 |
| **Ember II** | Guiado, explosão em área | Raro | 2.240–2.800 | – | 230 | 920 | 1.500 | 600 | 800 créditos | 2.000 |
| **Ember III** | Guiado, explosão em área | Épico | 3.360–4.200 | – | 300 | 1.150 | 2.030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Reto, explosão em área | Comum | 1.400–1.750 | – | 210 | – | 1.088 | 640 | 500 créditos | 5.000 |
| **Scatter II** | Reto, explosão em área | Raro | 2.800–3.500 | – | 290 | – | 1.080 | 540 | 800 créditos | 2.000 |
| **Scatter III** | Reto, explosão em área | Épico | 4.200–5.250 | – | 400 | – | 1.092 | 420 | 5 Thulium | 500 |

Quanto mais cara a raridade, mais forte o foguete bate, mais longe ele chega, mais penetração de escudo ele tem e menos você pode carregar; os caros também dão o maior dano pelo que custam. Um foguete reto causa **25% a mais** que o foguete guiado da mesma raridade e do mesmo tipo pelo mesmo preço, porque você precisa mirar. Uma explosão causa 70% do foguete de alvo único da mesma raridade, a toda nave que ela cobre. O dano de uma explosão é o do centro; ele cai para 25 a 35% na borda. Um disparo causa em média 90% do número máximo, e a tabela que conta foguetes mais abaixo usa esse valor.

## Quanto custam {#what-they-cost}

Um foguete Comum custa 500 créditos, um Raro 800 créditos e um Épico 5 Thulium, em todos os tipos. Disparados a cada temporizador, isso dá 6.000 créditos por minuto para um foguete Comum, 9.600 para um Raro e 60 Thulium para um Épico, contra os 1.800 créditos por minuto que os três lasers de uma Ostirion queimam a x1. Uma pilha cheia são 5.000 foguetes Comuns (2.500.000 créditos), 2.000 Raros (1.600.000 créditos) ou 500 Épicos (2.500 Thulium): você compra quantos quiser até esse limite, e o *máximo que você carrega* de um foguete é o único limite de quantos você tem. Foguetes não pesam nada: não ocupam espaço no Cache de Transporte. Um foguete a cada 5 segundos são só doze por minuto, então um foguete é o golpe extra por cima dos seus lasers: os baratos para os alienígenas fracos, os caros para as grandes lutas.

A Loja lista os foguetes um tipo de cada vez, cada um sob o seu nome, com o foguete Comum primeiro e o Épico por último; o hangar, o Cache de Transporte e o seletor de Foguetes usam a mesma ordem.

## Contra os alienígenas {#against-the-aliens}

Os foguetes necessários para matar um alienígena, um tipo de foguete de cada vez (Alpha; os alienígenas do Beta e do Gamma têm 1,5 e 2 vezes a força). Uma explosão conta como a nave ao lado da qual ela explode a recebe, um pouco aquém do centro. O escudo de um alienígena recebe 80% de um impacto, menos a penetração de escudo do foguete. Aqui cada foguete sorteia a média. Com o sorteio mais baixo, um abate leva cerca de 10 a 15% mais foguetes do que a tabela diz (um Lancet I precisa de 50 para um Goombah, não de 45); com o melhor, cerca de 10% menos (40). Um Rivet II só mata um Phantasm com um acerto num sorteio de 89% ou mais; abaixo disso, precisa de dois.

| Foguetes para matar | Seeker (1.600) | Phantasm (5.200) | Bulwark (26.000) | Goombah (80.000) | Crystalys (416.000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 15 | 45 | 232 |
| **Lancet II** | 1 | 2 | 8 | 20 | 116 |
| **Lancet III** | 1 | 1 | 5 | 11 | 78 |
| **Rivet I** | 1 | 3 | 12 | 36 | 185 |
| **Rivet II** | 1 | 1 | 6 | 16 | 93 |
| **Rivet III** | 1 | 1 | 4 | 9 | 62 |
| **Ember I** | 2 | 5 | 25 | 77 | 399 |
| **Ember II** | 1 | 3 | 13 | 37 | 193 |
| **Ember III** | 1 | 2 | 8 | 25 | 128 |
| **Scatter I** | 2 | 4 | 20 | 60 | 311 |
| **Scatter II** | 1 | 2 | 10 | 29 | 151 |
| **Scatter III** | 1 | 2 | 7 | 20 | 100 |

- Os foguetes de alvo único **Comuns** matam um Seeker com um acerto em qualquer sorteio e um Phantasm com três (um Lancet I precisa de um quarto no sorteio mais baixo); são os foguetes do dia a dia dos primeiros setores. Os **Raros** são para o Bulwark e o Goombah: oito foguetes Lancet II derrubam um Bulwark em cerca de 35 segundos de temporizador. Os **Épicos** matam um Phantasm com um acerto em qualquer sorteio e um Goombah com nove a onze. As explosões valem o preço quando vários alienígenas estão juntos: um Scatter III explodindo sobre um bando de cinco Phantasms causa cerca de 18.000 de dano ao bando em um único disparo.
- Um abate só com foguetes é um gasto de verdade, não um jeito de ficar rico: para o alienígena a que se destina, um foguete de alvo único custa de cerca de um sétimo a três quartos do que o abate paga (créditos, e Thulium a 200 créditos cada), e os foguetes fracos contra os alienígenas fortes custam mais do que o abate paga. Matar o **Crystalys** com um único tipo exige de 62 a 399 foguetes e no mínimo cinco minutos de temporizador; uma pilha cheia de 500 foguetes Épicos basta para quatro a oito deles. O alienígena mais forte pede um plano: seus lasers com munição x2, um foguete intermediário a cada 5 segundos desde o primeiro segundo, e os foguetes grandes abaixo como o golpe extra.
- O pagamento de um abate é o mesmo, seja como for que ele foi feito (veja [o Crystalys](/wiki/04-Aliens/Crystalys.md) para o maior), então um abate com foguetes compensa quando poupa tempo e custa menos do que paga.
- **Alienígenas também disparam foguetes.** O Pirate Boss, a Dormant Force e as Pulses dos [enxames](/wiki/05-Swarms/Swarms.md) lançam foguetes Rivet retos no piloto que os atacou, com o mesmo temporizador de 5 segundos. Uma nave que não para de se mover os esquiva. Os chefes dos enxames também largam foguetes nas suas caixas.

## Os foguetes só por criação {#the-craft-only-rockets}

Dois foguetes não estão na Loja. A **Montagem** os fabrica, e eles seguem todas as regras abaixo (o temporizador compartilhado, zonas seguras, a sua corporação). Os dois são foguetes retos: voam em direção ao ponto sob o seu cursor, como todo foguete reto (o jogo envia a direção do cursor seja o que for que você tenha selecionado; só um cliente antigo 0.4.3, que não envia direção, faz o servidor lançá-los contra o alvo selecionado, ou então contra o ponto sob o cursor dele, ou então para onde a nave aponta). Eles sorteiam entre **90% e 100%** do número máximo, uma faixa mais estreita que a dos doze, então o que destroem com um acerto abaixo vale também no sorteio mais baixo.

| Nome | Tipo | Raridade | Dano | Penetração de escudo | Raio da explosão | Alcance | Velocidade | Máximo que você carrega | Feito com |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Reto, explosão em área | Lendário | 45.000–50.000 | – | 900 | 1.200 | 300 | 10 | 1 N.U.K.E. por criação: 150.000 créditos, 3.000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Reto, alvo único | Mítico | 67.500–75.000 | 35% | – | 4.050 | 900 | 20 | 5 N.I.K.E. por criação: 100.000 créditos, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: a maior explosão do jogo. Uma explosão de 900 unidades, o dobro do alcance dos 400 do Scatter III e cinco vezes a área dele: de 45.000 a 50.000 para toda nave nela no centro, caindo para a metade disso, de 22.500 a 25.000, na borda. É lenta (quatro segundos no ar). Uma N.U.K.E. elimina todo Seeker e Phantasm em toda a sua explosão e um Bulwark a até 830 unidades da explosão (934 no melhor sorteio), ou seja, quase toda ela; ela leva mais da metade de um Goombah e um nono de um Crystalys. Contra pilotos, é o maior golpe que existe: veja as regras abaixo. O anel no mapa é o alcance exato dela.
- **N.I.K.E.**: um foguete de alvo único como um Rivet I, com dano de 67.500 a 75.000 e uma penetração de escudo de 35%: **ele atinge a primeira nave que toca e se gasta nela.** Também é o foguete que produz [Dark Matter](/wiki/03-Mechanics/Black-Hole.md): disparado contra o buraco negro no meio do Setor de perigo 4, ele é engolido ao cruzar o horizonte de eventos, e o buraco devolve Dark Matter. Ele voa 4.050 unidades em 4,5 segundos: dispare-o de qualquer ponto entre a borda da radiação e 4.380 unidades do centro. De mais longe, ele não alcança e é desperdiçado. Cinco N.I.K.E. rendem cerca de dez Dark Matter.
- **O porém.** Uma N.I.K.E. que encontra uma nave no caminho, um rival à espera na linha ou qualquer outra coisa que ela possa ferir, a atinge com 67.500 a 75.000 e some: o buraco negro não recebe nada, e você também não. Nada mais circula dentro do anel do buraco para ela atingir por acidente (alienígenas e pilotos de corporação ficam fora dele): só pilotos que entraram atrás de Dark Matter, ou que esperam você na borda. Ela atravessa a sua própria corporação, naves em uma zona segura e naves que você ainda não pode ferir. Se você sai do mapa depois de dispará-la, ela continua voando sem ferir ninguém e ainda produz a sua Dark Matter.
- A Montagem não inicia uma criação que deixaria você com mais do que o *máximo que você carrega* de um foguete, contando o que você já colocou na fila.

## Disparo {#firing}

1. Compre foguetes na Loja (a categoria **Foguetes**), até o *máximo que você carrega* de cada um: créditos para os Comuns e Raros, Thulium para os Épicos.
2. Abra **Foguetes** acima da barra de atalhos e arraste os que você quer para os slots. O seletor mostra uma coluna por tipo e uma linha por raridade, com o que você carrega de cada um. Sob elas há uma linha própria, **Especiais · só na Montagem**, para a N.U.K.E. e a N.I.K.E. (um pequeno martelo marca aquela de que você não carrega nenhuma).
3. Pressione a tecla do slot. Clicar no slot de um foguete **guiado** o dispara contra o seu alvo selecionado; clicar no slot de um foguete **reto** o arma, e o seu próximo clique no espaço o dispara ali. A tecla **Disparar foguete** (`R` por padrão, alterável em Configurações › Controles) dispara o foguete que você disparou por último, ou o primeiro da barra.
4. Um indicador circular percorre **todos** os slots de foguete durante os 5 segundos até o próximo lançamento, com os segundos restantes no meio. Se você disparar antes disso, o jogo apenas avisa que os foguetes estão recarregando (um disparo na última décima de segundo ainda sai). Uma formação de drones pode deixar a espera entre 3,65 e 6,75 segundos (veja abaixo).

Passe o mouse sobre um slot de foguete para ver os números dele (o dano mais baixo e o mais alto dele; a Loja e o hangar dizem o mesmo) e, no mundo, o anel de travamento dele (verde quando o alvo selecionado está ao alcance) ou a linha e o círculo da explosão. Um foguete travado em **você** faz a borda da sua tela piscar em vermelho.

A **N.U.K.E.** desenha a explosão dela no mapa antes de você disparar (o círculo de 900 unidades no ponto mirado) e, quando detona, um clarão branco sobre a visão, um anel que se expande até o alcance exato em cerca de um segundo e permanece por mais dois, uma nuvem que sobe como um cogumelo, e um tremor da câmera que é mais forte quanto mais perto você está. **Reduzir tremor da tela** remove o tremor, e **Reduzir movimento** encurta o clarão para um terço de segundo, com menos da metade da luz dele (os dois estão em Configurações › Gráficos); uma qualidade de partículas mais baixa afina a nuvem e tira as faíscas, nunca o clarão nem o anel. A **N.I.K.E.** é mirada como um Rivet I, pela linha da sua nave até o cursor, e o jogo nunca a recusa por estar longe do buraco negro ou em um mapa sem um: para onde ela vai é você quem julga. O cartão dela diz **Buraco negro: Gera Dark Matter** ao lado do dano. Ela deixa um rastro violeta com faíscas girando em volta; uma nave que ela encontra recebe o impacto como de qualquer foguete, e quando ela cruza o horizonte, em vez disso, o buraco lampeja.

## Formações de drones e foguetes {#drone-formations-and-rockets}

Uma [formação de drones](/wiki/03-Mechanics/Formations.md) em uso é a única coisa que muda um foguete. Todos os números de dano desta página são de uma nave sem formação.

- **Dano.** O bônus de foguetes de Ballista (+55%), Bodkin (+29%) e Asterism (+24%) multiplica o dano de todos os 14 foguetes, N.U.K.E. e N.I.K.E. incluídos. O custo de todo o dano de Testudo também conta nos foguetes, e o dano a alienígenas de Culler conta num foguete que acerta um alienígena. Todos os fatores de um foguete juntos param em ×1,59.
- **Recarga.** Asterism alonga o temporizador compartilhado em 35% (6,75 segundos), Cordon em 11% (5,55) e Redoubt o encurta em 27% (3,65), mas nunca abaixo do voo do foguete mais um instante: 4,1 segundos depois de um N.U.K.E. e 4,6 depois de um N.I.K.E. A espera é fixada ao disparar, então trocar de formação depois não a encurta, e o círculo sobre os slots de foguete a acompanha.
- **Os limites dos dois grandes continuam valendo.** Com a melhor formação, um N.I.K.E. acerta com até 116.250, o que um Paragon intacto (128.000) sobrevive, e um N.U.K.E. com até 77.500, o que um Goombah (80.000) sobrevive.
- **Evasão.** Os 7% de evasão de Asterism dão a um foguete direto que atinge você 7% de chance de não causar dano nenhum, e um “Errou” flutuante aparece sobre a sua nave; uma explosão em área não mira e nunca é esquivada.
- **Penetração.** Gemini e Stiletto somam seus pontos à penetração de escudo de um foguete direto (uma explosão não tem), até 40% no total.

## Regras {#rules}

- Você **não precisa de nenhum laser equipado** para disparar um foguete, e seus lasers não mudam o que ele causa nem até onde ele chega: um foguete guiado trava um alvo dentro do próprio alcance de travamento, e um reto voa a própria distância. Sem nenhum laser equipado, o bloco Alcance do hangar mostra um traço, e só os seus foguetes disparam.
- Um foguete é gasto por lançamento, acerte ou não.
- Os foguetes seguem as regras dos lasers: nada dentro de uma **zona segura** é ferido, nenhum piloto é ferido antes de o **Protocolo de Paz** terminar ou onde um setor proíbe PvP, e **a sua própria corporação e o seu próprio grupo nunca são feridos** pelos seus foguetes, de impacto direto ou de explosão.
- Lançar um foguete encerra na hora a sua própria proteção de zona segura. É um disparo: ele também encerra a sua própria **camuflagem**, e a Cloaking CPU então recarrega por um minuto, como depois de qualquer fim de camuflagem. Camuflado ou não, um lançamento impede você de se camuflar nos 10 segundos seguintes (veja [Extras](/wiki/06-Items/Extras.md)).
- Uma nave **camuflada** ou dentro dos **3 segundos do seu EMP** não pode ser travada: um foguete guiado é recusado, e um que já voa contra ela perde a trava e segue reto. Um foguete reto de alvo único atravessa uma nave assim. Uma **explosão em área** não precisa de trava, então fere as naves que ela cobre, camufladas ou não, e encerra uma camuflagem (veja [Extras](/wiki/06-Items/Extras.md)).
- **Nada limita o que um foguete causa a um piloto.** A nave de outro piloto recebe o dano inteiro: primeiro o escudo (a absorção dele menos a penetração de escudo do foguete), depois o casco. As naves pequenas não resistem. Com os núcleos de escudo de série (Light, 45% de absorção), uma N.I.K.E. destrói, em qualquer sorteio, uma Protos, Kitefin ou Ostirion intacta com um acerto (uma Paragon perde de 47 a 53% do casco, uma Wraith cerca de um quinto), e uma N.U.K.E. destrói uma Protos em qualquer ponto da sua explosão, uma Kitefin a até cerca de 50 unidades da explosão (220 no melhor sorteio) e nada maior em uma única explosão. Dois foguetes Lancet III ou dois Rivet III destroem uma Protos em qualquer sorteio; uma Wraith exige de 48 a 75 deles. O Protocolo de Paz, as zonas seguras e a sua corporação são o que fica entre um piloto e um foguete. Esses números são de uma nave sem formação; uma formação de foguetes os aumenta em até 55% (veja [Formações de drones e foguetes](#drone-formations-and-rockets)).
- Só o **acerto direto** de um foguete reivindica um alienígena (veja [Combate](/wiki/03-Mechanics/Combat.md)); a borda de uma explosão pode ferir um alienígena já reivindicado sem roubá-lo. Todo alienígena que uma explosão fere, um que dormia também, se volta contra você, como acontece com um acerto de laser (inclusive um Seeker ou um Goombah, que só revidam); o que a explosão erra continua dormindo.
- O temporizador é seu: ele sobrevive a um salto, a uma reconexão, a uma troca de nave e a uma nave destruída.

Os doze foguetes da primeira tabela são comprados (créditos para os Comuns e Raros, Thulium para os Épicos); a N.U.K.E. e a N.I.K.E. são criadas.

Veja também: [Lasers e munição](/wiki/06-Items/Lasers.md), [Combate](/wiki/03-Mechanics/Combat.md), [O buraco negro](/wiki/03-Mechanics/Black-Hole.md).
