---
document: vault-protocol
version: 1.0.0
last_updated: 2026-05-24
status: active
companion: criteria.md
---

# Vault Protocol (HOW)

Этот документ описывает **как** хранить, обновлять и переиспользовать данные ресёрча. Что именно исследовать — в `criteria.md`.

При разногласии:
- Вопросы домена (что искать, веса, тиры) — `criteria.md` главный.
- Вопросы формы (где хранить, как структурировать, какой workflow) — `vault-protocol.md` главный.

---

## 1. Структура vault

```
relocation-vault/
├── CONTEXT.md                    # entry point для агента
├── criteria.md                   # WHAT: критерии и веса
├── vault-protocol.md             # HOW: схемы, шаблоны, правила (этот файл)
├── GLOSSARY.md                   # термины, шкалы, маркеры, теги
├── MIGRATIONS.md                 # рецепты миграций между schema-версиями
├── INDEX.md                      # авто-обновляемая карта прогресса
├── CHANGELOG.md                  # короткие deltas
├── IMPROVEMENT_LOG.md            # лог применённых self-improvement
├── state.json                    # state v2 (per-country, per-section)
├── countries.yml                 # canonical список 33 стран
├── assumptions.md                # рабочие гипотезы про пару
├── open-questions.md             # глобальные открытые вопросы
├── verification-queue.md         # очередь верификаций
├── countries/
│   ├── _TEMPLATE.md              # шаблон для новых стран
│   └── <страна>.md               # профили с frontmatter
├── claims/
│   └── <страна>.yml              # atomic claims (критичные факты)
├── sources/
│   └── sources.md                # центральный реестр источников
├── dimensions/
│   └── <criterion>.md            # cross-country слайсы
├── decisions/
│   └── decisions.md              # лог нетривиальных решений
├── synthesis/
│   └── final-synthesis.md        # скелет итогового документа
├── digests/
│   └── week-NN.md                # еженедельные сводки
├── proposals/
│   ├── queue.md                  # индекс pending-proposals
│   ├── log.md                    # история (applied/rejected)
│   └── proposal-NNN-*.md         # individual proposals
├── runs/
│   └── run-NNN-*.md              # immutable history
├── scripts/
│   ├── validate-frontmatter.py
│   ├── check-sources.py
│   ├── find-stale.py
│   └── dump-state.py
└── archive/                      # старые файлы при ресетах/миграциях
```

---

## 2. Reading order для cold-start агента

Каждая итерация Hermes начинается с холодного старта. В **строгом порядке** читать:

1. `CONTEXT.md` (~150 строк) — общая картина.
2. `criteria.md` — что исследовать (контракт).
3. `vault-protocol.md` (этот файл) — как работать.
4. `state.json` — где остановилась предыдущая итерация.
5. `proposals/queue.md` — pending self-improvement (если есть accepted — применить перед работой).
6. `verification-queue.md` (если выбран mode = verification).
7. `INDEX.md` — быстрый обзор прогресса.
8. 1–2 последних `runs/run-NNN-*.md` для контекста.
9. Релевантные файлы по текущей теме: `countries/<X>.md`, `claims/<X>.yml`, и т.д.

`assumptions.md`, `open-questions.md`, `GLOSSARY.md` — читаются по ситуации.

---

## 3. File schemas

### 3.1. `countries/<страна>.md` frontmatter

```yaml
---
country: Greece
tier: 1                            # 1, 2, 3, X — заполняется по итогам
depth_score: 4                     # 0–10
last_updated: 2026-05-24T11:00:00Z
sections_completed: [5.1, 5.2]     # секции с DoD = passed
sections_partial: [5.3]            # частично покрытые
sections_pending: [5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11]
risk_flags: [unmarried-partner-dependency, exact-dn-threshold]
sources_used: [src-001, src-005, src-012]
unverified_count: 4
tier_rationale_ref: "section-1-summary"
schema_version: 2.0.0
---
```

После frontmatter — содержание профиля по блокам 1–8 (см. §4 ниже).

### 3.2. `runs/run-NNN-*.md` frontmatter

