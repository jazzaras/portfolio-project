from django.shortcuts import render


from .models import Job

def home(request):
	jobs = Job.objects
	return render(request, 'jobs/home.html', {'jobs':jobs})

def aboutme(request):
	return render(request, 'aboutme/aboutme.html')

def resume(request):
	return render(request, 'resume/resume.html')