from djongo import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Extended user profile for fitness tracking"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    height = models.FloatField(null=True, blank=True)  # in cm
    weight = models.FloatField(null=True, blank=True)  # in kg
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class Team(models.Model):
    """Team model for group competitions and activities"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='teams')
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    """Activity model for tracking user workouts"""
    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('walking', 'Walking'),
        ('strength', 'Strength Training'),
        ('yoga', 'Yoga'),
        ('basketball', 'Basketball'),
        ('football', 'Football'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration = models.DurationField()
    distance = models.FloatField(null=True, blank=True)  # in km
    calories_burned = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.date}"
    
    class Meta:
        verbose_name_plural = "Activities"

class Leaderboard(models.Model):
    """Leaderboard model for tracking user rankings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.score} points"

class Workout(models.Model):
    """Workout template model for predefined workout plans"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    difficulty_level = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    activity_type = models.CharField(max_length=20, choices=Activity.ACTIVITY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_workouts')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name