# true_data - pandas.DataFrame с истинными значениями меток.
# pred_data - pandas.DataFrame с предсказанными значениями меток.

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import recall_score, precision_score

def f1_sampled(actual, pred):
    mlb = MultiLabelBinarizer()
    all_classes = pd.concat((actual, pred))
    mlb.fit(all_classes)
    actual = mlb.transform(actual)
    pred = mlb.transform(pred)
    f1 = f1_score(actual, pred, average = "samples")
    return f1

def preprocess_tags(data):
    """Преобразует строку, содержащую значения меток, в список меток."""
    for col in ['Объектные', 'Функциональные', 'Процессные', 'Ограничения', 'Структурные']:
        data[col] = [[i] for i in data[col].values]
        data[col] = data[col].apply(lambda x: str(x[0]).split(';'))
    return data

def compute_final_score(true_data, pred_data):
    """Среднее значение F1 samples по всем типам тегов."""
    scores = []
    true_data = preprocess_tags(true_data)
    pred_data = preprocess_tags(pred_data)
    for i in ['Объектные', 'Функциональные', 'Процессные', 'Ограничения', 'Структурные']:
        scores.append(f1_sampled(true_data[i], pred_data[i]))
    return np.mean(scores)
