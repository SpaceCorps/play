<!-- wiki-i18n source: 6d47517c2e0ba61e -->
<!-- wiki-i18n title: Skylab -->
# Skylab

O Skylab é a sua instalação orbital pessoal. Ele constrói e melhora módulos que produzem créditos e Thulium, extraem minério, forjam as placas que a Montagem transforma nos melhores lasers e, a partir do nível 10 do Núcleo, pesquisam as tecnologias de que a Montagem precisa. Ele trabalha para você mesmo quando você está offline.

No nível 10 do Núcleo, o Skylab ainda cresce: uma **ponte** liga o Núcleo a um segundo Núcleo com seis slots a mais para módulos, e dois módulos a mais se encaixam nele, a **Impressora de munição** e a **Fábrica de foguetes**, que produzem munição e foguetes do nada (veja [A ponte e o Núcleo 2](#the-bridge-and-core-2)).

> [!NOTE]
> **O que mudou na 0.4.10.** Cada módulo do Skylab agora tem a sua própria tabela de produção, preços e tempos, nível por nível. Você manteve os seus níveis: nada foi cobrado e nada foi devolvido pela diferença. O que as suas minas e os seus coletores guardavam nos armazenamentos quando a atualização chegou foi pago **uma única vez, pela taxa antiga**: os créditos e o Thulium foram para a sua conta, o minério para o seu Depósito de recursos, e os armazenamentos recomeçaram vazios.
>
> Duas regras são novas. **A Usina solar produz só 25% da sua energia enquanto é melhorada**, então na maioria das estações todas as minas e todos os coletores param até a melhoria terminar (veja [Módulo Usina solar](#solar-module) e [Planejando uma melhoria da Usina solar](#timing-a-solar-upgrade)). **O Depósito de recursos tem um limite próprio para cada minério**: um dia da produção do coletor no nível 1, quatro dias no nível 20.

> [!NOTE]
> **O que mudou na 0.4.15.** O passo do Núcleo do nível 9 para o nível 10 agora custa **2.000 Thulium** a mais, e quando termina surgem uma **ponte** e um segundo Núcleo, o **Núcleo 2**, com seis novos slots de módulo. A Usina solar se muda para o Núcleo 2. Dois módulos novos se encaixam nele: a **Impressora de munição** e a **Fábrica de foguetes**. Além disso, a Usina solar produz mais energia a partir do nível 7, para que uma estação completa continue coberta. Nada do que você construiu se perde: um Núcleo que já está no nível 10 ou mais tem a ponte na hora e não paga nada.

![The Skylab station fully grown](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage and power of every module, with the 0.4.10 numbers](../../img/wiki-img/shots/skylab-table.jpg)

## Em um minuto {#in-one-minute}

- Construa primeiro a **Usina solar**: sem a energia dela, nada no Skylab funciona. A Mina de créditos não custa nada para construir, e a Mina de Thulium custa 5.000 créditos e 500 Thulium.
- As minas e os coletores enchem um **armazenamento** (de 72 horas) enquanto você está fora. **Coletar** o leva para a sua conta (créditos, Thulium) ou para o seu Depósito de recursos (minério).
- A **Mina de Thulium** é a sua principal fonte de Thulium: 50 por hora no nível 1, 1.600 no nível 20. A Mina de créditos produz 500 créditos por hora no nível 1 e 50.000 no nível 20.
- O **Núcleo** dita o ritmo: nenhum módulo passa dele, e a subida dele sozinha leva cerca de 16 dias e meio.
- No **nível 10 do Núcleo**, uma **ponte** constrói o **Núcleo 2**, com seis slots a mais para módulos, e a **Impressora de munição** e a **Fábrica de foguetes** se encaixam nele. O passo para o nível 10 custa 2.000 Thulium a mais.
- **A Usina solar produz só 25% da sua energia enquanto é melhorada**, então as suas minas e os seus coletores param até ela terminar. [Planeje isso](#timing-a-solar-upgrade).

## Visão geral {#overview}

O Skylab funciona no seu próprio relógio, separado da sua nave: os módulos produzem e forjam enquanto você está fora. O que você faz é construir, melhorar, manter a energia em equilíbrio e coletar. A página tem quatro visões da mesma estação: **Estação** (a estação em 3D, com uma etiqueta sobre cada módulo; clique em uma para abrir a ficha do módulo, ou pressione **1** a **9**), **Lista** (um cartão para cada módulo), **Tabela** (os números de todos os módulos em uma só tabela) e **Pesquisa** (a tela própria do Centro de Pesquisa, veja [Pesquisa](/wiki/03-Mechanics/Research.md)). Passar o mouse sobre **Construir** ou **Melhorar** mostra o que o próximo nível muda, quanto custa e quanto tempo leva.

Onze módulos formam a estação:

| Módulo | O que produz ou faz | Construído a partir de |
| :--- | :--- | :--- |
| **Núcleo** | Define o nível mais alto de todos os outros módulos | Sempre presente |
| **Usina solar** | Produz energia | Qualquer nível do Núcleo |
| **Mina de créditos** | Produz [créditos](/wiki/01-General/Getting-Started.md) | Qualquer nível do Núcleo |
| **Mina de Thulium** | Produz [Thulium](/wiki/01-General/Getting-Started.md) | Qualquer nível do Núcleo |
| **Coletor de Velkonite** | Extrai minério de Velkonite | Núcleo no nível 5 |
| **Coletor de Orvium** | Extrai minério de Orvium | Núcleo no nível 5 |
| **Depósito de recursos** | Guarda o minério | Núcleo no nível 5 |
| **Forja** | Forja o minério em placas | Núcleo no nível 5 |
| **Centro de Pesquisa** | Transforma recursos em ciência e pesquisa [tecnologias](/wiki/03-Mechanics/Research.md) | Núcleo no nível 10 |
| **Impressora de munição** | Imprime munição x2, x3 ou x4 do nada | Núcleo no nível 10, no Núcleo 2 |
| **Fábrica de foguetes** | Fabrica foguetes da loja do nada | Núcleo no nível 10, no Núcleo 2 |

A **ponte** e o **Núcleo 2** não são módulos: eles surgem quando o Núcleo chega ao nível 10, e o Núcleo 2 não tem nível próprio (veja [A ponte e o Núcleo 2](#the-bridge-and-core-2)).

**Missões para ele.** Dez [missões da estação](/wiki/03-Mechanics/Quests.md#station-missions) no Mission Control conduzem você pelo Skylab: construir a Usina solar, uma Mina de créditos e uma Mina de Thulium, levar o Núcleo e a Usina solar a níveis mais altos, coletar os seus primeiros 50.000 créditos e abrir a cadeia de suprimentos, e pagam um pouco por cada etapa. A primeira está aberta desde o nível 1.

## A estação em cada nível {#the-station-at-every-level}

Estas são as visões da Estação do Skylab em cada nível de 1 a 20, todas do mesmo ângulo, com todos os módulos no mesmo nível. A visão encaixa a estação inteira na imagem, então a escala não é a mesma em todas: ela dá um salto quando a forma cresce. A estação cresce por etapas: a forma muda nos **níveis 1, 5, 10, 15 e 20**, e entre eles cada nível acende **mais uma lâmpada** no colar de cada módulo (o número de lâmpadas acesas é o nível, e o anel de vinte lâmpadas do Núcleo se enche do mesmo jeito).

As imagens a partir do nível 10 mostram a estação como era antes da ponte: desde a 0.4.15, o passo do Núcleo para o nível 10 também constrói a ponte e o Núcleo 2, e a Usina solar fica no Núcleo 2 (veja [A ponte e o Núcleo 2](#the-bridge-and-core-2)).

**Níveis 1 a 4.** Os quatro primeiros módulos ao redor do Núcleo: a Usina solar, a Mina de créditos, a Mina de Thulium e a baía de atracação que abriga a sua nave. A cadeia de suprimentos ainda não pode ser construída.

![Nível 1](../../img/skylab/wiki/level-01.jpg)
![Nível 2](../../img/skylab/wiki/level-02.jpg)
![Nível 3](../../img/skylab/wiki/level-03.jpg)
![Nível 4](../../img/skylab/wiki/level-04.jpg)

**Níveis 5 a 9.** Com o Núcleo no nível 5, a cadeia de suprimentos pode ser construída: os dois coletores em suas estruturas acima da estação, o Depósito de recursos na porta nordeste do Núcleo e a Forja na porta noroeste dele (aqui eles aparecem construídos).

![Nível 5](../../img/skylab/wiki/level-05.jpg)
![Nível 6](../../img/skylab/wiki/level-06.jpg)
![Nível 7](../../img/skylab/wiki/level-07.jpg)
![Nível 8](../../img/skylab/wiki/level-08.jpg)
![Nível 9](../../img/skylab/wiki/level-09.jpg)

**Níveis 10 a 14.** O Núcleo ganha o seu anel, as minas e os coletores assumem a forma maior e a Mina de Thulium ganha um anel próprio.

![Nível 10](../../img/skylab/wiki/level-10.jpg)
![Nível 11](../../img/skylab/wiki/level-11.jpg)
![Nível 12](../../img/skylab/wiki/level-12.jpg)
![Nível 13](../../img/skylab/wiki/level-13.jpg)
![Nível 14](../../img/skylab/wiki/level-14.jpg)

**Níveis 15 a 19.** As minas se enchem de caixas e cristais, a baía de atracação ilumina a sua aproximação e o conjunto da Usina solar ganha um topo.

![Nível 15](../../img/skylab/wiki/level-15.jpg)
![Nível 16](../../img/skylab/wiki/level-16.jpg)
![Nível 17](../../img/skylab/wiki/level-17.jpg)
![Nível 18](../../img/skylab/wiki/level-18.jpg)
![Nível 19](../../img/skylab/wiki/level-19.jpg)

**Nível 20.** O topo da escada: a coroa no Núcleo e as torres plenamente desenvolvidas das minas e da cadeia de suprimentos.

![Nível 20](../../img/skylab/wiki/level-20.jpg)

**Os cartões dos nove módulos.** A visão em Lista da mesma estação no nível 20: os quatro módulos da primeira versão, o Coletor de Velkonite, o Coletor de Orvium, o Depósito de recursos e a Forja, que vieram com a cadeia de suprimentos, e o Centro de Pesquisa. Cada cartão mostra o nível do módulo, a produção, a energia e o interruptor dele. Todos os cartões mostram o nível 20, exceto o do Centro de Pesquisa: ele tem os níveis 1 a 10, então o cartão dele mostra o nível 10, o máximo. A Impressora de munição e a Fábrica de foguetes têm cartões próprios na mesma visão; eles são descritos [mais abaixo](#the-bridge-and-core-2).

![A visão em Lista no nível 20: os cartões do Núcleo, da Usina solar, da Mina de créditos, da Mina de Thulium, do Coletor de Velkonite, do Coletor de Orvium, do Depósito de recursos, da Forja e do Centro de Pesquisa](../../img/skylab/wiki/modules.jpg)

## Os quatro primeiros módulos {#the-first-four-modules}

### Módulo Núcleo {#core-module}

O coração do seu Skylab. O nível do Núcleo decide o nível mais alto de todos os outros módulos: você não pode melhorar nenhum módulo acima do seu Núcleo. O Núcleo vai até o nível 20 e, a partir do **nível 5**, abre a cadeia de suprimentos descrita mais abaixo. As melhorias dele custam créditos, e o passo para o **nível 10** custa **2.000 Thulium** a mais e constrói a ponte e o Núcleo 2 (veja [A ponte e o Núcleo 2](#the-bridge-and-core-2)). No total são 112.326 créditos até o nível 10 e 6.647.504 até o nível 20, mais esses 2.000 Thulium, e levam cerca de 16 dias e meio (veja [Tempos de melhoria](#upgrade-times)).

### Módulo Usina solar {#solar-module}

A energia é o sangue do Skylab. O módulo Usina solar produz a energia que todos os outros módulos usam.

- **Importância**: se o seu consumo de energia for maior que a energia produzida, as suas minas e os seus coletores param de produzir.
- **Energia produzida**: um módulo Usina solar no nível N produz o bastante para **todos os outros módulos no nível N**, e cerca de um décimo a mais: 255 no nível 1, 965 no nível 7, 17.890 no nível 20. Uma Usina solar de nível 7 alimenta uma estação inteira no nível 7 (veja Gerenciamento de energia para todos os níveis).
- **Preço**: construir a Usina solar custa **500 créditos e 50 Thulium**. As melhorias dela custam o mesmo e levam o mesmo tempo que as da Forja: de 8.000 créditos e 25 Thulium para o nível 2 (5 minutos) a 9.000.000 de créditos e 10.000 Thulium para o nível 20 (24 horas).
- **Melhoria**: enquanto é melhorada, a Usina solar produz só **25%** da energia do seu nível atual, e a do novo nível a partir do momento em que a melhoria termina. Uma estação que usa mais do que isso para: toda mina e todo coletor deixam de produzir, e a Forja não inicia nenhum lote novo até a melhoria terminar. Para quase toda estação é assim: ela só continua funcionando durante a melhoria se todos os outros módulos estiverem pelo menos cinco níveis abaixo da Usina solar (seis níveis a partir do nível 10 da Usina solar). Planeje a melhoria da Usina solar como um apagão das suas minas (veja Construção e melhoria).
- **Lugar**: a partir do nível 10 do Núcleo, a Usina solar fica no Núcleo 2, na outra ponta da estação (veja [A ponte e o Núcleo 2](#the-bridge-and-core-2)).

### Mina de créditos e Mina de Thulium {#credit-farm-and-thulium-farm}

- **Mina de créditos**: produz créditos ao longo do tempo: **500 por hora no nível 1, 50.000 no nível 20** (nível 5: 2.500; nível 10: 7.500; nível 15: 17.000). Construí-la não custa nada.
- **Mina de Thulium**: produz Thulium ao longo do tempo: **50 por hora no nível 1, 1.600 no nível 20** (nível 5: 180; nível 10: 450; nível 15: 950). Construí-la custa 5.000 créditos e 500 Thulium.
- Ambas precisam de energia, e cada uma guarda 72 horas do que produz até você coletar.

## A cadeia de suprimentos {#the-supply-chain}

Quatro módulos transformam o tempo longe do teclado nas placas para os seus melhores lasers. O minério vem **só** dos coletores (todos os materiais e moedas estão na página [Recursos](/wiki/06-Items/Resources.md)): os alienígenas não o soltam e a Loja não o vende. (Uma [escavadeira gigante](/wiki/03-Mechanics/Giant-Excavator.md) também solta um pouco de Velkonite e Orvium em caixas, mas esse minério vai para a sua carga, onde é combustível do Centro de Pesquisa, e a Forja não o pega.)

1. Um **coletor** extrai minério, uma quantidade por hora, para o seu próprio armazenamento (o equivalente a 72 horas).
2. **Coletar** move o minério do armazenamento para o **Depósito de recursos**, onde cada minério fica guardado à parte.
3. A **Forja** pega no depósito o minério de que precisa quando um lote começa e faz placas, 10 segundos por placa, um lote de cada vez.
4. **Coletar placas** move as placas prontas para o seu inventário (a sua nave precisa estar pousada). A [Montagem](/wiki/06-Items/Lasers.md) as transforma em um Quantum Laser III, um Starfire-III ou um Helios Beam e, uma de cada com 5 Dark Matter, em uma Dark Matter Plate, que a [Forja](/wiki/06-Items/Forge.md) e o último nível de cada cadeia de melhoria pedem.

### Coletor de Velkonite e Coletor de Orvium {#velkonite-collector-and-orvium-collector}

- **Minério**: o Coletor de Velkonite extrai **10 de Velkonite por hora** no nível 1 e o Coletor de Orvium **10 de Orvium por hora**, e cada nível tem a sua própria taxa: até 80 de Velkonite e 40 de Orvium por hora no nível 20 (nível 5: 18 e 14 por hora; nível 10: 32 e 24).
- **Armazenamento**: cada um guarda 72 horas do seu minério e para de extrair quando está cheio.
- **Coletar**: move o minério para o Depósito de recursos, até onde houver espaço. Sem depósito construído, ou com o depósito cheio daquele minério, não há onde colocá-lo e o botão diz o motivo. O resto fica no armazenamento.
- **Energia**: 20 (Velkonite) e 30 (Orvium) no nível 1, crescendo 15% por nível.

### Depósito de recursos {#resource-storage}

- **Depósito**: guarda o Velkonite e o Orvium separados, e comporta uma quantidade diferente de cada um: **240 de cada no nível 1**, até 7.680 de Velkonite e 3.840 de Orvium no nível 20 (nível 5: 720 e 560; nível 10: 1.920 e 1.440).
- **Limite**: um dia da produção do coletor dele no nível 1, até quatro dias no nível 20. O armazenamento de um coletor guarda três dias, então, a partir do nível 13, o depósito comporta pelo menos um armazenamento cheio.
- **Acima do limite**: se um depósito tem mais do que o seu limite (o pagamento da atualização 0.4.10 pode tê-lo deixado assim), nada é tirado, mas Coletar não acrescenta mais desse minério até você ter gastado um pouco.
- O minério só entra coletando de um coletor e só sai para a Forja. Ele nunca chega ao seu inventário.
- **O minério guardado permanece** no reset da temporada.
- **Energia**: 10 no nível 1, crescendo 10% por nível. Ele não pode ser desligado.

### Forja {#forgery}

- **Placas**: a Forja faz uma **Velkonite Reinforced Plate** a partir de Velkonite e uma **Orvium Reinforced Plate** a partir de Orvium: **40 de Velkonite** ou **80 de Orvium** por placa no nível 1, caindo a cada nível até 30 e 60 no nível 20 (nunca abaixo de 75%).
- **Lotes**: um lote de um tipo de placa por vez, **10 placas no nível 1** e mais 5 para cada nível acima. O minério sai do Depósito de recursos no instante em que o lote começa, e cada placa leva **10 segundos**. As placas são feitas uma depois da outra, também enquanto você está fora.
- **Coletar placas**: move as placas prontas para o seu inventário enquanto a sua **nave está pousada**, e o resto do lote continua. Um novo lote pode começar quando a Forja estiver vazia.
- Um lote em andamento termina mesmo que você desligue a Forja ou a melhore. Um **novo** lote precisa que a Forja esteja ligada, sem estar em melhoria, e que a energia do Skylab esteja em equilíbrio.
- **Energia**: 30 no nível 1, crescendo 15% por nível.
- **Não vendável**: as placas que a Forja faz não podem ser vendidas no [Leilão](/wiki/03-Mechanics/Auction.md#marketable-items); senão seriam a maior mercadoria do Mercado. Elas continuam servindo de material para a Montagem e a Forja.

### Construindo os módulos {#building-them}

Os dois coletores custam **10 Ship Fragments, 20.000 créditos e 500 Thulium** cada um, o Depósito de recursos **10 Ship Fragments, 5.000 créditos e 250 Thulium** e a Forja **10 Ship Fragments, 5.000 créditos e 500 Thulium**; os quatro exigem o Núcleo no nível 5.

- Os Ship Fragments são tirados do seu inventário (não do Cache de Transporte) e a sua nave precisa estar pousada. A ficha de construção mostra o que você tem em comparação com o que é preciso, e o que falta.
- Eles consomem energia. Antes de construir, a ficha mostra o seu balanço de energia agora e depois: **construir pode deixar uma estação em déficit** quando a sua Usina solar está atrás dos outros módulos, e um único déficit para todas as minas e todos os coletores. Desligue um módulo ou melhore antes a Usina solar.
- Os dois coletores ficam pendurados em estruturas acima da estação, o Depósito de recursos fica na porta nordeste do Núcleo e a Forja, na porta noroeste dele.

## O Centro de Pesquisa {#the-research-centre}

O nono módulo transforma recursos em ciência e pesquisa as tecnologias de que a Montagem precisa antes de criar qualquer coisa nova. Ele é construído a partir do nível 10 do Núcleo, tem os níveis 1 a 10, consome energia e não pode ser desligado. Os números dele, o que ele queima como combustível, o boost e toda a árvore de tecnologias estão na página [Pesquisa](/wiki/03-Mechanics/Research.md). As tecnologias mais altas também exigem Dark Matter, que você adiciona ao Centro: [Dark Matter e Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) explica como conseguir.

## A ponte e o Núcleo 2 {#the-bridge-and-core-2}

A melhoria do Núcleo para o **nível 10** constrói uma **ponte** e um segundo Núcleo. A ponte se encaixa na porta norte do Núcleo, onde ficava a Usina solar, e o liga, na outra ponta, ao **Núcleo 2**.

- **Custo**: o passo do nível 9 para o nível 10 custa **2.000 Thulium** além dos seus 38.443 créditos, e leva o mesmo tempo de antes, 1 h 20 min. A ponte e o Núcleo 2 não custam mais nada e não levam tempo próprio. Uma melhoria que já estava em andamento mantém o preço com que começou, e um Núcleo no nível 10 ou mais não paga nada.
- **O Núcleo 2 não tem nível**: não há nada para melhorar nem para pagar. Ele dá à sua estação **seis slots a mais para módulos**, e o cartão do Núcleo mostra quantos estão livres.
- **A Usina solar se muda**: a Usina solar deixa a porta norte do Núcleo, que agora a ponte ocupa, e passa para a porta norte do Núcleo 2, na outra ponta da estação. O nível dela, a energia dela e uma melhoria em andamento ficam intactos.
- **Uma regra, não uma obra**: onde cada módulo fica depende só do nível do Núcleo. A ponte surge no momento em que a melhoria do Núcleo para o nível 10 termina (um som discreto e uma mensagem avisam você), e um Skylab cujo Núcleo já está no nível 10 ou mais a tem na próxima vez que você olhar. Nenhum módulo se perde ou é apagado, e só a Usina solar muda de lugar.
- **Slots**: a **Impressora de munição** ocupa o slot nordeste do Núcleo 2 e a **Fábrica de foguetes** o noroeste; os outros quatro ficam livres para módulos futuros. As duas só podem ser construídas quando o Núcleo 2 existe: antes disso, o botão de construir diz “Requer Núcleo 2”.
- **Níveis**: um módulo no Núcleo 2 segue o nível do Núcleo como qualquer outro módulo: nenhum passa do Núcleo, então o Núcleo 2 acrescenta slots, não níveis.

### Impressora de munição {#ammo-printer}

A Impressora de munição imprime munição de laser do nada, de um tipo por vez: sem minério e sem créditos, só energia. Ela tem os níveis 1 a 20.

- **Produção**: **x2** (Advanced Plasma) **100 por hora no nível 1, 2.000 no nível 20** (100 a mais a cada nível); **x3** (Ultra Core) metade disso, de 50 a 1.000; **x4** (Experimental Fusion Core) um quarto, de 25 a 500.
- **Modo**: você escolhe x2, x3 ou x4 no cartão ou na ficha dela. Uma troca mantém as horas já armazenadas e passa a contá-las na taxa do novo modo.
- **Armazenamento**: um dia, 24 horas de produção no nível e no tipo em uso (2.400 de x2 no nível 1, 48.000 no nível 20). O tempo offline conta, e um armazenamento cheio simplesmente para.
- **Coletar**: move as unidades inteiras para o seu inventário enquanto a sua **nave está pousada**. A munição não tem limite de carga, e a fração de uma unidade fica e continua contando.
- **Energia**: 40 no nível 1, crescendo 20% por nível. Num déficit de energia ela para como as minas e os coletores, e o que ela guarda fica e pode ser coletado.
- **Construção**: 20.000 créditos, 500 Thulium e 10 Ship Fragments (do seu inventário, com a nave pousada), só no Núcleo 2. As melhorias dela custam de 21.000 créditos e 140 Thulium a 5.600.000 créditos e 11.000 Thulium e levam o mesmo tempo que as da Forja, de 5 minutos a 24 horas e 5 d 13 h no total (veja as tabelas mais abaixo).
- **Não vendável**: o que ela imprime não pode ser vendido no [Leilão](/wiki/03-Mechanics/Auction.md#marketable-items).

### Fábrica de foguetes {#rocket-factory}

A Fábrica de foguetes fabrica foguetes da loja do nada, de um tipo por vez. Ela tem os níveis 1 a 20.

- **O que ela faz**: um só dos doze foguetes da loja, o que você escolher: Lancet, Rivet, Scatter ou Ember, raridades I, II e III. O N.U.K.E. e o N.I.K.E. nunca são fabricados.
- **Produção**: a raridade III faz **0,5 por hora no nível 1 e 10 no nível 20** (0,5 a mais a cada nível), a raridade II faz 1,25 vezes isso e a raridade I o dobro. Só contam foguetes inteiros: a fração de um fica e continua contando.
- **Armazenamento**: um dia, 24 horas de produção no nível e com o foguete em uso (240 de raridade III no nível 20). O tempo offline conta, um armazenamento cheio simplesmente para, e uma troca de foguete mantém as horas já armazenadas.
- **Coletar**: move os foguetes para o seu inventário enquanto a sua **nave está pousada**, quantos você puder carregar: no máximo 5.000 de raridade I, 2.000 de raridade II e 500 de raridade III, o limite da própria loja. O que não couber fica na fábrica.
- **Energia**: 24 no nível 1, crescendo 15% por nível. Num déficit de energia ela para como a impressora.
- **Construção**: 20.000 créditos, 500 Thulium e 15 Ship Fragments (do seu inventário, com a nave pousada), só no Núcleo 2. As melhorias dela custam um quarto das da impressora, de 5.300 créditos e 35 Thulium a 1.400.000 créditos e 2.800 Thulium, e levam o mesmo tempo: 5 d 13 h no total.
- **Não vendável**: o que ela fabrica não pode ser vendido no [Leilão](/wiki/03-Mechanics/Auction.md#marketable-items).

## Mecânicas {#mechanics}

### Construção e melhoria {#building-and-upgrading}

- **Construção**: cada módulo é construído por conta própria. Um módulo está no nível 1 no instante em que é construído, e melhorá-lo aumenta a produção dele (ou a energia que ele produz) e o armazenamento, e também o que ele custa em energia.
- **Tempo e custo**: as melhorias custam créditos e Thulium e levam tempo, e cada módulo tem para cada nível o seu próprio preço e tempo (passe o mouse sobre **Melhorar** para ver o próximo; os totais estão mais abaixo). O preço é pago quando você inicia a melhoria. O custo não depende do tempo.
- **Temporizadores**: uma melhoria corre no relógio do servidor, então termina enquanto você está fora, dias depois se for preciso. Comece-a, desconecte, volte: o módulo está no novo nível quando você abre a página do Skylab.
- **Tempos de melhoria**: os primeiros níveis são rápidos e os últimos levam até 36 horas, os do Núcleo até 6 dias (veja as tabelas abaixo). Cada módulo tem o seu próprio temporizador, então você pode melhorar vários ao mesmo tempo.
- **Pausa na produção**: enquanto um módulo está sendo melhorado, ele fica offline: não produz nada e não usa energia. A Usina solar é a exceção: ela continua produzindo um quarto da sua energia (veja abaixo).
- **A Usina solar produz só 25% da sua energia enquanto é melhorada**: a Usina solar produz toda a energia do Skylab e, enquanto é melhorada (24 horas no último nível), produz um quarto da energia do nível **atual**; a do novo nível assume no momento em que a melhoria termina. Uma estação completa usa cerca de 90% do que a Usina solar produz no próprio nível, então um quarto disso sustenta uma estação só de cinco a seis níveis abaixo da Usina solar. Caso contrário, toda mina e todo coletor param durante toda a melhoria, o que você guardou continua lá e pode ser coletado, e a Forja não inicia nenhum lote novo. Um módulo em melhoria ou desligado não usa energia, então melhorar as minas junto com a Usina solar não custa nada a mais, e desligar módulos abre espaço para os outros; a Mina de Thulium é, de longe, a que mais consome.

### Quanto custa {#what-it-costs}

O preço da subida inteira, a construção mais cada melhoria, até o nível 10 e até o nível 20. O Núcleo está sempre lá e os passos dele custam créditos, com 2.000 Thulium a mais no passo para o nível 10; o Centro de Pesquisa tem os níveis 1 a 10 e os números dele estão na página [Pesquisa](/wiki/03-Mechanics/Research.md). A Impressora de munição e a Fábrica de foguetes são construídas no Núcleo 2, portanto só quando o Núcleo está no nível 10, e o nível 1 delas é a construção.

| Módulo | Créditos até o nível 10 | Thulium até o nível 10 | Créditos até o nível 20 | Thulium até o nível 20 |
| :--- | ---: | ---: | ---: | ---: |
| Núcleo | 112.326 | 2.000 | 6.647.504 | 2.000 |
| Usina solar | 1.219.500 | 1.600 | 35.039.500 | 36.850 |
| Mina de créditos | 840.000 | 109 | 26.240.000 | 2.399 |
| Mina de Thulium | 1.154.000 | 4.190 | 32.254.000 | 67.890 |
| Coletor de Velkonite | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Coletor de Orvium | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Depósito de recursos | 619.500 | 359 | 18.169.500 | 2.649 |
| Forja | 1.224.000 | 2.050 | 35.044.000 | 37.300 |
| Impressora de munição | 1.411.000 | 5.140 | 22.031.000 | 47.940 |
| Fábrica de foguetes | 377.300 | 1.674 | 5.547.300 | 12.494 |

Os primeiros passos são baratos e os últimos caros: o passo da Mina de créditos do nível 1 ao 2 custa 5.000 créditos e 1 Thulium, e o do 19 ao 20 custa 7.000.000 de créditos e 550 Thulium. Os da Mina de Thulium custam 7.000 créditos e 45 Thulium, depois 8.500.000 créditos e 16.000 Thulium. As melhorias da Usina solar custam em cada nível o mesmo que as da Forja, e os dois coletores custam o mesmo entre si.

### Tempos de melhoria {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Tempos de melhoria**, por módulo (a melhoria a partir do nível da primeira coluna):

| Nível | Núcleo | Usina solar | Mina de créditos | Mina de Thulium | Depósito de recursos | Coletor de Velkonite | Coletor de Orvium | Forja | Centro de Pesquisa |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 a 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| 2 a 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| 3 a 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| 4 a 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| 5 a 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| 6 a 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| 7 a 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| 8 a 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| 9 a 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| 10 a 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| 11 a 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| 12 a 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| 13 a 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| 14 a 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| 15 a 16 | 1 d | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| 16 a 17 | 1 d 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| 17 a 18 | 2 d 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| 18 a 19 | 4 d | 20 h | 10 h | 1 d | 10 h | 20 h | 1 d | 20 h | – |
| 19 a 20 | 6 d | 1 d | 12 h | 1 d 12 h | 12 h | 1 d | 1 d 12 h | 1 d | – |
| **Total** | 16 d 13 h | 5 d 13 h | 2 d 14 h | 6 d 13 h | 2 d 14 h | 4 d 16 h | 5 d 10 h | 5 d 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

Uma melhoria que já está em andamento quando os tempos mudam mantém o horário de término que recebeu. Só o Núcleo leva cerca de **16 dias e meio** de melhorias seguidas para ir do nível 1 ao nível 20. Nenhum módulo passa do nível do Núcleo, então a última etapa de cada outro módulo (de 12 a 36 horas) só pode começar quando o Núcleo estiver no nível 20: com todos os temporizadores ocupados, e com os créditos e o Thulium disponíveis, a estação inteira leva cerca de **18 dias**.

### Gerenciamento de energia {#power-management}

O seu Skylab tem um orçamento de energia limitado.

- **Balanço**: mantenha a produção da Usina solar acima da energia que todos os outros módulos usam. A página do Skylab mostra o balanço e avisa antes que uma construção o empurre para abaixo de zero.
- **A Usina solar acompanha**: um módulo Usina solar no nível N produz a energia de **todos os outros módulos no nível N** (o Núcleo, as duas minas, o Depósito de recursos, os dois coletores e a Forja, e a partir do nível 10 o Centro de Pesquisa) e cerca de um décimo a mais, então uma estação cujos módulos estão todos no nível 7 precisa da Usina solar 7 e a tem coberta. Uma Usina solar um nível abaixo não basta para uma estação completa (a última coluna), então a Usina solar ainda precisa acompanhar os demais na subida. O Núcleo consome pouco, então pode ir na frente: a Usina solar 5 e acima cobre uma estação completa no nível dela com o Núcleo em qualquer nível. A tabela mais abaixo conta também a Impressora de munição a partir do nível 7 e a Fábrica de foguetes a partir do nível 10.
- **Estado ativo**: você pode ligar ou desligar as minas, os coletores e a Forja para administrar a energia. O Núcleo, a Usina solar, o Depósito de recursos e o Centro de Pesquisa sempre funcionam. A Impressora de munição e a Fábrica de foguetes também podem ser ligadas e desligadas.
- **Déficit de energia**: se o consumo de energia for maior que a produção, todas as minas e todos os coletores param de produzir até o balanço voltar. O que eles já guardam continua lá, e você ainda pode coletar. A Forja não inicia nenhum lote novo, e o Centro de Pesquisa não inicia nenhuma pesquisa nova (uma pesquisa já em andamento continua). A Impressora de munição e a Fábrica de foguetes param como as minas e os coletores.
- **Melhoria da Usina solar**: enquanto é melhorada, a Usina solar produz só um quarto da sua energia, então, se os seus outros módulos não estiverem bem abaixo, a estação entra em déficit e as minas e os coletores param até a melhoria terminar (veja [Módulo Usina solar](#solar-module)).

A energia da Usina solar em cada nível, contra o que os outros módulos usam no mesmo nível (todos os módulos nesse nível, o Núcleo incluído, e o Centro de Pesquisa a partir do nível 10):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Nível | A Usina solar produz | Os outros sete módulos consomem | Sobra | Com a Usina solar um nível abaixo |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: faltam 23 |
| 3 | 375 | 337 | 38 | 310: faltam 27 |
| 4 | 455 | 410 | 45 | 375: faltam 35 |
| 5 | 555 | 501 | 54 | 455: faltam 46 |
| 6 | 680 | 615 | 65 | 555: faltam 60 |
| 7 | 965 | 875 | 90 | 680: faltam 195 |
| 8 | 1.185 | 1.076 | 109 | 965: faltam 111 |
| 9 | 1.460 | 1.327 | 133 | 1.185: faltam 142 |
| 10 | 2.000 | 1.814 | 186 | 1.460: faltam 354 |
| 11 | 2.445 | 2.221 | 224 | 2.000: faltam 221 |
| 12 | 3.005 | 2.731 | 274 | 2.445: faltam 286 |
| 13 | 3.715 | 3.373 | 342 | 3.005: faltam 368 |
| 14 | 4.605 | 4.183 | 422 | 3.715: faltam 468 |
| 15 | 5.730 | 5.205 | 525 | 4.605: faltam 600 |
| 16 | 7.150 | 6.499 | 651 | 5.730: faltam 769 |
| 17 | 8.955 | 8.140 | 815 | 7.150: faltam 990 |
| 18 | 11.250 | 10.225 | 1.025 | 8.955: faltam 1.270 |
| 19 | 14.170 | 12.879 | 1.291 | 11.250: faltam 1.629 |
| 20 | 17.890 | 16.261 | 1.629 | 14.170: faltam 2.091 |
<!-- skylab-power:end -->

A tabela conta todos os módulos no mesmo nível. A Mina de Thulium consome quase três quartos desse total no topo (11.695 no nível 20, contra 16.261 para os dez juntos), então uma estação com essa mina bem à frente do resto precisa de mais Usina solar do que o seu Núcleo sugere.

### Coleta {#collecting}

Cada mina e cada coletor tem um armazenamento para cerca de 72 horas do que produz. Você coleta manualmente.

- **Capacidade**: quando um armazenamento está cheio, ele para de produzir até você coletar.
- **Minas**: os créditos e o Thulium coletados vão direto para a sua conta.
- **Coletores**: o minério vai para o Depósito de recursos, até onde houver espaço.
- **Forja**: as placas vão para o seu inventário, quando a sua nave está pousada.
- **Impressora de munição e Fábrica de foguetes**: a munição e os foguetes vão para o seu inventário, quando a sua nave está pousada. Cada uma guarda só 24 horas de produção (veja [Impressora de munição](#ammo-printer) e [Fábrica de foguetes](#rocket-factory)).
- **Coletar tudo** pega tudo de uma vez, inclusive de módulos desligados e em melhoria.
- Um selo **(!)** aponta um armazenamento cheio que você pode esvaziar, e as placas que esperam na Forja, na página do Skylab e na linha do Skylab da barra lateral.

### O reset {#the-wipe}

O Skylab nunca sofre reset: os módulos mantêm os níveis, o Depósito de recursos mantém o minério e o Centro de Pesquisa mantém as tecnologias, o tanque de ciência, a Dark Matter que ele contém e uma pesquisa em andamento. As placas no seu inventário são itens como quaisquer outros, então seguem as [regras do reset](/wiki/03-Mechanics/Wipe-Timeline.md). A Impressora de munição e a Fábrica de foguetes mantêm os seus níveis, o que foram ajustadas para fazer e o que guardam.

## Planejando o seu Skylab {#planning-your-skylab}

O Skylab leva semanas para crescer, então um pouco de planejamento compensa. Os números são os das tabelas acima.

### O que melhorar primeiro {#what-to-upgrade-first}

1. **A Usina solar, depois a Mina de créditos.** A Usina solar custa 500 créditos e 50 Thulium e sem ela nada funciona; a Mina de créditos não custa nada. As dez [missões da estação](/wiki/03-Mechanics/Quests.md#station-missions) guiam você nesses primeiros passos e pagam 52.000 créditos e 610 Thulium por eles, na base: o seu mundo, os seus boosters e os bônus do seu clã a multiplicam.
2. **Depois a Mina de Thulium: é a sua principal fonte de Thulium.** No nível 10 ela produz 450 Thulium por hora, 10.800 por dia, tanto quanto pagam 54 abates de um [Crystalys](/wiki/04-Aliens/Crystalys.md) em Alpha (200 cada). A subida até o nível 10 custa 1.154.000 créditos e 4.190 Thulium, com a construção incluída. No nível 15 a mina produz 22.800 por dia e no nível 20, 38.400. O armazenamento dela guarda 72 horas, então volte pelo menos a cada três dias. O que o Thulium compra está na página [Recursos](/wiki/06-Items/Resources.md#thulium).
3. **A Mina de créditos é a renda constante de apoio.** No nível 10 ela produz 7.500 créditos por hora, 180.000 por dia, por 840.000 créditos e 109 Thulium. Os níveis mais altos se pagam devagar: o passo do nível 9 ao 10 custa 300.000 créditos por 1.000 a mais por hora, ou seja, 300 horas. Melhore-a quando sobrarem créditos.
4. **Mantenha o Núcleo ocupado.** Nada passa do Núcleo, e o Núcleo sozinho leva cerca de 16 dias e meio para chegar ao nível 20. Não há fila, então inicie o próximo passo dele toda vez que voltar.
5. **Construa a cadeia de suprimentos como um conjunto.** Os coletores, o Depósito de recursos e a Forja abrem no nível 5 do Núcleo. Um coletor só pode depositar minério em um Depósito de recursos, e o depósito comporta um dia da produção do coletor dele no nível 1 e quatro dias no nível 20, então melhore o Depósito junto com os coletores, senão o minério fica esperando nos armazenamentos deles.
6. **Deixe 2.000 Thulium prontos para o nível 10 do Núcleo.** O passo do Núcleo do nível 9 para o nível 10 pede isso, e ele constrói a ponte e o Núcleo 2, onde são construídas a [Impressora de munição](#ammo-printer) e a [Fábrica de foguetes](#rocket-factory).

### Planejando uma melhoria da Usina solar {#timing-a-solar-upgrade}

Enquanto é melhorada, a Usina solar produz um quarto da sua energia, e uma estação quase sempre usa mais do que isso. As minas e os coletores então param durante toda a melhoria: o que eles guardam continua lá, mas o que teriam produzido se perde. A tabela dá, para cada passo da Usina solar, o tempo dele, a maior estação que ainda funciona durante ele (todos os módulos no mesmo nível, com o Núcleo e a cadeia de suprimentos; uma estação menor aguenta um pouco mais) e o que uma Mina de créditos e uma Mina de Thulium desse nível teriam produzido nesse tempo. Por exemplo, a Usina solar do nível 10 ao 11 leva 4 horas, e minas de nível 10 teriam produzido nelas 30.000 créditos e 1.800 Thulium. A tabela conta também a Impressora de munição a partir do nível 7 e a Fábrica de foguetes a partir do nível 10.

| Melhoria da Usina solar | Tempo | Estação que continua funcionando, até o nível | A Mina de créditos produz nesse tempo | A Mina de Thulium produz nesse tempo |
| :--- | ---: | ---: | ---: | ---: |
| 1 a 2 | 5 min | nenhuma | 42 | 4 |
| 2 a 3 | 15 min | nenhuma | 250 | 20 |
| 3 a 4 | 30 min | nenhuma | 750 | 55 |
| 4 a 5 | 45 min | nenhuma | 1.500 | 105 |
| 5 a 6 | 1 h | nenhuma | 2.500 | 180 |
| 6 a 7 | 1 h 15 min | nenhuma | 4.375 | 288 |
| 7 a 8 | 1 h 30 min | 1 | 6.750 | 420 |
| 8 a 9 | 2 h | 2 | 11.000 | 660 |
| 9 a 10 | 3 h | 3 | 19.500 | 1.140 |
| 10 a 11 | 4 h | 4 | 30.000 | 1.800 |
| 11 a 12 | 5 h | 5 | 45.000 | 2.750 |
| 12 a 13 | 6 h | 6 | 66.000 | 3.900 |
| 13 a 14 | 8 h | 7 | 104.000 | 6.000 |
| 14 a 15 | 10 h | 8 | 150.000 | 8.500 |
| 15 a 16 | 12 h | 9 | 204.000 | 11.400 |
| 16 a 17 | 16 h | 9 | 320.000 | 17.600 |
| 17 a 18 | 18 h | 11 | 432.000 | 22.500 |
| 18 a 19 | 20 h | 12 | 580.000 | 28.000 |
| 19 a 20 | 1 d | 13 | 840.000 | 36.000 |

- **Melhore as minas junto com a Usina solar.** Um módulo em melhoria não produz nada e não usa energia de qualquer jeito, então o tempo que uma mina passa em melhoria durante a pausa não custa nada a mais.
- **Mantenha os outros módulos baixos se você não pode pagar uma pausa.** Uma estação só continua funcionando durante a melhoria da Usina solar se todos os outros módulos dela estiverem pelo menos cinco níveis abaixo da Usina solar (seis a partir do nível 10 da Usina solar), e uma estação completa precisa de um pouco mais, como a tabela mostra.
- **Desligue o que você puder dispensar.** Um módulo desligado não usa energia, então desligar a Mina de Thulium, a que mais consome (80 no nível 1, e 30% a mais a cada nível), abre espaço para os outros.
