# Описание API final_yatube

API для проекта Yatube, социальной сети для обмена постами и комментариями.

## Основные эндпоинты

### Посты

- `GET /api/posts/`
  - Получить список всех постов.
  
- `GET /api/posts/{id}/`
  - Получить пост по его ID.

- `POST /api/posts/`
  - Создать новый пост.
  - **Тело запроса:**
    ```json
    {
      "title": "string",
      "content": "string"
    }
    
- `PUT /api/posts/{id}/`
  - Обновить существующий пост.
  - **Тело запроса:**
   ```json
    {
      "title": "string",
      "content": "string"
    }