```yaml
---
run_id: 003
date: 2026-05-25T08:00:00Z
agent: hermes
mode: country-deep-dive            # см. §6
target_country: Greece              # nullable
target_sections: [5.4, 5.5]         # nullable
target_criterion: null              # для criterion-slice
duration_minutes: 45
sources_added: [src-045, src-046]
facts_added: 12
facts_verified: 3
claims_added: [claim-greece-007]
files_modified:
  - countries/greece.md
  - state.json
  - sources/sources.md
  - claims/greece.yml
proposals_created: []
completed_at: 2026-05-25T08:45:00Z   # nullable — отсутствие означает aborted
status: completed | aborted | partial
schema_version: 2.0.0
---
```

Тело: «План», «Что сделано», «Что осталось», «Открытые вопросы добавлены», «Рекомендация для следующей итерации».

### 3.3. `state.json` v2 schema

```json
{
  "version": 2,
  "iteration": 5,
  "schema_doc": "criteria.md",
  "schema_doc_version": "2.0.0",
  "protocol_doc": "vault-protocol.md",
  "protocol_doc_version": "1.0.0",
  "last_run_timestamp": "2026-05-25T08:45:00Z",
  "current_focus": {
    "mode": "country-deep-dive",
    "country": "Greece",
    "sections": ["5.4", "5.5"]
  },
  "next_iteration_hint": {
    "suggested_mode": "country-deep-dive",
    "suggested_country": "Portugal",
    "reason": "Lowest depth_score among Tier-1 candidates"
  },
  "countries": {
    "Greece": {
      "tier": 1,
      "tier_confidence": "medium",
      "depth_score": 4,
      "sections_completed": ["5.1", "5.2"],
      "sections_partial": ["5.3"],
      "sections_pending": ["5.4","5.5","5.6","5.7","5.8","5.9","5.10","5.11"],
      "risk_flags": ["unmarried-partner-dependency"],
      "last_iteration": 4
    }
  },
  "verification_queue_size": 6,
  "sources_count": 12,
  "claims_count": 24,
  "proposals_pending": 1
}
```

### 3.4. `sources/sources.md` format

```markdown
## src-005
- **Title**: Greek Law 5078/2023, Article 194
- **URL**: https://www.kodiko.gr/nomologia/document/...
- **Archive**: https://web.archive.org/web/20260524/https://...
- **Type**: official-primary
- **Date published**: 2023-12-20
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: TP→ВНЖ transition rule (claim-greece-002)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-24
```

Типы: `official-primary`, `official-secondary`, `reputable-secondary`, `community`, `commercial`, `aggregator`.

### 3.5. `claims/<страна>.yml` format

Atomic claims — только для критичных фактов (визы, налоговые ставки, ПМЖ-сроки, минимальные доходы).

```yaml
- id: claim-greece-001
  topic: dn_visa_income_threshold
  value: 3500
  unit: EUR/month
  source: src-005
  date_verified: 2026-05-24
  confidence: high                # см. §5
  tags: [dn-visa, income-threshold, eu]
  notes: "Required gross monthly income for primary applicant"

- id: claim-greece-002
  topic: tp_to_vnzh_transition
  value: "Law 5078/2023 Art.194 allows direct transition without leaving country"
  source: src-007
  date_verified: 2026-05-24
  confidence: high
  tags: [tp-transition, post-2027, legislated]
```

### 3.6. `dimensions/<criterion>.md` format

Cross-country слайсы, заполняемые в `mode: criterion-slice`.

```markdown
# Dimension: DN-visa income thresholds (5.1)

Last updated: 2026-05-25
Source dimension claim_id: dn_visa_income_threshold

| Country | Threshold | Unit | Source | Date Verified | Confidence |
|---|---:|---|---|---|---|
| Greece | 3500 | EUR/mo | src-005 | 2026-05-24 | high |
| Portugal | 3480 | EUR/mo | src-043 | 2026-05-25 | high |
| Spain | 2762 | EUR/mo | src-052 | 2026-05-25 | medium-high |
```

### 3.7. `verification-queue.md` format

```markdown
## vq-007 [high priority]
- **Fact**: "Greece DN visa requires €3500/mo income"
- **Country**: Greece
- **Section**: 5.1
- **Current source**: src-005 (community, 2025-08)
- **Why uncertain**: Single community post, no official confirmation found
- **Suggested verification**: Check migration.gov.gr official DN page; check Law 5089/2023
- **Created**: 2026-05-24 (run-002)
- **Status**: pending | in-progress | resolved | dropped
```

### 3.8. `proposals/proposal-NNN-*.md` format

См. §13 (Self-improvement protocol).

### 3.9. `decisions/decisions.md` format

