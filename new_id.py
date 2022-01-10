# 신규아이디 추천
def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for id in new_id:
        if id == '-' or id == '_' or id == '.' or id.islower() or id.isdigit():
            answer = answer + id
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
    length = len(answer)
    if length != 0 and answer[length-1] == '.':
        answer = answer[:length-1]
    # 5단계
    if answer == "":
        answer = answer + 'a'
    # 6단계
    length = len(answer)
    if length >= 16:
        answer = answer[:15]
    length = len(answer)
    if length != 0 and answer[length-1] == '.':
        answer = answer[:length-1]
    # 7단계
    length = len(answer)
    while length <= 2:
        last_char = answer[length-1]
        answer = answer+last_char
        length = len(answer)
    return answer


def main():
    a = [1, 3, 19]
    print(a[0])
