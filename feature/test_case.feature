#languare: ru
# content of test_case.feature

Функционал: Сортировка смартфонов в Яндекс.Маркете
    Для того, чтобы протестировать Яндекс.Маркет
    В качестве параметра открытие в полноэкранном режиме
    Я хочу открыть браузер

    Сценарий: Зайти на "yandex.ru"
        Дано Открыт браузер
        Когда Зайду на сайт "https//yandex.ru/"
        То Увижу, что сайт "Яндекс" открыт в браузере

    Сценарий: "Cмартфоны" в разделе "Маркет"
        Дано Открыт сайт "https//yandex.ru/"
        Когда Я в разделе «Маркет» выбрал «Смартфоны»
        И Когда перешел в «Все фильтры»
        То Увидел страницу «Все фильтры»

    Сценарий: "Cмартфоны" в разделе "Маркет"
        Дано Открыта страница «Все фильтры».
        Когда Задал параметр поиска до 20000 рублей и Диагональ экрана от 3 дюймов
        И Выбрал не менее 5 любых производителей
        И Нажал кнопку "Показать"
        То Увидел страницу со списком отсортированных смартфонов

    Сценарий: Вывод рейтинга определенного товара
        Дано Страница со списком отсортированных смартфонов
        Когда Я посчитал кол-во смартфонов на одной странице
        И Запомнил последний из списка
        И Изменил Сортировку на другую (по цене/ по рейтингу/ по скидке)
        И Найти и нажать по имени запомненного объекта
        И Вывести рейтинг выбранного товара
        То Увидел рейтинг выбранного товара

    Сценарий: Закрыть браузер
        Дано Открыт браузер
        Когда Я закрою браузер
        То Увижу, что он закрылся