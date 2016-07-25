import datetime
import requests
import json

from .utils import URI_TIPAGOS


class BuyerTipagos:
    @staticmethod
    def create_payment(payment):
        body_json = BuyerTipagos.get_credit_card_json(payment)
        return BuyerTipagos.do_request(URI_TIPAGOS['create-payment-credit-card'], body_json)

    @staticmethod
    def create_billet(billet):
        today = datetime.date.today()
        due_date = datetime.datetime.strptime(str(billet.due_date), '%d%m%Y').date()

        if due_date <= today:
            due_date = today + datetime.timedelta(days=3)
            billet.due_date = due_date.strftime('%d%m%Y')

        body_json = BuyerTipagos.get_billet_json(billet)
        return BuyerTipagos.do_request(URI_TIPAGOS['create-payment-billet'], body_json)

    @staticmethod
    def create_account_pf(account):
        body_json = BuyerTipagos.get_account_pf_json(account)
        return BuyerTipagos.do_request(URI_TIPAGOS['create-account-pf'], body_json)

    @staticmethod
    def create_account_pj(account):
        body_json = BuyerTipagos.get_account_pj_json(account)
        return BuyerTipagos.do_request(URI_TIPAGOS['create-account-pj'], body_json)

    @staticmethod
    def do_request(url, body_json):
        r = requests.post(url, data=body_json, headers={'Content-type': 'application/json'})
        if r.status_code == 404:
            return False

        return json.loads(r.content)

    @staticmethod
    def get_account_pf_json(self):
        dict_from_payment = {
            "codigoProduto": self.product_code,
            "nome": self.name,
            "dataNascimento": self.birth_date,
            "sexo": self.gender,
            "documento": self.document,
            "rg": self.rg,
            "emissor": self.issuing,
            "dataEmissao": self.date_issue,
            "email": self.email,
            "emailSecundario": self.alternative_email,
            "nacionalidade": self.nationality,
            "estado": self.state,
            "ddiCelular": self.ddi,
            "dddCelular": self.ddd,
            "numeroCelular": self.phone_number,
            "operadora": self.mobile_operator,
            "tipoSo": self.os_type,
            "cepResidencial": self.residence_zip_code,
            "estadoResidencia": self.residence_state,
            "cidadeResidencia":self.residence_city,
            "bairroResidencia": self.residence_neighborhood,
            "logradouroResidencia": self.residence_address,
            "numeroResidencia": self.residence_number,
            "complemento": self.residence_complement,
            "ddiTelefoneResidencial": self.residence_ddi,
            "dddTelefoneResidencial": self.residence_ddd,
            "numeroTelefoneResidencial": self.residence_phone_number,
            "dddComercial": self.commercial_ddd,
            "telefoneComercial": self.commercial_phone_number,
            "ramalComercial": self.commercial_branch_line,
            "codBanco": self.bank_code,
            "agenciaBanco": self.bank_agency,
            "contaBanco": self.bank_account,
            "tpConta": self.bank_account_type,
            "documentoTitular": self.bank_document_holder,
            "ativarProtocolo": self.protocol_activation,
            "cadastroBasico": self.basic_register,
            "enviarEmail": self.send_email,
            "status": self.status
        }
        return json.dumps(dict_from_payment)

    @staticmethod
    def get_account_pj_json(self):
        dict_from_payment = {
            "codigoProduto": self.product_code,
            "nome": self.name,
            "dataNascimento": self.birth_date,
            "sexo": self.gender,
            "cpf": self.cpf,
            "rg": self.rg,
            "emissor": self.issuing,
            "dataEmissao": self.date_issue,
            "email": self.email,
            "estadoCivil": self.civil_state,
            "grauEscolar": self.education,
            "nomeMae": self.mother_name,
            "nomePai": self.father_name,
            "paisOrigem": self.nationality,
            "ddiCelular": self.ddi,
            "dddCelular": self.ddd,
            "numeroCelular": self.phone_number,
            "operadora": self.mobile_operator,
            "tipoSo": self.os_type,
            "cepResidencial": self.residence_zip_code,
            "estadoResidencia": self.residence_state,
            "cidadeResidencia": self.residence_city,
            "bairroResidencia": self.residence_neighborhood,
            "logradouroResidencia": self.residence_address,
            "numeroResidencia": self.residence_number,
            "complemento": self.residence_complement,
            "ddiTelefoneResidencial": self.residence_ddi,
            "dddTelefoneResidencial": self.residence_ddd,
            "numeroTelefoneResidencial": self.residence_phone_number,
            "dddComercial": self.commercial_ddd,
            "numeroTelefoneResidencial": self.commercial_phone_number,
            "razaoSocial": self.company_name,
            "nomeFantasia": self.trading_name,
            "cpfCnpjEmp": self.commercial_document,
            "dataConstituicao": self.commercial_open_date,
            "dddComercial": self.commercial_ddd,
            "telefoneComercial": self.commercial_phone_number,
            "ramalComercial": self.commercial_branch_line,
            "cepEmpr": self.commercial_zip_code,
            "estadoEmpr": self.commercial_state,
            "cidadeEmpr": self.commercial_city,
            "bairroEmpr": self.commercial_neighborhood,
            "logradouroEmpr": self.commercial_address,
            "numeroEmpr": self.commercial_number,
            "codBanco": self.bank_code,
            "agenciaBanco": self.bank_agency,
            "contaBanco": self.bank_account,
            "tpConta": self.bank_account_type,
            "nomeContaCorrente": self.bank_account_name,
            "vincularPlanos": self.plans_link,
            "receberCreditos": self.receiving_credits,
        }
        return json.dumps(dict_from_payment)

    @staticmethod
    def get_credit_card_json(self):
        dict_from_payment = {
            'header': dict(idLoja=self.id_store,
                           keyLoja=self.key_store,
                           codProduto=self.product_code
                           ),
            'tipoCapturaCliente': self.type_client_capture,
            'dadosCliente': self.data_client,
            'codSeguranca': self.security_code,
            'valor': self.value,
            'formaPagamento': self.form_of_payment,
            'qtdeParcelas': self.installments,
            'transacaoCapturada': self.captured_transaction,
            'descricaoPedido': self.order_description,
            'nsuTransacao': str(self.nsu_transaction),
            'split_value': str(self.split_value),
        }
        return json.dumps(dict_from_payment)

    @staticmethod
    def get_billet_json(billet):
        dict_from_billet = {
            "ddiCelular": billet.ddi,
            "dddCelular": billet.ddd,
            "numeroCelular": billet.phone_number,
            "codigoProduto": billet.product_code,
            "dataVencimento": billet.due_date,
            "valor": billet.value,
            "emailBoleto": billet.email,
            "ddiBoleto": billet.billet_ddi,
            "dddBoleto": billet.ddd,
            "numeroCelularBoleto": billet.phone_number,
            "sacadoEmBranco": billet.drawn_blank,
            "sacado": {
                "nome": billet.payer.name,
                "cpfCnpj": billet.payer.cpf_cnpj,
                "endereco": billet.payer.address,
                "bairro": billet.payer.neighborhood,
                "cidade": billet.payer.city,
                "cep": billet.payer.zipcode,
                "uf": billet.payer.state,
                "ddiTerceiro": billet.payer.ddi,
                "dddTerceiro": billet.payer.ddd,
                "numeroCelularTerceiro": billet.payer.phone_number
            }
        }

        return json.dumps(dict_from_billet)

    def __init__(self):
        pass
