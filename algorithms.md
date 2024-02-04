# Описание алгоритмов

## Алгоритм "в лоб" (SimpleQueryGeocoder)
- Для каждого id алгоритм делает запрос на /areas/{{area_id}}
  - Алгоритм получает лист дерева, получает parent_id и делает запрос на /areas/{{area_id}} с parent_id
  - Алгоритм повторяет предыдущий шаг до тех пор, пока не дойдет до корня
  - Алгоритм возвращает полный адрес

### Примечание
У API hh.ru есть ограничение на кол-во запросов, поэтому не рекомендуется декодировать при помощи данного алгоритма более 10000 id в день

## Перебор дерева (SimpleTreeGeocoder)
- При инициализации алгоритм получает данные из /areas
- Для каждого id алгоритм осуществляет перебор дерева:
  - При нахождении необходимого узла, алгоритм возвращает этот узел "вверх" по дереву
  - При движении "вверх" по дереву собирается массив узлов необходимой ветки
  - По найденому массиву узлов алгоритм формирует полный адрес

## Инверсия дерева (InvertedTreeGeocoder)
- При инициализации алгоритм получает данные из /areas
- Алгоритм осуществляет перебор дерева регионов
  - Создается дерево регионов, позволяющее по id найти родительский узел
  - На основе созданного дерева создается словарь, позволяющий по id получить полный путь
- Для каждого id алгоритм возвращает данные из созданного словаря адресов