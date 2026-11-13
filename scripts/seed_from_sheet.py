"""Engångsimport: bygger data/trupp.json från Google-arket 'AIK Fotboll Trupp' (läst 2026-11-13)."""
import json
# namn, nr, land, pos, födelsedag, kontraktsslut, hemmafostrad, AIK U  (fliken Herr-A Total Trupp)
TOTAL = """Eskil Edh|2|Norge|YB|2002-08-04|2027-12-31|Nej|Nej
Hervé Matthys|3|Belgien|MB|1996-01-19|2028-12-31|Nej|Nej
Sotirios Papagiannopoulos|4|Sverige|MB|1990-09-05|2027-12-31|Ja|Ja
Lukas Berquist|5|Sverige|YB|2000-06-28|2027-12-31|Ja|Nej
Martin Ellingsen|6|Norge|CM|1995-05-04|2026-12-31|Nej|Nej
Amel Mujanic|7|Sverige|CM|2001-04-01|2030-12-31|Ja|Nej
Johan Hove|8|Norge|CM|2000-09-07|2028-12-31|Nej|Nej
Linus Carlstrand|9|Sverige|ANF|2004-08-31|2030-12-31|Ja|Nej
Charlie Pavey|12|Sverige|YB|2008-06-07|2027-12-31|Ja|Ja
Fredrik Nissen|14|Sverige|MB|2005-03-28|2029-12-31|Ja|Nej
Kristoffer Nordfeldt|15|Sverige|MV|1989-06-23|2027-12-31|Ja|Nej
Sixten Gustafsson|16|Sverige|ANF|2007-02-05|2030-12-31|Ja|Ja
Mads Thychosen|17|Danmark|YB|1997-06-27|2027-12-31|Nej|Nej
Abdihakin Ali|18|Sverige|CM|2002-01-22|2026-12-31|Ja|Ja
Dino Beširović|19|Bosnien|CM|1994-01-31|2027-12-31|Nej|Nej
Sebastian Hausner|20|Danmark|MB|2000-04-11|2026-12-31|Nej|Nej
Stanley Wilson|21|Kenya|CM|2006-08-21|2029-12-31|Nej|Nej
Adrian Helm|22|Sverige|YM|2005-09-27|2029-12-31|Ja|Nej
Andreas Redkin|24|Sverige|CM|2007-01-19|2029-12-31|Ja|Ja
Ibrahim Cissé|25|Elfenbenskusten|MB|1999-01-11|2028-12-31|Nej|Nej
Linus Järeteg|28|Sverige|CM|2007-01-20|2029-12-31|Ja|Ja
Kevin Filling|29|Sverige|ANF|2008-11-30|2028-06-30|Ja|Ja
Kalle Joelsson|30|Sverige|MV|1998-03-21|2027-12-31|Ja|Nej
Emmanuel Gono|31|Liberia|ANF|2005-10-25|2028-12-31|Nej|Nej
Wilmer Olofsson|34|Sverige|MB|2005-09-16|2028-12-31|Ja|Ja
Norton de Carvalho Otterud|40|Sverige|MV|2008-06-14|2029-04-16|Ja|Ja
Taha Ayari|45|Sverige|YM|2005-05-10|2028-12-31|Ja|Ja
Yannick Geiger|46|Sverige|CM|2007-06-23|2029-12-31|Ja|Ja
Axel Kouame|48|Elfenbenskusten|CM|2003-10-14|2029-12-31|Nej|Nej
Nana-Kofi Donkor||Ghana|YM|2007-01-05|2030-12-31|Nej|Nej
Oskar Pukelis||Sverige|VB|2008-02-29|2029-12-31|Ja|Ja
Filip Lukic||Sverige|CM|2007-04-12|2029-12-31|Ja|Ja
Aziz Harabi||Sverige|YB|2002-12-11|2030-12-31|Ja|Nej
Ibrahima Chérif Fofana||Guinea|CM|2006-10-27|2030-12-31|Nej|Nej
Aaron Stoch Rydell||Sverige|YM|2006-10-14|2026-12-31|Ja|Nej
Kazper Karlsson||Sverige|CM|2005-03-21|2028-12-31|Ja|Nej"""
# Finns bara i fliken Effektiv trupp / Utlånade Spelare
EXTRA = """Diogo Tomas|33|Finland|MB|1997-07-31|2026-12-31|Nej|Nej
Henry Atola Meja||Kenya|ANF|2001-12-21|2026-09-01|Nej|Nej
Jere Uronen||Finland|YB|1994-07-13|2026-12-31|Ja|Nej"""
EFFEKTIV = {"Eskil Edh","Hervé Matthys","Sotirios Papagiannopoulos","Lukas Berquist","Martin Ellingsen","Amel Mujanic","Johan Hove","Linus Carlstrand","Charlie Pavey","Fredrik Nissen","Kristoffer Nordfeldt","Sixten Gustafsson","Mads Thychosen","Abdihakin Ali","Dino Beširović","Stanley Wilson","Adrian Helm","Andreas Redkin","Ibrahim Cissé","Linus Järeteg","Kevin Filling","Kalle Joelsson","Diogo Tomas","Norton de Carvalho Otterud","Taha Ayari","Yannick Geiger","Axel Kouame","Nana-Kofi Donkor"}
UTLANADE = {"Aaron Stoch Rydell","Emmanuel Gono","Henry Atola Meja","Jere Uronen","Kazper Karlsson"}
spelare = []
for block, in_total in ((TOTAL, True), (EXTRA, False)):
    for line in block.splitlines():
        n, nr, land, pos, fodd, slut, hf, aiku = line.split("|")
        spelare.append({"namn": n, "nr": int(nr) if nr else None, "land": land, "pos": pos, "fodd": fodd,
                        "kontraktsslut": slut, "hemmafostrad": hf, "aiku": aiku,
                        "total": in_total, "effektiv": n in EFFEKTIV, "utlanad": n in UTLANADE})
db = {"meta": {"version": 1, "uppdaterad": "2026-11-13T18:10:00Z", "mejl_kontrollerade_till": "2026-11-13",
               "kalla": "Import från Google-arket AIK Fotboll Trupp 2026-11-13"},
      "spelare": spelare,
      "logg": [{"datum": "2026-11-13", "namn": "", "typ": "import", "andring": f"{len(spelare)} spelare importerade från Google-arket", "kalla": "Google-arket AIK Fotboll Trupp", "mejl_id": ""}]}
json.dump(db, open("data/trupp.json", "w"), ensure_ascii=False, indent=1)
print(len(spelare), sum(s["total"] for s in spelare), sum(s["effektiv"] for s in spelare), sum(s["utlanad"] for s in spelare))
