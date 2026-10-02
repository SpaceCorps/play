<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Clan -->
# Clan {#clans}

Fondare un clan o entrare in uno ti permette di mettere in comune le risorse, far salire di livello la banca condivisa, fissare le aliquote fiscali, coordinarti con i membri della fazione e gestire la diplomazia.

## Progressione del clan {#clan-progression}

I clan iniziano al livello 1 e possono essere potenziati fino al livello 5. Potenziare il clan richiede crediti pagati dalla **banca del clan**. I potenziamenti aumentano la capacità di membri e i limiti giornalieri dei pagamenti.

| Livello del clan | Limite di membri | Limite giornaliero di pagamenti (per membro) | Costo di potenziamento (crediti) |
| :---: | :---: | :---: | :--- |
| **Livello 1** | 10 | 1.000.000 Cr | — |
| **Livello 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Livello 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Livello 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Livello 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Economia e tassazione del clan {#clan-economy-taxation}

I clan funzionano con un sistema finanziario basato sulle tasse:

### 1. Tassazione giornaliera {#1-daily-taxation}

- **Aliquota**: il Leader o i Co-leader possono fissare un’aliquota fiscale giornaliera tra lo **0% e il 5%**.
- **Prelievo automatico**: una volta al giorno (UTC), il server preleva automaticamente le tasse da tutti i membri del clan.
- **Formula**: la tassa è calcolata come `ClanTaxRate` del saldo attuale di crediti di ciascun membro.
  - *Esempio*: se hai 10.000.000 crediti e la tassa del clan è del 2%, 200.000 crediti verranno detratti dal tuo account e versati nella banca del clan.
  - Si possono fare anche donazioni volontarie di crediti, fino al limite indicato nella sezione successiva.

### 2. Donazioni {#2-donations}

- **Donare**: qualsiasi membro può inviare crediti alla banca del clan dalla pagina Clan. Il pannello mostra quanto puoi ancora inviare.
- **Limite di donazioni**: un pilota può inviare al massimo **1.000.000 crediti ai clan in qualsiasi periodo di 24 ore**, contando tutti i clan in cui è stato. Lasciare un clan ed entrare in un altro non azzera il limite.
- **Nessun azzeramento giornaliero**: le 24 ore scorrono. Ogni donazione smette di contare esattamente 24 ore dopo essere stata fatta, e il pannello ti dice quando succede per la più vecchia e quanto torna disponibile. Una donazione superiore a ciò che resta viene rifiutata per intero.
- La tassa giornaliera non è una donazione e non consuma il tuo limite.

### 3. Pagamenti dalla banca {#3-bank-payouts}

- **Limiti dei pagamenti**: i leader e gli ufficiali del clan possono distribuire crediti dalla banca del clan ai singoli membri.
- **Limite giornaliero**: un membro non può ricevere più di `1,000,000 * ClanLevel` crediti in pagamenti in un singolo giorno di calendario (UTC).

---

## Gerarchia e ruoli {#hierarchy-roles}

I clan usano una struttura di gradi basata sui ruoli per gestire i permessi:

- **Leader (ruolo 3)**: ha accesso amministrativo completo, compresi potenziamento, tasse, diplomazia, promozioni, espulsioni e scioglimento del clan.
- **Co-leader (ruolo 2)**: può fissare le aliquote fiscali, pagare crediti, gestire la diplomazia e promuovere o retrocedere i gradi inferiori.
- **Veterano (ruolo 1)**: membro di fiducia che può accettare le nuove richieste di ingresso nel clan.
- **Membro (ruolo 0)**: giocatore standard senza permessi amministrativi.

### Tabella dei permessi {#permissions-table}

| Azione | Leader | Co-leader | Veterano | Membro |
| :--- | :---: | :---: | :---: | :---: |
| **Sciogliere il clan** | ✅ | ❌ | ❌ | ❌ |
| **Potenziare il clan** | ✅ | ❌ | ❌ | ❌ |
| **Fissare l’aliquota** | ✅ | ✅ | ❌ | ❌ |
| **Pagare crediti** | ✅ | ✅ | ❌ | ❌ |
| **Gestire la diplomazia** | ✅ | ✅ | ❌ | ❌ |
| **Promuovere / espellere** | ✅ | ✅* | ❌ | ❌ |
| **Accettare le richieste** | ✅ | ✅ | ✅ | ❌ |

*\*I Co-leader possono promuovere, retrocedere o espellere solo membri di grado inferiore al proprio.*

### Quando il Leader se ne va {#when-the-leader-leaves}

Un Leader non può lasciare un clan che ha ancora altri membri: prima promuovi un Co-leader a Leader (il Leader passa a Co-leader), oppure esci per ultimo, cosa che scioglie il clan. Se il Leader elimina il proprio account (Impostazioni › Account), la guida passa al membro di grado più alto, a parità a quello con più anzianità nel clan; un Leader rimasto solo nel clan lo scioglie, banca compresa.

---

## Diplomazia {#diplomacy}

I clan possono stabilire relazioni diplomatiche formali con altre organizzazioni inserendo il tag del clan bersaglio:

- **Alleanza**: clan alleati in modo formale. Lo stato di amicizia viene mostrato sulla mappa.
- **Patto di non aggressione (NAP)**: ci si accorda per non avviare ostilità.
- **Guerra**: dichiarazione formale di guerra. I bersagli di guerra possono essere attaccati ovunque senza penalità.

---

## Portare un amico {#bringing-a-friend}

Un amico nuovo del gioco può entrare con il tuo codice invito personale e riceve un pacchetto iniziale; vedi [Invita amici](/wiki/03-Mechanics/Invite-Friends.md). Una volta nel gioco può candidarsi al tuo clan come qualsiasi pilota.