```markdown
## 2026-05-25 — Greece classified as Tier 1
**Decision**: Greece → Tier 1.
**Rationale**: Law 5078/2023 Art.194 makes TP→ВНЖ transition explicit and legislated, not declarative. PR in 5 years, citizenship in 7. DN visa available. 50% tax reduction for new residents.
**Source**: src-005, src-007, src-012.
**Iteration**: run-002.
**Counterevidence considered**: Exact DN income threshold (€3500) is at the upper edge of $3000 budget — flagged but not disqualifying.
```

### 3.10. `CHANGELOG.md`

```markdown
## 2026-05-25 — run-005
- Greece: depth_score 4 → 6 (sections 5.4, 5.5 completed)
- Sources added: src-045, src-046, src-047
- Claims added: claim-greece-007, claim-greece-008
- Proposals created: 1 (proposal-003, pending)
- Verification queue: 6 → 4 (2 resolved)
```

---

## 4. Output structure per country (8 blocks)

Каждый `countries/<страна>.md` содержит после frontmatter:

### Блок 1 — Сводка
Tier (с 2-3 предложениями обоснования), depth_score, дата последнего обновления, ссылка на `decisions/decisions.md` если тир дискуссионный.

### Блок 2 — Скоринг
Таблица: критерий | балл 1–10 | confidence | краткое обоснование | ссылка на секцию профиля. Все 9 критериев из `criteria.md` §4.

### Блок 3 — Профиль по разделам
Разделы 5.1–5.11. Каждый со своим заголовком и маркером:

```markdown
## 5.1. Легализация {status: deep, depth: 3, last_updated: 2026-05-24, dod: passed}
```

### Блок 4 — Измерения риска
Сводка по 5.10: 4 категории риска с уровнем (низкий/средний/высокий) и обоснованием.

### Блок 5 — Практический вывод
- Можно переехать сейчас: да / нет / сложно / только при условии X.
- Лучший путь легализации для мужчины.
- Лучший путь легализации для девушки.
- Меняет ли ситуацию брак.
- Реалистичность остаться после 03.2027: высокая / средняя / низкая.
- Главные плюсы (3–5).
- Главные минусы / риски (3–5).

### Блок 6 — Practical playbook
Пошаговый рабочий гид: до переезда / первый месяц / первые 3–6 месяцев / до марта 2027 / долгосрочно / бюджет переезда таблицей / контакты и сообщества. См. подробный спек в `_TEMPLATE.md`.

### Блок 7 — Источники
По категориям:
- 7a. Официальные первичные.
- 7b. Надёжные вторичные.
- 7c. Комьюнити и форумы (с обязательными датами постов).
- 7d. Стат/коммерческие.
- 7e. Не найдено (явный список того, что искалось безуспешно).

Ссылки — по ID источника (`[src-NNN]`), а не дублировать URL.

### Блок 8 — Открытые вопросы и пометки верификации
Все `[требует верификации]` для этой страны + ссылки на соответствующие записи в `verification-queue.md`.

---

## 5. Confidence scale (формализована)

| Уровень | Определение |
|---------|-------------|
| **high** | Официальный первичный источник, 2025–2026; либо ≥2 независимых официальных. |
| **medium-high** | Официальный первичный 2023–2024 (возможно устарел) или 2+ cross-referenced reputable secondary 2025–2026. |
| **medium** | Один reputable secondary 2025–2026, или 3+ форумных поста 2025–2026 с согласующимися данными. |
| **low** | Единичный форумный пост, экспертная оценка без подтверждения, или старые (2023–) данные без cross-reference. |
| **N/A** | `[требует верификации]` — факт не используется в скоринге. |

В atomic claims confidence обязателен. В прозе — для критичных фактов рекомендован.

---

## 6. Modes of iteration

Hermes выбирает один из режимов на каждую итерацию. В state.json фиксируется `current_focus.mode`.

| Mode | Описание | Цель за итерацию |
|------|----------|-------------------|
| `bootstrap` | Первичное создание vault структуры | Все необходимые директории и файлы созданы |
| `country-deep-dive` | Глубокий ресёрч одной страны | +2 к depth_score, минимум 2 секции закрыты до DoD |
| `criterion-slice` | Один критерий через несколько стран | Минимум 4 страны покрыты по этому критерию, обновлён `dimensions/<criterion>.md` |
| `verification` | Закрытие `[требует верификации]` маркеров | Минимум 5 элементов очереди закрыто или dropped |
| `cross-reference` | Сверка фактов между странами/источниками | Найдены расхождения, отмечены, добавлены в decisions log |
| `staleness-check` | Обновление устаревших фактов | Обновлены факты старше threshold (см. §10) |
| `consolidation` | Мердж дубликатов, нормализация | Дубликаты удалены/смерджены, структура нормализована |
| `proposal-apply` | Применение accepted proposals | Все accepted proposals применены, версии повышены |

