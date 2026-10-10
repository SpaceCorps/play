<!-- wiki-i18n source: 13c9ac551cfd01fa -->
<!-- wiki-i18n title: Secteurs dangereux -->
# Secteurs dangereux {#danger-sectors}

<!-- wiki-search: ds; ds-1; ds-2; ds-3; ds-4; central pvp zone; pvp zone; pulsar; giant excavator; excavator; dormant swamp; swamp; event 2; tech surge; secteur dangereux; excavatrice géante; excavatrice; marais; essor technologique -->

Les **secteurs dangereux** sont les quatre secteurs du centre de la galaxie, `DS-1` à `DS-4`. Les trois corporations s’y rencontrent, et les pilotes peuvent s’y affronter dans tous les mondes ([Navigation spatiale](/wiki/01-General/Spacemap%20Travel.md)). `DS-1`, `DS-2` et `DS-3` ont chacun la porte d’une corporation ; `DS-4` est le cœur, avec le [trou noir](/wiki/03-Mechanics/Black-Hole.md) au milieu. Aucun n’a de station : les seuls endroits sûrs sont les anneaux autour des portes de saut.

Une civilisation de l’ancienne galaxie a vécu ici, avancée et d’un noir violacé, et pour une raison que personne ne connaît, elle s’est effondrée. Ses vestiges n’ont jamais été tout à fait morts : l’[Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) en a été le premier signe. À partir du **jour 11 de la saison**, début de l’événement 2 (**Essor technologique**, voir la [Chronologie des réinitialisations](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)), davantage s’en réveille et les secteurs dangereux changent. Chaque pilote du monde en est prévenu le jour où cela commence, et ce qui est nouveau reste jusqu’à la réinitialisation.

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## Ce qui est nouveau dès le jour 11 {#what-is-new-from-day-11}

- **Des excavatrices géantes.** `DS-1`, `DS-2` et `DS-3` ont chacun un pulsar dès le premier jour de la saison, une lumière dans le ciel et rien de plus ; à partir du jour 11, chacun reçoit une **excavatrice géante** à côté. Mettez de la Dark Matter dans le réservoir de l’excavatrice, choisissez une ressource, et elle exploite le pulsar : du Thulium et des minerais rares tombent autour d’elle dans des caisses que n’importe qui peut prendre. C’est ce qu’il y a de plus riche à se disputer dans les secteurs dangereux, et de plus dangereux. Voir [Excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md).
- **Des Slumbering Voids.** Pendant qu’une excavatrice travaille, des **Slumbering Voids** arrivent par vagues du bord de la carte et traquent les pilotes qui s’en approchent. D’autres patrouillent autour du marais. Voir [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).
- **Le Dormant Swamp.** Dans un coin de `DS-4` se dresse la base de la civilisation perdue : des canons qui tirent sur tout vaisseau qu’ils voient, des Inert Masses qui la gardent et, au milieu, l’Unwakened. C’est un endroit que les pilotes ne sont pas encore censés visiter. Voir [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md).
- **Un Essaim Dormant plus rapide et plus riche.** L’essaim apparaît désormais au marais, revient plus tôt après sa destruction et paie le double. Voir [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md).
- **Avant le jour 11**, seuls les pulsars brillent : les secteurs dangereux sont sinon tels que les décrit [Navigation spatiale](/wiki/01-General/Spacemap%20Travel.md). Un monde au jour 11 ou après a tout d’un coup.

## Où se trouve quoi {#where-everything-is}

Chaque monde a sa propre copie de tout, et un pulsar et son excavatrice se tiennent dans le tiers dégagé de leur secteur, loin de tous les anneaux de portes, du côté qui regarde vers le milieu de la carte. Les distances sont en unités de la carte ; les secteurs font 32 000 sur 18 000 unités.

<!-- danger-sites:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Secteur | Porte de la corporation | Pulsar | Excavatrice géante |
| :--- | :--- | :--- | :--- |
| `DS-1` | Mars | 8 000 / 5 000 | 8 805 / 5 402 |
| `DS-2` | Terra | 8 000 / 13 000 | 8 805 / 12 598 |
| `DS-3` | Galactic | 24 000 / 13 000 | 23 195 / 12 598 |

<!-- danger-sites:end -->

`DS-4` n’a pas de pulsar : le trou noir y est. Son coin contient à la place le Dormant Swamp ; ses chiffres sont dans [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#at-a-glance).

<!-- danger-rules:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- Les pulsars brillent dès le premier jour de la saison ; tout le reste de ce qui est nouveau apparaît au jour 11 de la saison et reste jusqu’à la réinitialisation.
- Chaque monde a ses propres pulsars, excavatrices et marais : ce qui arrive dans l’un n’arrive pas dans l’autre.
- Aucun astéroïde ne se trouve à moins de 2 600 unités d’un pulsar, à moins de 2 200 unités d’une excavatrice géante ni à moins de 4 900 unités du milieu du Dormant Swamp.

<!-- danger-rules:end -->

## Éviter les ennuis {#keeping-out-of-trouble}

- **Radiation.** Une excavatrice qui a surchauffé ou qui a été détruite, et son pulsar, brûlent tout vaisseau qui reste dans leurs cercles ([Excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md#heat-and-radiation)). Le jeu vous prévient avant, et les cercles sont dessinés au sol en vol et sur la minicarte.
- **Les canons du marais.** Les tourelles du marais tirent sur un vaisseau qu’elles voient bien avant qu’il puisse voir quoi que ce soit qui vaille le voyage ([Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-guns)). Un cap que vous cliquez est infléchi autour des canons et de la radiation, comme autour du trou noir, et une alerte vous prévient quand l’endroit cliqué se trouve à l’intérieur.
- **Si vous êtes détruit là-bas,** le choix de revenir **sur place** vous met au point le plus proche hors de la radiation et hors de la zone du marais, comme pour le trou noir ([Premiers pas](/wiki/01-General/Getting-Started.md#dying-and-coming-back)).
- **Un groupe et une issue.** Les excavatrices attirent autant les Voids que les rivaux. Venez avec un [groupe](/wiki/03-Mechanics/Groups.md), sachez quelle porte est la plus proche et rappelez-vous que, dans les secteurs dangereux, vous ne pouvez pas sauter tant qu’on vous attaque ([Sauter sous le feu](/wiki/01-General/Spacemap%20Travel.md#jumping-under-fire)).
- **Le reste est du PvP comme toujours.** Rien ici n’est un endroit sûr : les règles normales de votre monde s’appliquent, rivaux compris.

## Pour en savoir plus {#where-to-read-more}

- [Excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md) : le panneau, le carburant, ce qu’elle extrait, les Voids, la chaleur et la radiation.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) : les canons, les trois aliens et la nouvelle demeure de l’essaim.
- [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) et [Essaims](/wiki/05-Swarms/Swarms.md).
- [Le trou noir](/wiki/03-Mechanics/Black-Hole.md) et [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) : d’où vient le carburant.
- [Extraction d’astéroïdes](/wiki/03-Mechanics/Asteroid-Mining.md) : les roches des secteurs dangereux.
