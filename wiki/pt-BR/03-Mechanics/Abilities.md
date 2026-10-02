<!-- wiki-i18n source: ae35d5bdcf504de8 -->
<!-- wiki-i18n title: Habilidades -->
# Habilidades ativas da nave {#active-ship-abilities}

As habilidades são os botões que você pressiona no calor de uma luta: um escudo que volta, uma explosão de velocidade para sair do alcance, um reparo quando o seu casco está quase no fim. Elas vêm do **escudo, motor ou drone de reparo** que você encaixa nos **slots de habilidade** da sua nave, e quanto melhor o item, melhor a habilidade. Elas foram feitas para o momento em que você precisa delas, não para serem pressionadas a cada recarga: cada uma dura cerca de dez segundos e depois descansa de um minuto e meio a dois minutos.

Um piloto novo começa com uma: o **Repair Drone I** do kit inicial já vem encaixado no slot de habilidade da Protos, então o botão do Emergency Repair (`E`) está lá desde o primeiro minuto.

## Slots de habilidade {#ability-slots}

Toda nave tem um número fixo de slots de habilidade no hangar:

- **Protos** (inicial): 1 slot
- **Kitefin**: 1 slot
- **Ostirion**: 2 slots
- **Paragon**: 3 slots
- **Ironclad**: 3 slots
- **Wraith**: 3 slots

Um slot de habilidade aceita um **escudo**, um **motor** ou um **drone de reparo**, e cada um cria a sua própria habilidade. Arraste o item para o slot. A configuração 1 e a configuração 2 têm os seus próprios slots.

- **Células de escudo e propulsores não cabem em um slot de habilidade.** Eles são módulos de escudos, motores e núcleos adaptativos.
- **Um item em um slot de habilidade não dá mais nada.** Ele não dá capacidade de escudo, recarga, absorção nem velocidade, e também não traz a lentidão que um escudo causa. O mesmo Heavy Shield Core ou fica em um slot de gerador, pelo escudo dele a todo momento, ou em um slot de habilidade, pelo Surge dele. A escolha é sua.
- Um escudo ou motor que tem células ou propulsores encaixados os devolve ao seu inventário quando você o arrasta para um slot de habilidade.
- Um drone de reparo em um slot de habilidade cria o Emergency Repair e não repara o casco por conta própria. O drone lento (**REP**) precisa de um drone de reparo em um slot extra.

## Vários módulos do mesmo tipo {#several-modules-of-one-kind}

Você pode encaixar **vários escudos, motores ou drones de reparo** nos slots de habilidade de uma configuração. Continua sendo uma habilidade, um botão e um tempo de recarga, só que mais forte:

- **O módulo de menor nível define a base.** O nível dele dá a força e o tempo de recarga. Um Heavy Shield Core ao lado de um Light Shield Core se comporta como dois módulos de nível I: um segundo módulo melhor compra o bônus e nunca uma força melhor nem um tempo de recarga menor.
- **Cada um dos outros módulos acrescenta 50% da base**, em soma e não em multiplicação. Os motores fazem o Afterburner **durar mais**: 10 s, 15 s com dois motores, 20 s com três (o bônus de velocidade e o tempo de recarga não mudam). Os escudos fazem o Shield Surge **restaurar mais**, e os drones de reparo fazem o Emergency Repair **curar mais**, nos mesmos dez segundos: 100%, 150% e 200% do total para um, dois e três módulos.
- **Os módulos extras custam slots.** Uma nave com três slots de habilidade pode ter três de um tipo, ou um de cada, ou dois e um. Uma Protos ou uma Kitefin tem um único slot e não pode empilhar; uma Ostirion pode ter dois de um tipo.
- Níveis iguais são simplesmente aquele nível. De dois módulos do mesmo nível, o de encantamento mais fraco define a base.

## As três habilidades {#the-three-abilities}

### Shield Surge (escudos), tecla `Q` {#shield-surge-shields-key-q}

Durante dez segundos o escudo da sua nave é **reparado**: o Surge restaura uma parte do seu escudo máximo de forma uniforme, até o máximo e nunca acima dele. Não é uma barreira e não muda como os acertos são divididos; ele devolve escudo, e o que devolveu fica. Ele não para quando você é atingido (a recarga comum espera 15 segundos depois de um acerto; o Surge não). Uma nave com o escudo cheio ganha pouco com ele, então pressione-o quando o escudo estiver se esgotando. O total nunca é menor que a capacidade do próprio núcleo, de modo que uma nave com pouco escudo ainda recebe um reparo de verdade (até o máximo).

- Recusado dentro da proteção de uma zona segura e em uma nave sem escudo algum, para que um clique errado não o gaste.
- Os foguetes de penetração de escudo ainda passam em parte pelos escudos, como sempre passaram.

### Afterburner (motores), tecla `W` {#afterburner-engines-key-w}

