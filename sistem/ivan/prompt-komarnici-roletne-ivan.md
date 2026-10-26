# Prompt za Claude Code: sajt "Komarnici i Roletne Ivan"

Kopiraj sve ispod linije u Claude Code, u praznom folderu projekta.

---

Napravi kompletan, produkcijski spreman sajt za firmu **Komarnici i Roletne Ivan** iz Beograda. Sajt treba da bude brz, odlično SEO optimizovan za lokalne pretrage i da deluje premijum, kao da ga je radio iskusan dizajner i programer, a ne šablon ili AI. Ovaj sajt će vlasnik videti pre nego što odluči da li ga kupuje, zato svaka sitnica mora biti urađena kako treba.

## 0. Pre nego što počneš

1. Učitaj i koristi skill/plugin **frontend-design** za sve dizajnerske odluke. Ako imaš i **design** plugin, iskoristi ga za proveru dizajna na kraju.
2. Proveri da li su dostupni MCP serveri. Ako nisu, dodaj ih:
   ```
   claude mcp add playwright -- npx @playwright/mcp@latest
   claude mcp add context7 -- npx -y @upstash/context7-mcp
   ```
   Playwright koristiš za screenshotove i proveru sajta u browseru (desktop i telefon), a Context7 za aktuelnu dokumentaciju (sharp, Vercel, schema.org) kad ti zatreba.
3. Prvo napravi plan (struktura fajlova, sekcije, dizajn sistem), pokaži mi ga ukratko i odmah kreni da radiš, ne čekaj odobrenje.

## 1. Tehnički okvir

- Čist **HTML + CSS + vanilla JS**, bez frameworka, bez jQuery-ja, bez Bootstrap-a i Tailwind CDN-a. Statičan sajt koji može odmah na **Vercel** i na **GitHub Pages**.
- Više HTML stranica zbog SEO-a (svaka usluga ima svoju stranicu i svoj naslov za Google):
  ```
  /index.html                 naslovna
  /komarnici/index.html       komarnici po meri (svi tipovi)
  /roletne/index.html         aluminijumske roletne (svi tipovi)
  /servis/index.html          servis i popravke (komarnici, roletne, štelovanje stolarije, popravka prozora i vrata)
  /kontakt/index.html         kontakt, mapa, forma
  /404.html
  /assets/css/style.css       jedan CSS fajl, mobile first
  /assets/js/main.js          jedan mali JS fajl, defer
  /assets/img/...             optimizovane slike
  /assets/fonts/...           self-hosted woff2 fontovi
  /robots.txt, /sitemap.xml, /site.webmanifest, favicon set
  /vercel.json
  /scripts/                   pomoćne skripte (preuzimanje i obrada slika)
  ```
- Zajednički header i footer drži doslovno isti na svim stranicama (nema build alata, pa pazi da linkovi budu tačni i relativni ili apsolutni od korena).
- Jezik: `<html lang="sr-Latn">`, srpski latinica, ekavica, persiranje ("vi").

## 2. Podaci o firmi (koristi SAMO ove, ništa ne izmišljaj)

- **Naziv:** Komarnici i Roletne Ivan (na starom sajtu stoji i "Komarnici i roletne Beograd" / "Komarnici-Roletne Servis Beograd")
- **Vlasnik i majstor:** Ivan
- **Adresa:** Dimitrija Tucovića 119, 11050 Beograd
- **Telefon:** +381 60 193 0660 (prikaz: 060 193 0660)
- **Email:** ivan.mijatovic.1984@gmail.com
- **Domen:** komarnici-roletneservis.rs
- **Google:** ocena 5,0 iz 121 recenzije
- **Radno vreme po Google-u:** radi do 23:30. Tačan raspored po danima NE znamo, zato ga ne ispisuj po danima, napiši "Pozovite ili pošaljite poruku, javljamo se brzo" i ostavi TODO komentar u kodu.
- **Viber i WhatsApp:** isti broj. Na starom sajtu stoji: "Slikajte kvar i pošaljite nam fotografiju na Viber ili WhatsApp." Ovo je odlična stvar i treba da bude istaknuta.
- **O nama (sa starog sajta):** "Nudimo kvalitetnu izradu i ugradnju aluminijumskih komarnika i roletni svih tipova. Pored izrade i ugradnje komarnika i roletni, obezbeđujemo i usluge servisa i štelovanja stolarije bilo koje vrste."

