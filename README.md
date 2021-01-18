# 사용법
```bash
python3 -m pip install --no-cache-dir requirements.txt
```

패키지 설치

---

```bash
python3 -c "import imdb_learn; imdb_learn.learning_imdb().create_model()"
```

위의 명령어를 이용하여 .h5 모델을 제작

---

```bash
flask run --port=8080 --host=0.0.0.0
```

웹서비스 시작

---
# features

## 3

imdb 리뷰를 Flask 웹 서비스를 통해 입력값을 받아오고 같은지 확인후 부정, 긍정 확률을 출력

## 2

imdb_learn.py 파일을 클래스화

---

## 1

flask를 활용하여 데이터를 송수신

---

## 0

함수에 데이터 값을 넣고 긍정적 리뷰 혹은 부정적 리뷰를 판결
