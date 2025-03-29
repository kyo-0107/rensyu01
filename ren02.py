import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv("cars.csv")

# データ確認
print(df)
df.columns = df.columns.str.strip()  # カラム名の前後の空白を削除
print(df.columns.tolist())  # カラム名一覧をリスト形式で表示
# 馬力と燃費の散布図
plt.scatter(df['馬力'], df['燃費（km/L）'])
plt.title('馬力 vs 燃費')
plt.xlabel('馬力')
plt.ylabel('燃費（km/L）')
plt.grid(True)
plt.show()

# 価格ランキング棒グラフ
df.sort_values(by='価格（万円）', ascending=False).plot(x='車種', y='価格（万円）', kind='bar', legend=False)
plt.title('車種ごとの価格比較')
plt.ylabel('価格（万円）')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()