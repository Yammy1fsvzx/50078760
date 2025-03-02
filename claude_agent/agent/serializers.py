from rest_framework import serializers
from .models import Document, Analysis

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'name', 'file_type', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at', 'file_type']

class AnalysisSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)
    document_ids = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True
    )
    
    class Meta:
        model = Analysis
        fields = ['id', 'documents', 'document_ids', 'custom_prompt', 'result', 'created_at', 'completed_at', 'status']
        read_only_fields = ['id', 'result', 'created_at', 'completed_at', 'status']
    
    def create(self, validated_data):
        document_ids = validated_data.pop('document_ids')
        analysis = Analysis.objects.create(**validated_data)
        analysis.documents.set(Document.objects.filter(id__in=document_ids))
        return analysis 