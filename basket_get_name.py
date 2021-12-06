import pandas as pd
import time

start_time = time.time()
data_cormat = pd.read_csv("d:/corrmat.csv")
len_col = len(data_cormat.columns.tolist())
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
count = 0
for i in range(1, len_col):
    for j in range(i + 1, len_col):
        for k in range(j + 1, len_col):
            for l in range(k + 1, len_col):
                for m in range(l + 1, len_col):
                    s1.append(data_cormat.columns.tolist()[i])
                    s2.append(data_cormat.columns.tolist()[j])
                    s3.append(data_cormat.columns.tolist()[k])
                    s4.append(data_cormat.columns.tolist()[l])
                    s5.append(data_cormat.columns.tolist()[m])
                    count += 1
                    print(count)
    print("--- %s seconds ---" % (time.time() - start_time))
basket_name = {
    'Source1': s1,
    'Source2': s2,
    'Source3': s3,
    'Source4': s4,

}
pd.DataFrame(data=basket_name).to_csv("d:/basket_name.csv", index=False)
