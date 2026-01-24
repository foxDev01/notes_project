#  определяет сериализаторы  дял модели нтоте
 
from rest_framework import serializers
from gjango.utils.html import escape
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        field = ['id','title','content','created_at','update_at']
        read_only_field=['id','created_at','update_at']
# проверка наличия заголовка
    def validate_title(self,value):
        if not value.strip():
            raise serializers.ValidateError('Заголовок не может быть пустым')
        return escape(value.strip())
# проверка наличия контента
    def validate_content(self,value):
        if not value.strip():
            raise serializers.ValidateError('Содержание не может быть пустым')
        return escape(value.strip())


class NoteCreateSerializer(NoteSerializer):
    pass


class NoteUpdateSerializer(NoteSerializer):
    # для обновлвения заметок делает поля необязательными 
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)