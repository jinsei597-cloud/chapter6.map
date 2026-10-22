import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import math

# 1. 앱 제목 설정
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석 앱")

# 2. 파일 업로드 기능
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 3. CSV 데이터 불러오기
    df = pd.read_csv(uploaded_file)

    # ① 데이터 표로 보여주기
    st.subheader("📊 데이터 확인하기")
    st.dataframe(df)

    # ② 지도 생성 (부산 중심 좌표 설정)
    st.subheader("🗺️ 지하철역 이용객 지도")
    # 부산시청 근처 좌표(위도: 35.1796, 경도: 129.0756)를 중심으로 설정
    m = folium.Map(location=[35.1796, 129.0756], zoom_start=11)

    # 데이터 프레임의 각 행을 반복하면서 지도에 원(CircleMarker) 표시
    for index, row in df.iterrows():
        # 이용객수에 비례하여 반지름 설정 (면적이 비례하도록 제곱근 사용)
        # 숫자가 너무 작으면 안 보이므로 적당히 배수(* 0.05)를 곱해줍니다.
        radius_val = math.sqrt(row['이용객수']) * 0.05

        # 지도에 동그라미 마커 추가
        folium.CircleMarker(
            location=[row['위도'], row['경도']],  # 마커 위치 (위도, 경도)
            radius=radius_val,  # 계산한 반지름
            color='blue',  # 테두리 색상
            fill=True,  # 채우기 여부
            fill_color='blue',  # 채우기 색상
            fill_opacity=0.6,  # 투명도 (0~1 사이)
            tooltip=row['역명'],  # ③ 마우스를 올렸을 때: 역명
            popup=f"{row['역명']} 이용객 수: {row['이용객수']:,}명"  # ③ 클릭했을 때: 이용객 수
        ).add_to(m)

    # Streamlit 화면에 folium 지도 출력하기
    st_folium(m, width=700, height=500)

else:
    st.info("💡 위에서 busan_subway.csv 파일을 업로드해주세요!")