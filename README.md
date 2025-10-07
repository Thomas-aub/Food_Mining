# Food Mining

## Overview
This project focuses on **data mining and analysis of food recipes**.  
The goal is to clean, standardize, and semantically group ingredients, then explore patterns in recipes, nutrition, and cuisine types.

Key objectives:
1. **Ingredient cleaning and normalization**:
   - Lowercase, remove accents and punctuation.
   - Deduplicate and unify similar ingredients (e.g., "tomatoes" vs "cherry tomatoes").
2. **Semantic grouping**:
   - Use embeddings (SentenceTransformers) to cluster similar ingredients.
   - Reduce vocabulary size while keeping semantic meaning.
3. **Data analysis & pattern discovery**:
   - Explore ingredient co-occurrences.
   - Identify clusters of recipes with similar ingredient profiles.
   - Detect patterns by cuisine/country, nutrition, or recipe complexity.
4. **Visualization**:
   - UMAP projections of ingredient embeddings.
   - Histograms, bar charts, and scatter plots to explore clusters.
5. **Output**:
   - A clean, reduced dataset ready for downstream analysis or ML.

---

## Dataset
- Input: `data/clean_data/recipes_cleaned.csv`  
  (contains recipes with ingredients, nutrition, steps, etc.)
- Output: `data/clean_data/ingredients_reduced.csv`  
  (recipes with cleaned and semantically grouped ingredients)

---

## Quick Start

### 1️⃣ Create a Conda Environment

```bash
conda env create -f environment.yml
conda activate food_mining
```

### 2️⃣ Install via pip (optional)

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the notebook

1. Open `Food_Mining.ipynb` in Jupyter or VS Code.

2. Follow the steps:
    - Load and parse the recipes dataset.
    - Clean ingredients and generate embeddings.
    - Cluster ingredients and apply the mapping to recipes.
    - Explore clusters and visualize patterns.
    - Save the cleaned CSV for further analysis.

### 4️⃣ Explore & analyze

- Use `ingredients_reduced.csv` for:
    -Co-occurrence analysis.
    -Country or cuisine-based grouping.
    -Nutrition or preparation time patterns.
    -Machine learning or recommendation systems.

## Requirements

- Python 3.10+
- See `environment.yml` or `requirements.txt` for full dependencies.