# DbuProject_upgraded
[반응형 모바일 WepApp]던바이어스 출석체크프로그램 카메라성능 및 부가적기능추가 version


![header](https://capsule-render.vercel.app/api?type=waving&color=292929&height=300&section=header&text=DBUChecker&fontSize=90&animation=fadeIn&fontAlignY=38&desc=던바이어스%20자동화%20회원관리서비스&descAlignY=60&fontColor=ffffff)

<h3 align="center">던바이어스 출석체크프로그램 카메라성능 및 부가적기능추가 version</h3>
<p align="center"><img align="center" src="https://user-images.githubusercontent.com/37100067/199920801-fe62b9f4-ff68-40d1-a435-f6e517119cad.png" width="33%" /></p>



<h1>DbuChecker</h1>
> Django 및 JsQr 기반 던바이어스 회원관리 웹 서비스

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FChominsu98%2FDbuProject_upgraded%2F&count_bg=%2379C83D&title_bg=%23555555&icon=insomnia.svg&icon_color=%232DCE89&title=%EB%B0%A9%EB%AC%B8&edge_flat=false)](https://hits.seeyoufarm.com)
[![GitHub forks](https://img.shields.io/github/forks/Chominsu98/DbuProject_upgraded?color=2379C83D)](https://github.com/Chominsu98/DbuProject_upgraded/network)
[![GitHub stars](https://img.shields.io/github/stars/Chominsu98/DbuProject_upgraded?color=2379C83D)](https://github.com/Chominsu98/DbuProject_upgraded/stargazers)

영어스피킹커뮤니티 회사 DoneByUs의 외주요청-Qr코드기반 출석체크 웹사이트
jsQr을 통한 qrcode인식으로 ajax로 서버로 보내어 GoogleDocs에 출석부를 생성후 관리해주는 웹사이트
관리자 페이지가 따로 존재하여 관리자만 직접 금일 출석정보 관리가능

## :hammer_and_pick:기술태그:hammer_and_pick:

<div style="display:flex">
   <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
   <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
   <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
   <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
   <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
</div>






# :desktop_computer:대표적 기능

* <a href="">각 팀의 리더들만 접속가능</a>
* <a href="">qr코드 인식을 통한 회원들의 출석서비스 구글스프레드시트와 연동</a>
* <a href="">금일 출석명단 확인가능</a>
* <a href="">관리자페이지</a>


<!-- 이미지들을 깃허브에서 가로정렬을 하기위해서는 쭉 한줄로 최대한 연결해주면 됨 인라인 스타일 css안먹힘 -->



<p>
   <img src="https://user-images.githubusercontent.com/37100067/199925044-3fbdaa18-4cf1-4366-bbe8-8f7881859667.png" width="25%" /><img src="https://user-images.githubusercontent.com/37100067/199926630-4de4b4ab-125e-42c8-9f0c-80ead9690af1.png" width="25%" /><img src="https://user-images.githubusercontent.com/37100067/199927235-4acb761c-8a26-4ff5-bce2-51e9cb431cad.png" width="25%" /><img src="https://user-images.githubusercontent.com/37100067/199928558-7f2d6716-62fc-4e11-8f30-4701a109c104.png" width="25%" />
</p>



## :printer:사용 예제

1.던바이어스 리더들만의 코드를 입력해주시고 접속해주세요!

2. 접속 후 회원들의 qr코드를 스캔하여 회원들의 출석을 체크해주세요!

<img src="https://user-images.githubusercontent.com/37100067/199933059-98fdbbc8-cefc-4444-8817-928f6ccd4a3c.gif">

## :gear:개발 환경 설정

원활한 사용을 위해서는 
1.가상환경 설정
2. django 3.2.4version 설치
```bash
  pip install --upgrade oauth2client
  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
(되도록이면 버젼을 맞춰 설정해주세요)

## :watch:업데이트 내역

* 1.0.0(07.16)
    * 3차 최종판 릴리즈


## :technologist:개발자정보

* :technologist:조민수(FE&BE개발) –<a href="https://github.com/Chominsu98/"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a><a href="https://velog.io/@woo0_hooo"><img src="https://img.shields.io/badge/Tech%20Blog-11B48A?style=flat-square&logo=Vimeo&logoColor=white&link=https://velog.io/@plugnplay"/></a>


## :computer_mouse:기여 방법

1. (<https://github.com/PockeTrainer/Pocket_Trainer.git>)을 포크합니다.
2. (`git checkout -b feature/fooBar`) 명령어로 새 브랜치를 만드세요.
3. (`git commit -am 'Add some fooBar'`) 명령어로 커밋하세요.
4. (`git push origin feature/fooBar`) 명령어로 브랜치에 푸시하세요. 
5. 풀리퀘스트를 보내주세요.

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki


## :keyboard:참고한 OpenSource

1. <a href="https://github.com/cozmo/jsQR">(qr코드인식)JsQr</a>

2. <a href="https://code.google.com/archive/p/java-simple-serial-connector/">(gspread)-구글스프레드시트 조작 패키지</a>

3. <a href="https://html5up.net/spectral">반응형 레이아웃구성</a>




