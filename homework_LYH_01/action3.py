import numpy as np, pandas as pd

# 导入数据
print('*' * 50 + '原始数据' + '*' * 50)
df = pd.read_csv('data/car_data_analyze/car_complain.csv')
print(df)

# 数据预处理
print('*' * 50 + '原始数据预处理' + '*' * 50)
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))
print(df)

# 按品牌统计投诉总数
print('*' * 50 + '按品牌统计投诉总数' + '*' * 50)


def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x


df['brand'] = df['brand'].apply(f)
result1 = df.groupby(['brand'])['id'].agg(['count'])
print(result1.sort_values('count', ascending=False))

# 按车型统计投诉总数
print('*' * 50 + '按车型统计投诉总数' + '*' * 50)
result2 = df.groupby(['car_model'])['id'].agg(['count'])
print(result2.sort_values('count', ascending=False))

# 品牌的平均车型投诉最多
print('*' * 50 + '按品牌的平均车型投诉排序' + '*' * 50)
result3 = df.groupby(['brand', 'car_model'])['id'].agg(['count'])
result3 = result3.reset_index()
result4 = result3.groupby(["brand"])['count'].agg([np.mean])
print(result4.sort_values('mean', ascending=False))
