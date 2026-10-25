# Sistem za pronalaženje klijenata (Stefan, izrada sajtova)

Ovo je uputstvo koje Claude prati svakog radnog dana. Sve se radi kroz Claude in Chrome (Stefanov Chrome, WhatsApp Web na novom broju) i ovaj repo.

## Pravila poruka (obavezno)
- Srpski, latinica, ekavica, persiranje ("vi").
- Bez crtica (— i –) i bez " - " u tekstu. Ne zvučati kao AI, ne previše formalno.
- Ne pominjati prethodne projekte. Ne lagati: svaka tvrdnja o sajtu mora biti proverena (domen ne postoji, sajt se ne otvara, zastareo izgled...).
- Uvek personalizovano: ime firme, mesto, nešto iz Google recenzija (ime majstora, šta ljudi hvale) i konkretan problem njihovog sajta.
- Nedeljom početi izvinjenjem što se piše nedeljom. Ne slati za vreme izbora ili praznika ako Stefan kaže.
- Struktura: pozdrav i ko sam (Stefan, iz Obrenovca kad je firma iz okoline), šta sam primetio na sajtu, "napravio sam primer, evo slike", poziv bez pritiska.

## Ko se NE kontaktira
- Auto škola Start, Kafeterija Mlin, Foto studio Lazarević (060 1499117), sačuvani kontakti.
- Klima firme (konkurencija klijenta Pro Klima): TN-Frigo, Delta Frigo, Team Mont Plus, SZTR Termomontaža i ostale firme za kućne klime.
- Stomatolozi (Stefan: imaju dovoljno posla).
- Svako ko je već u `data.json` (proveri po broju telefona, poslednjih 8 cifara).
- Nikad dva puta isti broj. Posle greške ili prekida prvo otvori čet i proveri.

## Ciljna grupa
Firme koje VEĆ imaju sajt, ali je loš: domen ne postoji (NXDOMAIN), "Account Suspended", sajt se ne otvara, zastareo dizajn, stock slike, slika koja nema veze sa firmom. Najbolje: link do mrtvog sajta stoji na Google mapama. Prvi pravi klijenti (Pro Klima, Boškova voda) bili su upravo ovakvi.
Dobre delatnosti: auto servisi, šlep, PVC/ALU stolarija, roletne, nekretnine, selidbe, smeštaj, sale, građevina. Prvo Obrenovac i okolina, pa Beograd i veći gradovi.

## Dnevni tok (5 do 8 poruka dnevno, radnim danima)
1. **Odgovori prvo.** U WhatsApp Web listi četova pročitaj sve gde poslednja poruka nije naša. Topli kontakti (traže primer, cenu) su prioritet. Javi Stefanu svaki odgovor. Ne pregovaraj o ceni sam.
2. **Pretraga.** Google Maps u Chrome-u: `python3 sistem/mb.py <tab> "upit 1" "upit 2"` daje browser_batch. Ekstraktor (`maps_extract.js`) čuva rezultate u `localStorage.sl` na google.com (ime, sajt, mobilni, ocena, broj recenzija). Čitaj u delovima od 950 znakova (izlaz alata se seče na oko 1000 znakova). Upiši upite u `sistem/pretrage.txt` da se ne ponavljaju.
3. **Izbaci duplikate** prema `data.json` i `sistem/kontakti.json` (poslednjih 8 cifara broja).
4. **WhatsApp provera PRE svega ostalog.** `https://web.whatsapp.com/send?phone=381XXXXXXXX`, čekaj 15 s, dijalog "isn't on WhatsApp" znači nema WA. Stariji majstori često imaju samo Viber: njih zapiši kao "Viber (ručno)", Stefan im šalje sa telefona.
5. **Provera sajta.** DNS: otvori `https://dns.google/resolve?name=DOMEN&type=A` i fetch iz te stranice za više domena (Status 3 = domen ne postoji). Živi sajtovi: otvori, screenshot na 0.3 do 0.4, zapiši 1 do 3 konkretna problema. Ne tvrdi ništa što nisi video.
6. **Detalji za personalizaciju.** Google Maps kartica: adresa, ocena, broj recenzija, 5 do 8 recenzija (ime majstora, šta hvale).
7. **Primer nove naslovne.**
   - Mrtav ili loš sajt bez dobrih fotografija: `sistem/danas.json` (polje `mock`, `kind`: auto | pvc | nekretnine) pa `cd sistem/mockup && npm i && python3 render.py ../danas.json`. Slike idu u `/mnt/user-data/outputs/mockups/`, kopiraj ih u `mockups/` u repou, commit i push.
   - Sajt sa dobrim fotografijama: napravi HTML stranicu sa njihovim slikama (relativne putanje sa njihovog domena), `python3 sistem/mockup/inplace/wrap.py strana.html domen`, sačuvaj kao `*-wrap.html`, push, pa u Chrome tabu na NJIHOVOM domenu: `fetch(raw.githubusercontent.com/.../<commit-sha>/...)` i `document.write`. Tako se njihove slike učitaju same. Ovo daje najbolje primere.
   - Uvek pogledaj sliku pre slanja (Read na jpg ili screenshot).
8. **Slanje (slika + tekst u jednoj poruci).** `sistem/tabs.json` sadrži id tabova (wa, img). Za svaku firmu:
   - `python3 sistem/wa_img.py prep "<ime>"` daje batch: otvara sliku u img tabu i pravi PUN screenshot (bez `scale`, inače se šalje mutna slika), otvara čet, proverava broj u zaglavlju i da u četu nema poruka, otvara "Photos & videos" input (presretanjem `HTMLInputElement.click`, da se ne otvori prozor za fajlove).
   - `find` "file input elements" pa uzmi DRUGI ref (prvi je za nalepnice, sticker!).
   - `upload_image` sa id-jem screenshota i tim ref-om (mora pisati oko 70 KB ili više).
   - `python3 sistem/wa_img.py send "<ime>"` daje JS koji nalepi tekst u polje za opis, proveri da je upisan, klikne "Send 1 selected" i proveri da je poslato.
   - Raw linkovi uvek sa commit sha (raw.githubusercontent.com/.../main se kešira 5 min).
   - Pre screenshota slike ne klikći po img tabu (kursor ostaje na slici).
9. **Upis.** Dodaj firme u `sistem/kontakti.json` (status, datum, `followup` za 4 dana), pokreni `python3 gen.py` i build iz README, objavi artifact "Lista klijenata", commit i push.
10. **Podsetnik.** Posle 4 radna dana bez odgovora, jedna kratka poruka u jednom redu (npr. "Dobar dan, samo da proverim da li ste stigli da pogledate primer 🙂"). Samo jednom.
11. **Izveštaj Stefanu.** Koliko je poslato i kome, ko nema WhatsApp (spremno za Viber), svi odgovori (topli kontakti na vrhu).

## Fajlovi
- `data.json` / `gen.py` / `template.html`: lista klijenata (artifact https://claude.ai/artifact/N8mJd2pdLKhZ6wYM1YDAd3).
- `sistem/kontakti.json`: kontakti iz novog sistema (od 25.10.2026).
- `sistem/danas.json`: radni fajl za današnju turu (mock podaci i poruke).
- `mockups/`: gotove slike (javno, samo javni podaci firmi).
- `waq.json`, `rec.py`, `nb.py`: stari red generičkih poruka (pauziran 25.10.).
