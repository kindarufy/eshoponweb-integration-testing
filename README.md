# eShopOnWeb Integration Testing

**eShopOnWeb Integration Testing** — проект по интеграционному и E2E-тестированию open-source приложения **Microsoft eShopOnWeb**.

Исходный код eShopOnWeb не копируется в этот репозиторий. Здесь находятся только мои тестовые артефакты: стратегия, test plan, test cases, Postman smoke collection, findings, отчёт и вспомогательные инструкции.

## Объект тестирования

Microsoft eShopOnWeb — reference application на ASP.NET Core с каталогом, корзиной, оформлением заказа, Identity-аутентификацией, admin-интерфейсом и Public API.

Оригинальный проект:

```text
https://github.com/dotnet-architecture/eShopOnWeb
```

## Мой вклад

В рамках проекта подготовлены:

- integration test plan;
- стратегия Big Bang Integration Testing;
- ручные test cases;
- E2E checklist ключевых пользовательских сценариев;
- Postman smoke collection;
- реестр findings и рисков;
- security checklist;
- итоговый test report;
- инструкции по подготовке environment;
- scripts-подсказки для запуска приложения;
- CI-проверка структуры тестовых артефактов.

## Структура

```text
eshoponweb-integration-testing/
├── docs/
│   ├── environment.md
│   ├── security-checklist.md
│   ├── test-cases.md
│   ├── test-plan.md
│   └── test-strategy.md
├── checklists/
│   └── e2e-checklist.md
├── postman/
├── reports/
│   ├── anomalies.md
│   ├── findings.csv
│   ├── findings.md
│   └── test-report.md
├── scripts/
├── tools/
│   └── validate_artifacts.py
├── .github/workflows/ci.yml
└── README.md
```

## Подход

Для учебного анализа используется **Big Bang Integration Testing**: приложение рассматривается как уже собранная система, а проверка строится вокруг сквозных сценариев.

Покрываются:

- открытие и работа каталога;
- фильтрация и пагинация;
- корзина;
- authentication;
- оформление заказа;
- история заказов;
- административная часть;
- базовые API/smoke checks через Postman.

Ограничение подхода также зафиксировано: при падении длинного E2E-flow локализовать проблемный компонент сложнее, поэтому в отчёте есть рекомендации по дальнейшей декомпозиции тестирования.

## Быстрый старт

Клонировать репозиторий:

```bash
git clone https://github.com/nikamurkaa/eshoponweb-integration-testing.git
cd eshoponweb-integration-testing
```

Оригинальное приложение клонируется отдельно:

```bash
git clone https://github.com/dotnet-architecture/eShopOnWeb.git
```

Рекомендуемая структура:

```text
workspace/
├── eShopOnWeb/
└── eshoponweb-integration-testing/
```

Запуск оригинального проекта через Docker выполняется из его репозитория согласно его актуальной документации.

После запуска импортируйте в Postman:

```text
postman/eshoponweb.smoke.postman_collection.json
postman/eshoponweb.local.postman_environment.json
```

## Ключевые артефакты

1. [`docs/test-plan.md`](docs/test-plan.md) — объём и цели тестирования.
2. [`docs/test-strategy.md`](docs/test-strategy.md) — выбранный integration approach и ограничения.
3. [`docs/test-cases.md`](docs/test-cases.md) — ручные сценарии.
4. [`checklists/e2e-checklist.md`](checklists/e2e-checklist.md) — E2E coverage.
5. [`reports/findings.md`](reports/findings.md) — обнаруженные проблемы и риски.
6. [`reports/test-report.md`](reports/test-report.md) — итоговые выводы.
7. [`docs/security-checklist.md`](docs/security-checklist.md) — security-oriented checks.

## Проверка артефактов

```bash
python tools/validate_artifacts.py
```

CI workflow также проверяет структуру проекта автоматически.

## Статус

Проект завершён. Основные технические акценты — **integration testing, E2E, API testing, test design и техническая документация**.

## Автор

[Николь Журбенко](https://github.com/nikamurkaa)
