import pandas as panda

data = {
    "isim":  ["Emin", "efe", "ali"],
    "yas":   [19, 20, 21],
    "sehir": ["İstanbul", "istanbul", "İstanbul"],
    "bolum": ["bilgisayar", "fizyoterapi", "havacılık elektriği"]
}
df = panda.DataFrame(data)
print(df[df["yas"] > 19])
