<!-- wiki-i18n source: 815a7ed973fd7e50 -->
<!-- wiki-i18n title: Escudos -->
# Mecânica dos escudos {#shield-mechanics}

Os escudos absorvem a maior parte do dano recebido e protegem o casco da sua nave do dano direto.

## Cálculos do escudo {#shield-calculations}

Os parâmetros finais de escudo da sua nave são calculados assim:

\[\text{Capacidade final do escudo} = \text{Capacidade base total} \times (1,0 + \text{Percentual total de bônus de escudo})\]
\[\text{Taxa final de recarga do escudo} = \text{Recarga base total} \times (1,0 + \text{Percentual total de bônus de escudo})\]

### 1. Eficiência do slot e retornos decrescentes {#1-slot-efficiency-diminishing-returns}

Assim como os motores, os escudos equipados (e os geradores híbridos) são ordenados por capacidade e sujeitos à eficiência do slot (núcleo: 100%, suporte: 75%, auxiliar: 50%, o slot de um drone: 100%, como um slot de núcleo) e a uma curva de retornos decrescentes conforme a posição deles. Um escudo em um dos seus [drones](/wiki/03-Mechanics/Drones.md) é ordenado junto com os da própria nave:

- **1º ao 4º escudo**: eficiência marginal de **100%** (1,0).
- **5º escudo**: eficiência marginal de **85%** (0,85).
- **6º escudo**: eficiência marginal de **70%** (0,70).
- **7º escudo**: eficiência marginal de **55%** (0,55).
- **8º em diante**: eficiência marginal de **50%** (0,50). (Até a versão 0.4.7 eram 25%, como nos motores; os motores continuam em 25%, veja [Velocidade](/wiki/03-Mechanics/Speed.md).)

**O hangar mostra.** Um escudo, motor ou núcleo adaptativo que não conta com toda a sua força leva uma pequena porcentagem no slot (por exemplo, `64%`: o 5º escudo, a 85%, em um slot de suporte, a 75%), e passar o cursor por cima mostra o detalhamento. Passe o cursor pelos blocos Escudos e Velocidade das estatísticas de combate para ver seus itens por posição e quanto contaria mais um. A janela Nave em voo mostra as mesmas listas quando você passa o cursor pela barra de escudo e pela velocidade.

### 2. Absorção do escudo (divisão do dano) {#2-shield-absorbance-damage-split-}

A absorção é a parte de cada impacto que os seus escudos recebem; o resto vai direto para os pontos de vida (HP).
- **Por escudo**: a absorção de um escudo mais a das células de escudo encaixadas nele. Um escudo sozinho tem **45 a 50%** (Light 45%, Basic 48%, Heavy 50%); as células somam de 2 a 10 pontos cada (Capacity Shield Cell I a IV +2%, +3%, +4%, +5%; Absorption Shield Cell I a IV +4%, +6%, +8%, +10%).
- **Absorção média**: a absorção da sua nave é a média simples dos escudos nos slots de núcleo, suporte e auxiliares e nos seus drones. Os núcleos adaptativos não têm absorção própria e não entram na média (as células em um núcleo adaptativo somam só capacidade e recarga). Sem nenhum escudo equipado, a sua absorção é 0%: o casco recebe todos os impactos, e os pontos de escudo das células em um núcleo adaptativo ficam sem uso, então equipe também um escudo.
- **O máximo de fábrica é 80%**: o melhor escudo com as melhores células, um Heavy Shield Core com três Absorption Shield Cell IV em cada slot. Misturar escudos mais fracos reduz a média. Nenhum bônus da Loja de PR nem da Forja entra nesse número.
- **Exemplo**: um Basic Shield Core (48%) com duas Absorption Shield Cell I dá 56%; somando um Light Shield Core (45%), a média é 50,5%.
- **O atributo não tem teto de 100%.** É o que os escudos receberiam de um impacto, antes de descontar a *penetração de escudo* de quem ataca, então uma nave pode ter mais do que um impacto inteiro: 112% ainda recebe um impacto inteiro de um atacante com até 12% de penetração.

#### Penetração de escudo {#shield-penetration}

Alguns ataques têm uma **penetração de escudo**: pontos que são descontados da sua absorção naquele impacto. A parte que os seus escudos recebem é

\[\text{Parte do escudo} = \text{limitar}(\text{Absorção} - \text{Penetração},\ 0,\ 100\%)\]

