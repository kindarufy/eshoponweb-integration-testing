# eShopOnWeb Integration Testing

Кейс по интеграционному тестированию учебного ASP.NET Core-приложения **Microsoft eShopOnWeb**.

Проект оформлен как портфолио-кейс: в репозитории собраны тестовые артефакты, которые показывают подход к планированию, проведению и документированию интеграционного тестирования готового веб-приложения.

## GitHub About

Рекомендуемое описание для поля **About / Description** на GitHub:

```text
Integration testing case study for Microsoft eShopOnWeb: test plan, Big Bang strategy, E2E checklist, Postman smoke collection, findings register, and final report.
```

Рекомендуемые topics:

```text
testing, integration-testing, qa, postman, test-plan, checklist, dotnet, aspnetcore, eshoponweb, portfolio
```

## Объект тестирования

Объектом тестирования является внешний open-source проект:

```text
Microsoft eShopOnWeb
https://github.com/dotnet-architecture/eShopOnWeb
```

По приложенному архиву `eShopOnWeb-main.zip` проект представляет собой ASP.NET Core reference application с веб-интерфейсом, каталогом товаров, корзиной, оформлением заказа, Identity-аутентификацией, административной частью и отдельным `PublicApi`, который используется admin-интерфейсом.

Важно: исходный код eShopOnWeb **не входит** в этот репозиторий. Этот репозиторий содержит только мои тестовые материалы: тест-план, стратегию, чек-листы, Postman-коллекцию, реестр findings, отчёты и вспомогательные инструкции.

## Мой вклад

В рамках проекта подготовлены:

- тест-план интеграционного тестирования;
- стратегия Big Bang Integration Testing;
- набор тест-кейсов для ручной проверки;
- E2E-чек-лист основных пользовательских сценариев;
- Postman-коллекция для базовой smoke-проверки;
- реестр тестовых находок и рисков;
- итоговый отчёт;
- инструкции по запуску eShopOnWeb для тестирования;
- скрипты-подсказки для запуска приложения;
- CI-проверка структуры тестовых артефактов.

## Структура репозитория

```text
eshoponweb-integration-testing/
├── README.md
├── docs/
│   ├── environment.md
│   ├── security-checklist.md
│   ├── test-cases.md
│   ├── test-plan.md
│   └── test-strategy.md
├── checklists/
│   └── e2e-checklist.md
├── postman/
│   ├── eshoponweb.local.postman_environment.json
│   └── eshoponweb.smoke.postman_collection.json
├── reports/
│   ├── anomalies.md
│   ├── findings.csv
│   ├── findings.md
│   └── test-report.md
├── scripts/
│   ├── run-eshoponweb.ps1
│   └── run-eshoponweb.sh
├── tools/
│   └── validate_artifacts.py
├── .github/workflows/ci.yml
├── .editorconfig
├── .gitignore
└── LICENSE
```

## Подход к тестированию

Для учебного кейса выбран подход **Big Bang Integration Testing**.

При таком подходе приложение рассматривается как уже собранная единая система, а тестирование выполняется через сквозные пользовательские сценарии:

- открытие главной страницы;
- просмотр каталога;
- фильтрация и пагинация товаров;
- добавление товара в корзину;
- изменение состава корзины;
- авторизация пользователя;
- оформление заказа;
- проверка истории заказов;
- проверка административной части;
- smoke-проверки через Postman.

Такой подход подходит для учебного анализа, но имеет ограничение: если ошибка возникает на сквозном сценарии, сложнее сразу определить, в каком модуле находится причина. Поэтому в отчёте отдельно зафиксированы риски и рекомендации по дальнейшей декомпозиции тестирования.

## Быстрый старт

### 1. Клонировать этот репозиторий

```bash
git clone https://github.com/kindarufy/eshoponweb-integration-testing.git
cd eshoponweb-integration-testing
```

### 2. Клонировать оригинальный eShopOnWeb отдельно

```bash
git clone https://github.com/dotnet-architecture/eShopOnWeb.git
```

Рекомендуемая структура папок рядом друг с другом:

```text
workspace/
├── eShopOnWeb/
└── eshoponweb-integration-testing/
```

### 3. Запустить eShopOnWeb

Вариант через Docker из корня оригинального eShopOnWeb:

```bash
cd eShopOnWeb
docker compose build
docker compose up
```

После запуска Web-приложение обычно доступно на:

```text
http://localhost:5106
```

Public API обычно доступен на:

```text
http://localhost:5200
```

Альтернативный запуск без Docker описан в `docs/environment.md`.

### 4. Импортировать Postman-коллекцию

В Postman импортировать файлы:

```text
postman/eshoponweb.smoke.postman_collection.json
postman/eshoponweb.local.postman_environment.json
```

По умолчанию в environment используется:

```text
webBaseUrl = http://localhost:5106
```

### 5. Запустить smoke-проверки

В Postman выбрать environment `eShopOnWeb Local` и запустить коллекцию `eShopOnWeb Smoke Tests`.

Коллекция проверяет базовую доступность ключевых страниц и не заменяет полноценное E2E-тестирование через браузер.

## Тестовые учётные данные

В eShopOnWeb для демо-входа используются:

```text
User: demouser@microsoft.com
Admin: admin@microsoft.com
Password: Pass@word1
```

Эти данные используются только для локального тестирования demo-приложения.

## Документация

Основные материалы:

- `docs/test-plan.md` — тест-план;
- `docs/test-strategy.md` — стратегия Big Bang Integration Testing;
- `docs/test-cases.md` — тест-кейсы;
- `docs/security-checklist.md` — базовый security-чек-лист;
- `checklists/e2e-checklist.md` — чек-лист сквозных сценариев;
- `reports/findings.csv` — реестр findings;
- `reports/test-report.md` — итоговый отчёт.

## Важное уточнение про findings

Файл `reports/findings.csv` содержит не только подтверждённые баги, а **тестовые находки, риски и сценарии для проверки**.

Это сделано специально: без полного воспроизводимого прогона, скриншотов, логов и точных окружений некорректно называть каждую проблему доказанным дефектом. Поэтому часть записей имеет тип `Risk`, `Observation`, `Coverage Gap` или `Security Test Scenario`.

Такой формат честнее и профессиональнее для портфолио.

## Проверка структуры проекта

В репозитории есть скрипт, который проверяет, что основные артефакты на месте, Postman JSON валиден, а CSV с findings имеет нужные колонки.

```bash
python tools/validate_artifacts.py
```

GitHub Actions запускает эту проверку при push и pull request.

## Что демонстрирует проект

Проект показывает навыки:

- анализа внешнего open-source приложения как объекта тестирования;
- планирования интеграционного тестирования;
- подготовки тестовой документации;
- проектирования E2E-сценариев;
- работы с Postman;
- оформления реестра findings;
- описания ограничений тестирования.

## Статус проекта

Проект является учебным портфолио-кейсом по интеграционному тестированию. Исходный код eShopOnWeb не изменялся и не включался в этот репозиторий.
