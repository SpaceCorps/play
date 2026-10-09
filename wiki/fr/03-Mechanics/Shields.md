<!-- wiki-i18n source: fa02f72ab515dfbf -->
<!-- wiki-i18n title: Boucliers -->
# Mécaniques des boucliers {#shield-mechanics}

Les boucliers absorbent la majeure partie des dégâts reçus et protègent la coque de votre vaisseau des dégâts directs.

## Calculs du bouclier {#shield-calculations}

Les paramètres finaux de bouclier de votre vaisseau sont calculés ainsi :

\[\text{Capacité finale du bouclier} = \text{Capacité de base totale} \times (1,0 + \text{Pourcentage total de bonus de bouclier})\]
\[\text{Vitesse de recharge finale du bouclier} = \text{Recharge de base totale} \times (1,0 + \text{Pourcentage total de bonus de bouclier})\]

### 1. Efficacité des emplacements et rendements décroissants {#1-slot-efficiency-diminishing-returns}

Comme pour les moteurs, les boucliers équipés (et les générateurs hybrides) sont classés du meilleur au moins bon, puis soumis à l’efficacité de leur emplacement (principal : 100 %, de soutien : 75 %, auxiliaire : 50 %, emplacement de drone : 100 %, comme un emplacement principal) et à une courbe de rendements décroissants selon leur rang. Un bouclier est classé selon ce qui compte de lui : sa capacité multipliée par la part de son emplacement. La recharge a son propre ordre (sa valeur multipliée par la part de l’emplacement), et les **quatre meilleurs** bonus de bouclier comptent. Un bouclier sur l’un de vos [drones](/wiki/03-Mechanics/Drones.md) est classé avec ceux du vaisseau :

- **1er au 4e bouclier** : efficacité marginale de **100 %** (1,0).
- **5e bouclier** : efficacité marginale de **85 %** (0,85).
- **6e bouclier** : efficacité marginale de **70 %** (0,70).
- **7e bouclier** : efficacité marginale de **55 %** (0,55).
- **8e bouclier et suivants** : efficacité marginale de **50 %** (0,50). (Jusqu’à la version 0.4.7, c’était 25 %, comme pour les moteurs ; les moteurs gardent 25 %, voir [Vitesse](/wiki/03-Mechanics/Speed.md).)

**Ajouter ne baisse jamais votre bouclier.** Ajouter un bouclier ou une cellule de bouclier ne baisse jamais votre capacité de bouclier ni votre recharge : chaque chiffre est classé du meilleur au moins bon selon ce qui compte, si bien qu’une nouvelle pièce prend la place qu’elle mérite. L’absorption est la moyenne de vos boucliers : un nouveau bouclier plus faible que votre moyenne la baisse, une cellule jamais.

**Le hangar l’indique.** Un bouclier, un moteur ou un cœur adaptatif qui ne compte pas pour toute sa puissance affiche un petit pourcentage sur son emplacement (par exemple `64%` : le 5e bouclier, à 85 %, dans un emplacement de soutien, à 75 %), et le survol donne le détail. Survolez les cases Boucliers et Vitesse des stats de combat pour voir vos objets par rang et ce que compterait un de plus. La fenêtre Vaisseau en vol montre les mêmes listes quand vous survolez sa barre de bouclier et sa vitesse.

### 2. Absorption du bouclier (répartition des dégâts) {#2-shield-absorbance-damage-split-}

