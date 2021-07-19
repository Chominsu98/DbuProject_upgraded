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
