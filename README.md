# Recipe Ingredient Clustering and Analysis

This repository contains a complete pipeline for **preprocessing, embedding, clustering, and analyzing recipe ingredients**. The workflow is implemented across multiple Jupyter notebooks, from raw data cleaning to semantic cluster evaluation using TF-IDF and cosine similarity.

---

## Notebooks Overview

### 0_process_raw_data.ipynb
- **Purpose:** Load raw CSV files (`recipes.csv` and `terms.csv`), merge them, and select relevant columns (`name_x`, `nutrition`, `n_steps`, `ingredients_y`, `minutes`).  
- **Output:** Cleaned dataset saved as `data/clean_data/recipes.csv`.

### 1_ingredients_emb.ipynb
- **Purpose:** Preprocess and semantically cluster ingredients.  
- **Key Steps:**
  - Parse and clean raw ingredient text (lowercasing, lemmatization, synonym mapping, noise removal).  
  - Generate embeddings for unique ingredients using `SentenceTransformer` (`all-MiniLM-L6-v2`).  
  - Perform hierarchical clustering on embeddings based on cosine similarity.  
  - Visualize clusters with UMAP and produce statistics on cluster sizes and vocabulary reduction.  
- **Output:** `recipes_cleaned.csv` and `ingredient_dictionary.csv`.

### 2_ReducedDimension_DBSCAN_VS_HDBSCAN.ipynb
- **Purpose:** Cluster recipes and ingredients in reduced-dimensional space for analysis.  
- **Key Steps:**
  1. Load cleaned recipes and parse ingredients.  
  2. Build a sparse ingredient–recipe matrix and reduce dimensionality with **TruncatedSVD**.  
  3. Apply clustering algorithms: KMeans, MiniBatchKMeans, DBSCAN, HDBSCAN.  
  4. Evaluate clusters using silhouette, Calinski–Harabasz, and Davies–Bouldin scores.  
  5. Visualize clusters in 2D using UMAP and interactive Plotly plots.

### 3_tf_idf.ipynb
- **Purpose:** Refine and evaluate ingredient clusters using **TF-IDF**.  
- **Key Steps:**
  1. Load cleaned recipes and clustering labels.  
  2. Create cluster-level documents by aggregating ingredients and recipes.  
  3. Compute TF-IDF scores to identify the most characteristic ingredients per cluster.  
  4. Evaluate cluster purity using exclusivity, internal coherence, cuisine purity, semantic density, and size penalties.  
  5. Save comprehensive TF-IDF and purity reports per clustering method.

### 4_tf_idf_cos.ipynb
- **Purpose:** Advanced ingredient-level clustering using TF-IDF embeddings with **cosine similarity**.  
- **Key Steps:**
  1. Load cleaned recipes and ingredient lists.  
  2. Build and reduce a recipe–ingredient TF-IDF matrix using **TruncatedSVD**.  
  3. Apply **DBSCAN** and **HDBSCAN** clustering.  
  4. Identify top ingredients per cluster with TF-IDF.  
  5. Evaluate clusters via multiple metrics (exclusivity, internal coherence, cuisine purity, semantic density, size penalty).  
  6. Optionally compare with precomputed labels.  
  7. Export detailed TF-IDF and purity metrics to CSV files.

### keywords.py
- **Manual labeling** : Food and cuisine keyword mappings for cluster purity and theme detection.

---

## Installation

The environment can be set up using **conda** from the provided `environment.yml` file.

```bash
# Clone the repository
git clone https://github.com/Thomas-aub/Food_Mining.git
cd Food_Mining

# Create the environment
conda env create -f environment.yml

# Activate the environment
conda activate food_mining
```

### Dependencies included:

- Python 3.10+
- pandas, numpy, scikit-learn
- hdbscan, umap-learn
- sentence-transformers
- plotly
- Jupyter and notebook extensions

---

## Usage

1. **Start with raw data preprocessing:**  
   `0_process_raw_data.ipynb` → generates `recipes.csv`.

2. **Ingredient embedding and cleaning:**  
   `1_ingredients_emb.ipynb` → generates `recipes_cleaned.csv` and ingredient dictionary.

3. **Dimensionality reduction and clustering:**  
   `2_ReducedDimension_DBSCAN_VS_HDBSCAN.ipynb` → produces cluster labels and visualizations.

4. **TF-IDF cluster refinement and purity analysis:**  
   `3_tf_idf.ipynb` → produces cluster-level TF-IDF and purity reports.

5. **Advanced TF-IDF ingredient embeddings with cosine similarity:**  
   `4_tf_idf_cos.ipynb` → performs ingredient-level evaluation and generates combined CSV summaries.

---

## Output

- Cleaned datasets: `data/clean_data/recipes.csv`, `recipes_cleaned.csv`
- Ingredient dictionary: `data/clean_data/ingredient_dictionary.csv`
- Cluster labels (DBSCAN, HDBSCAN, KMeans, Agglomerative) : `notebooks/outputlabels`
- TF-IDF reports and purity metrics: `notebooks/tfidf/`

---

## Notes

- The pipeline is modular: you can skip steps if preprocessed datasets or labels already exist.  
- TF-IDF and cosine-based clustering analyses can be used for **ingredient recommendation**, **recipe similarity**, and **semantic analysis** of culinary data.
