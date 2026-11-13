# AIK-trupp – dagligt uppdateringsjobb

Ett schemalagt Claude-jobb körs varje kväll 20:47 (Stockholm). Det läser nya pressmeddelanden från
"AIK Fotboll" <mail@distribution.cision.com> i Gmail och uppdaterar truppdatabasen (`trupp.json`)
som är kopplad till dashboarden "AIK Herr-A – Truppöversikt".

- Databasen: JSON-fil i dashboarden (`spelare`, `logg`, `meta`). `data/trupp.json` här är startimporten.
- Startimport: `scripts/seed_from_sheet.py` (från Google-arket AIK Fotboll Trupp, 2026-11-13).
- Varje ändring loggas i `logg` med pressmeddelandets ämne och mejl-id och visas på dashboarden.
