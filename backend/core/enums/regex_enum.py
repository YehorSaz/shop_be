from enum import Enum


class RegExEnum(Enum):
    NAME_SURNAME = (
        r'^(?!.*[эЭыЫ])[А-яіІїЇґҐєЄ-]{2,50}$',
        [
            'Only Ukrainian letters or "-"',
            'min 2 characters',
            'max 50 characters',
        ]
    )

    PHONE = (
        r'^(38)?0\d{9}$',
        'only numbers, example: 380xxxxxxxxx, 0xxxxxxxxx'

    )

    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])\S{8,30}$',
        [
            'min 1 lowercase ch',
            'min 1 uppercase ch',
            'min 1 digit',
            'min 1 special character',
            'length 8-30'
        ]
    )

    COURSE_NAME = (
        r'^[a-zA-Z]{2,20}$',
        'Only latin letters min 2 max 20 ch'
    )

    MODULE_NAME = (
        r'^[a-zA-Z]{2,11}$',
        'Only latin letters min 2 max 11 ch'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