L’absorption est la part de chaque tir que prennent vos boucliers ; le reste va directement aux points de vie (PV).
- **Par bouclier** : l’absorption d’un bouclier plus celle des cellules de bouclier qui y sont installées. Un bouclier seul donne **45 à 50 %** (Light 45 %, Basic 48 %, Heavy 50 %) ; chaque cellule ajoute de 2 à 10 points (Capacity Shield Cell I à IV +2 %, +3 %, +4 %, +5 % ; Absorption Shield Cell I à IV +4 %, +6 %, +8 %, +10 %).
- **Absorption moyenne** : l’absorption de votre vaisseau est la simple moyenne des boucliers installés dans les emplacements principaux, de soutien et auxiliaires, et sur vos drones. Les cœurs adaptatifs n’ont pas d’absorption propre et ne comptent pas dans la moyenne (les cellules d’un cœur adaptatif n’ajoutent que de la capacité et de la recharge). Sans bouclier équipé, votre absorption est de 0 % : la coque encaisse chaque tir, et les points de bouclier des cellules d’un cœur adaptatif restent inutilisés ; équipez donc aussi un bouclier.
- **Le maximum sans bonus est de 80 %** : le meilleur bouclier avec les meilleures cellules, soit un Heavy Shield Core avec trois Absorption Shield Cell IV dans chaque emplacement. Mélanger des boucliers plus faibles fait baisser la moyenne. Aucun bonus de la Boutique de saison ni de la Forge n’entre dans ce chiffre.
- **Exemple** : un Basic Shield Core (48 %) avec deux Absorption Shield Cell I donne 56 % ; ajoutez un Light Shield Core (45 %) et la moyenne est de 50,5 %.
- **Cette statistique n’est pas plafonnée à 100 %.** C’est ce que les boucliers prendraient d’un tir, avant que la *pénétration de bouclier* de l’attaquant en soit retranchée : un vaisseau peut donc avoir plus que de quoi absorber un tir entier. Avec 112 %, les boucliers prennent encore un tir entier face à un attaquant dont la pénétration va jusqu’à 12 %.

#### Pénétration de bouclier {#shield-penetration}

Certaines attaques ont une **pénétration de bouclier** : des points retranchés de votre absorption pour ce tir. La part que prennent vos boucliers est

\[\text{Part du bouclier} = \text{borner}(\text{Absorption} - \text{Pénétration},\ 0,\ 100\ \%)\]