A sua velocidade final é multiplicada pelo bônus do nível durante a duração. Ele não muda a manobrabilidade, a mira nem o dano recebido: transforma tempo em distância. Use-o para sair de uma luta, para chegar ao anel de uma estação ou de um portal, ou para alcançar um alvo que foge. Funciona em qualquer lugar, inclusive em zonas seguras. Mais motores fazem durar mais, não ir mais rápido.

### Emergency Repair (drones de reparo), tecla `E` {#emergency-repair-repair-drones-key-e}

Cura uma parte do seu **casco máximo de forma uniforme ao longo de dez segundos**, nunca acima do máximo. Os acertos não o interrompem: é uma habilidade de emergência e funciona sob fogo, na radiação do buraco negro, sob camuflagem e dentro de uma janela de EMP. Termina quando o tempo acaba ou quando a sua nave é destruída. Não mexe no seu escudo, não conta como um acerto e deixa o reparo lento REP como estava. Recusado com o casco cheio.

## Níveis {#ranks}

A força de uma habilidade é uma **parte do número da sua própria nave** (escudo máximo, velocidade, casco máximo), então ela cresce com a nave. O nível vem do item: um modelo melhor dá uma habilidade melhor. Um item encantado soma o bônus de encantamento à força, no máximo 15%. A tabela vale para um módulo; a pilha vem logo abaixo.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Habilidade | Nível | Item | Força (um módulo) | Duração | Recarga | Ativa |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | restaura 30% do seu escudo máximo | 10 s | 120 s | 8,3% |
| **Shield Surge** | II | Basic Shield Core | restaura 60% do seu escudo máximo | 10 s | 105 s | 9,5% |
| **Shield Surge** | III | Heavy Shield Core | restaura 100% do seu escudo máximo | 10 s | 90 s | 11,1% |
| **Afterburner** | I | Engine I | +30% de velocidade | 10 s | 120 s | 8,3% |
| **Afterburner** | II | Engine II | +45% de velocidade | 10 s | 105 s | 9,5% |
| **Afterburner** | III | Engine III | +60% de velocidade | 10 s | 90 s | 11,1% |
| **Emergency Repair** | I | Repair Drone I | cura 20% do seu casco máximo | 10 s | 120 s | 8,3% |
| **Emergency Repair** | II | Repair Drone II | cura 25% do seu casco máximo | 10 s | 105 s | 9,5% |
| **Emergency Repair** | III | Repair Drone III | cura 32% do seu casco máximo | 10 s | 90 s | 11,1% |
| **Emergency Repair** | IV | Repair Drone IV | cura 40% do seu casco máximo | 10 s | 75 s | 13,3% |

Vários módulos do mesmo tipo em uma configuração: o de menor nível define a força e a recarga acima, e cada um dos outros acrescenta 50% dela.

| Módulos do mesmo tipo | Afterburner dura | Shield Surge restaura | Emergency Repair cura |
| :---: | --: | --: | --: |
| 1 | 10 s | 100% | 100% |
| 2 | 15 s | 150% | 150% |
| 3 | 20 s | 200% | 200% |

<!-- abilities:end -->

