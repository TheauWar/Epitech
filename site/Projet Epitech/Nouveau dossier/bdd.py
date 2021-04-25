
# Créé par Pierr, le 24/04/2021 en Python 3.7
import sqlite3
import os

os.remove("bddCovid.db")
with sqlite3.connect("bddCovid.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""create table PRODUIT (
                    IDP integer,
                    TYPE char(10),
                    NOMP varchar(30),
                    COULEUR varchar(30),
                    PRIX float,
                    NBR integer,
                    DESC text,
                    IMAGE varchar(30),
                    constraint PK_ID primary key (IDP)
                    );""")


    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (0, "masque", "Masque chirugicaux", "Gris", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm""" , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (1, "masque", "Masque chirugicaux", "Bleu", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm"""  , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (2, "masque", "Masque chirugicaux", "Violet", 15, 99, """Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm""" , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (3, "masque", "Masque chirugicaux", "Rouge", 15, 99, """Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm""" , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (4, "masque", "Masque chirugicaux", "Rose", 15, 99, """Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm""" , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (5, "masque", "Masque chirugicaux", "Orange", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm"""  , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (6, "masque", "Masque chirugicaux", "Jaune", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm"""  , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (7, "masque", "Masque chirugicaux", "Vert clair", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm"""  , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (8, "masque", "Masque chirugicaux", "Vert", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm"""  , "cgi-bin/masqueChirurgical.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (9, "masque", "Masque chirugicaux", "Noir", 15, 99,"""Boîte de 50 Masques Chirurgicaux fabriqués en France.<br/><br/>
                                                                                                                                Masques 3 plis, à usage unique, de TYPE IIR.<br/>
                                                                                                                                Constitués de trois couches de polypropylène en non-tissé: <br/>
                                                                                                                                -Deux couches extérieures en SpunBond<br/>
                                                                                                                                -Une couche intérieure en MeltBlown<br/><br/>
                                                                                                                                Chaque côté du masque dispose d’un élastique permettant la fixation du masque sur le visage.
                                                                                                                                Une barrette nasale métallique et recouverte de plastique permet d’ajuster le masque sur le visage au niveau du nez.<br/>
                                                                                                                                Extrêmement léger et confortable.<br/><br/>
                                                                                                                                Dimensions du Masque : (L x l ) 170 x 95 mm<br/>
                                                                                                                                Dimensions des Fixations (Oreilles) : Standard 185-190 mm"""  , "cgi-bin/masqueChirurgical.png"))



    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (10, "masque", "Masque en tissu", "", 8, 99, """1 masque en tissu noir multi-couches fabriqué en France.<br/><br/>
                                                                                                                                Fabriqué selon les normes SPEC S76-001.<br/>
                                                                                                                                Les 2 élastiques se positionnent derrière les oreilles, ce qui permet un maintien parfait et une adhérence optimale du masque bleu marine sur le visage.<br/>
                                                                                                                                Notre tissu de coton respecte les normes recommandées l'IFTH et la DGA.<br/>
                                                                                                                                Laver a 60 degres cycle court, ne pas utiliser de clore ou de javel, repasser au maximun a 150 degres.<br/>
                                                                                                                                Nos masques en tissu ont une durée d'au moins 50 lavages en machine.<br/>
                                                                                                                                L'élastique n'est pas fait pour subir de nombreux lavages à 60°. <br/><br/>
                                                                                                                                Pour allonger sa durée de vie, vous pouvez : <br/>
                                                                                                                                - le mettre dans un sac de lavage, pour réduire les frottements<br/>
                                                                                                                                - faire des petits nœuds si l'élastique se détend
                                                                                                                                Dimensions du masque adultes plié : 10 x 20cm""", "cgi-bin/masqueTissu.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (11, "masque", "Masque Itech", "", 140, 99, """1 masque Itech fabriqué en France.<br/><br/>
                                                                                                                            Nous sommes convaincus que l’accès à un air pur est un droit fondamental ; Votre nouvelle référence pour une respiration de qualité le masque halo smart.<br/>
                                                                                                                            - DESIGN - Conception innovante brevetée | Un système breveté hermétique à 360°, une membrane très douce de qualité médicale et une construction ultralégère : nos masques Active sont équipés d'un filtre qui s'adapte parfaitement aux contours de votre visage. En association avec des bandes élastiques ajustables au niveau des oreilles, le masque offre l'ajustement idéal pour chaque visage. <br/>
                                                                                                                            - FILTRATION | Une efficacité > à 99% | Protection respiratoire et barrière en seul masque ! Une efficacité de filtration des particules à 99,3% (test PFE) et de filtration des bactéries à 99,9% (test EFB) ainsi qu'une résistance aux fluides. Dépasse ainsi les attentes moyennes concernant les masques de protection d'après les lignes directrices de la norme européenne CWA 17553:2020 et les directives françaises AFNOR SPEC S76-001. Une respirabilité inégalée.<br/>
                                                                                                                            - FONCTION | Notre structure unique 3D forme une voûte d'air et crée ainsi un espace entre le visage et le masque pour une respirabilité sans effort. Réalisé à partir de matériaux à faible résistance, notre modèle de masque Active permet une circulation d'air illimitée pour une respiration plus facile. 40 heures de port | Des filtres remplaçables conçus pour être portés pendant une semaine ou jusqu'à 40 heures. Fournit avec 5 filtre.""", "cgi-bin/masqueItech.png"))



    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (12, "masque", "Recharge de masque", "", 30, 99, """5 Recharges pour le Masque Itech fabriqués en France.<br/><br/>
                                                                                                                            Le filtre remplaçable bloque les bactéries, la poussière et les particules grâce à une double couche en nanofiltre TorayMicron chargée électrostatiquement. <br/>
                                                                                                                            La couche extérieure unique protège des polluants atmosphériques tandis que la couche intérieure est douce pour la peau et hypoallergénique.<br/>
                                                                                                                            Ces recharges sont compatibles avec votre masques itech COVISHOP.""", "cgi-bin/rechargeMasque.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (13, "masque", "Masque transparent", "", 2, 99, """Deux Masques transparents fabriqués en France.<br/><br/>
                                                                                                                                        Masque barrière à fenêtre anti-projection lavable et anti-buée ayant reçu les résultats des tests réalisés par la DGA (Direction Générale de l'Armement) conformes à la note d'information interministérielle du 29 Mars 2020, mise à jour le 28 Janvier 2021, pour un usage non sanitaire (= hors médical) de catégorie UNS1* .<br/>
                                                                                                                                        Le Masque Inclusif se compose d'un tissu léger, fin et respirant, agréable au porté. <br/>
                                                                                                                                        La bande transparente est anti-buée, elle offre la possibilité de voir l'expression du visage et de lire sur les lèvres. <br/><br/>
                                                                                                                                        Détails :<br/>
                                                                                                                                        - Le masque est maintenu sur le visage au moyen d'élastiques à placer derrière les oreilles.<br/>
                                                                                                                                        - Barrette nasale amovible : pour un maintien personnalisables et ajustable selon les différentes morphologies du visage. Elle est fournie avec chaque masque.<br/>
                                                                                                                                        - Design ergonomique : la paroi est éloignée de la bouche offrant un confort optimal lors de l'élocution.<br/>
                                                                                                                                        - Composition : Tissu : 100% polypropylèneBande transparente : crystal PET.<br/>
                                                                                                                                        - Conseils d'entretien : Afin de conserver la qualité de l'anti-buée, ne pas utiliser de détergent.<br/>
                                                                                                                                        Laver à 60° durant 30 minutes, il est recommandé de laver le masque seul à la machine/Lavable 20 fois.<br/>
                                                                                                                                        Laisser sécher à l'air libre/Ne pas utiliser de sèche-linge, ne pas repasser.""", "cgi-bin/masqueTransparent.png"))




    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (14, "masque", "Visière", "", 9, 99, """Une Visière fabriquée en France.<br/><br/>
                                                                                                                                Cet écran de protection faciale couvre le visage, le menton et le cou.<br/>
                                                                                                                                Il s’emboite facilement sur la tête comme une casquette et s’ajuste en fonction de votre tour de tête.<br/><br/>
                                                                                                                                L’armature de cette visière est réalisée en injection plastique avec du PVC recyclé issu de bouteilles de plastiques, la face de protection est en polypropylène transparent recyclable (norme jouet).<br/>
                                                                                                                                C’est un produit qui vient compléter un masque grand public ainsi que le port de gants et le respect des gestes barrières.<br/><br/>
                                                                                                                                Idéale pour des environnements de travail, de commerce et de transport, cette visière vous apportera une protection efficace contre les postillons tout en vous permettant de travailler confortablement.<br/><br/>
                                                                                                                                L’avantage de cet outil : il est réutilisable ; un coup de désinfectant des deux côtés après chaque utilisation suffit !<br/>
                                                                                                                                Si vous êtes en contact avec les clients cette visière permet une barrière entre vous et ce dernier. Si vous êtes sur votre bureau toute la journée, cette visière sera utile pour tous vos déplacements et moment en public.<br/><br/>
                                                                                                                                De taille unique, la visière se serre avec un système de cerceaux sur les côtés de votre tête. Vous pourrez l’ajuster à tout moment et elle peut se porter avec une casquette, un casque de chantier, des lunettes ainsi qu’un masque papier ou tissus. <br/>
                                                                                                                                Cette visière est anti-buée, si toutefois vous en avez un peu, il suffit de remonter un peu l’écran en baissant la bande à l’arrière de votre tête pour l’éloigner un peu de votre visage.<br/><br/>
                                                                                                                                Taille : largeur 250 mm x hauteur 250 mm<br/><br/>
                                                                                                                                Cette solution ne doit en aucun cas se substituer à l’utilisation d’un masque de protection (si disponible) aux gestes barrières ainsi qu'aux équipements professionnels obligatoires""", "cgi-bin/visiere.png"))



    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (15, "gel", "Gels hydroalcoolique", "50ml", 2, 99, """Gel Hydro-Alcoolique fabriqué en France<br/><br/>
                                                                                                                                    Gel antibactérien désinfectant et nettoyant pour lavage des mains.<br/><br/>
                                                                                                                                    BACTERICIDE EN1276 FONGICIDE EN1650 VIRUCIDE H1N1 NORME EN14476<br/><br/>
                                                                                                                                    Gel transparent incolore indispensable dans la vie de tous les jours.<br/>
                                                                                                                                    Les gels hydro alcooliques et anti-bactériens sont à emporter partout avec soi pour se désinfecter les mains en toute occasion.<br/><br/>
                                                                                                                                    Sans eau, ni savon, les gels gardent les mains propres.<br/><br/>
                                                                                                                                    A utiliser avec précaution, ne nécessite aucun rinçage. <br/>
                                                                                                                                    Appliquer le produit sur la peau saine, propre et sèche. <br/>
                                                                                                                                    Frictionner les mains entre 30 et 60 secondes. <br/>
                                                                                                                                    Laisser sécher. <br/>
                                                                                                                                    Ne pas avaler. <br/>
                                                                                                                                    Ne pas inhaler.""", "cgi-bin/gell.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (16, "gel", "Gels hydroalcoolique", "250ml", 5, 99,"""Gel Hydro-Alcoolique fabriqué en France<br/><br/>
                                                                                                                                    Gel antibactérien désinfectant et nettoyant pour lavage des mains.<br/><br/>
                                                                                                                                    BACTERICIDE EN1276 FONGICIDE EN1650 VIRUCIDE H1N1 NORME EN14476<br/><br/>
                                                                                                                                    Gel transparent incolore indispensable dans la vie de tous les jours.<br/>
                                                                                                                                    Les gels hydro alcooliques et anti-bactériens sont à emporter partout avec soi pour se désinfecter les mains en toute occasion.<br/><br/>
                                                                                                                                    Sans eau, ni savon, les gels gardent les mains propres.<br/><br/>
                                                                                                                                    A utiliser avec précaution, ne nécessite aucun rinçage. <br/>
                                                                                                                                    Appliquer le produit sur la peau saine, propre et sèche. <br/>
                                                                                                                                    Frictionner les mains entre 30 et 60 secondes. <br/>
                                                                                                                                    Laisser sécher. <br/>
                                                                                                                                    Ne pas avaler. <br/>
                                                                                                                                    Ne pas inhaler.""" , "cgi-bin/gell.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (17, "gel", "Gels hydroalcoolique", "500ml", 8, 99,"""Gel Hydro-Alcoolique fabriqué en France<br/><br/>
                                                                                                                                    Gel antibactérien désinfectant et nettoyant pour lavage des mains.<br/><br/>
                                                                                                                                    BACTERICIDE EN1276 FONGICIDE EN1650 VIRUCIDE H1N1 NORME EN14476<br/><br/>
                                                                                                                                    Gel transparent incolore indispensable dans la vie de tous les jours.<br/>
                                                                                                                                    Les gels hydro alcooliques et anti-bactériens sont à emporter partout avec soi pour se désinfecter les mains en toute occasion.<br/><br/>
                                                                                                                                    Sans eau, ni savon, les gels gardent les mains propres.<br/><br/>
                                                                                                                                    A utiliser avec précaution, ne nécessite aucun rinçage. <br/>
                                                                                                                                    Appliquer le produit sur la peau saine, propre et sèche. <br/>
                                                                                                                                    Frictionner les mains entre 30 et 60 secondes. <br/>
                                                                                                                                    Laisser sécher. <br/>
                                                                                                                                    Ne pas avaler. <br/>
                                                                                                                                    Ne pas inhaler.""" , "cgi-bin/gell.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (18, "gel", "Désinfectants", "2l", 10, 99, """Désinfectant fabriqué en France.<br/><br/>
                                                                                                                        Gardez vos mains et toutes vos surfaces de travail propres et désinfectées grâce à notre spray désinfectant.<br/><br/>
                                                                                                                        A base d’alcool, destiné à la maîtrise des risques microbiologiques en environnement médical (hôpitaux, cliniques, maisons de retraite, crèches, etc.), il a été développé pour divers usages :<br/>
                                                                                                                        Pour la désinfection des surfaces lavables :<br/>
                                                                                                                        - Les plans de travail et paillasses<br/>
                                                                                                                        - L’ameublement (placard des patients, lits, chaises et fauteuils, chariots...)<br/>
                                                                                                                        - Les lunettes de toilettes<br/>
                                                                                                                        - Les plateaux repas<br/>
                                                                                                                        - Les poignées de portes<br/>
                                                                                                                        - Les banques réfrigérées et réfrigérateurs<br/>
                                                                                                                        - L’ensemble du matériel médical en contact avec les patients et le personnel médical.<br/><br/>
                                                                                                                        Procurez-vous notre spray désinfectant sans rinçage afin de garder vos mains et vos surfaces de travail parfaitement propres.<br/><br/>
                                                                                                                        Ses avantages :<br/>
                                                                                                                        - Ses propriétés désinfectantes garantissent un large spectre d’activité biocide, avec une rapidité d’action et laisse des surfaces parfaitement nettoyées sans trace.<br/>
                                                                                                                        - Virucide selon la norme EN 14476, efficace contre polyovirus, adénovirus, influenza virus (H1N1 Grippe A, H5N1 Grippe aviaire), hépatite B et C, HIV, Rotavirus (gastro enterite), virus Herpès simplex<br/>
                                                                                                                        - Bactéricide selon la norme EN 13727/Fongicide selon la norme EN 1275<br/>
                                                                                                                        - Label ECOCERT<br/><br/>
                                                                                                                         Précautions d’emploi :<br/>
                                                                                                                        - Utiliser ce spray antibactérien avec précaution. Avant toute utilisation, lisez l’étiquette et les informations concernant le produit.<br/>
                                                                                                                        - Ne pas mélanger à d’autres produits.<br/>
                                                                                                                        - Reproduire l’étiquetage si transvasement dans un autre contenant.<br/>
                                                                                                                        - Respecter les précautions de l’étiquetage réglementaire.<br/>
                                                                                                                        - L’emballage, vide ou contenant encore du produit, doit être éliminé en tant que déchet dangereux sous l’entière responsabilité du détenteur de ce déchet.<br/>
                                                                                                                        - Ne pas rejeter les résidus dans les égouts et les cours d’eau.<br/>
                                                                                                                        - En cas d’ingestion, ne pas faire vomir, consulter immédiatement un médecin et lui montrer l’emballage ou l’étiquette/Consulter le centre antipoison le plus proche.<br/>
                                                                                                                        - En cas de doute, faire un essai préalable sur une partie cachée afin de vérifier la compatibilité du produit avec les surfaces à traiter.<br/><br/>
                                                                                                                        Important : ce spray désinfectant contre le COVID-19 n’exonère absolument pas l'utilisateur de l’application des gestes barrières qui sont essentiels.""", "cgi-bin/desinfectant.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (19, "gel", "Désinfectants", "5l", 20, 99,"""Désinfectant fabriqué en France.<br/><br/>
                                                                                                                        Gardez vos mains et toutes vos surfaces de travail propres et désinfectées grâce à notre spray désinfectant.<br/><br/>
                                                                                                                        A base d’alcool, destiné à la maîtrise des risques microbiologiques en environnement médical (hôpitaux, cliniques, maisons de retraite, crèches, etc.), il a été développé pour divers usages :<br/>
                                                                                                                        Pour la désinfection des surfaces lavables :<br/>
                                                                                                                        - Les plans de travail et paillasses<br/>
                                                                                                                        - L’ameublement (placard des patients, lits, chaises et fauteuils, chariots...)<br/>
                                                                                                                        - Les lunettes de toilettes<br/>
                                                                                                                        - Les plateaux repas<br/>
                                                                                                                        - Les poignées de portes<br/>
                                                                                                                        - Les banques réfrigérées et réfrigérateurs<br/>
                                                                                                                        - L’ensemble du matériel médical en contact avec les patients et le personnel médical.<br/><br/>
                                                                                                                        Procurez-vous notre spray désinfectant sans rinçage afin de garder vos mains et vos surfaces de travail parfaitement propres.<br/><br/>
                                                                                                                        Ses avantages :<br/>
                                                                                                                        - Ses propriétés désinfectantes garantissent un large spectre d’activité biocide, avec une rapidité d’action et laisse des surfaces parfaitement nettoyées sans trace.<br/>
                                                                                                                        - Virucide selon la norme EN 14476, efficace contre polyovirus, adénovirus, influenza virus (H1N1 Grippe A, H5N1 Grippe aviaire), hépatite B et C, HIV, Rotavirus (gastro enterite), virus Herpès simplex<br/>
                                                                                                                        - Bactéricide selon la norme EN 13727/Fongicide selon la norme EN 1275<br/>
                                                                                                                        - Label ECOCERT<br/><br/>
                                                                                                                         Précautions d’emploi :<br/>
                                                                                                                        - Utiliser ce spray antibactérien avec précaution. Avant toute utilisation, lisez l’étiquette et les informations concernant le produit.<br/>
                                                                                                                        - Ne pas mélanger à d’autres produits.<br/>
                                                                                                                        - Reproduire l’étiquetage si transvasement dans un autre contenant.<br/>
                                                                                                                        - Respecter les précautions de l’étiquetage réglementaire.<br/>
                                                                                                                        - L’emballage, vide ou contenant encore du produit, doit être éliminé en tant que déchet dangereux sous l’entière responsabilité du détenteur de ce déchet.<br/>
                                                                                                                        - Ne pas rejeter les résidus dans les égouts et les cours d’eau.<br/>
                                                                                                                        - En cas d’ingestion, ne pas faire vomir, consulter immédiatement un médecin et lui montrer l’emballage ou l’étiquette/Consulter le centre antipoison le plus proche.<br/>
                                                                                                                        - En cas de doute, faire un essai préalable sur une partie cachée afin de vérifier la compatibilité du produit avec les surfaces à traiter.<br/><br/>
                                                                                                                        Important : ce spray désinfectant contre le COVID-19 n’exonère absolument pas l'utilisateur de l’application des gestes barrières qui sont essentiels.""" , "cgi-bin/desinfectant.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (20, "gel", "Désinfectants", "750ml", 5, 99, """Désinfectant fabriqué en France.<br/><br/>
                                                                                                                        Gardez vos mains et toutes vos surfaces de travail propres et désinfectées grâce à notre spray désinfectant.<br/><br/>
                                                                                                                        A base d’alcool, destiné à la maîtrise des risques microbiologiques en environnement médical (hôpitaux, cliniques, maisons de retraite, crèches, etc.), il a été développé pour divers usages :<br/>
                                                                                                                        Pour la désinfection des surfaces lavables :<br/>
                                                                                                                        - Les plans de travail et paillasses<br/>
                                                                                                                        - L’ameublement (placard des patients, lits, chaises et fauteuils, chariots...)<br/>
                                                                                                                        - Les lunettes de toilettes<br/>
                                                                                                                        - Les plateaux repas<br/>
                                                                                                                        - Les poignées de portes<br/>
                                                                                                                        - Les banques réfrigérées et réfrigérateurs<br/>
                                                                                                                        - L’ensemble du matériel médical en contact avec les patients et le personnel médical.<br/><br/>
                                                                                                                        Procurez-vous notre spray désinfectant sans rinçage afin de garder vos mains et vos surfaces de travail parfaitement propres.<br/><br/>
                                                                                                                        Ses avantages :<br/>
                                                                                                                        - Ses propriétés désinfectantes garantissent un large spectre d’activité biocide, avec une rapidité d’action et laisse des surfaces parfaitement nettoyées sans trace.<br/>
                                                                                                                        - Virucide selon la norme EN 14476, efficace contre polyovirus, adénovirus, influenza virus (H1N1 Grippe A, H5N1 Grippe aviaire), hépatite B et C, HIV, Rotavirus (gastro enterite), virus Herpès simplex<br/>
                                                                                                                        - Bactéricide selon la norme EN 13727/Fongicide selon la norme EN 1275<br/>
                                                                                                                        - Label ECOCERT<br/><br/>
                                                                                                                         Précautions d’emploi :<br/>
                                                                                                                        - Utiliser ce spray antibactérien avec précaution. Avant toute utilisation, lisez l’étiquette et les informations concernant le produit.<br/>
                                                                                                                        - Ne pas mélanger à d’autres produits.<br/>
                                                                                                                        - Reproduire l’étiquetage si transvasement dans un autre contenant.<br/>
                                                                                                                        - Respecter les précautions de l’étiquetage réglementaire.<br/>
                                                                                                                        - L’emballage, vide ou contenant encore du produit, doit être éliminé en tant que déchet dangereux sous l’entière responsabilité du détenteur de ce déchet.<br/>
                                                                                                                        - Ne pas rejeter les résidus dans les égouts et les cours d’eau.<br/>
                                                                                                                        - En cas d’ingestion, ne pas faire vomir, consulter immédiatement un médecin et lui montrer l’emballage ou l’étiquette/Consulter le centre antipoison le plus proche.<br/>
                                                                                                                        - En cas de doute, faire un essai préalable sur une partie cachée afin de vérifier la compatibilité du produit avec les surfaces à traiter.<br/><br/>
                                                                                                                        Important : ce spray désinfectant contre le COVID-19 n’exonère absolument pas l'utilisateur de l’application des gestes barrières qui sont essentiels.""", "cgi-bin/desinfectant.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (21, "test", "Test anti-covid", "", 25, 99, """Lot de 5 Tests Antigénique.<br/><br/>
                                                                                                                        Le test rapide de l'antigène COVID-19 de CLUNGENE fournit des résultats dans un délai très court (15 - 20 minutes).<br/>
                                                                                                                        Le test rapide de CLUNGENE sur l'antigène COVID-19 est un test immunologique dit chromatographique en format de flux latéral. <br/>
                                                                                                                        Le test recherche des fragments de protéines du virus et donc sa présence directe et physique dans l'organisme. <br/>
                                                                                                                        Les résultats positifs indiquent la présence de l'antigène du SRAS-CoV-2. <br/><br/>
                                                                                                                        Coûts faibles par rapport à un test PCR<br/>
                                                                                                                        Résultats très rapides (15 min)<br/>
                                                                                                                        Sensibilité 97,5% et spécificité 99,4%.<br/>
                                                                                                                        Écouvillon nasal antérieur simple (nasal 25 mm), pas d'écouvillon dans la gorge<br/><br/>
                                                                                                                        Test officiel de laïcité <br/>
                                                                                                                        Liste officielle au BfArM """, "cgi-bin/test.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (22, "accessoire", "Boite de rangement de masque pliable", "", 5, 99, """1 Boîte de Rangement de Masque Pliable fabriquée en France.<br/><br/>
                                                                                                                                                    La boîte de rangement du masque est faite de matériau PP respectueux de l'environnement, sûr et hygiénique<br/>
                                                                                                                                                    Petit et exquis, vous pouvez le transporter avec vous et l'emporter lorsque vous l'utilisez.<br/>
                                                                                                                                                    La conception de la boucle bien emballée permet d'isoler efficacement la poussière et la saleté, et de garder le masque propre.<br/>
                                                                                                                                                    Conception avec couvercle, étanche à l'humidité et à la poussière.<br/><br/>
                                                                                                                                                    Plusieurs masques peuvent être stockés en même temps pour les besoins d'urgence.<br/><br/>
                                                                                                                                                    Caractéristiques:<br/>
                                                                                                                                                    - Matériau principal: matériau PP respectueux de l'environnement<br/>
                                                                                                                                                    - Taille du produit: 190 mm * 110 mm * 15 mm <br/>
                                                                                                                                                    - Poids: environ 64g""", "cgi-bin/boite.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (23, "accessoire", "Porte-clé sans-contact", "", 6, 99, """Lot de 3 Porte-Clé Sans-Contact fabriqués en France<br/><br/>
                                                                                                                                    NOUVELLE NORME - On nous encourage à éviter les poignées de portes qui peuvent être contaminées.<br/>
                                                                                                                                    Cet outil ouvre-porte possède également un stylet pour les écrans tactiles, claviers, et ATM. <br/><br/>
                                                                                                                                    ZERO CONTACT - Réduisez les contacts directs avec les gens ou les objets avec cet ouvre-porte.<br/>
                                                                                                                                    Il permet notamment d'enfoncer les boutons d'ascenseurs ou d'ouvrir un robinet sans rien toucher.<br/><br/>
                                                                                                                                    PRENEZ LE PARTOUT - Petit et léger, cet ouvre-porte entre facilement dans les sacs à mains, poches, ou portefeuilles. <br/>
                                                                                                                                    C'est aussi un porte clef, vous pouvez l'accrocher où vous voulez.<br/><br/>
                                                                                                                                    ROBUSTE ET ÉLÉGANT - Protégez-vous avec style avec cet ouvre porte.<br/>
                                                                                                                                    Sa jolie couleur dorée se fond facilement avec les clés ordinaires, et ses matériaux premium supporteront un usage quotidien. <br/><br/>
                                                                                                                                    DÉSINFECTION FACILE - Pour préserver le crochet des saletés, nous recommandons de le nettoyer chaque soir. <br/>
                                                                                                                                    Lavez-le au savon et à l'eau puis essuyez-le au désinfectant ou à l'alcool. <br/><br/>
                                                                                                                                    - Dimensions : 7.5 x 12 x 1.4 cm<br/>
                                                                                                                                    - Poids: 60 grammes """, "cgi-bin/porteCle.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (24, "accessoire", "Ajusteur de masque", "", 10, 99, """Lot de 10 Ajusteurs de Masque fabriqués en France.<br/><br/>
                                                                                                                                    Une aide pour porter un masque :<br/>
                                                                                                                                    Porter un masque pendant une longue période pourrait gêner les oreilles, tandis que cette barrette peut résoudre ce problème et le rendre plus facile à porter. <br/><br/>
                                                                                                                                    Convient pour les personnes qui ont besoin de porter des masques pendant une longue période, tels que les travailleurs exposés aux poussières, les travailleurs du domaine alimentaire, etc. <br/>
                                                                                                                                    6 niveaux pour différents besoins : barrette à 6 niveaux adaptée aux adultes, médecins, infirmières, enfants, etc.<br/>
                                                                                                                                    Matériau de qualité supérieure : la barrette pour masque est fabriqué en plastique durable qui est en mesure de vous offrir une expérience de port confortable.Cette barrette peut être lavée à plusieurs reprises, sûre et durable.<br/><br/>
                                                                                                                                    Compact et facile à utiliser : sa petite taille vous permet de le transporter facilement et de l'utiliser à tout moment et n'importe où. Vous pouvez l’enlever en 2 simples étapes.<br/><br/>
                                                                                                                                    Large application : convient pour différents types de masque avec connexion à deux points, tels que les masques jetables anti-poussière, etc.""", "cgi-bin/ajusteur.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (25, "accessoire", "Distributeur de gel automatique", "", 25, 99, """1 Distributeur de Savon à Capteur Automatique fabriqué en France.<br/><br/>
                                                                                                                                                    Équipé d'un capteur de mouvement infrarouge, le distributeur de savon libère automatiquement la lotion pour les mains dès que le capteur détecte vos mains.<br/>
                                                                                                                                                    Juste en tenant votre main, une quantité modérée de savon sortira facilement.<br/><br/>
                                                                                                                                                    Il a une conception transparente unique de grande capacité de 400 ml, pas besoin de remplacer le savon fréquemment, et il est compatible avec la plupart des types de liquides.tels que: <br/>
                                                                                                                                                    - gel hydroalcoolique<br/>
                                                                                                                                                    - savon pour les mains<br/>
                                                                                                                                                    - liquide vaisselle shampoing<br/>
                                                                                                                                                    - gel douche, lotion, etc.<br/><br/>
                                                                                                                                                    Étant donné que le distributeur de savon est alimenté par batterie et ne nécessite pas de prise, pas besoin de le charger et de l'installer.<br/>
                                                                                                                                                    Le distributeur de savon du capteur étanche IPX7, conçu avec une base étanche et des joints en caoutchouc pour empêcher l'eau de pénétrer dans le compartiment des piles.<br/><br/>
                                                                                                                                                    Il a un contrôle de distribution variable, le volume de savon avec le commutateur +/- vous permet de contrôler le volume de liquide libéré de 0,3 s à 2 s (6 réglages).<br/>
                                                                                                                                                    Vous n'avez pas besoin d'arrêter l'appareil, il se mettra automatiquement en veille lorsqu'il ne fonctionnera pas.""", "cgi-bin/distributeur.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (26, "kit", "Kit pour particulier", "", 22, 99, """1 Kit pour Particulier<br/><br/>
                                                                                                                                - 2 masques en tissu<br/>
                                                                                                                                - 1 flacon de gel hydroalccolique (250ml)<br/>
                                                                                                                                - 1 lot de 3 porte-clé sans-contact<br/><br/>
                                                                                                                                Économie de 5€""", "cgi-bin/kitParticulier.png"))

    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (27, "kit", "Kit pour entreprise", "", 110, 99, """1 Kit pour Entreprise<br/><br/>
                                                                                                                                - 5 boîte de 50 masques chirurgicaux<br/>
                                                                                                                                - 2 flacon de gel hydroalccolique (500ml)<br/>
                                                                                                                                - 1 distributeur de gel automatique<br/>
                                                                                                                                - 1 bouteille de désinfectant (5l)<br/><br/>
                                                                                                                                Économie de 26€""", "cgi-bin/kitEntreprise.jpg"))
conn.commit()
##    cursor.execute("""insert into PRODUIT values(?, ?, ?, ?, ?, ?, ?, ?)""", (10, "masque", "Masque en tissu", "Noir", 8, 99, """""", "img.jpg"))
##