### Komarnici (sa starog sajta)
- Rade se od kvalitetnih aluminijumskih profila sa mrežicama željenog tipa.
- Tipovi: **Rolo klasik**, **Rolo sa završnom lajsnom**, **Plise (harmonika)**, **Fiksni spoljni**, **Fiksni unutrašnji**.
- Rolo komarnici su najtraženiji: jednostavni za ugradnju i održavanje, a kad se ne koriste mrežica se podigne i urola u kutiju, pa ne smeta i duže traje.
- Boje: bela, antracit, braon. Boja može da se uklopi sa stolarijom.

### Roletne (sa starog sajta)
- Aluminijumske roletne od profila najvišeg kvaliteta, sa čepovanim lamelama punjenim poliuretanskom penom. Čepovi štite od prodora vode, a pena daje termo izolaciju i tiši rad pri spuštanju i podizanju.
- Tipovi: **Rondo sa zaobljenom kutijom**, **sa petougaonom kutijom**, **sa gurtnom (trakom)**, **sa kanapom**, **sa elektro motorom**.
- Boje: bela, antracit (tamnija siva), braon.

### Servis (sa starog sajta)
- Popravka prozora i vrata, servis komarnika, servis roletni, servis i štelovanje stolarije bilo koje vrste.
- Iz recenzija: popravka pale roletne, zamena kaiševa (gurtni).
- Ivan je na Google profilu objavio: "Spremite se za košavu na vreme! Zviždi vam vetar kroz prozor jer roletna ne može do kraja da se spusti? Gurtna je pri kraju..." Iskoristi tu temu (štelovanje pred zimu, zamena gurtne) na stranici servisa.

### Cenovnik (sa starog sajta)
- Cene komarnika su **na upit**, izražavaju se po metru kvadratnom i odnose se na belu boju. **Antracit i braon se doplaćuju 2 evra po m².**
- Cene popravke, servisa i štelovanja se znaju kada se ustanovi kvar, na terenu ili na osnovu opisa ili slike kvara.
- Ne izmišljaj nikakve cene u evrima. Umesto tabele sa ciframa napravi lep blok "Kako se formira cena" sa ova tri pravila i dugmetom "Pošaljite mere ili sliku za ponudu".

### Prave Google recenzije (prepisane na latinicu, koristi ih doslovno, ime + inicijal prezimena)
1. **Tatjana D.:** "Majstor je ugradio komarnike u našem stanu po meri i uskladio boju sa prozorima po odličnoj ceni. Za veoma kratko vreme izašao je na teren da meri prozore i brzo je ugradio komarnike. Brza i kvalitetna usluga. Veoma ljubazan, fin, prijatan čovek koji ima razumne savete u vezi sa zamenom roletni i drugim popravkama po stanu. Srdačno preporučujem!"
2. **Milutin S.:** "Izuzetno stručan i profesionalan gospodin Ivan. Svaki problem zna da praktično reši. Za svaku preporuku."
3. **Olga K.:** "Brzo je došao, popravio sve što je trebalo popraviti, držao se svoje cene, čak je stavio higijenske navlake za cipele kada je ušao u stan. Svaka pohvala!"
4. **Dijana D.:** "Brza i efikasna montaža, Ivan je sve završio pre nego što sam mu čak i ponudila kafu, a ne i napravila. Sve preporuke, a mi ćemo ga ponovo pozvati za druge prozore i vrata kada bude potrebno."
5. **Saša M.:** "Brzo, efikasno i povoljno. Dogovor lak a majstor odradio sve što je trebalo bez ikakvih problema. Imali smo popravku pale roletne i zamenu kaiševa. Sada je sve tip top. Preporuka!"
6. **Bojana R. Č.:** "Profesionalno obavljen posao. Veoma brza i laka komunikacija. Ivan se čak prilagodio našim planovima za odmor, tako da je sve instalirano onako kako nam je najviše odgovaralo. Toplo preporučujem!"
7. **Marija P.:** "Odlična saradnja, brz dogovor, završeno pre dogovorenog roka. Toplo preporučujem!"
8. **Marina R.** (na engleskom, može kao kraći citat): "Efficient, professional. Prompt response. Clean and tidy."

