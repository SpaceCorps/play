<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Habilidades especiais -->
# Habilidades especiais {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; habilidades especiais; regeneração; explosão de escudo; blindagem reforçada; fúria; chamar reforços; clones; fugir e voltar; dreno de vida; pulso nova; salva de foguetes; véu; semear minas -->

Alguns alienígenas têm uma **habilidade especial**: algo que fazem uma única vez na vida, quando metade do casco já se foi. Regenerar-se, uma explosão de escudo, uma fuga, um pedido de ajuda. Nada aparece antes de começar, então toda caçada pode terminar em surpresa. Esta página diz o que cada habilidade faz e como responder a ela. Os chefes funcionam de outro jeito: mudam a forma de lutar em três etapas conforme o casco cai, e os alienígenas pequenos do último nível podem se partir em fragmentos se forem destruídos rápido demais.

## Como funciona {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Uma vez.** Um alienígena que tem uma habilidade a usa uma única vez na vida: quando, em um combate, seu casco (não o escudo) cai abaixo de 50% do máximo. Um golpe que o destrói de cima dessa linha nunca o deixa disparar, e um alienígena que não está em combate espera até que um comece.
- **Primeiro um aviso.** A habilidade começa com um aviso: um anel que se fecha sobre a nave e uma palavra acima dela. Uma habilidade cuja entrada abaixo diz que começa na hora não tem aviso. O alienígena ainda pode ser destruído durante o aviso; então nada acontece e ele paga como de costume. As espécies leves (Seeker e Phantasm) são mais rápidas: seus avisos e seus efeitos duram 50% do normal.
- **Nada aparece antes.** Um alienígena que tem uma habilidade é igual a qualquer outro, em todos os detalhes, até o aviso começar. Nada no jogo diz qual é, nem mesmo o [Guia do Viajante](/wiki/03-Mechanics/Travelers-Guide.md).
- **Quem tem uma.** Uma pequena parte dos alienígenas dos setores das corporações e dos setores de perigo: quanto mais forte o nível, maior a parte, e os líderes dos enxames (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah e Boss Crystalys) têm mais chance de ter uma do que os demais. Os alienígenas do Deep Void, das masmorras de clã e dos portões solo nunca têm uma, nem os seguidores de um enxame, as ondas de um Warden, a Dormant Force ou o Tesseract.
- **Paga o que qualquer alienígena paga.** Um alienígena que usa uma habilidade paga, solta itens e conta exatamente como um que não usa: a habilidade não acrescenta nada ao abate e tira tempo dele. O abate continua com o piloto que o tinha: enquanto o alienígena foge, se repara ou se esconde, a posse não expira.
- **Naves chamadas e cópias não são abates.** As naves que um alienígena chama e as cópias que ele faz não pagam nada, não soltam nada e não contam para nenhuma missão, estatística ou ranking. No máximo 6 existem para cada chamador e 24 em um mapa, e os alienígenas próprios do mapa continuam voltando no horário.
- **Todos no mapa veem.** Os pilotos do mapa são avisados quando uma habilidade começa: o jogo desenha o anel, a palavra e o efeito e toca um som.

<!-- mob-rules:end -->

## As doze habilidades {#the-twelve-abilities}

Uma habilidade começa com um **aviso**, a menos que a sua entrada diga que ela começa na hora: um anel que se fecha sobre a nave e uma palavra acima dela. Os tempos e os números abaixo são os das espécies pesadas. Onde um número tem vários valores, eles são dos níveis citados entre parênteses, a letra grega antes do nome de um alienígena.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Regeneração {#regenerate}

Ele fica parado e recupera 15% / 20% / 25% / 30% (α / β / γ / δ) do casco e do escudo em 6 s, sem disparar nada nesse tempo. Um dano que some 10% do casco e do escudo juntos o interrompe, e ele mantém o que já recuperou.

- **Aviso**: 1,5 s
- **A palavra sobre a nave**: REGENERANDO
- **Quem tem**: qualquer alienígena
- **Resposta**: Derrube-o com foguetes ou com uma multidão de naves, ou destrua-o durante o aviso.

### Explosão de escudo {#shield-burst}

Uma camada nova de escudo de 15% / 20% / 30% / 40% (α / β / γ / δ) do casco máximo vem por cima do escudo. Enquanto está de pé, ela absorve cada ponto de um golpe; some quando se esgota ou após 10 s.

- **Aviso**: 1 s
- **A palavra sobre a nave**: ESCUDO ATIVO
- **Quem tem**: qualquer alienígena
- **Resposta**: Munição e foguetes que perfuram escudos passam melhor por ela. Ou atire em outro alienígena até ela sumir.

### Blindagem reforçada {#hardened-plating}

Por 7 s / 8 s / 10 s (β / γ / δ) ele recebe apenas 50% de cada golpe, casco e escudo igualmente: duas vezes mais resistente. Ele continua lutando, e os números dos seus golpes ficam cinzentos.

- **Aviso**: 1,5 s
- **A palavra sobre a nave**: BLINDAGEM
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Pirate Boss e Boss Phantasm), a partir de β
- **Resposta**: Espere passar, acerte outro alienígena enquanto isso e guarde suas rajadas para depois.

