# UML & Appoche orientée Objet / Paradigmes de Programmation
## Partie 1
1. Une **Classe** est la representation d'un objet de la realite, alors qu'un **Objet** est une instance d'une classe. Exemple: la classe *Member* qui a les attributs name, email et l'object *M1* de name *jean* et d'email *jean@gmail.com*
2. l'**Encapsulation** est une technique de protection des donnees qui determine le niveau d'acces a une donnee; sur la classe *Loan*, elle s'appliquera sur ses attributs.
3. Difference:
* une **Association** est un lien d'egale a egale entre deux classe;
* une **Agregation** est une relation *maitre/esclave* entre deux classe où la destruction du maitre n'entraine pas forcement celle de ses esclaves;
* un **Composition** est une relation *maitre/esclave* entre deux classe où la destruction du maitre entraine celle de ses esclaves;
4. l'**Heritage** est une relation *parent/enfant* entre deux classes dans laquelle l'*enfant* herite de toute les proprietées publique de son parent; Oui il y'a un cas d'heritage dans ce systeme, car la classe *Member* possede les memes attributs de base que la classe *Librarian* et pour eviter de creer les memes attributs plusieurs fois il faut creer une classe parente dont ses enfants *Member et Librarian* heriterait de ses attributs de base.
5. le **Polymorphisme** est la capacite pour une meme methode de s'executer en fonction du contexte de la sous-classe dans laquelle elle se trouve; Exemple : Une methode de la classe *Person* calculerSalaire() qui s'excecutera d'une façon different selon le member ou le librarian.
6. Difference:
* Le **Diagramme de cas d'utilisation** montre les differentes sequences d'action qu'utilisateur sera emmener a faire lors de l'utilisation de l'application;
* Le **Diagramme de sequence** momtre comment une sequence d'action specifique ce deroule;
7. Difference:
* Une relation **include** entre une classe A et une classe B, signifie que pendant l'execution de A, B s'execute egalement; Exemple: La relation entre les cas << Emprunter un livre >> et << Valider un emprunt >> est *Include*,
* Une relation **extend** entre une classe A et une classe B, signifie que pendant l'execution de A, B peut egalement s'execute ; Exemple: La relation entre les cas << Emprunter un livre >> et << Suspendre un membre >> est *extend*.
10. L'**approche orientee object** permet de representée de façons visuel un systeme dans sa globalitée en ce basant sur le concept d'objet, alors que l'**approche procedural** se concentre plutôt sur les fonctions du systemes.
# Partie 2
1. 
Voici deux concepts encore plus disruptifs, qui s'attaquent à des secteurs où circulent des **milliards de FCFA de manière informelle ou opaque** au Cameroun. Ils combinent un impact social massif, une rentabilité explosive immédiate et un périmètre de développement strictement calibré pour être bouclé en un mois par un développeur rigoureux.

---

## 1. Mboa-Chantier : Le Tracker Anti-Fraude pour la Diaspora

**Le Problème Camerounais :** C'est le drame numéro un de la diaspora camerounaise. Des millions de personnes basées à l'étranger envoient des fonds massifs à des proches pour construire une maison au pays. Trop souvent, l'argent est détourné, les matériaux achetés sont de mauvaise qualité, ou le chantier est tout simplement fantôme. La confiance est brisée.

### La Révolution (Le Concept)

Une application web et mobile (SaaS) de **gestion et de supervision de chantiers à distance**, axée sur la transparence absolue.

1. Le propriétaire (Diaspora) crée le projet et définit les étapes (Fondations, Murs, Toiture).
2. Le chef de chantier (au pays) n'a qu'une seule tâche : via son téléphone, il valide chaque sous-étape en envoyant une **photo géolocalisée et horodatée** avec le détail des matériaux utilisés (ex: "Coulage de la dalle : 40 sacs de ciment Cimencam utilisés").
3. L'application génère un **Timeline interactif et haut de gamme** (style fil d'actualité moderne) et un tableau de bord financier : Argent envoyé vs Réalisation physique visible.

### Pourquoi c'est ultra-rentable ?

