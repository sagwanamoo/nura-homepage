# NURA 홈페이지

전국대학교로켓연합회(NURA) 공식 홈페이지입니다.

정적 HTML/CSS/JavaScript 기반으로 구성되어 있으며, 반복적으로 바뀌는 콘텐츠는 주로 `data/site-data.js`에서 관리합니다. 헤더, 푸터, 데스크톱/모바일 네비게이션은 `data/shared-layout.js`에서 공통으로 렌더링합니다.

## 📁 프로젝트 구조

```
nura-homepage/
├── index.html                    # 메인 페이지
├── README.md                     # 이 문서
├── image_postprocessing.py       # 개요 이미지 블러 처리 스크립트
├── about/
│   └── index.html                # About / 연혁 페이지
├── activities/
│   ├── index.html                # Activities 목록 페이지
│   ├── meeting/
│   │   └── index.html            # 대표자 회의
│   ├── kspe/
│   │   └── index.html            # 춘추계 학술대회
│   ├── conference/
│   │   └── index.html            # 학술대회
│   └── launch/
│       ├── index.html            # 발사대회
│       └── apply/
│           └── index.html        # 발사대회 신청 페이지
├── members/
│   ├── university/
│   │   └── index.html            # 회원대학 지도/목록/로고 페이지
│   └── leadership/
│       └── index.html            # 역대회장단 페이지
├── resources/
│   └── index.html                # 자료실 페이지
├── partnership/
│   └── index.html                # 후원/협력 페이지
├── privacy/
│   └── index.html                # 개인정보처리방침
├── sitemap/
│   └── index.html                # 사이트맵
├── data/
│   ├── shared-layout.js          # 공통 헤더, 네비게이션, 푸터
│   └── site-data.js              # 공통 콘텐츠 데이터
├── source/
│   ├── overview/blurred/         # 메인 개요 슬라이드용 블러 이미지
│   ├── resources/                # 로고, 파비콘, 규정집, 제안서, 활동 이미지
│   ├── partnership/              # 후원사/협력기관 로고
│   ├── members/
│   │   ├── south-korea.svg       # 회원대학 지도 SVG
│   │   └── used-logos/           # 회원대학 로고
│   └── news/                     # 메인 뉴스 이미지
├── robots.txt
├── sitemap.xml
└── naver489cbd41cbce3895ff5c2fbf7e61e54c.html
```

## 🚀 시작하기

### 기본 실행

정적 사이트이므로 프로젝트 루트에서 간단한 로컬 서버를 띄우면 됩니다.

```bash
python -m http.server 8000
```

macOS/Linux에서 `python` 명령이 없으면 아래처럼 실행합니다.

```bash
python3 -m http.server 8000
```

이후 브라우저에서 아래 주소를 열면 됩니다.

```text
http://localhost:8000
```

### 그냥 HTML 파일을 직접 열어도 되나요?

가능한 경우도 있지만, 상대 경로·링크·이미지·공통 JS 로딩을 안정적으로 확인하려면 **로컬 서버 방식**을 권장합니다.

### 개발 환경 설정 (선택사항)

이미지 후처리 스크립트를 사용할 때만 Python 이미지 라이브러리가 필요합니다.

```bash
# Python 가상환경 활성화
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux

# 필요한 패키지 설치
pip install Pillow
```

---

## 📁 핵심 파일 설명

### `data/shared-layout.js`

공통 레이아웃 파일입니다.

다음 요소를 담당합니다.

- 상단 헤더 렌더링
- 데스크톱/모바일 네비게이션
- Activities 드롭다운 메뉴
- Members 드롭다운 메뉴
- 모바일 메뉴 열림/닫힘 및 스크롤 잠금
- 공통 푸터 렌더링
- 현재 페이지 강조 표시

각 HTML 파일의 `body`에는 아래 속성이 들어가 있어야 공통 네비게이션이 올바르게 동작합니다.

```html
<body data-current-page="home" data-base-path=".">
```

하위 폴더 페이지에서는 보통 아래처럼 설정합니다.

```html
<body data-current-page="about" data-base-path="..">
```

두 단계 아래 페이지에서는 아래처럼 설정합니다.

```html
<body data-current-page="members" data-base-path="../..">
```