Uz recenzije stavi jasan link "Pogledajte svih 121 recenziju na Google-u" (link ka Google Maps pretrazi: `https://www.google.com/maps/search/?api=1&query=Komarnici+i+Roletne+Ivan+Dimitrija+Tucovi%C4%87a+119+Beograd`).

## 3. Fotografije (prave fotografije njegovih radova sa Google profila)

Ne koristi nijednu stock fotografiju, ilustraciju ni AI sliku. Koristi isključivo ove prave fotografije. Napravi skriptu `scripts/fetch-images.mjs` koja ih preuzme (Node 18+, `fetch`), sačuva originale u `scripts/raw/` i zatim ih sa **sharp** (`npm i -D sharp`) obradi u `assets/img/`:
- formati AVIF i WebP, plus JPG kao fallback,
- širine 480, 800, 1200, 1600 (za hero i 2000),
- ime fajla opisno, na srpskom bez dijakritika (npr. `plise-komarnik-drveni-prozor-800.avif`),
- skini EXIF podatke.

Osnovni URL: dodaj prefiks `https://lh3.googleusercontent.com/` i sufiks `=w2400` na svaki ID.

| # | ID | Šta je na slici | Upotreba |
|---|----|----|----|
| 4 | `gps-cs-s/ANWiy9TBThRND6m0r0i5gpi8OGzXzQPGNlK-_z-i_W5Oa3WBRq9dtlddFSxUwES38oRJYr_uA4iy8Bofdpjww6YiQl9haWZe1whBsvMhcCR8pKpqjX4FGQrmP8AlBSzpjqhsxqisD6pHH2x23I8` | plise komarnik na prozoru sa drvenim okvirom, unutrašnjost | **HERO naslovne** |
| 11 | `gps-cs-s/ANWiy9QvZngke-viSUUnmBKfgdQiRuAn6oMzwLRGWJKPQhevPgkY2NgdIEbxyUvoK-tqGHKexjG1sawz3oaaK31ZhB2zkUIbxGiDMWJDkxsSiCoN2_YteP6tIgHQEtiGamRdt22ghNF8KlRzzGsM` | pogled sa terase na grad kroz komarnik | hero stranice Komarnici ili veliki vizual |
| 0 | `gps-cs-s/ANWiy9QOtRULEBzPRnvBWay8MNiVxI4QQH01aeHI2f-6kvrleTqJwqOWueZdokS6vdfSfGmLDDR5S_jl3GBsWNem5XwSwWPoP3G0wRIptH-tSU2GsyBiCo2iNCj1qppfHAP3UkZwTMivAWw0kDc` | komarnik na vratima, fasada od cigle | komarnici za vrata |
| 3 | `gps-cs-s/ANWiy9T_24g1iezmigvaZ3j4PtobaNcXnDg1ePPSZgozNSzS5rvwEPMM_W0UIf_TICZprmEri_NC2ksDcM5I2VR-Txo6nupKAsUZZ6sXgRpYj-05LvoMj_qrFkVRVC-ZtGmIs8WwrAlUZtn8A144` | komarnik na balkonskim vratima, cveće | komarnici, galerija |
| 5 | `gps-cs-s/ANWiy9QG4E1Q74IokTIwTkqTAPIW-dV67quGwN1oEIInxH_9NCvEdPrgFskUrplZTVprV1T0clH_FKcBfYZgfGh_RrXDqd3B2BpBjQ2Lj-WH1Miap3fmKmrM_r0Q6XbbHfdx6VtljLYTFwE9HjiD` | komarnik u tamnom (antracit) okviru na vratima | boje, galerija |
| 6 | `gps-cs-s/ANWiy9TUMZ3jGzzx3RJ0-5DTDH9HJZ-iWVyG5g9NB2X5EAD7LMLr3xpngTl9DImbxFxXBq0gTJUqQCoxU4keb_LjFV0SLqBKRUR1dil3w2mYiFo29qEZv9vogYv0vytOCnBntI4GreVyWzSROt1U` | ALU profil i mrežica na stolu, izrada | sekcija "Sami pravimo" / proces |
| 7 | `gps-cs-s/ANWiy9Siz7HgrYrx7-Y2c7DdzlxMhAT2BNK4CO92YgGWml6SS9tRtsEXlx0NkDAKdPlcBksMFSP6M4EONc1vLRi7gVC4v2rx5ch0rHNr_FWrvrMr0nD5EemnwR-upOTCKCCs0jaNxVKawuUyVxra` | beli komarnik na prozoru, spolja | fiksni komarnik, galerija |
| 8 | `gps-cs-s/ANWiy9RuDfBnoXMJcnWhaX9M6-kX7yZc7-5L3LvWMOvzmAh-HI647hQKNbxIOMy8_v3b8enjKvLd92mRnAaKc9yGQzifjypW2cz_BIz5-fjezNjE_NeDsaEVlqLgI_PMbKzEA828L7bBB8T7WuM` | beli okvir sa mrežicom, unutra | galerija |
| 9 | `gps-cs-s/ANWiy9SgHhCQdl_WJ3TPPodW4JkuzlrgRqAOT312l3k1fCKfS9XMs7otreGbdvGvyFa-kyATT8tLdtx006eS8ndgodHuzHt9Q85kWHM3UjvsQY7DyLsUJ3tBKjcliknqgy9K5DTmI8VI9wQDsp-0` | plise komarnik pored drvenih vrata | plise, galerija |
| 10 | `gps-cs-s/ANWiy9RI6u0IBoGcgb_yrx9qZGfjLpVCX84GD8Y2EMsgCZAYAttDpn_igPOnH8c2671HyzqsxE4lTCwbMidcCow6MxHyltizRpqn7rxEK256XpLegrNHFq-2FbnozzL01mQ2iWB6TaxyVs5dBDU` | bela mrežica, detalj | galerija |
| 12 | `gps-cs-s/ANWiy9SEWD0L4BXXXc7sX5dbWzp_6YpbM8ZkAHErkzHewC8uuOGzPcxBd8-zG2ZwwdwfDiweP3b8FunzCTyeKs2wuumYy8l0yw6lqYUb32hciVYwIm6iNJ-WdcQ9jLwO1-oVaVV_c48xtywBL85-` | tamne roletne na terasi | **hero stranice Roletne** |
| 1 | `gps-cs-s/ANWiy9S6xeqnPzhIPopvZXlTeyyMPAsaZ0uVyD7PaT1cdXTcDtgBerSQpLuYI_BC7dD5PpbB-MHQl13OGEk7XjZ4vZA8vrj8_83Sc-YHKvABEhtcVQzQS1MCAbhdDgfdnXAc3VhgzV6kdRS9HsI` | kutija roletne i gurtna, unutra | servis (zamena gurtne) |
| 2 | `gps-cs-s/ANWiy9TkhwP28Bt7WagYcik3f4ZjaJUJHDxIFgUT_okWmFMjWG4qXZ83m5MLjnZbyRK5kdNT_hmPzF-98QnBwi_gQpE_hrOsaoH5bH2uakGF8tv6g0hvC274LQBcz9BgUYYquj4ivnOSgS7HWn3y` | popravka, na slici piše "Može se popraviti i ovako" | servis, iseci deo bez teksta ili preskoči |
| 13 | `gps-cs-s/ANWiy9SQ393a2pQlXzwtqK9y4_3BaijxNR2jJy-YYLPTCWs6Is4duCK6FLEkTHinyRpo4kSIu86DncS6u5dZ3zhbmChqVRAmT8PJygcJcgqfzoX8V3pBSjNCApWAi1Ra4ImP1EIqtqOr64A5T3mg` | reklamna grafika sa tekstom | NE koristi |
| 14 | `gps-cs-s/ANWiy9R-MGWCgjd1lM6yn3JvtG1adQZruLX8OeVXhZV1aMIAaT4ccMidE9U-TEW_pbAfVmqY9pD4BgHZ342YjkHj0mM1nwCC_zuV5xTA21Y2BJptONbBuSSK7OOZM5VE0yJKVlMoui9ALE8oHqXh` | nejasno | pogledaj, verovatno ne koristi |
| 15 | `gps-cs-s/ANWiy9RSPBKIKhJ7b3K_KN0lnhhzjVvwN_4vnaJzOoLSifPTDISUgcPle_WXDd6zjMwK1jyoDt5LjZj50SxsRgEMNEPs6OKudt2vBTXQeTR0ClgGLmnoRuf3YtSDpQGahiU8_c-1rlSMUEX_wUo` | nije vezano za posao | NE koristi |