### Выбор mode по умолчанию

Логика выбора:

1. Если есть accepted proposals в `proposals/queue.md` → `proposal-apply`.
2. Если `verification_queue_size > 10` → `verification`.
3. Если средний возраст фактов превысил staleness threshold для какого-то типа → `staleness-check`.
4. Если есть страна с `depth_score < 7` → `country-deep-dive` (берём с минимальным depth среди не-Tier-X).
5. Если все базовые страны на depth ≥ 7 → `criterion-slice` (по критерию с самым неполным `dimensions/<criterion>.md`).
6. Если ничего — `consolidation`.

---

## 7. Definition-of-Done per section

Секция считается `completed` когда выполнены **все** пункты её DoD. Иначе `partial`.

### 5.1. Легализация
- [ ] Все применимые пути перечислены с official-primary ссылками.
- [ ] Минимальный доход для каждого пути верифицирован (claim-запись).
- [ ] Список документов с пометками апостиль/перевод для каждого пути.
- [ ] Post-March-2027 transition pathway документирован с ссылкой на закон.
- [ ] Polish karta pobytu interaction explicitly addressed.
- [ ] Personal playbook для нашей пары присутствует.
- [ ] Все факты в секции имеют confidence ≥ medium.

### 5.2. Климат
- [ ] Январь/июль температура в 3+ городах.
- [ ] Солнечные дни в году.
- [ ] Влажность и комфорт круглый год.

### 5.3. Налоги
- [ ] Эффективная ставка для $3000/мес посчитана в применимом режиме.
- [ ] Конкретный пример расчёта gross → net.
- [ ] Процедура регистрации режима описана.
- [ ] Льготы для новых резидентов / IT покрыты.
- [ ] Налоговый эффект брака описан.

### 5.4. Стоимость жизни
- [ ] Расходы для 2+ городов посчитаны.
- [ ] Вывод по бюджету $3000/мес явный.

### 5.5. Аренда
- [ ] Цены 2BR для 3+ городов с диапазонами.
- [ ] % от $3000 рассчитан.
- [ ] 2+ платформы поиска для страны.
- [ ] Требования арендодателя описаны.

### 5.6. Медицина
- [ ] Как встать на учёт после переезда.
- [ ] Стоимость частной страховки на двоих.
- [ ] Условия для беременных / роды.

### 5.7. Образование (будущий ребёнок)
- [ ] Стоимость детских садов.
- [ ] Качество гос школ для иностранцев.
- [ ] Альтернатива международной школы со стоимостью.

### 5.8. Комфорт
- [ ] Безопасность с конкретными данными.
- [ ] Отношение к украинцам с источниками.
- [ ] Уровень английского.

### 5.9. Партнёр
- [ ] Статус как dependent/partner с браком и без.
- [ ] Возможность ВНЖ как студент украинского вуза.
- [ ] Возможность работы.
- [ ] Минимальный доход спонсора.

### 5.10. Измерения риска
- [ ] Все 4 категории риска (валюта/банки, политика, связь с Украиной, диаспора) оценены.

### 5.11. Бюрократия
- [ ] Сроки рассмотрения для основных путей.
- [ ] Можно ли подаваться изнутри или из УА.
- [ ] Контакты юристов (минимум 1).

### depth_score arithmetic

```
depth_score = (количество completed секций) + 0.5 * (количество partial)
```

Максимум — 10 (округление). Достижение 10 = все 11 секций completed + есть Practical Playbook в Блоке 6.

---

## 8. Pre-flight checks

Hermes в начале каждой итерации выполняет:

1. `state.json` парсится и соответствует schema v2.
2. Все frontmatter в `countries/*.md` валидны (можно запустить `scripts/validate-frontmatter.py`).
3. Все `[src-NNN]` ссылки в файлах находят запись в `sources.md` (запустить `scripts/check-sources.py`).
4. Нет полу-записанных runs (run-файл существует, но `status` != `completed`/`aborted`/`partial`).
5. Если `proposals/queue.md` содержит accepted — добавить в план итерации.

