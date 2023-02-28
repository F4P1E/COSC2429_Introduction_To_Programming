def test(dict, N):
    result = sorted(dict, key=dict.get, reverse=True)[:N]
    return result
dict = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
print("\nOriginal Dictionary:")
print(dict)
N = 1
print("\n",N,"maximum value(s) in the said dictionary:")
print(test(dict, N))
N = 2
print("\n",N,"maximum value(s) in the said dictionary:")
print(test(dict, N))
N = 5
print("\n",N,"maximum value(s) in the said dictionary:")
print(test(dict, N))
