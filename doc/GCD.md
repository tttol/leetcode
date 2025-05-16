
# ユークリッドの互除法の性質
```
A % B = Rの時、GCD(A, B) = GCD(B, R)である
```
# フロー
```mermaid
flowchart TD
    Start([開始])
    Input[入力: 2つの整数 a, b]
    CheckZero{b == 0?}
    OutputGCD[出力: a が最大公約数]
    ModCalc[一時変数 r に a % b を代入]
    Assign[次の a に b、b に r を代入]
    End([終了])

    Start --> Input --> CheckZero
    CheckZero -- はい --> OutputGCD --> End
    CheckZero -- いいえ --> ModCalc --> Assign --> CheckZero
```

# 実装
### 再帰
```py
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)
```

### while
```py
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```