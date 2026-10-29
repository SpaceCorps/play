<!-- wiki-i18n source: c6cf04f6e8e99425 -->
<!-- wiki-i18n title: Recompensas diárias -->
# Recompensas diárias {#daily-rewards}

<!-- wiki-search: daily reward; daily rewards; daily login; login bonus; login reward; calendar; advent calendar; chest; chests; season prize; souvenir; blueprint; streak; recompensa diária; recompensas diárias; login diário; calendário; baú; prêmio da temporada; lembrança; projeto; sequência -->

Cada temporada tem um **calendário de recompensas diárias**: um presente pequeno para cada dia da temporada. Na estação, aperte **Coletar** e o presente do dia é seu. Quanto mais dias você coleta, mais você ganha: quatro **baús** chegam com 7, 14, 21 e 28 dias coletados e, nos últimos três dias da temporada, você pode levar o **prêmio da temporada**. Um dia perdido custa o presente daquele dia e mais nada. O calendário fica no **Painel** (o cartão **Recompensas diárias**) e em **Temporada e perfil › Calendário**.

## Em um minuto {#in-one-minute}

- **29 blocos.** Um para cada dia UTC da temporada. A temporada tem 30 dias, mas o dia 30 é a contagem regressiva de 5 minutos do [Reset](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule), então não há nada para coletar nele.
- **Você aperta Coletar.** Um toque coleta um bloco, uma vez por piloto. Nada é coletado por você.
- **6 horas de tolerância.** Um bloco continua aberto por 6 horas depois do fim do seu dia.
- **Sem sequência.** Um dia perdido faz perder só o bloco daquele dia e mais nada. O que conta é quantos dias você coletou, não se foram seguidos.
- **4 baús**, com 7, 14, 21 e 28 dias coletados.
- **Um prêmio da temporada** nos últimos três dias da temporada: um visual de lembrança com 10 dias coletados e o projeto de um design de nave com 20.
- **Um calendário novo a cada reset.** Você vê todos os presentes da temporada desde o dia 1.
- **Pequeno de propósito.** Os 29 dias juntos valem mais ou menos algumas horas de caça, espalhadas ao longo de uma temporada.

## O dia {#the-day}

