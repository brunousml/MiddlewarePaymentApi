# choices Fields
TYPE_CLIENT_CAPTURE = (
    ('3', 'credit_card_not_cryptography'),
)

TYPE_OF_CIVIL_STATE = (
    ('1', 'unmarried'),
    ('2', 'married'),
    ('3', 'divorced'),
    ('4', 'widower'),
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

TYPE_OF_EDUCATION = (
    ('1', 'incomplete_primary_school'),
    ('2', 'complete_primary_school'),
    ('3', 'incomplete_high_school'),
    ('4', 'complete_high_school'),
    ('5', 'incomplete_third_school'),
    ('6', 'complete_third_school'),
)

MOBILE_OPERATORS = (
    ('1', 'claro'),
    ('2', 'vivo'),
    ('3', 'tim'),
    ('4', 'nextel'),
    ('5', 'br_telecon'),
    ('6', 'oi'),
    ('99', 'other'),
)

OS_TYPE = (
    ('1', 'Android'),
    ('2', 'BlackBerry'),
    ('3', 'IPhone'),
    ('4', 'Windows Phone'),
    ('5', 'Symbian'),
    ('6', 'other'),
)


FORM_OF_PAYMENT = (
    ('1', 'in_cash'),
    ('2', 'installments_without_interest'),
    ('3', 'installments_with_interest'),
)

# Setup URIs TIPAGOS
URI_TIPAGOS = {
    'create-payment-credit-card': 'http://example.com',
    'create-payment-billet': 'http://example.com',
    'create-account-pf': 'http://example.com',
    'create-account-pj': 'http://example.com',

}
