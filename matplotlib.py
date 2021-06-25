import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font) # 한글 폰트 잦아 사용하기

ratio = [34, 32, 16, 18]
labels = ['사과', '바나나', '메론', '포도']

plt.title('과일 선호도 조사') # 제목
plt.pie(ratio, labels=labels, autopct='%.1f%%') # 그래프 출력
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1)) # 범례
plt.grid(True)
plt.show() # 뷰어
