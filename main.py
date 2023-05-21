import re

#패턴 매칭
pattern = r"abc"  # 정규 표현식 패턴
text = "abcdef"  # 검색 대상 문자열

match = re.search(pattern, text)
if match:
    print("매칭되었습니다.")
else:
    print("매칭되지 않았습니다.")

#패턴 추출
pattern = r"(\d{4})-(\d{2})-(\d{2})"  # 날짜 형식 패턴
text = "생성일자: 2023-05-21"

match = re.search(pattern, text)
if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    print(f"년: {year}, 월: {month}, 일: {day}")

#문자열 대체
pattern = r"apple"
text = "I have an apple."

new_text = re.sub(pattern, "orange", text)
print(new_text)  # "I have an orange."
