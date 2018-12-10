from django.shortcuts import render
from .models import Steel
from django.core.exceptions import ObjectDoesNotExist

def steel(request):
    if "check" in request.GET:
        steel_type = request.GET.get("steeltype")
        heat_treatment = request.GET.get("Heat-treatment")
        holding_time = request.GET.get("Holding-time")
        cooling_media = request.GET.get("cooling-media")
        heat_temp = request.GET.get("Heat-Temp")


        test = Steel.objects.filter(steel_type= steel_type,heat_treatment = heat_treatment, holding_time= holding_time, 
                cooling_media = cooling_media, heat_temp = heat_temp ).values("image", "notes")
        print(test)

        if test.exists():
            test = test[0]
        else:
            return render(request, "steel_app/index.html",{"notes":"Test not found!"})

        return render(request, "steel_app/index.html",{"test":test})

    if request.method == "GET":
        return render(request, "steel_app/index.html")

