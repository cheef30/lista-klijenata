# -*- coding: utf-8 -*-
import json
from collections import Counter
from leads import L, OKOLINA

# (naziv kategorije, recenica zasto im treba sajt)
CAT = {
 "restoran": ("Restoran / kafana", "Dosta ljudi pre nego što izađe prvo pogleda na netu gde da ide, i sajt sa menijem, slikama i brojem za rezervaciju bi vam doneo dosta gostiju."),
 "picerija": ("Picerija", "Mislim da bi vam sajt sa menijem i cenama dobro došao, ljudi bi vas zvali direktno umesto preko Glova i Wolta, pa ne bi plaćali proviziju."),
 "kafic": ("Kafić / bar", "Na sajtu bi mogli da imate meni, najave za kvizove i svirke i rezervacije za vikend, sve na jednom linku koji stavite i na Instagram."),
 "poslasticarnica": ("Poslastičarnica", "Mislim da bi vam dobro došao sajt sa slikama torti i kolača gde ljudi mogu da poruče tortu za rođendan ili slavu."),
 "sala": ("Sala za proslave", "Mladenci danas skoro uvek prvo traže salu na netu, i sajt sa slikama, menijima i cenama po osobi bi vam doneo dosta upita."),
 "smestaj": ("Smeštaj / etno", "Sa svojim sajtom gosti mogu da rezervišu direktno kod vas, pa ne plaćate proviziju Booking-u, a to se brzo isplati."),
 "auto": ("Auto servis", "Kad ljudi traže servis, prvo guglaju, i sajt sa uslugama i brojem bi vam doneo nove mušterije iz celog kraja."),
 "slep": ("Vulkanizer / šlep", "Kad nekom pukne guma ili stane auto, prvo gugla, i sajt sa velikim dugmetom za poziv bi značio da zovu baš vas."),
 "perionica": ("Perionica", "Mislim da bi vam dobro došao sajt sa cenovnikom i brojem za zakazivanje."),
 "autodelovi": ("Auto delovi", "Mislim da bi vam dobro došao sajt gde ljudi vide šta imate i mogu da pošalju upit za deo pre nego što dođu."),
 "rentacar": ("Rent a car", "Sajt sa vozilima i cenama bi vam doneo rezervacije i od stranaca i ljudi iz dijaspore koji traže auto pre nego što dođu."),
 "autoskola": ("Auto škola", "Budući kandidati prvo guglaju, i sajt sa cenama kategorija i prijavom bi vam doneo dosta upisa."),
 "majstor": ("Električar / majstor", "Kad ljudima treba majstor prvo guglaju, i sajt sa uslugama i radovima bi vam doneo nove poslove."),
 "klime": ("Klime", "Pred leto i zimu svi guglaju ugradnju i servis klima, i sajt sa cenama i brojem bi vam doneo dosta poziva."),
 "stolarija": ("Stolarija / nameštaj", "Ljudi pre nego što pozovu žele da vide šta ste već radili, i sajt sa galerijom radova i upitom za ponudu bi prodavao umesto vas."),
 "gradjevina": ("Građevinski materijal", "Mislim da bi vam dobro došao sajt gde majstori i kupci vide šta imate i kako ide dostava pre nego što dođu."),
 "bravarija": ("Bravarija", "Sajt sa slikama ograda, kapija i konstrukcija koje ste radili je najbolja reklama za bravarski posao."),
 "selidbe": ("Selidbe / prevoz", "Ljudi selidbu skoro uvek traže na netu, i sajt sa cenama i brojem bi vam doneo još poslova."),
 "investitor": ("Gradnja / investitor", "Kupci stanova žele da vide raspored i kvadraturu pre nego što pozovu, i sajt sa stanovima u ponudi bi vam dosta ubrzao prodaju."),
 "skola": ("Škola jezika", "Sajt sa kursevima, cenama i prijavom bi vam doneo upise i van radnog vremena, posebno pred novi semestar."),
 "vrtic": ("Vrtić", "Na sajtu bi mogli lepo da objasnite kako ide upis i lista čekanja i da roditelji sami ostave prijavu, pa bi bilo manje nesporazuma."),
 "igraonica": ("Igraonica", "Roditelji traže igraonicu za rođendan na netu, i sajt sa paketima, cenama i slobodnim terminima bi vam doneo dosta rezervacija."),
 "sport": ("Sportski klub", "Roditelji traže klub za decu na netu, i sajt sa treninzima, terminima i upisom bi vam doneo nove članove."),
 "teretana": ("Teretana", "Sajt sa članarinama i rasporedom treninga bi vam doneo nove članove, a cene možete da menjate sami kad god hoćete."),
 "cvecara": ("Cvećara", "Mislim da bi vam dobro došao sajt gde ljudi mogu da poruče buket sa dostavom, i oni koji žive van grada a šalju cveće nekom ovde."),
 "rasadnik": ("Rasadnik", "Mislim da bi vam dobro došao sajt sa slikama sadnica i cenama, ljudi bi znali šta imate pre nego što dođu."),
 "mesara": ("Mesara", "Mislim da bi vam dobro došao sajt sa ponudom i brojem za porudžbine, posebno za roštilj i pečenje za slave i praznike."),
 "radnja": ("Radnja", "Mislim da bi vam dobro došao jednostavan sajt sa ponudom, radnim vremenom i brojem, ljudi bi vas lakše našli."),
 "fotograf": ("Fotograf", "Za fotografa je sajt sa galerijom najbolja reklama, mladenci i roditelji uvek prvo gledaju radove na netu."),
 "it": ("Servis / IT", "Kad ljudima crkne telefon ili računar, prvo guglaju servis, i sajt sa uslugama i cenama bi vam doneo nove mušterije."),
 "stamparija": ("Štamparija", "Mislim da bi vam dobro došao sajt gde ljudi vide šta sve štampate i mogu da pošalju fajl i upit odmah."),
 "veterinar": ("Veterinar", "Kad se ljubimcu nešto desi ljudi prvo guglaju, i sajt sa radnim vremenom, hitnim brojem i zakazivanjem bi vam dosta značio."),
 "knjigovodstvo": ("Knjigovodstvo", "Preduzetnici danas knjigovođu traže na netu, i sajt sa uslugama i cenama za paušalce i firme bi vam doneo nove klijente."),
}

