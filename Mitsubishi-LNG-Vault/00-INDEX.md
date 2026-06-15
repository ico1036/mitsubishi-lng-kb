---
title: 미쓰비시 상사 LNG 밸류체인 — 마스터 인덱스
type: index
tags: [index, mitsubishi, LNG, energy]
created: 2026-06-07
research_method: deep-research (24 sources → 83 claims → 25 verified → 23 confirmed → 14 findings)
updated: 2026-06-16
ingest: mitsubishi_v3.xlsx (IR/AFR 재무) + mitsubishi-lng-report-style-OFFLINE-20260602.html (자체 종합 리포트) → +7 findings / +4 sources
audit: 닥터체크(워크플로우 22에이전트, 397원자 vs 44노트) → 15후보 → 8확정/7기각. +3 findings, +온톨로지(33노드·41관계), +데이터레이어(CSV 7종+스킬)
---

# 🗂️ 미쓰비시 상사 LNG 밸류체인 — 마스터 인덱스

> 워런 버핏(버크셔)이 일본 5대 종합상사 바스켓을 *very long term·many decades* 보유하겠다고 밝힌 미쓰비시 상사의 50년 LNG 밸류체인 구축 사례와 한국 에너지 산업 함의. ("미쓰비시만 영원히 보유"는 부정확 → [[F-버핏-very-long-term-many-decades]])
> deep-research 하베스트(3표 적대검증) 결과를 클러스터별로 정리한 볼트.

## 🧭 클러스터 (Maps of Content)
이 6개 허브가 그래프 뷰의 클러스터 중심입니다. 각 발견 노트는 자신의 허브로 링크됩니다.

- [[MOC-1-밸류체인-구축]] — 🏗️ 50년 단계적 구축, 타임라인·지분 (Q1)
- [[MOC-2-버핏-버크셔-투자]] — 💰 버크셔 지분·*very long term* (Q2) 🟢 추가자료로 부분 해소
- [[MOC-3-종합상사-모델]] — ⚙️ 수직통합 수익구조 (Q3)
- [[MOC-4-한국-함의]] — 🇰🇷 SK E&S·포스코인터·KOGAS 벤치마킹 (Q4)
- [[MOC-5-지정학-호르무즈]] — 🌍 이란 전쟁·호르무즈 disruption (Q5)
- [[MOC-6-미해결질문-supersearch]] — ❓ 공백 + supersearch 추격 후보

## 📌 전체 발견 노트 (24)
> 🆕 = 2026-06-16 추가 자료(xlsx IR/AFR · HTML 리포트)에서 통합. ✅ = 닥터체크 감사로 보강. 적대검증 미실시분은 노트 내 명시.

### 🏗️ 밸류체인 구축
- [[F-알래스카-1969-수입대행-시작]]
- [[F-13개-프로젝트-14_9MTPA]]
- [[F-상류-액화-지분]]
- [[F-Cameron-LNG-상업운전-톨링]]
- [[F-LNG-Canada-FID-첫선적]]
- [[F-Malaysia-PETRONAS-46년]] 🆕
- [[F-Donggi-Senoro-KOGAS공동투자]] 🆕
- [[F-경로선택권-option-value-thesis]] ✅
### ⚙️ 종합상사 모델
- [[F-Corporate-Strategy-2027-DGI-KOGAS]]
- [[F-Aethon-인수-중동피벗]]
- [[F-연결순이익-LNG베타]] 🆕
- [[F-EE세그먼트-지분법이익]] 🆕
### 💰 버핏 / 버크셔
- [[F-버핏-very-long-term-many-decades]] 🆕
### 🇰🇷 한국 함의
- [[F-SK-ES-수직통합]]
- [[F-포스코인터-알래스카LNG]]
- [[F-한국석유공사-90만배럴-사건]] 🆕
- [[F-한국판-에너지상사-모델-함께움직이기]] ✅
### 🌍 지정학·호르무즈
- [[F-일본-수입의존-호르무즈-원유]]
- [[F-일본-LNG-다변화-29to11]]
- [[F-호르무즈-chokepoint-35-20]]
- [[F-Fordow-폭격-유가급등]]
- [[F-IEEFA-다변화-한계-JKM]]
- [[F-호르무즈-EIA-KIET-한국원가]] 🆕
- [[F-다중병목-말라카-파나마-한국노출]] ✅

