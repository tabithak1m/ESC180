text = open("text.txt", encoding="latin-1").read().split()

freq = {}
for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

import random

L = []
for i in range(100):
    L.append(int(random.random()*100))

def top10(L):
    L.sort()
    return L[-11:-1]


inv_freq = [(v, k) for k, v in freq.items()]
print(sorted(inv_freq)[-11:-1])




#
# # http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=SEARCHINPUT
#
#
# import urllib.request
# f = urllib.request.urlopen("https://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=python")
# page = f.read().decode("utf-8")
# f.close()
# # print(page.split("0 results"))
#
# # print(page.find("0 results"))
# # print(page[page.find("0 results")])
#
# for j in page.split("<span>"):
#     print(j.find("0 results"))
#     if j.find("0 results") != -1:
#         a = j[0].find("s")
#         print(j[0][0:a])
#         # print(j[0][])
#
# # import urllib.request
# # f = urllib.request.urlopen()
# # f = urllib.request.urlopen("http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=hi")
# # f.close()
# # print(page)
#
# variants = ["five-year+anniversary", "fifth+anniversary"]
# l = []
# #
# # def choose_variant(variants):
# #     for i in range(len(variants)):
# #         link = "https://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=" + variants[i]
# #         print(link)
# #         f = urllib.request.urlopen(link)
# #         f.close()
# #         for j in page.split("0 results"):
# #             if j.find("0 results") >= 0:
# #                 l.append(j)
# #         # l.append()
# #     print(l)
# #
# # print(l)


























