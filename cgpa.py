import pandas as pd

sdf = pd.DataFrame({
    "a": (1,2,3),
    "b": ("anmol","asdf","qwerty")
})

# s = sdf[sdf["a"]>2]
s = sdf["a"]/sdf["a"].max()
print(type(s))
print(s)

# print(sdf)
# print(type(sdf))
