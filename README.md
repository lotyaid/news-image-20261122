# newsbot22

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/lotyaid/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/lotyaid/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

THE WORLD TODAY — Sunday, 22 November 2026. One page, 34 stories from around the world: the Gulf war widens as Iran strikes US bases in Kuwait and Bahrain, Russian missiles land in Poland, COP31 runs into overtime in Antalya, a 6.7 quake shakes Peru, the EU and Indonesia sign a decade-in-the-making trade deal, and Mexico captures "El Chapo Isidro". A lead feature with a schematic Gulf map, five illustrated features, a diplomacy band, a day-in-numbers strip (400+ drones, 110+ missiles, 11 killed in Sinaloa, 6.7 magnitude, 98.5% tariffs) and 24 briefs. Every story checked against wire reports.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=q0a4tfr8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>

## What's on the page

**Lead — Middle East, the Gulf war:** Iran fires drones and missiles at US military targets in Kuwait (Ali Al Salem air base) and Bahrain, its Revolutionary Guard said; both countries say their defences intercepted the attacks with no casualties reported. A tanker is hit by a mine east of the Strait of Hormuz; more tankers are attacked off Oman. Sources: IRIB via AP/Reuters, US Central Command, Kuwaiti and Bahraini armed forces.

**Climate — COP31, Antalya:** Talks stretch into a second day of overtime on Sunday, deadlocked over a draft deal that mentions no fossil fuels at all; a new package goes to nearly 200 delegations in the early hours and the presidency hopes to approve it on Sunday morning. The EU warns it will take "a good deal or no deal". Sources: Reuters, AP.

**Europe — war in Ukraine:** Two Russian cruise missiles and a drone come down in south-east Poland during a huge overnight assault on Ukraine — more than 400 drones and 110 missiles, Kyiv said. Lviv is hit hard: 2 killed, 10 hurt. Warsaw calls it a deliberate provocation; NATO chief Mark Rutte flies to Warsaw and vows to defend "every inch" of Polish soil. Sources: Reuters, AP, Polish Defence Ministry, President Zelenskyy.

**Americas — earthquake:** A magnitude 6.7 earthquake (USGS) strikes the Andes in central Peru on Friday evening, epicentre near Junín, sending residents of Lima into the streets. No casualties or major damage reported. Sources: USGS, AP, Peru's Geophysical Institute.

**Trade — Brussels:** The EU and Indonesia sign a trade pact in Brussels on Saturday, ending nearly 10 years of talks. Once in force, tariffs fall on 98.5% of EU goods and over 90% of Indonesian goods. Parliaments must still approve it; entry into force is targeted for 2027. Sources: European Commission, Reuters, AFP.

**Americas — cartels:** Mexican special forces capture Fausto Isidro Meza Flores, "El Chapo Isidro", an FBI Top 10 fugitive, in Guasave on Friday night. The raid sets off gun battles across Sinaloa that leave 11 dead — 7 gunmen and 4 soldiers. He is flown to Mexico City. Sources: Reuters, AP, Mexican Defence Ministry.

**Diplomacy band:** Trump, Xi and Putin meet face to face in Shenzhen with little agreed; Zelensky says new peace talks may open on the G20 sidelines; Vance declines to back Trump's strikes on Iran; the COP31 draft drops the $120bn adaptation-finance target.

**The day in numbers:** 400+ drones and 110+ missiles in Russia's overnight barrage; 11 killed in Sinaloa; magnitude 6.7 in Peru (USGS); 98.5% of EU goods to go tariff-free under the Indonesia deal.

**24 briefs:** Hong Kong Election Committee voting; Denmark expels Moscow's envoy over an alleged plot against a Ukrainian rapper; drone hits a Russian cargo ship off Finland; tech sell-off; FBI probes a suspected hack of its criminal database; Bolsonaro in intensive care; Tasis alliance seizes Bau in Sudan; bootleg liquor kills 11 in Manipur; Estonia closes its Russia border; UN fails to agree autonomous-weapons rules; Japan's first live-fire drill in India; SCO summit in New Delhi; Hormuz and Oman shipping attacks; Kuwait and Bahrain air defences; Lviv and Kyiv damage; NATO council meeting Monday; Guasave baseball game; the $5m US reward on "El Chapo Isidro"; Sinaloa troop deployment; Lima anchor reporting through the quake; Junín epicentre details.

## How it was built

`draw.py` renders the front page with Pillow (DejaVu/Liberation fonts) and saves `entry.png` (1024×1024). `main.py` (Python 3 standard library only) copies that image to `/output/entry.png` — deterministic, no network. Run `python3 draw.py` to re-render.
