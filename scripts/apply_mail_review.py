"""Rättningar efter genomgång av AIK Fotbolls pressmeddelanden 2023-11 – 2026-11 (gjord 2026-11-13)."""
import json
db = json.load(open("data/trupp.json"))
S = {s["namn"]: s for s in db["spelare"]}
logg = db["logg"]
def log(datum, namn, typ, andring, kalla, mid):
    logg.append({"id": f"{mid}-{sum(1 for e in logg if e.get('mejl_id')==mid)+1}", "datum": datum, "namn": namn, "typ": typ,
                 "andring": andring, "kalla": kalla, "mejl_id": mid})
def kontrakt(namn, ny, datum, kalla, mid):
    s = S[namn]; gammal = s["kontraktsslut"]; s["kontraktsslut"] = ny
    log(datum, namn, "rättning", f"Kontrakt {gammal} -> {ny}", kalla, mid)

kontrakt("Charlie Pavey", "2030-12-31", "2026-09-15", "AIK Fotboll förlänger med Charlie Pavey", "1a0a4b98831a984c")
kontrakt("Kevin Filling", "2029-08-31", "2026-09-03", "AIK Fotboll förlänger med Kevin Filling", "1a067c9241577809")
kontrakt("Filip Lukic", "2029-08-31", "2026-10-29", "Filip Lukic klar för AIK Fotboll", "1a188640f99d7af8")

S["Lukas Berquist"]["namn"] = "Lukas Bergquist"
log("2026-02-27", "Lukas Bergquist", "rättning", "Namn Berquist -> Bergquist", "Lukas Bergquist klar för AIK Fotboll", "19c9e8b089b3220a")

for n, d, k, m in [("Aziz Harabi", "2026-08-28", "AIK Fotboll värvar Aziz Harabi inför 2027", "1a048c8de8848dad"),
                   ("Ibrahima Chérif Fofana", "2026-11-04", "Ibrahima Chérif Fofana klar för AIK Fotboll", "1a1a6dc4d193e0f3")]:
    S[n]["fran"] = "2027-01-01"
    log(d, n, "rättning", "Kontraktet gäller från 2027-01-01", k, m)

S["Wilmer Olofsson"]["effektiv"] = True
log("2026-07-24", "Wilmer Olofsson", "återkomst", "Tillbaka från lån i Moss FK -> med i effektiv trupp", "Wilmer Olofsson tillbaka från utlåning", "19f93e3f4ec8404b")
S["Sebastian Hausner"]["effektiv"] = True
log("2026-08-31", "Sebastian Hausner", "rättning", "Inlånad från AC Horsens över 2026 -> med i effektiv trupp", "Sebastian Hausner lånas in över 2026", "1a059840e811667f")
S["Diogo Tomas"]["total"] = True
log("2026-08-01", "Diogo Tomas", "rättning", "Saknades i total trupp -> tillagd (avtal säsongen 2026 + option)", "Diogo Tomas till AIK Fotboll", "19fbc56bca51a07b")

for n, d, k, m in [("Jere Uronen", "2026-07-26", "Jere Uronen lämnar AIK Fotboll", "19f9eba2450c53d5"),
                   ("Henry Atola Meja", "2026-09-07", "Henry \"Meja\" Atola lämnar AIK Fotboll", "1a07b18f68548183")]:
    db["spelare"].remove(S.pop(n))
    log(d, n, "lämnar", "Borttagen ur utlånade (har lämnat klubben)", k, m)

NYA = [  # namn, land, pos, kontraktsslut, hemmafostrad, aiku, effektiv, datum, ämne, mejl_id, notering
 ("Lucas Assadi", "Chile", "CM", "2030-12-31", "Nej", "Nej", True, "2026-08-27", "Lucas Assadi klar för AIK Fotboll", "1a043bc8520ae383", "värvning, omgående transfer"),
 ("Oreoluwa Agbenla", "Nigeria", "CM", "2030-12-31", "Nej", "Nej", False, "2026-07-17", "Oreoluwa Agbenla klar för AIK Fotboll", "19f6f4e2cf87b9c7", "övergångsspelaravtal (akademin)"),
 ("David Oluwaseyi Oludase", "Nigeria", "YM", "2029-12-31", "Nej", "Nej", False, "2026-08-31", "David Oluwaseyi Oludase klar för AIK Fotboll", "1a058df61a269cb9", "övergångsspelaravtal (akademin)"),
 ("Robin Krügel", "", "CM", "2029-08-31", "Nej", "Nej", False, "2026-09-01", "Robin Krügel värvas till AIK Fotboll", "1a05ca0870ac53e5", "övergångsspelaravtal (akademin)"),
 ("Kalle Hagen", "Sverige", "MB", "2029-12-31", "Ja", "Ja", False, "2026-09-01", "Kalle Hagen skriver A-lagskontrakt", "1a05dea24b4c433f", "övergångsspelaravtal, från AIK U"),
 ("Muslim Adamovich Sultygov", "", "ANF", "2029-12-31", "Nej", "Ja", False, "2026-07-02", "Muslim Adamovich Sultygov skriver A-lagskontrakt", "19f21a1034342603", "övergångsspelaravtal, från AIK P19"),
 ("Mohammed Shilla", "Tanzania", "", "2030-12-31", "Nej", "Nej", False, "2026-01-25", "Mohammed Shilla klar för AIK Fotboll", "19bf4990a5cfcc54", "övergångsspelaravtal (akademin)"),
 ("Nikolaj Staykov", "", "ANF", "2029-12-31", "Nej", "Nej", False, "2025-10-14", "Nikolaj Staykov till AIK Fotboll", "199e297d0573ae36", "övergångsspelaravtal (akademin)"),
 ("Tinde Teribe", "", "", "2029-12-31", "Nej", "Nej", False, "2025-10-14", "Tinde Teribe skriver avtal med AIK Fotboll", "199e229e610ce892", "övergångsspelaravtal (akademin)"),
]
for n, land, pos, slut, hf, aiku, eff, d, k, m, note in NYA:
    s = {"namn": n, "nr": None, "land": land, "pos": pos, "fodd": "", "kontraktsslut": slut, "hemmafostrad": hf, "aiku": aiku,
         "total": True, "effektiv": eff, "utlanad": False}
    db["spelare"].append(s); S[n] = s
    log(d, n, "värvning", f"Tillagd ({note}), kontrakt t.o.m. {slut}", k, m)

db["meta"].update({"version": 2, "uppdaterad": "2026-11-13T19:30:00Z", "mejl_kontrollerade_till": "2026-11-13",
                   "granskning": "Kontrollerad mot AIK Fotbolls pressmeddelanden 2023-11-13 – 2026-11-13"})
json.dump(db, open("data/trupp.json", "w"), ensure_ascii=False, indent=1)
sp = db["spelare"]
print(len(sp), sum(s["total"] for s in sp), sum(s["effektiv"] for s in sp), sum(s["utlanad"] for s in sp), len(logg))