Posle preuzimanja **pogledaj svaku sliku** (Read na fajl) i potvrdi da opis odgovara. Ako je neka mutna ili loše kadrirana, ne koristi je. Slike nisu profesionalne, pa ih ujednači: blago podigni kontrast i oštrinu sa sharp (`modulate`, `sharpen`), ali bez filtera koji menjaju boje. Kadriraj ih tako da linije prozora budu prave.

Ako ti treba još fotografija, profil ima 39 slika. Otvori Playwright na `https://www.google.com/maps/search/Komarnici+i+Roletne+Ivan+Beograd`, klikni na firmu pa na "Prikaži slike" i pokupi `lh3.googleusercontent.com/gps-cs-s/...` linkove.

## 4. Dizajn: pravac i pravila

Ovo je zanatska firma jednog majstora koga ljudi hvale za tačnost, čistoću i preciznost. Sajt treba da prenese **preciznost po meri** i **mir i svež vazduh u stanu**, a ne "jeftino i brzo".

**Paleta:**
- Grafit `#1D2422` (tekst, tamne površine)
- Topla bela `#F4F3EF` (pozadina)
- Čista bela `#FFFFFF` (kartice i forme)
- Šumsko zelena `#2D6A4F` (jedini akcenat: dugmad, linkovi, ikonice)
- Siva za sporedni tekst `#56605B`
- Tri boje profila kao stvarne boje proizvoda, koristi ih samo u biraču boja: bela `#F2F2EE`, antracit `#3B3F42`, braon `#5A3E2B`

