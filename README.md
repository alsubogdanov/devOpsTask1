# devOpsTasks

## Первая задача: работа с API Accuweather через Postman и Python (1.1)
1. Регистрируемся на https://developer.accuweather.com/user/register и получаем свой api-key
2. Используя postman узнаём locationkey своего города https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/geoposition/search (это можно сделать и без postman, прямо на сайте, но попробуйте postman)
3. пишем код на python, который получает 12 часовой прогноз для вашего города и выводит его в консоль построчно для каждого часа в формате "hh:mm, temperature, icon phrase"

## Вторая задача: сделать свой API используя python и Flask (1.2)
1. Реализовать три функции доступные через API c помощью разных HTTP методов (например: get, post и delete)
2. Протестировать работу реализованных функций с помощью Postman
3. Функции могут работать с файлами или выполнять какие-то простейшие математические функции
Accuweather
AccuWeather APIs | Geoposition Search

[Returns information about a specific location, by GeoPosition (Latitude and Longitude)](https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/geoposition/search)


