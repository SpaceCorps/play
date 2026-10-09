<!-- wiki-i18n source: 5df6b18400b138dc -->
<!-- wiki-i18n title: Escavadeira gigante -->
# Escavadeira gigante {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; escavadeira; escavadeira gigante; combustível; painel de controle; superaquecimento; radiação; onda -->

A partir do dia 11 da temporada, um **pulsar** brilha em cada um dos setores de perigo `DS-1`, `DS-2` e `DS-3`, e uma **escavadeira gigante** fica ao lado dele. A escavadeira minera o pulsar atrás de **Thulium e minérios raros**, e para isso queima [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md). Qualquer um pode abastecê-la, escolher o que ela minera e ligá-la, e tudo o que ela produz fica em volta dela em caixas que qualquer um pode pegar. Mas uma rodada é barulhenta: o mundo inteiro é avisado quando ela começa, **Slumbering Voids** vão atrás dela em ondas, e uma escavadeira trabalhada por tempo demais superaquece e irradia toda a área. Esta página diz como uma rodada se desenrola, o que ela produz e como sobreviver a ela. Os setores estão em [Setores de perigo](/wiki/01-General/Danger-Sectors.md); os Voids, em [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

## Em resumo {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Onde**: Um pulsar com uma escavadeira gigante em cada um dos setores `DS-1`, `DS-2` e `DS-3`, em todos os mundos
- **Aparece**: Do dia 11 da temporada até o reset
- **Combustível**: Dark Matter. Um queima por 10 min; o tanque comporta 3, o que dá 30 min de mineração. Qualquer um pode adicionar um de cada vez, da própria carga
- **Painel**: A janela funciona a até 600 unidades da escavadeira, e o rótulo aparece a partir de 1.400 unidades. Qualquer um pode abastecer, escolher e iniciar; a escolha fica travada enquanto ela funciona
- **Caixas**: Uma caixa a cada 20 s, entre 450 e 900 unidades da escavadeira, livre para qualquer um desde o momento em que cai. Ela fica por 5 min, e no máximo 24 ficam ao mesmo tempo num mapa
- **Calor**: 30 min de mineração, em quantas rodadas forem necessárias, e a escavadeira superaquece por 1 h. O calor é mantido entre as rodadas e some depois do descanso
- **Radiação**: Enquanto está superaquecida ou destruída, a escavadeira (a até 1.100 unidades) e o pulsar dela (a até 1.300 unidades) queimam toda nave dentro: 10% do HP total dela por segundo
- **Casco**: 200.000 HP em Alpha, 300.000 em Beta e 400.000 em Gamma. Só os Slumbering Voids podem feri-la, e só quando não resta nenhum piloto para defendê-la
- **Voids**: 2 Slumbering Voids a cada 2 min enquanto ela minera, os primeiros 1 min depois do início; no máximo 8 vivos num mapa
- **Avisos**: Os pilotos do mundo inteiro são avisados quando uma rodada começa, quando a escavadeira superaquece e quando é destruída; o resto vai para os pilotos do setor dela. São linhas do Sistema: aparecem na aba **Sistema** do chat e no Registro do jogo, e não em **Global** nem em **Local**.

<!-- excavator-glance:end -->

## Como uma rodada se desenrola {#how-a-run-goes}

1. **Encontre uma.** Cada um dos três setores de perigo que têm um pulsar tem uma escavadeira, em cada mundo. Um rótulo, **Escavadeira**, paira sobre ela quando você está perto, e o mapa do Sistema estelar mostra o estado da escavadeira do setor em que você voa.
2. **Abra o painel.** Clique no rótulo. A janela **Escavadeira gigante** funciona enquanto sua nave estiver ao alcance do painel da escavadeira (a lista *Em resumo* informa). Uma nave camuflada pode usá-lo, e usá-lo não encerra o camuflado.
3. **Abasteça.** **Adicionar Dark Matter** põe um Dark Matter da sua carga no tanque. Qualquer um pode fazer isso. O tanque nunca aceita mais do que a escavadeira pode queimar antes de superaquecer, então nenhum combustível é desperdiçado.
4. **Escolha o que minerar** na lista e então aperte **Iniciar mineração**. É preciso pelo menos um Dark Matter no tanque e um recurso. Qualquer um pode mudar a escolha até o início; depois que ela está funcionando, o recurso fica travado. O início é anunciado a todos os pilotos do mundo, com o seu nome, o setor e o recurso.
5. **Segure-a.** Enquanto minera, uma caixa cai em volta da escavadeira a cada poucos segundos, e logo depois do início chegam os primeiros Slumbering Voids. Defenda a escavadeira e pegue as caixas.
6. **Vigie o calor.** A barra de Calor enche enquanto a escavadeira minera e nunca esvazia enquanto ela espera. No limite, a escavadeira superaquece. Vá embora antes: o jogo avisa o mapa duas vezes.
7. **Ela descansa.** Superaquecida ou destruída, a escavadeira e seu pulsar ficam irradiados até o descanso acabar; então ela fica pronta de novo, com o calor zerado e o casco cheio.

A janela mostra também o setor, o tanque (uma célula para cada Dark Matter, a que está queimando desenhada pela metade), quanto Dark Matter você carrega, o casco da escavadeira, o que cada recurso produz por minuto no seu mundo e, enquanto ela minera, o tempo até a próxima onda e os Voids vivos. Quando algo é recusado, você lê o motivo em vermelho: você está longe demais do painel, não tem Dark Matter, o tanque está cheio, ainda não há combustível ou recurso escolhido, o recurso está travado enquanto ela funciona, ou a escavadeira está quente.

| Estado | O que é | O que você pode fazer |
| :--- | :--- | :--- |
| **Pronta** | Sem combustível, ou com combustível e sem ter começado. O calor acumulado é mantido. | Adicionar Dark Matter, escolher, iniciar. |
| **Minerando** | Queima Dark Matter e acumula calor; o recurso fica travado. | Adicionar mais Dark Matter até o espaço que sobra, combater os Voids, pegar as caixas. |
| **Superaquecida** | O calor chegou ao limite. O tanque é esvaziado; as caixas já soltas ficam. | Nada. A área está irradiada: fique fora. |
| **Destruída** | Os Voids levaram o casco a zero. O combustível se perde, o casco volta a ficar cheio na hora. | Nada. A área está irradiada: fique fora. |

Se o combustível acabar antes do limite, a escavadeira volta a **Pronta** com o calor mantido, e os Voids que sobram vão embora depois de um tempo, a menos que estejam lutando.

## O que ela minera {#what-it-mines}

Um tanque cheio é calibrado para produzir mais ou menos o que dois ou três pilotos ganhariam em meia hora do melhor cultivo de Thulium. Beta e Gamma produzem mais, assim como pagam mais por cada abate. Você escolhe um recurso por rodada. Uma caixa é igual para todos, e uma caixa de Thulium é dinheiro vivo, pago ao pegá-la, como o Thulium dos asteroides.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Um tanque cheio (3 Dark Matter, 30 min de mineração) produz as quantidades abaixo, em 90 caixas.

| Recurso | Alpha | Beta | Gamma | Um minuto, em Alpha | Uma caixa, em Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 4.821 | 7.714 | 9.643 | 160,7 | 53,6 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 1.157 | 1.851 | 2.314 | 38,6 | 12,9 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 514 | 823 | 1.029 | 17,1 | 5,7 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 320 | 320 | 320 | 10,7 | 3,6 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 160 | 160 | 160 | 5,3 | 1,8 |

- Uma rodada de Velkonite ou Orvium produz no máximo 4 horas de um coletor de nível 20 do [Skylab](/wiki/03-Mechanics/Skylab.md) desse minério (320 Velkonite, 160 Orvium), em todos os mundos: são os minérios do Skylab, e uma rodada nunca acelera o ritmo dele mais do que isso.
- Uma caixa contém cerca da quantidade da última coluna, com variação de 15%. Uma caixa de Thulium é dinheiro vivo: a coleta o paga. Uma caixa de minério contém o item.

<!-- excavator-resources:end -->

Os boosters do próprio piloto funcionam como em qualquer carga: o bônus do Resource Magnet Booster aumenta uma caixa de minério. Não há limite diário para as caixas: o combustível e o relógio é que limitam uma rodada.

**Para que serve o minério.** O minério de uma caixa vai para a sua carga como qualquer item. Cataclysite e Quorvium são usados na Montagem e na Forja ([Recursos](/wiki/06-Items/Resources.md)). A Forja do Skylab pega seu minério só do Depósito de recursos, que os coletores enchem; então o Velkonite e o Orvium de uma caixa são combustível para o [Centro de Pesquisa](/wiki/03-Mechanics/Research.md#fuel), não para a Forja.

## Os Slumbering Voids {#the-slumbering-voids}

Uma rodada atrai **Slumbering Voids**, caçadores da civilização perdida que voam da borda do mapa para proteger o pulsar de quem quiser esvaziá-lo. Eles caçam os pilotos perto da escavadeira e, quando não há mais ninguém para caçar, vão atrás da escavadeira. Os números do Void e o seu pagamento estão em [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Ondas.** 2 Slumbering Voids a cada 2 min; as primeiras 1 min depois do início, e nenhuma nos últimos 1 min de uma rodada. No máximo 8 estão vivos ao mesmo tempo num mapa: uma onda que encontra o mapa cheio é pulada.
- **Chegada.** Uma onda aparece na borda do mapa, 900 unidades para dentro e a pelo menos 2.500 unidades de todo anel de portão, e voa até a escavadeira em cerca de 20 s. A mensagem diz de que lado do mapa ela vem.
- **Caça.** Um Void caça o piloto mais próximo que consegue ver a até 2.500 unidades, e fica a até 7.000 unidades da escavadeira.
- **Cerco.** Quando, por 15 s, nenhum piloto que eles consigam ver está a até 7.000 unidades da escavadeira, os Voids atacam a escavadeira, e cada laser causa 25% do dano usual. Em zero a escavadeira é destruída: o combustível se perde, o casco volta a ficar cheio na hora, e ela descansa por 1 h.
- **Partida.** Quando uma rodada termina, os Voids que sobram ficam mais 90 s e continuam lutando se forem combatidos; depois vão embora.

<!-- excavator-voids:end -->

- **Um Void é um canhão de vidro.** O escudo dele é grande, mas absorve 80% de um acerto, então o casco atrás dele acaba depois de poucas vezes o seu tamanho em dano, e bem antes com penetração de escudo. Dois ou três pilotos bem equipados seguram uma rodada em Alpha; Beta e Gamma pedem grupos maiores, como para qualquer alienígena.
- **Um camuflado não defende o local.** Os Voids não veem naves camufladas, então um piloto que se esconde não os afasta da escavadeira; e um piloto que se abriga num anel de portão não pode ser alcançado e também não conta.
- **Cada Void paga,** conforme o dano que você causou, e solta uma caixa ([como paga o abate de um chefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Os abates deles somam aos seus pontos PvE de patente como os de uma nave de enxame.

## Calor e radiação {#heat-and-radiation}

A mineração soma calor segundo a segundo. O calor é **cumulativo e nunca esfria enquanto a escavadeira espera**: uma rodada que acaba cedo deixa uma mais curta para o próximo piloto. Quando atinge o limite, a escavadeira **superaquece**, e quando o casco dela chega a zero ela é **destruída**; nos dois casos a escavadeira e o pulsar irradiam até o descanso acabar.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Círculo | Raio | HP total por segundo | Uma nave cheia aguenta |
| :--- | ---: | ---: | ---: |
| A escavadeira gigante | 1.100 | 10% | 10 s |
| O pulsar | 1.300 | 10% | 10 s |

- **A dose.** 10% do HP máximo total de uma nave (casco mais escudo) por segundo, então uma nave cheia aguenta 10 s, seja qual for a classe. O escudo a recebe primeiro e a absorção dele não conta.
- **Quem.** Toda nave dentro dos círculos, camufladas inclusive; nenhum alienígena. É dano sofrido: um Drone de reparo para e o escudo não recarrega, como no buraco negro.
- **Crédito.** Um piloto que morre queimado é creditado ao último inimigo que o acertou nos 15 s anteriores.
- **Avisos.** O mapa é avisado 1 min e 15 s antes do superaquecimento.

<!-- excavator-radiation:end -->

- **O aviso.** Duas vezes antes do superaquecimento (os tempos estão na lista acima) o mapa é avisado, uma nave dentro dos círculos vê um alerta, e os círculos são desenhados no mapa do Sistema estelar e no minimapa. Quando irradiam, os círculos ficam vermelhos e o medidor de Radiação mostra a dose.
- **Sair.** Toda nave de série consegue sair da borda do painel ou da caixa mais distante que ainda esteja lá, exceto a Ironclad, que é lenta: ela sai durante o aviso, ou não sai. Não fique em cima de uma caixa quando o calor chegar ao limite.
- **Espólio nos círculos.** As caixas soltas antes do superaquecimento ficam, na radiação: uma caixa que está lá quando ela começa é pega ao preço da dose.
- **A reinicialização do servidor** pausa uma rodada: o combustível e o calor voltam como estavam, o descanso segue pelo relógio, e a primeira onda depois do reinício chega um minuto depois.

## Lutar por uma rodada {#fighting-over-a-run}

A escavadeira **não tem anel especial**: valem as regras normais do seu mundo, então rivais podem vir, atirar em você e levar as caixas (uma caixa é livre para qualquer um desde o momento em que cai). Roubar e fazer emboscadas faz parte do evento. Algumas coisas para prever:

- **Quem abastece não é quem ganha.** Qualquer um pode abastecer, escolher e iniciar; um rival pode mudar o recurso antes de você apertar Iniciar. Confira a escolha antes de apertar.
- **O combustível corre risco.** Se a escavadeira for destruída, o Dark Matter no tanque se perde, e ninguém o recupera. O máximo que se pode perder é o tanque cheio.
- **Leve um grupo** e combinem quem fica perto da escavadeira e quem pega as caixas, e fique de olho no calor: os pilotos que pegam as últimas caixas são os que a radiação apanha.
- **Os Voids vão à escavadeira, não às caixas.** Um grupo que segura a escavadeira mantém os Voids ocupados; o que se afasta a deixa para o cerco.

## O que o mundo fica sabendo {#what-the-world-is-told}

São linhas do Sistema (aparecem na aba **Sistema** do chat e no Registro do jogo, e não em **Global** nem em **Local**). As três primeiras vão para o mundo inteiro; a última, para os pilotos do setor da escavadeira.

- No dia em que o evento 2 começa: os setores de perigo mudaram.
- Um piloto **inicia** uma escavadeira, com o setor, o recurso e os minutos de combustível.
- A escavadeira **superaquece** ou é **destruída**.
- O combustível acaba; a escavadeira está prestes a superaquecer (dois avisos); uma **onda** de Voids está chegando, com seu número e o lado do mapa de onde vem; não resta nenhum piloto, então os Voids atacam a escavadeira.

Cada ação do painel e cada aviso tem um som discreto próprio, no volume dos efeitos.

## Onde ler mais {#where-to-read-more}

- [Setores de perigo](/wiki/01-General/Danger-Sectors.md): onde ficam os pulsares e o que mais há de novo.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): o Slumbering Void, a Inert Mass e o Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) e [O buraco negro](/wiki/03-Mechanics/Black-Hole.md): de onde vem o combustível.
- [Recursos](/wiki/06-Items/Resources.md): os minérios que a escavadeira produz.
- [Caixas de carga](/wiki/03-Mechanics/Cargo.md): caixas, coleta e o Resource Magnet Booster.
- [Patentes](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): os pontos PvE de um Void.
