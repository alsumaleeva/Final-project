# Алсу Малеева, 47-я когорта — Финальный проект. Инженер по тестированию плюс
-- Для запуска тестов должны быть установлены пакеты pytest и requests  
-- Запуск всех тестов выполняется командой pytest  
-- В configuration.py хранятся все пути  
-- В sender_stand_request.py хранятся все запросы  
-- В data.py хранятся все данные  
-- В test_accept_order.py хранятся тесты для 1 и 2 задания, в test_get_order_by_track.py для 3 задания  

-- В configuration.py поменять URL на действующий (без / в конце)  
-- Запускать теста из файлов test_accept_order.py и test_get_order_by_track.py 

# Задание 1
-- После запуска файла test_accept_order.py в терминале вбить следующий код чтоб проверить отображается ли созданный заказ в базе данных.  
```sql
    SELECT c.login, COUNT(o.id)
    FROM "Couriers" AS c
    JOIN "Orders" AS o ON c.id = o."courierId"
    WHERE o."inDelivery" = true
    GROUP BY c.login;
```

# Задание 2
-- После запуска файла test_accept_order.py в терминале вбить следующий код чтоб убедиться, что в базе данных статусы заказов записываются корректно.  
```sql
SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";
```

# Задание 3
-- Запустить файл test_get_order_by_track.py  
-- Скриншот в файле test_result.png