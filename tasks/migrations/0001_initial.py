
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('importance', models.IntegerField(default=5)),
                ('estimated_hours', models.IntegerField(default=1)),
                ('dependencies', models.JSONField(default=list, blank=True)),
            ],
        ),
    ]
