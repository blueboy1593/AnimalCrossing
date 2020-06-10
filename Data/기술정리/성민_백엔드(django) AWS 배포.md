# 백엔드(django) AWS 배포



http://k02a4031.p.ssafy.io



### 그룹 권한 설정하기

putty 접속 후, 그룹 계정 설정

```bash
sudo groupadd djangogroup
sudo useradd -g djangogroup -b /home -m -s /bin/bash django
```

나는 /var/www/animalcrossing 에다가 소스코드를 올렸다.

```bash
sudo mkdir -p /var/www/animalcrossing
```

해당  폴더에 django 유저와 djangogroup 그룹에 소유권을 설정. choose owner

```
sudo chown django:djangogroup /var/www/animalcrossing
```

ubuntu유저를 djangogroup에 추가.

```bash
sudo usermod -a -G djangogroup ubuntu
```

animalcrossing 폴더 쓰기 권한을 그룹에 속한 모든 유저에게 부여.

```bash
sudo chmod g+w /var/www/animalcrossing
```



### 패키지 설치

필요한 라이브러리.. 왜필요한지는 모르겠다.. 일단 설치하라 해서 했음.

```
sudo apt-get install build-essential libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libssl-dev
```



파이썬 관련 라이브러리 설치

```
sudo apt-get install python3-dev python3-pip python3-cffi python3-venv
```



### 소스코드 업로드

기존 django에서 라이브러리를 추출한다.

```bash
$ pip freeze > requirements.txt
```

django 프로젝트의 settings.py 설정을 변경

animal/settings.py

```python
DEBUG = False
ALLOWED_HOSTS = ["*"]
```



그다음 filezila를 활용하여 소스코드(requirements.txt 포함)를  /var/www/animalcrossing 에 업로드한다.

venv 폴더는 제외하고 업로드한다!



### 파이썬 가상환경 설정

업로드 폴더로 이동.

```bash
cd /var/www/animalcrossing
```

venv 모듈을 이용해 venv라는 경로에 가상환경을 만든다.

```bash
sudo python3 -m venv venv
```

관리자 상태로 변경(권한설정)

```bash
sudo -s
```

가상환경 활성화 (venv) 표시 생기면 활성화 된거임! 끄는건 deactivate

```bash
source venv/bin/activate
```



업로드한 requirements.txt 를  이용해서 모듈들을 설치한다.

```bash
pip install -r requirements.txt
```



프로젝트 실행

```
python manage.py runserver # 테스트해본다.
```

실행이 확인되었으면 끄고, static파일을 모아준다.

```bash
python manage.py collectstatic # 실행하면 static폴더에 모아진다. swagger 사용시에 꼭 해줘야함!! 얘네도 static임
```





여기서부터 두가지 방법이 있는데 

1. uWSGI 미들웨어
2. gunicorn 미들웨어

지영이의 조언에 따르면, uwsgi는 소켓 연결인데 싸피 사무국측에서 이러한 통신을 막아둬서 잘 안되는거 같다고 해서

gunicorn을 사용했다.

책엔 uwsgi로 진행하였는데, 따라해보니 이유를 모르겠지만 그냥 안됨... 내가 제대로 못했을 수도....



## gunicorn 설치

gunicorn 설치

```
pip install gunicorn
```

프로젝트 폴더로 이동해서 실행시킨다.


```bash
cd /var/www/animalcrossing
gunicorn --bind 0.0.0.0:8000 animal.wsgi:application #animal은 프로젝트 이름.
# 위 명령은 python manage.py runserver 와 같은 의미라 생각하면 된다.
```

다음 명령으로 구동 중인지 확인

```
ps -ef | grep news
```



### 서비스 등록 스크립트 생성

/etc/systemd/system/gunicorn.service 파일을 아래와 같은 내용으로 생성.

```
cd /etc/systemd/system/
sudo vim gunicorn.service
```



```nginx
[Unit]
Description=gunicorn daemon
After=network.target


[Service]
User=django # 기본값은 ubuntu로 하면 된다고 한다. 나는 위에서 설정했기때문에 이렇게함.
Group=djangogroup
WorkingDirectory=/var/www/animalcrossing # 프로젝트 경로
ExecStart=/var/www/animalcrossing/venv/bin/gunicorn \ # gunicorn이 깔린 경로. venv
        --workers 5 \ # 프로세스 갯수 같다.
        --bind 127.0.0.1:8000 \ # django 애플리케이션 서버 주소
        animal.wsgi:application

[Install]
WantedBy=multi-user.target
```



#### GuniCorn 서비스 등록

```bash
sudo systemctl start gunicorn # 실행
sudo systemctl enable gunicorn # 등록?
systemctl status gunicorn # 현재 정보 확인
```



### Nginx (웹서버) 

프론트와 같다.

```bash
sudo apt install nginx
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
cd /etc/nginx/sites-available/
sudo touch myapp.conf
sudo vi myapp.conf 
```

처음에는 conf 파일을 두개 만들어서 각각 run 시키는 줄 알았는데 아니었다.. 하나의 파일에 두개의 server를 등록하는것!!

프론트에서 만든 myapp.conf를 다음과 같이 수정한다.

```nginx

server {
  listen 80; ## 기본주소:80으로 접속하면 프론트
        listen [::]:80;
  root   "/home/ubuntu/dist";
  index  index.html;
  location / {
    try_files $uri $uri/ /index.html;

  }
}
server{
        listen 8001; # 기본주소:8001로 접속하면 백엔드
        charset utf-8;
    location /static/ {
                root /var/www/animalcrossing/; # 프로젝트 위치. swagger도 static파일을 사용하기 때문에 넣어줘야 한다.
    }
    location / {
    include proxy_params;
    proxy_pass http://127.0.0.1:8000; ## 위에서 설정한 django 앱서버 주소.
    }
    error_page 404 = /error_404.html;

}

```



심볼릭 링크를 site-enabled에 작성.

 ln -s 기능을 사용하여 sites-enabled에 연동시켜준다고 생각하면 된다. 

sites-available/ 여기에 저장된건 실제 nginx에 반영 X

```bash
sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
```



nginx 실행

```bash
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl status nginx
```





#### 참고자료

NGinx, gunicorn 배포: https://wikidocs.net/6601

Python WAS 구축: http://dveamer.github.io/backend/PythonWAS.html

심볼릭 링크 관련 :https://forteleaf.tistory.com/entry/nginx-site-enabled-site-availablemd



요청 -> 웹서버(k~)