O dia do calendário é um **dia UTC**: ele vira às **00:00 UTC**, para todos os pilotos no mesmo instante, e é a mesma contagem de dias da linha diária dos clãs («Dia *n* de 29», veja [Clãs](/wiki/03-Mechanics/Clans.md#the-day)). Ele não segue o seu fuso horário e não é o dia de temporada da página Temporada, que vira no horário do dia em que a temporada começou. O relógio do servidor decide tudo: o relógio do seu computador não muda nada.

O cartão e a aba dizem os dois quando a próxima recompensa abre **no seu próprio fuso horário** («As novas recompensas abrem às 02:00 no seu horário (00:00 UTC)»). Para calcular você mesmo, converta 00:00 UTC. Alguns exemplos:

| Onde | A meia-noite UTC é às |
| :--- | :--- |
| Europa Central | 01:00 (inverno) ou 02:00 (verão) |
| Moscou, Istambul | 03:00 |
| Japão, Coreia | 09:00 |
| Costa Leste dos EUA | 19:00 (inverno) ou 20:00 (verão) |
| Costa Oeste dos EUA | 16:00 (inverno) ou 17:00 (verão) |

- **O dia 1 é curto.** A temporada começa no Reset, no meio de um dia UTC, então o bloco 1 fica aberto desde então até o fim desse dia, mais a tolerância.
- **O dia 29 é longo.** O último bloco fica aberto até a contagem regressiva do Reset começar, o que pode ser mais de 24 horas depois de ele abrir. Com a contagem regressiva em andamento, nada pode ser coletado até a nova temporada começar.
- **Os administradores podem mover o dia da temporada.** O calendário acompanha: os dias pulados contam como perdidos para todos, e um bloco que você já coletou continua coletado.

## Os blocos {#the-tiles}

A aba Calendário mostra uma grade com um bloco para cada dia: o número do dia, o presente e um estado em palavras. Todos os presentes da temporada ficam visíveis desde o primeiro dia, então você vê o que vem pela frente. Ela também conta os seus dias (por exemplo, «11 de 29 dias coletados») e diz quando chega o próximo baú. O cartão do Painel mostra o presente de hoje e um único botão **Coletar**.

| Estado | O que significa |
| :--- | :--- |
| **Hoje** | Aberto agora. Aperte **Coletar**. |
| **Coletado** | Você já o tem. |
| **Ontem** | O bloco de ontem, ainda aberto durante a tolerância. Mostra quanto tempo falta e tem o seu próprio botão **Coletar**. |
| **Perdido** | O dia e a tolerância dele acabaram. O presente se foi, e mais nada mudou. |
| **Abre em …** | Um dia que ainda vai chegar. Você vê o presente, mas ainda não pode coletar. |
| **Antes de entrar** | Um dia anterior ao seu primeiro login. Não pode ser coletado. |

Enquanto uma recompensa espera, aparece um pequeno **(!)** em **Temporada e perfil** na barra lateral e em **Voltar à base** em voo, e uma mensagem ao entrar avisa você (uma vez por dia em cada computador).

## Tolerância e dias perdidos {#grace-and-missed-days}

Um bloco não fecha à meia-noite: ele continua aberto por **6 horas** depois do fim do seu dia UTC. Nessas 6 horas, dois blocos ficam abertos, o de ontem e o de hoje, e você coleta cada um com o seu próprio toque. Passada a tolerância, o bloco de ontem fica **Perdido** de vez, e você não pode voltar mais do que isso.

Um dia perdido custa **o presente daquele dia e mais nada**. Não há sequência para quebrar: a sua contagem de dias coletados, os seus baús e o prêmio da temporada seguem em frente. Um bloco que você coleta durante a tolerância conta exatamente como um coletado a tempo.

## Baús {#chests}

Um baú chega com o **Coletar** que faz a sua contagem de dias coletados alcançar um número, e não antes: não há nada para apertar nem chave para achar. O que importa é a contagem, não a data: o baú dos 7 dias chega com o seu 7º dia coletado, seja qual for esse dia da temporada.

| Baú | Chega com |
| :---: | :--- |
| **1º** | 7 dias coletados |
| **2º** | 14 dias coletados |
| **3º** | 21 dias coletados |
| **4º** | 28 dias coletados |

Cada baú contém um **Specimen Vault**, o contêiner que guarda um pouco de tudo. Os baús finais podem trazer um pequeno extra que o reset não leva. A aba Calendário mostra o que cada baú contém. Um contêiner é só seu e você o abre na página Contêineres. Um contêiner que você não abriu continua na sua conta mesmo depois do [reset](/wiki/03-Mechanics/Wipe-Timeline.md).

Se o jogo não puder entregar o contêiner, por exemplo porque os contêineres não estão ativados, o baú paga no lugar um **pacote** de créditos, Thulium e um booster de valor parecido. Um baú nunca se perde, e você nunca recebe os dois.

## Prêmio da temporada {#season-prize}

O prêmio da temporada tem duas etapas. Você as coleta nos **últimos três dias** da temporada (dias 27 a 29), até a contagem regressiva do Reset começar. Antes do dia 27, a aba diz **Abre nos últimos três dias**, mesmo que você já tenha os dias. Cada etapa é coletada uma vez, em qualquer ordem.

| Etapa | Exige | Prêmio |
| :---: | :--- | :--- |
| **1** | 10 dias coletados | Uma **lembrança da temporada**: um visual |
| **2** | 20 dias coletados | Um **projeto de design**: a tecnologia de um design de nave |

- **A lembrança** é uma skin, uma cor, um rastro ou uma aura ([Cosméticos](/wiki/06-Items/Cosmetics.md)), escolhida para a temporada em uma lista curta de visuais reservados para isso e nunca acima de Épico. Como todo visual, é só enfeite, pertence à sua conta e fica depois do reset. Se você já a tem, recebe a próxima lembrança que não tem. Se você as tem todas, recebe 250 Thulium.
- **O projeto** é a pesquisa de um design de nave, feita por você: a tecnologia do design e as tecnologias de que ela precisa. Converter uma nave para o design continua sendo feito na Montagem e continua custando o que diz [Designs de naves](/wiki/03-Mechanics/Ship-Designs.md#getting-a-design). O design de uma temporada é um dos 13, tomados em uma ordem fixa, de modo que um design só volta depois de 13 temporadas. Se você já o conhece, recebe o próximo design que lhe falta. Se você conhece os 13, recebe 4 Dark Matter Plates, que são itens: coloque-as no Cache de Transporte antes do reset.

## Os presentes {#the-gifts}

O presente de um dia é pequeno. É um destes:

- **Munição e foguetes**, em pilhas modestas.
- **Materiais, placas e consumíveis**, entre eles Forge kits (os materiais de uma etapa da Forja).
- **Boosters** de algumas horas. Um presente de booster soma as suas horas aos seus [boosters](/wiki/06-Items/Boosters.md#active-boosters).
- **Créditos e Thulium**, em pequenas quantidades.
- **Alguns itens especiais** (Workforce Contract, Forger's Seal): nunca mais de 4 blocos de uma temporada.

Esta página não cita nenhum presente de nenhuma temporada, porque o calendário é diferente a cada reset. A aba Calendário mostra os presentes desta temporada. Presente é presente: os itens do calendário não têm a etiqueta **Vendável** ([Itens vendáveis](/wiki/03-Mechanics/Inventory.md#marketable-items)) e não podem ser anunciados no [Leilão](/wiki/03-Mechanics/Auction.md).

## O Reset {#the-wipe}

Uma temporada nova é um calendário novo. No [Reset](/wiki/03-Mechanics/Wipe-Timeline.md), o antigo fecha e o novo abre com os seus próprios 29 presentes, e a sua contagem recomeça em 0. O reset não leva nada do que você coletou, exceto o que leva de todos os itens:

- **Apagados:** os presentes que são itens (munição, foguetes, materiais, placas, consumíveis) são apagados pelo reset se não estiverem no seu [Cache de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-). O Calendário marca esse presente com um aviso.
- **Mantidos:** boosters, créditos, Thulium, itens especiais, visuais, tecnologias (um projeto) e contêineres.
- **Os últimos quatro dias (26 a 29) só dão presentes que são mantidos**, então um presente da última semana nunca se perde por causa do reset.

## Quem chega tarde e calendários tardios {#late-joiners-and-late-calendars}

**Se você entra no meio de uma temporada,** os blocos anteriores ao seu primeiro login mostram **Antes de entrar** e não podem ser coletados. Os baús e o prêmio da temporada pedem o mesmo número de dias de todos, então um piloto que chega tarde alcança menos deles. Um piloto que faz o primeiro login no dia 16 tem 14 blocos pela frente, então 14 dias é o máximo que ele pode coletar: os dois primeiros baús e a etapa 1 do prêmio da temporada estão ao alcance, a etapa 2 (20 dias) não.

**Um calendário também pode começar tarde.** Em geral ele abre com a temporada. Pode abrir mais tarde, por exemplo quando o jogo ganha as Recompensas diárias no meio de uma temporada. Um calendário assim tem só os dias que restam, e tudo se ajusta: um que abre no dia 14 tem 16 blocos («de 16»), baús com 4, 8, 12 e 15 dias coletados e etapas do prêmio da temporada com 6 e 11. O cartão do Painel diz em que dia ele abriu. Se restam menos de 10 dias, a temporada em curso fica sem calendário (**Esta temporada não tem calendário**) e o próximo começa com o reset.

## Perguntas {#questions}

- **Por que não consigo coletar o dia N?** Há quatro motivos. O dia ainda não chegou (**Abre em …**). O dia e a tolerância dele acabaram (**Perdido**). O dia era anterior ao seu primeiro login (**Antes de entrar**). Ou a contagem regressiva do Reset começou. Uma temporada sem calendário, ou um calendário desligado, não tem nada para coletar.
- **Ele segue o meu fuso horário?** Não. O dia é um dia UTC. Só os horários mostrados são convertidos para o seu fuso horário ([O dia](#the-day)).
- **E se o servidor ficou fora do ar?** As 6 horas de tolerância cobrem uma queda curta em torno da meia-noite. Para uma mais longa, um administrador pode manter um dia aberto por mais tempo para todos. O bloco dele aparece então como **Ontem**, com a sua própria contagem regressiva.
- **Posso coletar dois dias de uma vez?** Só enquanto dois blocos estiverem abertos, nas 6 horas depois de uma meia-noite UTC: o de ontem e o de hoje, um toque cada. Um bloco não pode ser coletado duas vezes nem com antecedência.
- **Preciso entrar todo dia?** Não. Não há sequência: um dia que você pula custa o presente daquele dia, e os baús e o prêmio da temporada só contam quantos dias você coletou.
- **O Premium muda alguma coisa?** Não. O Premium não dá blocos extras nem presentes melhores, e o calendário não dá dias de Premium.
- **Preciso de um clã?** Não. O calendário usa o mesmo dia da linha diária dos clãs, mas é só seu.
- **Existe limite de nível?** Não. Todo piloto pode coletar, a partir do nível 1.
- **O que acontece no reset?** Você recebe um calendário novo e recomeça em 0 dias. Os presentes que são itens são apagados se não estiverem no Cache de Transporte; o resto é mantido ([O Reset](#the-wipe)).

## Bom saber {#good-to-know}

- Os presentes, os números e a tolerância são definidos no servidor do jogo e podem mudar com uma atualização; a aba Calendário sempre mostra os que estão em vigor.
- Um servidor de jogo anterior às Recompensas diárias não tem calendário, e o cartão e a aba ficam escondidos. Um administrador também pode desligar o calendário; o que você coletou continua coletado.
- Cada calendário novo é preparado antes do reset, para que os administradores do jogo possam olhá-lo antes de ele começar e trocar um presente errado.