`data-current-page`는 현재 메뉴 강조에 사용되고, `data-base-path`는 공통 헤더/푸터 안의 링크와 로고 이미지 경로를 계산하는 데 사용됩니다.

### `data/site-data.js`

반복적으로 렌더링되는 데이터 모음입니다. 파일 안의 `window.NURA_DATA` 객체를 각 페이지가 읽어서 화면을 구성합니다.

현재 관리 항목:

- `overviewStats` : 메인 페이지 통계 카드
- `newsItems` : 메인 페이지 관련 기사 카드
- `resourceDocuments` : 자료실 문서 목록
- `historyData` : About 페이지 연혁 목록
- `memberOrganizations` : 회원 대학/동아리 목록
- `memberRegions` : 회원 대학 세부 권역 정의
- `presidentsData` : 역대회장단 목록
- `conferenceAwards` : 학술대회 역대 시상 목록
- `launchAwards` : 발사대회 역대 시상 목록

숫자, 뉴스, 자료실, 연혁, 회원대학, 역대회장단, 역대 시상처럼 반복 렌더링되는 항목은 HTML 본문을 직접 수정하기 전에 이 파일을 먼저 확인하는 것이 좋습니다.

### 각 페이지의 HTML 파일

페이지별 본문 구조와 페이지 전용 스타일은 각 HTML 파일 안에 직접 작성되어 있습니다.

- `index.html` : 메인 비주얼, 단체 소개, 뉴스, 통계, 파트너 섹션
- `about/index.html` : About 설명과 연혁 렌더링
- `activities/index.html` : 활동 카드 목록
- `activities/meeting/index.html` : 대표자 회의
- `activities/kspe/index.html` : 춘추계 학술대회
- `activities/conference/index.html` : 학술대회 상세 및 역대 시상
- `activities/launch/index.html` : 발사대회 상세 및 역대 시상
- `activities/launch/apply/index.html` : 발사대회 신청 안내
- `members/university/index.html` : 지도 기반 권역별 회원 대학 소개 및 로고 월
- `members/leadership/index.html` : 역대회장단 목록
- `resources/index.html` : 자료 목록 렌더링 화면
- `partnership/index.html` : 협력 개요, 후원 안내, 계좌 안내, 문의 CTA
- `privacy/index.html` : 개인정보처리방침
- `sitemap/index.html` : 사이트맵

---

## 🎨 디자인 커스터마이징

### 색상 변경

Tailwind CSS 클래스를 사용하여 색상을 변경할 수 있습니다.

- 메인 색상: `text-blue-400`, `bg-blue-600`
- 배경색: `bg-black`, `bg-gray-900`
- 텍스트 색상: `text-white`, `text-gray-300`

### 커스터마이징

이 프로젝트는 Tailwind CDN 기반이지만, 실제로는 다음 두 방식이 함께 사용됩니다.

- HTML 내 Tailwind 유틸리티 클래스
- 각 페이지 내부 `<style>` 블록의 커스텀 CSS

따라서 디자인 수정 시 아래 순서로 확인하는 것이 좋습니다.

1. HTML 클래스 값 확인
2. 페이지 내부 `<style>` 확인
3. 공통 요소면 `data/shared-layout.js` 확인

특히 아래 항목은 페이지마다 직접 스타일이 들어가 있습니다.

- 히어로 영역 높이/여백
- 타임라인 카드
- 활동 카드
- 드롭다운 메뉴
- 모바일 메뉴
- 회원 대학 지도/로고 영역
- 후원 안내 카드와 계좌 팝오버

---

## 🛠️ 유지보수 가이드

### 먼저 확인할 파일

수정하려는 내용에 따라 아래 순서로 확인하면 빠릅니다.

1. 반복 데이터인지 확인: `data/site-data.js`
2. 공통 헤더/푸터/메뉴인지 확인: `data/shared-layout.js`
3. 특정 페이지 본문이나 스타일인지 확인: 해당 `index.html`
4. 이미지, PDF, 로고 파일인지 확인: `source/` 하위 폴더

### 메인 페이지 숫자 카드 수정

`index.html`은 `data/site-data.js`의 `overviewStats` 배열을 읽어서 통계 카드를 생성합니다.

