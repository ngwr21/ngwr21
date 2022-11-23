from django.db import models

##a_record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
##a_record.save()
class Meta:
    model = User
    fields = ("username",)
