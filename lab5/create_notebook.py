import nbformat as nbf

nb = nbf.v4.new_notebook()

nb.cells = [
    nbf.v4.new_markdown_cell("# Lab 5: Testing ML model quality with pytest"),
    nbf.v4.new_markdown_cell("Цель работы: создать модель линейной регрессии и проверить её качество с помощью pytest на чистых и зашумленных данных."),
    nbf.v4.new_code_cell("""import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib"""),
    nbf.v4.new_code_cell("""def make_clean_data(seed, n=100):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = 3 * x + 5 + rng.normal(0, 0.5, n)
    return x.reshape(-1, 1), y

def make_noisy_data(seed, n=100):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = rng.normal(0, 20, n)
    return x.reshape(-1, 1), y"""),
    nbf.v4.new_code_cell("""x_train, y_train = make_clean_data(1)

model = LinearRegression()
model.fit(x_train, y_train)

joblib.dump(model, "model.pkl")

print("Model trained successfully")"""),
    nbf.v4.new_code_cell("""x_clean, y_clean = make_clean_data(2)
y_pred_clean = model.predict(x_clean)

print("R2 clean:", r2_score(y_clean, y_pred_clean))

plt.scatter(x_clean, y_clean)
plt.plot(x_clean, y_pred_clean)
plt.title("Clean data")
plt.savefig("clean_data.png")
plt.show()"""),
    nbf.v4.new_code_cell("""x_noisy, y_noisy = make_noisy_data(5)
y_pred_noisy = model.predict(x_noisy)

print("R2 noisy:", r2_score(y_noisy, y_pred_noisy))

plt.scatter(x_noisy, y_noisy)
plt.plot(x_noisy, y_pred_noisy)
plt.title("Noised data")
plt.savefig("noised_data.png")
plt.show()"""),
    nbf.v4.new_code_cell("""!pytest -v test_model.py"""),
    nbf.v4.new_markdown_cell("Вывод: модель показывает высокое качество на чистых данных, а тесты позволяют обнаружить проблему качества на зашумленном датасете.")
]

with open("lab5/lab5.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)
