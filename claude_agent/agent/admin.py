from django.contrib import admin
from .models import Document, Analysis

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_type', 'uploaded_at')
    list_filter = ('file_type', 'uploaded_at')
    search_fields = ('name',)
    date_hierarchy = 'uploaded_at'

@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'completed_at', 'document_count')
    list_filter = ('status', 'created_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('id', 'created_at', 'completed_at')
    filter_horizontal = ('documents',)
    
    def document_count(self, obj):
        return obj.documents.count()
    document_count.short_description = 'Документов'