**Tipografija (self-hosted woff2, subset latin + latin-ext zbog č, ć, š, ž, đ):**
- **Archivo** za naslove (700 do 800, malo zbijen razmak slova) i za tekst (400 i 600). Preuzmi sa `@fontsource/archivo` ili Google Fonts, stavi u `/assets/fonts`, `font-display: swap`, preload samo za fajl koji treba za hero naslov.
- Tipografska skala po principima "The Elements of Typographic Style": osnova 18px na desktopu, 16px na telefonu, odnos oko 1.25, linija teksta do 70 karaktera, `line-height` 1.55 za tekst.

**Motiv koji se pamti (samo jedan):** fina mreža kao mrežica komarnika. Suptilan SVG uzorak (tanke linije, 6 do 8 px korak, providnost oko 6%) koji se koristi na samo dva mesta: iza hero fotografije kao "okvir" i u bloku za poziv na akciju. Nigde drugde.

**Izbegni ove AI šablone:**
- krem pozadina sa terakota akcentom, tamna pozadina sa neon zelenim akcentom,
- svi sadržaji sečeni u identične kartice sa istim zaobljenjem i senkom,
- velika natpisna slova (ALL CAPS) iznad svakog naslova,
- numeracija 01 / 02 / 03 osim tamo gde je stvarno redosled (proces rada jeste redosled, tu je ok),
- jedna reč u naslovu obojena drugom bojom ili u kurzivu,
- strelica "→" na kraju dugmadi, srednja tačka "·" između stavki,
- fade-in animacija na svakoj sekciji.

**Pokret:** samo jedan orkestriran trenutak, pri učitavanju hero sekcije (naslov, tekst i fotografija se pojave u kratkom nizu, ukupno ispod 700 ms). Sve ostalo bez animacija, osim reakcije na korisnika (hover na dugmetu, otvaranje FAQ-a, lightbox). Poštuj `prefers-reduced-motion`.

## 5. Naslovna stranica, sekciju po sekciju

