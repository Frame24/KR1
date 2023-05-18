import streamlit as st
import pandas as pd


def main():
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        accept_multiple_files=False)
    if uploaded_file:
        st.header("Задание 1:")
        isSurvived = st.radio(
            label="Выжили ли:",
            options=["Выжили", "Погибли"])
        age = st.radio(label="Возраст:", options=["<30", ">60"])

        st.write("Результат:")
        df = load_dataframe(uploaded_file)
        young_survived, old_survived = task1(df, "Age", 30, 60, "Survived")

        if isSurvived == "Выжили":
            if age == "<30":
                result_mean = 100 * young_survived.mean()
            if age == ">60":
                result_mean = 100 * old_survived.mean()
        else:
            if age == "<30":
                result_mean = 100 * (1 - young_survived.mean())
            if age == ">60":
                result_mean = 100 * (1 - old_survived.mean())

        st.write(str(round(result_mean, 2)) + "%")

        st.header("Задание 2:")

        Sex = st.radio(label="Пол:", options=["Мужской", "Женский"])
        st.write("Результат:")

        if Sex == "Мужской":
            result_sex_mean = 100 * task2(df, "male", True)
        elif Sex == "Женский":
            result_sex_mean = 100 * task2(df, "female", True)

        st.write(str(round(result_sex_mean, 2)) + "%")


def load_dataframe(data):
    return pd.read_csv(data)


def task1(df, column1, number1, number2, column2):
    young_survived = df[df[column1] < number1][column2]
    old_survived = df[df[column1] > number2][column2]
    return (young_survived, old_survived)


def task2(df, Sex, isSurvived: bool = True):
    res = df[df["Sex"] == Sex]["Survived"]
    if isSurvived:
        return res.mean()
    else:
        return 1 - res.mean()


def foo(a, b):
    return a + b


if __name__ == "__main__":
    main()
