## Pourquoi faire de la réduction de dimension

Dans notre cas, on part d’une **matrice “recettes × ingrédients”**, de très grande taille :

* quelques milliers de recettes,
* plusieurs centaines voire milliers d’ingrédients.

👉 Chaque ingrédient est une **dimension**.
On a donc un espace **hautement dimensionnel et très creux** (sparse).

**Conséquences :**

* Les distances (cosine, Jaccard, euclidienne…) deviennent **peu discriminantes** — beaucoup de points sont “presque à égale distance”.
* Les algorithmes de clustering (DBSCAN, KMeans…) perdent en performance.
* La visualisation devient impossible directement (plus de 2–3 dimensions).

La **réduction de dimension** permet donc de :

* **Projeter** ces données dans un espace plus petit (ex : 2D ou 3D) pour les visualiser ;
* **Dénser** légèrement les données → distances plus significatives ;
* **Accélérer** les algorithmes de clustering et d’analyse ;
* **Débruiter** la matrice initiale et faire ressortir les relations latentes entre ingrédients.

---

## 2. Méthodes possibles 



| Objectif                     | Méthode                                     | Adaptée à                  | Avantages                                                | Inconvénients                    |
| ---------------------------- | ------------------------------------------- | -------------------------- | -------------------------------------------------------- | -------------------------------- |
| Préparer clustering rapide   | **TruncatedSVD** (PCA pour matrices sparse) | TF-IDF ou binaire sparse   | Rapide, linéaire, compatible sklearn                     | linéaire uniquement              |
| Visualisation claire         | **t-SNE** ou **UMAP**                       | données denses ou réduites | capte non-linéarités, très lisible                       | plus lent, dépend des paramètres |
| Détection de structure dense | **UMAP + HDBSCAN**                          | données sparse             | très bon combo pour data mining exploratoire             | plus complexe à paramétrer       |
| Extraction de thématiques    | **NMF** (Non-negative Matrix Factorization) | TF-IDF                     | interprétable (chaque composante = groupe d’ingrédients) | nécessite tuning du rang         |

---

## Enjeux et limites

### 🔍 Enjeux

* **Compréhension** : visualiser des patterns, tendances, familles de recettes.
* **Communication** : présenter les résultats à un public non technique.
* **Feature engineering** : utiliser les composantes réduites comme “facteurs latents” dans un modèle de recommandation (ex : “recettes proches”).
* **Aide au choix du clustering** : si les points se séparent mal, il faut revoir la métrique ou la représentation.

### ⚠️ Limites

* t-SNE / UMAP **ne préservent pas les distances globales** (juste les voisinages).
  → Bonne visualisation, mais pas une “preuve” que les clusters sont séparés numériquement.
* La **stabilité** des projections dépend du random_state et des hyperparamètres.
* Attention à la **taille mémoire** : t-SNE et UMAP ne scalent pas bien sur 100k+ points.
