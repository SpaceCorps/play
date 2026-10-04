<!-- wiki-i18n source: 4f84f886cea54500 -->
<!-- wiki-i18n title: Buraco negro -->
# O buraco negro {#the-black-hole}

No exato centro do Setor de perigo 4 (`DS-4`, o centro da zona PvP), um buraco negro paira na escuridão. Ele é o mesmo em todos os mundos (Alpha, Beta e Gamma), em todos os dias da temporada, inclusive durante o Protocolo de Paz. Ele leva o que chega perto demais e devolve uma única coisa: [Dark Matter](#dark-matter), por um foguete N.I.K.E. disparado nele.

## Os anéis {#the-rings}

As distâncias são contadas a partir do centro do setor, em unidades do mapa. O setor tem 32.000 por 18.000 unidades.

| Anel | Distância | O que acontece |
| :--- | ---: | :--- |
| **Radiação** | 4.000 | A sua nave sofre dano a cada segundo, uma parte do total dos HP máximos dela. Quanto mais perto, mais. |
| **Atração** | 3.000 | O buraco negro puxa a sua nave em direção ao centro, com mais força quanto mais perto você está. Uma nave que não está voando é arrastada. |
| **Ponto sem retorno** | cerca de 1.000 a 2.600 | Onde a atração se iguala à velocidade da sua nave. Dentro dele, mesmo a toda potência, você é puxado para dentro. Depende da sua velocidade. |
| **Horizonte de eventos** | 300 | Qualquer nave que o alcance é destruída na hora, seja qual for o casco e o escudo. |

Os portais do Setor de perigo 4 e as rotas entre eles passam bem longe da radiação, então você nunca a encontra por acidente no caminho.

## Radiação {#radiation}

O dano é uma **porcentagem do total dos HP máximos da sua nave** (casco mais escudo) a cada segundo, então toda classe de nave dura exatamente o mesmo tempo a uma dada distância: uma Protos e uma Wraith a 2.000 unidades consomem uma nave cheia em 50 segundos.

| Distância | Dano por segundo | Uma nave cheia dura |
| ---: | ---: | ---: |
| 4.000 | 0,3% | 333 s |
| 3.500 | 0,55% | 182 s |
| 3.000 | 0,8% | 125 s |
| 2.000 | 2% | 50 s |
| 1.200 | 5% | 20 s |
| 700 | 11% | 9 s |
| 300 | 24% | 4 s |

Entre duas linhas da tabela o dano sobe em linha reta. Em pontos de vida por segundo, para as configurações originais das naves:

| Nave | HP máx. total | A 3.500 | A 3.000 | A 2.000 | A 1.200 | A 700 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Protos | 30.000 | 165 | 240 | 600 | 1.500 | 3.300 |
| Kitefin | 46.000 | 253 | 368 | 920 | 2.300 | 5.060 |
| Ostirion | 82.500 | 454 | 660 | 1.650 | 4.125 | 9.075 |
| Nomad | 130.500 | 718 | 1.044 | 2.610 | 6.525 | 14.355 |
| Paragon | 162.500 | 894 | 1.300 | 3.250 | 8.125 | 17.875 |
| Storm | 194.500 | 1.070 | 1.556 | 3.890 | 9.725 | 21.395 |
| Wraith | 372.000 | 2.046 | 2.976 | 7.440 | 18.600 | 40.920 |
| Ironclad | 673.200 | 3.703 | 5.386 | 13.464 | 33.660 | 74.052 |

- O **escudo recebe o dano primeiro**, depois o casco. Não é um acerto: a absorção do escudo não entra na conta, e ele não pode ser desviado.
- A radiação conta como **dano recebido**: o seu escudo não recarrega, um drone de reparo para (“Reparos interrompidos: radiação.”) e não pode ser iniciado, e uma zona segura só protegeria você 5 segundos depois da última dose.
- Os boosters e as melhorias mudam o tamanho do seu total, não por quanto tempo você aguenta: o dano é uma parte dele.
- Nada torna uma nave imune. A radiação não é um acerto, então nada a absorve; mas as habilidades continuam funcionando nela: um Shield Surge continua restaurando o seu escudo e um Emergency Repair continua curando o seu casco durante os seus dez segundos (elas não são os reparos naturais que a dose interrompe). A camuflagem não esconde a nave da radiação.

## A atração {#the-pull}

Dentro de 3.000 unidades o buraco negro puxa toda nave em direção ao centro, e a atração só aumenta quanto mais perto você está. Ela começa suave na borda e já se faz sentir 200 unidades adentro:

| Distância | Atração (unidades por segundo) | Uma nave que não está voando é arrastada |
| ---: | ---: | :--- |
| 3.000 | 0 | nada ainda |
| 2.800 | 25 | 25 unidades em um segundo |
| 2.300 | 60 | 60 unidades em um segundo |
| 1.800 | 120 | 120 unidades em um segundo |
| 1.300 | 220 | 220 unidades em um segundo |
| 1.000 | 262 | 262 unidades em um segundo, e aumentando |
| 900 | 289 | 289 unidades em um segundo, e aumentando rápido |
| 700 | 496 | até o horizonte em cerca de um segundo |
| 300 | 2.829 | o horizonte de eventos |

De 3.000 até 925 unidades a atração sobe em linha reta entre duas linhas da tabela; dentro de 925 ela segue uma curva mais íngreme (as três últimas linhas estão nela). É uma correnteza: ela move a sua nave, e os seus motores lutam contra ela.

- **Uma nave que não voa não consegue ficar parada.** Se você para (chega ao lugar em que clicou, ou nunca deu uma ordem), o buraco negro leva a sua nave em direção ao centro e a sua ordem vai junto, então a sua nave continua caindo por mais rápidos que os motores dela pudessem voar. Para manter um lugar, você precisa continuar voando até ele: mantenha o botão do mouse pressionado sobre ele, e a sua nave se mantém onde a velocidade dela está acima da atração, cedendo um pouco entre uma ordem e outra. Duas naves que param para trocar tiros dentro da atração são arrastadas juntas para dentro.
- **Uma nave que voa sente um vento contrário.** Voando em linha reta para longe do centro, a velocidade da sua nave é reduzida pela atração no ponto onde você está: com velocidade 155, você faz 130 unidades por segundo a 2.800, 95 a 2.300 e 35 a 1.800, e a 1.500 (uma atração de 180) nenhum avanço.

O seu **ponto sem retorno** é a distância em que a atração se iguala à sua velocidade. Uma nave com velocidade 150 o tem a 1.650 unidades; quanto mais rápido você for, mais fundo ele fica:

| Nave (configuração original) | Velocidade | Ponto sem retorno |
| :--- | ---: | ---: |
| Ironclad | 99 | 1.974 |
| Protos | 155 | 1.627 |
| Kitefin | 184 | 1.480 |
| Ostirion | 208 | 1.362 |
| Nomad | 211 | 1.347 |
| Paragon | 222 | 1.287 |
| Wraith | 238 | 1.171 |
| Storm | 256 | 1.046 |

Uma nave mais rápida que 272 unidades por segundo (uma configuração de corredor, ou uma Wraith original com um Afterburner em andamento) tem o seu ponto sem retorno onde sempre esteve: com velocidade 300 ele fica em 885, com 432 em 747.

Monte para a velocidade e você consegue sair de mais fundo; carregue escudos pesados e não consegue (uma Ironclad, a nave mais lenta, com um Heavy Shield Core em todos os seus 14 slots voa a 39,1, com o ponto sem retorno em cerca de 2.600). Só uma explosão de velocidade faz uma nave voltar de logo depois do seu ponto sem retorno: um [Afterburner](/wiki/03-Mechanics/Abilities.md) em andamento conta, e leva o ponto sem retorno para mais fundo enquanto dura (dez segundos com um motor, quinze com dois, vinte com três; o Afterburner III leva o de uma Protos original de 1.627 para 1.105 e o de uma Wraith original de 1.171 para 793). Nada consegue sair de dentro de cerca de 390 unidades, nem mesmo uma nave montada para a velocidade, com todos os atributos de velocidade encantados ao máximo e a explosão mais forte em andamento (um Afterburner III encantado até o limite, x1,69); uma nave sem encantamentos, montada para a velocidade (Engine III e Adaptive Core II, com Impulse Thruster IV e Momentum Thruster IV) e com um Afterburner III, sai de fora dos 425 no melhor dos casos.

A queda a partir do ponto sem retorno começa devagar: uma nave poucas unidades dentro dele, a toda potência, é puxada para dentro ao longo de vinte segundos ou mais, e depois cada vez mais rápido. A atração não é voo: ela não conta como distância voada.

## O horizonte de eventos {#the-event-horizon}

Uma nave que chega a 300 unidades do centro é destruída. Uma nave cujo casco se esgota sob a radiação no caminho é destruída pela radiação. De um jeito ou de outro:

- É uma destruição comum: você escolhe onde voltar (veja [Destruição e reaparecimento](/wiki/01-General/Getting-Started.md)), com no máximo 10.000 de casco e o escudo vazio (veja essa página), e ela custa o que uma destruição sempre custa. “No local” nunca coloca você de volta dentro do anel: ele move você para o ponto mais próximo fora dele (a 4.500 unidades do centro) e avisa você.
- **Sem destroços, sem caixa, sem saque**, e sem perda de honra.
- A sua destruição é creditada como um abate PvP ao **último piloto inimigo que atingiu a sua nave nos 15 segundos antes de ela morrer**: um piloto de outra corporação (onde e quando o PvP é permitido), por menor que tenha sido o acerto. É um abate nas estatísticas dele e pontos de ranking PvP de acordo com o tipo da sua nave, e nada mais. Um único disparo basta, e se ninguém de outra corporação atingiu você nesses 15 segundos, ninguém ganha nada.
- Os colegas de corporação que atingiram a sua nave nesses 15 segundos ainda perdem a honra por fogo amigo, seja o que for que a destruiu.
- Os alienígenas e os pilotos de corporação nunca se aproximam dele. Se um acabar lá dentro mesmo assim, ele some sem saque, recompensa nem reivindicação.

## O que você vê e ouve {#what-you-see-and-hear}

A visão é pequena (cerca de 1.900 por 1.150 unidades na tela com o zoom padrão, 4.400 por 2.650 com o zoom todo afastado), então a imagem do próprio buraco negro só aparece a até cerca de três mil unidades dele (3.600 com o zoom todo afastado). De mais longe, nada na tela aponta para ele (olhe o minimapa ou o mapa do Sistema estelar, abaixo); o aviso da interface serve para quando você está perto:

- **De longe.** Se você abaixar a câmera para olhar ao longo do plano, o buraco negro é desenhado onde está na tela, de qualquer lugar do setor, sempre que está no quadro: um disco preto com um anel em um brilho de luz de acreção, com a escala ajustada para continuar fácil de ver (cerca de 2% da altura da visão a partir do canto mais distante, que fica a cerca de 18.000 unidades), e ele cresce até virar a sua própria imagem conforme você se aproxima. Nada nele se move sozinho. Com o buraco negro fora da visão, não há marcador dele na tela.
- **Anéis no plano de voo.** Uma faixa violeta brilha até uma borda nítida no limite da radiação (4.000 unidades), e uma mais fina, âmbar, marca o limite da atração (3.000). Dentro da atração, uma **linha vermelha** mostra o *seu próprio* ponto sem retorno. Ela acompanha a sua velocidade, então se move conforme a sua nave fica mais rápida ou mais lenta.
- **O medidor**, acima da barra de atalhos, aparece a até mil unidades da borda e fica enquanto você queima. Ele mostra a radiação em porcentagem do total de HP da sua nave por segundo, quanto tempo a radiação sozinha levaria para consumir o que resta (“Letal em 31 s”, em vermelho abaixo de dez), uma barra desse HP, a atração onde você está contra a sua velocidade e a distância que ainda falta voar até o seu ponto sem retorno, ou um aviso piscante quando você já passou dele. Passe o mouse sobre uma linha para ver o que ela significa; o (i) abre um cartão.
- **As bordas da tela** brilham em violeta, ficando vermelhas conforme a dose sobe, e pulsam uma vez por segundo.
- **O minimapa** desenha o buraco negro com os seus anéis como elipses (o mapa se estica junto com a janela dele), e a dica ao passar o mouse informa os raios. O mapa do Sistema estelar marca o setor com um pequeno buraco negro.
- **Um contador de radiação** estala mais rápido conforme a dose sobe, por cima do som da luta. Um aviso de dois tons soa quando você cruza a borda e de novo no seu ponto sem retorno, e um ronco grave é ouvido a partir de cerca de 6.500 unidades, mais grave quanto mais perto você está.
- **A imagem:** a partir da qualidade gráfica **Média** (com o pós-processamento ligado) o buraco é desenhado seguindo a luz ao redor dele, raio a raio: uma sombra preta com um fino anel de fótons branco em volta e o disco de acreção como a luz dele chegaria até você. Com a câmera alta, é um anel brilhante em volta do escuro; incline a câmera para baixo e o lado distante do disco se curva por cima do buraco e a parte de baixo dele por baixo, com o lado próximo cruzando pela frente. O céu atrás do buraco também se curva, com moderação: as estrelas, a nebulosa, os planetas e os asteroides são empurrados para fora em volta da sombra e suas linhas se curvam ao redor dela. As naves são desenhadas por cima do buraco e não ficam mais cobertas de preto por ele: um casco entre você e o buraco fica na frente. A Média segue a luz por menos voltas, desenha menos imagens do disco e deixa de fora o brilho a mais do lado que gira em sua direção, que a Alta e a Ultra acrescentam. A qualidade gráfica **Baixa**, e um quadro sem pós-processamento, mantêm a imagem antiga: um disco preto com um anel brilhante e um disco de acreção de três camadas que giram em sentidos opostos, sem curvar o céu. Uma placa de vídeo que não consegue montar a imagem nova também volta à imagem antiga, com a leve curvatura das estrelas que ela tinha. Em todas as qualidades somam-se rastros de matéria caindo ao longo da atração (eles caem na própria velocidade da atração, então uma nave que não voa é arrastada no mesmo passo que eles, e uma que voa para fora contra a atração os vê passar correndo). Uma nave que a atração arrasta não acende a chama dos motores e não deixa rastro; uma que voa para fora contra ela queima a chama na sua velocidade total através da correnteza, e o rastro dela flui em direção ao buraco. O tremor da câmera cresce com a atração, em proporção à velocidade da sua nave, está no nível definido no seu ponto sem retorno e continua subindo até o horizonte. Uma nave que o buraco está queimando solta faíscas violeta; uma que ele engole é puxada para o centro e esticada até ficar fina. O céu do setor é o violeta-escuro e verde do `DS-3`.
- **Os detritos:** rochas e pedaços de cascos destruídos giram em torno do buraco negro e caem em espirais, da borda da atração até o horizonte: devagar no início e depois cada vez mais rápido, girando em volta dele e rodopiando mais depressa quanto mais se aproximam. Eles brilham em laranja na luz do disco, são esticados em agulhas ao serem despedaçados e somem antes de chegar ao horizonte. Há algumas rochas grandes entre eles, e alguns flutuam acima do plano de voo, de modo que as naves passam por baixo. São só cenário: nada os atinge e eles não atingem nada, e só aparecem a até cerca de quatro mil unidades do buraco negro, desaparecendo aos poucos em direção a 6.500. A luz do disco também cai sobre a sua nave quando ela está perto.
- **Quando você morre**, o aviso na tela diz o motivo: “Engolido pelo buraco negro” ou “Consumido pela radiação”, e o Registro do jogo traz a linha.

As configurações ajudam quando o buraco negro pesa no desempenho do computador ou cansa os olhos: **Reduzir movimento** para o disco e os rastros, mantém os detritos parados e interrompe a pulsação das bordas da tela, e **Reduzir tremor da tela** interrompe o tremor da câmera perto do buraco; a qualidade gráfica **Baixa** mantém a imagem antiga, sem a lente por traçado de raios, desenha menos rastros (40, contra 100 na Média e 200 acima) e menos pedaços de detritos (30, contra 80 na Média e 160 acima), faz o anel brilhar mais para compensar e desenha a visão distante com um brilho a menos. Uma **qualidade das partículas** menor deixa os detritos mais ralos, do mesmo jeito que deixa mais ralas as rochas do fundo.

## Mantendo distância {#staying-out}

- O servidor guia você: uma ordem de movimento que levaria a sua nave através do anel de radiação (a 4.200 unidades do centro, um pouco mais largo que a própria radiação) é cumprida **contornando-o**, ao longo da sua borda. As ordens que terminam dentro do anel são cumpridas como dadas; entrar é uma escolha sua. As rotas através do setor ficam até um quinto mais longas; as rotas entre os portais, em nada.
- A aba **Sistema** do chat avisa você quando cruza o limite da radiação, o limite da atração e o seu próprio ponto sem retorno, e de novo quando você sai do alcance. Essas linhas não aparecem em **Global** nem em **Local**.
- Se você sai do jogo na radiação, fora da atração, volta no limite externo do anel, parado, com o casco que tinha. Se você sai **dentro da atração** (3.000 unidades), volta exatamente onde saiu, com o casco que tinha, e a queda continua: desconectar-se não é saída do buraco negro.
- Uma versão mais antiga do jogo não mostra o buraco negro. Ela ainda recebe os avisos e a condução, e ainda pode voar para dentro do anel se você der essa ordem.

Os drones voam com a sua nave. A carga nunca é deixada dentro do anel: uma caixa que cairia ali é colocada na borda. As caixas de Dark Matter são a única exceção.

## Dark Matter {#dark-matter}

O buraco devolve **Dark Matter** por um foguete **N.I.K.E.** que o alcance. Uma N.I.K.E. é um foguete de 67.500 a 75.000 de dano que atinge a primeira nave que pode ferir e se gasta nela; se nada estiver no caminho, ela voa até o buraco e é consumida quando cruza o horizonte de eventos. A [Montagem](/wiki/06-Items/Rockets.md) fabrica N.I.K.E. depois que a tecnologia delas é pesquisada ([Pesquisa](/wiki/03-Mechanics/Research.md)), cinco por criação (100.000 créditos, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite).

- **Disparo.** Uma N.I.K.E. voa 4.050 unidades em 4,5 segundos (900 por segundo) em linha reta para o ponto em que você a mirou: sem alvo selecionado, ponha o cursor sobre o buraco negro (ou aponte a sua nave para ele). Ela chega ao horizonte a partir de qualquer ponto entre a borda da radiação (4.000 unidades) e 4.380 unidades do centro. Mais longe, ela não alcança e é desperdiçada. Como todo foguete, usa a recarga compartilhada de 5 segundos (não é preciso ter um laser equipado); dispará-la encerra a sua proteção de zona segura e a sua camuflagem. **Uma nave na linha a recebe no seu lugar**: um rival esperando na borda, ou um piloto de outra corporação coletando caixas no caminho, leva de 67.500 a 75.000 de dano e o buraco não ganha nada. Alienígenas e pilotos de corporação nunca entram no anel, então manter a linha livre fica por sua conta; ela atravessa a sua própria corporação e as naves que estão a salvo de você. Se você sair do mapa depois do disparo, ela continua voando sem ferir ninguém e ainda produz a sua Dark Matter.
- **O que volta.** Cada N.I.K.E. que chega ao horizonte dá **1, 2 ou 3 Dark Matter** (2 em média, então cerca de cinco N.I.K.E. rendem dez), em uma ou duas caixas pequenas que surgem na borda da zona do buraco, **a 3.050 a 3.950 unidades do centro**, perto da linha por onde o seu disparo entrou. A atração termina em 3.000, então as caixas e as naves que as pegam não são puxadas, e a radiação ali é de 0,3 a 0,8% do HP de uma nave por segundo: um minuto no meio da faixa custa um terço da sua nave. Uma nave cheia aguenta três minutos ali.
- **De quem.** As caixas são suas, e do seu clã, durante **60 segundos** a partir do disparo. Depois disso, qualquer um no mapa pode pegá-las, e elas somem à deriva depois de **4 minutos**. O Setor de perigo é um setor PvP, então espere companhia. Um piloto que se desconecta depois de disparar ainda tem as suas caixas.
- **Quantas.** Um mapa comporta no máximo 32 caixas de Dark Matter; uma nova empurra para fora a mais antiga delas, e nunca outro tipo de caixa. O [Resource Magnet](/wiki/03-Mechanics/Cargo.md) não soma nada ao Dark Matter.
- **O que você vê.** Quando uma N.I.K.E. cruza o horizonte, ela é esticada para dentro do buraco, o espaço ondula a partir de onde ela entrou, e o disco e o anel de fótons lampejam por cerca de um segundo e meio (um terço disso, com metade da luz, com **Reduzir movimento**). Um instante depois as caixas saem do buraco e derivam até os seus lugares na borda: cada uma é uma esfera preto-violeta com a borda brilhante e cintilações, fácil de ver de longe, e com o título **Dark Matter** quando você passa o mouse sobre ela. As suas mostram, acima delas, os segundos que ainda restam e aparecem no minimapa como uma pequena marca violeta, como também aparecem para o seu clã; as caixas dos outros pilotos só aparecem no minimapa depois que o minuto delas termina.
- **Para que serve.** A Montagem prensa 5 Dark Matter com uma Velkonite Reinforced Plate e uma Orvium Reinforced Plate em uma **Dark Matter Plate**, e a [Forja](/wiki/06-Items/Forge.md) pede duas delas para elevar um item de Divino a Rompedor e de novo de Rompedor a Eterno: dez Dark Matter por etapa. O [Centro de Pesquisa](/wiki/03-Mechanics/Research.md#dark-matter) do Skylab também precisa de Dark Matter: 10 para cada uma das 15 tecnologias do topo da árvore, 150 no total, inseridas antes de a pesquisa começar.
