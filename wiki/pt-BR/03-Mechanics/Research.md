<!-- wiki-i18n source: 20209f353955718c -->
<!-- wiki-i18n title: Pesquisa -->
# Pesquisa {#research}

O **Centro de Pesquisa** é o laboratório do seu [Skylab](/wiki/03-Mechanics/Skylab.md). Você o alimenta com recursos, ele os transforma em **ciência**, e a ciência pesquisa **tecnologias**. Toda criação na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules) exige antes a sua tecnologia: uma nave, um laser, um propulsor ou uma CPU não podem ser criados enquanto não forem pesquisados.

Esta página reúne a árvore de tecnologias completa com o tempo de cada uma, a ciência que cada recurso dá, o boost de Thulium, a regra da Dark Matter e as novas CPUs. Os números são lidos dos próprios dados do jogo, então são sempre os do jogo. Para ver tudo o que um item exige (primeiro a tecnologia a pesquisar, com seu tempo e as tecnologias de que ela precisa, depois os materiais e a criação), abra o item no [Livro de receitas](/wiki/01-General/Recipe-Book.md).

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)
![The Research view with technologies queued behind the running one: the Dark Matter all of them need, what the Research Centre holds and the Add button that gives the rest](../../img/wiki-img/shots/research-queue.jpg)

## O Centro de Pesquisa {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Desbloqueia no nível 10 do Núcleo.** O Centro de Pesquisa é um módulo do seu [Skylab](/wiki/03-Mechanics/Skylab.md), construído como os outros: 25 Ship Fragments do seu inventário (com a nave pousada), 25.000 créditos e 500 Thulium. A tela dele é a visão **Pesquisa** da página do Skylab.
- **Níveis 1 a 10.** Um nível maior dá um tanque maior e consome mais energia. Ele não deixa a pesquisa mais rápida: uma tecnologia leva o mesmo tempo em todos os níveis.
- **O tanque.** O Centro guarda a ciência em um tanque que, no nível 1, comporta 12 h de pesquisa e, a cada nível, 25% a mais (veja a tabela abaixo).
- **Do combustível à ciência.** Um recurso que você coloca vira ciência na hora, como mostra a tabela de combustível. Uma pesquisa queima 1 de ciência por segundo do seu tempo de pesquisa; com o tanque vazio ela espera, e continua quando você alimenta o Centro.
- **Uma primeira hora de graça.** Um Centro novo começa com 3.600 de ciência no tanque, ou seja, 1 h de pesquisa.
- **Uma de cada vez.** O Centro pesquisa uma tecnologia por vez, mas com o botão Pôr na fila você pode deixar até 5 a mais atrás dela. Cada uma começa sozinha assim que a anterior termina, mesmo com você fora. Pôr na fila não custa nada: a tecnologia usa a Dark Matter quando começa, e uma que está na fila pode ser tirada de novo de graça.
- **Enquanto você está fora.** Uma pesquisa corre no relógio do servidor, então continua depois que você sai, até terminar ou o tanque esvaziar. Um déficit de energia ou uma melhoria do Centro não a interrompe.
- **Energia.** O Centro consome 25 no nível 1 e, a cada nível, 15% a mais, e não pode ser desligado.
- **O reset mantém tudo:** suas tecnologias, a ciência do tanque, a Dark Matter inserida, uma pesquisa em andamento e o boost.
- **O que você tem é seu.** Quando a pesquisa chegou ao jogo, cada piloto recebeu a tecnologia de cada item que já possuía e as tecnologias de que eles precisavam. Um item que chega depois (um presente, um código, uma recompensa) não desbloqueia a tecnologia dele, com uma exceção: um Engine II, um Engine III, um Adaptive Core II ou um Adaptive Core III que um código, uma missão, um convite ou um administrador lhe dá desbloqueia na hora a tecnologia dele e as que ela exige.
- **Abaixo do nível 10 do Núcleo** você não pode pesquisar, então ainda não pode criar nada novo na Montagem. As missões da estação guiam você na subida do Núcleo.

