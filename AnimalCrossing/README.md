# README

## Backend Local 실행

```bash
# 얘는 venv가 없을때만 해주면 됨
python -m venv venv

# 가상환경 실행
source venv/Script/activate

# pip등 깔려있지 않을 때
pip list # 하고 나오는 upgrage 복사해서 하기

# requirements에 저장된 것들 설치
pip install -r requirements.txt

# 백엔드 쟝고 실행
python manage.py runserver
```

## Frontend Local 실행

```bash
# module 새로 추가된 것 있으면 설치
npm install

# 실행
npm run serve
```

