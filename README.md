
# Thought Embedding Application

This repository contains a simple Streamlit application for embedding and analyzing user thoughts using PostgreSQL and Principal Component Analysis (PCA).

## Table of Contents

- [Cloud Setting](#cloud_setting)
- - [API](#API)
- - [Queries](#Queries)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
  - [import_embedding.py](#import_embedding.py)
  - [stream_app.py](#stream_app.py) 
  - [utils.py]
- [License](#license)

## Cloud Setting
1. Create a Google Cloud Account
2. Create an AlloyDB Cluster
3. Create an AlloyDB instance

### API
Enable below APIs:
1. AlloyDB API
2. Compute Engine API
3. Cloud Resource Manager API
4. Service Networking API

### Queries
#### Create table
CREATE TABLE "public".thought_embedding (
    thought TEXT,
    thought_id SERIAL PRIMARY KEY,
    entry_date TIMESTAMP
);

#### Enable below extensions
CREATE EXTENSION IF NOT EXISTS vector
CREATE EXTENSION IF NOT EXISTS google_ml_integration

#### Query to autogenerate vectors
ALTER TABLE thought_embedding ADD COLUMN embedding vector GENERATED ALWAYS AS (embedding('textembedding-gecko@001',thought)) STORED;

## Functions Overview

### import_embedding.py
- **`getconn()`**:  Establishes connection to PostgreSQL using Google Cloud AlloyDB.

- **`inserttodb(thought: str)`**:  Inserts a user thought into the PostgreSQL database.

- **`getembedding()`**:  Retrieves all stored thought embeddings from the database.

- **`similar_thoughts(thought)`**:  Finds top 3 similar thoughts based on vector similarity.

### stream_app.py

- **User Interface**:  Collects and records thoughts, displaying similar entries and PCA plot.

### utils.py

- **`compute_pca()`**:  Performs PCA on embeddings, returning principal components for visualization.

### Requirements

- Python 3.8+
- PostgreSQL
- Google Cloud AlloyDB
- Required Python packages:

```bash
pip install sqlalchemy streamlit pandas matplotlib scikit-learn pg8000
```
![image](https://github.com/user-attachments/assets/6381166d-551c-4da3-8a35-e0e59de0610d)