- Os escudos recebem no máximo `round(damage x share)` do impacto; o casco recebe o resto. Um escudo baixo demais para a sua parte passa a diferença para os HP, e se os escudos estão em 0, todo o dano atinge os HP diretamente.
- **De onde vem a penetração**: a *Penetração de escudo* de um foguete de alvo único (Lancet I 10%, Lancet II 25%, Lancet III 35%, Rivet I 5%, Rivet II 25%, Rivet III 35%, N.I.K.E. 35%; as explosões em área não têm, veja [Foguetes](/wiki/06-Items/Rockets.md)) e a da munição de laser (Ultra Core 5%, Experimental Fusion Core 10%; veja [Lasers e munição](/wiki/06-Items/Lasers.md)). Os alienígenas não têm, e a munição x1 e x2 também não.
- **Exemplos**: 80% de absorção contra um Lancet III (35%): os escudos recebem 45% do impacto, o casco 55%. 100% contra ele: 65% e 35%. 112% contra 12% de penetração: o impacto inteiro. 45% (um Light Shield Core sozinho) contra 35%: 10% no escudo, o resto no casco. Nenhum foguete penetra completamente um Light Shield Core.
- Os alienígenas não têm atributo de absorção: eles dividem cada impacto em 80% / 20%, menos a penetração do impacto.
- O dano de uma Siphon Battery sai só do escudo: a absorção e a penetração não entram na conta.

#### Chegar a 100% e passar dele {#reaching-and-passing-100-}

- **De fábrica**: no máximo 80% (acima).
- **Shield Absorbance Boost**: um bônus permanente da Loja de PR, comprado com pontos de reset, de **+0,1 ponto por nível, no máximo +10 pontos** (100 níveis, 25 PR cada). Ele soma pontos fixos à absorção da sua nave, igual em qualquer nave com escudo: 80% viram 80,4% com 4 níveis (100 PR), e os 45% de um Light Shield Core viram 46,2% com 12 níveis (300 PR). Uma nave sem escudo equipado continua em 0%. Os 100 níveis custam 2.500 PR, uma meta para vários resets: as fontes atuais de pontos de reset (os marcos de abates e as missões) pagam 855 PR no total, no limite, acumulados entre os resets, e isso compra 34 níveis, +3,4 pontos. Mais fontes de pontos de reset estão planejadas. Veja [Temporada e pontos de reset](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Forja**: escudos e células de escudo podem sortear um bônus de **Absorção**, que multiplica o atributo: +5% em um escudo de 50% são +2,5 pontos. Um conjunto Eterno do melhor tipo, totalmente forjado (núcleo e três células, todos os bônus sorteados no máximo, +15%), soma até 12 pontos, cerca de 10 em média (veja [A Forja](/wiki/06-Items/Forge.md)).
- **Juntos**: 80% de fábrica, +3,4 pontos de bônus (todos os 855 pontos de reset de hoje) e até +12 pontos de bônus da Forja chegam a **95,4%** no máximo hoje; com todos os 100 níveis do bônus (+10 pontos, 2.500 PR) seriam 102%. Nem o bônus nem a Forja sozinhos chegam a 100%; chegar lá é uma meta para vários resets, e mais fontes de pontos de reset estão planejadas.

### Bônus de escudo: capacidade, absorção, recarga {#shield-boosts-capacity-absorbance-recharge}

Todo bônus de escudo aumenta um dos três atributos e aparece na janela Boosters sob a sua própria categoria:

- **Capacidade** (pontos de escudo máximos): os boosters Shield Wall e o Shield Capacity Boost permanente.
- **Absorção** (a parte de um impacto que os seus escudos recebem): o Shield Absorbance Boost permanente (+0,1 ponto por nível, no máximo +10 pontos).
- **Recarga** (pontos de escudo restaurados por segundo): o booster Shield Regen.

Veja [Boosters](/wiki/06-Items/Boosters.md) para os números.

---

## Regeneração passiva do escudo {#shield-passive-regeneration}

Os escudos se regeneram passivamente com o tempo para manter você pronto para o combate.

- **Pulso de regeneração**: se os escudos estão abaixo da capacidade máxima, eles restauram pontos de escudo iguais à sua taxa de recarga por segundo.
- **Interrupção por combate (atraso de 15 s)**: a regeneração para quando você sofre dano e só volta depois de **15 segundos** sem receber dano.
