from googlesearch import search

results = search("Prateek Chaplot")

# for result in results:
#     print(result)

# print(results[0])

# results.gi_yieldfrom
first = ""
for index, result in enumerate(results):
    first = result
    if index == 0:
        break

print(first)
