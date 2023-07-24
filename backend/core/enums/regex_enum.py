from enum import Enum


class RegExEnum(Enum):
    NAME_SURNAME = (
        r'^(?:(?!.*[эЭыЫ]))[А-яіІїЇґҐєЄ-]{2,50}$',
        [
            'Only Ukrainian letters or "-"',
            'min 2 characters',
            'max 50 characters',
        ]
    )

    PHONE = (
        r'^\d{12}$',
        'Only numbers, 12 numbers'

    )

    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=(?:.*[`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]))[a-zA-Z\d`~!@#$%^&*('
        r')\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]{8,30}$',
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
        'Only letters min 2 max 20 ch'
    )
    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
