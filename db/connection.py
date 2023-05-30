# 데이터베이스 사용 방법

# 1. connection 맺기 (DB ~~~~~~~~Python 프로그램)
# - IP      : 컴퓨터 주소
# - Port    : 27017
# - ID & PW : 계정 정보
# 2. 명령 보내기(python ~~~~~~→ DB)
# 3. 결과 받기 (Python ←~~~~~~ DB)
# 4. connection 끊기 (Python XXXXX DB)

from pymongo import MongoClient


# MongoDB conncection
def conn():
    client = MongoClient("mongodb+srv://cnu:cnu1234@chaeyeon.peaa4pa.mongodb.net/")  # IP, Port, ID&PW
    db = client["movie"]

    collection = db.get_collection("movie")
    return collection
