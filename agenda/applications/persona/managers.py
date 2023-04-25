from django.db import models
from django.db.models import Count

class MeetingManager(models.Manager):
    
    def meetings_job_count(self):
        result = self.values('person__job').annotate(
            cantidad = Count('id')
        )
        print("===========================")
        print(result)
        return result

    def meetings_by_asunto(self):
        result = self.annotate(
            cantidad = Count('asunto')
        )
        print("===========================")
        print(result)
        return result