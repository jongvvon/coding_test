from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    # today to datetime
    today_dt = datetime.strptime(today, "%Y.%m.%d")
    # 'A': ['6']
    terms_dict = {items.split()[0]: items.split()[1:] for items in terms}
    # ['2021.05.02', 'A']
    privacies_matrix = [item.split() for item in privacies]

    for i in range(len(privacies_matrix)):
        privacies_date = datetime.strptime(privacies_matrix[i][0], "%Y.%m.%d") + relativedelta(months=int(terms_dict[privacies_matrix[i][-1]][0]))
        if today_dt >= privacies_date:
            answer.append(i+1)
        
    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today, terms, privacies))


# 모든 달은 28일!

def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
