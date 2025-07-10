
import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Лотто Прогноз", layout="centered")

st.title("🎯 Умный прогноз лотерей")

tabs = st.tabs(["6 из 45", "5 из 36", "4 из 20"])

def load_data(file):
    return pd.read_csv(file, header=None)

def show_stats(df, max_number):
    flat_numbers = df.values.flatten()
    flat_numbers = [n for n in flat_numbers if 1 <= n <= max_number]
    freq = pd.Series(flat_numbers).value_counts().sort_index()
    st.subheader("📊 Частота выпадения чисел")
    st.bar_chart(freq)

    st.subheader("🔢 Частотная таблица")
    st.dataframe(freq.rename("Количество"), use_container_width=True)

def generate_prediction(df, max_number, count):
    flat_numbers = df.values.flatten()
    freq = pd.Series(flat_numbers).value_counts()
    top_numbers = freq.nlargest(25).index.tolist()
    prediction = sorted(random.sample(top_numbers, count))
    return prediction

with tabs[0]:
    st.header("Лотерея 6 из 45")
    df = load_data("lotto_data/6-45.csv")
    if st.button("🎲 Прогноз (6 из 45)"):
        st.success(f"Прогноз: {generate_prediction(df, 45, 6)}")
    show_stats(df, 45)

with tabs[1]:
    st.header("Лотерея 5 из 36")
    df = load_data("lotto_data/5-36.csv")
    if st.button("🎲 Прогноз (5 из 36)"):
        st.success(f"Прогноз: {generate_prediction(df, 36, 5)}")
    show_stats(df, 36)

with tabs[2]:
    st.header("Лотерея 4 из 20")
    df = load_data("lotto_data/4-20.csv")
    if st.button("🎲 Прогноз (4 из 20)"):
        st.success(f"Прогноз: {generate_prediction(df, 20, 4)}")
    show_stats(df, 20)
