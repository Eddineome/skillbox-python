## Задача 3. JSON-логирование
### Что нужно сделать
Удобно сохранять логи в определённом формате, чтобы затем их можно было фильтровать и анализировать. Сконфигурируйте логгер так, чтобы он писал логи в файл `skillbox_json_messages.log` в следующем формате:
```python
{"time": "<время>", "level": "<уровень лога>", "message": "<сообщение>"}
```
Но есть проблема: если в message передать двойную кавычку, то лог перестанет быть валидной JSON-строкой:
```python
{"time": "21:54:15", "level": "INFO", "message": """}
```s
Чтобы этого избежать, потребуется `LoggerAdapter`. Это класс из модуля `logging`, который позволяет модифицировать логи перед тем, как они выводятся.

У него есть единственный метод — `process`, который изменяет сообщение или именованные аргументы, переданные на вход.

```python
class JsonAdapter(logging.LoggerAdapter):
  def process(self, msg, kwargs):
    # меняем msg
    return msg, kwargs
```
Использовать можно так:
```python
logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Сообщение')
```
Вам нужно дописать метод `process` так, чтобы в логах была всегда JSON-валидная строка.
### Советы и рекомендации
* [LoggerAdapter Objects](https://docs.python.org/3/library/logging.html#loggeradapter-objects).
* Для создания JSON-валидной строки воспользуйтесь методом [json.dumps](https://docs.python.org/3/library/json.html#json.dumps).
### Что оценивается
* Лог выводится в формате JSON.
* Лог является валидной JSON-строкой.