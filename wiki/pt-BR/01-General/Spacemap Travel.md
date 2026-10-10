<!-- wiki-i18n source: 129abc8d9ddf80be -->
<!-- wiki-i18n title: Viagem pelo mapa espacial -->
# Viagem pelo mapa espacial {#spacemap-travel}

O mapa espacial é a sua interface de navegação para percorrer o universo do SpaceCorps. Cada corporação controla um setor do espaço, organizado em uma topologia específica que favorece tanto a exploração segura quanto os perigosos encontros PvP.

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## A estrutura do universo {#the-universe-structure}

O universo é formado por três setores principais de corporações (Mars, Terra, Galactic) e uma zona PvP central.

- **x-1 (Base de origem)**: O mapa inicial de cada corporação (M-1, T-1, G-1). A zona mais segura.
- **x-2 -> x-3**: Zonas de expansão com alienígenas cada vez mais fortes.
- **x-4 (Fronteira)**: A porta de entrada para o setor PvP e para o `x-3` de outra corporação (o Anel, abaixo).
- **DS-x (Setores de perigo)**: A zona PvP central que conecta todas as corporações: DS-1 a DS-4. Ele contém um pulsar em cada um de DS-1 a DS-3 desde o primeiro dia da temporada e, a partir do dia 11, uma escavadeira gigante ao lado de cada um e o Dormant Swamp ([Setores de perigo](/wiki/01-General/Danger-Sectors.md)).

Só as bases de origem têm uma estação. É nela que abre **Mission Control**, e a zona segura dela alcança 1.600 unidades ao redor. Os setores de perigo não têm estação, nem o `DS-1`: as únicas zonas seguras ali são os anéis de 660 unidades ao redor dos portais de salto, e **Mission Control** não pode ser aberto ali; volte voando à sua base para ver as suas missões.

Cada [mundo](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) tem a sua própria cópia de todo este mapa, e onde os pilotos podem lutar entre si depende do mundo: em Alpha apenas em `x-4` e `DS-x`, em Beta em qualquer lugar, exceto `x-1`, em Gamma em qualquer lugar. O mapa da galáxia colore os setores conforme a regra do seu mundo.

## Visualização {#visualization}

O mapa da galáxia abaixo mostra, em tempo real, a disposição do universo conhecido. No jogo, esse mesmo mapa é a janela **Sistema estelar**.

```spacemap

```

Com uma [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) equipada, o mapa também escolhe o seu destino: pressione o slot da CPU na barra de atalhos (**JMP**) e a janela Sistema estelar abre em modo de seleção. Os setores aonde a CPU pode levar você ficam iluminados; o seu próprio setor e os setores de perigo, não. Aponte para um setor iluminado para ler o preço, clique nele e confirme o salto quando o mapa pedir (500 Thulium).

## Como viajar {#how-to-travel}

A viagem pelo mapa espacial é feita por **portais de salto**. A [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) é o outro caminho: ela não precisa de portal (veja o fim desta página).

1. **Encontre um portal**: Os portais ficam, em geral, nos cantos ou nas bordas de um mapa.
2. **Navegação**: Voe com a sua nave até perto da estrutura do portal.
3. **Ativação**: Pressione **'J'** a até 500 unidades do portal para iniciar o salto.
4. **Aguarde**: O salto **leva 3 segundos**. Enquanto isso, uma barra acima da sua barra de atalhos (“Saltando…”) se enche, e o portal brilha mais forte conforme se carrega; os outros pilotos veem a mesma carga no portal quando você salta. Sua nave continua voando, mas você precisa ficar a até 500 unidades do portal até o tempo acabar: se sair do alcance, o salto é cancelado (“Portal longe demais para saltar.”, e a barra fica vermelha). Pressionar **'J'** de novo durante o salto não faz nada, só avisa você disso.
5. **Destino**: Você chega ao portal correspondente no mapa de destino.

### Saltar sob fogo {#jumping-under-fire}

- **Fora dos setores de perigo**, ser atacado, por alienígenas ou por outros pilotos, **não** interrompe o seu salto: ele se completa.
- **Nos setores de perigo (`DS-1` a `DS-4`)** você não pode saltar para fora enquanto está sendo atacado. Se um piloto ou um alienígena atingiu a sua nave (os escudos ou o casco) nos últimos **10 segundos**, o salto não começa (“Você está sob ataque: não é possível saltar para fora de um setor de perigo.”), e um acerto durante o salto o cancela (a barra fica vermelha e o jogo diz o motivo). O dano que você sofre pela radiação do buraco negro não é um ataque, nem um tiro que uma zona segura bloqueou. Um acerto que você levou no mapa de onde saltou não segue você pelo portal: você chega com a ficha limpa.
- Você faz uma coisa de cada vez: não é possível coletar uma [caixa de carga](/wiki/03-Mechanics/Cargo.md) enquanto salta, e iniciar um salto cancela uma coleta que você tinha começado.
- Fechar o jogo ou voltar à base no meio de um salto o cancela: você não chega.
- **O teletransporte de uma CPU carrega como um salto de portal.** Uma Jump CPU carrega por 5 segundos e uma Base CPU por 10, com uma barra acima da barra de atalhos. Um tiro seu ou um acerto que você sofra, em qualquer setor, cancela o teletransporte (nada é pago nem gasto), e nenhuma das duas CPUs inicia em até 10 segundos depois de um tiro ou de um acerto. Pressione o slot da CPU de novo para cancelá-lo você mesmo.

