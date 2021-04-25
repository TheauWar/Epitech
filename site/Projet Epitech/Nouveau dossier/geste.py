import cgi
import cgitb
import sys
cgitb.enable()
import sqlite3

params = {}
fieldStorage = cgi.FieldStorage()
for key in fieldStorage.keys():
    params[key] = fieldStorage[key].value
if "recherche" in params.keys():
    recherche = params["recherche"]
else:
    recherche = None

if "p" in params.keys():
    page = int(params["p"])
else:
    page = 1


form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

if form.getvalue("recherche") is None and recherche is None:
    html = """<html><head>
	<meta charset="utf_8">
	<title>Epitech - La covid 19</title>
	<style type="text/css">

	head{
		background-color:red;
	}

	.categorie_produit{

       	margin-left:20%;
	}

	.recherche{
		margin-left: 75%;
		top:0;
		width: 20%;}

	.caddie{
		float:left;
		height: 30px;
		width: auto;
		margin-left:98%;
		padding-top:0%;}


	body
		{background-image: url("cgi-bin/bg.jpg");
		font-family:Arial,Verdanasans-serif;
		}

	h1
		{color : black;
		font-size : 200%;
		background : none;
		text-align : center;
        text-decoration: underline;
		}
	h2
		{color : black;
		font-size : 150%;
		top:50%;
		text-decoration: underline;
		}
	ul
		{
		list-style-type : none;
		}

	#menu
		{position: fixed;
		left: 5;
		top: 10%;
		width: 15%;
		background:rgb(225,225,225);
		border-radius: 10px;
		}

	.boutonmenuprincipal {
            background-color: black;
            color: white;
            border: none;
            cursor: pointer;
            width: 200px;
            padding:20px;
            margin-top:20px;
            font-size: 30px;
            }
    .boutonmenuprincipal:hover {
            background-color: grey;
            }
    .dropdown {
            position: fixed;
            display: inline-block;
			top: 10%;
			width: 15%;
			left: 5px;
            }
    .dropdown-child {
            display: none;
            background-color: white;
            min-width: 50px;
            }
	.dropdown-child a {
            color: black;
            padding: 20px;
            text-decoration: none;
            display: block;
            }
    .dropdown:hover .dropdown-child {
            display: block;
            }

	#bouton_valider{
		position :static;
		margin-left:75%;
		top:5%;
	}
	.table{
		width:50%;
		height: auto;
		}

	.tableau{
		width: 50%;
		height: auto;
		margin-left:15%;
	}
    .imageTop{
        border: solid;
        border-color:grey;
        width: 250px;
        height: auto;
    }

    .logo{
        height: 10%;
        width: auto;
    }
    
    .img_mesure{
        margin-left:15%;
    }
	</style>
</head>
<body>


	<h1>Covishop<img class="logo" src = "cgi-bin/logo.png"/></h1>
	<img class="caddie" src="cgi-bin/caddie.png" alt="image_panier">
	<label for="recherche"></label>
    <form accept-charset="utf-8" action = "accueil.py">
	<input type="text" class="recherche" name="recherche" maxlength="16" size="10" placeholder="Vous recherchez quelque chose ?">
	<input type="submit" id="bouton_valider" value="Rechercher">
    </form>




	<div class="dropdown">
		<button class="boutonmenuprincipal"> Menu</button>
		<div class="dropdown-child">
			<a href="accueil.py">Accueil</a>
			<a href="produit.py">Nos produits</a>
			<a href="production.py">Production</a>
		</div>
	</div>


	<h2 class="categorie_produit">Pour tous se proteger !</h2>

    <img src="cgi-bin/mesures_barrieres.jpg" class="img_mesure">

</body>
</html>
"""
else:
    with sqlite3.connect("bddCovid.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select NOMP, IDP, IMAGE from PRODUIT where NOMP like '%{}%'".format(recherche))
    wsh = cursor.fetchall()

    uwu = []
    temp = []

    for elt in wsh:
        if elt[0] not in uwu:
            uwu.append(elt[0])

            temp.append(elt)

    i = len(temp)

    p = []
    for k in range((i-1)//6+1):
        p.append(temp[6*k:6*k+6])

    html = """<head>
	<meta charset="utf_8">
	<title>Epitech - La covid 19</title>

        <style type="text/css">

            head{
                background-color:red;
            }

            .categorie_produit{
                margin-left:20%;
            }

            .recherche{
                margin-left: 75%;
                top:0;
                width: 20%;}

            .caddie{
                float:left;
                height: 30px;
                width: auto;
                margin-left:98%;
                padding-top:0%;}


            body
                {background-image: url("cgi-bin/bg.jpg");
                font-family:Arial,Verdanasans-serif;
                }

            h1
                {color : black;
                font-size : 200%;
                background : none;
                text-align : center;
                text-decoration: underline;
                }
            h2
                {color : black;
                font-size : 150%;
                top:50%;
                text-decoration: underline;
                }
        .logo{
            height: 10%;
            width: auto;
        }
            ul
                {
                list-style-type : none;
                }

            #menu
                {position: fixed;
                left: 5;
                top: 10%;
                width: 15%;
                background:rgb(225,225,225);
                border-radius: 10px;
                }

            .boutonmenuprincipal {
                background-color: black;
                color: white;
                border: none;
                cursor: pointer;
                width: 200px;
                padding:20px;
                margin-top:20px;
                font-size: 30px;
                }
            .boutonmenuprincipal:hover {
                    background-color: grey;
                    }
            .dropdown {
                    position: fixed;
                    display: inline-block;
                    top: 10%;
                    width: 15%;
                    left: 5px;
                    }
            .dropdown-child {
                    display: none;
                    background-color: white;
                    min-width: 50px;
                    }
            .dropdown-child a {
                    color: black;
                    padding: 20px;
                    text-decoration: none;
                    display: block;
                    }
            .dropdown:hover .dropdown-child {
                    display: block;
                    }

            #bouton_valider{
                position :static;
                margin-left:75%;
                top:5%;
            }


            .image_categorie{
                height: 200px;
                width: auto;
            }

            .presentation{
                padding-left:15%;
                width:auto;
            }

            .table{
                width:50%;
                height: auto;
            }

            .tableau{
                width: 50%;
                height: auto;
                margin-left:15%;
            }
            .img{
                width: 50%;
                height: auto;
            }

            #nb_page{
                text-align: center;
            }

            </style>
</head>
	<body>
	<h1>Covishop - Recherche<img class="logo" src = "cgi-bin/logo.png"/></h1>
	<div class="dropdown">
		<button class="boutonmenuprincipal"> Menu</button>
		<div class="dropdown-child">
			<a href="accueil.py">Accueil</a>
			<a href="produit.py">Nos produits</a>
			<a href="production.py">Production</a>
		</div>
	</div>
    <form action = accueil.py>
	<label for="recherche"></label>
	<input type="text" class="recherche" name="recherche" maxlength="16" size="10" placeholder="Vous recherchez quelque chose ?">
	<img class="caddie" src="cgi-bin/caddie.png" alt="image_panier">
    <input type="submit" id="bouton_valider" value="Rechercher">
    </form>

	<div class="categorie_produit">
		<h2>Résulat(s) de la recherche :</h2>
	</div>

    <div class="tableau">

        <table>"""
    if i != 0:
        x = len(p[page-1])
        compteur = 0
        html += "<tr>"
        for elt in p[page-1]:
                html += """
    				<td width="10%">
    				<h2><a href='article.py?item="""+str(elt[1])+"""'>"""+elt[0]+"""</a></h2>
    					<a href='article.py?item="""+str(elt[1])+"""'><img class = 'img' src='"""+elt[2]+"""' class="image_categorie"></a>
    				</td>"""
                if compteur == 2:
                    html+= "<tr></tr>"
                compteur +=1

        html += "</tr>"


    else:
        html += """<p>Aucun produit ne correspond à votre recherche.</p>"""
    html += """</table><p id="nb_page">"""

    for w in range(len(p)):
        html+="""<a href='accueil.py?p="""+str(w+1)+"""&recherche="""+recherche+"""'>"""+str(w+1)+"""</a> ;"""


    html= html[:-1]
    html += """</p></body>
	</html>"""


sys.stdout.buffer.write(html.encode('utf-8') + b'\n')
