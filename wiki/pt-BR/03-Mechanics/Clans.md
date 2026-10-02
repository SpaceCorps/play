<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Clãs -->
# Clãs {#clans}

Fundar um clã ou entrar em um permite reunir recursos, melhorar o banco compartilhado, definir taxas de imposto, coordenar-se com os membros da corporação e gerenciar a diplomacia.

## Progressão do clã {#clan-progression}

Os clãs começam no nível 1 e podem ser melhorados até o nível 5. Melhorar o clã exige créditos pagos com o **Banco do clã**. As melhorias aumentam a capacidade de membros e os limites diários de pagamento.

| Nível do clã | Limite de membros | Limite diário de pagamentos (por membro) | Custo da melhoria (créditos) |
| :---: | :---: | :---: | :--- |
| **Nível 1** | 10 | 1.000.000 Cr | — |
| **Nível 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Nível 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Nível 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Nível 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Economia e impostos do clã {#clan-economy-taxation}

Os clãs funcionam com um sistema financeiro baseado em impostos:

### 1. Imposto diário {#1-daily-taxation}

- **Taxa de imposto**: o Líder ou os Vice-líderes podem definir uma taxa de imposto diária entre **0% e 5%**.
- **Cobrança automática**: uma vez por dia (UTC), o servidor cobra automaticamente o imposto de todos os membros do clã.
- **Fórmula**: o imposto é calculado como `ClanTaxRate` do saldo de créditos atual de cada membro.
  - *Exemplo*: se você tem 10.000.000 de créditos e o imposto do clã é 2%, 200.000 créditos serão descontados da sua conta e depositados no Banco do clã.
  - Também é possível fazer doações voluntárias de créditos, até o limite descrito na próxima seção.

### 2. Doações {#2-donations}

- **Doar**: qualquer membro pode enviar créditos ao Banco do clã pela página Clã. A janela mostra quanto você ainda pode enviar.
- **Limite de doações**: um piloto pode enviar no máximo **1.000.000 de créditos a clãs em qualquer período de 24 horas**, somando todos os clãs em que o piloto já esteve. Sair de um clã e entrar em outro não dá um novo limite.
- **Sem reinício diário**: as 24 horas são deslizantes. Cada doação deixa de contar exatamente 24 horas depois de feita, e a janela informa quando a mais antiga deixa de contar e quanto volta a ficar disponível. Uma doação acima do que resta é recusada por inteiro.
- O imposto diário não é uma doação e não consome o seu limite.

### 3. Pagamentos do banco {#3-bank-payouts}

- **Limites de pagamento**: os líderes e oficiais do clã podem distribuir créditos do Banco do clã a membros individuais.
- **Limite diário**: um membro não pode receber mais de `1,000,000 * ClanLevel` créditos em pagamentos em um único dia civil (UTC).

---

## Hierarquia e funções {#hierarchy-roles}

Os clãs usam uma estrutura de patentes baseada em funções para gerenciar as permissões:

- **Líder (função 3)**: tem acesso administrativo completo, incluindo melhorar o clã, definir impostos, diplomacia, promoções, expulsões e dissolver o clã.
- **Vice-líder (função 2)**: pode definir taxas de imposto, pagar créditos, gerenciar a diplomacia e promover ou rebaixar patentes inferiores.
- **Ancião (função 1)**: membro de confiança que pode aceitar novas candidaturas ao clã.
- **Membro (função 0)**: jogador comum, sem permissões administrativas.

### Tabela de permissões {#permissions-table}

| Ação | Líder | Vice-líder | Ancião | Membro |
| :--- | :---: | :---: | :---: | :---: |
| **Dissolver o clã** | ✅ | ❌ | ❌ | ❌ |
| **Melhorar o clã** | ✅ | ❌ | ❌ | ❌ |
| **Definir a taxa de imposto** | ✅ | ✅ | ❌ | ❌ |
| **Pagar créditos** | ✅ | ✅ | ❌ | ❌ |
| **Gerenciar a diplomacia** | ✅ | ✅ | ❌ | ❌ |
| **Promover / Expulsar** | ✅ | ✅* | ❌ | ❌ |
| **Aceitar candidaturas** | ✅ | ✅ | ✅ | ❌ |

*\*Os Vice-líderes só podem promover, rebaixar ou expulsar membros de patente inferior à sua.*

### Quando o Líder sai {#when-the-leader-leaves}

Um Líder não pode sair de um clã que ainda tem outros membros: primeiro promova um Vice-líder a Líder (o Líder passa a Vice-líder) ou saia por último, o que dissolve o clã. Se o Líder excluir a conta (Configurações › Conta), a liderança passa ao membro de patente mais alta e, em caso de empate, ao mais antigo no clã; um Líder sozinho no clã o dissolve, junto com o banco.

---

## Diplomacia {#diplomacy}

Os clãs podem estabelecer relações diplomáticas formais com outras organizações informando a tag do clã-alvo:

- **Aliança**: clãs formalmente aliados. O status amistoso aparece no mapa.
- **NAP (Pacto de não agressão)**: acordo para não entrar em hostilidades.
- **Guerra**: declaração formal de guerra. Alvos de guerra podem ser atacados em qualquer lugar, sem penalidade.

---

## Convidando um amigo {#bringing-a-friend}

Um amigo que é novo no jogo pode entrar com o seu código de convite pessoal e recebe um pacote inicial; veja [Convidar amigos](/wiki/03-Mechanics/Invite-Friends.md). Já dentro do jogo, ele pode se candidatar ao seu clã como qualquer piloto.
