---
name: mitsubishi-data
description: Query the Mitsubishi LNG value-chain knowledge base (financials, EE segment, LNG/shale assets, key metrics, ontology graph, source ledger) plus the markdown research notes. Use for any question about Mitsubishi/8058.T net income & LNG beta, EE segment equity income, LNG asset breakdown, Hormuz/Aethon/Berkshire/Bintulu/LNG-Canada/KOGAS numbers, the ontology entities/relations, or which sources back a claim.
---

# Mitsubishi LNG 리서치 데이터 조회

미쓰비시상사 LNG 밸류체인 지식베이스의 **정량 데이터(CSV) + 정성 노트(.md)**를 하나의 도구로 조회한다.
**의존성 없음** — `python3`만 있으면 동작한다(pandas/설치 불필요). 코드를 모르는 사용자가 Claude에게 질문하면 Claude가 이 도구를 대신 실행한다.

## 도구
`python3 .claude/skills/mitsubishi-data/query.py <명령>` (경로는 어디서 실행해도 자동 탐지)

| 명령 | 설명 |
|---|---|
| `finance` | 연결순이익 FY2016–FY2025 + LNG 베타(6.8배) 요약 |
| `search "<검색어>"` | **CSV 데이터 + 모든 노트(.md)** 동시 검색 (one-stop) |
| `list` | 데이터셋 목록 |
| `show <ds> [--where 컬럼=값]` | 데이터셋 출력/필터 |
| `graph [--entity <키>]` | 온톨로지 33노드·41관계 |
| `sources [--quality primary]` | 소스 원장 34개 |

## 데이터셋 (`Mitsubishi-LNG-Vault/_data/`)
`financials_net_income` · `ee_segment` · `lng_shale_assets_fy2025` · `key_metrics`(53행) · `ontology_nodes`(33) · `ontology_edges`(41) · `sources`(34)

## 도구 없이도 가능
모든 데이터는 평문 CSV/Markdown이다. python3가 없거나 막히면 **그냥 파일을 읽어라**: `Mitsubishi-LNG-Vault/00-INDEX.md`(목차) → `_data/*.csv`(숫자) → `S/ F/ MOC/*.md`(분석).

## 데이터 품질 주의
- `confidence` 컬럼을 확인. `low`(NWS 16.67%·사할린 10%·2030s 18Mtpa·석유공사 90만배럴)는 1차 미확인 — 인용 전 검증.
- 호르무즈 원유 비중은 **두 값 공존**: vault/Reuters ~35% vs EIA ~21% (`key_metrics`에 둘 다, 출처 명시해 인용).
- 재무 FY2016–2018은 ±5% 역산, FY2019–2025는 공식 확인. EE 세그먼트 컬럼은 회계연도 종료월(FYE) 기준.
- 동의어 주의: `버핏`↔`버크셔`, `Aethon`↔`헤인스빌`, `DGI`↔`Diamond Gas International`.