SITE_LABEL = {"N":"Nema sajt (provereno)","U":"Nije provereno","O":"Ima stariji sajt","H":"Ima dobar sajt"}
HOT = {"restoran","sala","smestaj","stolarija","investitor","picerija","poslasticarnica","klime","igraonica"}

INTRO = ["Ja sam {IME}, pravim sajtove za lokalne firme.",
         "Zovem se {IME} i bavim se pravljenjem sajtova.",
         "Ja sam {IME}, pravim sajtove za radnje i lokale."]
ASK = {"U":["Hteo sam da pitam da li imate sajt?","Da li imate sajt?","Hteo sam da pitam da li ste razmišljali o sajtu?"],
       "N":["Koliko vidim nemate sajt, samo Google i društvene mreže.","Primetio sam da nemate sajt.","Koliko vidim nemate svoj sajt."],
       "O":["Gledao sam i vaš sajt i imam par ideja kako bi mogao da vam donosi više upita, posebno sa telefona.","Video sam vaš sajt i mislim da bi uz par izmena mogao da vam donosi više mušterija."]}
OFFER = ["Ako hoćete, mogu besplatno da vam napravim kako bi to izgledalo, pa ako vam se svidi dogovorimo se, ako ne nema veze.",
         "Mogu prvo besplatno da napravim primer da vidite kako bi izgledalo, bez ikakve obaveze.",
         "Ako vas zanima, napravim vam besplatno primer pa vi odlučite."]
GREET = ["Pozdrav!","Zdravo!","Pozdrav!"]

def prio(cat, site, rev, name):
    if site == "H": return "C"
    if site == "N" or name == "Auto škola Start": return "A"
    if site == "U" and cat in HOT and rev >= 150: return "A"
    return "B"

