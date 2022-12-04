from rest_framework import serializers
from .models import *
from fbrq_api.utils import serialize, serialize_list


class MailDisSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    phone_code = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = MailDis
        fields = "__all__"


class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = ('name',)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name',)



class MailDiscCreateSerializer(serializers.ModelSerializer):
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Tags.objects.all())
    # phone_code = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Codes.objects.all())
    # tags = TagsSerializer(many=True)
    # phone_code = CodesSerializer(many=True)
    tags = serializers.ListField()
    phone_code = serializers.ListField()
    class Meta:
        model = MailDis
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        t = [serialize(TagsSerializer, 'name', data={'name': m}) for m in validated_data.pop('tags')]
        p = [serialize(CodesSerializer, 'name', data={'name': m}) for m in validated_data.pop('phone_code')]
        start_time = validated_data.pop('start_time')
        mes = validated_data.pop('mes')
        end_time = validated_data.pop('end_time')
        disc = MailDis.objects.create(start_time=start_time, mes=mes, end_time=end_time)
        disc.tags.add(*t)
        disc.phone_code.add(*p)

        return disc
