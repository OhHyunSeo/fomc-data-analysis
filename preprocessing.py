#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 19:21:38 2025

@author: oh
"""
'''
분석 목표 :
미국 연준의 FOMC 회의 일정과 그 결과(금리 인상/동결/인하)가 
미국 증시(S&P 500 등)에 단기적으로 어떤 영향을 주는지 분석
→ 주가 수익률 및 변동성(Volatility)이 발표일 전후로 어떻게 달라지는지를 시계열적으로 분석

[FOMC 일정과 주가 변동성 분석] 프로젝트 흐름

수행 순서

1. 데이터 수집

1.1 FOMC 일정 및 정책 발표 수집
데이터 항목: 날짜, 기준금리 결정, 금리 변화 여부 (인상/동결/인하), 성명서 요약(optional)

수집 방법: 연준 공식 홈페이지 (FOMC calendar)

참고로 수동 수집도 가능 (10년치 일정 많지 않음)

2.1 주가 데이터 수집
대상:

S&P 500 지수 (^GSPC)

NASDAQ (^IXIC)

VIX 변동성 지수 (^VIX)

도구: yfinance (간단하고 안정적)
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf


































