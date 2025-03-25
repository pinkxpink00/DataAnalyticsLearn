import numpy as np

# arr = np.array([1,2,3,4,5])
# matrix = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
#
# print(arr * 2)
# print(matrix * 2)

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