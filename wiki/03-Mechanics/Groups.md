# Groups

A group is up to **5 pilots** who fly together, of any companies: friends who fly for different companies, even enemies in the PvP sectors, can be one group. Members see each other's ship, hull and shield, share the rewards of the aliens they destroy and get each other's kills counted for their missions. There is a chat channel for the group too.

## Forming a Group

- **Invite** a pilot three ways: select them and press **Invite to group** in the Target window, right-click their name in the chat and choose **Invite to group**, or press **+** in the Group window's title bar for a list of the pilots on your map (an enemy's name is amber in it). You can invite a pilot of any company. If it is another company's, their prompt names your company, marks it **Enemy** and warns what accepting means (they see your ship on every map, cloaked or not, and you cannot attack each other), so nobody joins by mistake, and you can ask at most **3 pilots of other companies a minute**. A pilot of another company who leaves your group cannot be invited by you again for **a minute**.
- The pilot sees a card with **Accept** and **Deny**, counting the **60 seconds** they have to answer, and a notice. **Y** accepts and **Escape** denies (a text field in use, or a window open on top, keeps the keys). If several invitations wait, the card takes them in turn. It shows at the station too. When the time is out the invitation lapses and you are told which. You cannot invite a pilot who is in a group already, who has set **Do Not Disturb**, or who has too many invitations waiting, and you can send at most 10 invitations a minute (3 to other companies).
- **Do Not Disturb** turns invitations off: the bell in the Group window's title bar, or Settings › General › Groups. Nobody can invite you while it is on, and you are not asked.
- Whoever's invitation is accepted first becomes the **leader**. The leader invites, removes members and makes another member the leader. Anyone can leave. A group of one pilot ends by itself. When the leader leaves, the member who has been in the group the longest leads.
- You are in **one group at a time**. Changing your company does not take you out of your group (you show under your new company); the season's wipe does.
- If your connection drops, or you dock and launch again, your place is kept for **2 minutes**. A member away longer than that is removed. A server update ends every group: invite each other again.

## Seeing Your Group

Once you accept, the **Group window** opens (the **B** key or its button in the toolbar shows and hides it; rebind the key in Settings › Controls). Each member has a row: their ship, their name and level, and a **hull bar** and a **shield bar** (hover for the numbers). A member on your map shows how far away they are and in which direction, as the minimap draws it (up is the top of the map); one on another map shows that map's name, with the world when it is another world. A **crown** marks the leader, a **ghost** a member who is cloaked (a group shares its cloaked ships, whatever the companies), a **shield** one in a safe zone. A member who has docked, was destroyed or lost their connection is dimmed and says so. Click a row to select that ship when it is on your map (you cannot fire on a groupmate: the game holds fire).
- The **leader** right-clicks a row to **Make leader** or **Remove from group**. Anyone right-clicks their own row, or uses the menu, to **Leave group**.
- The minimise button folds the window to one small pair of bars for each member; its place, size and folded state are remembered.
- Members **see each other's cloaks** and cannot break them: an EMP that goes off near a cloaked groupmate leaves its cloak as it is.
- On the map the group's pilots are pink: a pink dot on the minimap, and a pink group mark, hull bar and shield bar over their ships in flight. Hover a dot for the name. Company mates outside the group stay green.
- Every member shows the **company** they fly for: its tag in the company's colour before the name ("[T] rex"), as everywhere in the game. A member of another company, an enemy outside the group, has its name in amber and says so in its card. Nobody outside your group sees any of this, and when you leave or are removed you see none of it any more, at once.

## Sharing Kills

When a member destroys an alien (or is paid for it by its [claim](/wiki/03-Mechanics/Combat.md)), the rewards (credits, Thulium, experience and honor) are shared among the members who are:

- on the **same map** (in the same world),
- **alive** and within **4,000 units** of the wreck, and
- **shooting**: they fired a laser or a rocket at anything within the last 15 seconds.