1. **Header:** levo naziv "Komarnici i roletne Ivan" kao tekstualni logo (Archivo 800, "i roletne" u zelenoj je jedini izuzetak od pravila o bojenju jer je deo naziva), linkovi Komarnici, Roletne, Servis, Kontakt, desno dugme "060 193 0660" (`tel:+381601930660`). Na telefonu hamburger meni koji radi i tastaturom.
2. **Hero (split, kao na primeru koji je vlasnik video):** levo naslov "Komarnici i roletne po meri vašeg prozora", ispod: "Izrada, ugradnja i popravka u Beogradu. Dođemo na merenje, a boju uskladimo sa vašom stolarijom." Dva dugmeta: "Zakažite merenje" (otvara kontakt formu) i "Pošaljite sliku na WhatsApp" (`https://wa.me/381601930660?text=...` sa unapred upisanim tekstom "Dobar dan, želeo bih ponudu za..."). Ispod: "5,0" i pet zvezdica, "121 recenzija na Google-u". Desno velika fotografija #4 sa zaobljenim uglovima, a preko donje leve ivice bela kartica sa citatom Milutina S. Iza fotografije suptilna mreža (motiv).
3. **Traka poverenja (jedan red, bez kartica):** "Merenje na vašoj adresi", "Boja po izboru: bela, antracit, braon", "Pošaljite sliku kvara na Viber ili WhatsApp", "Popravljamo i ono što drugi ne žele".
   Proveri četvrtu stavku: ako zvuči kao izmišljotina, zameni je sa "Aluminijumski profili i kvalitetne mrežice".
