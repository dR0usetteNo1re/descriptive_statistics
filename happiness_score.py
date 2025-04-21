from datetime import datetime

start_time = datetime.now()

# ANSI for colors
CYAN = "\033[96m"
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

# Визуализация
import matplotlib.pyplot as plt
import seaborn as sns

# Расчеты
from scipy import stats
import pandas as pd
import numpy as np

plt.style.use("ggplot")  # Стили графиков

df = pd.read_csv('/your/path/to/2015.csv')

# Удаляю ненужные (неинтересные) столбцы при помощи метода dataframe.drop()
df = df.drop('Standard Error', axis=1).drop('Dystopia Residual', axis=1)

print(df.head)  # Отображение первой и последней пятерки значений таблицы

names = [i for i in df.columns]  # Заголовки таблицы

# Переименовываю названия столбцов, чтобы было понятнее
names_rus = ['Страна', 'Регион', 'Ранг_счастья', 'Оценка_счастья', 'Экономика', 'Семья', 'Здоровье', 'Свобода',
             'Доверие', 'Щедрость']

for i in range(len(df.columns)):
    df = df.rename(columns={df.columns[i]: names_rus[i]})

# Описательные статистики (Начинаю перебор со второго элемента, так как первые два - словесные атрибуты)
for i in range(2, len(names_rus)):
    print(names_rus[i], end='\n')
    # Среднее или математическое ожидание
    print(f"Среднее = {df[names_rus[i]].mean()}")

    print(f"Максимальное значение = {df[names_rus[i]].max()}")
    print(f"Минимальное значение = {df[names_rus[i]].min()}")

    # Медиана показывает, что ровно половина выборки меньше медианы, а половина больше
    print(f"Медиана = {df[names_rus[i]].median()}")

    # Дисперсия - разброс случайной величины вокруг её математического ожидания
    # (ddof=0) - Стандартная дисперсия, (ddof=1) - Несмещенный вариант
    print(f"Дисперсия = {df[names_rus[i]].var(ddof=0)}")

    # Квантили поставил на 0.75, это значит, что 75% выборки меньше значения квантилей
    print(f"Квантили = {df[names_rus[i]].quantile(0.75)}")

    # Среднеквадратичное отклонение
    # (ddof=0) - Стандартное отклонение, (ddof=1) - Несмещенный вариант
    print(f"Среднеквадратичное отклонение = {df[names_rus[i]].std(ddof=0)}\n")

# Группировка
print(f"Средняя Оценка Счастья для Western Europe = {df[df['Регион'] == 'Western Europe'].Оценка_счастья.mean()}")

# Графики
## График 1: Распределение оценки счастья
plt.figure(figsize=(14, 7))

plt.title("Распределение Оценки счастья")
df['Оценка_счастья'].hist(bins=50, density=True, color='blue')
df['Оценка_счастья'].plot(kind='kde', linewidth=4, color='green')

## График 2: Распределение всей выборки
# Логарифмирую для сглаживания графика
columns = names_rus[2:]
df[columns].hist(figsize=(14, 7), log=True, color='green')
plt.suptitle("Распределение всей выборки")

## График 3: Оценка счастья по региону
# Использование BoxPlot (Seaborn)
df_log = df[columns].apply(lambda x: np.log(x + 1))
df_log['Регион'] = df['Регион']

plt.figure(figsize=(14, 7))

sns.boxplot(x='Регион', y='Оценка_счастья', data=df_log)
plt.xlabel("Регион")
plt.ylabel("Логарифм Оценки счастья")
plt.xticks([])
plt.suptitle("Оценка счастья по региону")

plt.show()

end_time = datetime.now()
execution_time = end_time - start_time

print(f"Время выполнения программы = {execution_time}")
