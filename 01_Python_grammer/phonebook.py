num = 0
man = ""
phone_num = ""
Phone_book = {}

while True:
    print("########## 연락처 관리 시스템 메뉴 ##########")
    print("1. 연락처 등록")
    print("2. 연락처 전체보기")
    print("3. 이름으로 연락처 조회")
    print("4. 연락처 수정")
    print("5. 연락처 삭제")
    print("6. 종료")
    print("##########################################")
    num = int(input("원하는 작업을 번호를 입력해주세요: "))
    if num == 1:
        man = input("등록할 사람의 이름을 입력하세요: ")
        if man in Phone_book:
            print("이미 등록되어 있습니다. 전화번호 수정이 필요하시면 4번 작업을 선택해 주세요.")
        else:
            phone_num = input("등록할 전화번호를 '-'을(를) 제외하고 입력하세요: ")        
            Phone_book[man] = phone_num
            print("등록 완료!")        
    elif num == 2:
        print("********** 연락처 등록 현황 **********")
        print("이름",(" "*(11-len("이름"))),"연락처")
        for man in Phone_book:
            print(man, (" "*(10-len(man))),Phone_book[man])
        print("*************************************")
    elif num == 3:
        man = input("연락처를 검색할 사람의 이름을 입력하세요: ")
        print("********** 조회 결과 **********")
        if man in Phone_book:
            phone_num = Phone_book[man]
        else:
            phone_num = "등록된 역락처가 없습니다."
        print(phone_num)
        print("*******************************") 
    elif num == 4:
        man = input("연락처를 수정할 사람의 이름을 입력하세요: ")        
        if man in Phone_book:
            phone_num = input("새로운 엽락처를 입력하세요: ")  
            Phone_book[man] = phone_num
            print("수정 완료!")
        else:
            print("등록된 역락처가 없습니다. 추가를 원하시면 1번 작업을 선택해 주세요.")
    elif num == 5:
        man = input("연락처를 삭제할 사람의 이름을 입력하세요: ")        
        if man in Phone_book:
            del Phone_book[man]
            print("삭제 완료!")
        else:
            print("등록된 역락처가 없습니다.")
    elif num >= 6:
        break
    print()