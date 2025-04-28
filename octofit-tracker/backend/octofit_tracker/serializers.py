from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'height', 'weight', 'birth_date']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 
                 'calories_burned', 'date', 'time', 'notes', 'created_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score', 'last_updated']

class WorkoutSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration', 'difficulty_level',
                 'activity_type', 'created_by', 'created_at']