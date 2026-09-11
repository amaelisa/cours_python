#1. interagir avec l'utilisateur
nom_utilisateur = input("Quel est ton prenom ? ")
print("Enchante(e)", nom_utilisateur, "! Bienvenue dans ton programme python.")

#2. conversion de texte en nombre (int)
age_saisi = input("Quel est votre age ? ")
age = int(age_saisi)

#3. Prise de decision (if / elif/ else)
if age < 18:
    print("Tu es mineur(e). Bon courage pour les etudes !")
elif age >= 18 and age < 25:
    print("Tu es dans la tranche d'age ideale pour reussir ton stage et ton memoire !")
else:
    print("Bienvenue dans le monde professionnel !")
    
#4. Excercie : Question Oui \ Non 
reponse = input("Aimes-tu le developpement web ? (oui/non) : ")

if reponse.lower() == "oui":
    print("super On va concevoir de superbes API avec Python et FastApi !")

else:
    print("Ne t'inquietes pas, tu vas u=y prendre gout tres vite !")