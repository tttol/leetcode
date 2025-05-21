# Cumulative Sum/累積和
> [!NOTE]
> prefix sum ともいう

- 定義
```
s[0] = 0
s[1] = a[0]
s[2] = a[0] + a[1]
...
s[i] = a[0] + a[1] + ... + a[i-1]
```
- s[i]＝i-1番目までの総和。`[0, i)`区間の総和とも言える。
# 実装
```py
cumsum = [0] * (n + 1) # 元の配列より要素数が一個多くなる！s[0] = 0なので。
cumsum[0] = 0
for i in range(1, n + 1):
    cumsum[i] = nums[i - 1] + cumsum[i - 1]
```

#　 s[0]=0の理由
- https://qiita.com/drken/items/56a6b68edef8fc605821#2-3-s_0--0-%E3%81%AE%E6%84%8F%E5%91%B3
- s[i]はiを含まない。s[0]は0番目を含まない総和となり、和は0になる。
