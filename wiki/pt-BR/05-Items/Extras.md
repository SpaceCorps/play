<!-- wiki-i18n source: 46436d9c65bc6c7e -->
<!-- wiki-i18n title: Extras -->
# Extras {#extras}

Os extras são os equipamentos utilitários dos **slots extras** de uma nave (três em cada nave, por configuração). Você ativa um pelo seletor de Extras da barra de atalhos ou por um slot da barra de atalhos que você tenha dado a ele. Eles só funcionam na configuração que você pilota: equipe um na outra configuração e ele espera até você trocar.

| Extra | O que faz | Usos | Preço |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I a IV** | Repara seu casco, 1,5%, 2,25%, 3,5% e 5% do máximo por segundo | ilimitados | 5.000 / 15.000 / 35.000 créditos, 2.000 Thulium |
| **Cloaking CPU S** | Esconde sua nave | 10 | 5.000 Thulium |
| **Cloaking CPU M** | Esconde sua nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Esconde sua nave | 50 | 20.000 Thulium |
| **EMP Charge** | Por 3 segundos ninguém pode mirar em você, toda trava sobre você se desfaz e toda camuflagem perto de você termina | 1 | 500 Thulium |

As Cloaking CPUs e a EMP Charge são vendidas só na Loja. Elas não podem ser fundidas, e nada as dá de graça.

## Drones de reparo {#repair-drones}

Ative um Repair Drone (REP) e ele conserta o casco até que esteja cheio. Ele só começa depois de 10 segundos sem sofrer um acerto, e qualquer acerto o desliga. Com vários equipados, funciona o melhor deles. As taxas estão em [Combate](/wiki/03-Mechanics/Combat.md).

## Cloaking CPU {#cloaking-cpu}

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

## EMP Charge {#emp-charge}

Pressione o slot EMP em uma luta. Por **3 segundos** ninguém pode travar você, e **todos que estavam com você travado perdem a trava** na hora, onde quer que estejam: pilotos, alienígenas e pilotos de corporação. Um piloto cuja trava se desfaz recebe o aviso “Trava perdida: o alvo usou um EMP”. Quem tentar travar você nesses 3 segundos é recusado.

- **Não é invulnerabilidade.** Ele impede o que precisa de trava: lasers, foguetes guiados e o toque de um foguete reto de alvo único, que atravessa você. Uma **explosão em área** não precisa de trava, então ainda fere você se você estiver dentro dela, e o buraco negro não é um tiro de forma alguma.
- **Você ainda pode agir.** Atirar não o encerra. Você pode se camuflar (se as regras da própria camuflagem permitirem) e usar outros extras.
- **Ele encerra as camuflagens por perto.** Toda nave camuflada a até **1.500 unidades** de você quando o pulso dispara é revelada na hora e a CPU dela começa os 60 segundos de recarga, seja qual for a corporação dela, inclusive a sua; as naves do seu próprio [grupo](/wiki/03-Mechanics/Groups.md) são a exceção: elas mantêm as camuflagens. O piloto recebe o aviso “Camuflagem desfeita: um EMP foi disparado por perto.”, vê a nave reaparecer com a mesma ondulação de qualquer fim de camuflagem, e o slot começa a recarregar. Você não pode usar um EMP enquanto você mesmo estiver camuflado.
- **Ele não esconde nada.** Todo mundo ainda vê você, com uma casca elétrica crepitante durante os 3 segundos.
- **Você não pode usá-lo** enquanto uma zona segura protege você, enquanto estiver camuflado, nem nos **30 segundos** seguintes ao último. Ele funciona em qualquer outro lugar, inclusive nos primeiros dias de uma temporada (o Protocolo de Paz): os alienígenas continuam caçando nesse período.
- Um alienígena que você acerta durante os 3 segundos só se volta contra você quando eles terminam. Suas reivindicações de abate e as regras do primeiro acerto não mudam.
- **O que você vê.** Um pulso de espaço distorcido se propaga a partir do piloto até onde o pulso encerra camuflagens (1.500 unidades), todos no alcance o veem, e uma casca elétrica crepitante envolve a nave durante os 3 segundos, com um anel em volta da sua própria nave e uma etiqueta no topo da tela que contam o tempo. O anel de alvo de todos que tinham você selecionado se desfaz, com um curto estalo. O slot EMP mostra as cargas que você tem, acende em azul enquanto a casca está ativa e escurece enquanto recarrega.
- **Uma carga, um uso.** O slot é reabastecido a partir do seu inventário quando você tem mais. Os **30 segundos** de recarga não são salvos: sair do jogo ou saltar por um portal os zera, e o pulso seguinte custa uma carga.
