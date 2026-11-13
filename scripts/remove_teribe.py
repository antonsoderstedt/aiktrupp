import json
db = json.load(open("data/trupp.json"))
db["spelare"] = [s for s in db["spelare"] if s["namn"] != "Tinde Teribe"]
db["logg"].append({"id": "manuell-2026-11-13-teribe", "datum": "2026-11-13", "namn": "Tinde Teribe", "typ": "lämnar",
                   "andring": "Borttagen: har inte längre kontrakt med AIK", "kalla": "Uppgift från Anton", "mejl_id": ""})
db["meta"]["uppdaterad"] = "2026-11-13T20:30:00Z"
db["meta"]["falt"] = {"pos": "huvudposition", "pos_ovr": "lista med övriga positioner (valfri)"}
json.dump(db, open("data/trupp.json", "w"), ensure_ascii=False, indent=1)
print(len(db["spelare"]))
