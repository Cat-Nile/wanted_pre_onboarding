# wanted_pre_onboarding

## 1. 프로젝트 정보
---
본 서비스는 기업의 채용을 위한 웹 서비스 입니다.  
회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.


## 2. 설치 및 실행 방법
---
### Local 개발 및 테스트용
1. 해당 프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
```cmd
git clone https://github.com/Cat-Nile/wanted_pre_onboarding.git
```
```cmd
cd wanted_pre_onboarding
```

2. 가상 환경 생성 및 실행
```cmd
python -m venv myvenv
myvenv\Scripts\activate
```
3. Python 패키지 설치
```cmd
pip install -r requirements.txt
```
4. DB 생성 후 model의 변경사항을 DB에 반영한다.
```cmd
python manage.py makemigrations
python manage.py migrate
```
5. 서버를 실행한다.
```cmd
python manage.py runserver
```    


## 3. 사용 기술 및 Tools
---
1. Python 3.9.13
2. Django 3.2.13
3. djangorestframework 3.13.1
4. insomnia 2022.4.1(API Request 테스트용)


## 4. DB modeling
---
![onboarding](https://user-images.githubusercontent.com/107024591/174970823-8c18ac84-d7fb-4caa-a475-6e3ca4f491bb.jpg)


## 5. 구현 기능
---
1. 채용공고 등록 API
2. 채용공고 수정 API
3. 채용공고 삭제 API
4. 채용공고 목록 조회 API
	- 채용공고의 상세 페이지 조회하는 기능 구현(채용공고 목록에서는 나오지 않았던 채용내용('description') 필드 데이터가 나타남)
5. 채용 지원 API
	- 사용자는 채용공고_id를 통해 채용공고에 지원할 수 있음

##### 유의사항
\# SECURITY WARNING: keep the secret key used in production secret!
```
SECRET_KEY = os.environ['secret_key']
```
\# SECRET_KEY가 노출되는 것을 막기위해서 django_environ 패키지를 설치하였습니다.  
환경변수를 등록하여 거기에 SECRET_KEY를 환경변수에 저장하는 작업이 반드시 필요합니다.   
※ 환경변수 적용을 위해 재부팅이 필요할 수 있습니다.      

- 윈도우 환경변수 편집(SECRET_KEY)         
![환경변수편집](https://user-images.githubusercontent.com/107024591/175000346-fe1fb9c7-80fb-46c3-ad6b-ff6bb93e293b.jpg)

                         
### 가장 신경 쓴 부분
---
+ RESTFUL API를 효율적으로 다룰 수 있도록 코드를 설계하였습니다.   
프론트엔드 개발자나, 프로젝트 팀원과 원활한 소통과 빠른 프로젝트 진행을 위해 최대한 API 데이터를 선발과제 예시와 같이 깔끔하고 단순하게 표현하도록 했습니다.  
 - 그 과정에서 nested_serializer 사용으로 인한 중첩을 Flatten하게 구현하였습니다.
 - 상세한 설명 없이도 Class와 Serializer, Method, URL 등을 바로 직관적으로 알 수 있도록 명명하였습니다.

## 7. DB Superuser 설정
---
```cmd
python manage.py createsuperuser
```


## 8. 테스트
---
아래는 insomnia로 로컬에서 테스트한 문서 링크를 공유해드립니다.
* 채용담당자 생성  
![채용담당자 생성](https://user-images.githubusercontent.com/107024591/174989926-22763a93-3033-43f7-8df9-6e9671806df5.jpg)
* 채용공고 등록  
![채용공고_등록](https://user-images.githubusercontent.com/107024591/174989980-5ae1f672-8328-43de-a4c7-896bc99c8fe4.png)
* 채용공고 수정  
![채용공고 수정](https://user-images.githubusercontent.com/107024591/174989970-b6f6c7f4-5965-4fec-b7ef-c170fd126b3f.jpg)
* 채용공고목록 조회
![채용공고목록 조회](https://user-images.githubusercontent.com/107024591/174990017-9d24b593-08a8-41f1-a00f-b878d206b3bf.jpg)
* 채용상세페이지 조회
![채용상세페이지조회](https://user-images.githubusercontent.com/107024591/174989956-370e8825-e758-4d03-ad98-6601582d62ae.jpg)
* 채용공고 삭제
![채용공고 삭제](https://user-images.githubusercontent.com/107024591/174989914-467be210-0a61-4fc3-b380-45c01f0b205a.jpg)
* 채용공고 지원현황 목록(지원자_id:채용공고_id)
![채용공고_지원_현황_목록](https://user-images.githubusercontent.com/107024591/174989995-c2c0b269-8b16-4c89-8273-64259966c583.jpg)
                                 
