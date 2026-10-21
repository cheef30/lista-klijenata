import json,random,urllib.parse,re
random.seed(21)
P={
'kozmetika':["Na sajtu bi klijentkinje mogle da vide cenovnik i tretmane i same da zakažu termin, čak i dok vi radite.","Sajt sa cenovnikom, slikama radova i zakazivanjem bi vam doneo nove klijentkinje, a manje poziva usred tretmana."],
'frizer':["Sajt sa cenovnikom i zakazivanjem bi vam uštedeo dosta poziva dok šišate.","Na sajtu bi ljudi videli cene, slike radova i mogli sami da zakažu termin."],
'barber':["Sajt sa cenovnikom i online zakazivanjem bi vam uštedeo pozive dok radite.","Na sajtu bi momci videli cene i slobodne termine i zakazali sami."],
'stomatolog':["Pacijenti danas zubara prvo traže na Google-u, i sajt sa uslugama i brojem za zakazivanje bi vam doveo nove ljude.","Sajt sa uslugama, okvirnim cenama i zakazivanjem bi vam doneo nove pacijente, posebno one koji se tek doselili."],
'smestaj':["Sa svojim sajtom gosti mogu da rezervišu direktno kod vas, pa ne plaćate proviziju Booking-u.","Sajt sa slikama, cenama i rezervacijom direktno kod vas bi vam uštedeo proviziju koju dajete Booking-u."],
'restoran':["Meni sa slikama i broj za rezervaciju na jednom mestu, pa taj link stavite i na Google i na Instagram.","Sajt sa menijem, slikama i rezervacijom bi vam doveo i ljude koji su tu prvi put i biraju gde da jedu."],
'teretana':["Sajt sa članarinama, rasporedom i prijavom bi vam doveo nove članove.","Na sajtu bi ljudi videli cene članarina i treninge i prijavili se odmah."],
'auto':["Kad nekome zatreba servis prvo gugla, i sajt sa uslugama i brojem bi značio da zovu baš vas.","Jednostavan sajt sa uslugama, radnim vremenom i brojem bi vam doneo nove mušterije iz celog kraja."],
'fotograf':["Za fotografa je sajt sa galerijom najbolja reklama, ljudi uvek prvo gledaju radove.","Sajt sa galerijom radova i paketima bi vam doneo dosta upita za svadbe i krštenja."],
'cvecara':["Sajt gde ljudi mogu da naruče buket sa dostavom bi vam doneo porudžbine i od onih koji nisu iz grada.","Na sajtu bi ljudi videli bukete i naručili sa dostavom, i kad niste u radnji."],
'veterinar':["Sajt sa radnim vremenom, hitnim brojem i uslugama bi vlasnicima ljubimaca mnogo značio.","Kad se ljubimcu nešto desi ljudi prvo guglaju, i sajt sa hitnim brojem i uslugama bi im mnogo pomogao."],
'pekara':["Sajt sa ponudom i porudžbinama za proslave i firme bi vam doneo veće narudžbine.","Na sajtu bi ljudi mogli da vide ponudu i poruče za slave i rođendane."],
}
INTRO=["Pozdrav! Ja sam Stefan, pravim sajtove.","Zdravo! Stefan ovde, bavim se izradom sajtova.","Pozdrav! Zovem se Stefan i pravim sajtove za lokalne firme.","Zdravo! Ja sam Stefan, pravim sajtove za radnje i lokale."]
ASK=["Hteo sam da pitam da li imate sajt?","Da li imate sajt?","Da li ste razmišljali o sajtu?"]
END=["Mogu prvo besplatno da napravim primer da vidite kako bi izgledalo, bez ikakve obaveze.","Ako vas zanima, napravim vam primer besplatno pa vi odlučite.","Ako hoćete, napravim vam besplatno primer, pa ako se svidi pričamo dalje.","Mogu da vam napravim primer besplatno, pa ako vam se ne svidi nema veze 🙂"]
out=[]
for l in open('new_leads.tsv'):
    n,c,cat,ph,rt,cnt,h=l.rstrip('\n').split('\t')
    m=f"{random.choice(INTRO)} Video sam da {h}.\n\n{random.choice(ASK)} {random.choice(P[cat])}\n\n{random.choice(END)}"
    assert '—' not in m and '–' not in m
    dig='381'+re.sub(r'\D','',ph)[1:]
    out.append({'n':n,'grad':c,'cat':cat,'tel':ph,'rt':float(rt),'rev':int(cnt),'msg':m,'url':f"https://web.whatsapp.com/send?phone={dig}&text="+urllib.parse.quote(m)})
json.dump(out,open('nova_lista.json','w'),ensure_ascii=False,indent=1)
json.dump([{'n':x['n'],'url':x['url']} for x in out],open('waq2.json','w'),ensure_ascii=False)
import collections;print(len(out),collections.Counter(x['cat'] for x in out));print(out[5]['msg']);print('---');print(out[60]['msg'])