EMAIL = {
 "Veterinarska ambulanta Animalia":"info@animalia.rs","Skillton škola jezika":"info@skilltonschool.rs",
 "Etno selo Gostoljublje":"rezervacija@gostoljublje.com","Milenković gradnja":"evrogradnjamsplus@gmail.com",
 "Restoran Đukić":"restorandjukic@gmail.com","Hotel Svetionik":"svetionikdoo@gmail.com","Ranč Sava":"office@rancsava.rs",
 "Savski kutak":"office@savskikutak.rs","Rustikana":"tesic.m@rustikana.rs","Restoran Aleksandar":"pera.nikolic1412@gmail.com",
 "Ring Gym":"info@ringcentar.rs","Etno selo Zabran":"restoranzabran84@yahoo.com","Life & Fitness":"lifefitnessobrenovac@gmail.com",
 "Dukos":"dukos.vrata@gmail.com","Kod tri lepe":"kuburovicdanijel@gmail.com",
}
TURA1 = {
 "WhatsApp":["Zona Event Hall","Splav restoran kod Dejana","Vulkanizer Pavlović 24h","Kombi prevoz i selidbe Obrenovac",
   "Auto servis Mijatović","Golden Servis klime i bela tehnika","Pro Klima","Mesara kod Bobana","Mala Kolubara","Domaća brza hrana Nedelja M",
   "Vaš Kutak","Picerija Kraljica","Foto studio Lazarević","Deževa doo"],
 "Instagram":["Kod tri lepe","Restoran Koncept","Deky Gym","Poslastičarnica Saša","Sremački zet","Zona Lounge Bar",
   "Legura Bar","Antica Picerija","Zavet Cafe Bar","Cvećara Marina","Bubble Gum igraonica","Candy Land igraonica","Level Fitness",
   "Ubska kapija","Blaža","Zlatni roštilj"],
 "Mejl":["Restoran Đukić","Hotel Svetionik","Ranč Sava","Savski kutak","Rustikana","Restoran Aleksandar","Ring Gym","Etno selo Zabran",
   "Life & Fitness","Dukos"],
}
TURA2 = {
 "WhatsApp":["Svečana sala Fontana","Event hall The Lake","Royal mesara","Arma Fert Product","Mesara Popović SSS","Auto servis Tošić","WellVet",
   "Štamparija Easy Design","Roštilj i pice kod Bože","Rasadnik Popović","Auto centar Ub servis Goran","Svečana sala Urovci",
   "Jana Di Company Rent a car","Auto servis Mojsilović","La Flamingo","Svečana sala Imperia Gold","Picerija Venezia"],
 "Instagram":["Restoran Bajka","Fabrika Italia","Restoran Bajka Ub","Pikadili splav","Pizzeria Đuka","Gostionica Karađorđe","Kafanica",
   "Zabran61 Caffebar","Caffe i igraonica Džigibau","Tom & Jerry igraonica","Cvećara BV","Cvećara Dve Frajle","Cvećara NIVA",
   "Vinoteka Obrenovac","Apartmani Nenadović","Restoran Kale","Restoran Školarac","Leskovčanka","Aleksandar foto studio MiS","Exclusive NS"],
 "Mejl":["Veterinarska ambulanta Animalia","Skillton škola jezika","Etno selo Gostoljublje","Milenković gradnja"],
}
KANAL = {n:k for k,v in TURA1.items() for n in v}
TURA = {n:1 for n in KANAL}
for k,v in TURA2.items():
    for n in v: KANAL[n]=k; TURA[n]=2