```javascript
overviewStats: [
  {
    basis: "2026년 5월 기준",
    label: "참여 대학",
    value: 38,
    unit: "개교"
  }
]
```

회원 대학 수를 바꾸는 경우 `memberOrganizations`의 실제 항목 수와도 함께 맞는지 확인합니다.

### 메인 페이지 기사 카드 수정

`index.html`은 `data/site-data.js`의 `newsItems` 배열을 읽어서 뉴스 슬라이드를 생성합니다.

```javascript
newsItems: [
  {
    date: "2024.07.08",
    title: "기사 제목",
    summary: "기사 요약",
    image: "source/news/news1.jpg",
    href: "https://..."
  }
]
```

뉴스 이미지는 `source/news/`에 추가하고, `image`에는 메인 페이지 기준 경로를 넣습니다.

### 자료실 목록 수정

`resources/index.html`은 `data/site-data.js`의 `resourceDocuments` 배열을 읽어서 목록을 생성합니다.

```javascript
resourceDocuments: [
  {
    date: "2026.04",
    title: "2026 전국대학교로켓학술대회 규정",
    category: "Conference",
    format: "pdf",
    size: "491KB",
    description: "2026 전국대학교로켓학술대회 규정입니다.",
    href: "../source/resources/2026 전국대학교로켓학술대회 규정_260402.pdf"
  }
]
```

새 자료를 추가할 때는 보통 아래를 함께 처리합니다.

1. 파일을 `source/resources/`에 추가
2. `resourceDocuments`에 항목 추가
3. `href` 경로가 `resources/index.html` 기준으로 맞는지 확인
4. 실제 파일명이 한글이면 배포 환경에서 다운로드가 정상 동작하는지 확인

업로드 예정 상태로 표시하고 싶다면:

```javascript
{
  title: "활동 브로슈어",
  category: "Brochure",
  format: "PDF",
  status: "coming-soon"
}
```

### 연혁 목록 수정

`about/index.html`은 `data/site-data.js`의 `historyData` 배열을 읽어서 연혁 목록을 생성합니다.

```javascript
historyData: [
  {
    year: 1992,
    featured: true,
    items: ["제1회 로켓발사대회(한국항공대학교)"]
  }
]
```

`items`는 같은 연도에 여러 문장을 넣을 수 있는 배열입니다. 중요한 연도는 `featured: true`로 표시할 수 있습니다.

### 회원 대학 데이터 수정

회원대학 페이지는 `members/university/index.html`입니다. 기본 목록은 `data/site-data.js`의 `memberOrganizations`와 `memberRegions`를 읽어서 생성합니다.

예시:

```javascript
memberOrganizations: [
  {
    name: "전북대학교",
    region: "jeonbuk",
    clubName: "JURG",
    description: "전북특별자치도 전주시 덕진구 백제대로 567",
    website: "https://www.jbnu.ac.kr/",
    instagramHandle: "@jbnu_ohcket",
    primaryLink: "instagram"
  }
]
```

`region` 값은 `memberRegions`의 `id`와 일치해야 합니다.

회원 대학을 추가/수정할 때는 보통 아래 항목을 함께 확인합니다.

1. `data/site-data.js`의 `memberOrganizations`에 학교 데이터 추가
2. `name`, `region`, `clubName`, `description` 입력
3. 학교 공식 홈페이지가 있으면 `website` 입력
4. 인스타그램이 있으면 `instagramHandle` 입력
5. 기본으로 열릴 링크를 정하고 싶으면 `primaryLink: "website"` 또는 `primaryLink: "instagram"` 지정
6. 신규 학교라면 참여 대학 수(`overviewStats`의 `참여 대학`)도 실제 수와 맞게 수정
7. 로고를 노출하려면 `source/members/used-logos/`에 파일을 넣고, `members/university/index.html`의 `memberLogoPathByName`에 학교명과 파일 경로를 연결
8. 특정 로고만 크기 보정이 필요하면 `members/university/index.html`의 `logoImageClassByName`에 전용 클래스를 연결하고, 같은 파일의 CSS에 스타일 추가

회원 대학 카드와 로고 월의 외부 링크는 기본적으로 아래 순서로 사용됩니다.

