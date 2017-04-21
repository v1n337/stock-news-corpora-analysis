trend_terms_all = {'surge', 'rise', 'shrink', 'jump', 'drop', 'fall', 'plunge', 'gain', 'slump'}

trend_terms_1 = {'surge', 'rise', 'drop'}
trend_terms_2 = {'drop', 'fall', 'plunge', 'gain', 'slump'}


print(trend_terms_1 & trend_terms_2)

if trend_terms_1 & trend_terms_2:
    print("non-empty set")
else:
    print("no object")