### Fúria {#enrage}

Por 10 s o dano dele é multiplicado por ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) e a velocidade por ×1,25.

- **Aviso**: 1 s
- **A palavra sobre a nave**: ENFURECIDO
- **Quem tem**: qualquer alienígena
- **Resposta**: Mantenha o escudo ativo, continue se movendo e fique fora do alcance dele.

### Chamar reforços {#call-reinforcements}

4 / 6 (γ / δ) alienígenas menores entram pela borda mais próxima do mapa, em 2 ondas com 3 s de intervalo. A espécie que vem: Phantasm (chamado por Bulwark e Goombah); Bulwark (chamado por Crystalys). Juntos têm 45% / 60% (γ / δ) do casco e do escudo dele e disparam 50% da salva dele. Não pagam nada, não soltam nada e não contam para nada, e vão embora após 45 s ou quando o chamador é destruído.

- **Aviso**: 2 s
- **A palavra sobre a nave**: CHAMANDO
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Boss Phantasm e Boss Goombah), a partir de γ
- **Resposta**: Destrua o chamador: as naves dele vão junto. Uma arma que atinge uma área as limpa.

### Clones

3 (γ / δ) cópias dele aparecem ao redor, com o mesmo nome e a mesma aparência. Juntas têm 18% (γ / δ) do casco e do escudo dele; não disparam nada, não pagam nada e duram 15 s ou até o verdadeiro ser destruído. O verdadeiro usa um anel fino enquanto as cópias estão fora, e a janela de alvo chama uma cópia de "Isca".

- **Aviso**: 1 s
- **A palavra sobre a nave**: CLONANDO
- **Quem tem**: qualquer alienígena, a partir de γ
- **Resposta**: Siga o anel e a barra de casco em movimento do verdadeiro, ou use uma arma que atinge uma área.

### Fugir e voltar {#flee-and-return}

Ele foge dos atacantes com velocidade ×2 por 5 s / 6 s / 7 s / 8 s (α / β / γ / δ) e depois se volta contra o primeiro piloto que o atingiu. Nunca sai do mapa nem entra em uma zona segura, pode ser atingido o tempo todo, e o piloto que tinha o abate o mantém.

- **Aviso**: 0,5 s
- **A palavra sobre a nave**: FUGINDO
- **Quem tem**: qualquer alienígena
- **Resposta**: Persiga-o ou acerte-o com foguetes enquanto ele voa.

### Dreno de vida {#life-drain}

Por 10 s ele não dispara mais nada: uma vez por segundo drena toda nave ao alcance com uma salva completa que nada desvia, e recupera 75% / 100% / 100% (β / γ / δ) do dano que causa, no máximo 20% do casco no total.

- **Aviso**: 1 s
- **A palavra sobre a nave**: DRENANDO
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Pirate Boss, Boss Phantasm, Boss Goombah e Boss Crystalys), a partir de β
- **Resposta**: Ponha uma rocha ou uma parede na linha, fique invisível ou saia do alcance dele.

### Pulso nova {#nova-pulse}

Um anel cresce no chão ao redor dele durante o aviso. Quando o anel enche, atinge toda nave dentro dele uma vez, com 4 / 5 (γ / δ) das salvas dele. O raio, em unidades, é 700 / 800 (γ / δ).

