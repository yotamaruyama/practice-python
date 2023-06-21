import io

import matplotlib.pyplot as plt
import pandas as pd

# CSVファイルの内容を直接指定
csv_data = """Frequency,Amplitude
978260.869565,-12.84657288
3043478.26087,-89.57724762
5000000.0,-27.14009476
6956521.73913,-30.25602722
9021739.130435,-91.22879028
10978260.869565,-34.86124039
13043478.26087,-98.52215576
15000000.0,-38.74108124
16956521.73913,-40.6708107
19021739.130435,-97.49814606
20978260.869565,-44.70291901
23043478.26087,-99.14854431
25000000.0,-49.04697037
26956521.73913,-51.32144165
29021739.130435,-99.06274414
30978260.869565,-56.56246185
33043478.26087,-99.0848465
35000000.0,-63.54853058
36956521.73913,-67.68768311
39021739.130435,-99.57354736
40978260.869565,-76.81336975
43043478.26087,-98.00592804
45000000.0,-85.80337524
46956521.73913,-90.30324554
49021739.130435,-98.62519836
"""

# CSVデータを文字列IOとして読み込む
df = pd.read_csv(io.StringIO(csv_data))

# データをグラフ化
plt.plot(df["Frequency"], df["Amplitude"])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dBm)")
plt.title("Spectrum Analyzer Data")
plt.grid(True)
plt.show()
