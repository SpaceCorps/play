<!-- wiki-i18n source: 1adce749be3cd1f3 -->
<!-- wiki-i18n title: Escudos -->
# Escudos e defesa {#shields-defense}

Os módulos defensivos dão capacidade de escudo, absorvem dano e recarregam suas defesas.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | buy 4000 Thulium | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I -> Adaptive Core II -> Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Núcleos de escudo {#shield-cores}

Equipe núcleos de escudo para gerar barreiras defensivas ativas, nos slots de gerador da sua nave ou nos seus [drones](/wiki/03-Mechanics/Drones.md) (o slot de um drone conta como um slot de núcleo). Note que escudos pesados diminuem sua velocidade. Um núcleo de escudo em um **slot de habilidade** dá a você, em vez disso, o **Shield Surge** da coluna Efeito especial, um reparo de escudo ao longo de dez segundos, e não acrescenta escudo próprio (veja [Habilidades](/wiki/03-Mechanics/Abilities.md)).

| Nome | Raridade | Capacidade | Taxa de recarga | Absorção | Escudo % | Veloc. % | Slots de célula | Efeito especial | Custo |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Inferior | 10.000 | 333/s | 45% | +5% | -1% | 1 | Shield Surge I | 20.000 créditos |
| **Basic Shield Core** | Comum | 15.000 | 500/s | 48% | +10% | -3% | 2 | Shield Surge II | 2.000 Thulium |
| **Heavy Shield Core** | Raro | 25.000 | 833/s | 50% | +20% | -5% | 3 | Shield Surge III | Só por criação |

O **Heavy Shield Core** é feito na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules) a partir de um Basic Shield Core, com 2.000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates e 6 Velkonite Reinforced Plates do seu Skylab. Ele mantém o grau de encantamento do núcleo que consome, e os bônus dele são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retire primeiro o Basic Shield Core da sua nave (e as células de dentro dele): um núcleo que está encaixado ou que guarda células não é consumido.

A **absorção** é a parte de cada impacto que seus escudos recebem; o casco recebe o resto. Um escudo sozinho tem de **45 a 50%**, e as células dele somam o resto: o melhor escudo com as melhores células (um Heavy Shield Core com três Absorption Shield Cell IV) chega a **80%**, o máximo que uma nave tem de série. Dois bônus permanentes se somam a isso: o Shield Absorbance Boost da Loja de PR (+0,1 ponto por nível, 100 níveis, 25 pontos de reset cada) e os bônus de absorção da Forja. As fontes atuais de pontos de reset (855 no total em seus limites, mantidos entre os resets; mais fontes estão planejadas) compram 34 desses 100 níveis (+3,4 pontos), o que, com um conjunto Eterno totalmente forjado, dá cerca de **95%**. Mesmo assim, o atributo não tem teto em 100%: a *penetração de escudo* de quem ataca é descontada dele, então o que uma nave tem acima de 100% é a margem dela contra a penetração. Veja [Mecânica dos escudos](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Geradores híbridos (núcleos adaptativos) {#hybrid-generators-adaptive-cores-}

Os núcleos adaptativos funcionam como geradores híbridos, combinando capacidades de escudo e de velocidade. Eles aceitam propulsores e células de escudo em seus slots (um módulo por slot, de qualquer um dos dois tipos). O bônus de escudo e o bônus de velocidade deles contam como os de um escudo ou de um motor (os quatro melhores, vezes a parte do slot). Eles não têm absorção: não alteram a absorção da sua nave, e as células neles só acrescentam capacidade e recarga. Só os escudos recebem uma parte do impacto, então as células em um núcleo adaptativo também exigem um escudo na nave.

| Nome | Raridade | Bônus de escudo % | Bônus de velocidade % | Slots | Efeito especial | Custo |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Inferior | +5% | +3% | 1 | — | 100.000 créditos |
| **Adaptive Core II** | Comum | +8% | +4% | 2 | — | 4.000 Thulium |
| **Adaptive Core III** | Raro | +15% | +5% | 3 | — | Só por criação |

---

## Células de escudo {#shield-cells}

As células de escudo se encaixam dentro de núcleos de escudo ou de núcleos adaptativos (tantas quantos forem os slots do núcleo) para reforçar esse núcleo. Em um núcleo de escudo, elas aumentam também a absorção dele, em pontos, e com ela a parte de cada impacto que seus escudos recebem. Há duas famílias de quatro níveis cada uma: as **Capacity Shield Cells** dão mais escudo e recarga, as **Absorption Shield Cells** mais absorção (em cada nível, o dobro da absorção e metade do escudo e da recarga da Capacity do mesmo nível). A Capacity ajuda uma nave em que o escudo decide o combate; a Absorption, uma em que quem decide é o casco. Um núcleo com todos os slots cheios de uma mesma célula: um Light Shield Core (1 slot) fica entre 47 e 55%, um Basic Shield Core (2 slots) entre 52 e 68% e um Heavy Shield Core (3 slots) entre 56 e 80%, das células Capacity de nível I às Absorption de nível IV. Desequipar o núcleo, ou consumi-lo como doador de uma combinação da [Forja](/wiki/06-Items/Forge.md), devolve as células dele ao inventário.

| Nome | Raridade | Capacidade extra | Recarga extra | Absorção extra | Custo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Inferior | +3.000 | +250/s | +2% | 30.000 créditos |
| **Capacity Shield Cell II** | Comum | +6.000 | +500/s | +3% | Só por criação |
| **Capacity Shield Cell III** | Raro | +9.000 | +750/s | +4% | Só por criação |
| **Capacity Shield Cell IV** | Épico | +12.000 | +1.000/s | +5% | Só por criação |
| **Absorption Shield Cell I** | Inferior | +1.500 | +125/s | +4% | 30.000 créditos |
| **Absorption Shield Cell II** | Comum | +3.000 | +250/s | +6% | Só por criação |
| **Absorption Shield Cell III** | Raro | +4.500 | +375/s | +8% | Só por criação |
| **Absorption Shield Cell IV** | Épico | +6.000 | +500/s | +10% | Só por criação |

O nível I de cada família é vendido por 30.000 créditos. Os níveis II a IV são feitos na [Montagem](/wiki/06-Items/Overview.md#upgrading-modules), cada um a partir da célula da mesma família um nível abaixo (uma Capacity Shield Cell II a partir de uma Capacity Shield Cell I, uma III a partir de uma II, uma IV a partir de uma III), com Thulium, drops e Velkonite Reinforced Plates do seu Skylab (2, 4 e 6 placas). Uma célula nunca muda de família: você escolhe Capacity ou Absorption ao comprar o nível I. A célula nova mantém o grau de encantamento da célula que consome, e os bônus dela são sorteados de novo ([Melhorias de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). As células não cabem em um [slot de habilidade](/wiki/03-Mechanics/Abilities.md); o lugar delas é dentro de escudos e de núcleos adaptativos.