- **Aviso**: 2,5 s
- **A palavra sobre a nave**: NOVA
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Pirate Boss, Boss Phantasm e Boss Goombah), a partir de γ
- **Resposta**: Saia do anel antes que ele encha: é a única explosão que dá para esquivar.

### Salva de foguetes {#rocket-barrage}

Em 3 s ele dispara 4 / 6 / 8 (β / γ / δ) [foguetes Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) no alvo: Rivet I / II / II (β / γ / δ). Voam em linha reta e não são teleguiados.

- **Aviso**: 1,5 s
- **A palavra sobre a nave**: SALVA
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Boss Phantasm e Boss Goombah), a partir de β
- **Resposta**: Continue se movendo: os foguetes vão em linha reta. Uma rocha no caminho os para.

### Véu {#veil}

Por 6 s / 8 s (γ / δ) uma nave a mais de 700 unidades dele não consegue travar mira nele, e uma mira já travada é perdida. Mais perto que isso ele é visto como de costume. Ele continua lutando, e uma explosão ainda o atinge.

- **Aviso**: nenhum, começa na hora.
- **A palavra sobre a nave**: SUMINDO
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Pirate Boss, Boss Phantasm, Boss Goombah e Boss Crystalys), a partir de γ
- **Resposta**: Aproxime-se a até 700 unidades.

### Semear minas {#sow-mines}

Ele planta 4 / 6 / 8 (β / γ / δ) minas em um anel de 500 unidades ao redor do lugar onde o alvo estava. Uma mina arma 3 s após cair, dura 30 s e explode uma vez, sob a primeira nave de piloto que passar sobre ela, com 2 / 3 / 3 (β / γ / δ) das salvas do alienígena. Uma mina nunca fere um alienígena.

- **Aviso**: 1,5 s
- **A palavra sobre a nave**: SEMEANDO MINAS
- **Quem tem**: as espécies pesadas (Bulwark, Goombah e Crystalys) e os líderes de enxame pesados (Pirate Boss, Boss Phantasm, Boss Goombah e Boss Crystalys), a partir de β
- **Resposta**: Contorne-as: elas aparecem desenhadas no chão e armam tarde.


<!-- mob-abilities:end -->

## Divisão {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Os alienígenas pequenos do último nível também podem se dividir quando são destruídos rápido demais. Isso é só dos Seeker, Phantasm, Bulwark, Goombah e Crystalys do nível δ e de nenhum outro alienígena, e não é uma das habilidades acima: um alienígena pode ter as duas.

- **Quando**: um piloto o destrói em até 5 s do primeiro dano que ele sofreu. Nem todo alienígena que morre tão rápido se divide.
- **O que sai**: 3 alienígenas da mesma espécie e nível, com 70% do tamanho, cada um com 25% do casco e do escudo e uma salva completa, ao redor do lugar onde foi destruído. Eles vão atrás do piloto que o destruiu e vão embora após 180 s.
- **São alienígenas comuns**: cada um paga o que a sua espécie paga, solta o que ela solta e conta para missões e estatísticas. Não têm habilidade e nunca se dividem.
- **Limites**: no máximo 60 fragmentos existem em um mapa, e eles não seguram os alienígenas próprios do mapa.
- **O que significa**: uma tripulação que destrói seus alienígenas rápido o bastante pode ganhar até 4 abates de um só alienígena. Uma que não consegue não ganha nada com isso.

<!-- mob-split:end -->

## As três etapas dos chefes {#the-bosses-three-steps}

Cada chefe muda a forma de lutar em três etapas: quando a luta começa, quando o casco cai abaixo de dois terços e quando cai abaixo de um terço. Uma etapa acontece uma vez e nunca volta atrás, a menos que o chefe recomece, como se diz abaixo.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Uma pausa em cada etapa.** Quando uma etapa que tem algo a fazer começa depois da primeira, o chefe não pode ser ferido por 1,5 s (3 s para o Dungeon Warlord e os chefes dos portões solo).
- **Também uma habilidade especial.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah e Boss Crystalys também podem ter uma habilidade especial (Dormant Force e Tesseract nunca): ela vem entre a segunda e a terceira etapa; quando as duas começariam juntas, a que vem depois espera 3 s no máximo. Nunca é uma habilidade que as próprias etapas do líder usam.
- **Recomeçar.** Tesseract recomeça suas etapas depois de se reparar por completo.

### Os líderes do enxame {#the-swarm-leaders}

