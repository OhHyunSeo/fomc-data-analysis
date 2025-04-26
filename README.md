<h1 align="center">📈 FOMC Data Analysis</h1>
<p align="center">
  <b>FOMC 회의 일정이 금융시장에 미치는 영향을 시계열 데이터로 분석하는 프로젝트</b><br>
  Python · 데이터 수집 · 시각화 · 금융시장 분석
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Dataframe-informational?logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-Graph-orange?logo=plotly&logoColor=white">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/YFinance-API-success?logo=yahoo&logoColor=white">
</p>

---

## 📝 프로젝트 소개

FOMC(연방공개시장위원회) 회의 일정이 금융시장에 미치는 영향을 분석하는 프로젝트입니다.  
Python과 Jupyter Notebook을 활용하여 FOMC 일정과 주가 변동 간의 관계를 시계열 데이터로 분석하고 시각화합니다.

---

## ✨ 주요 기능

- 🗓️ FOMC 공식 사이트에서 회의 일정 자동 수집
- 📈 yfinance를 이용해 주식 및 금융 지표 데이터 다운로드
- 🔍 FOMC 일정 전후 금융시장 반응 분석
- 📊 데이터 시각화 및 인사이트 도출

---

## 🛠️ 사용 기술

- <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" height="20"/> Python
- <img src="https://img.shields.io/badge/Pandas-Dataframe-informational?logo=pandas&logoColor=white" height="20"/> Pandas
- <img src="https://img.shields.io/badge/Matplotlib-Graph-orange?logo=plotly&logoColor=white" height="20"/> Matplotlib
- <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white" height="20"/> Jupyter Notebook
- <img src="https://img.shields.io/badge/YFinance-API-success?logo=yahoo&logoColor=white" height="20"/> yfinance
- BeautifulSoup4, Requests

---

## 📦 설치 방법

```bash
# 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows

# 필수 패키지 설치
pip install yfinance pandas matplotlib jupyter beautifulsoup4 requests
```

---

## 🚀 사용 방법

```bash
# Jupyter Notebook 실행
jupyter notebook

# "fomc_analysis.ipynb" 파일 열기
```

---

## 📁 프로젝트 구조

```
.
├── data/                  # 수집한 데이터 저장 폴더
├── notebooks/             # 분석용 Jupyter 노트북 파일
├── scripts/               # 데이터 수집 및 처리용 파이썬 스크립트
├── README.md              # 프로젝트 설명 파일
```

---

## 📊 결과 예시

- 📈 FOMC 발표 전후 S&P500 지수의 변동성 분석
- 📉 FOMC 일정에 따른 주요 주식/섹터 반응 패턴 분석

---


<p align="center"><i>Made with ❤️ by Python & Data Science</i></p>
