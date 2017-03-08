""" . """
from rest_framework import serializers
from variant.models import (
    SNP,
    Indel,
    Annotation,
    Comment,
    Feature,
    Filter,
    Reference
)


class SNPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNP
        exclude = ('members',)


class InDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indel
        exclude = ('members',)


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference