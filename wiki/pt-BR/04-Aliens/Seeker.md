<!-- wiki-i18n source: f0eea7ebd1631a1f -->
<!-- wiki-i18n title: Seeker -->
# Seeker {#seeker}

Os Seekers são unidades básicas de exploração e reconhecimento. São passivos, ou seja, nunca começam um combate: um Seeker se volta contra o piloto que atira nele, e só contra esse piloto. Ele desiste se ninguém o atingir por 10 segundos, e seu casco se repara depois de ficar 30 segundos em paz. O Boss Seeker e os Seeker Slaves do [Enxame Seeker](/wiki/05-Swarms/Seeker-Swarm.md) parecem Seekers, mas são tipos próprios: os abates deles são contados com o nome deles, não como abates de Seeker.

## Atributos {#stats}

- **Pontos de vida (HP)**: 800
- **Escudo**: 800
- **Dano**: 180
- **Velocidade**: 120
- **Alcance de ataque**: 600
- **Comportamento**: Passivo

## Comportamento {#behavior}

- Um Seeker nunca vai atrás de uma nave que se aproxima: ele vagueia até alguém atirar nele e então persegue e dispara contra o primeiro piloto que atirou nele, enquanto esse piloto continuar a atingi-lo e ele conseguir alcançá-lo; os tiros de outros pilotos não o desviam nesse meio-tempo e, quando o primeiro sai da luta, ele passa ao próximo piloto que entrou na luta (veja [Contra quem um alienígena luta](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)). O fogo de outro alienígena e um acerto que não causa dano nunca o provocam.
- Ele desiste **10 segundos** depois do último acerto de quem quer que seja e volta a vaguear. Enquanto um piloto continua a atingi-lo, ele voa até esse piloto sempre que o piloto está além do alcance das suas armas (600 unidades) e dispara assim que o piloto entra no alcance.
- Ele deixa de perseguir um piloto que esteja a mais de **2.500 unidades** de distância, ou quando já voou **3.000 unidades** desde onde a perseguição começou, e não vai atrás desse piloto de novo por 8 segundos, a menos que o piloto atire nele mais uma vez (veja [Combate](/wiki/03-Mechanics/Combat.md)).
- Deixado em paz por **30 segundos**, seu casco se repara, 2% do máximo por segundo (um casco cheio em cerca de 50 segundos). Seu escudo recarrega como o de qualquer alienígena, a partir de 15 segundos depois do último acerto.
- Ele não luta com ninguém que não o tenha atingido e nunca chama outro alienígena para o seu lado.
- Os [pilotos de corporação](/wiki/03-Mechanics/Company-Pilots.md) caçam Seekers. Um piloto que atira em um deles atrai o seu fogo, a menos que o Seeker já esteja lutando contra outra pessoa.

## Recompensas {#rewards}

- **Créditos**: 1.000
- **Thulium**: 4
- **Experiência (XP)**: 100
- **Honra**: 2
- **Pontos PvE por abate**: 1
- **Recarga do escudo**: 10 por segundo (15 s de atraso)

## Saque {#loot-drops}

Cai como uma [caixa de carga](/wiki/03-Mechanics/Cargo.md) no local onde ele explode, reservada por 30 segundos a quem o abateu.

Para que serve cada item e onde mais encontrá-lo: [Recursos](/wiki/06-Items/Resources.md).

- **Ship Fragment**: 20% de chance (Mín.: 1, Máx.: 1)
- **Daraxium**: 50% de chance (Mín.: 1, Máx.: 2)

## História {#lore}

Os Seekers são sondas leves de reconhecimento lançadas pelo Enxame alienígena para mapear os portais de salto dos setores e rastrear as assinaturas eletromagnéticas das frotas humanas. Com armamento mínimo e estruturas frágeis, são extremamente passivos: recuam ou ignoram as naves, a menos que sejam atacados. Mesmo assim, coordenam-se com unidades de combate maiores e sinalizam suas posições quando entram em combate.
