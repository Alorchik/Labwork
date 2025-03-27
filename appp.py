import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
@st.cache_data  # Кэширование, чтобы не загружать данные каждый раз
def load_data():
    url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Заголовок приложения
st.title("Дашборд: Анализ выживаемости пассажиров Титаника 🚢")

# 1. Описательная статистика
st.header("1. Описательная статистика")
st.write("**Размер таблицы:**", data.shape)
st.write("**Типы данных:**")
st.write(data.dtypes)
st.write("**Первые 5 строк:**")
st.write(data.head())

# 2. Графики
st.header("2. Визуализация данных")

# Гистограмма возрастов
st.subheader("Распределение возрастов пассажиров")
fig1, ax1 = plt.subplots()
sns.histplot(data['Age'].dropna(), kde=True, ax=ax1)
st.pyplot(fig1)

# Круговая диаграмма по полу
st.subheader("Соотношение мужчин и женщин")
gender_counts = data['Sex'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
st.pyplot(fig2)

# Boxplot по возрасту и классу билета
st.subheader("Распределение возраста по классам билетов")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Pclass', y='Age', data=data, ax=ax3)
st.pyplot(fig3)

# График выживаемости по полу (столбчатая диаграмма)
st.subheader("Выживаемость по полу")
fig4, ax4 = plt.subplots()
sns.countplot(x='Sex', hue='Survived', data=data, ax=ax4)
st.pyplot(fig4)

# 3. Интерактивный график (реагирует на ввод)
st.subheader("Интерактивный график: Выживаемость по классу билета")
selected_class = st.selectbox("Выберите класс билета", [1, 2, 3])
filtered_data = data[data['Pclass'] == selected_class]
survival_rate = filtered_data['Survived'].mean()
st.write(f"Процент выживших в {selected_class} классе: {survival_rate:.2%}")

# 4. Вывод N строк таблицы
st.header("3. Просмотр данных")
n_rows = st.slider("Выберите количество строк для отображения", 1, 50, 5)
st.write(data.head(n_rows))