Os escudos e motores de nível III (o Heavy Shield Core, o Engine III) não são vendidos: você os faz na [Montagem](/wiki/05-Items/Overview.md#upgrading-modules) a partir de um Basic Shield Core e de um Engine II, com Thulium, drops e Velkonite Reinforced Plates da Forja do seu [Skylab](/wiki/03-Mechanics/Skylab.md). O Emergency Repair tem um quarto nível, o Repair Drone IV.

## Tempos de recarga e limites {#cooldowns-and-limits}

- **O tempo de recarga começa quando você pressiona** a habilidade e inclui a duração dela. Assim, um Surge de 10 segundos com 90 segundos de recarga fica ativo no máximo 11% do tempo e indisponível por 80 segundos depois de terminar. Vários módulos não o encurtam (vale o do módulo de menor nível); até três Afterburners ficam ativos no máximo 22% do tempo.
- **Os tempos de recarga pertencem a você, não ao item.** Trocar de configuração, trocar o item, saltar para outro setor e se desconectar não os zeram. Uma nave destruída começa o próximo voo com todas as habilidades prontas.
- **Cada habilidade tem o seu próprio tempo de recarga.** Usar uma não bloqueia as outras.
- **Um efeito em andamento mantém os números com que começou.** Desequipar o item ou trocar de configuração não o muda nem o encerra. Um salto ou uma reconexão também não o encerra; se desconectar encerra, e o tempo de recarga continua.
- Os outros pilotos veem os temporizadores das suas habilidades no mapa, como sempre viram: um Surge gasto avisa a eles que os próximos minutos estão livres.

## Teclas e botões {#keys-and-buttons}

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair (todas reatribuíveis nas configurações). Cada botão aparece ao lado da barra de atalhos somente quando a sua configuração tem aquela habilidade, então o `E` de um piloto novo está lá desde o primeiro minuto. O anel em volta do ícone mostra em que estado a habilidade está: inteiro, na cor da habilidade, quando ela está pronta; esvaziando conforme os segundos restantes enquanto ela atua (o Emergency Repair também, agora que ele cura ao longo de dez segundos); e se enchendo de novo enquanto ela recarrega, com os segundos restantes no meio. Uma pilha de vários módulos traz a sua marca (`x2`, `x3`) no canto do botão. O botão do Emergency Repair fica esmaecido enquanto o seu casco está cheio, e o do Shield Surge em uma nave sem escudo algum. Passe o mouse sobre um botão para ver os números na sua nave, com a pilha contada (por exemplo, *Afterburner II x2: +45% de velocidade por 15 s*) e, enquanto um Surge ou um reparo atua, quanto ele dá por segundo e quanto ainda falta vir.

## No hangar {#in-the-hangar}

Arraste um escudo, um motor ou um drone de reparo para um slot de habilidade, ou clique com o botão direito nele no inventário para colocá-lo no primeiro slot livre. Um segundo e um terceiro do mesmo tipo vão para os próximos slots livres e se empilham. O nome e o nível da habilidade ficam sob cada slot preenchido, com a marca da pilha e os números de todos os seus módulos juntos (*Afterburner II x2*, *x2 · 15 s*; para um Repair Drone II em uma Wraith, *+81.000 de casco*), e passar o mouse sobre um slot mostra quanto ele vale na sua nave, com a pilha contada, e qual módulo da pilha define o nível. Todos os módulos de um tipo mostram a mesma habilidade, porque são uma só. Passar o mouse sobre o item em qualquer outro lugar mostra a habilidade com as parcelas da sua própria nave e uma frase sobre o que um módulo a mais acrescenta.

## O que todos veem {#what-everyone-sees}

Um Shield Surge é uma bolha em volta da nave enquanto dura, que pisca nos últimos dois segundos e se fecha quando termina. As barras de escudo (a sua, na janela da nave, e a do alvo, na janela do alvo) simplesmente se enchem conforme o Surge devolve escudo, e a barra pulsa de leve enquanto há espaço para ele. Um Afterburner faz os motores queimarem mais quentes enquanto dura, 10, 15 ou 20 segundos, e envia um anel para fora da nave quando começa, mais largo para uma pilha. Um Emergency Repair envia um pulso verde quando começa, depois, durante os seus dez segundos, envolve o casco em um brilho verde suave com alguns sinais de mais subindo dele, mostra flutuando sobre a sua própria nave o casco que ele cura a cada segundo e termina com um último clarão. Enquanto ele atua, pequenos drones de reparo circulam a nave e a consertam: um para um Repair Drone I, dois para um II, três para um III ou IV, e mais um para cada Repair Drone adicional em uma pilha (nunca mais de três). Eles saem do casco, apontam feixes verdes suaves para as placas dele, enviam pulsos pelos feixes a partir do nível II e voltam para atracar quando os dez segundos terminam; um Shield Surge tem até dois drones azuis dentro da sua bolha. Todo piloto no mapa vê as três habilidades, os drones também (menores na nave de outro piloto, e em menor número nas configurações gráficas mais baixas, em que a qualidade Baixa mostra feixes e brilhos sem modelos de drones; e com um feixe um pouco mais largo a cada nível do drone), então um Surge gasto é um sinal para o inimigo tanto quanto para você. Os drones fazem três sons discretos próprios, bem abaixo do sino do reparo: um bipe suave quando saem do casco, outro quando atracam e um tom fraco sob os feixes enquanto trabalham (os drones de um Surge, um pouco mais agudos); você os ouve nas naves que estão na sua tela, no máximo alguns de cada vez, e o volume dos Efeitos sonoros os abaixa. Com *Reduzir movimento* ligado, o brilho fica constante, os sinais de mais são omitidos, o último clarão vira um esmaecer e os drones ficam estacionados ao lado da nave, com um feixe constante (os sons continuam).

## O que mudou {#what-changed}

Antes da atualização 0.4.3, os slots de habilidade aceitavam células de escudo (Regen. de escudo) e propulsores (Turbo). As células de escudo e os propulsores que estavam em slots de habilidade voltaram ao seu inventário quando o jogo foi atualizado, e você os mantém: eles continuam sendo módulos de escudos, motores e núcleos adaptativos. Desde então, o Shield Surge deixou de dar uma barreira de escudo extra e passou a reparar o seu escudo ao longo de dez segundos, o Emergency Repair cura ao longo de dez segundos em vez de na hora, e você pode encaixar vários módulos de um tipo para um Afterburner mais longo, um Surge maior ou um reparo maior.
