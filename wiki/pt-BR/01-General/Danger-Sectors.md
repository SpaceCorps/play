<!-- wiki-i18n source: 13c9ac551cfd01fa -->
<!-- wiki-i18n title: Setores de perigo -->
# Setores de perigo {#danger-sectors}

<!-- wiki-search: ds; ds-1; ds-2; ds-3; ds-4; central pvp zone; pvp zone; pulsar; giant excavator; excavator; dormant swamp; swamp; event 2; tech surge; setor de perigo; escavadeira gigante; escavadeira; pântano; onda tecnológica -->

Os **setores de perigo** são os quatro setores no meio da galáxia, de `DS-1` a `DS-4`. As três corporações se encontram ali, e em todos os mundos os pilotos podem lutar entre si ([Viagem pelo mapa espacial](/wiki/01-General/Spacemap%20Travel.md)). `DS-1`, `DS-2` e `DS-3` têm cada um o portão de uma corporação; `DS-4` é o núcleo, com o [buraco negro](/wiki/03-Mechanics/Black-Hole.md) no meio. Nenhum deles tem estação: os únicos lugares seguros são os anéis em volta dos portões de salto.

Uma civilização da velha galáxia viveu aqui, avançada e de um preto arroxeado, e por um motivo que ninguém conhece ela ruiu. Seus restos nunca estiveram de todo mortos: o [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md) foi o primeiro sinal. A partir do **dia 11 da temporada**, o início do evento 2 (**Onda Tecnológica**, veja a [Linha do tempo do reset](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)), mais dela desperta e os setores de perigo mudam. Todos os pilotos do mundo são avisados no dia em que começa, e o que é novo fica até o reset.

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## O que há de novo a partir do dia 11 {#what-is-new-from-day-11}

- **Escavadeiras gigantes.** `DS-1`, `DS-2` e `DS-3` têm cada um um pulsar desde o primeiro dia da temporada, uma luz no céu e nada mais; a partir do dia 11 cada um ganha uma **escavadeira gigante** ao lado. Coloque Dark Matter no tanque da escavadeira, escolha um recurso, e ela minera o pulsar: Thulium e minérios raros caem em volta dela em caixas que qualquer um pode pegar. É a coisa mais rica pela qual lutar nos setores de perigo, e a mais perigosa. Veja [Escavadeira gigante](/wiki/03-Mechanics/Giant-Excavator.md).
- **Slumbering Voids.** Enquanto uma escavadeira minera, **Slumbering Voids** chegam em ondas da borda do mapa e caçam os pilotos perto dela. Outros patrulham o pântano. Veja [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).
- **O Dormant Swamp.** Num canto de `DS-4` fica a base da civilização perdida: canhões que atiram em toda nave que veem, Inert Masses que a guardam e, no meio, o Unwakened. É um lugar que os pilotos ainda não devem visitar. Veja [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md).
- **Um Enxame Dormant mais rápido e mais rico.** O enxame agora aparece no pântano, volta mais cedo depois de destruído e paga o dobro. Veja [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md).
- **Antes do dia 11** só os pulsares brilham: de resto, os setores de perigo são como a [Viagem pelo mapa espacial](/wiki/01-General/Spacemap%20Travel.md) os descreve. Um mundo no dia 11 ou depois tem tudo de uma vez.

## Onde fica cada coisa {#where-everything-is}

Cada mundo tem a sua própria cópia de tudo, e um pulsar e sua escavadeira ficam no terço aberto do setor, longe de todos os anéis de portão, do lado que olha para o meio do mapa. As distâncias são em unidades do mapa; os setores têm 32.000 por 18.000 unidades.

<!-- danger-sites:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Setor | Portão da corporação | Pulsar | Escavadeira gigante |
| :--- | :--- | :--- | :--- |
| `DS-1` | Mars | 8.000 / 5.000 | 8.805 / 5.402 |
| `DS-2` | Terra | 8.000 / 13.000 | 8.805 / 12.598 |
| `DS-3` | Galactic | 24.000 / 13.000 | 23.195 / 12.598 |

<!-- danger-sites:end -->

`DS-4` não tem pulsar: o buraco negro está lá. Seu canto tem em vez disso o Dormant Swamp; os números do pântano estão em [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#at-a-glance).

<!-- danger-rules:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- Os pulsares brilham desde o primeiro dia da temporada; tudo o mais que é novo aparece no dia 11 da temporada e fica até o reset.
- Cada mundo tem seus próprios pulsares, escavadeiras e pântano: o que acontece em um não acontece em outro.
- Nenhum asteroide fica a menos de 2.600 unidades de um pulsar, a menos de 2.200 unidades de uma escavadeira gigante nem a menos de 4.900 unidades do meio do Dormant Swamp.

<!-- danger-rules:end -->

## Como evitar problemas {#keeping-out-of-trouble}

- **Radiação.** Uma escavadeira que superaqueceu ou foi destruída, e seu pulsar, queimam toda nave que ficar dentro dos seus círculos ([Escavadeira gigante](/wiki/03-Mechanics/Giant-Excavator.md#heat-and-radiation)). O jogo avisa antes, e os círculos são desenhados no chão durante o voo e no minimapa.
- **Os canhões do pântano.** As torres do pântano atiram numa nave que conseguem ver muito antes de ela ver algo que valha a viagem ([Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-guns)). Um rumo que você clica é desviado em volta dos canhões e da radiação, como em volta do buraco negro, e um aviso alerta quando o lugar clicado fica dentro.
- **Se você for destruído lá,** a opção de voltar **no local** o coloca no ponto mais próximo fora da radiação e fora da zona do pântano, como no buraco negro ([Primeiros passos](/wiki/01-General/Getting-Started.md#dying-and-coming-back)).
- **Um grupo e uma saída.** As escavadeiras atraem Voids e rivais por igual. Leve um [grupo](/wiki/03-Mechanics/Groups.md), saiba qual portão é o mais próximo e lembre que, nos setores de perigo, você não pode sair por salto enquanto é atacado ([Saltar sob fogo](/wiki/01-General/Spacemap%20Travel.md#jumping-under-fire)).
- **O resto é PvP como sempre.** Nada aqui é lugar seguro: valem as regras normais do seu mundo, rivais incluídos.

## Onde ler mais {#where-to-read-more}

- [Escavadeira gigante](/wiki/03-Mechanics/Giant-Excavator.md): o painel, o combustível, o que ela minera, os Voids, o calor e a radiação.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): os canhões, os três alienígenas e o novo lar do enxame.
- [Enxame Dormant](/wiki/05-Swarms/Dormant-Swarm.md) e [Enxames](/wiki/05-Swarms/Swarms.md).
- [O buraco negro](/wiki/03-Mechanics/Black-Hole.md) e [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md): de onde vem o combustível.
- [Mineração de asteroides](/wiki/03-Mechanics/Asteroid-Mining.md): as rochas dos setores de perigo.
