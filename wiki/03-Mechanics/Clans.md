# Clans

Forming or joining a Clan allows you to pool resources, level up shared banking, set taxation rates, coordinate with faction members, and manage diplomacy.

## Clan Progression

Clans start at Level 1 and can upgrade to Level 5. Upgrading the clan requires Credits to be paid from the **Clan Bank**. Upgrades increase member capacity and daily payout limits.

| Clan Level | Member Limit | Daily Payout Limit (Per Member) | Upgrade Cost (Credits) |
| :---: | :---: | :---: | :--- |
| **Level 1** | 10 | 1,000,000 Cr | — |
| **Level 2** | 25 | 2,000,000 Cr | 10,000,000 Cr |
| **Level 3** | 50 | 3,000,000 Cr | 100,000,000 Cr |
| **Level 4** | 75 | 4,000,000 Cr | 1,000,000,000 Cr |
| **Level 5** | 100 | 5,000,000 Cr | 10,000,000,000 Cr |

---

## Clan Economy & Taxation

Clans operate on a tax-based financial system:

### 1. Daily Taxation

- **Tax Rate**: The Leader or Co-Leaders can set a daily tax rate between **0% and 5%**.
- **Automated Collection**: Once per day (UTC), the server automatically collects taxes from all clan members.
- **Formula**: The tax is calculated as `ClanTaxRate` of each member's current Credit balance.
  - *Example*: If you have 10,000,000 Credits and the clan tax is 2%, 200,000 Credits will be deducted from your account and deposited into the Clan Bank.
  - Voluntary credit donations can also be made, up to the cap in the next section.

### 2. Donations

- **Donating**: any member can send Credits into the Clan Bank from the Clan page. The sheet shows what you can still send.
- **Donation Cap**: a pilot can send at most **1,000,000 Credits into clans in any 24 hours**, counted over every clan the pilot has been in. Leaving a clan and joining another does not give a new allowance.
- **No daily reset**: the 24 hours slide. Each donation stops counting exactly 24 hours after it was made, and the sheet tells you when the oldest one does and how much comes back. A donation over what is left is refused whole.
- The daily tax is not a donation and does not use up your allowance.

### 3. Bank Payouts

- **Payout Limits**: Clan leaders and officers can distribute credits from the Clan Bank to individual members.
- **Daily Cap**: A member cannot receive more than `1,000,000 * ClanLevel` Credits in payouts in a single calendar day (UTC).

---

## Hierarchy & Roles

Clans utilize a role-based rank structure to manage permissions:

- **Leader (Role 3)**: Has complete administrative access, including upgrading, sets taxes, diplomacy, promotions, kicking, and disbanding the clan.
- **Co-Leader (Role 2)**: Can set tax rates, payout credits, manage diplomacy, and promote/demote lower ranks.
- **Elder (Role 1)**: Trusted member who can accept new applications to the clan.
- **Member (Role 0)**: Standard player with no administrative permissions.

### Permissions Table

| Action | Leader | Co-Leader | Elder | Member |
| :--- | :---: | :---: | :---: | :---: |
| **Disband Clan** | ✅ | ❌ | ❌ | ❌ |
| **Upgrade Clan** | ✅ | ❌ | ❌ | ❌ |
| **Set Tax Rate** | ✅ | ✅ | ❌ | ❌ |
| **Payout Credits** | ✅ | ✅ | ❌ | ❌ |
| **Manage Diplomacy** | ✅ | ✅ | ❌ | ❌ |
| **Promote / Kick** | ✅ | ✅* | ❌ | ❌ |
| **Accept Applications** | ✅ | ✅ | ✅ | ❌ |

*\*Co-Leaders can only promote, demote, or kick members of a lower rank than themselves.*

### When the Leader Leaves

A Leader can't leave a clan that still has other members: promote a Co-Leader to Leader first (the Leader steps down to Co-Leader), or leave last, which disbands the clan. If the Leader deletes their account (Settings › Account), the lead passes to the highest-ranking member, the longest-serving on a tie; a Leader alone in the clan disbands it, bank included.

---

## Diplomacy

Clans can establish formal diplomatic relations with other organizations by entering the target clan's Tag:

- **Alliance**: Formally allied clans. Friendly status is displayed on the map.
- **NAP (Non-Aggression Pact)**: Agree not to engage in hostilities.
- **War**: Formal declaration of war. War targets can be engaged anywhere without penalty.

---

## Bringing a Friend

A friend who is new to the game can join with your personal invite code and gets a starter pack; see [Invite Friends](/wiki/03-Mechanics/Invite-Friends.md). Once in the game they can apply to your clan like any pilot.
