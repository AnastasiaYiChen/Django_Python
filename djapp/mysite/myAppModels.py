from polls.models import Choice, Question
from django.utils import timezone

print("Hello Yi!")

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.

# id=2
Question.objects.all()
q = Question(question_text="What's your favorite color?",pub_date=timezone.now())
q.save()
q.id

# id=3
q = Question(question_text="What's your favorite character?", pub_date=timezone.now())
q.save()
q.id

# id=4
q = Question(question_text="What's your favorite animation?", pub_date=timezone.now())
q.save()
q.id

# id=5
q = Question(question_text="What's your favoriate film?", pub_date=timezone.now())
q.save()
q.id

# id=6
q = Question(question_text="Who will you select?", pub_date=timezone.now())
q.save()
q.id

# id=7
q = Question(question_text="Are you going to go trick or treat?", pub_date=timezone.now())
q.save()
q.id

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.

# choices for "What's your favorite color?"
q = Question.objects.get(pk=2)
q.choice_set.all()
q.choice_set.create(choice_text='red', votes=0)
q.choice_set.create(choice_text='green', votes=0)
q.choice_set.create(choice_text='blue', votes=0)

# choices for "What's your favorite character?"
q = Question.objects.get(pk=3)
q.choice_set.all()
q.choice_set.create(choice_text='Snow White', votes=0)
q.choice_set.create(choice_text='Evil steomother', votes=0)
q.choice_set.create(choice_text='Seven Dwarfs', votes=0)

# choices for "What's your favorite animation?"
q = Question.objects.get(pk=4)
q.choice_set.all()
q.choice_set.create(choice_text='How to training your dragon', votes=0)
q.choice_set.create(choice_text='frozen', votes=0)
q.choice_set.create(choice_text='Moana', votes=0)

# choices for "What's your favorite film?"
q = Question.objects.get(pk=5)
q.choice_set.all()
q.choice_set.create(choice_text='Life is beautiful', votes=0)
q.choice_set.create(choice_text='Children of heaven', votes=0)
q.choice_set.create(choice_text='The Shawshank Redemption', votes=0)
q.choice_set.create(choice_text='Forrest Gump', votes=0)

# choices for "Who will you select?"
q = Question.objects.get(pk=6)
q.choice_set.create(choice_text='Donald Trump', votes=0)
q.choice_set.create(choice_text='Joe Biden', votes=0)
q.choice_set.create(choice_text='Yi Chen', votes=0)

# choices for "Are you going to go trick or treat?"
q = Question.objects.get(pk=7)
q.choice_set.all()
q.choice_set.create(choice_text='Yes', votes=0)
q.choice_set.create(choice_text='No', votes=0)
q.choice_set.create(choice_text='No idea', votes=0)
