<!-- wiki-i18n source: ff48d8fc96e1198c -->
<!-- wiki-i18n title: Extras -->
# Extras

Os extras são os equipamentos utilitários dos **slots extras** de uma nave (dois na Protos, na Kitefin, na Ostirion e na Nomad, as naves com que você começa ou que compra, e três na Paragon, na Ironclad, na Wraith e na Storm, as naves que você fabrica, por configuração, e 3, 5 ou 7 a mais com as Extra Slots CPUs). Você ativa um pelo seletor de Extras da barra de atalhos ou por um slot da barra de atalhos que você tenha dado a ele. Eles só funcionam na configuração que você pilota: equipe um na outra configuração e ele espera até você trocar.

| Extra | O que faz | Usos | Preço |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I a IV** | Repara seu casco, 1,5%, 2,25%, 3,5% e 5% do máximo por segundo | ilimitados | 5.000 / 15.000 / 35.000 créditos, 2.000 Thulium |
| **Cloaking CPU S** | Esconde sua nave | 10 | 5.000 Thulium |
| **Cloaking CPU M** | Esconde sua nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Esconde sua nave | 50 | 20.000 Thulium |
| **EMP Charge** | Por 3 segundos ninguém pode mirar em você, toda trava sobre você se desfaz e toda camuflagem perto de você termina | 1 | 500 Thulium |

As Cloaking CPUs e a EMP Charge são vendidas só na Loja. Elas não podem ser fundidas, e nada as dá de graça.

O **kit inicial** de um piloto novo já equipa dois extras nos dois slots extras da Protos: uma **Base CPU I** (10 usos, um teletransporte até a base da sua corporação) e um **Repair Drone I**. Arraste-os do seletor de Extras da barra de atalhos para um slot para usá-los. Só os pilotos novos recebem o kit: quem se alistou antes da 0.4.10 não o tem.

