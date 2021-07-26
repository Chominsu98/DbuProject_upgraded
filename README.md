# DbuProject_upgraded
던바이어스 출석체크프로그램 카메라성능 및 부가적기능추가 version

기본적으로 Django 기반 웹서비스


사용하기 위한 기본환경설정


Django 가상환경에다가 
-django 3.2.4version 설치

-pip install gspread 구글스프레드시트를 쓰기 위한 환경들입니다.밑에는

-pip install --upgrade oauth2client

-pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

구글스프레드시트를 사용하기 위해서는 api를 사용해야하므로

api를 사용하기 위해서 json파일을 사용하는데 해당 api의 client 이메일을 원하는 파일에서 이메일 공유하기를 한다

글고 각자 자신의 api를 원하는 경로에 폴더에 넣고 그 경로만 잘 view.py에서 넣어주면 됨



[07.20업데이트내역]->이건 두번째 커밋에 적용되어있지 않지만은 결론적으로 던바 세번째 수정버젼에 같이 들어가있음
-중간 팝업페이지 삭제

-메인 홈페이지에서 바로 출석누를시 카메라화면쪽으로 이동

-종종 브라우저 껐다가 키면 들어가면 뜨던 에러페이지 삭제

-카메라 페이지 UI변경

-파일소유자 변경->던바꺼로






[07.26 업데이트 내역]->third_upgraded 브랜치에 푸시해놓음
1.관리자페이지 UI생성

2.관리자외 관리자이후 페이지 접근 금지

3.관리자페이지 접속시 두가지 메뉴가능

-패스코드 변경

-금일 출석 현황 확인가능

(굳이 매번 스프레드시트 들어가면 귀찮으니까?)
