import numpy as np
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["Math", "Physics", "CS", "Math", "CS"],
    "GPA": [3.9, 3.5, 3.8, 3.7, 3.6],
    "Credits": [30, 28, 32, 30, 26]
}
columns = ["Name", "Age", "Department", "GPA", "Credits"]
data_array = np.array(
    [
        data["Name"],
        data["Age"],
        data["Department"],
        data["GPA"],
        data["Credits"],
    ],
    dtype=object,
).T
#-1
print("1) NumPy массив (таблица):")
print(data_array)
#-2
print("\n2.1) Студенты с GPA > 3.7:")
gpa_filter = data_array[:, 3].astype(float) > 3.7
print(data_array[gpa_filter])
print("\n2.2) Студенты с кафедры Math:")
department_filter = data_array[:, 2] == "Math"
print(data_array[department_filter])
#-3
print("\n3.1) Сортировка по возрасту:")
age_sorted = data_array[np.argsort(data_array[:, 1].astype(int))]
print(age_sorted)
print("\n3.2) Сортировка по GPA в порядке убывания:")
gpa_sorted = data_array[np.argsort(data_array[:, 3].astype(float))[::-1]]
print(gpa_sorted)
#-4
print("\n4.1) Средний GPA по кафедрам:")
departments = np.unique(data_array[:, 2])
for dept in departments:
    dept_gpa = data_array[data_array[:, 2] == dept][:, 3].astype(float)
    print(f"{dept}: {np.mean(dept_gpa):.2f}")
print("\n4.2) Количество студентов по кафедрам:")
for dept in departments:
    dept_count = np.sum(data_array[:, 2] == dept)
    print(f"{dept}: {dept_count}")
#-5
print("\n5) Добавление столбца Internship:")
internship = np.array([True, False, np.nan, True, np.nan], dtype=object)
data_array = np.column_stack((data_array, internship))
print(data_array)
print("\n5.1) Строки с пропущенными значениями в столбце Internship:")
missing_internship = np.array([x is np.nan for x in data_array[:, -1]])
print(data_array[missing_internship])
data_array[missing_internship, -1] = False
print("\n5.2) После замены NaN на False:")
print(data_array)
#-6
print("\n6) Добавление столбца Final Credits:")
final_credits = data_array[:, 4].astype(float) * data_array[:, 3].astype(float)
data_array = np.column_stack((data_array, final_credits))
print(data_array)
#-7
print("\n7.1) Данные о втором студенте:")
print(data_array[1, :])
print("\n7.2) Имена и GPA первых трёх студентов:")
print(data_array[:3, [0, 3]])
data_array[3, 3] = 3.95
print("\n7.3) После изменения GPA у четвёртого студента:")
print(data_array[3])
print("\n7.4) Последние два столбца для всех студентов:")
print(data_array[:, -2:])