import re
from validate_docbr import CPF


def invalid_cpf(cpf_number):
    cpf = CPF()
    is_cpf_validate = cpf.validate(cpf_number)
    return not is_cpf_validate

def name_not_alpha(name):
    return not name.isalpha()

def invalid_phone_number(phone_number):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phone_number)

    return not response