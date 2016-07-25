from tastypie.resources import ModelResource
from tastypie import fields
from .models import Payment, Error, Billet, PayerOfBillet, Account
from tastypie.authorization import Authorization


class ErrorResource(ModelResource):
    class Meta:
        queryset = Error.objects.all()
        resource_name = 'error'
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True


class PaymentResource(ModelResource):
    error = fields.ForeignKey(ErrorResource, 'error', null=True, full=True)

    class Meta:
        queryset = Payment.objects.all()
        resource_name = 'payment'
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        always_return_data = True


class PayerOfBilletResource(ModelResource):
    class Meta:
        queryset = PayerOfBillet.objects.all()
        resource_name = 'payer_of_billet'
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True


class BilletResource(ModelResource):
    error = fields.ForeignKey(ErrorResource, 'error', null=True, full=True)
    payer = fields.ToOneField(PayerOfBilletResource, 'payer', null=True)

    class Meta:
        queryset = Billet.objects.all()
        resource_name = 'billet'
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        always_return_data = True


class AccountResource(ModelResource):
    error = fields.ForeignKey(ErrorResource, 'error', null=True, full=True)

    class Meta:
        queryset = Account.objects.all()
        resource_name = 'account'
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        always_return_data = True
