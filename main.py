# 724-774 1 経済
# 869-904 2 政治
# 520-615 3 国際政治経済
# 001-763 4 ジャーナリズム
# 101-108 5 学際領域

# 科目名, 副題, 事前・事後学習の内容,　授業概要, 備考・関連URL

import csv

f = open('waseda_zemi_syllabus.csv', 'a')
writer = csv.writer(f)
writer.writerow(["科目名", "副題", "事前・事後学習の内容", "授業概要", "備考・関連URL"])
f.close()

import urllib.request, urllib.error
from bs4 import BeautifulSoup

code_list = ["100", "200", "300", "400", "500"]
num_start  = [724, 869, 520, 1, 101]
num_end  =   [774, 904, 615, 763, 108]
alpa = "P" # P/Q
# alpa = "Q"

flag = False
end = False
tag = ""
key = ""
i = 0
# i = 4


while (end != True):

    f = open('waseda_zemi_syllabus.csv', 'a')
    writer = csv.writer(f)

    for num in range(num_start[i], num_end[i] + 1):

        csv_list = [None]*5

        code = code_list[i]

        key = code + alpa + str(num).zfill(3)                                            # 3ケタにゼロ埋め

        url = "https://www.wsl.waseda.jp/syllabus/JAA104.php?pKey=110" + key + "012021110" + key + "11&pLng=jp"

        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")

            tbody = soup.find_all("tbody")

            base_info = tbody[1]
            det_info  = tbody[2].text.split("\n")

            course_title = base_info.text.split("\n")[6]                        # 科目名

            print("科目名:" + course_title)

            csv_list[0] = course_title

            for info in det_info:

                if (flag == True):
                    print(tag + ":" + info + "\n")

                    if (tag == "副題"):
                        csv_list[1] = info
                    elif (tag == "事前・事後学習の内容"):
                        csv_list[2] = info
                    elif (tag == "授業概要"):
                        csv_list[3] = info
                    elif (tag == "備考・関連URL"):
                        csv_list[4] = info

                if (info == "副題" or info == "事前・事後学習の内容" or
                    info == "授業概要" or info == "備考・関連URL"):
                    flag = True
                    tag = info
                else:
                    flag = False

            writer.writerow(csv_list)

        except:
            pass

        if (key == "500Q108"):
            end = True
            f.close()
            break

        if (num == num_end[i] and alpa == "P"):
            alpa = "Q"
        elif (num == num_end[i] and alpa == "Q"):
            alpa = "P"
            i += 1