* **Pouvoir d'achat de la diaspora :** Un Camerounais de la diaspora préférera payer un abonnement de **10 000 FCFA à 15 000 FCFA (15€ à 22€) par mois** pour avoir l'esprit tranquille plutôt que de risquer de perdre 10 millions de FCFA.
* **B2B potentiel :** Les petites agences immobilières ou constructeurs locaux peuvent acheter une licence pour offrir ce service de "transparence" comme argument de vente à leurs clients.

### Le Plan de Route sur 4 Semaines (MVP)

* **Semaine 1 (Modélisation) :** Schéma UML centré sur trois entités : *Projet*, *Étape du Chantier*, et *Rapport Visuel* (Liaison image + coordonnées GPS + logs).
* **Semaine 2 (Backend API) :** API de gestion des fichiers (upload d'images optimisé) et système de calcul des dépenses/budgets restants.
* **Semaine 3 (Frontend UI/UX) :** Création d'une interface "Timeline" ultra-pro et épurée. Côté diaspora : des graphiques clairs sur l'évolution. Côté ouvrier : un bouton d'upload ultra-simple qui compresse l'image pour économiser la data locale.
* **Semaine 4 (Sécurité & Déploiement) :** Verrouillage des métadonnées des photos pour empêcher la triche (vérification que la photo a bien été prise le jour même sur le lieu du chantier) et mise en production.

---

## 2. Concours-Pass : Le Hub P2P de la Préparation aux Grandes Écoles

**Le Problème Camerounais :** Chaque année, des vagues de bacheliers et d'étudiants se lancent dans les concours les plus sélectifs du pays (Polytech, ENAM, CUSS, Beaux-Arts, IRIC, etc.). Les "cours de prépa" physiques coûtent extrêmement cher (parfois plus de 100 000 FCFA) et sont concentrés à Yaoundé et Douala. Les étudiants des autres régions n'ont accès qu'à des anciennes épreuves photocopiées, souvent mal corrigées, vendues à la sauvette aux carrefours.

### La Révolution (Le Concept)

Une plateforme de type **Marketplace P2P (Peer-to-Peer)** dédiée exclusivement aux corrigés et astuces des concours camerounais.

1. Les étudiants qui ont réussi ces concours majeurs (les "Majors") créent et uploadent des fiches de révision, des corrections détaillées en PDF, ou de courts audios d'explications de 5 minutes sur des sujets complexes.
2. Les candidats de tout le pays (Maroua, Bafoussam, Garoua, etc.) parcourent le catalogue et achètent la ressource spécifique dont ils ont besoin pour des micro-sommes (ex: 200 FCFA, 500 FCFA, 1000 FCFA).

### Pourquoi c'est ultra-rentable ?

* **L'effet de masse :** Le marché est gigantesque (des centaines de milliers de candidats chaque année). Si 5 000 candidats achètent en moyenne pour 2 000 FCFA de ressources sur votre plateforme, cela représente **10 000 000 FCFA** de flux. En prenant une commission de 20% sur chaque vente, votre plateforme génère un profit net automatisé, sans que vous n'ayez à produire le moindre contenu.

### Le Plan de Route sur 4 Semaines (MVP)

* **Semaine 1 (Architecture) :** Base de données structurée pour gérer un catalogue de produits digitaux (fichiers), les profils "Vendeurs certifiés" (les étudiants des grandes écoles) et les profils "Acheteurs".
* **Semaine 2 (Sécurité des fichiers) :** Backend robuste permettant de stocker les PDF en sécurité et d'intégrer une passerelle de simulation de paiement Mobile Money / Orange Money.
* **Semaine 3 (UI/UX Moderne) :** Design d'une interface type "E-Commerce de documents" ultra-rapide sur mobile. Un système de notation et d'avis (étoiles) pour garantir que les corrections vendues sont de haute qualité.
* **Semaine 4 (Automatisation) :** Système de reversement automatique des gains aux vendeurs (80%) après validation de l'achat, et lancement du MVP.

---

## Synthèse Impact & Faisabilité

>