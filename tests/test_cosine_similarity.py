import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

arr_1 = np.array([0, 1, 2]).reshape(1, -1)
arr_2 = np.array([0, 1, 3]).reshape(1, -1)

print(cosine_similarity(arr_1, arr_2)[0][0])

