## Описание
Библиотека для рассчета различных показателей, характеризующих рельеф

## Структура репозитория 

```
dem_analysis_api/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── data_download.py
│   ├── calculations.py
│   ├── utils.py
└── examples/
    ├── example_usage.py
```
## Использование

**Установка**
1. Клонируйте репозиторий
```bash
git clone https://github.com/ваш_аккаунт/dem_analysis_api.git
cd dem_analysis_api
```
2. Установите зависимости
```bash
Copy code
pip install -e .
```

**Авторизация в Google Earth Engine** 
Перед использованием необходимо авторизоваться в Google Earth Engine:

Выполните команду:
```bash
earthengine authenticate
```
Войдите в свой Google-аккаунт и скопируйте предоставленный токен.

Вставьте токен в терминал.

## Пример использования

Пример использования представлен в файле ```example_usage.py```

