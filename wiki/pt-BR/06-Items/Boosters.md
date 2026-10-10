<!-- wiki-i18n source: 6227a03e20405285 -->
<!-- wiki-i18n title: Boosters -->
# Boosters

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Os boosters dão modificações temporárias de atributos para reforçar o combate, a defesa, a evolução de nível e a coleta de recursos da sua nave.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árvore de itens {#item-tree}

O que a Montagem faz exige antes a sua tecnologia; passe o mouse sobre um item para ver quanto tempo leva para pesquisá-la. A árvore de tecnologias, o combustível e o boost: [Pesquisa](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster I | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster I -> Shield Wall Booster II
Hull Plating Booster I -> Hull Plating Booster II
Laser Damage Booster I -> Laser Damage Booster II
```
<!-- item-tree:end -->

## Regras de empilhamento {#stacking-rules}

Os boosters usam um sistema de escala aditiva:
1. **Os percentuais de bônus se somam**: se você comprar dois boosters diferentes que dão +10% de dano de laser cada um, receberá um bônus total de **+20% de dano de laser**.
2. **As durações se empilham de forma multiplicativa**: comprar o _mesmo_ booster várias vezes prolonga a duração dele. Os temporizadores de boosters _diferentes_ correm em paralelo.
3. **Visualização dos temporizadores**: os boosters ativos aparecem no HUD, na janela Boosters, que mostra o total dos bônus ativos agrupados e o próximo evento de expiração.
4. **Os números os contam**: o dano, os escudos, a recarga do escudo, a absorção, a velocidade e o casco do Hangar, e a sua página de piloto, incluem seus boosters ativos, os buffs da Loja de PR e os reforços do seu clã; uma pequena etiqueta *com boosters* no card de estatísticas de combate indica isso. Penetração, chance de crítico e alcance não mudam com os boosters.

---

## Boosters ativos {#active-boosters}

Todo booster dura **10 horas** de base e é ativado assim que você o compra, o recebe ou o recolhe. Os três boosters **de segundo nível** (Laser Damage Booster II, Shield Wall Booster II e Hull Plating Booster II) não são vendidos: você pesquisa a tecnologia deles no Skylab ([Pesquisa](/wiki/03-Mechanics/Research.md)) e depois os cria na Montagem, e, ao recolher um, as 10 horas dele começam na hora, como ao comprá-lo.

| Nome | Raridade | Efeito base (10 horas) | Preço (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster I** | Raro | +10% de dano de laser | 20.000 |
| **Laser Damage Booster II** | Raro | +10% de dano de laser | Montagem: 20.000 |
| **Shield Wall Booster I** | Raro | +25% de capacidade do escudo (máximo de pontos de escudo) | 15.000 |
| **Shield Wall Booster II** | Raro | +25% de capacidade do escudo (máximo de pontos de escudo) | Montagem: 15.000 |
| **Hull Plating Booster I** | Raro | +10% de pontos de vida máximos | 15.000 |
| **Hull Plating Booster II** | Raro | +10% de pontos de vida máximos | Montagem: 15.000 |
| **Shield Regen Booster** | Raro | +25% de taxa de recarga do escudo (pontos de escudo restaurados por segundo) | 10.000 |
| **Experience Booster** | Comum | +20% de ganho de experiência | 8.000 |
| **Honor Booster** | Comum | +20% de ganho de pontos de honra | 10.000 |
| **Resource Magnet Booster** | Raro | +25% de rendimento das caixas de carga | 18.000 |
| **Loot Luck Booster** | Lendário | +5% de chance de drop raro de NPCs | 30.000 |

> [!NOTE]
> **Booster ou amp?** São coisas diferentes. Todo booster tem **Booster** no nome, funciona com um prazo e não tem nada para encaixar: o **Laser Damage Booster I** e o **Laser Damage Booster II** dão +10% de dano de laser por 10 horas, da Loja ou da Montagem. O **Damage Amp**, o **Crit Amp** e o **Penetration Amp** (níveis I a IV) são amplificadores de laser: módulos que você encaixa no slot de amp de um laser, sem prazo ([Lasers e munição](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). Antes de 0.4.12 os boosters se chamavam Damage Amp e Damage Amp II, Shield Wall e Shield Wall II, Hull Plating e Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet e Loot Luck; os que você tinha em andamento continuaram com os novos nomes. O Hull Plating **Booster** não é a blindagem **Hull Plating** que se encaixa nos slots de blindagem de uma nave ([Blindagem de casco](/wiki/06-Items/Hull-Plating.md#hull-plating-or-booster)).

---

## Bônus de escudo: três tipos {#shield-boosts-three-kinds}

Os escudos têm três atributos separados, e cada bônus de escudo aumenta exatamente um deles. A janela Boosters os mantém separados, com um ícone e um total para cada um:

| Tipo | O que é | Bônus que o aumentam |
| :--- | :--- | :--- |
| **Capacidade do escudo** | Seus pontos de escudo máximos | Shield Wall Booster I, Shield Wall Booster II, o **Shield Capacity Boost** permanente (Loja de PR) |
| **Absorção do escudo** | A parte de cada impacto que seus escudos recebem (o resto atinge o casco); pode passar de 100% | O **Shield Absorbance Boost** permanente (Loja de PR): +0,1 ponto por nível, a 25 PR cada, no máximo +10 pontos. Nenhum booster a aumenta |
| **Recarga do escudo** | Pontos de escudo restaurados por segundo | Shield Regen Booster. Nenhum bônus permanente a aumenta |

Os bônus de um tipo se somam; eles nunca contam para outro tipo. Os bônus permanentes estão descritos em [Progressão entre temporadas](/wiki/03-Mechanics/Wipe-Timeline.md); os atributos em si, em [Mecânica dos escudos](/wiki/03-Mechanics/Shields.md).
