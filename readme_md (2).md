# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 지도 상에 시각화하는 대화형 Web Application입니다.

---

## 📌 주요 기능

1. **데이터 업로드 및 확인**: `busan_subway.csv` 파일을 업로드하고, 데이터 프레임을 표 형태로 한눈에 확인합니다.
2. **지하철역 지도 시각화**: 
   - 부산 주요 역의 위도, 경도 좌표를 기반으로 지도를 생성합니다.
   - 각 역의 **이용객 수에 비례(면적 비례, 제곱근 적용)하여 원(CircleMarker)의 크기를 다르게 표시**합니다.
3. **인터랙티브 마커 반응**:
   - **Hover (마우스 오버)**: 해당 위치의 **역명**을 표시합니다.
   - **Click (마우스 클릭)**: 해당 역의 **이용객 수**를 팝업창으로 출력합니다.

---

## 📂 파일 구성

- `app.py`: Streamlit 메인 실행 파이썬 코드
- `busan_subway.csv`: 부산 지하철 역별 데이터 (호선, 역명, 위도, 경도, 이용객수 포함)
- `requirements.txt`: 프로젝트 실행을 위한 의존성 라이브러리 목록
- `README.md`: 프로젝트 설명 문서

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language**: Python
- **Web Framework**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Folium, Streamlit-Folium

---

## 🚀 실행 방법 (Local Run)

1. **저장소 클론 (Clone)**
   ```bash
   git clone https://github.com/사용자이름/저장소이름.git
   cd 저장소이름
   ```

2. **필요 라이브러리 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **앱 실행**
   ```bash
   streamlit run app.py
   ```