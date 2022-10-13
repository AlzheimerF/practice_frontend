# practice_frontend
Project name endpoints:

##  Получение списка новостей по методу GET -->  http://alzheimer4.pythonanywhere.com/news_list/
##  Получение новостей (detail) по методу GET --> http://alzheimer4.pythonanywhere.com/news_detail/1/
#### По айдишнику ищется конкретная новость для полного отображения новости /news_detail/1/ .
## Создание новостей (create) по методу POST --> http://alzheimer4.pythonanywhere.com/news_create/
##### Пример json строки для создания новостей
#### 
       {
        "id": 2,
        "title": "sfjlskdjfn",
        "description": "kjfsdfkdslf",
        "date": "2022-10-13T13:42:41.774165Z",
        "published": true 
       }
#### 
## Удаление новостей (delete) по методу DELETE --> http://alzheimer4.pythonanywhere.com/news_delete/1/
#### По айдишнику ищется конкретная новость для удаления /news_delete/1/ .
