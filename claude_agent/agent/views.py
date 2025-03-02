from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime
import mimetypes
import os
from .models import Document, Analysis
from .serializers import DocumentSerializer, AnalysisSerializer
from .services import ClaudeService

# Create your views here.

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def perform_create(self, serializer):
        file = self.request.FILES.get('file')
        file_name = file.name
        mime_type, _ = mimetypes.guess_type(file_name)
        
        # Определение типа файла по расширению, если mime_type не определен
        if not mime_type:
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension == '.txt':
                mime_type = 'text/plain'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'
            elif file_extension == '.docx':
                mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            elif file_extension == '.xlsx':
                mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            elif file_extension == '.csv':
                mime_type = 'text/csv'
            elif file_extension == '.json':
                mime_type = 'application/json'
            elif file_extension == '.mp3':
                mime_type = 'audio/mpeg'
            elif file_extension == '.wav':
                mime_type = 'audio/wav'
            elif file_extension == '.ogg':
                mime_type = 'audio/ogg'
            elif file_extension == '.m4a':
                mime_type = 'audio/m4a'
            elif file_extension == '.flac':
                mime_type = 'audio/flac'
            else:
                mime_type = 'application/octet-stream'
        
        # Записываем тип в консоль для диагностики
        print(f"Загружен файл: {file_name}, тип: {mime_type}")
        
        serializer.save(file_type=mime_type)

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    
    def perform_create(self, serializer):
        analysis = serializer.save(status='pending')
        self.run_analysis(analysis)
        
    def run_analysis(self, analysis):
        try:
            # Update status to processing
            analysis.status = 'processing'
            analysis.save()
            
            # Get documents
            documents = analysis.documents.all()
            
            if not documents:
                analysis.status = 'failed'
                analysis.result = "No documents provided for analysis"
                analysis.save()
                return
            
            # Process documents with Claude
            claude_service = ClaudeService()
            result = claude_service.compare_documents(
                documents=documents,
                custom_prompt=analysis.custom_prompt
            )
            
            # Update analysis with results
            analysis.result = result
            analysis.status = 'completed'
            analysis.completed_at = datetime.now()
            analysis.save()
            
        except Exception as e:
            analysis.status = 'failed'
            analysis.result = f"Analysis failed: {str(e)}"
            analysis.save()
    
    @action(detail=True, methods=['post'])
    def retry(self, request, pk=None):
        analysis = self.get_object()
        analysis.status = 'pending'
        analysis.result = None
        analysis.completed_at = None
        analysis.save()
        
        self.run_analysis(analysis)
        return Response(self.get_serializer(analysis).data)
