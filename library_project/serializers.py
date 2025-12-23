from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','title', 'subtitle', 'author','isbn_number', 'price']
        
        
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        
        # Check if title contains only alphabetic characters
        if not title.isalpha():
            raise serializers.ValidationError("Title should only contain alphabetic characters.")
        
        
        # Check author and title are not the same
        if Books.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError("A book with this title and author already exists.")
            
        
        return data
        
        
        
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value   
        