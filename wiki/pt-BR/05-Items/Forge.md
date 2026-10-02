<!-- wiki-i18n source: 8adf8c0b49b112f5 -->
<!-- wiki-i18n title: Forja -->
# A Forja {#the-forge}

A **Forja** é a segunda aba da página da Montagem (e da janela da Montagem em voo). Ela faz duas coisas com o equipamento que você tem: **eleva um item em um grau** por créditos e drops de alienígenas, e **combina duas cópias** de um item em uma que mantém o melhor das duas. Ela substituiu a antiga Câmara de Fusão, que exigia cinco itens idênticos e deixava o resultado a cargo de um sorteio de 25%.

## O que pode ser forjado {#what-can-be-forged}

Lasers, amplificadores de laser, núcleos de escudo, células de escudo, motores, propulsores, núcleos adaptativos e Repair Drones: qualquer peça de equipamento que possa levar [bônus de encantamento](/wiki/05-Items/Overview.md). Ela pode estar no seu inventário, em uma nave (continua lá e funciona com o novo grau na hora) ou encaixada em outro item. Drones, naves, munição, recursos e boosters não podem ser forjados, e nada no Cache de Transporte também pode: retire-o primeiro.

## Subir de grau {#tier-up}

Escolha um item e o painel mostra o grau dele, o grau que ele alcançaria, o que isso muda (quantos bônus ele pode comportar e o tamanho deles) e o preço, com o que você tem de cada parte: em verde quando você tem o bastante, em vermelho quando não tem, e quantos faltam. Quando você tem tudo, **Subir de grau** eleva o item em exatamente um grau. Não há saltos: para chegar a Eterno, um item passa por Maculado, Divino e Rompedor, cada um com o seu preço.

| Etapa | Sucesso | Créditos | Thulium | Materiais |
| :--- | :---: | :---: | :---: | :--- |
| Padrão para Maculado | 100% | 10.000 | – | 5 Ship Fragment, 15 Daraxium |
| Maculado para Divino | 90% | 50.000 | – | 30 Ship Fragment, 45 Nyxite |
| Divino para Rompedor | 75% | 200.000 | – | 20 Reinforced Hull Plate, 120 Cataclysite, 2 Dark Matter Plate |
| Rompedor para Eterno | 60% | 500.000 | 2.000 | 8 Power Core, 240 Quorvium, 2 Dark Matter Plate |

- Os **materiais** vêm das suas pilhas soltas: itens em uma nave e pilhas no Cache de Transporte não são usados. O painel avisa quando os que faltam estão no cache.
- **Uma etapa pode falhar.** O item continua exatamente como estava, os créditos se perdem, e metade dos materiais e metade do Thulium voltam (arredondado para baixo; de duas Dark Matter Plates, uma). O painel informa a chance e isso antes de você pressionar.
- **Em caso de sucesso**, cada bônus que o item tem é sorteado de novo na faixa do novo grau e fica com o melhor valor, e as vagas de bônus extras do grau recebem novos bônus em outros atributos do item. O resultado aparece acima do painel; o item continua selecionado, então a próxima etapa dele já está na tela.
- Subir de grau é instantâneo.

### Placas de Dark Matter {#dark-matter-plates}

As duas últimas etapas pedem **2 Dark Matter Plates** cada um, além de tudo o mais. Uma placa é prensada na [Montagem](/wiki/05-Items/Overview.md) a partir de **5 Dark Matter, 1 Velkonite Reinforced Plate e 1 Orvium Reinforced Plate** (250 Thulium, 2 minutos), então uma etapa exige 10 Dark Matter, 2 Velkonite Reinforced Plates e 2 Orvium Reinforced Plates. A Dark Matter vem do [buraco negro](/wiki/03-Mechanics/Black-Hole.md): cerca de cinco foguetes N.I.K.E. (veja [Foguetes](/wiki/05-Items/Rockets.md)) rendem dez; uma N.I.K.E. que encontra uma nave no caminho atinge essa nave e não rende nenhuma. As placas são tiradas das suas pilhas soltas como os outros materiais, e o painel as nomeia se faltarem.

### Bônus por grau {#buffs-by-tier}

| Grau | Máximo de bônus | Tamanho de cada bônus |
| :--- | :---: | :---: |
| Maculado | 1 | +2% a +5% |
| Divino | 2 | +4% a +8% |
| Rompedor | 3 | +6% a +11% |
| Eterno | 4 | +9% a +15% |

O equipamento feito antes da Forja mantém os bônus com que foi sorteado, e eles costumam ser menores que os da tabela (uma peça Divina daquela época pode ter +2%). Nada os aumenta sozinho: subir de grau sorteia cada bônus de novo na faixa do novo grau e fica com o melhor valor, e uma combinação fica com o melhor valor de cada atributo.

Um item não pode comportar mais bônus do que tem atributos: um núcleo de escudo tem quatro, um laser três (o Quantum Laser 1 e o 2 têm dois), um motor, um propulsor ou um núcleo adaptativo dois, um Crit Amp 1 ou um Repair Drone um, os amps de crítico mais altos dois, os amps de dano e as células de escudo três. Quando o grau seguinte não comporta mais bônus do que o item consegue levar, o painel avisa: o grau então só deixa os bônus mais fortes. Os bônus de alcance nunca passam de +5%.

