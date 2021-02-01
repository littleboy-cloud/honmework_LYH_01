import numpy as np, pandas as pd

# 原表格
# df = pd.DataFrame({'姓名':['张飞', '关羽', '刘备', '典韦', '许褚'], '语文':[68,95,98,90,80],'数学':[68,76,86,88,90],'英语':[30,98,88,77,90]})
print('*' * 30 + '原始数据' + '*' * 30)
data = {'语文': [68, 95, 98, 90, 80], '数学': [68, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print(df)

# 求平均值，最小成绩，最大成绩，方差，标准差
print('*' * 17 + '求平均值，最小成绩，最大成绩，方差，标准差' + '*' * 17)
df1 = df.describe()
print(df1)

# 在原表格增加总分column并排名
print('*' * 30 + '按照总分排名' + '*' * 30)
df['总分'] = df.apply(lambda x: x.sum(), axis=1)
df.sort_values(by='总分', ascending=False, inplace=True)  # 按照总分排名替换原表格输出
print(df)
