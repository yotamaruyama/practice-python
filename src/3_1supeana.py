import matplotlib.pyplot as plt
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv(
    "TRACE003.CSV",
    skiprows=11,
    encoding="shift-jis",
)  # 'your_file.csv'はあなたのCSVファイルのパスに置き換えてください

# 'Frequency'と'Amplitude'列を抽出
data = df[["Frequency", "Amplitude"]]
# data["Frequency"] = data["Frequency"].astype(float)
data["Frequency"] = data["Frequency"].str.replace("Hz", "").astype(float)
data["Amplitude"] = data["Amplitude"].str.replace("dBm", "").astype(float)


# データをグラフ化
plt.plot(data["Frequency"], data["Amplitude"])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dBm)")
plt.title("Spectrum Analyzer Data")
plt.grid(True)
plt.show()