POSLATO = {  # 2.10.2026, 6.10.2026, 9.10.2026
 "Mali Balkan":"Mejl 9.10.",
 **{n:"WhatsApp 9.10." for n in ["Event hall The Lake","Arma Fert Product"]},
 **{n:"Mejl 6.10." for n in ["Skillton škola jezika","Etno selo Gostoljublje","Milenković gradnja"]},
 **{n:"Instagram 6.10." for n in ["Fabrika Italia","Pikadili splav","Caffe i igraonica Džigibau","Gostionica Karađorđe"]},
 **{n:"Mejl 2.10." for n in ["Life & Fitness","Etno selo Zabran","Ranč Sava","Hotel Svetionik","Restoran Đukić","Restoran Aleksandar","Savski kutak","Rustikana","Ring Gym","Dukos"]},
 **{n:"WhatsApp 2.10." for n in ["Splav restoran kod Dejana","Zona Event Hall","Mala Kolubara","Vulkanizer Pavlović 24h","Kombi prevoz i selidbe Obrenovac","Golden Servis klime i bela tehnika","Pro Klima"]},
 **{n:"Instagram 2.10." for n in ["Kod tri lepe","Deky Gym","Poslastičarnica Saša","Sremački zet","Cvećara Marina","Legura Bar","Antica Picerija","Bubble Gum igraonica"]},
}
NAPOMENA = {
 **{n:"Nema WhatsApp" for n in ["La Flamingo","Svečana sala Fontana","Pizzeria Đuka","Zona Lounge Bar","Restoran Bajka","Svečana sala Imperia Gold","Restoran Bajka Ub","Royal mesara","Restoran Koncept"]},
 "Blaža":"WhatsApp: proveri da li je poruka otišla (prekid 9.10.)",
 "Zabran61 Caffebar":"Instagram neaktivan od 2018, probaj WhatsApp","Tom & Jerry igraonica":"Instagram nalog prazan","Cvećara NIVA":"Instagram ne prima poruke",
 "Cvećara Dve Frajle":"Instagram nije pronađen (nađeni nalog je iz Banatskog Dvora)",
 
 "Pizzeria Đuka":"Instagram nije pronađen (nađeni nalog nije iz Obrenovca)",
 "Veterinarska ambulanta Animalia":"Mejl nije poslat (blokirano), pošalji ručno na info@animalia.rs",
 "Pro Klima":"Klijent: radi se sajt (100 €)","TN-Frigo klime":"Konkurencija Pro Klime, ne kontaktirati za sada","Delta Frigo":"Konkurencija Pro Klime, ne kontaktirati za sada",
 "Domaća brza hrana Nedelja M":"Nema WhatsApp","Vaš Kutak":"Nema WhatsApp","Deževa doo":"Nema WhatsApp","Auto servis Mijatović":"Nema WhatsApp",
 "Picerija Kraljica":"Nema WhatsApp","Mesara kod Bobana":"Nema WhatsApp",
 "Foto studio Lazarević":"Broj ti je u kontaktima kao Solja, nije poslato",
 "Blaža":"Privatan Instagram, bez poruka",
 "Zona Lounge Bar":"Instagram nije pronađen (zona.lounge.bar je iz Hrvatske)","Ubska kapija":"Instagram nije pronađen","Level Fitness":"Instagram nije pronađen",
 "Zlatni roštilj":"Instagram nije pronađen","Zavet Cafe Bar":"Instagram nije pronađen",
 "Auto škola Start":"Ne kontaktirati",
}
import json as _j, os as _o
if _o.path.exists('wa_res.json'):
    for _n,_s in _j.load(open('wa_res.json')).items():
        if _s=='POSLATO': POSLATO.setdefault(_n,"WhatsApp 9.10.")
        elif _s=='nema WA':
            _old=NAPOMENA.get(_n,'')
            if 'Nema WhatsApp' not in _old: NAPOMENA[_n]=("Nema WhatsApp. "+_old).strip()
        elif _s.startswith('preskoceno'): NAPOMENA.setdefault(_n,"Ista firma kao Rasadnik Popović, nije slato posebno")
