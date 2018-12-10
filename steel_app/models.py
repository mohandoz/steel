from django.db import models


STEEL_TYPE_CHOICE = (
    ('1080', '1080'),
    ('9310', '9310'),
    ('8645', '8645'),
    ('8620', '8620'),
    ('8617', '8617'),
    ('6150', '6150'),
    ('5160', '5160'),
    ('4620', '4620'),
    ('4140', '4140'),
    ('4130', '4130'),
    ('4118', '4118'),
    ('4047', '4047'),
)


HEAT_TREATMENT_CHOICE = (
    ('austenitizing', 'austenitizing'),
    ('carburizing', 'carburizing'),
    ('normalizing', 'normalizing'),
    ('annealing', 'annealing'),
    ('quencheing', 'quencheing'),
    ('carbonitrieding', 'carbonitrieding'),
)


HEAT_TEMP_CHOICE = (
    ('1050', '1050'),
    ('925', '925'),
    ('885', '885'),
    ('815', '815'),
    ('845', '845'),
    ('900', '900'),
    ('925', '925'),
    ('870', '870'),
    ('880', '880'),
    ('940', '940'),
    ('830', '830'),
)

HOLDING_TIME_CHOICE = (
    ('30 min', '30 min'),
    ('4 hour', '4 hour'),
    ('2 hour', '2 hour'),
    ('1 hour', '1 hour'),
    ('0 hour', '0 hour'),
    ('11 hour', '11 hour'),
    ('3 hour', '3 hour'),
    ('20 min', '20 min'),
    ('5 min', '5 min'),
    ('8 hour', '8 hour'),
)

COOLING_MEDIA_CHOICE = (
    ('furnace', 'furnace'),
    ('oil', 'oil'),
    ('air', 'air'),
    ('water', 'water'),
)





class Steel(models.Model):
    steel_type = models.CharField(choices=STEEL_TYPE_CHOICE, max_length=50)
    heat_treatment = models.CharField(choices=HEAT_TREATMENT_CHOICE, max_length=50)
    heat_temp = models.CharField(choices=HEAT_TEMP_CHOICE, max_length=50)
    holding_time = models.CharField(choices=HOLDING_TIME_CHOICE, max_length=50)
    cooling_media = models.CharField(choices=COOLING_MEDIA_CHOICE, max_length=50)
    image = models.ImageField(upload_to="images")
    notes =  models.CharField(max_length=150)