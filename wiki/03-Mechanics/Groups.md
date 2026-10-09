# Groups

A group is up to **5 pilots** who fly together, of any companies: friends who fly for different companies, even enemies in the PvP sectors, can be one group. Members see each other's ship, hull and shield, share the rewards of the aliens they destroy and get each other's kills counted for their missions. There is a chat channel for the group too.

![The Group window with five members: each row has the hull bar in green with the shield bar in blue beneath it, and two mates who are shooting show their target to the right of their bars](../img/wiki-img/shots/group-window.jpg)

## Forming a Group

- **Invite** a pilot four ways: select them and press **Invite to group** in the Target window, right-click their name in the chat and choose **Invite to group**, press **+** in the Group window's title bar for a list of the pilots on your map (an enemy's name is amber in it), or press **Invite** beside a name in the **Who is online** window (the **H** key), which lists the pilots of your whole world ([Clans](/wiki/03-Mechanics/Clans.md#who-is-online)). You can invite a pilot of any company. If it is another company's, their prompt names your company, marks it **Enemy** and warns what accepting means (they see your ship on every map, cloaked or not, and you cannot attack each other), so nobody joins by mistake, and you can ask at most **3 pilots of other companies a minute**. A pilot of another company who leaves your group cannot be invited by you again for **a minute**.
- The pilot sees a card with **Accept** and **Deny**, counting the **60 seconds** they have to answer, and a notice. **Y** accepts and **Escape** denies (a text field in use, or a window open on top, keeps the keys). If several invitations wait, the card takes them in turn. It shows at the station too. When the time is out the invitation lapses and you are told which. You cannot invite a pilot who is in a group already, who has set **Do Not Disturb**, or who has too many invitations waiting, and you can send at most 10 invitations a minute (3 to other companies).
- **Do Not Disturb** turns invitations off: the bell in the Group window's title bar, or Settings › General › Groups. Nobody can invite you while it is on, and you are not asked.
- Whoever's invitation is accepted first becomes the **leader**. The leader invites, removes members and makes another member the leader. Anyone can leave. A group of one pilot ends by itself. When the leader leaves, the member who has been in the group the longest leads.
- You are in **one group at a time**. [Changing your company](/wiki/01-General/Getting-Started.md#changing-your-company) does not take you out of your group (you show under your new company); the season's wipe does.
- If your connection drops, or you dock and launch again, your place is kept for **2 minutes**. A member away longer than that is removed. A server update ends every group: invite each other again.

## Seeing Your Group

Once you accept, the **Group window** opens (the **B** key or its button in the toolbar shows and hides it; rebind the key in Settings › Controls). Each member has a row: their ship, their name and level, and under them the **hull bar** (green) with the **shield bar** (blue) beneath it, each as wide as the row (hover for the numbers). A ship with no shield fitted shows the hull bar alone. A member on your map shows how far away they are and in which direction at the top right of the row, as the minimap draws it (up is the top of the map); one on another map shows that map's name there, with the world when it is another world. A **crown** marks the leader, a **ghost** a member who is cloaked (a group shares its cloaked ships, whatever the companies), a **shield** one in a safe zone. A member who has docked, was destroyed or lost their connection is dimmed and says so. Click a row to select that ship when it is on your map (you cannot fire on a groupmate: the game holds fire).
- A member who is **shooting** shows its **target** too, to the **right** of its bars: a small mark for what it is (a skull for an alien), the target's name and two thin bars, the target's **hull** and **shield** (hover for the numbers). The member's own bars give up some of their length for it, and the row keeps its height whether a mate has a target or not. You see the target and its hull and shield of every group mate who is shooting at an alien, another pilot or a company pilot. A laser lock or a guided rocket in flight counts, and the target stays for **5 seconds** after the last one. It is shown only for a mate who flies on your map (in your world), and only for a ship you could see there yourself: the hull and shield of a cloaked pilot are never shown to a mate who cannot see that pilot. A station or a gate is no target. Your own row shows no target (the Target window is that), nor does the folded window. If you drag the window narrower (it resizes from any side or corner), there is no room beside the bars any more: the target then goes **beneath** them and the row grows taller.
- The **leader** right-clicks a row to **Make leader** or **Remove from group**. Anyone right-clicks their own row, or uses the menu, to **Leave group**.
- The minimise button folds the window to one small pair of bars for each member; its place, size and folded state are remembered. A new layout opens it **280 points** wide, so a member's target beside the bars shows more of a long name; a window you have already moved or resized keeps the width you gave it.
- Members **see each other's cloaks** and cannot break them: an EMP that goes off near a cloaked groupmate leaves its cloak as it is.
- On the map the group's pilots are pink: a pink dot on the minimap, and a pink group mark, hull bar and shield bar over their ships in flight. Hover a dot for the name. Company mates outside the group stay green.
- Every member shows the **company** they fly for: its tag in the company's colour before the name ("[T] rex"), as everywhere in the game. A member of another company, an enemy outside the group, has its name in amber and says so in its card. Nobody outside your group sees any of this, and when you leave or are removed you see none of it any more, at once.

## Sharing Kills

When a member destroys an alien (or is paid for it by its [claim](/wiki/03-Mechanics/Combat.md)), the rewards (credits, Thulium, experience and honor) are shared among the members who are:

- on the **same map** (in the same world),
- **alive** and within **4,000 units** of the wreck, and
- **shooting**: they fired a laser or a rocket at anything within the last 15 seconds.

Each gets a part in proportion to their **level**, whatever their company (the credits and honor are each pilot's own; no company keeps any): a level 15 pilot with a level 5 mate takes 75% and the mate 25%. Every credit is handed out: the pilot who made the kill gets what is left when the parts are rounded down. The whole reward is the killer's own: their boosters, their world's multiplier and their premium apply, and a mate's do not. Alone, or with nobody else in reach, a kill pays what it always did. A pilot standing near the fight without firing gets no part.

The kill's notice says so: the killer's own **REWARDS** line shows their part, followed by "Rewards shared with 2 group mates: your part is 40%", and a mate who is paid a part reads "*Alien* was destroyed by *pilot*; your group's share pays you" with the amounts. The notices show in the Game Log.

What stays the killer's alone: the **cargo crate** (loot and resources; a [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) is the exception, whose loot is a private box for every mate who is paid a part), the kill in their statistics and ranking, the Wipe Point kill count and the drones' experience. Kills of other pilots are not shared.

## Sharing Missions

A kill also counts for the **kill missions** of every other member who is on the same map and **fired a laser or rocket at anything in the last 15 seconds**, wherever they are on it, as if they had destroyed the alien themselves. The mission's own rules still decide: the alien must be the mission's kind and the sector the mission names. A mate who did not shoot, or is on another map, gets no count. Missions keep their own company's rules: a mission that asks for a kill in "another company's sector 4" counts for the member for whom that sector is another company's. When a mate's kill counts for one of your missions, a notice tells you which. In the [Challenge line](/wiki/03-Mechanics/Quests.md#where-it-counts) a member must also be within **4,000 units** of the wreck to count, and every member who has a mission with a quest item rolls and sees their own item: nobody can share one.

## Chat Channels

The chat has a row of tabs on top: **Global**, **Local**, **Group** (while you are in a group) and, last, **System**. The line you type goes to the tab in view, and the tab you last used is remembered. Each channel has its colour and a short tag on every line (GLB, LOC, GRP), a tab counts the lines you have not read, and the chat's button in the toolbar carries the count while the window is closed. Or start a line with a command:

| Channel | Who hears it | Command |
| :--- | :--- | :--- |
| **Local** | pilots on your map | `/l` or `/local` |
| **Global** | every pilot online | `/g` or `/global` |
| **Group** | your group, wherever they are | `/p`, `/party` or `/group` |

A command switches the tab too, and typed alone (`/g`) it only switches. Group chat needs a group. On a game server from before the channels the chat is the one list it was, and a group cannot be formed.

**System** is gold and read-only, with a list of its own: it holds what the server says on its own (the welcome, the restart, update and wipe warnings, the swarm announcements) and what your ship reports (repairs, cloaking, EMPs, rockets). Those lines are in no other tab, so a busy Global cannot push them out, and the pilots' tabs hold what pilots say. The tab's count is for the announcements; a restart or update countdown and the wipe warnings also pop up as a notice. The [kill feed](#the-kill-feed) stays in **Global**, with its own switch, and the lines about pilots joining or leaving your group are in **Group**.

### Typing

**Enter** opens the chat and gives it the keyboard. Send a line with **Enter** and the box keeps the keyboard, so the next line can follow at once; while it does, the hotbar and the ability keys stay off. Typing ends when you press **Escape**, press **Enter** with nothing typed, click the map with the left button (the same click still steers your ship), leave the box empty and press no key for 15 seconds, or your ship is destroyed. On the System tab, where you cannot write, **Enter** takes you back to the channel you wrote in last.

### The Chat Rules

The server holds every line to a few rules, the same in Local, Global and Group. A line it refuses is not sent, and the reason shows under the input for a few seconds, with your text put back in the box.

- **A limit on how fast you send.** You can send **5 lines** at once, then **one more line every 2 seconds**, counted together for Local, Global and Group. Send a line when none is left and the chat **pauses** for you: for **10 seconds** the first time, then **30**, **120** and **300 seconds** for every repeat within 10 minutes of the last pause (after 10 minutes without a pause the count starts again). While it lasts the Send button is grey and "Chat paused: 7 s" counts down under the input. **The text you typed stays in the box** and the box keeps the keyboard: wait, or press **Escape**. A normal conversation never reaches the limit. A line the rules refuse counts as 2 lines of the allowance.
- **200 characters** to a line. A counter ("150/200") shows from 120 characters, and a longer line is cut.
- **Latin letters only.** The letters of the Latin alphabets with their accents (é, ß, ñ, ø, ő), digits, the usual punctuation and the marks ¡ ¿ « » ° £ €. Cyrillic, Chinese, Japanese, Korean, emoji and other symbols are refused, and the box drops them as you type or paste.
- **No links.** A line with a web address, an invitation link or an e-mail address is refused, even when it is disguised in the usual ways. Words alone are fine: "join my discord" goes out.
- **No repeats.** The same line as your last one, sent again within 10 seconds, is refused, and so is a line with the same character more than 8 times in a row or with no letter or digit in it.

Admins are not held to these rules, except for the 200 characters. The rules need a game server from 0.4.9; an older one only limits Global, to 3 lines at once and then one every 2 seconds.

### The Kill Feed

The **Global** tab also carries a kill feed: a muted line with a skull whenever a pilot is destroyed, worded with a little humour ("vega asked the black hole for directions"). It says who died and who or what did it: a pilot's lasers, a rocket (the **N.U.K.E.** and the **N.I.K.E.** have lines of their own), an alien by its name, the black hole's horizon or its radiation, or an enemy who pushed the pilot in. The names wear their company's tag and colour. It never says **where**: no map and no position, so a cloaked pilot's death gives nothing away. Only pilots get a line: an alien or a company pilot being destroyed does not, and a pilot who logs out in a fight is not destroyed, so there is no line for that either.

When many pilots die within seconds (a N.U.K.E. over a dogfight) you see the first few and then one line, "7 more pilots died". The feed has its own place in the scrollback, so a battle never pushes your friends' messages out.

Turn it off with the menu button in the chat window's title bar (**Show kill feed**) or in **Settings > Interface > Chat**. Off only hides the lines; they come back when you turn it on. The feed needs a game server from 0.4.5: on an older one the Global tab has none.

### Hiding, Ignoring and Reporting

Global reaches every pilot online, so the chat has three tools to keep it comfortable. They are in the chat window: the menu button in its title bar, and a right-click on a pilot's name.

- **Hide Global chat** (the menu, or Settings › Interface › Chat): the Global tab shows nothing, the kill feed's lines included, and stops counting unread lines. The tab stays, says "Global is hidden" and has a button that shows it again; what you send to Global still goes out. Turn it off and every line that came meanwhile is there.
- **Ignore** (right-click a name, then **Ignore**): that pilot's lines in Global and Local are hidden, and their group invitations are turned down without asking you. They are not told. They stay visible in the **Group** tab: a group mate you ignore is still your group, so leave the group to be rid of them. The server's own lines are never hidden. **Stop ignoring** is on the same menu, and **Settings › Interface › Chat** lists the ignored pilots (up to 200) with a **Remove** button for each.
- **Report** (right-click a name, then **Report…**): pick a reason (spam, abuse or harassment, cheating, or something else) and send. The report carries your name, the pilot's, the channel, the reason and the last line of that pilot that your chat shows (up to 200 characters). The game's admins read it; nobody is punished automatically, and the pilot is not told who reported them. You can send 5 reports an hour.

Your ignored list and the Hide Global switch are kept with your account, so they follow you to other computers. The game has no word filter and mutes nobody for what they say: the pause for sending too fast ([The Chat Rules](#the-chat-rules)) is its only automatic stop, and the tools above are yours to use.

## Rules of Engagement

**Members of one group cannot hurt each other**, whatever their companies: you cannot lock on to a groupmate (lasers or rockets), your shots and blasts pass through them, and nothing you do to one counts as a kill, a PvP kill or a black hole kill for anyone. Company mates who are **not** in the same group are as before: hitting one costs **100 Honor** when it is destroyed. Leave the group and a former mate, enemy or not, is fair game again at once (where the sector and the season allow fighting at all). Everyone outside your group is treated as ever, and safe zones, the Peace Protocol and the sectors' PvP rules do not change for anyone.

## Bringing a Friend

A friend who is new to the game can join with your personal code and gets a starter pack; see [Invite Friends](/wiki/03-Mechanics/Invite-Friends.md).
