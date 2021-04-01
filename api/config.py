# encoding: utf-8

class Config:
    HOST = 'https://rest.selleractive.com'


class BeenimaxConfig(Config):
    USERNAME = 'admin@beenimax.com'
    PASSWORD = 'HrhHadj174$'
    SELLER_ID = '9913'
    API_KEY = 'X254WXUIBW5WR94WM11AUB2AYGSAG1ZKUVABPVL2C1EREC289KJ35YJWA5EQETCL'


class WideStepConfig(Config):
    USERNAME = 'info@wdstp.com'
    PASSWORD = 'TwQ#BRNcFYsOBJ9bS#D6'
    SELLER_ID = '9043'
    API_KEY = 'QTNDCKYNWFY7JJKPBEICMFVPH3UX8T0R6PR2A24P06S75375N7PWNJ9L887J1APC'


CONFIGS = dict(
    bnm=BeenimaxConfig,
    beenimax=BeenimaxConfig,
    wdstp=WideStepConfig,
    wide_step=WideStepConfig
)

