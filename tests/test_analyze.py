import sys
import os
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from analyze import clean_data


def test_clean_data_removes_cabin():
    df = pd.DataFrame({
        "Age": [22, None, 30],
        "Cabin": ["C1", None, "C3"],
        "Embarked": ["S", "S", None],
    })
    result = clean_data(df)
    assert "Cabin" not in result.columns


def test_clean_data_fills_age():
    df = pd.DataFrame({
        "Age": [20, None, 30],
        "Cabin": ["C1", "C2", "C3"],
        "Embarked": ["S", "S", "S"],
    })
    result = clean_data(df)
    assert result["Age"].isnull().sum() == 0


def test_clean_data_drops_missing_embarked():
    df = pd.DataFrame({
        "Age": [20, 25, 30],
        "Cabin": ["C1", "C2", "C3"],
        "Embarked": ["S", None, "C"],
    })
    result = clean_data(df)
    assert len(result) == 2