O **bônus de absorção de um escudo** (e a absorção extra de uma célula de escudo) multiplica o atributo, então vale pontos de [absorção](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) em proporção a ele: +5% sobre os 50% de um Heavy Shield Core são +2,5 pontos, e +15% em cada peça do melhor conjunto (um Heavy Shield Core e três Sovereign Shield Cells, 80% no total) são +12 pontos. Um conjunto Eterno rende entre +7 e +12 pontos, cerca de 10 em média; com o Shield Absorbance Boost da Loja de PR (+10 pontos no limite; os pontos de reset do jogo inteiro compram 34 dos 100 níveis dele, +3,4 pontos), isso leva uma nave a 95%, e a absorção só passa de 100% com o bônus no limite, o que o atributo permite: a penetração de escudo de quem ataca é descontada dele. Um conjunto Divino rende entre 3 e 6 pontos.

Motores, propulsores, núcleos adaptativos e Repair Drones mudam muito pouco com um bônus percentual (um Engine II soma 4 de velocidade, então +12% é meio ponto): forje-os se quiser o grau, não pelos atributos.

### Onde os materiais caem {#where-the-materials-drop}

| Material | Cai de |
| :--- | :--- |
| **Ship Fragment** | todo alienígena |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | nenhum alienígena: a Montagem a prensa a partir de Dark Matter (o [buraco negro](/wiki/03-Mechanics/Black-Hole.md)) e das placas do Skylab |

Os cristais seguem os graus: o Daraxium é azul como o Maculado, a Nyxite é amarela como o Divino, a Cataclysite é laranja como o Rompedor e o Quorvium é violeta como o Eterno. Todas as fontes, com as chances e as quantidades, estão na página [Recursos](/wiki/05-Items/Resources.md) e na página de cada alienígena; o booster Resource Magnet acrescenta 25% ao que uma caixa contém.

## Combinar {#merge}

Duas cópias do mesmo item (dois Light Shield Cores, dois Quantum Laser 2) viram uma. Mude para **Combinar** e clique no item que você quer manter (a **base**), depois em uma segunda cópia (o **doador**). O painel mostra o resultado antes de você confirmar.

- **A base é mantida.** Ela continua no lugar dela: pode estar em uma nave, ou encaixada em outro item, e os módulos encaixados nela ficam. **O doador é consumido.** Ele precisa estar solto (não em uma nave, não encaixado), e os módulos encaixados nele voltam ao seu inventário.
- **O resultado tem o maior dos dois graus** e, para cada atributo, o **melhor dos dois valores**.
- **Ele nunca comporta mais bônus do que o grau dele permite.** Se os dois itens juntos têm mais bônus do que o grau do resultado comporta, os melhores são mantidos e o resto é descartado; a tabela os marca (riscados, “acima do limite”). Para comportar mais bônus, suba o item de grau primeiro. Uma combinação nunca sorteia nada: o que a prévia mostra é o que você recebe.
- **Uma combinação custa créditos conforme o grau que gera**: 5.000 para Maculado, 25.000 para Divino, 100.000 para Rompedor, 250.000 para Eterno. Nenhum material.
- Uma combinação que não mudaria nada (o resultado não é melhor que a base) é recusada.
- Depois de uma combinação, o resultado continua selecionado e o espaço do doador fica vazio: coloque o próximo doador ou volte para Subir de grau.

Uma combinação refina um item; não o multiplica. Dois núcleos de escudo Divinos combinados valem cerca de um ponto e meio de bônus a mais que um só. A utilidade dela é escolher: um núcleo Divino com os atributos que você quer, ou um grau passado para o item que está na sua nave sem precisar retirá-lo.

## Melhorias de módulos na Montagem {#module-upgrades-in-the-assembly}

Os dois melhores lasers, os melhores amps de laser, a melhor célula de escudo e os melhores propulsores, o Heavy Shield Core e o Engine III não são vendidos. Você os faz na aba **Criação** da Montagem, melhorando a peça um degrau abaixo: um Pulse Amp em um **Nova Amp**, um Prism Amp em um **Apex Amp**, uma Prime Shield Cell em uma **Sovereign Shield Cell**, um Ion Thruster em um **Plasma Thruster**, um Thruster II em um **Thruster III**, um Basic Shield Core em um **Heavy Shield Core**, um Engine II em um **Engine III**, um Quantum Laser 3 em um **Starfire-3** e um Starfire-3 em um **Helios Beam**. O que a Forja tem a ver com isso é o grau.

