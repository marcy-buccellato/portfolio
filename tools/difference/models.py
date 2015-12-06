from math import pow

from django.db import models


def get_difference(number):
    """
    Get difference between the sum of the squares and the square of the sums
    for a given number
    """
    if not isinstance(number, int):
        return

    sum_of_the_squares = 0
    sum_of_the_numbers = 0

    for x in range(1, number + 1):
        sum_of_the_squares += pow(x, 2)
        sum_of_the_numbers += x

    square_of_the_sums = pow(sum_of_the_numbers, 2)

    return square_of_the_sums - sum_of_the_squares


class Difference(models.Model):
    number = models.IntegerField(default=0, primary_key=True)
    value = models.IntegerField(default=0)
    occurrences = models.IntegerField(default=0)
    update_dt = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.value:
            self.value = get_difference(self.number)

        return super(Difference, self).save()
