def solution(chicken):
    service_chicken = 0
    while chicken >= 10:
        # 10장의 쿠폰으로 서비스 치킨 받기
        service_chicken += chicken // 10
        # 서비스 치킨 받고 남은 쿠폰과 서비스 치킨으로 받은 쿠폰 합산
        chicken = chicken // 10 + chicken % 10
    return service_chicken

def solution(chicken):
    return int(chicken*0.11111111111)