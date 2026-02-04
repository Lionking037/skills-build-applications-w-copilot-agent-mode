from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    rank = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - Rank {self.rank}"