1. `primaryLink`에 지정된 링크
2. `instagramHandle`
3. `website`

단, 카드 목록에서 사용하는 링크와 로고 월에서 사용하는 링크가 페이지 내부 스크립트에서 각각 처리되므로, 새 링크 정책을 넣을 때는 `members/university/index.html`의 `getPrimaryLink` 주변 로직도 같이 확인합니다.

`description`에는 보통 학교 주소를 넣습니다. 가능하면 학교 공식 홈페이지의 표기를 기준으로 맞춥니다.

로고 이미지는 `members/university/index.html`의 `memberLogoPathByName` 객체에서 학교명과 파일 경로를 연결합니다.

```javascript
const memberLogoPathByName = {
  '서울시립대학교': '../../source/members/used-logos/서울시립대.png'
};
```

로고 비율이나 여백이 어색한 학교는 전용 클래스를 하나 더 연결할 수 있습니다.

```javascript
const logoImageClassByName = {
  '서울시립대학교': 'members-logo-item__image--uos'
};
```

권역 정의는 `memberRegions`에서 관리합니다.

```javascript
memberRegions: [
  {
    id: "jeonbuk",
    name: "전북",
    coverage: "전북특별자치도",
    description: "전북 지역에 속한 회원 대학과 로켓 동아리 현황입니다."
  }
]
```

새 권역을 추가하는 경우 `members/university/index.html`의 `provinceGroupsByRegion`과 `macroRegions`도 함께 확인해야 지도와 아코디언이 맞게 동작합니다.

### 역대 회장단 수정

역대회장단 페이지는 `members/leadership/index.html`입니다. 이 페이지는 `data/site-data.js`의 `presidentsData` 배열을 읽고, `generation` 기준 최신순으로 정렬해서 출력합니다.

```javascript
presidentsData: [
  {
    generation: 35,
    name: "이창현",
    university: "광주과학기술원",
    term: "2026",
    vicePresident: "한재경(동국대학교)",
    secretary: "윤원빈(건국대학교)"
  }
]
```

- `generation`: 대수입니다. 화면에 `제N대`로 출력됩니다.
- `name`: 회장 이름입니다.
- `university`: 회장 소속 대학입니다.
- `term`: 임기 연도입니다.
- `vicePresident`: 부회장 정보입니다. 없으면 표시되지 않습니다.
- `secretary`: 총무/스태프 정보입니다. 없으면 표시되지 않습니다.

역대회장단과 연혁 문구가 함께 바뀌는 경우 `historyData`도 같이 확인합니다.

### 학술대회 / 발사대회 역대 시상 수정

학술대회 페이지는 `conferenceAwards`, 발사대회 페이지는 `launchAwards`를 사용합니다. 두 배열 모두 `data/site-data.js`에 있고, 같은 포맷을 사용합니다.

```javascript
conferenceAwards: [
  {
    year: 2025,
    rank: "대상",
    university: "서울대학교",
    team: "SNURocket"
  }
]
```

- `year`: 개최 연도입니다. 화면에서는 연도 기준으로 그룹화되고 최신순으로 출력됩니다.
- `rank`: 수상 훈격입니다.
- `university`: 수상 대학교입니다.
- `team`: 수상 팀명입니다. 선택사항이며, 있으면 대학교와 함께 표시됩니다.

데이터를 넣었는데 화면에 "데이터가 준비 중입니다."가 보이면 먼저 `data/site-data.js`가 실제로 최신 버전으로 로드되는지 확인합니다.

### 공통 네비게이션 수정

상단 메뉴, Activities 드롭다운, Members 드롭다운, 모바일 메뉴, 푸터는 `data/shared-layout.js`에서 수정합니다.

수정 가능 항목 예시:

- 메뉴 이름
- 드롭다운 항목
- 링크 경로
- 모바일 메뉴 구조
- 현재 페이지 강조 기준
- 상단바 스타일
- 푸터 연락처/단체 정보/사이트 링크

새 페이지를 추가할 때는 보통 아래를 함께 확인합니다.

1. 새 `index.html` 생성
2. `<body data-current-page="..." data-base-path="...">` 값 지정
3. 필요하면 `data/shared-layout.js`의 데스크톱/모바일 메뉴에 링크 추가
4. `sitemap/index.html`과 `sitemap.xml` 갱신
5. 새 페이지에서 필요한 공통 JS의 상대 경로 확인

