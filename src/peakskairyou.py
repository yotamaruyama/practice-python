import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("TRACE002.CSV", skiprows=11, encoding="shift-jis")

# 'Frequency'と'Amplitude'列を抽出
data = df[["Frequency", "Amplitude"]]
data["Frequency"] = data["Frequency"].str.replace("Hz", "").astype(float)
data["Amplitude"] = data["Amplitude"].str.replace("dBm", "").astype(float)

# データ列ごとに分割
frequency = data["Frequency"].values  # 周波数
amplitude = data["Amplitude"].values  # 振幅

# プロットする周波数範囲（基本周波数と奇数倍のピークのみ）
base_frequency = 1e6  # 基本周波数（1MHz）
max_frequency = frequency[-1]  # 計測周波数の最大値
plot_frequency = np.arange(
    base_frequency,
    max_frequency + 1,
    2 * base_frequency,
)  # 基本周波数の奇数倍

# 基本周波数と奇数倍のピークのインデックスを取得
peak_indices = []
for f in plot_frequency:
    index = np.abs(frequency - f).argmin()  # 最も近い周波数のインデックスを取得
    # ピークが極端に低い場合、その前後も探す
    if amplitude[index] < -60:
        for i in range(max(0, index - 5), min(len(frequency), index + 6)):
            if amplitude[i] > amplitude[index]:
                index = i
    peak_indices.append(index)

plt.plot(frequency / 1e6, amplitude, label="Spectrum")  # 周波数をMHz単位に変換
plt.scatter(
    frequency[peak_indices] / 1e6,  # 周波数をMHz単位に変換
    amplitude[peak_indices],
    color="red",
    label="Peaks",
)
plt.xlabel("Frequency [MHz]")  # x軸のラベルをMHz単位に変更
plt.ylabel("Amplitude [dBm]")
plt.legend()
plt.show()
# ピークの周波数と振幅を表示
for i in peak_indices:
    print(f"Frequency: {frequency[i]/1e6:.2f} MHz, Amplitude: {amplitude[i]:.2f} dBm")

# ピークの周波数と振幅をデータフレームに変換
peak_data = pd.DataFrame(
    {
        "Frequency": frequency[peak_indices] / 1e6,
        "Amplitude": amplitude[peak_indices],
    },
)

# CSVファイルに出力
peak_data.to_csv("peak_data.csv", index=False)
