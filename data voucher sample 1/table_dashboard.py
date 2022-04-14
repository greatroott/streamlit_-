import streamlit as st 
import pandas as pd 

# title 설정 
st.subheader("Sample dashboard")
# 텍스트 작성
st.write("현재 데이터는 예시 데이터로 실시간 업데이트가 되지 않습니다.")

# 다중 선택 박스 만들기 (고객 생애주기에 대한 정의를 진행함)
multi_select = st.multiselect("고객의 생애주기를 선택해주세요.",["영유아","아동","청소년","청년","중장년","노년","임신&출산"])

# 속도를 증진시키기 위해 캐시에 데이터를 저장함(캐시는 notion 정리할 것)
@st.cache
def load_data(select_name):
    df = pd.read_excel("test.xlsx",index_col=0)
    df = df[(df['생애주기'].str.contains("|".join(select_name),na = False)) ]
    return df.sort_values(by = ['조회수'],ascending = False).reset_index(drop=True)[['서비스명',"서비스 요약","서비스 상세 링크"]]

if multi_select: 
    df_load_state = st.text("Loading data ...")
    df = load_data(multi_select)
    st.write(df)
    df_load_state.text("Done!")
