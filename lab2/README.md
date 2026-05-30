## Состав

- `data_creation.py` - создает train/test выборки на основе `load_digits`.
- `data_preprocessing.py` - применяет `StandardScaler` и сохраняет обработанные данные.
- `model_preparation.py` - обучает `LogisticRegression` и сохраняет модель.
- `model_testing.py` - проверяет модель на тестовой выборке.
- `requirements.txt` - зависимости для запуска пайплайна.
- `Jenkinsfile-linux` - Jenkins Pipeline для Linux-агента.
- `Jenkinsfile-windows` - Jenkins Pipeline для Windows-агента.

## Этапы Jenkins Pipeline

1. Подготовка виртуального окружения.
2. Установка зависимостей из `requirements.txt`.
3. Создание данных.
4. Предобработка данных.
5. Обучение модели.
6. Тестирование модели.

## Локальный запуск

```bash
cd lab2
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python data_creation.py
.venv/bin/python data_preprocessing.py
.venv/bin/python model_preparation.py
.venv/bin/python model_testing.py
```

Для Windows используйте `.venv\Scripts\python.exe` вместо `.venv/bin/python`.

## Результат

На последнем этапе выводится accuracy модели:

```text
Model test accuracy is: ...
```
