## Состав

- `image_classification.py` - Streamlit-приложение для загрузки изображения и вывода top-3 предсказаний.
- `requirements.txt` - зависимости приложения.
- `dockerfile` - образ на базе `python:3.10` с запуском Streamlit на порту `8501`.
- `compose.yaml` - запуск сервиса через Docker Compose.
- `Jenkinsfile` - CI/CD пайплайн для сборки Docker-образа, тегирования по ветке и commit SHA и публикации в Docker Hub.

## Docker Hub

Готовый образ публикуется в Docker Hub:

<https://hub.docker.com/r/alabinskaya/mlops-lab3>

Имя образа:

```text
alabinskaya/mlops-lab3
```


## Запуск через Docker Compose

```bash
cd lab3
docker compose up --build
```

После запуска откройте `http://localhost:8501`, загрузите изображение и нажмите кнопку распознавания.

## Jenkins Pipeline

Pipeline выполняет checkout репозитория, формирует Docker-тег из имени ветки и короткого SHA коммита, собирает образ `alabinskaya/mlops-lab3` и публикует его в указанный Docker Hub репозиторий.