### Ligações de salto {#jump-links}

- **O circuito da corporação**: Mars, Terra e Galactic têm a mesma disposição. As conexões seguem `1 <-> 2 <-> 3` e `2 <-> 4` e `3 <-> 4`. Isso forma um circuito entre os mapas secundários (`x-2` e `x-3`) e o mapa de fronteira (`x-4`), com `x-1` funcionando como uma ponta de entrada segura, ligada apenas a `x-2`: o seu mapa inicial tem só um portal.
- **Portais de acesso aos setores de perigo**: O mapa de fronteira de cada corporação (`x-4`) se conecta diretamente ao seu próprio setor de perigo:
  - `M-4` se conecta a `DS-1`
  - `T-4` se conecta a `DS-2`
  - `G-4` se conecta a `DS-3`
- **O Anel**: O mapa de fronteira de cada corporação (`x-4`) tem mais um portal, para o `x-3` da **próxima corporação**, e todo `x-3` tem o portal de volta. As três ligações formam um anel em volta dos setores de perigo, de modo que cada corporação tem um caminho de saída e um de entrada:
  - `M-4` se conecta ao `T-3` da Terra
  - `T-4` se conecta ao `G-3` da Galactic
  - `G-4` se conecta ao `M-3` da Mars

  O Anel está aberto a todos os pilotos, seja qual for a corporação por que voem: é uma segunda forma de viajar entre os mapas das corporações que não atravessa a zona PvP. Um portal do Anel fica num canto só seu, longe dos outros portais do seu mapa, com a zona segura de sempre de 660 unidades ao redor, e o salto funciona como em qualquer portal. Onde você pode ser atacado do outro lado depende do seu mundo, como em todo lugar: em Alpha `T-3` não é um setor PvP, mas `T-4` é; em Beta os dois são; em Gamma todos os setores são.
- **Rotas de invasão (viagem entre corporações)**: Há dois caminhos pelos portais para o território de outra corporação. O curto é o Anel: um piloto da Mars voa de `M-4`, pelo portal do Anel, até o `T-3` da Terra (três saltos a partir da base da Mars, `M-1` → `M-2` → `M-4` → `T-3`) e segue para `T-4` ou `T-2`; o `G-4` da Galactic leva ao `M-3` da Mars e o `T-4` da Terra ao `G-3` da Galactic, do mesmo modo. O longo atravessa a zona PvP: de `M-4` até o setor de perigo `DS-1`, pelo portal de salto para `DS-2` e então para o espaço da Terra por `T-4`; para chegar à Galactic, atravessa-se o portal de salto para `DS-3` e entra-se por `G-4`.
- **O triângulo dos setores de perigo**: `DS-1`, `DS-2` e `DS-3` se conectam todos entre si. Cada um deles tem o portal de uma corporação (Mars em `DS-1`, Terra em `DS-2`, Galactic em `DS-3`); `DS-4` não tem nenhum.
- **O núcleo central**: Os três setores de perigo externos (`DS-1`, `DS-2` e `DS-3`) se conectam diretamente ao mapa central **`DS-4`**, a zona PvP mais perigosa e mais recompensadora do universo. Um **buraco negro** paira bem no meio dele: os portais e as rotas entre eles ficam bem longe, mas uma nave que entra sente a sua radiação, depois a sua atração e é destruída no horizonte de eventos. Veja [O buraco negro](/wiki/03-Mechanics/Black-Hole.md). A partir do dia 11 da temporada o canto superior esquerdo de `DS-4` abriga o [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), cujos canhões atiram em toda nave que veem.

### A Jump CPU {#the-jump-cpu}

A [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) leva a sua nave a qualquer setor de corporação do seu mundo sem usar um portal, por 500 Thulium o salto, inclusive os setores de origem dos inimigos. Ela nunca leva a um setor de perigo, não começa em combate e você a pesquisa antes no Centro de Pesquisa do Skylab ([Pesquisa](/wiki/03-Mechanics/Research.md)). As [Base CPUs](/wiki/06-Items/Extras.md#base-cpus) levam você para casa do mesmo jeito. Uma CPU de warp, isto é, a Jump CPU ou uma Base CPU, é recusada enquanto você carrega um item de missão (“Você não pode usar um CPU de warp enquanto carrega um item de missão.”): volte para casa pelos portais ([Itens de missão](/wiki/03-Mechanics/Quests.md#quest-items)).
