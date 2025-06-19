import sys

def welcome_to_this_quizz():
    print("Bonjour et bienvenue dans ce Quizz sur la culture générale de la France!")
    print("Commençons !")

welcome_to_this_quizz()

qcm  = [
    {
        "question" : "1. Quelle est la date de la prise de la Bastille ?",
        "options" : ["(A): 14 juillet 1789" , "(B):4 août 1789", "(C):1er mai 1789" , "(D):26 Janvier 1790"],
        "reponse" : "A",
        "temps": 10
    },
    {
        "question" : "2.Quelle ville est surnommé 'La cité des Papes'?",
        "options": ["(A) : Lyon", "(B): Avignon" , "(C):Marseille " , "(D):Toulouse"],
        "reponse": "B",
        "temps": 10
    },
    {
        "question":"3.Quelle est le plus long fleuve de France",
        "options": ["(A) : Rhône", "(B): Garonne", "(C): Loire", "(D): Seine"],
        "reponse":"C",
        "temps": 10
    },
    {
        "question": "4.Qui a écrit les Misérables?",
        "options":["(A): Honoré De Balzac" , "(B): Victor Hugo" , "(C): Emile Zola" , "(D): Alexandre Dumas"],
        "reponse":"B",
        "temps": 10
    },
    {
        "question":"5.Quelle est la devise de la République Française?",
        "options" : ["(A): Liberté , Ordre , Nation ", "(B) : Unité,Travail,Patrie" , "(C):Liberté, Egalité, Fraternité","(D): La Force et L'honneur"],
        "reponse":"C",
        "temps": 10
    },
    {
        "question":"6.Quelle joueur français a remporté le Ballon d'Or en 1998?",
        "options": ["(A): Karim Benzema", "(B): Zinedine Zidane" , "(C): Michel Platini", "(D): Thierry Henry"],
        "reponse":"B",
        "temps":10
    },
    {
        "question":"7.Quelle spécialité culinnaire est associé à la région lyonnaise?",
        "options":["(A):Cassoulet","(B):Quenelle","(C):Choucroute","(D):Tarte Tatin"],
        "reponse":"B",
        "temps":10
    },
    {
        "question":"8.Quelle chaîne de montagne sépare la France et l'Espagne?",
        "options":["(A):Les Alpes","(B):Les Vosges","(C):Le Jura", "(D):Les Pyrénnées"],
        "reponse":"A",
        "temps": 10
    },
    {
        "question":"9.Quelle équipe de handball masculine française a remporté 6 titres de champion du monde?",
        "options":["(A):Les Bleus","(B):Les Tricolores","(C):Les Coqs","(D):Les Experts"],
        "reponse":"D",
        "temps":10
    },
    {
        "question":"10.Quel roi est surnommé le Roi Soleil?",
        "options":["(A):Louis XIV","(B):Louis XVI","(C):Henri IV","(D):François 1er"],
        "reponse":"A",
        "temps": 10
    },
    {
        "question":"11.Quel monument fut construit pour l'Exposition universelle de 1889?",
        "options":["(A):Le Louvre","(B):La Tour Eiffel","(C):L'Arc de Triomphe","(D):Notre-Dame"],
        "reponse":"A",
        "temps": 10
    },
    {
        "question":"12.Qui est le joueur le plus décisif de l'histoire de l'Equipe de France de Handball?",
        "options":["(A):Sadou Ntanzi","(B):Elohim Prandi","(C):Luka Karabatic","(D):Nikola Karabatic"],
        "reponse":"D",
        "temps" : 10
    },
    {
        "question":"13.Quel est le style architectural de la cathédrale de Notre-Dame de Paris?",
        "options":["(A):Roman","(B):Gothique","(C):Baroque","(D):Renaissance"],
        "reponse":"B",
        "temps": 10
    },
    {
        "question":"14.Quelle ville est célèbre pour sa course cycliste annuelle 'Paris-Roubaix'?",
        "options":["(A):Lille","(B):Roubaix","(C):Amiens","(D):Calais"],
        "reponse":"B",
        "temps":10
    },
    {
        "question":"15.Qui était le premier président de la cinquième République Française?",
        "options":["(A):François Mitterand","(B):Charles de Gaulle","(C):Georges Pompidou","(D):Valéry Giscard d'Estaing"],
        "reponse":"B",
        "temps": 10
    },
    {
        "question":"16.Qui a peint La Liberté guidant le peuple?",
        "options":["(A):Ingres","(B):Courbet","(C):Delacroix","(D):David"],
        "reponse":"C",
        "temps": 10
    },
    {
        "question":"17.Quelle est la langue régionale parlée en Bretagne?",
        "options":["(A):Alsacien","(B):Basque","(C):Occitan","(D):Breton"],
        "reponse":"D",
        "temps": 10
    },
    {
        "question":"18.Quelle est la fête nationale française?",
        "options":["(A):1er Mai","(B):14 Juillet","(C):11 novembre","(D):25 Décembre"],
        "reponse":"B",
        "temps": 10
    },
    {
        "question":"19.Quel est le nom du Parlement français?",
        "options":["(A):l'Assemblée Populaire","(B):Le Sénat","(C):Le Parlement composé du Sénat et de l'Assemblée Nationale","(D):Le Congrès de la République"],
        "reponse":"C",
        "temps": 10
    },
    {
        "question":"20.Qui est le joueur le plus décisif de l'histoire de l'Equipe de France de football?",
        "options":["(A):Thierry Henry","(B):Karim Benzema","(C):Kylian Mbappé","(D):Antoine Griemann"],
        "reponse":"C",
        "temps": 10
    }
]

score = 0  # Initialisation du score

for q in qcm:
    print("-" * 40)
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    reponse = input("Votre réponse : ").upper()

    if reponse == q["reponse"]:
        print("Bonne réponse !\n")
        score += 1
    else:
        print(f"Réponse incorrecte ! La bonne réponse était {q['reponse']}.\n")

    print("-" * 40)

print("-" * 40)
print(f"Quiz terminé ! Votre score est {score} sur {len(qcm)}.")
print(f"Vous avez obtenu {score} points sur 20.")
print("-" * 40)