Each gets a part in proportion to their **level**, whatever their company (the credits and honor are each pilot's own; no company keeps any): a level 15 pilot with a level 5 mate takes 75% and the mate 25%. Every credit is handed out: the pilot who made the kill gets what is left when the parts are rounded down. The whole reward is the killer's own: their boosters, their world's multiplier and their premium apply, and a mate's do not. Alone, or with nobody else in reach, a kill pays what it always did. A pilot standing near the fight without firing gets no part.

The kill's notice says so: the killer's own **REWARDS** line shows their part, followed by "Rewards shared with 2 group mates: your part is 40%", and a mate who is paid a part reads "*Alien* was destroyed by *pilot*; your group's share pays you" with the amounts. The notices show in the Game Log and at the top of the screen.

What stays the killer's alone: the **cargo crate** (loot and resources), the kill in their statistics and ranking, the Wipe Point kill count and the drones' experience. Kills of other pilots are not shared.

## Sharing Missions

A kill also counts for the **kill missions** of every other member who is on the same map and **fired a laser or rocket at anything in the last 15 seconds**, wherever they are on it, as if they had destroyed the alien themselves. The mission's own rules still decide: the alien must be the mission's kind and the sector the mission names. A mate who did not shoot, or is on another map, gets no count. Missions keep their own company's rules: a mission that asks for a kill in "another company's sector 4" counts for the member for whom that sector is another company's. When a mate's kill counts for one of your missions, a notice tells you which.

## Chat Channels

The chat has a row of tabs on top: **Global**, **Local** and, while you are in a group, **Group**. The line you type goes to the tab in view, and the tab you last used is remembered. Each channel has its colour and a short tag on every line (GLB, LOC, GRP), a tab counts the lines you have not read, and the chat's button in the toolbar carries the count while the window is closed. The server's own lines show in every tab. Or start a line with a command:

| Channel | Who hears it | Command |
| :--- | :--- | :--- |
| **Local** | pilots on your map | `/l` or `/local` |
| **Global** | every pilot online | `/g` or `/global` |
| **Group** | your group, wherever they are | `/p`, `/party` or `/group` |

A command switches the tab too, and typed alone (`/g`) it only switches. Global has a limit: 3 lines in a burst, then one every 2 seconds. Group chat needs a group. On a game server from before the channels the chat is the one list it was, and a group cannot be formed.

### The Kill Feed

The **Global** tab also carries a kill feed: a muted line with a skull whenever a pilot is destroyed, worded with a little humour ("vega asked the black hole for directions"). It says who died and who or what did it: a pilot's lasers, a rocket (the **N.U.K.E.** and the **N.I.K.E.** have lines of their own), an alien by its name, the black hole's horizon or its radiation, or an enemy who pushed the pilot in. The names wear their company's tag and colour. It never says **where**: no map and no position, so a cloaked pilot's death gives nothing away. Only pilots get a line: an alien or a company pilot being destroyed does not, and a pilot who logs out in a fight is not destroyed, so there is no line for that either.

When many pilots die within seconds (a N.U.K.E. over a dogfight) you see the first few and then one line, "7 more pilots died". The feed has its own place in the scrollback, so a battle never pushes your friends' messages out.

Turn it off with the menu button in the chat window's title bar (**Show kill feed**) or in **Settings > General > Chat**. Off only hides the lines; they come back when you turn it on. The feed needs a game server from 0.4.5: on an older one the Global tab has none.

### Hiding, Ignoring and Reporting

Global reaches every pilot online, so the chat has three tools to keep it comfortable. They are in the chat window: the menu button in its title bar, and a right-click on a pilot's name.

- **Hide Global chat** (the menu, or Settings › General › Chat): the Global tab shows nothing, the kill feed's lines included, and stops counting unread lines. The tab stays, says "Global is hidden" and has a button that shows it again; what you send to Global still goes out. Turn it off and every line that came meanwhile is there.
- **Ignore** (right-click a name, then **Ignore**): that pilot's lines in Global and Local are hidden, and their group invitations are turned down without asking you. They are not told. They stay visible in the **Group** tab: a group mate you ignore is still your group, so leave the group to be rid of them. The server's own lines are never hidden. **Stop ignoring** is on the same menu, and **Settings › General › Chat** lists the ignored pilots (up to 200) with a **Remove** button for each.
- **Report** (right-click a name, then **Report…**): pick a reason (spam, abuse or harassment, cheating, or something else) and send. The report carries your name, the pilot's, the channel, the reason and the last line of that pilot that your chat shows (up to 200 characters). The game's admins read it; nobody is punished automatically, and the pilot is not told who reported them. You can send 5 reports an hour.

Your ignored list and the Hide Global switch are kept with your account, so they follow you to other computers. The game has no word filter and no automatic mutes: the tools above are yours to use.

## Rules of Engagement

**Members of one group cannot hurt each other**, whatever their companies: you cannot lock on to a groupmate (lasers or rockets), your shots and blasts pass through them, and nothing you do to one counts as a kill, a PvP kill or a black hole kill for anyone. Company mates who are **not** in the same group are as before: hitting one costs **100 Honor** when it is destroyed. Leave the group and a former mate, enemy or not, is fair game again at once (where the sector and the season allow fighting at all). Everyone outside your group is treated as ever, and safe zones, the Peace Protocol and the sectors' PvP rules do not change for anyone.

## Bringing a Friend

A friend who is new to the game can join with your personal code and gets a starter pack; see [Invite Friends](/wiki/03-Mechanics/Invite-Friends.md).
