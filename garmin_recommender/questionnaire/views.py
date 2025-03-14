from django.shortcuts import render
from .forms import WatchQuestionnaireForm
from .models import GarminWatch


def dashboard(request):
    return render(request, "questionnaire/dashboard.html")


def questionnaire_view(request):
    if request.method == "POST":
        form = WatchQuestionnaireForm(request.POST)
        if form.is_valid():
            activities = form.cleaned_data["activities"]
            features = form.cleaned_data["features"]
            battery_life = form.cleaned_data["battery_life"]
            rugged = form.cleaned_data["rugged"]

            # Filtering watches based on preferences
            recommendations = GarminWatch.objects.all()

            if "running" in activities:
                recommendations = recommendations.filter(running=True)
            if "cycling" in activities:
                recommendations = recommendations.filter(cycling=True)
            if "swimming" in activities:
                recommendations = recommendations.filter(swimming=True)
            if "hiking" in activities:
                recommendations = recommendations.filter(hiking=True)
            if "fitness_tracking" in features:
                recommendations = recommendations.filter(fitness_tracking=True)
            if "gps" in features:
                recommendations = recommendations.filter(gps=True)
            if "touchscreen" in features:
                recommendations = recommendations.filter(touchscreen=True)
            if "notifications" in features:
                recommendations = recommendations.filter(notifications=True)
            if rugged:
                recommendations = recommendations.filter(rugged=True)
            if battery_life == "long":
                recommendations = recommendations.filter(battery_life__gt=48)
            elif battery_life == "medium":
                recommendations = recommendations.filter(battery_life__gte=24, battery_life__lte=48)
            else:
                recommendations = recommendations.filter(battery_life__lte=24)

            return render(request, "questionnaire/results.html", {"watches": recommendations})

    else:
        form = WatchQuestionnaireForm()

    return render(request, "questionnaire/questionnaire.html", {"form": form})


def watch_catalog(request):
    watches = GarminWatch.objects.all()
    return render(request, "questionnaire/catalog.html", {"watches": watches})


def compare_watches(request):
    watches = GarminWatch.objects.all()
    selected_watches = None

    if request.GET.getlist("watch"):
        selected_watch_ids = request.GET.getlist("watch")
        selected_watches = GarminWatch.objects.filter(id__in=selected_watch_ids)

    return render(request, "questionnaire/compare.html", {
        "watches": watches,
        "selected_watches": selected_watches
    })
