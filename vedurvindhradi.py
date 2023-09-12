d = dict()
d['Logn'] = (0, 0.2)
d['Andvari'] = (0.3, 1.5)
d['Kul'] = (1.6, 3.3)
d['Gola'] = (3.4, 5.4)
d['Stinningsgola'] = (5.5, 7.9)
d['Kaldi'] = (8.0, 10.7)
d['Stinningskaldi'] = (10.8, 13.8)
d['Allhvass vindur'] = (13.9, 17.1)
d['Hvassvidri'] = (17.2, 20.7)
d["Stormur"] = (20.8, 24.4)
d["Rok"] = (24.5, 28.4)
d['Ofsavedur'] = (28.5, 32.6)
d['Farvidri'] = (32.7, 200.0)

k = float(input())
for key, value in d.items():
    if value[0] <= k <= value[1]:
        print(key)
        break