Mais sete CPUs não são vendidas: a Montagem as cria depois que o Centro de Pesquisa do Skylab as pesquisou (veja [Pesquisa](/wiki/03-Mechanics/Research.md)). São a Extra Slots CPU I, II e III, a Jump CPU, a Base CPU I e II e a Auto-Repair CPU, e [a última seção](#research-cpus) diz o que cada uma faz. Como a Cloaking CPU, a Jump CPU e as Base CPUs são para um momento tranquilo: nenhuma das três inicia em até 10 segundos depois de um tiro seu ou de um acerto que você sofra. As duas CPUs de warp, a Jump CPU e as Base CPUs, também são recusadas enquanto você carrega um item de missão (“Você não pode usar um CPU de warp enquanto carrega um item de missão.”): veja [Itens de missão](/wiki/03-Mechanics/Quests.md#quest-items).

Cada extra tem uma etiqueta curta no seu slot da barra de atalhos: **REP** para um Repair Drone, **CLK** para uma Cloaking CPU, **EMP** para a EMP Charge e **ARP**, **BSE** e **JMP** para a Auto-Repair CPU, as Base CPUs e a Jump CPU. As Extra Slots CPUs não têm slot: elas se instalam no seu Skylab. Aponte para um slot para ler o que um clique faz agora, ou por que não pode fazer nada.

![The Extras picker of the hotbar: Cloaking, Base and Jump CPUs to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Drones de reparo {#repair-drones}

Ative um Repair Drone (REP) e ele conserta o casco até que esteja cheio. Ele só começa depois de 10 segundos sem sofrer um acerto, e qualquer acerto o desliga. Com vários equipados, funciona o melhor deles. Uma [Auto-Repair CPU](#auto-repair-cpu) o liga de novo por você. As taxas estão em [Combate](/wiki/03-Mechanics/Combat.md). Enquanto repara, pequenos drones de reparo saem da nave, giram em volta dela e atingem o casco com feixes, um para um Repair Drone I, dois para um II, três para um III ou IV, e os pilotos por perto os veem; eles voltam a acoplar quando o reparo para.

## Cloaking CPU

Pressione o slot CLK para se camuflar. **Um acionamento é um uso**, seja qual for o pacote, e você vê os usos restantes no slot e no hangar. A camuflagem **não tem limite de tempo**: ela continua ativa até você desligá-la ou algo a quebrar.

- **Quem não vê você.** Pilotos de outras corporações e alienígenas não veem sua nave de forma alguma: ela não aparece na tela nem na lista de alvos deles, e ninguém pode travá-la. Os pilotos de corporação das outras corporações também a ignoram.
- **O ponto no radar.** Todo outro piloto no mapa, exceto os da sua própria corporação, vê um simples **ponto vermelho** no minimapa onde você está, para saber que há alguém camuflado por perto. O ponto não tem nome, nave, corporação nem ID e não pode ser clicado nem marcado como alvo; ao passar o mouse sobre ele, aparece só “Há algo camuflado aqui”. Ele é redondo, dentro de um anel (as naves no minimapa são quadrados), e o anel “respira” devagar, ou fica parado se você ativou Reduzir movimento. O servidor o atualiza cerca de duas vezes por segundo e o seu jogo o move suavemente entre uma atualização e outra. Ele diz que há alguém ali e onde, não quem: um piloto que viu você se camuflar pode seguir o ponto, e a **explosão de um foguete** mirada nele ainda encontra você.
- **Quem vê.** Você vê sua própria nave, esmaecida, com um contorno. Os pilotos da sua corporação veem você como um fantasma pálido; os colegas de clã de outras corporações não veem, porque um clã aceita qualquer um que se candidate. Ninguém pode marcar o fantasma como alvo, nem mesmo a sua corporação.
- **Você não pode se camuflar** dentro de uma zona segura, enquanto a CPU recarrega, nem nos **10 segundos** seguintes a um acerto sofrido ou a um tiro disparado.
- **O que a encerra.** Pressionar o slot de novo, a sua primeira rajada ou o seu primeiro foguete (o disparo atinge o alvo e você é visto), entrar em uma zona segura, a CPU sair da configuração que você pilota, um **EMP disparado a até 1.500 unidades** de você, seja quem for que o disparou (também o da sua própria corporação, mas não o de um colega de grupo), e a explosão em área de um foguete que atinge você. O tempo não a encerra, coletar carga não (uma caixa que você pega some para todos, então eles ficam sabendo que havia algo ao alcance daquele ponto, mas não quem), as habilidades não, e a radiação do buraco negro fere uma nave camuflada, mas não encerra a camuflagem dela. Sair do jogo ou morrer a encerra, porque uma nave que ninguém pilota não está camuflada.
- **Recarga.** Depois que uma camuflagem termina, de qualquer maneira que tenha terminado, a CPU recarrega por **60 segundos**. A recarga pertence a você, não à nave: ela continua se você saltar por um portal, sair do jogo ou morrer. Cada acionamento ainda custa um uso.
- **Os alienígenas** que estavam atrás de você perdem você de vista. Suas reivindicações de abate são liberadas quando você se camufla.
- **Foguetes.** Ninguém pode travar um foguete guiado em você, e um foguete reto de alvo único atravessa você. Uma **explosão em área** ainda fere uma nave que ela cubra e encerra a camuflagem dela, e os pilotos que conseguem ver o local da nave a veem antes de o número de dano aparecer. Lançar um foguete é um disparo: ele encerra a sua própria camuflagem como uma rajada (a CPU então recarrega pelos 60 segundos acima) e, camuflado ou não, impede você de se camuflar nos 10 segundos seguintes.
- **O buraco negro** engole uma nave camuflada como qualquer outra, e o mapa toma conhecimento.
- **O que você vê.** Sua nave fica translúcida, com um contorno tracejado violeta, e uma etiqueta no topo da tela diz “Camuflado” com os usos restantes (sem segundos: não há temporizador). O slot CLK mostra os usos restantes; enquanto você está camuflado, ele brilha em violeta e mostra ON, e quando a camuflagem termina, de qualquer maneira que tenha terminado, ele escurece e conta os 60 segundos de recarga. Um acionamento que o servidor recusa (em recarga, em zona segura, com um acerto ou um tiro nos últimos 10 segundos) faz o slot piscar em vermelho, e uma mensagem diz o motivo. Um aliado aparece como um fantasma pálido com uma marca de fantasma antes do nome, e um piloto que se camufla perto de você some em uma ondulação. Arraste o CLK dos Extras da barra de atalhos para um slot para usá-lo, como o REP.
- **Os usos** são salvos com a CPU. Sair do jogo, morrer ou reiniciar o jogo não devolve nenhum, e uma ativação que você cancela continua gasta. Quando o último uso de um pacote acaba, ele é consumido e o slot dele é reabastecido com uma CPU igual que esteja sobrando no seu inventário, se você tiver.
- **Várias CPUs** em uma mesma configuração não se somam. A que tem menos usos restantes é usada primeiro.

As versões S, M e L se comportam igual: os pacotes maiores só saem mais baratos por uso (500, 450 e 400 Thulium).

## EMP Charge

Pressione o slot EMP em uma luta. Por **3 segundos** ninguém pode travar você, e **todos que estavam com você travado perdem a trava** na hora, onde quer que estejam: pilotos, alienígenas e pilotos de corporação. Um piloto cuja trava se desfaz recebe o aviso “Trava perdida: o alvo usou um EMP”. Quem tentar travar você nesses 3 segundos é recusado.

- **Não é invulnerabilidade.** Ele impede o que precisa de trava: lasers, foguetes guiados e o toque de um foguete reto de alvo único, que atravessa você. Uma **explosão em área** não precisa de trava, então ainda fere você se você estiver dentro dela, e o buraco negro não é um tiro de forma alguma.
- **Você ainda pode agir.** Atirar não o encerra. Você pode se camuflar (se as regras da própria camuflagem permitirem) e usar outros extras.
- **Ele encerra as camuflagens por perto.** Toda nave camuflada a até **1.500 unidades** de você quando o pulso dispara é revelada na hora e a CPU dela começa os 60 segundos de recarga, seja qual for a corporação dela, inclusive a sua; as naves do seu próprio [grupo](/wiki/03-Mechanics/Groups.md) são a exceção: elas mantêm as camuflagens. O piloto recebe o aviso “Camuflagem desfeita: um EMP foi disparado por perto.”, vê a nave reaparecer com a mesma ondulação de qualquer fim de camuflagem, e o slot começa a recarregar. Você não pode usar um EMP enquanto você mesmo estiver camuflado.
- **Ele não esconde nada.** Todo mundo ainda vê você, com uma casca elétrica crepitante durante os 3 segundos.
- **Você não pode usá-lo** enquanto uma zona segura protege você, enquanto estiver camuflado, nem nos **30 segundos** seguintes ao último. Ele funciona em qualquer outro lugar, inclusive nos primeiros dias de uma temporada (o Protocolo de Paz): os alienígenas continuam caçando nesse período.
- Um alienígena que você acerta durante os 3 segundos só se volta contra você quando eles terminam. Suas reivindicações de abate e as regras do primeiro acerto não mudam.
- **O que você vê.** Um pulso de espaço distorcido se propaga a partir do piloto até onde o pulso encerra camuflagens (1.500 unidades), todos no alcance o veem, e uma casca elétrica crepitante envolve a nave durante os 3 segundos, com um anel em volta da sua própria nave e uma etiqueta no topo da tela que contam o tempo. O anel de alvo de todos que tinham você selecionado se desfaz, com um curto estalo. O slot EMP mostra as cargas que você tem, acende em azul enquanto a casca está ativa e escurece enquanto recarrega.
- **Uma carga, um uso.** O slot é reabastecido a partir do seu inventário quando você tem mais. Os **30 segundos** de recarga não são salvos: sair do jogo ou saltar por um portal os zera, e o pulso seguinte custa uma carga.

## CPUs do Centro de Pesquisa {#research-cpus}

Duas das CPUs pedem Dark Matter Plates, como o último nível de cada cadeia de melhoria: o **Extra Slots CPU III** pede 3 (e 6 Orvium Reinforced Plates) e o **Base CPU II** pede 3 (e 2 Orvium Reinforced Plates), então pesquise antes a Dark Matter Plate ([Dark Matter e Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

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


<!-- research-cpus:end -->
