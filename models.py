class TestModel(models.Model):
    test_name = models.CharField(max_length=1024)
    why = models.CharField(max_length=1023)
    why2 = models.CharField(max_length=1023)


