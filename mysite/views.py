from django.shortcuts import render

# Create your views here.

from .models import HomeSection, AboutSection, SkillCategory, PortfolioItem

def index(request):
    home_section = HomeSection.objects.first()
    about_section = AboutSection.objects.first()
    skill_categories = SkillCategory.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    
    context = {
        'home_section': home_section,
        'about_section': about_section,
        'skill_categories': skill_categories,
        'portfolio_items': portfolio_items,
    }
    
    # return render(request, 'mysite/index.html', context)
    return render(request, 'index.html', context)