- **O grau permanece.** Uma melhoria consome uma cópia da peça, e o novo item tem o grau dessa cópia: um Pulse Amp Divino faz um Nova Amp Divino, um Padrão faz um Nova Amp Padrão. O que você pagou à Forja não se perde. A melhoria não acrescenta grau nenhum por conta própria, então uma peça Padrão sempre gera um resultado Padrão.
- **Os bônus são sorteados de novo.** O novo item recebe bônus novos para o grau dele: tantos quantos o grau comporta e quantos atributos o novo item tem (um Nova Amp Divino comporta dois), cada um na faixa do grau da tabela acima, em atributos que o Nova Amp tem. Nada é copiado da peça antiga, então os novos bônus podem ser melhores ou piores que os que ela tinha; em média, são iguais. Os bônus são sorteados no momento em que você coloca a tarefa na fila, e o que você coleta é o que foi sorteado: esperar para coletar não muda nada. O motivo é que a melhoria constrói um item novo, e os dados da Forja são lançados sobre o item que você tem em mãos. O grau é a parte que custa: uma peça Eterna representa mais de um milhão de créditos em etapas da Forja, enquanto um bônus é alguns por cento de um atributo.
- **Placas.** Além de Thulium e do que os alienígenas deixam cair, toda melhoria de módulo exige **Velkonite Reinforced Plates**: 3 para um amp, 6 para uma célula ou um propulsor, 6 para um Heavy Shield Core ou um Engine III, 4 para um Thruster III e 8 para um Starfire-3 (o Helios Beam exige Orvium Reinforced Plates em vez delas, 18 no total). Os alienígenas não as deixam cair. A Forja do seu [Skylab](/wiki/03-Mechanics/Skylab.md) as faz a partir de minério de Velkonite, 40 de minério por placa no nível 1 da Forja. Um Coletor de Velkonite de nível 1 extrai 12 de minério por hora, então as placas de um amp são 10 horas de mineração e as de uma célula ou de um propulsor, 20 (4 e 8 horas com um coletor de nível 5). De onde vem cada material está na página [Recursos](/wiki/05-Items/Resources.md). As etapas da própria Forja exigem drops e créditos, e as etapas mais altas exigem placas também (Divino para Rompedor: 20 Reinforced Hull Plates e 2 Dark Matter Plates; Rompedor para Eterno: 2 Dark Matter Plates), o que é diferente das placas de Velkonite e de Orvium das melhorias de módulos.
- **Qual cópia é usada.** Você escolhe. Quando você tem cópias que diferem (outro grau ou outros bônus), o cartão da receita as mostra como uma fileira de blocos: clique na que quer usar, e a linha sob os blocos mostra no que ela se torna (“Pulse Amp Divino”, depois “Resultado: Nova Amp Divino”). Se você não escolher nenhuma, vai a mais simples: o menor grau primeiro, e entre cópias de um mesmo grau a mais antiga, sejam quais forem os bônus delas. Uma cópia Divina ou melhor nunca é usada enquanto houver uma mais simples solta. Usar uma cópia acima de Padrão pergunta antes e diz o nome do item.
- **Quais cópias podem ser usadas.** As soltas: uma cópia em uma nave (em um slot de habilidade também), encaixada em outro item, com células ou propulsores próprios encaixados nela, ou no [Cache de Transporte](/wiki/03-Mechanics/Cargo.md) não pode ser usada, e a Montagem avisa. Retire-a da nave ou do cache primeiro. Duas melhorias iniciadas juntas não podem usar a mesma cópia.

- **O Starfire-3 também é uma melhoria.** Ele é feito a partir de um **Quantum Laser 3** (com 1.500 Thulium, 100.000 créditos, drops e 8 Velkonite Reinforced Plates: veja [Lasers](/wiki/05-Items/Lasers.md)), e tudo o que foi dito acima vale: um Quantum Laser 3 Divino faz um Starfire-3 Divino com dois bônus novos, você escolhe a cópia, o cartão pergunta antes de consumir uma acima de Padrão, e o Quantum Laser 3 precisa estar solto: retire-o primeiro no hangar, e o botão Montar diz “Retire Quantum Laser 3 primeiro” até você fazer isso. O grau segue então adiante: um Starfire-3 Divino faz um Helios Beam Divino.

- **O Helios Beam também é uma melhoria.** Ele é feito a partir de um **Starfire-3** (com 2.000 Thulium, drops e 18 Orvium Reinforced Plates: veja [Lasers](/wiki/05-Items/Lasers.md)), e tudo o que foi dito acima vale: um Starfire-3 Divino faz um Helios Beam Divino com dois bônus novos (ele comporta dois dos três atributos dele), você escolhe a cópia, o cartão pergunta antes de consumir uma acima de Padrão, e o Starfire-3 precisa estar solto. Um laser fica encaixado em uma nave e leva amps, então muitas vezes não está solto: retire-o primeiro no hangar (os amps dele voltam ao seu inventário), e o botão Montar diz “Retire Starfire-3 primeiro” até você fazer isso.

As receitas, os custos delas e os números por trás da regra estão na [Visão geral dos itens](/wiki/05-Items/Overview.md#upgrading-modules) e, para o Starfire-3 e o Helios Beam, na página [Lasers](/wiki/05-Items/Lasers.md).

## Servidores antigos {#old-servers}

Um servidor de jogo que não foi atualizado para a Forja mostra “A Forja ainda não está neste servidor” no lugar da aba; a Criação funciona como antes. Um cliente do jogo anterior à Forja mostra a antiga aba Fusão em um servidor atualizado e recebe o aviso para atualizar.
