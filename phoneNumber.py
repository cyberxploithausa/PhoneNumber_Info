import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


ch_number = phonenumbers.parse("+2348185819414", "CH")
print(geocoder.description_for_number(ch_number, "en"))

service_numb = phonenumbers.parse("+2348185819414", "RO")
print(carrier.name_for_number(service_numb, "en"))

gb_number = phonenumbers.parse("+2348185819414", "GB")
print(timezone.time_zones_for_number(gb_number))