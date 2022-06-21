from sklearn.decomposition import PCA  # 导入 sklearn.decomposition.PCA 类
import numpy as np  # Youcans， XUPT
from sklearn.preprocessing import StandardScaler

# 扣除非经常性损益后的基本每股收益、扣除非经常性损益后的加权平均净资产收益率
#            资产负债率、扣非每股收益、扣非净资产收益率、预收款/营业收入、               应收账款/营业收入、               现金流量净额/营业收入,          毛利率、 净利率
x = np.array([[0.6978,  0.36,       0.07,             255682611.39/49589246312.08, 7798088572.87/49589246312.08, 435955993.59/49589246312.08, 0.075, 7.04/495.89],  # 2015
             [0.6899,  0.51,       0.0781,           293084014.43/61556839885.98, 9076016800/61556839885.98, 431263752.86/61556839885.98, 0.076, 9.04/615.57],  # 2016
             [0.6246,  0.61,       0.0751,           432320900.31/73942894403.06, 14106308680.89/73942894403.06, -1012045577.12/73942894403.06, 0.0831, 14.73/739.43],  # 2017
             [0.6943,  0.67,       0.0659,           789516875.10/87136358553.83, 20715491962.84/87136358553.83, 1222023164.60/87136358553.83, 0.0857, 13.81/871.36],  # 2018
             [0.6912,  0.83,       0.0823,           714645519.04/99497077396.63, 22913201149.70/99497077396.63, 2767873048/99497077396.63, 0.0865, 17.81/994.97],  # 2019
             [0.6831,  0.94,       0.0931,           732532455.49/110859514087.96, 25077003037.99/110859514087.96, 3443884108.92/110859514087.96, 0.0893, 33.85/1108.60],  # 2020
             [0.685,   0.69,       0.0624,           835544453.25/122407434023.04, 26406280353.18/122407434023.04, 3459045057.02/122407434023.04, 0.0801, 24.48/1224.07]], )  # 2021


x_scaler = StandardScaler().fit_transform(x)

modelPCA = PCA(n_components=0.95)
modelPCA.fit(x_scaler)  # 用数据集 X 训练 模型 modelPCA
print(modelPCA.n_components_)  # 返回 PCA 模型保留的主成份个数

print(modelPCA.explained_variance_ratio_)  # 返回 PCA 模型各主成份占比

print(modelPCA.singular_values_) # 返回 PCA 模型各主成份的奇异值

x_trans = modelPCA.fit_transform(x_scaler)
print(x_trans)
print('得分')
print(x_trans * modelPCA.explained_variance_ratio_)
print(np.sum(x_trans * modelPCA.explained_variance_ratio_, axis=1))