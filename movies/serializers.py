from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        reviews = obj.reviews.all()

        # 1º Veirficar se há alguma avaliação, senão houver não faz sentindo entrar nesse if
        if reviews:
            # No caso de haver alguma avaliação, então tá na hora de fazer a contagem para saber quantas estrelas existe cada filme
            # Somando as avaliações
            sum_reviews = 0

            # Iterando sobre cada avaliação
            for review in reviews:
                sum_reviews += review.stars
            
            reviews_count = reviews.count()
            return round(sum_reviews / reviews_count, 1)
        
        return sum_reviews
        
        # Senão houver nenhuma avaliação, retorna direto um null de cara, nem perde tempo verficando
        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser mais do que 200 caracteres.')
        return value
