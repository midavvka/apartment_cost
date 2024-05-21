import streamlit as st
import pickle
import pandas as pd

st.write("# Узнай актуальную цену квартиры в НН")
st.write("##### Отказ от ответственности: Пользователь использует приложение на свой страх и риск.")

area = st.slider(
    '### Площадь квартиры (кв.м.):',
    min_value=15.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

district = st.selectbox(
    "Район",
    ['Автозаводский район', 'Советский район', 'Канавинский район',
       'Московский район', 'Приокский район', 'Другой',
       'Нижегородский район', 'Сормовский район', 'Ленинский район']
)

building_type = st.selectbox(
    "Материал постройки",
    ['кирпич', 'панель', 'шлакоблок', 'блок+утеплитель', 'дерево',
       'монолитный железобетон']
)


year = st.slider(
    '### Год постройки:',
    min_value=1825.0,
    max_value=2027.0,
    value=2000.0,
    step=5.0
)

rooms = ['Студия', 'Однокомнатная', 'Двухкомнатная', 'Трехкомнатная', 'Четырехкомнатная']
rooms_count = st.selectbox(
    "Комнаты",
    rooms,
    index=2
)

room2count = dict(zip(rooms,[0.8,1,2,3,4]))

no_first_no_last = st.checkbox("Не первый не последний этаж", value=True)

appart =dict(zip(
    ['area1', 'district', 'building_type', 'year', 'rooms_count', 'no_first_no_last'],
    [area, district, building_type, year, room2count[rooms_count], no_first_no_last]
))

new = pd.DataFrame(appart, index=[0])
st.write(new)


model_pkl_file = "models/apartment_prices_regression.pkl"
with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)


st.write("## Оценочная стоимость квартиры:","{:,}".format(int(model.predict(new)[0])))