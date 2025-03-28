import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5])
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr * 2)
print(matrix * 2)

salaries = np.array([50,12,5,66,84,118,23,581,84,11,88965,2185,484])

#average salary
mean_salary = np.mean(salaries)
print (f"Average salary: {mean_salary}k$")

#max min
max_salary = np.max(salaries)
min_salary = np.min(salaries)
print (f"max salary: {max_salary}k$")
print (f"min salary: {min_salary}k$")

#standart deviation
std_salary = np.std(salaries)
print(f"std: {std_salary}")

above_mean = salaries[salaries>mean_salary]
print(f"Above mean: {above_mean}")

products_ids = np.array([100, 101, 102, 103, 104, 105])
prices = np.array([20, 11, 1, 51, 202, 68])
quantities = np.array([10, 5, 23, 36, 26, 8])
dates = np.array([
    '2023-07-01','2023-07-03','2023-07-07','2023-07-06','2023-07-05',
'2023-07-9','2023-07-12','2023-07-23','2023-07-13','2023-07-11'
])

total_sales = prices * quantities
print(f"Total Sales: {total_sales}")

total_revenue = np.sum(total_sales)
print(f"Total Revenue: {total_revenue}")

average_check = np.mean(total_sales)
print(f"Average check: {average_check:.2f}")

best_product_index = np.argmax(total_sales)
worst_product_index = np.argmin(total_sales)
print(f"Best product(ID: {products_ids[best_product_index]},Total Sales: {total_sales[best_product_index]}, Price:{prices[best_product_index]})")
print(f"Worst product(ID: {products_ids[worst_product_index]}, Total Sales: {total_sales[worst_product_index]},Price:{prices[worst_product_index]})")

dates_pd = pd.to_datetime(dates)
days_of_week = dates_pd.day_name()
print(f"Sales per week:{days_of_week}")

sales_by_day = dict()
for day, sale in zip(days_of_week,total_sales):
    if day in sales_by_day:
        sales_by_day[day] += sale
    else:
        sales_by_day[day] = sale

print(f"Sales per days: {sales_by_day}")
df_sales_by_day = pd.DataFrame(list(sales_by_day.items()), columns=['day', 'sales'])
df_sales_by_day.to_csv('sales_by_day.csv')

# data = {
#     'Name': ['John', 'Anna', 'Peter', 'Alex'],
#     'Age': [28,52,32,14],
#     'City': ['New York','Paris','Berlin','London']
# }
#
# df = pd.DataFrame(data)
# print(df.describe())

# df = pd.read_csv('info.csv')
#
# # print(df)
#
# print(df['Имя'])
# print(df['Возраст'])
#
# print(df.describe())

# df = pd.read_csv('platforms.csv')
# print("Data from file:")
# print(df.head())
#
# df['Views'] =df['Views'].fillna(df['Views'].mean())
# df['Revenue'] = df['Revenue'].fillna(0)
#
# df.drop_duplicates(inplace=True)
#
# df['Views'] = df['Views'].astype(int)
# df['Date'] = pd.to_datetime(df['Date'])
#
# # print("Describe:")
# # print(df.describe())
#
# filtered = df[df['Platform'] == 'YouTube']
# #print(filtered)
#
# grouped = filtered.groupby('Date').agg({'Views': 'sum', 'Revenue': 'sum'}).reset_index()
# print(grouped)
#
# mean_views = grouped['Views'].mean()
# mean_revenue = grouped['Revenue'].mean()
# print(f"Mean views: {mean_views} and mean revenue: {mean_revenue}")
#
# grouped.to_csv('new_data.csv', index=False)