from import_embedding import getembedding
from sklearn.decomposition import PCA
import numpy as np
import ast
import pandas as pd

def compute_pca():
   embedding_data=getembedding()
   float_embeddings = []
   thought_list = []
   for row in embedding_data:
      embedding_str = row.embedding
      embedding_list = ast.literal_eval(embedding_str)
      # embedding_list = [float(x) for x in embedding_str.split(',')]
      float_embeddings.append(embedding_list)
      thought_list.append(row.thought)
   float_embeddings = np.array(float_embeddings)

   print(type(embedding_data[0].embedding))
   pca=PCA(n_components=2)
   principalComponents=pca.fit_transform(float_embeddings)
   pca_with_labels = pd.DataFrame(principalComponents, columns=['PC1', 'PC2'])
   pca_with_labels['thoughts'] = thought_list
   # return True
   return pca_with_labels

