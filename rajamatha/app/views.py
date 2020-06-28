from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . models import AboutUs,LatestEvents,HomepageOurTeam,AboutUsOurTeam,WhyChooseUs,Gallary,ContactUs,CountNumbers,Achivements,NGOPartners,SocialMediaPartners,BannerImage,TestMonial
from .forms import AboutUsForm,LatestEventsForm,HomepageOurTeamForm,AboutUsOurTeamForm,WhyChooseUsForm,GallaryForm,CountNumbersForm,AchivementsForm,NGOPartnersForm,SocialMediaPartnersForm,BannerImageForm,TestMonialForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def login_admin(request):
    if request.user.is_authenticated:
        return redirect("app:index")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('app:index')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'login.html')
def index(request):
    events=LatestEvents.objects.all()
    teams=HomepageOurTeam.objects.all()
    count_numbers=CountNumbers.objects.all().first()
    achivements=Achivements.objects.all()
    banner_image=BannerImage.objects.all().first()
    return render(request,'index.html',{'events':events,'teams':teams,'count_numbers':count_numbers,'achivements':achivements,'banner_image':banner_image})
def payment_gateway(request):
    return render(request,'payment.html')
def about(request):
    goals=AboutUs.objects.all()
    theme=WhyChooseUs.objects.first()
    supporters=AboutUsOurTeam.objects.all()
    ngoparts=NGOPartners.objects.all()
    socparts=SocialMediaPartners.objects.all()
    testmonials=TestMonial.objects.all()
    return render(request,'about.html',{'goals':goals,'theme':theme,'supporters':supporters,'ngoparts':ngoparts,'socparts':socparts,'testmonials':testmonials})
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("pno")
        message=request.POST.get("message")
        new_contactus=ContactUs(name=name,email=email,phone=phone,message=message)
        new_contactus.save()
        return HttpResponse("Thanks for regestration mr . "+name+"<br> Our <a href='/'>Homepage</a>")
    return render(request,'contact.html')
def gallary(request):
    types=AboutUs.objects.all()
    images=[]
    for i in types:
        images.append(i.gallary_set.all())
    return render(request,'gallery.html',{'images':images})
@user_passes_test(lambda u: u.is_superuser)
def admin_logout(request):
    logout(request)
    return redirect('app:index')
@user_passes_test(lambda u: u.is_superuser)
def admin_panel(request):
    notifications=ContactUs.objects.all()
    return render(request,'admin-index.html',{'notifications':notifications})
@user_passes_test(lambda u: u.is_superuser)
def delete_notification(request,pk):
    notification=ContactUs.objects.get(id=pk)
    if request.method=="POST":
        notification.delete()
        return redirect('app:admin_panel')
    return render(request,'confirm.html',{'back_url':reverse('app:admin_panel')})
@user_passes_test(lambda u: u.is_superuser)
def admin_about(request):
    goals=AboutUs.objects.all()
    return render(request,'about-us-admin.html',{'goals':goals})
@user_passes_test(lambda u: u.is_superuser)
def create_About(request):
    if request.method=="POST":
        form=AboutUsForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_about')
    else:
        form=AboutUsForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_About(request,pk):
    instance=AboutUs.objects.get(id=pk)
    if request.method=="POST":
        form=AboutUsForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_about')
    else:
        form=AboutUsForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_about(request,pk):
    instance=AboutUs.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_about')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_about')})
@user_passes_test(lambda u: u.is_superuser)
def admin_events(request):
    events=LatestEvents.objects.all()
    return render(request,'admin-events.html',{'events':events})
@user_passes_test(lambda u: u.is_superuser)
def create_event(request):
    if request.method=="POST":
        form=LatestEventsForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_events')
    else:
        form=LatestEventsForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_event(request,pk):
    instance=LatestEvents.objects.get(id=pk)
    if request.method=="POST":
        form=LatestEventsForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_events')
    else:
        form=LatestEventsForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_event(request,pk):
    instance=LatestEvents.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_events')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_events')})
@user_passes_test(lambda u: u.is_superuser)
def admin_core_team(request):
    members=HomepageOurTeam.objects.all()
    return render(request,'admin-core-team.html',{'members':members})
@user_passes_test(lambda u: u.is_superuser)
def create_core_team(request):
    if request.method=="POST":
        form=HomepageOurTeamForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_core_team')
    else:
        form=HomepageOurTeamForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_core_team(request,pk):
    instance=HomepageOurTeam.objects.get(id=pk)
    if request.method=="POST":
        form=HomepageOurTeamForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_core_team')
    else:
        form=HomepageOurTeamForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_core_team(request,pk):
    instance=HomepageOurTeam.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_core_team')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_core_team')})
@user_passes_test(lambda u: u.is_superuser)
def admin_supporters(request):
    members=AboutUsOurTeam.objects.all()
    return render(request,'admin-supporters.html',{'members':members})