- Les boucliers prennent au plus `round(damage x share)` du tir ; la coque prend le reste. Un bouclier trop faible pour sa part reporte la différence sur les PV, et si les boucliers sont à 0, tous les dégâts frappent directement les PV.
- **D’où vient la pénétration** : la *pénétration de bouclier* d’une roquette directe (Lancet I 10 %, Lancet II 25 %, Lancet III 35 %, Rivet I 5 %, Rivet II 25 %, Rivet III 35 %, N.I.K.E. 35 % ; les explosions de zone n’en ont pas, voir [Roquettes](/wiki/06-Items/Rockets.md)) et celle des munitions laser (Ultra Core 5 %, Experimental Fusion Core 10 % ; voir [Lasers et munitions](/wiki/06-Items/Lasers.md)). Les aliens n’en ont pas, et les munitions x1 et x2 non plus. Un tir laser retranche aussi les Penetration Amps des lasers du tireur (+2 % à +8 % par emplacement, la moyenne de ses lasers) et la pénétration d’une formation de drones (Gemini +9 %, Stiletto +16 %) ; une roquette directe ajoute celle de la formation à la sienne. **Rien ne plafonne le total** : les boucliers encaissent l’absorption moins tout cela, jusqu’à ne plus rien encaisser du tir ([comment un tir laser s’additionne](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Exemples** : avec 80 % d’absorption face à une Lancet III (35 %), les boucliers prennent 45 % du tir, la coque 55 %. Avec 100 % : 65 % et 35 %. Avec 112 % face à 12 % de pénétration : la totalité du tir. Avec 45 % (un Light Shield Core seul) face à 35 % : 10 % sur le bouclier, le reste sur la coque. Une roquette seule ne pénètre complètement aucun noyau, mais une Lancet III avec un Stiletto (35 % + 16 % = 51 %) ne laisse rien du tir à un Light Shield Core seul (45 %), et le meilleur laser (50 %) non plus : contre ce laser, le meilleur bouclier (80 %) encaisse 30 % du tir et la coque 70 %.
- Les aliens n’ont pas de statistique d’absorption : ils répartissent chaque tir 80 % / 20 %, moins la pénétration du tir.
- Les dégâts d’une Siphon Battery sont pris sur le seul bouclier : l’absorption et la pénétration n’entrent pas en jeu.

**Là où les boucliers n’encaissent rien.** Une pénétration égale ou supérieure à l’absorption ne laisse rien du tir aux boucliers : la coque prend tout. Le tableau montre ce que les boucliers encaissent d’un tir du meilleur laser (50 %) et de la meilleure roquette directe (une Lancet III ou une Rivet III avec un Stiletto, 51 %) :

| Bouclier | Absorption | Les boucliers encaissent, meilleur laser (50 %) | Les boucliers encaissent, meilleure roquette directe (51 %) |
| :--- | ---: | ---: | ---: |
| Light Shield Core | 45 % | 0 % | 0 % |
| Basic Shield Core | 48 % | 0 % | 0 % |
| Heavy Shield Core | 50 % | 0 % | 0 % |
| Le meilleur bouclier d’origine | 80 % | 30 % | 29 % |
| Un bouclier à 100 % | 100 % | 50 % | 49 % |
| Un bouclier à 120 % | 120 % | 70 % | 69 % |

#### Atteindre et dépasser 100 % {#reaching-and-passing-100-}

- **Sans bonus** : 80 % au plus (voir ci-dessus).
- **Shield Absorbance Boost** : un bonus permanent de la Boutique de saison, acheté avec des points de réinitialisation, **+0,1 point par niveau, +10 points au maximum** (100 niveaux, 25 PR chacun). Il ajoute des points fixes à l’absorption de votre vaisseau, les mêmes sur n’importe quel vaisseau équipé d’un bouclier : 80 % deviennent 80,4 % avec 4 niveaux (100 PR), et les 45 % d’un Light Shield Core deviennent 46,2 % avec 12 niveaux (300 PR). Un vaisseau sans bouclier équipé reste à 0 %. Les 100 niveaux coûtent 2 500 PR, un objectif pour plusieurs réinitialisations : les sources actuelles de points de réinitialisation (les paliers d’éliminations et les missions) rapportent 855 PR en tout à leur plafond, cumulés d’une réinitialisation à l’autre, ce qui permet d’acheter 34 niveaux, soit +3,4 points. D’autres sources de points de réinitialisation sont prévues. Voir [Saison et points de réinitialisation](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Forge** : les boucliers et les cellules de bouclier peuvent obtenir un bonus d’**absorption**, qui multiplie la statistique : +5 % sur un bouclier à 50 % font +2,5 points. Le meilleur ensemble, Éternel et entièrement forgé (cœur et trois cellules, chaque bonus tiré au maximum, +15 %), ajoute jusqu’à 12 points, environ 10 en moyenne (voir [La Forge](/wiki/06-Items/Forge.md)).
- **Cumul** : 80 % sans bonus, +3,4 points de bonus (la totalité des 855 PR actuels) et jusqu’à +12 points de bonus de Forge donnent **95,4 %** au maximum aujourd’hui ; avec les 100 niveaux du bonus (+10 points, 2 500 PR), on arriverait à 102 %. Ni le bonus ni la Forge seuls n’atteignent 100 % ; y arriver est un objectif pour plusieurs réinitialisations, et d’autres sources de points de réinitialisation sont prévues.

### Bonus de bouclier : capacité, absorption, recharge {#shield-boosts-capacity-absorbance-recharge}

Chaque bonus de bouclier augmente l’une des trois statistiques et figure sous son propre type dans la fenêtre Boosters :

- **Capacité** (points de bouclier maximum) : les boosters Shield Wall Booster I et II et le Shield Capacity Boost permanent.
- **Absorption** (la part d’un tir que prennent vos boucliers) : le Shield Absorbance Boost permanent (+0,1 point par niveau, +10 points au maximum).
- **Recharge** (points de bouclier restaurés par seconde) : le Shield Regen Booster.

Voir [Boosters](/wiki/06-Items/Boosters.md) pour les chiffres.

---

## Régénération passive du bouclier {#shield-passive-regeneration}

Les boucliers se régénèrent passivement avec le temps pour que vous restiez prêt au combat.

- **Cycle de régénération** : si les boucliers sont sous leur capacité maximale, ils restaurent chaque seconde autant de points de bouclier que votre vitesse de recharge.
- **Interruption par le combat (délai de 15 s)** : la régénération cesse quand vous subissez des dégâts et ne reprend qu’après **15 secondes** sans dégâts. Les formations de drones Adamant et Redoubt ([Formations de drones](/wiki/03-Mechanics/Formations.md)) font exception : elles rendent du bouclier chaque seconde, même en combat.