NAPOMENA["Rent a car Spid N&N"]=NAPOMENA["Rasadnik Breković"]="WhatsApp: proveri da li je poruka otišla (Chrome se diskonektovao 9.10.)"; NAPOMENA.pop("Blaža",None); NAPOMENA["Blaža"]="Nema WhatsApp. Privatan Instagram, bez poruka"
IG_NADJEN = {"Restoran Bajka":"@restoran.bajka.lazarevac","Fabrika Italia":"@fabrika_italia_","Restoran Bajka Ub":"@restoran.bajka.ub",
 "Pikadili splav":"@pikadili_restoran_splav","Pizzeria Đuka":"@caffe_pizzeria_djuka","Gostionica Karađorđe":"@gostionica_karadjordje","Kafanica":"@kafanica.lazarevac",
 "Zabran61 Caffebar":"@caffebar_zabran61","Caffe i igraonica Džigibau":"@dzigibau_igraonica","Tom & Jerry igraonica":"@igraonica_tom_and_jerry_",
 "Cvećara BV":"@cvecara_bv","Cvećara Dve Frajle":"@dvef.rajle","Cvećara NIVA":"@niva.dv","Vinoteka Obrenovac":"@vinoteka_obrenovac",
 "Apartmani Nenadović":"@apartmani_nenadovic","Restoran Kale":"@restoran_kale","Restoran Školarac":"@skolarac.restoran.ub",
 "Leskovčanka":"@restoranleskovcanka","Aleksandar foto studio MiS":"@studio_mis_no1","Exclusive NS":"@ekskluzivns","Legura Bar":"@legura.bar","Antica Picerija":"@pizzeria_antica_","Bubble Gum igraonica":"@bubblegum_igraonica","Cvećara Marina":"@cvecara_marina","Candy Land igraonica":"@candy_land_obrenovac"}

SITE_O = {"Restoran Bajka","Restoran Bajka Ub","Restoran Koncept","Kafanica","Candy Land igraonica","Exclusive NS",
          "Lovački dom","Etno selo Boškova voda","Zlatna dvorana"}
out = []
for i,(n,grad,cat,tel,ig,site,rt,rev,hook) in enumerate(L):
    label, pitch = CAT[cat]
    if n in SITE_O: site = "O"
    v = i % 3
    if n == "Auto škola Start":
        msg = ("Pozdrav! Ja sam {IME}, pravim sajtove. Napravio sam primer sajta za vašu auto školu, sa cenama kategorija, rasporedom i prijavom za upis, "
               "pa sam hteo da vam pokažem. Evo linka cheef30.github.io/Auto-skola\n\n"
               "Ako vam se svidi, ubacim vaše prave podatke i slike i stavim ga na vaš domen. Mogu i da svratim da vam pokažem uživo, samo javite.")
    elif site == "H":
        msg = (f"{GREET[v]} {INTRO[v]} {hook} Vaš sajt je već dobar, pa ne nudim novi, "
               "ali ako vam treba neko da ga održava i menja stvari kad zatreba, tu sam. Javite ako vas zanima.")
    else:
        ask = ASK[site][v % len(ASK[site])]
        msg = f"{GREET[v]} {INTRO[v]} {hook}\n\n{ask} {pitch}\n\n{OFFER[v]}"
    if KANAL.get(n)=="Mejl":
        msg = msg + ("\n\n{IME}" if msg.startswith("Pozdrav!") else "\n\nPozdrav,\n{IME}")
    assert "—" not in msg and "–" not in msg, n
    out.append({"n":n,"grad":grad,"zona":"Obrenovac i okolina" if grad in OKOLINA else "Ostatak Srbije",
                "cat":label,"tel":tel,"ig":IG_NADJEN.get(n,"" if n=="Zona Lounge Bar" else ig),"sent":POSLATO.get(n,""),"note":NAPOMENA.get(n,""),"site":SITE_LABEL[site],"rt":rt,"rev":rev,
                "p":prio(cat,site,rev,n),"msg":msg,"email":EMAIL.get(n,""),"kanal":KANAL.get(n,""),"tura":TURA.get(n,0),
                "subj":f"Sajt za {n}" if KANAL.get(n)=="Mejl" else ""})

order = {"A":0,"B":1,"C":2}
out.sort(key=lambda x:(x["zona"]!="Obrenovac i okolina", order[x["p"]], x["site"]!="Nema sajt (provereno)", x["n"]!="Auto škola Start", -x["rev"]))
for k,o in enumerate(out,1): o["id"]=k
missing=[n for n in KANAL if n not in {o["n"] for o in out}]; assert not missing, missing
names=[o["n"] for o in out]; assert len(names)==len(set(names)), [x for x,c in Counter(names).items() if c>1]
json.dump(out, open("data.json","w"), ensure_ascii=False, indent=0)
print(len(out), Counter(o["zona"] for o in out), Counter(o["p"] for o in out))
print(Counter(o["kanal"] for o in out if o["kanal"]))
