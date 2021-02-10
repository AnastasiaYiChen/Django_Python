from blog.models import Post,Eventsview
from django.utils import timezone
from django.contrib.auth.models import User


User.objects.all()
u = User.objects.filter(username='aaa').first()
p = Post(title="good sky conference", content="look the sky and share the magic way to finish assignment", author=u)
p.save()
p = Post(title="Magic Stone", content="Make a gold stone, magic way", author=u)
p.save()
e = Eventsview(conference=p, events_name="Finish Assignment Spell", events_description="Share the latest spell study to help you achieve a perfect assignment", events_location="Flash Block")
e.save()
e = Eventsview(conference=p, events_name="Debug Spell", events_description="One spell bug dissapear", events_location="A Location")
e.save()

