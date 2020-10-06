import pandas as pd

file_xlsx = '/home/khoa/Documents/WORK_notation-helper/1.work_.wh Python_helper/pandas/template.xlsx'
file_data = pd.read_excel(file_xlsx, sheet_name='template')
# print(file_data)
# print('-'*20)
# col_header = file_data.iloc[8:,0]
df = pd.DataFrame(file_data)
# row_header = df.iloc[:5]

print(df.iloc[8])

print('/'*30, df)
# print(len(col_header))
# sku_sid, sku_name = df.iloc[7,2:], df.iloc[8,2:]
# plno_sid, plno_name = df.iloc[9:,0], df.iloc[9:,1]
# print(type(sku_name))
# print(list(sku_name))

# print('+'*30)
# print(sku_sid, '\n','*'*10, '\n', sku_name)
# print('+'*30)
# print(plno_sid, '\n','*'*10, '\n',  plno_name)


# print('\n', '-'*40, df)

# for i in df.iterrows():
#     print(i, type(i), len(i), '\n')

# for i in range(len(df)):
#     # row  = pd.DataFrame(df.iloc[i,:]).sum(numeric_only=True)
#     row  = pd.DataFrame(df.iloc[i,:])
#     print(row.sum(axis=1, numeric_only=True))
#     print(row)

#     # x = tuple(x)
#     # print(x, type(x), len(x), '\n')
# pd.to_numeric(df, errors = 'ignore')

# print(df)print(type(s_gt_0))
# errors = []
# for k,v in row_sum.items():
#     if v < 1:
#         errors.append(k+1)
#     print(k,v, type(v))
# print(errors)
# df2 = df.apply(pd.to_numeric, errors='ignore')

""" convert all to number """
# df2 = df.apply(pd.to_numeric, errors='coerprint(type(s_gt_0))
# errors = []
# for k,v in row_sum.items():pandas
#     if v < 1:
#         errors.append(k+1)
#     print(k,v, type(v))
# print(errors)

# print(df)
# print(df.loc['PLG-code-1', 'SKU-name-2'])
# print(df.loc['PLG-code-2', 'SKU-name-2'])
# print(df.loc['PLG-code-1'])
# print(df.loc['PLG-code-2'])
# print(df.loc['plan-code-3'])


# print(df, type(df))

# print (where(row_sum > 0))
# s = pd.Series(row_sum)
# s_gt_0 = s.where(s >= 1)
# print(s_gt_0)
# print(df)

# print(type(s_gt_0))
# errors = []


# updated_data = df.iloc[9:, 2:]
# updated_data.columns = sku_name
# updated_data.index = plno_name





# for index, row in updated_data.iterrows():
#     print(index, '--->')
#     for k, v in row.items():
#         print(k, type(k), '++', v, type(v))
#         if str(v).isnumeric():
#             print(f'--{v}--')


# for planogram_sid, planogram_row in updated_data.iterrows():
#     print(planogram_sid, '--->')
#     for sku_sid, sku_row in planogram_row.items():
#         print(sku_sid, type(sku_sid), '++', sku_row, type(sku_row))
#         if str(sku_row).isnumeric():
#             # pln_sku_obj.project_sid = project_sid
#             # pln_sku_obj.planogram_sid = planogram_sid
#             # pln_sku_obj.sku_sid = sku_sid
#             pass


"""
MUST CONNECT DATA BASE FOR THIS FILE TO TAKE A QUICK TEST
"""