@user_passes_test(lambda u: u.is_superuser)
def create_supporters(request):
    if request.method=="POST":
        form=AboutUsOurTeamForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_supporters')
    else:
        form=AboutUsOurTeamForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_supporters(request,pk):
    instance=AboutUsOurTeam.objects.get(id=pk)
    if request.method=="POST":
        form=AboutUsOurTeamForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_supporters')
    else:
        form=AboutUsOurTeamForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_supporters(request,pk):
    instance=AboutUsOurTeam.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_supporters')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_supporters')})
@user_passes_test(lambda u: u.is_superuser)
def update_why_choose_us(request):
    instance=WhyChooseUs.objects.first()
    if request.method=="POST":
        form=WhyChooseUsForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_panel')
    else:
        form=WhyChooseUsForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})

@user_passes_test(lambda u: u.is_superuser)
def admin_gallary(request):
    types=AboutUs.objects.all()
    return render(request,'admin-gallary.html',{'types':types})
@user_passes_test(lambda u: u.is_superuser)
def admin_gallary_detail(request,goal):
    theme=AboutUs.objects.get(title=goal)
    images=theme.gallary_set.all()
    return render(request,'gallary-admin-detail.html',{'images':images,'theme':theme})
@user_passes_test(lambda u: u.is_superuser)
def create_admin_gallary(request,goal):
    theme=AboutUs.objects.get(title=goal)
    if request.method=="POST":
        form=GallaryForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save(commit=False)
            about.aboutus=theme
            about.save()
            return redirect('app:admin_gallary_detail',theme.title)
    else:
        form=GallaryForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_admin_gallary(request,pk):
    instance=Gallary.objects.get(id=pk)
    if request.method=="POST":
        form=GallaryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_gallary_detail',instance.aboutus.title)
    else:
        form=GallaryForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_admin_gallary(request,pk):
    instance=Gallary.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_gallary_detail',instance.aboutus.title)
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_gallary_detail',kwargs={'goal':instance.aboutus.title})})
@user_passes_test(lambda u: u.is_superuser)
def admin_achivements(request):
    achivements=Achivements.objects.all()
    return render(request,'admin-achievements.html',{'achivements':achivements})
@user_passes_test(lambda u: u.is_superuser)
def create_achivements(request):
    if request.method=="POST":
        form=AchivementsForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_achivements')
    else:
        form=AchivementsForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_achivements(request,pk):
    instance=Achivements.objects.get(id=pk)
    if request.method=="POST":
        form=AchivementsForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_achivements')
    else:
        form=AchivementsForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_achivements(request,pk):
    instance=Achivements.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_achivements')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_achivements')})
@user_passes_test(lambda u: u.is_superuser)
def update_count(request):
    instance=CountNumbers.objects.first()
    if request.method=="POST":
        form=CountNumbersForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_panel')
    else:
        form=CountNumbersForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})

@user_passes_test(lambda u: u.is_superuser)
def admin_ngo(request):
    members=NGOPartners.objects.all()
    return render(request,'admin-ngo.html',{'members':members})
@user_passes_test(lambda u: u.is_superuser)
def create_ngo(request):
    if request.method=="POST":
        form=NGOPartnersForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_ngo')
    else:
        form=NGOPartnersForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_ngo(request,pk):
    instance=NGOPartners.objects.get(id=pk)
    if request.method=="POST":
        form=NGOPartnersForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_ngo')
    else:
        form=NGOPartnersForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_ngo(request,pk):
    instance=NGOPartners.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_ngo')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_ngo')})
@user_passes_test(lambda u: u.is_superuser)
def admin_social(request):
    members=SocialMediaPartners.objects.all()
    return render(request,'admin-social.html',{'members':members})
@user_passes_test(lambda u: u.is_superuser)
def create_social(request):
    if request.method=="POST":
        form=SocialMediaPartnersForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_social')
    else:
        form=SocialMediaPartnersForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_social(request,pk):
    instance=SocialMediaPartners.objects.get(id=pk)
    if request.method=="POST":
        form=SocialMediaPartnersForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_social')
    else:
        form=SocialMediaPartnersForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_social(request,pk):
    instance=SocialMediaPartners.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_social')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_social')})
@user_passes_test(lambda u: u.is_superuser)
def update_banner_image(request):
    instance=BannerImage.objects.first()
    if request.method=="POST":
        form=BannerImageForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_panel')
    else:
        form=BannerImageForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def admin_testmonial(request):
    testmonials=TestMonial.objects.all()
    return render(request,'admin-testmonial.html',{'testmonials':testmonials})
@user_passes_test(lambda u: u.is_superuser)
def create_testmonial(request):
    if request.method=="POST":
        form=TestMonialForm(request.POST)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_testmonial')
    else:
        form=TestMonialForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_testmonial(request,pk):
    instance=TestMonial.objects.get(id=pk)
    if request.method=="POST":
        form=TestMonialForm(request.POST,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:admin_testmonial')
    else:
        form=TestMonialForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_testmonial(request,pk):
    instance=TestMonial.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:admin_testmonial')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:admin_social')})