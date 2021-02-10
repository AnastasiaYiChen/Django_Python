***********************
=======================
Run it you have to install:

pip install Pillow

***********************
=======================
When you import myAppModels.py 
you may get error because:

the username you have to fill a of the "User.objects.all()" user
put in ''  where is (username='')

for exmaple:
aaa is the username where you used for registration

u = User.objects.filter(username='aaa').first()
