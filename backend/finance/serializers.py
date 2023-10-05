from rest_framework import serializers

from .models import Finance


class FinanceSerializer(serializers.ModelSerializer):
    repository = serializers.StringRelatedField(many=False)

    class Meta:
        model = Finance
        fields = "__all__"

    def validate(self, attrs):
        request = self.context.get("request")

        symbol = request.query_params.get("symbol", None)
        year = request.query_params.get("year", None)

        if not symbol or not year:
            raise serializers.ValidationError("symbol and year are required")

        return super().validate(attrs)
