import matplotlib.pyplot as plt
import numpy as np

# 時間の配列を作成
t = np.linspace(0, 1, 1000)

# デューティー比
duty = 0.50

# フーリエ級数展開で矩形波を作成
f = sum(
    4 / np.pi * (1 / n) * np.sin(n * 2 * np.pi * t / duty) for n in range(1, 100, 2)
)

# プロット
plt.plot(t, f)
plt.ylim(-1.5, 1.5)
plt.show()
