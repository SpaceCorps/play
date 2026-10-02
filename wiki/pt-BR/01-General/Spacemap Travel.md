<!-- wiki-i18n source: 48e9736362e10347 -->
<!-- wiki-i18n title: Viagem pelo mapa espacial -->
# Viagem pelo mapa espacial {#spacemap-travel}

O mapa espacial é a sua interface de navegação para percorrer o universo do SpaceCorps. Cada corporação controla um setor do espaço, organizado em uma topologia específica que favorece tanto a exploração segura quanto os perigosos encontros PvP.

## A estrutura do universo {#the-universe-structure}

O universo é formado por três setores principais de corporações (Mars, Terra, Galactic) e uma zona PvP central.

- **x-1 (Base de origem)**: O mapa inicial de cada corporação (M-1, T-1, G-1). A zona mais segura.
- **x-2 -> x-3**: Zonas de expansão com alienígenas cada vez mais fortes.
- **x-4 (Fronteira)**: A porta de entrada para o setor PvP.
- **DS-x (Setores de perigo)**: A zona PvP central que conecta todas as corporações: DS-1 a DS-4.

Cada [mundo](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) tem a sua própria cópia de todo este mapa, e onde os pilotos podem lutar entre si depende do mundo: em Alpha apenas em `x-4` e `DS-x`, em Beta em qualquer lugar, exceto `x-1`, em Gamma em qualquer lugar. O mapa da galáxia colore os setores conforme a regra do seu mundo.

## Visualização {#visualization}

O mapa da galáxia abaixo mostra, em tempo real, a disposição do universo conhecido.

```spacemap

```

## Como viajar {#how-to-travel}

A viagem pelo mapa espacial é feita por **portais de salto**.

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

### Ligações de salto {#jump-links}

- **O circuito da corporação**: Mars, Terra e Galactic têm a mesma disposição. As conexões seguem `1 <-> 2 <-> 3` e `2 <-> 4` e `3 <-> 4`. Isso forma um circuito entre os mapas secundários (`x-2` e `x-3`) e o mapa de fronteira (`x-4`), com `x-1` funcionando como uma ponta de entrada segura, ligada apenas a `x-2`: o seu mapa inicial tem só um portal.
- **Portais de acesso aos setores de perigo**: O mapa de fronteira de cada corporação (`x-4`) se conecta diretamente ao seu próprio setor de perigo:
  - `M-4` se conecta a `DS-1`
  - `T-4` se conecta a `DS-2`
  - `G-4` se conecta a `DS-3`
- **Rotas de invasão (viagem entre corporações)**: Para entrar no território de uma corporação inimiga, você precisa atravessar a zona PvP. Por exemplo, um piloto da Mars que queira invadir a Terra precisa voar de `M-4` até o setor de perigo `DS-1`, atravessar o portal de salto para `DS-2` e então entrar no espaço da Terra por `T-4`; para chegar à Galactic, atravesse o portal de salto para `DS-3` e entre por `G-4`.
- **O triângulo dos setores de perigo**: `DS-1`, `DS-2` e `DS-3` se conectam todos entre si. Cada um deles tem o portal de uma corporação (Mars em `DS-1`, Terra em `DS-2`, Galactic em `DS-3`); `DS-4` não tem nenhum.
- **O núcleo central**: Os três setores de perigo externos (`DS-1`, `DS-2` e `DS-3`) se conectam diretamente ao mapa central **`DS-4`**, a zona PvP mais perigosa e mais recompensadora do universo. Um **buraco negro** paira bem no meio dele: os portais e as rotas entre eles ficam bem longe, mas uma nave que entra sente a sua radiação, depois a sua atração e é destruída no horizonte de eventos. Veja [O buraco negro](/wiki/03-Mechanics/Black-Hole.md).
