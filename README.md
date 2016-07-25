# TIPAGOS API INTEGRATION
This project provides a  sample of middleware integration with TIPAGOS API to create payment, billets and more.

# Setup Application

## You need some software before installation

### Install git, pip, virtualenv and virtualenvwrapper

    $ sudo apt-get install git
    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv
    $ mkdir ~/.virtualenvs
    $ sudo pip install virtualenvwrapper

Setup virtualenvwrapper in ~/.bashrc
       
    # Create a backup of your .bashrc file
    cp ~/.bashrc ~/.bashrc-org
    
    # Be careful with this command
    printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
    'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc


## Create and set virtual env

    $ mkvirtualenv payment
    $ workon payment

## Install Django

    sudo apt-get install python-django

## Install requirements
    
    pip install -r requirements.txt
    
## Make migrations and runserver
    
    ./manage.py makemigrations && ./manage.py migrate && ./manage.py runserver

...and enjoy the requests with postman https://www.getpostman.com/


For more information about the cloud servers to python web applications here:
https://www.digitalocean.com/community/tutorials/how-to-set-up-ubuntu-cloud-servers-for-python-web-applications

# Resources

### Example of syntax suggested  for tastypie to call api through Ajax
        var data = JSON.stringify({
            "body": "This will prbbly be my lst post.",
            "pub_date": "2011-05-22T00:46:38",
            "slug": "another-post",
            "title": "Another Post"
        });
        
        $.ajax({
          url: 'http://104.236.47.168:8000/api/v1/payment/',
          type: 'POST',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          processData: false
        })


## Payment Resource

### Payment Fields:

    GET api/v1/payment/schema/?format=json
    
    Response:
    {
      "allowed_detail_http_methods": [
        "get",
        "post"
      ],
      "allowed_list_http_methods": [
        "get",
        "post"
      ],
      "default_format": "application/json",
      "default_limit": 20,
      "fields": {
        "authorization_code": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "authorization code"
        },
        "captured_transaction": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "captured transaction"
        },
        "data_client": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "data client"
        },
        "flag_code": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "flag code"
        },
        "form_of_payment": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "form of payment"
        },
        "id": {
          "blank": true,
          "default": "",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": true,
          "readonly": false,
          "type": "integer",
          "unique": true,
          "verbose_name": "ID"
        },
        "id_store": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "id store"
        },
        "installments": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "installments"
        },
        "key_store": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "key store"
        },
        "nsu_tipagos": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "nsu tipagos"
        },
        "nsu_transaction": {
          "blank": false,
          "default": "aa60563c-9319-41a4-a437-3bbb8e393395",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": true,
          "verbose_name": "nsu transaction"
        },
        "order_description": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "order description"
        },
        "product_code": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "product code"
        },
        "resource_uri": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": true,
          "type": "string",
          "unique": false,
          "verbose_name": "resource uri"
        },
        "security_code": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "security code"
        },
        "split_value": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "split value"
        },
        "type_client_capture": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "type client capture"
        },
        "value": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "value"
        }
      }
    }

### Billet Fields:

    GET api/v1/payment/schema/?format=json
    
    Response:
    {
      "allowed_detail_http_methods": [
        "get",
        "post"
      ],
      "allowed_list_http_methods": [
        "get",
        "post"
      ],
      "default_format": "application/json",
      "default_limit": 20,
      "fields": {
        "base64": {
          "blank": false,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "base64"
        },
        "billet_ddd": {
          "blank": false,
          "default": 21,
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "billet ddd"
        },
        "billet_ddi": {
          "blank": false,
          "default": 55,
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "billet ddi"
        },
        "billet_phone_number": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "billet phone number"
        },
        "ddd": {
          "blank": false,
          "default": 21,
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "ddd"
        },
        "ddi": {
          "blank": false,
          "default": 55,
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "ddi"
        },
        "digits": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "digits"
        },
        "drawn_blank": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "drawn blank"
        },
        "due_date": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "due date"
        },
        "email": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "email"
        },
        "id": {
          "blank": true,
          "default": "",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": true,
          "readonly": false,
          "type": "integer",
          "unique": true,
          "verbose_name": "ID"
        },
        "payer": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
          "nullable": true,
          "primary_key": false,
          "readonly": false,
          "related_schema": "/api/v1/payer_of_billet/schema/",
          "related_type": "to_one",
          "type": "related",
          "unique": false,
          "verbose_name": "payer"
        },
        "phone_number": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "phone number"
        },
        "product_code": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "product code"
        },
        "resource_uri": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": true,
          "type": "string",
          "unique": false,
          "verbose_name": "resource uri"
        },
        "tipagos_code": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "tipagos code"
        },
        "value": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "value"
        }
      }
    }
    
### Error Field

    Response:
    {
      "allowed_detail_http_methods": [
        "get"
      ],
      "allowed_list_http_methods": [
        "get"
      ],
      "default_format": "application/json",
      "default_limit": 20,
      "fields": {
        "authorization_code": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "authorization code"
        },
        "cancel_code_authorization": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "cancel code authorization"
        },
        "description": {
          "blank": true,
          "default": "",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "string",
          "unique": false,
          "verbose_name": "description"
        },
        "id": {
          "blank": true,
          "default": "",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": true,
          "readonly": false,
          "type": "integer",
          "unique": true,
          "verbose_name": "ID"
        },
        "rc": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Integer data. Ex: 2673",
          "nullable": false,
          "primary_key": false,
          "readonly": false,
          "type": "integer",
          "unique": false,
          "verbose_name": "rc"
        },
        "resource_uri": {
          "blank": false,
          "default": "No default provided.",
          "help_text": "Unicode string data. Ex: \"Hello World\"",
          "nullable": false,
          "primary_key": false,
          "readonly": true,
          "type": "string",
          "unique": false,
          "verbose_name": "resource uri"
        }
      }
    }