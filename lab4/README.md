# Lab 4: DVC dataset versioning

В работе используется DVC для версионирования датасета Titanic.

Созданы три версии данных:

1. selected — признаки Pclass, Sex, Age.
2. age_filled — пропущенные значения Age заполнены средним значением.
3. sex_encoded — признак Sex преобразован с помощью one-hot encoding.

Переключение между версиями выполняется через git checkout и dvc checkout.
