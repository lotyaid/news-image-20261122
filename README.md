# news-image-20261122 (revision)

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/lotyaid/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/lotyaid/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

THE WORLD TODAY — Sunday, 22 November 2026: the world in one day, 40 stories from 6 regions, with the news swept to 09:35 UTC — hours fresher than this entry's first edition. The Gulf war widens as Iran strikes US Patriot radars in Bahrain and tankers are hit near Hormuz; COP31 in Antalya puts a final deal with no mention of fossil fuels to a Sunday vote; a Russian missile kills a first responder and a seven-year-old in Kryvyi Rih; the AI sell-off pushes Wall Street into correction. A lead feature with a schematic Gulf map, four illustrated features, a consensus band of the five stories every wire carried (Shenzhen's three-leader meeting, the EU–Indonesia trade deal, Peru's 6.7 quake, Gaza's aid vehicle, the ICJ genocide ruling), a day-in-numbers strip (400+ drones, 110+ missiles, S&P −3.7%, Nikkei −5.1%, gold −4.6%, GTA VI $3.79bn, magnitude 6.7, a 35% electrification goal) and 30 briefs. Every story checked against the day's wire reporting.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## What's on the page

**Lead — the Gulf war:** Iran's Revolutionary Guard said its missiles and drones struck two US Patriot radars at the Al-Riffa and Awali bases in Bahrain late on Saturday, answering US drone flights and a strike on Hengam Island. Bahrain said an industrial site was hit and set ablaze — no injuries — and its defences intercepted the attacks; Kuwait engaged drones in its skies, tankers were hit near the Strait of Hormuz, and Washington says nearly all the fire was intercepted. Sources: Reuters, Al Jazeera, IRNA, Bahrain Defence Force, US Central Command.

**Climate — COP31, Antalya:** Two days into overtime, the presidency's ten-page text went to nearly 200 delegations before dawn on Sunday: it recalls the COP28 pact, sets electricity at 35% of world energy by 2035, drops the $120bn adaptation target, and is the first COP text to admit the 1.5°C limit will be overshot. Objections closed at 03:00 GMT and the adoption plenary slipped to late morning, with the EU calling the draft a backwards step. Sources: Reuters, AP, BBC, The Guardian.

**Conflict — Kryvyi Rih:** A Russian ballistic missile struck Zelensky's hometown on Saturday, killing a first responder and a seven-year-old boy and wounding dozens. Ukraine's drones answered: a Russian cargo ship burned in the Gulf of Finland (crew evacuated) and the Ust-Luga port was attacked. Sources: One Turn wires, Zelenskyy statement, Finland Border Guard.

**Justice — Guasave, Sinaloa:** Special forces arrested Fausto Isidro Meza Flores, "El Chapo Isidro", an FBI Top 10 fugitive, on Saturday. Seven gunmen and four soldiers died in the operation; the arrest was reported by 17 outlets. Sources: Al Jazeera, BBC, The Guardian.

**Economy — New York:** Friday's rout in AI and chip shares sent the S&P 500 down 3.7% and into correction territory with the Dow. Japan's Nikkei fell 5.06%, gold slid 4.62% and Bitcoin 1.79%; India's Sensex rose 2.3%.

**The consensus five:** Trump, Xi and Putin meet in Shenzhen and agree to open nuclear risk-reduction talks · the EU and Indonesia sign their trade deal in Brussels after ten years (98.5% of EU goods to enter tariff-free) · Peru's magnitude 6.7 quake near Junín leaves 170 homes affected and no deaths · an aid vehicle is hit in Gaza as Israeli strikes continue and Hamas seeks urgent talks · the ICJ finds Myanmar responsible for genocide against the Rohingya and advocates press for penalties.

**30 briefs:** Denmark expels Russia's attaché · Nigeria funeral boat capsizes, 24 dead · Serang candy factory fire · Houthis fire on Saudi Arabia · Finland probes a Russian helicopter incursion · Iran's F-16 claim, denied by Washington · UK–EU deals and Burnham · Lebanon's Aoun speaks out · West Bank settler attacks · EU–Rwanda hubs and digital tax · Haiti–El Salvador prisons pact · Bolsonaro in intensive care · Trump orders contractors to report Congress · Bangladesh garment strikes · Saudi oil stored in Japan triples · Argentina's $50bn LNG project · Belgian air-traffic strike · CRISPR therapy halves bad cholesterol · Princess Kate in remission · a new mini-moon, 2026 QQ8 · a pilotless air taxi flies in Japan · GTA VI's $3.79bn launch day · Leeds stun Chelsea 4–1 · Phumzile Mlambo-Ngcuka dies at 71 · Alcaraz–Zverev ATP final · BTS take five MAMA awards · a swimmer crosses Hormuz for wildlife · Iran rations electricity · Tunisia jails Bensedrine · Manipur's fake-liquor deaths.

## How it was built

`compose.py` draws the front page with Pillow (DejaVu/Liberation fonts) — masthead, schematic Gulf map, feature art, consensus band, numbers strip and brief columns — and saves `entry.png` (a JPEG, 1024×1024, under 1 MiB, byte-identical on every run). `main.py` (Python 3 standard library only) copies that image to the output directory. Run `python3 compose.py` to re-render. All facts come from the Sunday 22 November 2026 edition of One Turn (46 stories and 17 in brief, from 757 headlines), cross-checked against Reuters, AP, the BBC, Al Jazeera and official statements, with the sweep cut off at 09:35 UTC.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q0a4tfr8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
