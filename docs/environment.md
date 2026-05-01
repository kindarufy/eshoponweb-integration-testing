# Тестовое окружение

## Объект тестирования

Оригинальный проект:

```text
https://github.com/dotnet-architecture/eShopOnWeb
```

В рамках этого репозитория исходный код eShopOnWeb не хранится. Для проверки нужно отдельно клонировать оригинальный проект.

## Рекомендуемое окружение

- OS: Windows 10/11, macOS или Linux;
- Git;
- Docker Desktop — для запуска через Docker Compose;
- .NET SDK 8 — для локального запуска без Docker;
- Postman — для smoke-проверок;
- браузер: Chrome, Edge или Firefox.

## Запуск через Docker Compose

Из корня оригинального проекта eShopOnWeb:

```bash
docker compose build
docker compose up
```

Ожидаемые адреса:

```text
Web UI:     http://localhost:5106
Public API: http://localhost:5200
```

## Локальный запуск без Docker

Оригинальный README eShopOnWeb указывает, что большая часть функциональности работает при запуске Web-проекта, но административная часть зависит от `PublicApi`.

В первом терминале:

```bash
cd eShopOnWeb/src/PublicApi
dotnet run
```

Во втором терминале:

```bash
cd eShopOnWeb/src/Web
dotnet run --launch-profile Web
```

Ожидаемый адрес Web-приложения:

```text
https://localhost:5001
```

Если используется HTTPS с локальным сертификатом, Postman может потребовать отключить SSL certificate verification для локальной проверки.

## Демо-учётные данные

```text
User: demouser@microsoft.com
Admin: admin@microsoft.com
Password: Pass@word1
```

## Smoke-проверка

После запуска приложения импортировать в Postman:

```text
postman/eshoponweb.smoke.postman_collection.json
postman/eshoponweb.local.postman_environment.json
```

Перед запуском убедиться, что переменная `webBaseUrl` соответствует фактическому адресу Web-приложения.
