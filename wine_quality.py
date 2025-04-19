from datetime import datetime

start_time = datetime.now()

# ANSI for colors
CYAN = "\033[96m"
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

#Imports
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
import pandas as pd
import numpy as np


plt.style.use("ggplot")  # Стили графиков

df = pd.read_csv('/your/path/to/winequality-red.csv', sep=';')
print(df.head())

names = [i for i in df.columns]  # Заголовки таблицы

print(f"{GREEN}Количество наблюдений{RESET} = {df.shape}\n{CYAN}Кол-во элементов{RESET} = {df.size}", end='\n\n')

names_rus = ['Фиксированная кислотность', 'Летучая кислотность', 'Лимонная кислота', 'Остаточный сахар', 'Хлориды',
             'Свободный диоксид серы', 'Общее количество диоксида серы', 'Плотность', 'Кислотность', 'Сульфаты',
             'Алкоголь', 'Качество']

for ind, i in enumerate(names):
    print(f"{YELLOW}Результаты для {CYAN}{names_rus[ind]}")
    print(
        f"Максимальное{RESET} = {GREEN}{df[i].max()}\n{CYAN}Минимальное{RESET} = {GREEN}{df[i].min()}\n{CYAN}Среднее{RESET} = {GREEN}{df[i].mean()}{RESET}\n{CYAN}Медиана{RESET} = {GREEN}{df[i].median()}{RESET} Половина {i} меньше этого значения, половина больше{CYAN}\nДисперсия = {GREEN}{df[i].var(ddof=0)}\n{CYAN}Квантили = {GREEN}{df[i].quantile(0.99)}{RESET} У 99% выборки {i} меньше {df[i].quantile(0.99)} {i}, а у 1% больше",
        end='\n\n')

# Круговая диаграмма
plt.figure(figsize=(15, 10))
plt.title("Доля качества красного вина")
y = (df['quality'].value_counts() / df.shape[0])  # df.shape[0] --> Количество строк
plt.pie(y.values, labels=y.index, autopct='%1.1f%%')
plt.show()

# График значений всей выборки
df_wo_tf = df.drop('free sulfur dioxide', axis=1).drop('total sulfur dioxide', axis=1)
df.hist(figsize=(15, 10), bins=50, color='green')
plt.suptitle("График значений всей выборки")

# Логарифмирование используется для сглаживания выборки данных!!!!!
df_log = df[names].apply(lambda x: np.log(x + 1))  # снова прологарифмируем

colors_list = [
    '#78C850', '#F08030', '#6890F0',
    '#A8B820', '#F8D030', '#E0C068'
]

# data Заменить на df_log для более сглаженной выборки
plt.figure(figsize=(15, 10))
sns.violinplot(y='alcohol', x='quality', data=df, inner="quartile", palette=colors_list)
plt.xticks([])

plt.show()

end_time = datetime.now()
execution_time = end_time - start_time

print(f"Время выполнения программы = {execution_time}")
