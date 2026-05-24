---
document: context
version: 1.0.0
last_updated: 2026-05-24
---

# CONTEXT — Entry Point for Hermes

Этот файл — первое, что читает Hermes в начале каждой итерации. Он не содержит правил или критериев — только карту проекта и порядок чтения.

---

## Что это за проект

Iterative research vault для выбора страны для переезда украинской пары. Один партнёр работает удалённо в IT (~$3000/мес), второй учится в украинском вузе. Главный фильтр — реалистичная легализация после 4 марта 2027 года.

Исследуется ~33 страны. Каждая получает полный практический research-pack: процедуры, документы, цены, сроки, контакты юристов, рабочие сообщества. Это не сравнительная аналитика — это рабочий гид для реального переезда.

Финальный синтез (TOP-N, рекомендация) — **отдельный** downstream-процесс, **не часть** работы Hermes.

---

## Два главных документа

| Документ | Что определяет |
|----------|----------------|
| `criteria.md` | **WHAT**: что исследовать, какие критерии, веса, тиры, список стран |
| `vault-protocol.md` | **HOW**: схемы файлов, frontmatter, шаблоны, modes итерации, DoD, self-improvement protocol |

При разногласии: домен (`criteria.md`) > форма (`vault-protocol.md`).

---

## Reading order для cold-start

1. **`CONTEXT.md`** (этот файл) — общая ориентация.
2. **`criteria.md`** — контракт ресёрча.
3. **`vault-protocol.md`** — правила работы и формат.
4. **`state.json`** — где остановилась предыдущая итерация.
5. **`proposals/queue.md`** — pending self-improvement (если есть `accepted` — применить до новой работы).
6. **`verification-queue.md`** (если выбран mode = `verification`).
7. **`INDEX.md`** — быстрый обзор прогресса всех стран.
8. **1–2 последних `runs/run-NNN-*.md`** — контекст последних действий.
9. **Релевантные файлы** по выбранной теме (`countries/<X>.md`, `claims/<X>.yml`).

`assumptions.md`, `open-questions.md`, `GLOSSARY.md` — читать по ситуации.

---

## Карта vault

```
relocation-vault/
├── CONTEXT.md              (this file — entry point)
├── criteria.md             (WHAT: criteria, weights, tiers, countries)
├── vault-protocol.md       (HOW: schemas, workflows, self-improvement)
├── GLOSSARY.md             (terms, scales, markers, tags)
├── MIGRATIONS.md           (schema migration recipes)
├── INDEX.md                (live progress map)
├── CHANGELOG.md            (short deltas per iteration)
├── IMPROVEMENT_LOG.md      (applied self-improvements)
├── state.json              (state v2, per-country, per-section)
├── countries.yml           (canonical 33-country list)
├── assumptions.md          (working hypotheses about the couple)
├── open-questions.md       (global open research questions)
├── verification-queue.md   (facts needing cross-reference)
├── countries/              (per-country research files)
├── claims/                 (atomic claims, machine-readable)
├── sources/                (central source registry)
├── dimensions/             (cross-country slices per criterion)
├── decisions/              (non-trivial decision log)
├── synthesis/              (skeleton for final synthesis — not written by Hermes)
├── digests/                (weekly digests)
├── proposals/              (self-improvement proposals)
├── runs/                   (immutable iteration history)
├── scripts/                (validators: Python)
└── archive/                (old files preserved during resets/migrations)
```

---

## Ключевые концепции (см. `GLOSSARY.md` для полных определений)

- **Tier 1/2/3/X** — классификация страны по долгосрочному потенциалу.
- **depth_score (0–10)** — насколько полно покрыта страна (см. `vault-protocol.md` §7).
- **Mode of iteration** — `bootstrap`, `country-deep-dive`, `criterion-slice`, `verification`, `cross-reference`, `staleness-check`, `consolidation`, `proposal-apply`.
- **L1 / L2 / L3 autonomy** — что Hermes может менять автономно vs через proposal.
- **DoD (Definition of Done)** — чек-лист завершённости секции; см. `vault-protocol.md` §7.
- **`[требует верификации]`** — маркер неподтверждённого факта; не используется в скоринге.
- **`[stale, last verified YYYY-MM-DD]`** — маркер устаревшего факта.

---

## Всегда-первые правила (Always-do)

1. **Pre-flight** перед любой работой (см. `vault-protocol.md` §8).
2. **Если pre-flight упал** — `recovery mode`, не трогать data файлы, эскалировать.
3. **Если есть `accepted` proposals** — применить их **до** нового ресёрча.
4. **Anti-rework**: перед записью читать существующее содержание секции.
5. **Anti-clustering**: не более 3 итераций подряд по одной стране.
6. **Confidence обязателен** для всех фактов в claims и для критичных фактов в прозе.
7. **Source ID, не URL** — в `countries/*.md` ссылаться по `[src-NNN]`, URL в `sources.md`.
8. **Post-flight** перед завершением итерации.
9. **Telegram-уведомление** в стандартном формате (см. `vault-protocol.md` §14).

---

## Что Hermes **никогда** не делает автономно

- Не меняет `criteria.md` (L3 — только через proposal + approve).
- Не меняет `vault-protocol.md` (L3 — только через proposal + approve).
- Не меняет веса, DoD checklists, confidence scale без approve.
- Не удаляет собранные данные — только архивирует через `archive/` с записью в `decisions.md`.
- Не делает git commit / push.
- Не составляет финальный TOP-N рейтинг — это downstream-процесс.
- Не отправляет ничего в Telegram сверх стандартных уведомлений.

---

## Финальное правило

Если что-то непонятно или возник spec gap — **создать proposal** в `proposals/`, не угадывать.
