import pandas as pd
# Series Class = Value + Index, value of Index is Index label
s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=["서울", "부산", "인천", "대구"])
print(s)

print(pd.Series(range(10, 14)))
print(s.index)
print(s.values)

s.name = "인구"
s.index.name = "도시"
print(s)

# Series Calculate
print(s / 1000000)

# Series Indexing
print(s[1], s["부산"])
print(s[3], s["대구"])
print(s[[0, 3, 1]])
print(s[["서울", "대구", "부산"]])
print(s[(250e4 < s) & (s < 500e4)])  
# 250e4 < index label < 500e4

print(s[1:3])
print(s["부산":"대구"])
s0 = pd.Series(range(3), index=["a", "b", "c"])
print(s0)
print(s0.a)
print(s0.b)

# Series and Dictionary
print("서울" in s)
print("대전" in s)
# s.items method approach key & value
for k, v in s.items():
    print("%s = %d" % (k, v))
    
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158})
print(s2)

s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
               index=["부산", "서울", "인천", "대전"])
print(s2)

ds = s - s2
print(ds)
print(ds.notnull())
print(ds[ds.notnull()])

rs = (s - s2) / s2 * 100
rs = rs[rs.notnull()]
print(rs)

rs["부산"] = 1.63
print(rs)

del rs["서울"]
print(rs)

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)