### 활동 페이지 수정

활동 소개 페이지는 파일별로 직접 수정합니다.

- `activities/index.html` : Activities 목록 화면
- `activities/meeting/index.html` : 대표자 회의
- `activities/kspe/index.html` : 춘추계 학술대회
- `activities/conference/index.html` : 전국대학교로켓학술대회
- `activities/launch/index.html` : 전국대학교로켓발사대회
- `activities/launch/apply/index.html` : 발사대회 신청 안내

활동 상세 페이지의 대표 이미지는 주로 `source/resources/meeting.jpg`, `kspe.jpg`, `conference.jpg`, `launch.jpg`를 사용합니다.

### 새로운 후원사 추가

1. 로고 이미지를 `source/partnership/` 폴더에 추가
2. `index.html`의 파트너 로고 영역에 이미지와 링크 추가
3. 필요하면 `partnership/index.html`의 협력기관/후원 안내 영역도 함께 수정
4. 로고 비율이 어색하면 이미지 자체를 정리하거나 해당 페이지의 스타일을 보정

현재 사용 중인 후원사/협력기관 로고 파일 예시:

- `source/partnership/koreanair.svg`
- `source/partnership/innospace.svg`
- `source/partnership/kari.svg`
- `source/partnership/kasa.png`
- `source/partnership/ligpoongsan.webp`
- `source/partnership/ligpoongsan-transparent.png`
- `source/partnership/pdk.png`

### 후원 안내 수정

후원 방식, 후원 효과, 계좌 안내는 `partnership/index.html`에서 직접 수정합니다.

계좌 정보는 후원 안내 문장 안의 계좌 팝오버와 하단 CTA 영역에 들어가 있으므로, 변경 시 두 위치를 함께 확인하는 것이 좋습니다.

### 캐시 때문에 수정 내용이 바로 안 보일 때

이 사이트는 정적 파일을 직접 서빙하므로 브라우저가 오래된 JS 파일을 캐시할 수 있습니다.

특히 아래 파일을 수정했는데 배포 후에도 이전 데이터가 보이면 캐시를 의심합니다.

- `data/site-data.js`
- `data/shared-layout.js`

현재 각 HTML은 아래처럼 쿼리 문자열 버전을 붙여 공통 JS를 불러옵니다.

```html
<script src="../data/site-data.js?v=20260530-1"></script>
<script src="../data/shared-layout.js?v=20260530-2" defer></script>
```

두 단계 아래 페이지에서는 경로가 아래처럼 달라집니다.

```html
<script src="../../data/site-data.js?v=20260530-1"></script>
<script src="../../data/shared-layout.js?v=20260530-2" defer></script>
```

브라우저는 `site-data.js`와 `site-data.js?v=20260530-1`을 서로 다른 파일로 인식하므로, 버전 값을 바꾸면 새 파일을 다시 받아옵니다.

공통 데이터나 공통 레이아웃 JS를 수정해 배포할 때는:

1. 관련 HTML 파일들의 `?v=...` 값을 같은 새 버전으로 올립니다.
2. 날짜 기반 값(`YYYYMMDD`)을 쓰면 추적하기 쉽습니다.
3. `site-data.js`와 `shared-layout.js`를 모두 바꿨다면 두 버전을 모두 올립니다.
4. HTML 자체가 이미 캐시된 탭에서는 첫 한 번 새로고침이 필요할 수 있습니다.

현재 버전 문자열은 여러 HTML 파일에 직접 들어가 있으므로, 바꿀 때는 프로젝트 전체에서 검색해 한 번에 맞춥니다.

```bash
rg "site-data\.js\?v=|shared-layout\.js\?v="
```

### 파비콘 재생성

로고가 변경된 경우:

```bash
# Python 스크립트로 파비콘 생성
python -c "
from PIL import Image
img = Image.open('source/resources/nura-icon.png')
size = max(img.size)
favicon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
x_offset = (size - img.size[0]) // 2
y_offset = (size - img.size[1]) // 2
favicon.paste(img, (x_offset, y_offset))
favicon.resize((32, 32)).save('source/resources/favicon-32x32.png')
favicon.resize((16, 16)).save('source/resources/favicon-16x16.png')
"
```

