"""Sida (vänster/höger) för ytterbackar/yttrar där AIK:s pressmeddelanden anger den."""
import json
db = json.load(open("data/trupp.json")); S = {s["namn"]: s for s in db["spelare"]}
def setpos(n, ny, datum, kalla, mid):
    s = S[n]; old = s["pos"]; s["pos"] = ny
    db["logg"].append({"id": f"{mid}-pos", "datum": datum, "namn": n, "typ": "rättning", "andring": f"Position {old} -> {ny}", "kalla": kalla, "mejl_id": mid})
setpos("Aziz Harabi", "VB", "2026-08-28", "AIK Fotboll värvar Aziz Harabi inför 2027 (\"vänsterbacken\")", "1a048c8de8848dad")
setpos("Mads Thychosen", "HB", "2025-01-10", "Mads Thychosen förlänger med AIK Fotboll (\"högerbacken\")", "194515fc5bf0cc9d")
setpos("Nana-Kofi Donkor", "VM", "2026-08-06", "Nana-Kofi Donkor ansluter till AIK Fotboll (\"vänstermittfältaren\")", "19fd6845abee83b5")
db["meta"]["uppdaterad"] = "2026-11-13T20:00:00Z"
db["meta"]["positionskoder"] = {"MV": "Målvakt", "VB": "Vänsterback", "HB": "Högerback", "YB": "Ytterback (sida okänd)", "MB": "Mittback",
  "CM": "Central mittfältare", "VM": "Vänstermittfältare", "HM": "Högermittfältare", "YM": "Yttermittfältare (sida okänd)", "ANF": "Anfallare"}
json.dump(db, open("data/trupp.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter; print(Counter(s["pos"] for s in db["spelare"] if s["total"]))