Если **любой** check провалился → не делать новый ресёрч. Войти в `recovery mode` (см. §9).

## 9. Recovery mode

Если pre-flight нашёл проблему:

1. Создать `runs/run-NNN-recovery.md` с `mode: recovery`.
2. Описать что найдено.
3. **Не пытаться чинить автоматически.** Создать proposal с предложением фикса или эскалировать в Telegram.
4. Завершить итерацию без изменений в data файлах.

Исключение: если предыдущий run явно `status: aborted` или has missing `completed_at` — можно безопасно перезаписать его сводку и пометить `cleaned-up: true`.

## 10. Post-flight checks

В конце каждой итерации Hermes валидирует свою работу:

1. Frontmatter обновлён в изменённых `countries/*.md` (depth_score, sections_completed, last_updated).
2. Все новые источники в `sources.md`.
3. Run-лог создан, `completed_at` заполнен, `status: completed`.
4. `state.json` обновлён (iteration +1, current_focus, last_run_timestamp).
5. `CHANGELOG.md` дополнен короткой строкой.
6. `INDEX.md` обновлён.
7. Telegram-уведомление отправлено в стандартном формате (см. §14).

Если post-flight check фейлится — попытка одна, иначе run помечается `status: partial` и проблема логируется.

---

## 11. Anti-rework rule

Перед записью новой информации в секцию страны:

1. Прочитать существующее содержание секции.
2. Если confidence ≥ medium-high и last_updated < 6 месяцев — **не переписывать**. Только дополнять (новые подразделы, уточнения).
3. Если confidence = low или factual conflict с найденным — записать новую версию, **старую переместить в `archive/`-фрагмент с датой**, добавить запись в `decisions/decisions.md`.

Никогда не удалять собранные данные без записи в decisions log.

## 12. Anti-clustering rotation

Hermes не делает `country-deep-dive` по одной и той же стране более **3 итераций подряд**. После 3 итераций по одной стране обязательная ротация:
- Другая страна с близким приоритетом, либо
- Другой mode (criterion-slice, verification, etc.).

Это защищает от over-specialization на одной стране и обеспечивает равномерное покрытие.

## 13. Self-improvement protocol

### 13.1. Уровни автономии

| Уровень | Что Hermes может делать | Когда |
|---|---|---|
| **L1 — free** | Дополнять `countries/*.md`, `claims/*.yml`, `sources.md`, `state.json`, `runs/*.md`, `verification-queue.md`, `decisions.md`, `CHANGELOG.md`, `INDEX.md`, `digests/week-*.md` | Всегда |
| **L2 — log-and-apply** | Менять `countries/_TEMPLATE.md`, добавлять теги в `GLOSSARY.md`, расширять `scripts/`, обновлять секции `vault-protocol.md` помеченные `[L2-editable]` | После одобрения proposal'а один раз — далее свободно |
| **L3 — propose-only** | Менять `criteria.md`, основу `vault-protocol.md`, DoD checklists, веса, шкалу confidence | Только через explicit proposal + ручное одобрение |

### 13.2. Proposal lifecycle

1. **Триггер**: Hermes наблюдает паттерн **2+ раза** в разных run'ах. Не предлагает по единичному наблюдению.
2. **Лимит**: максимум **1 proposal на итерацию**. Если идей больше — выбрать самую важную.
3. **Дедупликация**: перед созданием proposal сканировать `proposals/log.md`. Если такое уже было rejected — не предлагать без новых evidence.

### 13.3. Proposal format

`proposals/proposal-NNN-<slug>.md`:

```yaml
---
proposal_id: 003
created: 2026-05-25T10:00:00Z
agent: hermes
type: protocol-change | criteria-change | template-update | workflow-tip | dod-refinement | new-source | query-pattern | new-mode | schema-evolution | new-country
target_file: vault-protocol.md
target_section: "8.2"
severity: low | medium | high
evidence_runs: [run-005, run-007, run-012]
expected_benefit: "Reduce time per country by ~15min"
risks: ["Minor risk of X"]
revert_recipe: "Restore vault-protocol.md to version 1.2.0; remove section 8.2.1"
status: pending           # pending | accepted | rejected | applied | reverted
reviewed_by: null
reviewed_at: null
applied_in_iteration: null
---

## Observation
[Что Hermes заметил во время работы — конкретные runs и моменты]

## Proposed change
[Конкретная правка — diff или новый текст секции]

## Why this helps
[Ожидаемый выигрыш]

## Trade-offs
[Что теряем]

## Test plan
[Как проверить эффективность после применения]
```

