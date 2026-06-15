---
title: 온톨로지 관계지도 — 미쓰비시 LNG 밸류체인 (33노드·41관계)
type: reference
tags: [ontology, reference, data]
created: 2026-06-16
provenance: mitsubishi-lng-report-style-OFFLINE-20260602.html (임베디드 그래프) + 감사 보강(MidOcean·KOREA LNG·Sulawesi)
data: _data/ontology_nodes.csv · _data/ontology_edges.csv
---

# 🧬 온톨로지 관계지도

> 오프라인 HTML 리포트에 임베드돼 있던 **지식그래프**(원본 30노드·35관계, 전 관계에 evidence URL 포함)를 추출해 볼트 데이터로 편입하고, 감사에서 확인된 누락 엔티티 3개를 보강한 **33노드·41관계** 버전.
> 원본 30→35는 [[S-LNG-밸류체인-리포트-HTML]]에서 추출. 정형 데이터는 `_data/ontology_nodes.csv` / `_data/ontology_edges.csv`에 있고, `mitsubishi-data` 스킬로 조회한다.

## 📊 그래프 통계 (현재)
- **노드 33** · **관계 41** · 국가 12
- 노드 유형: company 25 · other 5 · government 2 · investor 1
- 관계 유형: investment 14 · supply_chain 8 · subsidiary 7 · partnership 4 · customer 3 · membership 3 · acquisition 1 · government_funding 1
- 관계 신뢰도: high 32 · medium 7 · low 2

## 🔝 허브(연결도 상위)
| 엔티티 | 유형 | 국가 | degree |
|---|---|---|---|
| Mitsubishi Corporation | company | Japan | 14 |
| Donggi-Senoro LNG | company | Indonesia | 5 |
| MC Energies / Brunei LNG / Korean Manufacturing Base | company/other | US/Brunei/Korea | 4 |
| Diamond Gas International / LNG Canada / Aethon | company | SG/CA/US | 3 |

## ➕ 감사 보강 노드 (2026-06-16)
원본 그래프에 없어 추가한 엔티티 (관련 발견 노트 텍스트엔 있었으나 그래프에서 누락):
- **MidOcean Energy** — 미쓰비시 2024.4 전략투자, 간접 6개 LNG 프로젝트 추가 → [[F-13개-프로젝트-14_9MTPA]]
- **KOREA LNG** — KOGAS의 Oman LNG 5.0% 참여 vehicle
- **Sulawesi LNG Development** — MC 75 / KOGAS 25 지주회사, Donggi-Senoro의 모체 → [[F-Donggi-Senoro-KOGAS공동투자]]

## 🔗 노드 ↔ 발견 노트 매핑(주요)
- Mitsubishi Corporation → [[MOC-1-밸류체인-구축]] · [[MOC-3-종합상사-모델]]
- LNG Canada → [[F-LNG-Canada-FID-첫선적]] · Cameron LNG → [[F-Cameron-LNG-상업운전-톨링]]
- Aethon/Haynesville → [[F-Aethon-인수-중동피벗]] · Montney → [[F-EE세그먼트-지분법이익]]
- PETRONAS/MLNG → [[F-Malaysia-PETRONAS-46년]] · Brunei LNG → [[F-상류-액화-지분]]
- Donggi-Senoro / KOGAS → [[F-Donggi-Senoro-KOGAS공동투자]]
- Berkshire 5대상사 바스켓 → [[F-버핏-very-long-term-many-decades]]
- Strait of Hormuz / Korean Manufacturing → [[F-호르무즈-EIA-KIET-한국원가]]
- Diamond Gas International (Singapore) → [[F-Corporate-Strategy-2027-DGI-KOGAS]]

## 🛠 조회 방법
```bash
python3 .claude/skills/mitsubishi-data/query.py graph                       # 개요(허브·관계분포)
python3 .claude/skills/mitsubishi-data/query.py graph --entity donggi       # 특정 엔티티+연결관계
python3 .claude/skills/mitsubishi-data/query.py show ontology_edges --where confidence=low
```

← [[00-INDEX]] · 데이터 레이어 → [[00-INDEX#📦 데이터 레이어]]
