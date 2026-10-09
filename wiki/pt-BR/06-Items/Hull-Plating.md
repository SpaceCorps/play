<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Blindagem de casco -->
# Blindagem de casco {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; blindagem; slot de blindagem; placa de casco -->

O estudo do enxame Dormant mostrou avanços na tecnologia de blindagem. Com ela, as naves podem melhorar o casco: a **blindagem de casco** é uma blindagem que se encaixa em um slot de placa de casco de uma nave fabricada e acrescenta pontos de casco. Não é o Hull Plating **Booster** da página [Boosters](/wiki/06-Items/Boosters.md), que é um bônus temporário.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## As três blindagens {#the-three-platings}

| Item | Casco que acrescenta | De onde vem |
| :--- | ---: | :--- |
| **Hull Plating I** | 5.000 | Loja, 5.000 Thulium |
| **Hull Plating II** | 10.000 | Montagem, a partir de uma Hull Plating I |
| **Hull Plating III** | 15.000 | Montagem, a partir de uma Hull Plating II |

A Hull Plating I é comprada. **A II e a III são melhorias**: a Montagem consome uma blindagem do nível abaixo (solta no seu inventário) e pede Thulium, materiais e **Dark Matter Plates**, 5 para a II e 8 para a III, enquanto o último nível de qualquer outra peça de equipamento pede 3. Cada uma precisa antes da sua tecnologia, na árvore da Hull Plating da página [Pesquisa](/wiki/03-Mechanics/Research.md#tree-hull-plating): 1 dia e 25 Dark Matter para a II, 2 dias e 40 para a III, além da tecnologia da própria Dark Matter Plate. A árvore acima traz os preços, os materiais e os tempos.

A [Forja](/wiki/06-Items/Forge.md) aceita todas as blindagens, e uma melhoria mantém o grau de forja da blindagem que consumiu e sorteia o bônus de novo. Uma blindagem tem um único atributo, o casco, então leva um único bônus, de +2% a +15% conforme o grau: uma Hull Plating III Eterna soma até 17.250. O [Leilão](/wiki/03-Mechanics/Auction.md) lista a Hull Plating II e a III, nunca a Hull Plating I, que a Loja vende.

## Slots de blindagem {#hull-plate-slots}

A blindagem de casco só entra em **slots de blindagem**, um tipo de slot próprio que as quatro naves que você fabrica na Montagem têm além dos slots de laser, gerador, extra, habilidade e drone:

| Nave | Slots de blindagem | Um conjunto completo de Hull Plating III soma |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75.000 |
| **Storm** | 7 | 105.000 |
| **Ironclad** | 15 | 225.000 |
| **Wraith** | 9 | 135.000 |

- **Todos bloqueados no início.** Um slot abre quando você o pesquisa no Skylab: uma tecnologia para cada slot, 1 hora e 10 Dark Matter, em ordem a partir do primeiro. A tela de [Pesquisa](/wiki/03-Mechanics/Research.md#ship-technologies) mostra os slots de uma nave como um único cartão com um ponto para cada um.
- **Um tipo de nave, não uma nave só.** Os slots que você abriu para a Paragon estão abertos também em todos os designs da Paragon ([Designs de naves](/wiki/03-Mechanics/Ship-Designs.md)). Uma tecnologia é sua para sempre: o reset a mantém.
- **As duas configurações os compartilham.** As blindagens pertencem à nave: trocar de configuração as deixa no lugar, e o hangar mostra as mesmas nas duas.
- **Qualquer mistura.** Um slot aceita qualquer blindagem de casco, e duas iguais não são problema.
- **A sua proporção de casco continua.** Encaixar ou tirar uma blindagem mantém a proporção de casco que você tem, então uma blindagem nunca cura você nem machuca você.
- **Como todo equipamento**, as blindagens são encaixadas e tiradas no hangar, ou na janela dele a partir de uma zona segura, nunca em campo. Um slot que você não pesquisou recusa a blindagem.

No hangar, o cartão **Blindagem de casco** mostra os slots. Em um slot aberto você coloca uma blindagem arrastando e soltando, como em qualquer slot; um bloqueado mostra um cadeado, e um clique abre a pesquisa do Skylab. Um bloco ao lado dos outros atributos soma o que as blindagens encaixadas dão.

## Como o casco se soma {#how-the-hull-adds-up}

Uma blindagem soma o seu casco ao da própria nave, e o hangar e a janela da nave mostram o número maior. O casco da nave mais as suas blindagens passa então pelos multiplicadores de sempre: um [Hull Plating Booster](/wiki/06-Items/Boosters.md) e a [formação de drones](/wiki/03-Mechanics/Formations.md) que você usa. Um design que muda o casco (o BUCKY tem 25% a mais) muda o casco da própria nave, e as blindagens se somam por cima.

## Hull Plating ou Hull Plating Booster? {#hull-plating-or-booster}

Duas coisas dividem o nome. A **blindagem de casco** (esta página) é uma armadura: uma placa que fica em um slot de blindagem de uma nave fabricada e soma o seu casco enquanto estiver encaixada. O **Hull Plating Booster** é um bônus com prazo da página [Boosters](/wiki/06-Items/Boosters.md), +10% de pontos de casco máximos por 10 horas na nave que você pilota, e não há nada para encaixar. Eles se somam: as blindagens vêm primeiro, e os 10% do Booster são tirados do total.