### 13.4. Approval flow

1. Hermes создаёт proposal → отправляет Telegram-уведомление с кратким суммари.
2. Пользователь approve/reject через Telegram (через interactive buttons бота) или вручную правит `status:` в файле.
3. На следующей итерации Hermes:
   - Сканирует `proposals/queue.md`.
   - Для каждого `status: accepted` без `applied_in_iteration`:
     a. Делает правку в `target_file`.
     b. Повышает semver target_file (patch для template/workflow, minor для template change with new fields, major для breaking schema change).
     c. Записывает migration recipe в `MIGRATIONS.md` если нужно.
     d. Логирует в `IMPROVEMENT_LOG.md`.
     e. Меняет `status: applied`, заполняет `applied_in_iteration`.
   - Отправляет Telegram «✅ Applied #NNN».

### 13.5. Severity gating для Telegram

- **High**: уведомление сразу, требует ответа в течение 24ч.
- **Medium**: уведомление сразу, без срочности.
- **Low**: накапливается, отправляется батчем в weekly digest.

### 13.6. Reverting

Если применённое улучшение оказалось плохим — пользователь меняет `status: reverted` в applied proposal. Hermes применяет `revert_recipe` на следующей итерации.

---

## 14. Telegram format spec

### 14.1. Per-iteration сообщение

```
🤖 Hermes iter #{iteration_id}
Mode: {mode}
Target: {country/criterion} (sections {list})
Δ depth_score: +{delta} → {new_value}
Sources added: {count} ({src-IDs})
Verified: {count} facts
Flags: {count} new ({short list})
Next: {suggested_next_target}
```

Объём: ≤ 8 строк, ≤ 500 символов. Никакой прозы.

### 14.2. Proposal-уведомление

```
📝 New proposal #{NNN} [{severity}]
Type: {type}
Title: {one-line}

Observation: {≤120 chars}
Expected benefit: {≤80 chars}

[Approve] [Reject] [View]
```

### 14.3. Weekly digest

Раз в неделю (cron, отдельный job):

```
📊 Weekly digest — week NN

Iterations: {count}
Countries advanced: {list with Δ depth}
DoD passed sections this week: {count}
Sources added: {count}
Verifications resolved: {count}
Proposals: {created/accepted/applied/rejected counts}

Top finding: {≤200 chars}
Risk surfaced: {≤200 chars}
Bottleneck: {≤200 chars}

Pending action items for you:
- {≤4 bullets}
```

Объём: ≤ 25 строк, ≤ 1500 символов.

### 14.4. Health/error alert

```
⚠️ Hermes pre-flight failed (iter #{iteration_id})
Issue: {short description}
Action taken: recovery mode, no changes applied
Suggested fix: {if known}
```

---

## 15. Source handling rules

### 15.1. Категории источников

- **official-primary**: миграционные ведомства, налоговые службы, тексты законов на офиц. сайтах, EUR-Lex для EU решений.
- **official-secondary**: правительственные брошюры, посольские страницы, EU-уровневые fact-sheets.
- **reputable-secondary**: PWC/EY/Deloitte/KPMG налоговые гайды, статьи известных миграционных юристов с указанием автора.
- **community**: Reddit, Telegram-каналы, FB-группы, форумы — только с **датой исходного сообщения**.
- **commercial**: Numbeo, Idealista, и т.п.
- **aggregator**: VisaGuide.world, NomadList, Wikipedia — стартовая точка, не первичный источник.

### 15.2. Дата исходного сообщения

Для community-источников **обязательна дата исходного поста**, не только дата чтения. Без даты — `[без даты, требует верификации]`, факт не используется в скоринге.

### 15.3. Приоритет дат

- 2025–2026: можно использовать как факт (с соответствующим confidence).
- 2024: можно использовать с пометкой `[данные 2024, проверить актуальность]`.
- ≤ 2023: только как ориентир, с пометкой `[данные старше 2024, требует свежей верификации]`.

### 15.4. Cross-reference rule

Если 2–3 независимых поста подтверждают одно и то же → сигнал, но всё равно сверить с official-primary. Если official-primary найден — community становится `supporting`, не `primary`.

