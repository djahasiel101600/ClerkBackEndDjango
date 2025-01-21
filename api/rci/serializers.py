from rest_framework import serializers
from .models import ASDI_LFPS_DisbursmentVoucherRecord

class RCISerializer(serializers.HyperlinkedModelSerializer):
    check_no = serializers.IntegerField()
    class Meta:
        model = ASDI_LFPS_DisbursmentVoucherRecord
        fields = [
            'check_no',
            'dte',
            'no',
            'dv_no',
            'asa_no',
            'payee',
            'nature_of_transaction',
            'amountNetOfTax',
            'grossAmount',
        ]
        