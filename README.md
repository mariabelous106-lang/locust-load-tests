# Locust Load Tests

Нагрузочное тестирование публичного JSONPlaceholder API с помощью Locust.

## Стек
- Python 3.14
- Locust

## Установка и запуск

```bash
git clone https://github.com/mariabelous106-lang/locust-load-tests.git
cd locust-load-tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
locust
```

Открой http://localhost:8089 в браузере и запусти тест.

## Сценарии

- `GET /posts` — получение списка постов (вес 3)
- `GET /posts/1` — получение одного поста (вес 2)
- `GET /posts/99999` — негативный сценарий, 404 (вес 1)

## Результаты

Тест: 10 пользователей, ramp-up 2 пользователя/сек.

| Метрика | Значение |
|---------|----------|
| RPS | 4.7 |
| Среднее время ответа | 18 мс |
| Median | 14 мс |
| 95%ile | 24 мс |
| Реальные ошибки (без ожидаемого 404) | 0 |

**Вывод:** API стабильно выдерживает нагрузку в 10 пользователей, время ответа — менее 20 мс, реальных ошибок нет.