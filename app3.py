import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.font_manager as fm

# 한글 폰트 설정
#plt.rcParams['font.family'] = "AppleGothic"
# Windows, 리눅스 사용자
#plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['font.family'] = "LG Smart UI"
#plt.rcParams['font.family'] = "Nanum Gothic"
plt.rcParams['axes.unicode_minus'] = False

# # 나눔글꼴 경로 설정
#font_path = "C:/Users/종호/AppData/Local/Microsoft/Windows/Fonts/NanumGothic.ttf"

# # 폰트 이름 가져오기
#font_name = fm.FontProperties(fname=font_path).get_name()
# # 폰트 설정
#plt.rc('font', family=font_name)

# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=False)

fig, ax = plt.subplots()
ax.bar(data['이름'], data['나이'])
st.pyplot(fig)


barplot = sns.barplot(x='이름', y='나이', data=data, ax=ax, palette='Set2')
fig = barplot.get_figure()

st.pyplot(fig)

#############

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

st.pyplot(fig)

##### Barcode

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')

st.pyplot(fig)