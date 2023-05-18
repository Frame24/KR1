import Client
import pandas as pd


def test_foo():
    assert Client.foo(1, 2) == 3


def test_task1():
    df = pd.read_csv("./titanic_train.csv")
    young_survived, old_survived = Client.task1(df, "Age", 30, 60, "Survived")
    check1 = round(100 * young_survived.mean(), 2) == 40.62
    check2 = round(100 * old_survived.mean(), 2) == 22.73

    assert check1 and check2


def test_task2():
    df = pd.read_csv("./titanic_train.csv")
    check1 = round(100 * Client.task2(df, "male", False), 2) == 81.11
    check2 = round(100 * Client.task2(df, "female", True), 2) == 74.2
    assert check1 and check2
