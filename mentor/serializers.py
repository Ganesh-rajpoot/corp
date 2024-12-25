# mentor/serializers.py
from rest_framework import serializers
from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'email', 'mobile', 'linkedin_url', 'about', 'username',
                  'mentor_image', 'mentor_company', 'mentor_experience', 'skills', 'mentor_designation','password','confirm_password']

    # Additional validation for unique fields (username, email, mobile)
    def validate_username(self, value):
        if Mentor.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if Mentor.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_mobile(self, value):
        if Mentor.objects.filter(mobile=value).exists():
            raise serializers.ValidationError("This mobile number is already in use.")
        return value
    
    def validate(self, data):
        # Check that password and confirm_password match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password and Confirm Password do not match.")
        return data

    def create(self, validated_data):
        # Remove confirm_password before saving
        validated_data.pop('confirm_password', None)
        mentor = Mentor(**validated_data)
        mentor.save()  # Hashes the password during save
        return mentor
