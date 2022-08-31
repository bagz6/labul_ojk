from turtle import left
import pandas as pd

neraca = pd.read_csv('d:/ojk/neraca_BPR_Juni_2022.csv')
kap = pd.read_csv('d:/ojk/kap_BPR_Juni_2022.csv')
k_bpr = neraca.merge(kap, on='Kode Bank', how='left')
ke_bpr = k_bpr.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'Nama BPR_y'], axis=1)
print(ke_bpr)

df = pd.DataFrame(ke_bpr)
df.to_csv('d:/ojk/Kesehatan_BPR_Juni_2022.csv')
# kes_bpr = ke_bpr[ke_bpr['KPMM'].isna()]
# print(kes_bpr)
# kes_bpr['Nama BPR_x'] = kes_bpr['Nama BPR_x'].replace(' ', '+')
# print(kes_bpr['Nama BPR_x'])
# namas = nama.replace(" ", "+")
# df = pd.DataFrame(namas)
# df.to_csv('d:/ojk/list_nama_ulang.csv')

# ref = nama.replace(' ', '+')
# df = pd.DataFrame(ref)
# df.to_csv('d:/ojk/list_nama_ulang.csv')

# print(df)
# print(kesehatan_bpr)
# print(kap)
# kap_edited = kap.drop_duplicates()
# print(kap_edited)

# neraca = pd.read_csv('d:/ojk/Kesehatan_BPR_Juni_2022_edited.csv')
# neracae = neraca['Kabupaten'].replace('Kota', 'Kota ')
# print(neracae)