| Líder | No início | Abaixo de dois terços | Abaixo de um terço |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Dispara um leque de 3 foguetes, 12 graus entre si, no primeiro piloto que o atingiu. | Chama mais 5 Pirate Scouts de uma vez, no máximo 10 vivos. Não pagam nada e vão embora após 45 s. | Voa com velocidade ×1,8 até o portão mais próximo por 10 s e depois se volta contra os pilotos. |
| **Boss Seeker** | Seus Seeker Slaves o reparam ×2 mais rápido por 8 s. | 2 cópias dele aparecem, e o verdadeiro usa um anel. | Foge dos pilotos por 4 s e depois se volta contra eles. |
| **Boss Phantasm** | Cada um dos seus Phantasm Guards ergue uma camada de escudo de 10% do próprio casco. | 3 cópias dele aparecem, e o verdadeiro usa um anel. | Salta cerca de 2.500 unidades para longe dos pilotos, e seus Phantasm Guards voltam inteiros ao redor dele. |
| **Boss Goombah** | Recebe 50% de cada golpe por 6 s. | O dano dele é multiplicado por ×1,5 e a velocidade por ×1,25 por 10 s. | Recupera 25% do casco e do escudo (uma rajada de dano o interrompe), e seus Goombah Guards o reparam ×2 mais rápido nesse tempo. |
| **Boss Crystalys** | Recebe 50% de cada golpe por 8 s. | Um anel de 700 unidades atinge toda nave dentro dele com 4 das salvas dele, e ele dispara 4 foguetes. | Recupera 20% do casco e do escudo (uma rajada de dano o interrompe), e chegam mais 3 Crystalys Guards, no máximo 6 vivos. |
| **Dormant Force** | Recebe 70% de cada golpe enquanto um dos seus Dormant Pulses estiver vivo. | Seus Dormant Pulses disparam um foguete a cada 2,5 s por 15 s. | Enquanto todos os seus Dormant Pulses estiverem vivos, eles o reparam em 5% do casco por segundo por 6 s. |
| **Tesseract** | – | Chegam de uma vez mais 20 Facets, acima do número habitual. | – |

### Os Warden de clã {#the-clan-wardens}

| Warden | No início | Abaixo de dois terços | Abaixo de um terço |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Todos os 4 drones vêm para o lado dele de uma vez. | Seus drones o reparam ×1,5 mais rápido por 15 s. | Vêm mais 2 drones, acima do número habitual, por 30 s. Eles não pagam nada. |
| **Siege Warden** (I, II, III) | – | Dispara o foguete ×2 mais vezes por 20 s. | Recupera 15% do casco e do escudo (uma rajada de dano o interrompe). |
| **Wrath Warden** (I, II, III) | – | Seus lasers atingem ×1,25 mais forte. | Seus lasers atingem ×1,5 mais forte no total, não somado à etapa anterior. |

### O Dungeon Warlord {#the-dungeon-warlord}

- **Abaixo de dois terços**: O intervalo entre as habilidades cai para 4 s e as esperas delas para ×0,75.
- **Abaixo de um terço**: O intervalo cai para 2 s, as esperas para ×0,5 e o dano sobe para ×1,25; ele lança uma salva de Meteor grátis, e o Swarm dele nunca volta mais rápido que a cada 120 s.
- **Uma pausa em cada etapa.** Quando uma etapa começa, o Warlord não pode ser ferido por 3 s.

### Os chefes dos portões solo {#the-solo-gate-bosses}

Os seis chefes dos portões solo também têm três etapas, as suas fases: estão na tabela dos [chefes](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) do artigo Portões solo.

<!-- mob-ladders:end -->

## Para saber mais {#where-to-read-more}

- [Combate](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): contra quem um alienígena luta e quem fica com a sua destruição.
- [Enxames](/wiki/05-Swarms/Swarms.md): os líderes e as suas etapas, um artigo para cada enxame.
- [Warden de clã](/wiki/03-Mechanics/Clans.md#fighting-a-warden), o [Warlord da masmorra](/wiki/03-Mechanics/Dungeons.md#the-warlord) e os [chefes dos portões solo](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Guia do Viajante](/wiki/03-Mechanics/Travelers-Guide.md): o que você aprendeu sobre um alienígena. Ele nunca diz qual deles tem uma habilidade.
