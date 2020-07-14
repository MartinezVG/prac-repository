from django.db import models

class Member(models.Model):
    sbytes = models.FloatField()
    smean = models.FloatField()
    ct_srv_src = models.FloatField()
    sload = models.FloatField()
    synack = models.FloatField()
    ct_srv_dst = models.FloatField()
    ct_dst_src_ltm = models.FloatField()