## 🧬 온톨로지 & 📦 데이터 레이어
- [[ONTOLOGY-관계지도]] — 33노드·41관계 지식그래프 (HTML 임베디드 그래프 추출 + 감사 보강). 첫 병합에서 통째로 누락됐던 구조.
- **숫자 데이터(`_data/*.csv`)**: `financials_net_income`(순이익 시계열) · `ee_segment` · `lng_shale_assets_fy2025` · `key_metrics`(53행) · `ontology_nodes`/`ontology_edges` · `sources`(34개 소스 원장).
- **조회 스킬**: `python3 .claude/skills/mitsubishi-data/query.py {list|finance|search <term>|show <ds>|graph|sources}` — **의존성 없음(python3만 필요, 설치 불필요)**. 도구가 없거나 안 되면 `_data/*.csv`를 직접 읽으면 됨. → [[#🛠 데이터 조회]]
- **원본 텍스트(`_raw-sources/`)**: HTML 리포트·전략노트·온톨로지 JSON·xlsx 덤프 (Obsidian 전문검색용) + `_raw-deep-research-result.json`.

## 📚 소스 노트 (16, 검증 통과 인용 + 추가 자료)
### 🆕 추가 자료 (2026-06-16)
- [[S-AFR2025-재무제표]] ⭐primary (xlsx)
- [[S-미쓰비시-Flash-Report]] ⭐primary (xlsx)
- [[S-Berkshire-Annual-Reports]] ⭐primary (HTML)
- [[S-LNG-밸류체인-리포트-HTML]] (secondary, 자체 종합)
### 기존 (deep-research 검증)
- [[S-JOGMEC-저널-300799935]] ⭐primary
- [[S-JOGMEC-oilgas-2025-mitsubishi]] ⭐primary
- [[S-미쓰비시-천연가스그룹-US]] ⭐primary
- [[S-미쓰비시-Montney-프로젝트]] ⭐primary
- [[S-미쓰비시-Corporate-Strategy-2027]] ⭐primary
- [[S-미쓰비시-Aethon-인수-릴리스]] ⭐primary
- [[S-ORF-Middle-East]] ⭐primary
- [[S-SK-ES-LNG]] ⭐primary
- [[S-포스코인터-매거진-8620]] ⭐primary
- [[S-CSIS-Iran-Japan]] ⭐primary
- [[S-Washington-Institute-Gulf]] ⭐primary
- [[S-IEEFA-다변화-한계]] ⭐primary

## ❌ 반증되어 제외된 주장
- "미쓰비시가 Cameron 시설을 *운영*한다" → 실제는 지분/톨링 (0-3 기각)
- "일본 원유 95%+·페르시아만 LNG 83% 호르무즈 통과" → 표결 분열 (1-2 기각)

## 🛠 데이터 조회
의존성 없음(python3만 필요). 어느 폴더에서 실행해도 데이터 경로 자동 탐지 — `cd` 불필요.
```bash
python3 .claude/skills/mitsubishi-data/query.py finance          # 순이익 시계열 + LNG 베타(6.8배)
python3 .claude/skills/mitsubishi-data/query.py search 호르무즈    # CSV+노트 전체 검색 (35% vs 21% 두 값 확인)
python3 .claude/skills/mitsubishi-data/query.py graph --entity donggi
python3 .claude/skills/mitsubishi-data/query.py sources --quality primary
```
또는 Claude Code에서 `mitsubishi-data` 스킬 호출. 도구가 안 되면 `_data/*.csv`를 직접 읽으면 동일하게 활용 가능.

## 🏷️ 태그로 찾기
`#cluster/밸류체인` `#cluster/버핏` `#cluster/상사모델` `#cluster/한국` `#cluster/지정학`
`#confidence/high` `#confidence/unverified` `#type/finding` `#type/source` `#open-question` `#ontology` `#data`