### 15.5. Конфликт между источниками

Если данные противоречат:
- Приоритет у official-primary.
- Расхождение явно фиксируется в формате: «по {src-A} ({date}): X; по {src-B} ({date}): Y».
- Создаётся запись в `decisions/decisions.md`.

### 15.6. Single-source flag

Если важный факт только из одного источника → пометить `[единственный источник]` и добавить в `verification-queue.md` для cross-reference на следующей итерации.

### 15.7. Web archive snapshots

Для всех URL **кроме стабильных gov-доменов** (`*.gov.*`, `*.gob.*`, `eur-lex.europa.eu`, etc.) — сохранить Wayback Machine snapshot URL рядом с original URL в `sources.md`.

Способ создания snapshot: `https://web.archive.org/save/{URL}` (через web fetch). Если Wayback недоступен — пометка `[archive: failed YYYY-MM-DD]`.

### 15.8. Sources cross-referencing

Если факт применим к N странам (например, EU TP extension до 03.2027) — **один** источник в `sources.md`, ссылается из каждой страны. Не дублировать.

---

## 16. Staleness rules

| Тип фактов | Threshold устаревания |
|------------|----------------------|
| Визы / иммиграция / TP правила | 6 месяцев |
| Налоги / налоговые режимы | 12 месяцев (актуальный налоговый год) |
| Цены аренды | 6 месяцев |
| Стоимость жизни / цены продуктов | 6 месяцев |
| Климат / география | бессрочно |
| Школы / детсады / стоимость | 12 месяцев |
| ПМЖ / гражданство / процедуры | 12 месяцев |

Когда `date_verified` факта старше threshold:
- Факт всё ещё используется, но с пометкой `[stale, last verified YYYY-MM-DD]`.
- Confidence понижается на одну ступень (high → medium-high, и т.д.).
- Факт автоматически попадает в очередь `mode: staleness-check`.

---

## 17. Anti-bloat (длина секций)

Чтобы профили не превращались в эссе:

| Секция | Soft target (слов) |
|--------|-------------------:|
| 5.1 Легализация | 1200–2500 (главная секция, разрешено больше) |
| 5.2 Климат | 200–400 |
| 5.3 Налоги | 800–1500 |
| 5.4 Стоимость жизни | 500–900 |
| 5.5 Аренда | 600–1000 |
| 5.6 Медицина | 400–700 |
| 5.7 Образование | 300–500 |
| 5.8 Комфорт | 300–500 |
| 5.9 Партнёр | 500–800 |
| 5.10 Риски | 400–700 |
| 5.11 Бюрократия | 300–500 |
| Practical Playbook (Блок 6) | 800–1800 |

Если секция выходит за верхний предел — это сигнал, что её стоит разбить или сократить.

---

## 18. Validators (`scripts/`)

Простые скрипты для health-check vault. Hermes запускает в pre-flight и/или post-flight.

### `validate-frontmatter.py`
- Парсит YAML frontmatter всех `countries/*.md` и `runs/*.md`.
- Проверяет наличие обязательных полей, типы, валидность `schema_version`.
- Вывод: список файлов с проблемами или OK.

### `check-sources.py`
- Сканирует все `*.md` файлы на наличие `[src-NNN]` ссылок.
- Проверяет, что каждый ID есть в `sources/sources.md`.
- Обратно: предупреждает о sources, на которые никто не ссылается.

### `find-stale.py`
- Сканирует `claims/*.yml` на `date_verified` старше staleness thresholds.
- Выводит список stale claims с типом и возрастом.

### `dump-state.py`
- Короткий отчёт: total countries, по тирам, средний depth_score, sizes очередей.

Все скрипты — Python 3, читают только vault, никаких внешних зависимостей кроме `pyyaml`.

---

## 19. Migration & versioning

### 19.1. Semver

- `criteria.md` и `vault-protocol.md` имеют semver в frontmatter.
- **major**: breaking schema change (frontmatter перестал быть совместим).
- **minor**: новые поля/секции, обратно совместимо.
- **patch**: clarifications, typo, no schema change.

### 19.2. MIGRATIONS.md

Когда major или minor версия повышается, в `MIGRATIONS.md` добавляется секция:

```markdown
## 2.0.0 → 2.1.0 (vault-protocol.md)

**Changed**: Added new `risk_flags` enum value `political-instability`.

**Migration recipe**:
- Existing countries/*.md frontmatter: no change required.
- For new flagging, use the enum value.

**Backwards compatible**: yes.
```

