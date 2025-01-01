from django.db import models
from django.urls import reverse

class Plant(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Sunlight = models.CharField(max_length=50)
    Soil_type = models.CharField(max_length=50)
    Water_requirements = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        # Redirects to the plant detail view using the plant's primary key
        return reverse('plant-detail', kwargs={'pk': self.pk})

class PlantingTip(models.Model):
    Plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='tips')
    Tip = models.TextField()
    Step_number = models.TextField()

    def __str__(self):
        return f"Tip {self.Step_number} for {self.Plant.name}"


class PlantingCalendar(models.Model):
    Plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='calendar_entries')
    Season = models.CharField(max_length=50)
    Optimal_start_date = models.DateField()
    Optimal_end_date = models.DateField()

    def __str__(self):
        return f"{self.Plant.name} - {self.Season}"

class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField()
    Join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Username

class Reminder(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    Calendar_entry = models.ForeignKey(PlantingCalendar, on_delete=models.CASCADE, related_name='reminders')
    Reminder_date = models.DateField()

    def __str__(self):
        return f"Reminder for {self.User.Username} on {self.Reminder_date}"