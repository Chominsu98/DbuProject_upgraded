
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
# import simplejson as json
from django.http import JsonResponse
import json

import string
from datetime import datetime

#로그인페이지 구현을 위한 import
from django.core.exceptions import PermissionDenied
from django.urls import reverse


#내가 사용할려는 구글 스프레드시트의 url
default_url = 'https://docs.google.com/spreadsheets/d/116tUqWRAQBbTYeQrQQJ9Bl7I7BJxp3Dq_KyeQYZAnt8/edit#gid=0'
state=1
#스프레드시트 연관 클래스 생성
class GoogleSpreadSheet:

    def __init__(self,url):
        self.spreadsheet_url=url
        self.sheet="시트1"

    def set_spreadsheet_url(self,url):
        self.spreadsheet_url=url

    def set_sheet(self,sheet):
        self.sheet=sheet

    def google_spread_connection(self):
        scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
        ]
        json_file_name = os.getcwd()+'\showing_app\dbu_json\dbuchecker-edaf08093d83.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
        gc = gspread.authorize(credentials)
        # 스프레스시트 문서 가져오기 
        doc = gc.open_by_url(self.spreadsheet_url)
        # 시트 선택하기
        self.worksheet = doc.worksheet(self.sheet)   

        return self.worksheet

    def get_worksheet(self):
        return self.worksheet

    def cell_write(self):
        print("write")
    def cell_find(self,target):
       print("find")
       cell_info=str(self.worksheet.find(target)[0]).split()[1]
       return cell_info
    def cell_read(self): 
        print("read")   



#메인 홈페이지 UI 랜더링 함수
def home_UI(request):
    if request.session["login_page"]!=True:
        raise PermissionDenied
    global state
    if state==1:
        global spreadsheet
        spreadsheet=GoogleSpreadSheet(default_url)
        state+=1

        worksheet=spreadsheet.google_spread_connection()
        row_data=worksheet.row_values(1)
        print(row_data)
        #print(os.getcwd()+'\showing_app\dbu_json\dbuchecker-edaf08093d83.json')
    return render(request,"index.html")

#단순 카메라 인식페이지 랜더링 함수
def camera_exam(request):
    if request.session["login_page"]!=True:
        raise PermissionDenied
    return render(request,"camera_exam.html")    

#로그인 페이지
def login_render(request):
    request.session['login_page']=False
    return render(request,"login.html")

def login(request):
    secret_code="dbc1110"
    if request.method=="POST":
        print("들어와따")
        scan_code=json.loads(request.body)
        print(scan_code)
        scan_code.split('=')[1]
        if scan_code.split('=')[1]==secret_code:
            context={"result":True}
            request.session['login_page']=True
        else:
            context={"result":False}
        return JsonResponse(context)
def logout(request):#미완성-개발중
    del request.session['login_page']
    return redirect(reverse('login_render'))

#카메라인식페이지에서 데이터 가공과 함께 json보내주는 함수
def camera_data_pop(request):
    worksheet=spreadsheet.get_worksheet()

    if request.method=="POST":
        scan_data=json.loads(request.body)
        print(scan_data)
    today_date=datetime.today().strftime("%m"+'/'+"%d") #오늘 현재 날짜를 구해놓는다
    try:
        worksheet.find(today_date,in_row=1,in_column=None)#오늘날짜로 이미 만들어놓은적이 있는지 확인
    except:
        print("i need to make,,,,a new date")    #해당날짜로 만들어진게 없는 경우 오늘날짜로 출석부 하나 만듦
        row_data=worksheet.row_values(1)
        next_cell_date=string.ascii_uppercase[len(row_data)]+'1'#다음 추가할 셀의 위치 파악

        print(next_cell_date)
        print(today_date)
        worksheet.add_cols(1)#새롭게 날짜를 넣을 열 확장
        worksheet.update_acell(next_cell_date,today_date)#1열에 오늘날짜로 새롭게 추가
        worksheet.format(next_cell_date,{'textFormat':{'bold':True},'horizontalAlignment':"CENTER"})#날짜는 글씨 굵고 배치 가운데로 

    try:
        find_target_data=worksheet.find(scan_data,in_row=None,in_column=2)#해당 스캔정보로 해당 회원이 있는지 서치
        print(find_target_data)
    except:
        print("회원정보가 없다.")
        tmp="✔해당 정보의 회원은 존재하지 않습니다."

    else:    
        name=worksheet.cell(find_target_data.row,find_target_data.col-1).value
        row_info=int(find_target_data.row)
        col_info=len(worksheet.row_values(1))

        print(name)
        print("row_info:",row_info)
        print("col_info:",col_info)

        if worksheet.cell(row_info,col_info).value=="✔":
            tmp="✔"+name+"님은 이미 출석체크가 되셨습니다."
       

        else:
            worksheet.update_cell(row_info,col_info,"✔")    
            tmp="✔"+name+"님께서는"+" "+today_date+"로 출석체크 되셨습니다.환영합니다!"
    context={'result':tmp}
    return JsonResponse(context)

#테스트용 함수
def select(request):
    return render(request,"new_camera.html")