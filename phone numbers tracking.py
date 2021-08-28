import phonenumbers
from phonenumbers import geocoder
number="+7893592978"
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_numbers(service_number,"en"))
