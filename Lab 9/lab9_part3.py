import urllib.request
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
#         a = j.split("<")[0]
#         print(a)

# import urllib.request
# f = urllib.request.urlopen()
# f = urllib.request.urlopen("http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=hi")
# f.close()
# print(page)

variants = ["five-year anniversary", "fifth anniversary"]
l = []

a = 0

def choose_variant(variants):
    for i in range(len(variants)):
        variant = variants[i].replace(" ", "+")
        link = "https://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=" + variant
        # print(link)
        f = urllib.request.urlopen(link)
        page = f.read().decode("utf-8")
        f.close()
        for j in page.split("<span>"):
            # print(j.find("0 results"))
            if j.find("0 results") != -1:
                a = j.split("<")[0]
                l.append((a,variants[i]))
                # print(a)
        # for j in page.split("0 results"):
        #     if j.find("0 results") >= 0:
        #         l.append(j)
        # l.append()
    L = []
    for k in range(len(l)):
        L.append((len(l[k][0]),l[k][1]))
    # print(L)
    if max(l)[1] == max(L)[1]:
        print(max(l)[1])
    else:
        print(max(L)[1])
    #
    # print(l)
    # print(sorted(l)[-1][1])


# print(l)

















