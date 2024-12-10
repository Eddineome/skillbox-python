## Задача 7. Учёт финансов
### Что нужно сделать
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день, а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

- **/add/<date>/\<int:number\>** — сохранение информации о совершённой в рублях трате за какой-то день;
- **/calculate/\<int:year\>** — получение суммарных трат за указанный год;
- **/calculate/\<int:year>\<int:month>** — получение суммарных трат за указанные год и месяц.

Дата для `/sadd/` передаётся в формате _YYYYMMDD_, где _YYYY_ — год, _MM_ — месяц (от 1 до 12), _DD_ — число (от 01 до 31). Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
### Советы и рекомендации
- У словаря есть метод `setdefault`, который возвращает значение по ключу, а если такого ключа нет, инициализирует элемент заданным значением.

Вариант с большим количеством вложенных условий:

```python
if year in storage:
    if month in storage[year]:
        storage[year][month] += expense
    else:
        ...
else:
    ...
```

Вариант с использованием `setdefault`:

```python
storage.setdefault(year, {}).setdefault(month, {})
storage[year][month] += expense
```

- Рассмотрите несколько вариантов хранения информации. Какой из них будет работать наиболее эффективно? Нужно ли каждый раз пересчитывать траты за год или месяц?
### Что оценивается
- Расчёт затрат оптимизирован по времени и памяти.
- Отсутствует большое количество вложенных условий.