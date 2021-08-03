from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=300)
    url = models.TextField(null=True)
    source = models.CharField(max_length=50)
    timestamp = models.DateTimeField(null=True)
    type = models.IntegerField(null=True)

    def __str__(self):
        return self.headline

class IndexPrice(models.Model):
    productName = models.CharField(max_length=300)
    currentMarketPrice = models.FloatField(null=True)
    #priceChangePercentage = models.CharField(max_length=1000)

    def __str__(self):
        return self.productName

class CountryCovidData(models.Model):
    countryName = models.CharField(max_length=300)
    newDailyCase = models.IntegerField(null=True)
    newDeathCase = models.IntegerField(null=True)
    newRecoveredCase = models.IntegerField(null=True)
    activeCase = models.IntegerField(null=True)
    criticalCase = models.IntegerField(null=True)

    def __str__(self):
        return self.countryName

class NewsTech(models.Model):
    headline = models.CharField(max_length=300)
    url = models.TextField(null=True)
    source = models.CharField(max_length=50)
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return self.headline





