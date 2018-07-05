# 설명

외산 smi 파일을 가지고 번역된 smi 파일은 국산 제품 TV에서 인식을 못합니다.

국산 제품 TV는 smi 파일 내부 구조까지 KRCC(또는 KoreanSC) 형태를 띈 내부 구조만 인식합니다.

이 프로그램은 국산 제품 TV가 인식할 수 있도록 smi 파일 내부 구조를 KRCC 형태로 바꿔줍니다.

# 사용법

실행 파일을 smi 파일들이 있는 디렉토리에 넣고 실행합니다. 

현재 디렉토리 뿐만 아니라 모든 하위 디렉토리를 거쳐가면서 smi 파일들을 수정 작업하므로 수정을 바라지 않는 파일까지 수정되지않도록 주의하시기 바랍니다.

SMI FILES 폴더를 같이 동봉하였습니다. FixSmi.exe 파일을 실행하여 정상적으로 수행되는지 테스트해볼 수 있습니다.

# 작업 과정

FixSmi.py 파일을 직접 보시면 아시겠지만 굉장히 짧은 코드입니다.

1. encc 속성을 krcc로 바꿉니다.
2. enuscc 속성을 krcc로 바꿉니다.
3. '</p></sync>' 태그들을 삭제합니다.
4. '<samiparam>' 태그 전체 내용을 태그를 포함하여 삭제합니다.


# 예외 상황

이 프로그램을 실행해도 TV에서 자막이 보이지 않는다면 구글에  [tv usb 영화 자막]  이라고 검색하여 다른 해결책을 찾으시기 바랍니다. 

어쩌면 자막 파일 자체가 비정상적으로 작성된 파일일 수 있습니다.

