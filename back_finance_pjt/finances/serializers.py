from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)


class DepositProductsSerializer(serializers.ModelSerializer):
    # deposit_options = DepositOptionsSerializer(many=True, read_only=True)
    intr_rate_type_nm = serializers.SerializerMethodField()
    term_6 = serializers.SerializerMethodField()
    term_12 = serializers.SerializerMethodField()
    term_24 = serializers.SerializerMethodField()
    term_36 = serializers.SerializerMethodField()
    class Meta():
        model = DepositProducts
        fields = '__all__'

    def get_intr_rate_type_nm(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        intr_rate_type_nm = obj.deposit_options.filter(fin_prdt_cd=fin_prdt_cd)[0].intr_rate_type_nm
        return intr_rate_type_nm
    def get_term_6(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.deposit_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=6)) > 1:
            tmp = []
            for item in options.filter(save_trm=6):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=6).intr_rate2 if len(options.filter(save_trm=6)) > 0 else "-"
            return rate
    def get_term_12(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.deposit_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=12)) > 1:
            tmp = []
            for item in options.filter(save_trm=12):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=12).intr_rate2 if len(options.filter(save_trm=12)) > 0 else "-"
            return rate
    def get_term_24(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.deposit_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=24)) > 1:
            tmp = []
            for item in options.filter(save_trm=24):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=24).intr_rate2 if len(options.filter(save_trm=24)) > 0 else "-"
            return rate
    def get_term_36(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.deposit_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=36)) > 1:
            tmp = []
            for item in options.filter(save_trm=36):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=36).intr_rate2 if len(options.filter(save_trm=36)) > 0 else "-"
            return rate


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)


class SavingProductsSerializer(serializers.ModelSerializer):
    # saving_options = SavingOptionsSerializer(many=True, read_only=True)
    intr_rate_type_nm = serializers.SerializerMethodField()
    term_6 = serializers.SerializerMethodField()
    term_12 = serializers.SerializerMethodField()
    term_24 = serializers.SerializerMethodField()
    term_36 = serializers.SerializerMethodField()
    class Meta():
        model = SavingProducts
        fields = '__all__'
    
    def get_intr_rate_type_nm(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        # print(fin_prdt_cd)
        intr_rate_type_nm = obj.saving_options.filter(fin_prdt_cd=fin_prdt_cd)[0].intr_rate_type_nm
        return intr_rate_type_nm
    def get_term_6(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.saving_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=6)) > 1:
            tmp = []
            for item in options.filter(save_trm=6):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            print(tmp)
            return max(tmp)
        else:
            rate = options.get(save_trm=6).intr_rate2 if len(options.filter(save_trm=6)) > 0 else "-"
            return rate
    def get_term_12(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.saving_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=12)) > 1:
            tmp = []
            for item in options.filter(save_trm=12):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=12).intr_rate2 if len(options.filter(save_trm=12)) > 0 else "-"
            return rate
    def get_term_24(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.saving_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=24)) > 1:
            tmp = []
            for item in options.filter(save_trm=24):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=24).intr_rate2 if len(options.filter(save_trm=24)) > 0 else "-"
            return rate
    def get_term_36(self, obj):
        fin_prdt_cd = obj.fin_prdt_cd
        options = obj.saving_options.filter(fin_prdt_cd=fin_prdt_cd)
        if len(options.filter(save_trm=36)) > 1:
            tmp = []
            for item in options.filter(save_trm=36):
                rate = item.intr_rate2
                if rate:
                    tmp.append(rate)
            return max(tmp)
        else:
            rate = options.get(save_trm=36).intr_rate2 if len(options.filter(save_trm=36)) > 0 else "-"
            return rate