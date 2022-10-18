# 잔돈계산
def computeCharge(payM,recM):
    remM = recM - payM

    print(f'상품금액: {payM}원, 받은금액: {recM}원, 잔액: {remM}원')

    m_50000 = remM // 50000
    m_10000 = (remM%50000) // 10000
    m_5000 = (remM%10000) // 5000
    m_1000 = (remM%5000) // 1000
    m_500 = (remM%1000) // 500
    m_100 = (remM%500) // 100

    print(f'5만원: {m_50000:d}장 \n'
          f'1만원: {m_10000:d}장\n'
          f'5천원: {m_5000:d}장\n'
          f'1천원: {m_1000:d}장\n'
          f'5백원: {m_500:d}장\n'
          f'1백원: {m_100:d}장\n')

# 신용카드 판별
def checkCredit(card):
    card = str(card)
    result = ''
    if card[:2] == '35':
        nums = card[2:]  # 나머지 카드 번호 추출
        if nums == '6317':
            result = 'NH농협 JCB카드'
        elif nums == '6901':
            result = '신한 JCB카드'
        elif nums == '6912':
            result = 'KB국민 JCB카드'
        else:
            result = '잘못된 카드번호입니다!!'
    elif card[:1] == '4':
        nums = card[1:]  # 나머지 카드 번호 추출
        if nums == '04825':
            result = '비씨 비자카드'
        elif nums == '38676':
            result = '신한 비자카드'
        elif nums == '57973':
            result = '국민 비자카드'
        else:
            result = '잘못된 카드번호입니다!!'
    elif card[:1] == '5':
        nums = card[1:]  # 나머지 카드 번호 추출
        if nums == '15594':
            result = '신한 마스타카드'
        elif nums == '24353':
            result = '외환 마스타카드'
        elif nums == '40926':
            result = '국민 마스타카드'
        else:
            result = '잘못된 카드번호입니다!!'
    else:
        result = '잘못된 카드번호입니다!!'
    print(result)

# 해당년도 60갑자 출력
def checkChinaZodiac(year):
    year = str(year)
    sipgan = ('신', '임', '계', '갑', '을', '병', '정', '무', '기', '경',)
    sipizy = ('유', '술', '해', '자', '축', '인', '묘', '진', '사', '오', '미', '신')
    idx1 = int(year[3:]) - 1
    idx2 = int(year) % 12 - 1
    fYear = sipgan[idx1]
    lYear = sipizy[idx2]
    print(fYear + lYear, '년')

computeCharge(1000,48000)
checkCredit(540926)
checkChinaZodiac(1988)