### 19.3. Schema version в frontmatter

Каждый `countries/*.md` и `runs/*.md` фиксирует `schema_version` своего frontmatter. При чтении Hermes проверяет, и если файл написан в более старой major-версии — может потребоваться migration.

---

## 20. Iteration budget (рекомендация, не жёсткий лимит)

Чтобы итерация была завершённой и не разбухала:

- Время: 30–90 минут чистой работы.
- Tool calls (web fetch, search): не более ~100 за итерацию.
- Объём изменений в файлах: не более 8 файлов изменено за итерацию.
- Если бюджет начинает превышаться — закругляться, оставлять подробное «что осталось» в run-логе.

---

## 21. Language rule (output)

**All content written by Hermes into vault data files MUST be in English.** This applies to:

- `countries/*.md` (full profiles)
- `claims/*.yml` (atomic claims, including `notes`)
- `sources/sources.md` (source entries)
- `decisions/decisions.md` (decision log entries)
- `runs/*.md` (run logs)
- `dimensions/*.md` (cross-country slices)
- `digests/week-*.md` (weekly digests)
- `proposals/proposal-*.md` (self-improvement proposals, all fields and body)
- `INDEX.md` updates
- `CHANGELOG.md` entries
- `IMPROVEMENT_LOG.md` entries
- `verification-queue.md` entries
- `MIGRATIONS.md` entries
- `assumptions.md` updates
- `open-questions.md` updates
- Telegram messages (per §14)

Markers (per `GLOSSARY.md`) use the canonical English form: `[verification required]`, `[single source]`, `[no date, verification required]`, etc. Russian-language aliases exist only for legacy reference and must not appear in new content.

**Why English?** Sources are predominantly English; consistency across files makes cross-referencing and downstream synthesis easier; agent reasoning is more reliable in English on technical/legal content.

**Exceptions** (these documents may remain in their authoring language):
- `criteria.md`, `vault-protocol.md`, `CONTEXT.md`, `GLOSSARY.md` — instructions/contract. Translation is a separate task.

When citing original-language source material (Greek law text, Spanish tax form, etc.), include the original quote with an English translation alongside.

## 22. Hermes-initiated country additions

Hermes may **propose** adding a new country to the research set if, during research, evidence emerges that the country would be a strong fit. Examples that might trigger a proposal:

- A community source mentions a country with an exceptionally clear post-2027 pathway for Ukrainians that isn't in our list.
- A digital-nomad-friendly jurisdiction emerges with strong tax and climate profile that wasn't initially considered.
- A neighbour of an existing Tier 1 candidate shows comparable or better metrics on a specific dimension.

### 22.1. Proposal type

`type: new-country` in the proposal frontmatter (per §13.3).

Body must include:
- **Country name** and **group** (existing group or proposed new group).
- **Tier hint** with justification.
- **Why this country should be added** (specific evidence with sources cited).
- **Estimated fit** on the key criteria (legalization potential, climate, taxes, cost).
- **Risks of adding** (e.g., far from Ukraine, language barrier, political concerns).
- **Estimated cost** of researching it to depth_score 7 (≈ how many iterations).

### 22.2. Approval flow

Same as other proposals (§13.4). Approval threshold: medium severity (requires explicit human approve in Telegram or by editing `status:`).

### 22.3. On approval (applied)

Hermes performs in next iteration:

1. Append country entry to `countries.yml` (with `tier_hint`, `tier: null`, `status: pending`).
2. Append country to `state.json` `countries` block with default fields (depth_score 0, all sections pending).
3. Append country row to `INDEX.md` table.
4. Update `countries.yml` `total` count and group's country list.
5. If the country is in a new group not in `countries.yml`, add the group definition.
6. Update `IMPROVEMENT_LOG.md` and `CHANGELOG.md`.
7. Bump `countries.yml` minor version (1.0.0 → 1.1.0) since the canonical list changed.

### 22.4. Limit

To avoid scope creep:
- Maximum **2 new countries per month** can be applied. Excess pending proposals stay in queue.
- New country additions are reviewed cumulatively in the **weekly digest** if any pending.

## 23. What is **not** done in this document

- Description of research criteria content — that's in `criteria.md`.
- Final synthesis — separate downstream process.
- External integrations (Telegram bot internals, cron config) — at the Hermes-runtime layer, not vault.
