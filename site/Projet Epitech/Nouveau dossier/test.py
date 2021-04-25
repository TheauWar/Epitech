import sqlite3

with sqlite3.connect("bddCovid.db") as conn:
    cursor = conn.cursor()
    cursor.execute("select NOMP, IDP, IMAGE from PRODUIT where NOMP like '%{}%'".format("as"))
    temp = cursor.fetchall()
    i = len(temp)
    p = []
    for k in range((i-1)//6+1):
        p.append(temp[6*k:6*k+6])
    for i in p:
        print(i, len(i))


    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (11, "masque", "Masque Itech", "Noir", 140, 99, """1 masque Itech fabriqué en France.<br/>
    Nous sommes convaincus que l’accès à un air pur est un droit fondamental ; Votre nouvelle référence pour une respiration de qualité le masque halo smart.<br/>
    - DESIGN - Conception innovante brevetée | Un système breveté hermétique à 360°, une membrane très douce de qualité médicale et une construction ultralégère : nos masques Active sont équipés d'un filtre qui s'adapte parfaitement aux contours de votre visage. En association avec des bandes élastiques ajustables au niveau des oreilles, le masque offre l'ajustement idéal pour chaque visage. <br/>
    - FILTRATION | Une efficacité > à 99% | Protection respiratoire et barrière en seul masque ! Une efficacité de filtration des particules à 99,3% (test PFE) et de filtration des bactéries à 99,9% (test EFB) ainsi qu'une résistance aux fluides. Dépasse ainsi les attentes moyennes concernant les masques de protection d'après les lignes directrices de la norme européenne CWA 17553:2020 et les directives françaises AFNOR SPEC S76-001. Une respirabilité inégalée.<br/>
    - FONCTION | Notre structure unique 3D forme une voûte d'air et crée ainsi un espace entre le visage et le masque pour une respirabilité sans effort. Réalisé à partir de matériaux à faible résistance, notre modèle de masque Active permet une circulation d'air illimitée pour une respiration plus facile. 40 heures de port | Des filtres remplaçables conçus pour être portés pendant une semaine ou jusqu'à 40 heures. Fournit avec 5 filtre.""", "cgi-bin/masqueItech.png"))




    liste = []
    cursor.execute("select COULEUR from PRODUIT where NOMP={};".format(p[0]))
    other = cursor.fetchall()

    for elt in other:
        if elt[0] != p[3]:
            liste.append(elt[0])

    if liste != [""]:
        html +="""
    		<label>Autres</label>
    		<select>
    			<option value = '"""+p[3]+"""'>"""+p[3]+"""</option>"""
        for elt in liste:
            html +="""<option value = '"""+elt+"""'>"""+elt+"""</option>"""
    	html += """	</select>"""