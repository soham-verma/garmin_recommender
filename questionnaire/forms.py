from django import forms

class WatchQuestionnaireForm(forms.Form):
    ACTIVITIES = [
        ("running", "Running"),
        ("cycling", "Cycling"),
        ("swimming", "Swimming"),
        ("hiking", "Hiking"),
    ]
    FEATURES = [
        ("fitness_tracking", "Fitness Tracking"),
        ("gps", "GPS Navigation"),
        ("touchscreen", "Touchscreen"),
        ("notifications", "Smart Notifications"),
    ]
    
    activities = forms.MultipleChoiceField(
        choices=ACTIVITIES, widget=forms.CheckboxSelectMultiple, required=False, label="Which activities do you do?"
    )
    
    features = forms.MultipleChoiceField(
        choices=FEATURES, widget=forms.CheckboxSelectMultiple, required=False, label="Which features do you need?"
    )
    
    battery_life = forms.ChoiceField(
        choices=[("short", "Less than 24 hours"), ("medium", "24-48 hours"), ("long", "More than 48 hours")],
        label="Preferred Battery Life"
    )
    
    rugged = forms.BooleanField(required=False, label="Do you need a rugged, outdoor watch?")

