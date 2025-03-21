## Описание
Библиотека для рассчета различных показателей, характеризующих рельеф. 

Данные о высоте (DEM) загружаются из GEE (по API) для заданной области, показатели рассчитываются с помощью xdem.

Данные хранятся в float16

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
|   ├── plotting.py
└── examples/
    ├── example_usage.py
```
## Использование

**Установка**
1. Клонируйте репозиторий
```bash
git clone https://github.com/kostkornilov/dem_api
cd dem_api
```
2. Установите зависимости
```bash
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

Пример использования представлен в файле ```example_usage.ipynb```

## Рассчитываемые показатели
### Пример:
- Область с координатами центра lat, lon = 55.600, 37.172 и буфером в 0.1 градус
- Высота:
  
![Высота](examples/pictures/DEM.png)

- Экспозиция:

![Экспозиция](examples/pictures/Aspect.png)

Ниже приведен список показателей, которые можно рассчитать с помощью данной библиотеки:

- slope
- hillshade
- aspect
- curvature
- planform_curvature
- profile_curvature
- maximum_curvature
- topographic_position_index
- terrain_ruggedness_index
- roughness
- rugosity