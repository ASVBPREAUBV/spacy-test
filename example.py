import spacy
nlp = spacy.load('de')
doc = nlp(u"Ich habe schon eine PS4 bei mir zuhause und habe mir diese Konsole zugelegt, da die Spiele mit Mario exklusiv bei Nintendo liegen. Ich werden euch in meiner Rezension die Unterschiede der beiden Konsolen erlaeutern und auch erklaeren, wann man die Switch kaufen sollte und wann nicht.Jeder kennt ihn noch, den Super Nintendo oder Nintendo 64. Das waren die Konsolen, welche meine Kindheit und Jugend gepraegt haben. Lustige Spiele, welche man meist im Mulitplayer gespielt hat. ")
print([(w.text, w.pos_) for w in doc])