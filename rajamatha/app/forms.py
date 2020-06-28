from django import forms
from . models import AboutUs,LatestEvents,HomepageOurTeam,AboutUsOurTeam,WhyChooseUs,Gallary,ContactUs,CountNumbers,Achivements,NGOPartners,SocialMediaPartners,BannerImage,TestMonial
class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields="__all__"
class LatestEventsForm(forms.ModelForm):
    class Meta:
        model = LatestEvents
        fields="__all__"
class HomepageOurTeamForm(forms.ModelForm):
    class Meta:
        model=HomepageOurTeam
        fields="__all__"
class AboutUsOurTeamForm(forms.ModelForm):
    class Meta:
        model=AboutUsOurTeam
        fields="__all__"
class WhyChooseUsForm(forms.ModelForm):
    class Meta:
        model=WhyChooseUs
        fields="__all__"
class GallaryForm(forms.ModelForm):
    class Meta:
        model=Gallary
        fileds="__all__"
        exclude=['aboutus']
class CountNumbersForm(forms.ModelForm):
    class Meta:
        model=CountNumbers
        fields="__all__"
class AchivementsForm(forms.ModelForm):
    class Meta:
        model=Achivements
        fields="__all__"
class NGOPartnersForm(forms.ModelForm):
    class Meta:
        model=NGOPartners
        fields="__all__"
class SocialMediaPartnersForm(forms.ModelForm):
    class Meta:
        model=SocialMediaPartners
        fields="__all__"

class BannerImageForm(forms.ModelForm):
    class Meta:
        model=BannerImage
        fields="__all__"
class TestMonialForm(forms.ModelForm):
    class Meta:
        model=TestMonial
        fields="__all__"