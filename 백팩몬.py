from this import d
from threading import Thread
from time import sleep
import random
#레벨올리기가 이상한듯

two_sleep = 2
two_plus_sleep = two_sleep + 0.5

스토리 = 1
캐릭터 = '김백팩'
레벨 = 1
레벨올리기 = 0
기준 = 50
훈련 = ''
print('                     백팩몬')
print('                  모험의 시작')
print('')
print('                     로딩중')
if 스토리 == 0:
    print('나: 오늘은 내생일')
    sleep(two_sleep)
    print('나: 과연 무슨 선물을 줄지 기대되네~')
    sleep(two_sleep)
    print("나: '제발 백팩몬만 아니길 내 친구 말로는 완전 구리다던데..")
    sleep(two_sleep)
    print('두구두구')
    sleep(two_sleep)
    print('나: 히히 과연 뭘까?')
    sleep(two_sleep)
    print('아버지: 허허 놀라지마라.')
    sleep(two_plus_sleep)
    print('나: 히힛 짜잔!')
    sleep(1.5)
    print('나: 어?')
    sleep(two_sleep)
    print('나: 백팩몬이 잖아??!')
    sleep(two_sleep)
    print('그날 밤..')
    sleep(3)
    print('나: 하 아빠 진짜 너무하네')
    sleep(two_sleep)
    print('쿨쿨')
    print('')
    sleep(3.5)
    print('퍽퍽퍽')
    sleep(two_sleep)
    print('나: 으으 여긴 어디지? 그런데 누가 때렸지?')
    sleep(two_sleep)
    print('???: 어디긴 어디야 여기는 백팩몬 월드이다. 그리고 내가 때렸지')
    sleep(two_sleep)
    print('나: 백팩몬 월드??!')
    sleep(two_sleep)
    print('???: 이곳은 백팩몬을 위한 곳이지')
    sleep(two_sleep)
    print('???: 보아하니 백팩몬을 무시하는거 같던데,')
    print(      '백팩몬 토너먼트에서 우승하고 나랑 싸워서 이기면 내가 너를 백팩몬월드에서 해방시켜주지')
    sleep(3)
    print('나: 왓???! 이런 납치범을 봤나, 여기서 달랑 남겨놓고 백팩몬 토너먼트같은 소리 지껄이고 있네')
    print('    백팩몬도 없는데 어떻게..')
    sleep(two_plus_sleep)
    print('나: 흡!!')
    print('???: 그 백팩몬 가지고 잘해봐라 그럼 이만..')

적 = 0
전체체력 = 10
넘어가기 = 0
행동 = 0
결과 = 0
피해 = 0
내체력 = 10
내피해 = 0
랜덤체력 = 3
싸울적 = '카이리'
설정 = 0
공격력 = 1
방어력 = 0
적들 = ['카이리', '카를루스', '김강해', '블레이즈', '케르베우스', '파이루', '삐삐', '뽀삐', '삐룰루스', '파피루스', '샌즈', '나이몽', '나인테일', '무에타일', '허경영', '피에룬', '피까쮸', '뾰잉뾰잉', '엉금엉금', '샤악샤악', '으쌰으쌰', '킹문어', '키루키루']
if 스토리 == 0:
    캐릭터 = input('당신과 함께할 백팩몬 이름을 정하세요:  ')
sleep(1)
sleep(1)

