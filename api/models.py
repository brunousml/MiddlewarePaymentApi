# coding=utf-8
import uuid
import tipagos

from django.db import models
from utils import *


class Error(models.Model):
    rc = models.IntegerField()
    description = models.CharField(blank=True, max_length=255)
    authorization_code = models.CharField(blank=True, max_length=255)
    cancel_code_authorization = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return self.description


class Payment(models.Model):
    error = models.ForeignKey(Error, on_delete=models.CASCADE, null=True)

    id_store = models.CharField(max_length=255)
    key_store = models.CharField(blank=True, max_length=255)
    product_code = models.CharField(max_length=255)

    type_client_capture = models.CharField(choices=TYPE_CLIENT_CAPTURE, max_length=1)
    data_client = models.CharField(max_length=255)
    security_code = models.CharField(blank=True, max_length=255)

    value = models.IntegerField()
    form_of_payment = models.CharField(choices=FORM_OF_PAYMENT, max_length=255)
    installments = models.IntegerField()

    captured_transaction = models.CharField(max_length=255)
    order_description = models.CharField(blank=True, max_length=255)
    authorization_code = models.CharField(max_length=255)

    nsu_tipagos = models.CharField(max_length=255)
    nsu_transaction = models.CharField(max_length=255, unique=True, editable=False, default=uuid.uuid4)

    flag_code = models.CharField(max_length=255, blank=True)
    split_value = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return self.nsu_transaction

    def hide_sensitive_data(self):
        list_of_characters = list(self.data_client)
        initial = self.data_client.index(';')
        final = self.data_client.rfind(';')

        for number in reversed(list(enumerate(list_of_characters))):
            number = number[0]
            if number > initial:
                if number >= final:
                    list_of_characters[number] = ""
                elif number < (final - 4):
                    list_of_characters[number] = "*"

        self.data_client = "".join(list_of_characters)

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)

        response = tipagos.BuyerTipagos.create_payment(self)
        # Created with success
        if response.has_key('nsuTipagos'):
            self.nsu_tipagos = response['nsuTipagos']
            self.authorization_code = response['codAutorizacao']
            self.hide_sensitive_data()

        # Related error
        if response.has_key('retorno') and response['retorno'].has_key('rc') and response['retorno']['rc'] != 0:
            error = Error.objects.create(
                rc=response['retorno']['rc'],
                description=response['retorno']['descErro']
            )
            self.error = error

        super(Payment, self).save(*args, **kwargs)


class PayerOfBillet(models.Model):
    name = models.CharField(max_length=100)
    cpf_cnpj = models.IntegerField()
    address = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=2)
    ddi = models.IntegerField()
    ddd = models.IntegerField()
    phone_number = models.IntegerField()


class Billet(models.Model):
    payer = models.ForeignKey(PayerOfBillet, on_delete=models.CASCADE, null=True)
    error = models.ForeignKey(Error, on_delete=models.CASCADE, null=True)

    ddi = models.IntegerField(default=55)
    ddd = models.IntegerField(default=21)
    phone_number = models.IntegerField()

    product_code = models.IntegerField()
    due_date = models.CharField(max_length=8)  # minimum due_date is (today + 3 days)
    value = models.CharField(max_length=255)

    email = models.CharField(max_length=30)
    billet_ddi = models.IntegerField(default=55)
    billet_ddd = models.IntegerField(default=21)
    billet_phone_number = models.IntegerField()

    drawn_blank = models.CharField(max_length=5)

    tipagos_code = models.CharField(max_length=100)
    base64 = models.TextField()
    digits = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        response = tipagos.BuyerTipagos.create_billet(self)
        if response.has_key('codigoRetorno') and response['codigoRetorno'] == 0:
            self.base64 = response['base64']
            self.digits = response['linhaDigitavel']
            self.tipagos_code = response['nossoNumero']
        else:
            error = Error.objects.create(
                rc=response['codigoRetorno'],
                description=response['descricaoRetorno']
            )
            self.error = error

        super(Billet, self).save(*args, **kwargs)


class Account(models.Model):
    error = models.ForeignKey(Error, on_delete=models.CASCADE, null=True)

    # TIPAGOS Fields
    product_code = models.IntegerField(default=99)

    # User Fields
    name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER)

    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=22)
    issuing = models.CharField(max_length=6)
    date_issue = models.CharField(max_length=10)

    email = models.CharField(max_length=40)
    civil_state = models.CharField(max_length=1, choices=TYPE_OF_CIVIL_STATE, default=TYPE_OF_CIVIL_STATE[0])
    education = models.CharField(max_length=1, choices=TYPE_OF_EDUCATION)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    nationality = models.IntegerField(default=76)

    ddi = models.IntegerField()
    ddd = models.IntegerField()
    phone_number = models.IntegerField()

    mobile_operator = models.CharField(max_length=1, choices=MOBILE_OPERATORS)
    os_type = models.CharField(max_length=1, choices=OS_TYPE)

    # Residential Fields
    residence_zip_code = models.IntegerField()
    residence_state = models.CharField(max_length=2)
    residence_city = models.CharField(max_length=100)
    residence_neighborhood = models.CharField(max_length=100)
    residence_address = models.CharField(max_length=100)
    residence_number = models.CharField(max_length=5)
    residence_complement = models.CharField(max_length=100)
    residence_ddi = models.IntegerField()
    residence_ddd = models.IntegerField()
    residence_phone_number = models.IntegerField()

    # Commercial Fields
    company_name = models.CharField(max_length=100)
    trading_name = models.CharField(max_length=100)
    commercial_document = models.CharField(max_length=20)
    commercial_open_date = models.CharField(max_length=10)
    commercial_ddd = models.IntegerField()
    commercial_phone_number = models.IntegerField()
    commercial_branch_line = models.IntegerField(default=00)
    commercial_zip_code = models.IntegerField()
    commercial_state = models.CharField(max_length=2)
    commercial_city = models.CharField(max_length=100)
    commercial_neighborhood = models.CharField(max_length=100)
    commercial_address = models.CharField(max_length=100)
    commercial_number = models.CharField(max_length=5)

    # Bank Fields
    bank_code = models.CharField(max_length=4)
    bank_agency = models.CharField(max_length=9)
    bank_account = models.CharField(max_length=9)
    bank_account_type = models.CharField(max_length=1)
    bank_account_name = models.CharField(max_length=100)
    bank_document_holder = models.IntegerField()

    # Default Fields
    plans_link = models.CharField(max_length=5, default='true')
    receiving_credits = models.CharField(max_length=5, default="true")

    def save(self, *args, **kwargs):
        response = tipagos.BuyerTipagos.create_account_pj(self)
        if response['codigoRetorno'] != 0:
            error = Error.objects.create(
                rc=response['codigoRetorno'],
                description=response['descricaoRetorno']
            )
            self.error = error

        super(Account, self).save(*args, **kwargs)