4. **Tri usluge:** Komarnici, Roletne, Servis i popravke. Ovo NE sme biti tri ista kartice. Uradi asimetričan raspored: Komarnici zauzimaju veći deo (fotografija #11 ili #3), Roletne i Servis manji (fotografije #12 i #1). Svaka ima kratak opis sa starog sajta i link na svoju stranicu.
5. **Tipovi komarnika:** interaktivni izbor (tabovi ili lista levo, sadržaj desno) za Rolo klasik, Rolo sa završnom lajsnom, Plise, Fiksni spoljni, Fiksni unutrašnji. Za svaki jedna ili dve rečenice: šta je i kad je dobar izbor. Tekstove izvedi iz podataka sa starog sajta i iz opštih, proverljivih činjenica o tim tipovima. Bez izmišljenih brojeva.
6. **Birač boje profila:** tri kružića (bela, antracit, braon), klik menja fotografiju ili okvir. Ispod: "Bela je osnovna. Antracit i braon se doplaćuju 2 € po m²."
7. **Kako radimo (ovo je stvarni redosled, numeracija je ok):** 1. Pozovete ili pošaljete sliku na Viber ili WhatsApp. 2. Ivan dođe na merenje i dogovorite tip i boju. 3. Izrada i ugradnja, a stan ostaje čist (iz recenzije o navlakama za cipele). Uz korak 3 fotografija #6 (izrada).
8. **Galerija radova:** 8 do 10 pravih fotografija, raspored nalik masonry gridu sa različitim veličinama, lazy loading, lightbox na klik (sopstveni, mali, dostupan tastaturom: Esc zatvara, strelice listaju, fokus ostaje unutar).
9. **Recenzije:** izaberi 4 najjače (Tatjana D., Olga K., Dijana D., Saša M.), velik citat jedne i manji ostale, link ka svim recenzijama na Google-u. Bez lažnih avatara, samo ime i inicijal.
10. **Kako se formira cena:** tri pravila iz cenovnika, dugme "Zatražite ponudu".
11. **Česta pitanja (FAQ):** samo pitanja na koja imamo istinit odgovor iz podataka:
    - Da li dolazite na merenje? (Da, na vašu adresu u Beogradu.)
    - Koje boje komarnika i roletni imate? (Bela, antracit, braon. Doplata 2 € po m² za komarnike u boji.)
    - Mogu li da pošaljem sliku kvara? (Da, na Viber ili WhatsApp, 060 193 0660.)
    - Popravljate li i roletne koje niste vi ugradili? (Servis roletni, komarnika i stolarije bilo koje vrste.)
    - Koliko košta komarnik? (Cena po m², zavisi od tipa i boje, ponuda odmah po merama.)
    Ne pravi pitanja o garanciji i rokovima izrade dok vlasnik ne potvrdi (stavi ih u TODO listu).
12. **Kontakt blok + forma "Zatražite ponudu":** polja Ime, Telefon, Usluga (izbor), Mere ili opis, opcionalno "Mogu da pošaljem sliku". Pošto je sajt statičan, forma na submit sastavlja lepu poruku i otvara WhatsApp (`wa.me`) sa tim tekstom. Pored toga ponudi i "Pošalji emailom" (`mailto:` sa istim tekstom). Validacija na klijentu, jasne poruke o greškama.
13. **Mapa:** NE ugrađuj Google Maps iframe odmah (usporava sajt). Napravi "facade": statična slika ili stilizovan blok sa adresom i dugmetom "Prikaži mapu" koji tek na klik učita iframe. Plus link "Otvori u Google mapama".
14. **Footer:** NAP (naziv, adresa, telefon) identičan kao na Google profilu, email, linkovi stranica, "© 2026 Komarnici i Roletne Ivan". Ništa o tome ko je napravio sajt.
15. **Sticky traka na telefonu:** dole dva dugmeta "Pozovite" i "WhatsApp", pojavljuje se kad korisnik skroluje ispod hero sekcije.

## 6. Podstranice

- **/komarnici/**: hero sa fotografijom #11, svih 5 tipova detaljno, boje, fotografije #0, #3, #5, #7, #9, FAQ o komarnicima, CTA.
- **/roletne/**: hero sa fotografijom #12, tekst o lamelama sa poliuretanskom penom i čepovima, 5 tipova (Rondo, petougaona kutija, gurtna, kanap, elektro motor), boje, CTA.
- **/servis/**: popravka prozora i vrata, servis komarnika, servis roletni, štelovanje stolarije, zamena gurtne, pala roletna. Sekcija "Pripremite prozore za košavu" (iz Ivanove objave). Istakni "Slikajte kvar i pošaljite na Viber ili WhatsApp". Fotografija #1.
- **/kontakt/**: telefon, Viber, WhatsApp, email, adresa, mapa (facade), forma.
- **/404.html**: kratko, korisno, linkovi na usluge i telefon.

Svaka podstranica ima breadcrumbs (Početna > Komarnici) i jedan jasan H1.

## 7. Tekstovi (copywriting)

- Piši kao čovek, kao da Ivan priča mušteriji: jednostavno, toplo, konkretno. Bez marketinških fraza tipa "vrhunski kvalitet po najpovoljnijim cenama", "Vaš pouzdan partner", "rešenja po meri vaših potreba".
- **Strogo zabranjeno:** crtice "—" i "–" u tekstu (koristi zarez, tačku ili "i"). Obična crtica samo u složenicama i brojevima telefona.
- Nigde ne sme da piše da je ovo demo, primer, šablon, niti da je urađeno uz AI. Bez "Lorem ipsum".
- Dugmad govore šta se dešava: "Pozovite 060 193 0660", "Pošaljite sliku na WhatsApp", "Zakažite merenje", "Zatražite ponudu".
- Latinica, ekavica, persiranje.

## 8. SEO (lokalni, Beograd)

- **Ključne reči** (prirodno u naslovima, H1/H2, tekstu i alt tekstovima, bez nabijanja): komarnici Beograd, komarnici po meri, rolo komarnici, plise komarnici, komarnici za vrata, aluminijumske roletne Beograd, ugradnja roletni, popravka roletni, zamena gurtne, štelovanje prozora, servis stolarije, Zvezdara.
- **Title i meta description** za svaku stranicu, jedinstveni, title do 60 karaktera, description do 155. Primer naslovne: `Komarnici i roletne po meri Beograd | Ivan, 060 193 0660`.
- **Canonical** na svakoj stranici (`https://komarnici-roletneservis.rs/...`), Open Graph i Twitter kartice sa posebnom OG slikom 1200x630 (napravi je od hero fotografije sa nazivom firme preko).
- **Strukturirani podaci (JSON-LD):**
  - `HomeAndConstructionBusiness` (ili `LocalBusiness`) sa nazivom, adresom, telefonom, emailom, geo koordinatama (44.8014915, 20.4932133), `areaServed: Beograd`, `url`, `image`, `sameAs` (Google Maps link).
  - `Service` za komarnike, roletne i servis.
  - `FAQPage` za FAQ.
  - `BreadcrumbList` na podstranicama.
  - **NE** dodaj `aggregateRating` ni `Review` schema za sopstvene recenzije (Google to ne prikazuje za LocalBusiness i može da kazni kao samoreklamne recenzije). Recenzije su samo vidljiv sadržaj.
- `sitemap.xml` sa svim stranicama, `robots.txt` koji upućuje na sitemap.
- Semantički HTML: jedan H1 po stranici, logičan redosled naslova, `<main>`, `<nav>`, `<footer>`, `<address>`.
- Alt tekstovi opisni i na srpskom ("Plise komarnik na prozoru sa drvenim okvirom, ugradnja u Beogradu").
- Interni linkovi između usluga.
- NAP mora biti identičan svuda i isti kao na Google profilu.

## 9. Brzina (cilj: Lighthouse 95+ na telefonu u sve četiri kategorije)

- LCP slika (hero) kao `<img>` sa `srcset`, `sizes`, `width`, `height`, `fetchpriority="high"`, bez lazy loadinga. Sve ostale slike `loading="lazy"` i `decoding="async"`.
- `<picture>` sa AVIF, pa WebP, pa JPG.
- Kritični CSS za hero inline u `<head>` (mali), ostatak u `style.css`. CSS ukupno ispod 35 KB, JS ispod 15 KB, bez blokirajućih skripti (`defer`).
- Fontovi: maksimalno 3 fajla, preload samo jednog.
- Nema eksternih skripti (nema Google Analytics za sada, nema Font Awesome). Ikonice kao inline SVG.
- Bez layout shift-a (CLS blizu 0): sve slike sa dimenzijama, rezervisan prostor za mapu.
- `vercel.json`: `cleanUrls: true`, `trailingSlash` po želji ali dosledno, cache headeri (`/assets/` na godinu dana, `immutable`), security headeri (`X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`).

## 10. Pristupačnost

- Kontrast najmanje AA, vidljiv fokus na svim interaktivnim elementima, cela navigacija radi tastaturom, `aria` atributi na meniju, tabovima, FAQ-u i lightboxu.
- Dugmad i linkovi na telefonu najmanje 44x44 px.
- `prefers-reduced-motion` gasi animacije.

## 11. Provera pre nego što kažeš da je gotovo

1. Pokreni lokalno (`npx serve .`) i preko **Playwright MCP** napravi screenshotove svake stranice na širinama **390, 768 i 1440**. Pogledaj svaki screenshot i ispravi sve što izgleda loše (prelomi, preklapanja, prazni prostori, loše isečene slike).
2. Pokreni Lighthouse (`npx lighthouse http://localhost:3000 --preset=desktop` i mobilni) i ispravi dok ne bude 95+.
3. Proveri sve linkove (nijedan 404), `tel:`, `wa.me`, `viber://` i `mailto:` linkove.
4. `grep` kroz projekat: ne sme biti "—", "–", "demo", "lorem", "primer sajta", ni reč "AI" kao zasebna reč (`grep -w AI`).
5. Validiraj JSON-LD (struktura po schema.org) i HTML.
6. Na kraju mi daj kratak izveštaj: šta je urađeno, Lighthouse rezultati, screenshotovi.

## 12. Objava

- Inicijalizuj git, napravi `.gitignore` (bez `node_modules` i `scripts/raw`).
- Objavi na Vercel (`npx vercel` pa `npx vercel --prod`) kao projekat `komarnici-roletne-ivan`, tako da dobijem link tipa `komarnici-roletne-ivan.vercel.app` koji mogu da pošaljem vlasniku. Ako Vercel CLI traži login, reci mi šta da uradim.

## 13. TODO za vlasnika

Napravi fajl `TODO-za-Ivana.md` sa stvarima koje treba potvrditi pre pravog puštanja: tačno radno vreme po danima, garancija, rok izrade i ugradnje, okvirne cene po m² ako želi da ih prikaže, da li radi i van Beograda, logo (ako ima), Instagram/Facebook linkovi, pristup domenu komarnici-roletneservis.rs.
