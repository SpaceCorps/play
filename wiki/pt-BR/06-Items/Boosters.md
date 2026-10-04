<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: Boosters -->
# Boosters {#boosters}

Os boosters dão modificações temporárias de atributos para reforçar o combate, a defesa, a evolução de nível e a coleta de recursos da sua nave.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Experience Kit | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Beacon | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall -> Shield Wall II
Hull Plating -> Hull Plating II
Damage Amp -> Damage Amp II
```
<!-- item-tree:end -->

## Regras de empilhamento {#stacking-rules}

Os boosters usam um sistema de escala aditiva:
1. **Os percentuais de bônus se somam**: se você comprar dois boosters diferentes que dão +10% de dano de laser cada um, receberá um bônus total de **+20% de dano de laser**.
2. **As durações se empilham de forma multiplicativa**: comprar o _mesmo_ booster várias vezes prolonga a duração dele. Os temporizadores de boosters _diferentes_ correm em paralelo.
3. **Visualização dos temporizadores**: os boosters ativos aparecem no HUD, na janela Boosters, que mostra o total dos bônus ativos agrupados e o próximo evento de expiração.

---

## Boosters ativos {#active-boosters}

Todo booster dura **10 horas** de base e é ativado assim que você o compra, o recebe ou o recolhe. Os três boosters **II** não são vendidos: você pesquisa a tecnologia deles no Skylab ([Pesquisa](/wiki/03-Mechanics/Research.md)) e depois os cria na Montagem, e, ao recolher um, as 10 horas dele começam na hora, como ao comprá-lo.

| Nome | Raridade | Efeito base (10 horas) | Preço (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Raro | +10% de dano de laser | 20.000 |
| **Damage Amp II** | Raro | +10% de dano de laser | Montagem: 20.000 |
| **Shield Wall** | Raro | +25% de capacidade do escudo (máximo de pontos de escudo) | 15.000 |
| **Shield Wall II** | Raro | +25% de capacidade do escudo (máximo de pontos de escudo) | Montagem: 15.000 |
| **Hull Plating** | Raro | +10% de pontos de vida máximos | 15.000 |
| **Hull Plating II** | Raro | +10% de pontos de vida máximos | Montagem: 15.000 |
| **Shield Regen** | Raro | +25% de taxa de recarga do escudo (pontos de escudo restaurados por segundo) | 10.000 |
| **Experience Kit** | Comum | +20% de ganho de experiência | 8.000 |
| **Honor Beacon** | Comum | +20% de ganho de pontos de honra | 10.000 |
| **Resource Magnet** | Raro | +25% de rendimento das caixas de carga | 18.000 |
| **Loot Luck** | Lendário | +5% de chance de drop raro de NPCs | 30.000 |

---

## Bônus de escudo: três tipos {#shield-boosts-three-kinds}

Os escudos têm três atributos separados, e cada bônus de escudo aumenta exatamente um deles. A janela Boosters os mantém separados, com um ícone e um total para cada um:

| Tipo | O que é | Bônus que o aumentam |
| :--- | :--- | :--- |
| **Capacidade do escudo** | Seus pontos de escudo máximos | Shield Wall, Shield Wall II, o **Shield Capacity Boost** permanente (Loja de PR) |
| **Absorção do escudo** | A parte de cada impacto que seus escudos recebem (o resto atinge o casco); pode passar de 100% | O **Shield Absorbance Boost** permanente (Loja de PR): +0,1 ponto por nível, a 25 PR cada, no máximo +10 pontos. Nenhum booster a aumenta |
| **Recarga do escudo** | Pontos de escudo restaurados por segundo | Shield Regen. Nenhum bônus permanente a aumenta |

Os bônus de um tipo se somam; eles nunca contam para outro tipo. Os bônus permanentes estão descritos em [Progressão entre temporadas](/wiki/03-Mechanics/Wipe-Timeline.md); os atributos em si, em [Mecânica dos escudos](/wiki/03-Mechanics/Shields.md).
