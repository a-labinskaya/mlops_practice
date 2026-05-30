## Состав

- `data_creation.py` - загружает датасет, делит его на обучающую и тестовую выборки и сохраняет CSV-файлы в папки `train` и `test`.
- `data_preprocessing.py` - масштабирует признаки через `StandardScaler`, сохраняет обработанные данные и объект scaler.
- `model_preparation.py` - обучает `LogisticRegression` и сохраняет модель в `model.pkl`.
- `model_testing.py` - загружает модель, считает accuracy на тестовой выборке и печатает результат.
- `pipeline.sh` - последовательно запускает все этапы пайплайна.

## Как запустить

```bash
cd lab1
python3 -m pip install pandas scikit-learn
bash pipeline.sh
```

Ожидаемый результат - вывод метрики качества:

```text
Model test accuracy is: ...
```

## Артефакты

После запуска создаются папки `train`, `test`, обработанные CSV-файлы, `scaler.pkl` и `model.pkl`.