### SEO 정보 수정

각 HTML 파일의 `<head>`에는 기본 SEO 정보가 들어가 있습니다.

수정 대상 예시:

- `<title>`
- `<meta name="description">`
- `og:title`
- `og:description`
- `og:image`
- 파비콘 및 터치 아이콘 링크

네이버 사이트 인증 파일은 `naver489cbd41cbce3895ff5c2fbf7e61e54c.html`입니다. 인증 파일명은 검색 콘솔에서 발급된 값과 일치해야 합니다.

### 이미지 블러 처리

개요 슬라이드용 이미지를 블러 처리하려면:

```bash
python image_postprocessing.py
```

스크립트는 `source/overview/` 루트에 있는 원본 이미지들을 블러 처리하여 `source/overview/blurred/` 폴더에 `slide1.webp`, `slide2.webp` 형식으로 저장합니다. 현재 저장소에는 주로 결과물인 `source/overview/blurred/` 이미지가 들어 있으므로, 새로 생성하려면 원본 이미지를 `source/overview/` 루트에 먼저 넣습니다.

---

## ✅ 변경 후 확인 절차

수정 후에는 로컬 서버를 띄우고 주요 페이지를 직접 확인합니다.

```bash
python -m http.server 8000
```

`python` 명령이 없으면 `python3 -m http.server 8000`을 사용합니다.

브라우저에서 아래 페이지를 확인합니다.

- `http://localhost:8000/`
- `http://localhost:8000/about/`
- `http://localhost:8000/activities/meeting/`
- `http://localhost:8000/activities/conference/`
- `http://localhost:8000/activities/launch/`
- `http://localhost:8000/members/university/`
- `http://localhost:8000/members/leadership/`
- `http://localhost:8000/resources/`
- `http://localhost:8000/partnership/`

확인할 항목:

1. 데스크톱 헤더 메뉴와 드롭다운이 정상 동작하는지 확인
2. 모바일 메뉴의 Activities/Members 하위 메뉴가 열리고 닫히는지 확인
3. `data/site-data.js`에서 수정한 데이터가 화면에 반영되는지 확인
4. 이미지, 회원대학 로고, 지도 SVG가 깨지지 않는지 확인
5. 자료실 문서 링크와 외부 링크가 정상 이동하는지 확인
6. 콘솔에 공통 JS 로딩 오류나 경로 오류가 없는지 확인

---

## ⚠️ 주의사항

1. **이미지 최적화**: 웹용으로 이미지를 압축하여 로딩 속도를 개선하세요.
2. **파일명**: 새 이미지 파일명은 가능하면 영문으로 작성하세요.
3. **상대 경로**: 페이지 깊이에 따라 `../` 개수가 달라지므로 새 파일 추가 시 로컬 서버에서 확인하세요.
4. **자료 링크**: `resourceDocuments`에 `href`를 추가한 경우 실제 파일이 있는지 함께 확인하세요.
5. **캐시 버전**: `data/site-data.js`나 `data/shared-layout.js`를 수정했다면 HTML의 `?v=...` 값도 같이 올리세요.
6. **모바일 확인**: 헤더, 모바일 메뉴, 회원 지도, 후원 안내는 모바일에서 반드시 다시 확인하세요.

## 🔄 배포

### 자동 배포

- **클라우드플레어 스토리지** 기반으로 호스팅됩니다.
- Git 저장소에 푸시하면 자동으로 배포됩니다.
- 별도의 배포 설정이 필요하지 않습니다.

### 배포 과정

1. 로컬에서 변경사항을 Git에 커밋
2. `git push` 명령으로 원격 저장소에 푸시
3. 자동으로 클라우드플레어 스토리지에 반영
4. 웹사이트가 업데이트되었는지 실제 URL에서 확인
5. 공통 JS를 바꾼 경우 캐시 버전이 반영되었는지 확인

---

**마지막 업데이트**: 2026년 06월
- **현재 관리자**: 심승기(shimseunggi@naver.com)
- **기여자**: 전현우(jhw030520@gmail.com), 심승기(shimseunggi@naver.com)
