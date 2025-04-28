from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Profile, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, ProfileSerializer, TeamSerializer,
    ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    """
    Root API endpoint that lists all available endpoints
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'profiles': reverse('profile-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()
        # Add the creating user as a team member
        team = serializer.instance
        team.members.add(self.request.user)

class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities
    """
    queryset = Activity.objects.all().order_by('-date', '-time')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        Optionally filter activities by user and date
        """
        queryset = self.queryset
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user__username=user)
        
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard scores
    """
    queryset = Leaderboard.objects.all().order_by('-score')
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workout plans
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)