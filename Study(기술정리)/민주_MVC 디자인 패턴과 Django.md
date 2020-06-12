## MVC 디자인 패턴이란



### 디자인 패턴이란?

건축에서 유래(공법) 즉 소프트웨어 개발 방법을 공식화한 것. 뛰어난 엔지니어가 해결한 문제를 다수의 엔지니어가 처리할 수 있도록 한 규칙. 엔지니어들간의 커뮤니케이션을 높이는 기법

프로그램을 어떻게 짤 것인가? 디자인 할 것인가?

## MVC

애플리케이션을 세 가지 역할로 구분한 개발 방법론

https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/327/1262.png

사용자 시스템에게 명령 내리기(컨트롤러로 제어 시작) - 업데이트 - 결과 보여주기

모델: 데이터 핸들링

뷰: 시각적으로 보여주는 부분 핸들링

사용하는 목적: View 와 model사이에 controller을 두어 v / m의 의존성 제거(인터페이스간 의존성 제거)

그러나 현재 모델이 업데이트가 되면 view 도 업데이트 됨 -> MVP패턴

## 웹에서는

```
http://A4031ssafy.io/trade/detail/1
```



웹사이트 접속 - 컨트롤러가 모델 호출 - 모델은 데이터 소스 제어 후 결과 리턴 - 컨트롤러는 모델이 리턴한 결과를 뷰에 반영(업데이트) -  뷰가 보여짐

컨트롤러 : 사용자가 접근한 url에 따라 그 로직이 실행되도록 모델에 의뢰, 뷰 보여주기

모델: DB테이블 데이터 넘기기

뷰: html, css, javascript 등 클라이언트측 모아두기





# Django (object-relational mapping)

프레임워크의 핵심은 규칙이다!!!

ORM: 객체와 관계형 데이터베이스를 매핑하는 것, sql문을 이용할 필요가 없음

```
book_list = BookTable.query(author="ychaen")
```

장점: 간단하다, 코드가 줄어든다, 유지보수가 편하다, 코스를 재사용할 수 있다

단점: orm은 따로 배워야 한다, 큰 프로젝트에서는 sql문이 더 편할 수 있다



쿼리셋: 전달 받은 모델의 객체 목록

```
for e in Entry.objects.all():
    print(e.headline)
```

쿼리셋을 보여주기 위해 django orm을 이용하기, 장고를 데이터베이스에 연결

https://ychae-leah.tistory.com/135





## 모델

데이터에 대한 단 하나의 정보 소스

django.db.models.Model에 속한다

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)=
```

```
REATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

다대일 관계 정의하기 Foreign Key

```
class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
```

우리 플젝 trade, show

## 마이그래이션

모델에 생긴 변화를 반영하는 것, 데이터베이스 스키마를 위한 버전 관리 시스템(VCS)

makemigrations는 모델을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용합니다.

[`migrate`](https://docs.djangoproject.com/ko/3.0/ref/django-admin/#django-admin-migrate)  마이그레이션을 반영하거나 반영하지 않기 위해 사용합니다.





## 시리얼라이저 - Rest framework

웹 API를 만들려면 우선 Snippet 클래스의 인스턴스를 `json` 같은 형태로 직렬화(serializing)하거나 반직렬화(deserializing)할 수 있어야 합니다. Django REST 프레임워크에서는 Django 폼과 비슷한 방식으로 시리얼라이저를 작성합니다.

웹 API 통신을 위해서 Json형태로 만들기