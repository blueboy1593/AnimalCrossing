# 프론트엔드 AWS 배포하기

1. aws에 putty로 접속한다.

2. nginx를 설치한다!! 이건 웹서버

```bash
   sudo apt install nginx
   sudo rm /etc/nginx/sites-available/default
   sudo rm /etc/nginx/sites-enabled/default
   cd /etc/nginx/sites-available/
   sudo touch myapp.conf
```

```bash
sudo vi myapp.conf # sudo 명령어 안치면 수정 안됨!
```

myapp.conf 파일 내부를 다음과 같이 수정한다.

```
server {
  listen 80;
	listen [::]:80;
  root   "/home/ubuntu/dist"; 
  index  index.html;
  location / { 
    try_files $uri $uri/ /index.html;
   
  }
}

```

심볼릭 링크를 sites-enabled에 작성

```bash
sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
```

nginx 실행

```
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

![image-20200529180759813](C:\Users\qwes1\AppData\Roaming\Typora\typora-user-images\image-20200529180759813.png)

이렇게 나오면 성공함!

그다음 npm run build 결과물 (Dist)  폴더를 Filezila로 /home/ubuntu/에 옮기면 끝!