def 싸우기(s, b):
    넘어가기 = 0
    적 = s
    적 = str(적)
    적체력 = b
    적체력 = str(적체력)
    행동 = 0
    결과 = 0
    피해 = 0
    내피해 = 0
    내체력 = 10
    내체력 = int(내체력)
    sleep(1.5)
    print('야생의 ' + 적 + ' (이)가 나타났다!')
    print(캐릭터 + '의 체력은 ' + str(내체력) + ' 이다!')
    print(적 + '의 체력은 ' + 적체력 +' 이다!')
    while 넘어가기 == 0:
        print('어떻게 하겠는가?')
        행동 = 0
        결과 = 0
        방어력 = 0
        적체력 = b
        print('공격하기(1)')
        print('회복하기(2)')
        print('도망가기(3)')
        행동 = input()
        행동 = str(행동)
        if 행동 == '1':
            print(캐릭터 + '(이)가 공격을 했다!')
            sleep(1)
            공격력 = random.randrange(레벨, 레벨 + 3)
            공격력 = str(공격력)
            print(캐릭터 + '의 공격은 ' + 공격력 + ' 의 피해를 주었다!')
            공격력 = int(공격력)
            피해 += 공격력
            if 적체력 == '0':
                넘어가기 = 1
        if 행동 == '2':
            print(캐릭터 + '(이)가 회복을 했다!')
            방어력 = random.randrange(레벨, 레벨 + 3)
            방어력 = str(방어력)
            내체력 = int(내체력)
            print(캐릭터 + '(은)는 '  + 방어력 + ' 만큼 회복했다!')
            내체력 += int(방어력)

            print(캐릭터 + '의 체력은 ' + str(내체력) + ' 이다!')
            sleep(1)
        if 행동 == '3':
            print('당신은 도망을 시도했다!')
            결과 = '당신은 도망에 성공했다!'
            sleep(1)
            print(결과)
            return
        sleep(1)
        적체력 = b - 피해
        적체력 = int(적체력)
        if 적체력 <= 0:
            넘어가기 = 1
        else:
            적체력 = str(적체력)
            print('현재 ' + 적 +'의 체력이 ' + 적체력 + ' 이 됐다!')
        sleep(1)
        print(적 + '(이)가 공격을 했다!')
        sleep(1)
        공격력 = random.randrange(1, 3)
        공격력 = str(공격력)
        print(적 + '의 공격은 ' + 공격력 + ' 의 피해를 주었다!')
        sleep(1)
        공격력 = int(공격력)
        방어력 = int(방어력)

        내피해 += 공격력
        내체력 = int(내체력)
        내체력 = 내체력 - 내피해
        내체력 = str(내체력)
        if '0' == 내체력:
            print(캐릭터 + '(은)는 장렬히 목숨을 거뒀다...')
            sleep(two_sleep)
            print('당신은 재빨리 ' + 캐릭터 + '(와)과 병원으로 갔다.')
            sleep(1)
            print('이얍, 위이이잉 꿀꺽꿀꺽, 두두두두, 샤라랑샤라랑')
            내체력 = 전체체력
            sleep(3)
            print(캐릭터 + '(이)가 말끔히 치료되었다!')
            return
        sleep(1)
        print('현재 ' + 캐릭터 + '의 체력이' + 내체력 +'이 됐다!')
    
    print('와!' + 적 + '이(가)죽었다!')
    sleep(1.5)
    레벨올리기 += 40
    print('병원으로 가서 '+ 캐릭터 + '(을)를 치료하자')
    넘어가기 = 0

while True:
    print('병원가기(1)')
    print('야생의 백팩몬 잡기(2)')
    print('백팩몬 훈련시키기(3)')
    print('게임 끝내기(4)')
    print('설정(5)')
    print('토너먼트(6)')
    if 레벨올리기 >= 기준:
        레벨 += 1
        레벨올리기 = 0
        print(캐릭터 + ' 의 레벨이 ' + 레벨 + '(이)가 됐다!')

    행동 = input()
    if 행동 == '1':
        sleep(1)
        print('네 병원입니다. 무엇을 도와드릴까요.')
        print('백팩몬 치료를 맏길까? 예:1 / 아니오:2')
        맏길까 = input()
        if 맏길까 == '1':
            print('네 맏겨만주세요.')
            sleep(5)
            print(캐릭터 + '(이)가 말끔히 치료되었다!')
            내체력 = 전체체력
            레벨올리기 += 1
        if 맏길까 == '2':
            print('네 다음에 오세요~')
            sleep(0.5)
    if 행동 == '2':
        싸울적 = random.randrange(0, len(적들))
        랜덤체력 = random.randrange(3, 50 + 레벨)
        싸우기(적들[싸울적], 랜덤체력)
    if 행동 == '3':
        print('훈련 - 스페이스바+엔터키 연타')
        while 넘어가기 == 0:
            훈련 = input()
            if 훈련 == '그만':
                넘어가기 = 1
            else:
                if 훈련 == ' ':
                    레벨올리기 += 1
                if 레벨올리기 >= 기준:
                    레벨 += 1
                    레벨올리기 = 0
                    기준 += 1
                    print(캐릭터 + ' 의 레벨이 ' + str(레벨) + '(이)가 됐다!')
    if 행동 == '4':
        print('게임을 종료합니다.')
        exit()
    if 행동 == '5':
        print('네 설정입니다. 무엇을 도와드릴까요')
        print('캐릭터 개명(1)')
        print('진행현황(2)')
        print('개발자 모드(3)')
        설정 = input()
        if 설정 == '1':
            캐릭터 = input('개명할 이름을 적어주세요:  ')
            sleep(0.5)
            print('개명이 성공적으로 완료되었습니다.')
        if 설정 == '2':
            print('레벨:' + str(레벨))
            print('레벨올리기:' + str(기준) + ' / ' + str(레벨올리기))
            print('캐릭터 이름:' + str(캐릭터))
        if 설정 == '3':
            print('레벨을 정해주세요.')
            레벨 = int(input())
            print('성공적으로 마쳤습니다.')
        sleep(3)
    if 행동 == '6':
        if 레벨 <= 9:
                print('백팩몬 토너먼트는 10레벨부터 가능합니다.')
        else:
            print('백팩몬 토너먼트에 오신것을 환영합니다!')
            sleep(2)
            print('백팩몬 토너먼트는 총 24강이며,')
            sleep(2)
            print('우승을 하면 백팩몬월드의 왕을 만날 수 있습니다!')
            sleep(2)
            print("'흠 내가 만난 진상이 왕인가보군..")
            sleep(1.5)
            print('참가하겠습니다.')
            sleep(1.5)
            print('그러면 접수를 위해 이름을 알려주세요.')
            이름 = input()
            print(이름 + '님이 시군요! 접수 완료되셨습니다.')