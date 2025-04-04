import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Загрузка данных
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    data = pd.read_csv(url)
    return data
data = load_data()
# Заголовок приложения
st.title("Дашбоард под датасет пассажиров Титаника🗻🚢")
# 1. Описательная статистика
st.header("Описательная статистика")
st.write("**Размер таблицы:**", data.shape)
st.write("**Типы данных:**")
st.write(data.dtypes)
st.write("**Вид таблицы:**")
st.write(data.head())
# 2. Графики
st.header("Графики")
# Гистограмма возрастов
st.subheader("Распределение цен билетов")
fig1, ax1 = plt.subplots()
sns.histplot(data['Fare'].dropna(), kde=True, ax=ax1)
ax1.set_title("Гистограмма цен билетов")
ax1.set_xlabel("Цена билета")
ax1.set_ylabel("Количество пассажиров")
st.pyplot(fig1)
# Круговая диаграмма по классам
st.subheader("Распределение пассажиров по классам")
class_counts = data['Pclass'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')  # Чтобы круг был кругом
st.pyplot(fig2)
# Гистограмма возрастов
st.subheader("Распределение возрастов пассажиров")
fig2, ax2 = plt.subplots()
sns.histplot(data['Age'].dropna(), kde=True, ax=ax2)
ax2.set_title("Гистограмма возрастов пассажиров")
ax2.set_xlabel("Возраст")
ax2.set_ylabel("Количество пассажиров")
st.pyplot(fig2)
#Boxplot по полу и цене билета
st.subheader("Распределение цены билета по полам ")
fig, ax = plt.subplots()
sns.boxplot(x='Sex', y='Fare', data=data, ax=ax)
ax.set_title("Распределение цены билета по полам")
ax.set_xlabel("Пол")
ax.set_ylabel("Цена билета")
st.pyplot(fig)
# Boxplot по возрасту и классу билета
st.subheader("Распределение возраста по классам билетов")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Pclass', y='Age', data=data, ax=ax3)
st.pyplot(fig3)
# График выживаемости по классу билета (countplot)
st.subheader("3. Анализ выживаемости")
# Выбор класса билета
selected_class = st.radio(
    "Выберите класс для анализа:",
    [1, 2, 3],
    horizontal=True
)
# Фильтрация данных
class_data = data[data['Pclass'] == selected_class]
# Создание графика
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.countplot(
    x='Sex',
    hue='Survived',
    data=class_data,
    ax=ax4,
    palette=['#ff6b6b', '#51cf66']
)
# Настройка графика
ax4.set_title(f"Выживаемость в {selected_class}-м классе")
ax4.set_xlabel("Пол")
ax4.set_ylabel("Количество пассажиров")
ax4.legend(['Погиб', 'Выжил'])
# Добавление аннотаций
for p in ax4.patches:
    ax4.annotate(
        f"{p.get_height()}",
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha='center',
        va='center',
        xytext=(0, 5),
        textcoords='offset points'
    )
# Вывод статистики
survival_rate = class_data['Survived'].mean()
st.metric(
    f"Общая выживаемость в {selected_class}-м классе",
    f"{survival_rate:.1%}"
)
st.pyplot(fig4)
# 4. Вывод N строк таблицы
st.header("3. Просмотр данных")
n_rows = st.slider("Выберите количество строк для отображения", 1, 891, 5)
st.write(data.head(n_rows))
