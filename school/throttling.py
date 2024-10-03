from rest_framework.throttling import AnonRateThrottle

class RegisteredAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'