<!-- research-centre:end -->

**Schematics.** Um [Schematics](/wiki/06-Items/Special-Items.md#schematics) conclui na hora a pesquisa em andamento, se a tecnologia dela leva 24 horas ou menos para ser pesquisada (135 das 151 tecnologias). O que a pesquisa custou foi pago no início e não volta, a ciência que ela ainda não queimou fica no seu tanque e a próxima tecnologia da sua fila começa na hora.

**Os amplificadores de laser e o último nível.** Os Damage, Crit e Penetration Amps dos níveis II a IV são pesquisados como todo o resto que se cria. Os pilotos que tinham ou haviam enfileirado amps quando as linhas de amps chegaram receberam a tecnologia de cada um deles e a dos níveis abaixo. Treze tecnologias exigem uma tecnologia de outra árvore, a da Dark Matter Plate, da árvore Recursos, porque o último nível de cada cadeia de melhoria pede quatro plates e uma Ancient Control Unit: os Damage, Crit e Penetration Amps do nível IV, as Absorption e Capacity Shield Cells do nível IV, os Impulse e Momentum Thrusters do nível IV, o Heavy Shield Core, o Engine III, o Adaptive Core III, o Helios Beam, o Extra Slots CPU III e o Base CPU II. Quem pesquisou uma delas antes a mantém, e precisa da tecnologia da plate para fazer as plates dela. A árvore abaixo não traça seta para ela, mas a tabela a lista e o cartão no jogo a nomeia ([Dark Matter e Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

Na visão **Pesquisa** do seu Skylab, uma tecnologia diz mais do que uma caixa das árvores abaixo. Passe o mouse sobre uma tecnologia e um cartão se abre com o tempo de pesquisa e a ciência que ela queima e, embaixo, o que o item **é e faz**: o tipo dele e o grau na família (por exemplo, o terceiro dos quatro Impulse Thruster), a descrição, os números como o hangar e a Loja os mostram (o dano, a chance de crítico e o alcance de um laser, a capacidade, a recarga e a absorção de um escudo, a velocidade extra e o multiplicador de um propulsor, o dano, o raio da explosão e o alcance de um foguete, o que uma formação de drones dá e o que ela custa), uma pequena tabela dos graus da família e o que a Montagem pede depois para criá-lo: o tempo, os créditos e o Thulium e os materiais. Assim você vê o que um grau dá antes de pesquisá-lo. Clique em uma tecnologia para escolhê-la: o cartão ao lado da árvore mostra o mesmo por inteiro, sob o botão **Iniciar pesquisa**. Enquanto uma pesquisa está em andamento, **Pôr na fila** ocupa o lugar do botão de iniciar: uma tecnologia na fila mostra seu número de ordem na árvore, e um cartão da fila sob a pesquisa em andamento lista todas, cada uma com uma cruz para tirá-la. Se a próxima não puder começar (a Dark Matter de que ela precisa não está no Centro, ou o tanque está vazio), a fila espera e diz o motivo, até você resolver e apertar **Iniciar fila**.

### O tanque em cada nível {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Nível | Tanque (ciência) | Comporta pesquisa para | … com o boost | Energia |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43.200 | 12 h | 6 h | 25 |
| 2 | 54.000 | 15 h | 7,5 h | 28,7 |
| 3 | 67.500 | 18,8 h | 9,4 h | 33,1 |
| 4 | 84.375 | 23,4 h | 11,7 h | 38 |
| 5 | 105.469 | 29,3 h | 14,6 h | 43,7 |
| 6 | 131.836 | 36,6 h | 18,3 h | 50,3 |
| 7 | 164.795 | 45,8 h | 22,9 h | 57,8 |
| 8 | 205.994 | 57,2 h | 28,6 h | 66,5 |
| 9 | 257.492 | 71,5 h | 35,8 h | 76,5 |
| 10 | 321.865 | 89,4 h | 44,7 h | 87,9 |

<!-- research-tank:end -->

## Combustível {#fuel}

Você alimenta o Centro com recursos, e cada unidade vira ciência na hora. Quanto mais trabalho dá obter uma unidade, mais ciência ela rende: os valores seguem a dificuldade de obtê-la, não a etiqueta de raridade. Os minérios são a exceção: uma unidade rende mais ciência do que os segundos que um coletor leva para extraí-la, então uma hora do minério de um coletor no meio dos seus níveis alimenta cerca de duas horas de pesquisa. Os minérios vêm do Depósito de recursos do seu [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage); qualquer outro recurso vem do seu inventário, e a sua nave precisa estar pousada. A Velkonite Reinforced Plate, a Orvium Reinforced Plate, a Dark Matter Plate, o Dark Matter, os créditos e o Thulium não podem ser queimados; a Reinforced Hull Plate pode. O Velkonite e o Orvium que as caixas de uma escavadeira deixam no seu inventário chegam ao Depósito de recursos pela [Baía de minério](/wiki/03-Mechanics/Skylab.md#ore-bay).

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Recurso | Raridade | Tirado de | Ciência por unidade | Unidades para 1 hora |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Comum | Seu inventário | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Comum | Seu inventário | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Comum | Seu inventário | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Comum | Seu inventário | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Comum | Seu inventário | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Comum | Seu inventário | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Incomum | Seu inventário | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Incomum | Depósito de recursos | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Raro | Depósito de recursos | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Raro | Seu inventário | 650 | 6 |

A última coluna é o número de unidades que sustentam uma hora de pesquisa sem o boost, arredondado para cima; com o boost são 2 vezes mais.

<!-- research-fuel:end -->

## O boost de Thulium {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5.000 Thulium** compram um boost: o Centro pesquisa **2 vezes mais rápido por 24 horas**.
- Ele também **queima a ciência 2 vezes mais rápido**, então um boost compra tempo e nunca combustível: uma tecnologia queima a mesma ciência, com ou sem boost.
- Um boost começa no momento em que você o compra e corre no relógio, haja combustível no tanque ou não, então compre-o enquanto uma pesquisa estiver em andamento. O Centro recusa um quando nada está sendo pesquisado.
- Os boosts se somam: comprar um enquanto outro está ativo acrescenta 24 horas ao fim dele, até 72 horas à frente. Um boost pertence ao seu Centro de Pesquisa, não a uma pesquisa específica.

O que um boost faz com o tempo de uma pesquisa, com o boost ativo desde o início:

| Tempo de pesquisa | Com o boost | Boosts para ela toda | Thulium |
| :--- | :--- | ---: | ---: |
| 30 min | 15 min | 1 | 5.000 |
| 3 h | 1 h 30 min | 1 | 5.000 |
| 6 h | 3 h | 1 | 5.000 |
| 10 h | 5 h | 1 | 5.000 |
| 1 d | 12 h | 1 | 5.000 |
| 2 d | 1 d | 1 | 5.000 |

<!-- research-boost:end -->

## Dark Matter

As tecnologias do topo da árvore exigem também Dark Matter. Ela vem do [buraco negro](/wiki/03-Mechanics/Black-Hole.md#dark-matter), onde um foguete N.I.K.E. que o alcança deixa um pouco, e de vez em quando de um Dormant Pulse do [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** para cada uma das 16 tecnologias da tabela abaixo, além da ciência: insira-a no Centro de Pesquisa (do seu inventário, com a nave pousada) antes de começar, e a pesquisa a leva quando começa.
- **A regra:** um item de raridade Épico ou superior cuja pesquisa leva 10 h ou mais. A N.I.K.E., com a qual a Dark Matter é obtida, nunca precisa dela.
- **As formações de drones** ficam fora da regra: toda pesquisa de formação pede Dark Matter, 5, 13 ou 20 conforme a força, como a tabela mostra.
- **A blindagem de casco** também fica fora da regra: suas duas pesquisas pedem mais, 25 de Dark Matter por um dia de pesquisa e 40 por dois dias, como a tabela mostra.
- **Se você cancelar uma pesquisa,** a Dark Matter inserida para ela volta ao Centro. O progresso e a ciência já queimada, não.
- **Uma fila inteira.** Pôr na fila não custa nada, e cada tecnologia na fila usa a sua Dark Matter quando começa; por isso insira de uma vez a Dark Matter de toda a fila. O botão Adicionar enche o Centro até o que as tecnologias da fila usam no total (e a tecnologia escolhida, se ainda não estiver na fila), não importa quanto a primeira precise, e cada tecnologia da fila mostra se a Dark Matter do Centro a cobre. Uma fila parada por falta de Dark Matter começa sozinha no momento em que você adiciona o que faltava.
- Todas juntas pedem 414 Dark Matter.

| Tecnologia | Raridade | Tempo de pesquisa | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Épico | 10 h | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Épico | 10 h | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Épico | 10 h | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Épico | 10 h | 10 |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | Mítico | 1 d | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mítico | 1 d | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épico | 10 h | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épico | 10 h | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Épico | 1 d | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Épico | 1 d | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mítico | 2 d | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mítico | 1 d | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Lendário | 1 d | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Épico | 1 d | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Épico | 1 d | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 10 h | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 10 h | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mítico | 2 d | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 10 h | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mítico | 2 d | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mítico | 2 d | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 10 h | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 10 h | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épico | 1 d | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épico | 10 h | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Raro | 1 d | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Épico | 2 d | 40 |

<!-- research-dark-matter:end -->

## A árvore de tecnologias {#the-technology-tree}

Cada caixa é uma tecnologia: o item que ela permite criar, com o tempo de pesquisa sob o nome (o relógio) e, onde precisa de Dark Matter, o emblema da Dark Matter. Uma seta vai de uma tecnologia para a que a exige, e você pesquisa a primeira antes; uma caixa sem seta pode ser pesquisada de imediato. Passe o mouse sobre uma caixa para ver o tempo de pesquisa, a ciência que ela queima e o que a Montagem pede depois pelo item, e clique para abrir a página do item. As árvores são desenhadas a partir dos próprios dados do jogo. Duas das árvores, **Defesa** e **Ataque e mobilidade**, contêm as dezesseis [formações de drones](/wiki/03-Mechanics/Formations.md).

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Propulsão e velocidade {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Adaptive Core II | hybrid-generator, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
Engine II => Engine III
Adaptive Core II => Adaptive Core III
```

### Escudos e defesa {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 50 Ship Fragment, 8 Reinforced Hull Plate, 20 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 50 Ship Fragment, 10 Reinforced Hull Plate, 2 Power Core, 25 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 5000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 50 Ship Fragment, 8 Reinforced Hull Plate, 20 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 50 Ship Fragment, 10 Reinforced Hull Plate, 2 Power Core, 25 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 5000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lasers e munição {#tree-lasers}

```tree research
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 50 Cataclysite, 18 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 2400 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 2400 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 500 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 50 Ship Fragment, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 2000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 50 Ship Fragment, 2 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 500 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 50 Ship Fragment, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 2000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 50 Ship Fragment, 2 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 500 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 50 Ship Fragment, 20 Daraxium, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 2000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 50 Ship Fragment, 2 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 2400 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 40 Quorvium, 4 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser III => Starfire-III => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### Boosters {#tree-boosters}

```tree research
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Drones {#tree-drones}

```tree research
Master Drone | drone, rare | craft 1000000 Credits, 50000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 250 Ship Fragment, 2 Ancient Control Unit, 5 Velkonite Reinforced Plate, 5 Orvium Reinforced Plate, 10 Dark Matter Plate | /wiki/06-Items/Drones.md#available-drones
```

### Naves {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 500 Ship Fragment, 200 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 20 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 500 Ship Fragment, 200 Reinforced Hull Plate, 20 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Recursos {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Foguetes {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPUs {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Energetic Wall II | consumable, rare | craft 600 Thulium, 120 s | research 21600 s, 21600 science | 5 Ship Fragment, 1 Power Core | /wiki/06-Items/Extras.md#energetic-wall
Auto-Rocket CPU | extra, rare | craft 20000 Thulium, 900 s | research 36000 s, 36000 science | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 1 Ancient Control Unit, 8 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-rocket-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### Defesa {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 15000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 18000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 77000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 30 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 40000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 42000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 43000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### Ataque e mobilidade {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 42000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 14000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 76000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 30 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 48000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 92000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 30 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 17000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 40000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 41000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 16000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 40000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 15 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```

### Blindagem de casco {#tree-hull-plating}

```tree research
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating II => Hull Plating III
```

### P.E.T. {#tree-p-e-t}

```tree research
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
P.E.T. Station II | extra, uncommon | craft 300000 Credits, 4000 Thulium, 600 s | research 36000 s, 36000 science | 1 P.E.T. Station I, 35 Ship Fragment, 6 Reinforced Hull Plate, 2 Power Core, 4 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
P.E.T. Station III | extra, rare | craft 1100000 Credits, 12000 Thulium, 900 s | research 86400 s, 86400 science | 1 P.E.T. Station II, 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 2 Ancient Control Unit, 4 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md

P.E.T. Station I => P.E.T. Station II => P.E.T. Station III
```


<!-- research-tree:end -->

## Designs de naves e slots de blindagem {#ship-technologies}

A família Naves da tela de pesquisa do seu Skylab tem dois tipos de tecnologia que não são fabricações. A árvore acima as deixa de fora, porque o que elas abrem é um slot ou uma conversão, não um item.

- **Slots de blindagem.** Uma tecnologia para cada [slot de blindagem](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) das quatro naves que você fabrica. Cada uma vem depois da anterior, a primeira depois da tecnologia da própria nave. No jogo, os slots de uma nave são um único cartão com um ponto para cada slot.
- **Designs de naves.** Uma tecnologia para cada [design](/wiki/03-Mechanics/Ship-Designs.md). Cada uma precisa da tecnologia da nave dele e da Dark Matter Plate.

Os tempos, o Dark Matter e os totais estão na página [Designs de naves](/wiki/03-Mechanics/Ship-Designs.md#the-technologies).

## Módulos do Skylab {#module-technologies}

A família Skylab da visão de Pesquisa tem mais um tipo de tecnologia que não é uma fabricação: os níveis do **Módulo de motores**, do **Módulo de defesa** e do **Módulo de radar**, que o nível quinze do Core desbloqueia. Cada nível tem a sua própria tecnologia e só é construído depois dela; o primeiro nível de cada módulo não pede Dark Matter e os seguintes pedem mais a cada nível. A árvore acima os deixa de fora, porque o que eles abrem é um nível de módulo, não um item. O Dark Matter deles se soma aos totais acima, e [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) faz a conta. Os tempos deles e o que cada módulo faz estão no artigo [Skylab](/wiki/03-Mechanics/Skylab.md).

## Piloto {#pilot-technologies}

A família Piloto da visão de Pesquisa tem tecnologias que não são fabricações: elas não criam nada na Montagem. A maioria é de **melhorias permanentes** para você. A árvore acima as deixa de fora, porque o que elas abrem é uma melhoria, não um item.

- **O que custam.** Além da ciência e da Dark Matter, uma melhoria pede **créditos e Thulium**. O Centro leva tudo quando a pesquisa começa e devolve tudo se você a cancelar antes de ela terminar.
- **Elas ficam.** Como o resto da sua pesquisa, essas tecnologias permanecem após o reset, e as melhorias com elas.
- **Em série.** Cada nível exige o anterior, e um nível maior substitui o menor: a tabela mostra o total que cada nível dá, não o que ele acrescenta.
- **Lanches eficientes** (Kebab, Pelmeni, Hambúrguer) acrescentam casco a todas as naves que você tem, nas duas configurações.
- **Porta dos fundos selada** aumenta o limite de carga de todos os foguetes, onde quer que você os compre, fabrique ou troque.
- **Mineração com escavadeira** aumenta o que você leva de cada caixa de uma [escavadeira gigante](/wiki/03-Mechanics/Giant-Excavator.md), tanto de Thulium quanto de minério.
- **Teoria de campos** aumenta a parte de cada tiro que seus escudos absorvem. Uma nave sem escudo não ganha nada.
- **Conhecimento adormecido** paga pontos de reset por nível quando a pesquisa termina no Centro, e de novo depois de cada reset ([Como ganhar pontos de reset](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)). Além do nível anterior, exige uma parte das outras tecnologias pesquisadas (as do Piloto contam, as cinco de Conhecimento adormecido não), de qualquer forma que você as tenha obtido; a tabela mostra cada parte e quantas tecnologias são.

<!-- research-pilot:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Tecnologia | O que dá | Exige antes | Tempo de pesquisa | Dark Matter | Créditos | Thulium |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| Lanches eficientes: Kebab | +5.000 de casco em todas as suas naves | – | 10 h | 10 | 250.000 | 2.500 |
| Lanches eficientes: Pelmeni | +10.000 de casco em todas as suas naves | Lanches eficientes: Kebab | 1 d | 20 | 1.000.000 | 10.000 |
| Lanches eficientes: Hambúrguer | +15.000 de casco em todas as suas naves | Lanches eficientes: Pelmeni | 2 d | 30 | 3.500.000 | 35.000 |
| Porta dos fundos selada I | +25% no limite de carga de foguetes | – | 6 h | 5 | 100.000 | 1.000 |
| Porta dos fundos selada II | +50% no limite de carga de foguetes | Porta dos fundos selada I | 10 h | 10 | 300.000 | 3.000 |
| Porta dos fundos selada III | +100% no limite de carga de foguetes | Porta dos fundos selada II | 1 d | 15 | 750.000 | 7.500 |
| Porta dos fundos selada IV | +150% no limite de carga de foguetes | Porta dos fundos selada III | 2 d | 25 | 1.750.000 | 17.500 |
| Porta dos fundos selada V | +200% no limite de carga de foguetes | Porta dos fundos selada IV | 3 d | 40 | 3.500.000 | 35.000 |
| Mineração com escavadeira I | +20% na produção da escavadeira | – | 1 d | 10 | 500.000 | 5.000 |
| Mineração com escavadeira II | +30% na produção da escavadeira | Mineração com escavadeira I | 2 d | 20 | 1.500.000 | 15.000 |
| Mineração com escavadeira III | +40% na produção da escavadeira | Mineração com escavadeira II | 3 d | 30 | 4.000.000 | 40.000 |
| Teoria de campos I | +2% de absorção do escudo | – | 1 d | 20 | 500.000 | 5.000 |
| Teoria de campos II | +3% de absorção do escudo | Teoria de campos I | 2 d | 40 | 1.500.000 | 15.000 |
| Teoria de campos III | +5% de absorção do escudo | Teoria de campos II | 3 d | 60 | 5.000.000 | 50.000 |
| Conhecimento adormecido I | +50 pontos de reset | 20% das outras tecnologias (30 de 146) | 1 h | – | – | – |
| Conhecimento adormecido II | +50 pontos de reset | Conhecimento adormecido I; 40% das outras tecnologias (59 de 146) | 1 h | – | – | – |
| Conhecimento adormecido III | +50 pontos de reset | Conhecimento adormecido II; 60% das outras tecnologias (88 de 146) | 1 h | – | – | – |
| Conhecimento adormecido IV | +50 pontos de reset | Conhecimento adormecido III; 80% das outras tecnologias (117 de 146) | 1 h | – | – | – |
| Conhecimento adormecido V | +50 pontos de reset | Conhecimento adormecido IV; 100% das outras tecnologias (146 de 146) | 1 h | – | – | – |

<!-- research-pilot:end -->

## Todas as tecnologias {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Tecnologia | Exige antes | Classe | Tempo de pesquisa | Ciência | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1.800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10.800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36.000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1.800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10.800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36.000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Engine II](/wiki/06-Items/Propulsion.md#engines) | B | 3 h | 10.800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1.800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10.800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36.000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1.800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10.800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36.000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 h | 10.800 | – |
| [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 h | 10.800 | – |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | D | 1 d | 86.400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | D | 1 d | 86.400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36.000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36.000 | 10 |
| [Laser Damage Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10.800 | – |
| [Shield Wall Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10.800 | – |
| [Hull Plating Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10.800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36.000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 h | 21.600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 d | 86.400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 d | 86.400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 d | 172.800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 d | 86.400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 h | 10.800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 d | 86.400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 min | 1.800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 h | 36.000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 d | 86.400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 h | 10.800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36.000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 d | 86.400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 h | 21.600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2 d | 172.800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 d | 172.800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 d | 172.800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10 h | 36.000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 d | 86.400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36.000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1 d | 86.400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1.800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10.800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1.800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10.800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1.800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10.800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36.000 | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | D | 1 d | 86.400 | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | D | 2 d | 172.800 | 40 |
| [Engine II](/wiki/06-Items/Propulsion.md#engines) | – | A | 30 min | 1.800 | – |
| [Adaptive Core II](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-) | – | A | 30 min | 1.800 | – |
| [Adaptive Core III](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-) | [Adaptive Core II](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 h | 10.800 | – |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | – | B | 6 h | 21.600 | – |
| [P.E.T. Station I](/wiki/06-Items/Extras.md) | – | B | 3 h | 10.800 | – |
| [P.E.T. Station II](/wiki/06-Items/Extras.md) | [P.E.T. Station I](/wiki/06-Items/Extras.md) | C | 10 h | 36.000 | – |
| [P.E.T. Station III](/wiki/06-Items/Extras.md) | [P.E.T. Station II](/wiki/06-Items/Extras.md) | D | 1 d | 86.400 | – |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | – | C | 10 h | 36.000 | – |

As classes, por tempo de pesquisa:

| Classe | Tempo de pesquisa | Tecnologias | Uma após a outra | Ciência | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 min | 10 | 5 h | 18.000 | 0 |
| B | 3 h a 6 h | 20 | 2 d 21 h | 248.400 | 0 |
| C | 10 h | 17 | 7 d 2 h | 612.000 | 95 |
| D | 1 d a 2 d | 23 | 28 d | 2.419.200 | 319 |
| Todas |  | 70 | 38 d 4 h | 3.297.600 | 414 |

Pesquisada uma após a outra, a árvore inteira leva 38 d 4 h. Com o boost ligado o tempo todo, leva 19 d 2 h, o que dá 20 boosts e 100.000 Thulium; a ciência é a mesma.

<!-- research-technologies:end -->

## As CPUs {#the-cpus}

As novas CPUs também são pesquisadas aqui e depois criadas na Montagem. A mesma tabela e as mesmas notas estão na página [Extras](/wiki/06-Items/Extras.md#research-cpus).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Tempo de pesquisa | Exige antes | Thulium para criar | Tempo de criação |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12.000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30.000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75.000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8.000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20.000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40.000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15.000 | 10 min |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | 10 h | – | 20.000 | 15 min |

Nenhuma é vendida na Loja: pesquise a tecnologia e depois crie a CPU na Montagem. Passe o mouse sobre uma CPU na árvore dela para ver o que a Montagem pede para criá-la.

### Extra Slots CPUs

- **O que fazem.** As Extra Slots CPU I, II e III dão a toda nave 3, 5 e 7 slots extras a mais, ou seja, 6, 8 e 10 no total numa nave que já tem 3, e 5, 7 e 9 numa que já tem 2. Uma CPU maior substitui a anterior: a II não se soma à I.
- **Instalada, não carregada.** Uma Extra Slots CPU não é um item: quando você a coleta na Montagem, ela se instala no seu Skylab, para toda nave nas duas configurações, e não ocupa nenhum slot. Ela fica depois do reset.
- **Em ordem.** Crie-as uma após a outra: a II só quando a I está instalada, a III só quando a II está instalada; até lá a Montagem diz qual instalar primeiro. As três custam 117.000 Thulium no total: 12.000, 30.000 e 75.000.

### Jump CPU

- **O que faz.** Faz sua nave saltar para qualquer setor de corporação do seu mundo, tanto da sua corporação quanto das outras, setores-base incluídos (`M`, `T` e `G`, setores 1 a 4), por **500 Thulium** o salto. Não há limite de usos: você só paga o Thulium. Nunca leva a um setor de perigo (`DS`) nem a um setor neutro (`N`).
- **O salto.** Pressione o slot JMP, escolha o setor no mapa do Sistema estelar e confirme: a nave carrega por 5 segundos, depois chega a um portal desse setor, protegida como após qualquer salto de portal. A CPU esfria por 30 segundos depois que você chega.
- **Não em combate.** Ela não pode começar nos 10 segundos após um disparo ou um acerto, e um disparo ou um acerto durante a carga cancela o salto; nada é pago então. Você não pode saltar camuflado.
- **Não a partir de um setor neutro:** um piloto em um setor neutro ou sem corporação não pode usá-la.
- Ela pode sair de um setor de perigo quando você não está em combate.

### Base CPUs

- **O que fazem.** Teletransportam sua nave para a base da sua corporação, dentro da zona segura ao redor da estação (`M-1`, `T-1` ou `G-1`, o setor com a Mission Control), sem custo de Thulium. Você as inicia pelo slot BSE da barra de atalhos.
- **Não em combate.** Uma carga de 10 segundos, igual para as duas. Não pode começar nos 10 segundos após um disparo ou um acerto, nem camuflado ou quando você já está dentro da zona segura da sua base, e um disparo ou um acerto durante a carga a cancela.

| CPU | Usos | Recarga |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Gasta, não recarrega.** Cada uso consome um dos usos da CPU, e uma CPU sem usos restantes some: crie uma nova. Com as duas equipadas, a melhor (II) é usada primeiro.

### Auto-Repair CPU

- **O que faz.** Envia por conta própria o Repair Drone equipado nos seus slots extras, sempre que você poderia tê-lo enviado manualmente: seu casco não está cheio, o drone não está fora e já se passaram 10 segundos desde o último acerto. Não há nenhum nível de casco para configurar.
- Ocupa um slot extra só dela e não faz nada sem um Repair Drone em um slot extra da mesma configuração. Nunca envia um Repair Drone de um slot de habilidade (esse é o botão Emergency Repair).
- **Se você parar o drone manualmente,** a CPU o deixa em paz até o seu casco estar cheio de novo, ou até você enviar o drone por conta própria.

### Auto-Rocket CPU

- **O que faz.** Enquanto estiver em ON e você estiver em combate (seus lasers estão em um alienígena ou em um piloto inimigo), ela dispara sozinha o seu foguete ativo, o último que você disparou, nesse alvo, sempre que um clique na tecla Disparar foguete funcionaria: o temporizador dos foguetes está pronto e resta um. O servidor confere cada disparo como confere os seus.
- **O interruptor.** Equipe-a em um slot de Extras e clique no slot ARL dela para colocá-la em ON ou OFF. Ela começa em OFF e fica como você a deixou, mesmo quando você entra de novo. O slot mostra ON ou OFF e brilha quando a CPU dispara.
- **O que nunca faz.** Nunca escolhe um alvo, nunca dispara em asteroides, de uma zona segura ou camuflado, e nunca dispara uma N.U.K.E. ou uma N.I.K.E. Um foguete que você mesmo dispara sempre funciona. Sem tecla, clique ou movimento do mouse por 3 minutos, ela espera você fazer algo.
- **Sem foguetes.** Ela avisa uma vez e volta a disparar assim que você tiver mais.


<!-- research-cpus:end -->
