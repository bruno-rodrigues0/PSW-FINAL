from django.shortcuts import render


def index(request):
    """
    Render the home page.
    """
    context = {
        'page_title': 'Home',
        'page_description': 'Welcome to Xtundent, your go-to platform for online learning and professional development.'
    }
    return render(request, 'index.html', context)


def about(request):
    """
    Render the about page.
    """
    context = {
        'page_title': 'About Us',
        'page_description': 'Odio et unde deleniti. Deserunt numquam exercitationem. Officiis quo odio sint voluptas consequatur ut a odio voluptatem. Sit dolorum debitis veritatis natus dolores. Quasi ratione sint. Sit quaerat ipsum dolorem.'
    }
    return render(request, 'pages/about.html', context)


def courses(request):
    """
    Render the courses page.
    """
    context = {
        'page_title': 'Courses',
        'page_description': 'Explore our comprehensive range of courses designed to help you develop new skills and advance your career. From web development to digital marketing, we offer expert-led training programs.'
    }
    return render(request, 'pages/courses.html', context)


def trainers(request):
    """
    Render the trainers page.
    """
    context = {
        'page_title': 'Trainers',
        'page_description': 'Meet our team of experienced and passionate trainers who are dedicated to helping you achieve your learning goals. Each trainer brings years of industry experience and expertise.'
    }
    return render(request, 'pages/trainers.html', context)


def events(request):
    """
    Render the events page.
    """
    context = {
        'page_title': 'Events',
        'page_description': 'Stay updated with our latest events, workshops, and seminars. Join us for networking opportunities, skill-building sessions, and industry insights from leading experts.'
    }
    return render(request, 'pages/events.html', context)


def contact(request):
    """
    Render the contact page.
    """
    context = {
        'page_title': 'Contact Us',
        'page_description': 'Get in touch with us for any questions, inquiries, or support. We are here to help you on your learning journey and provide the assistance you need.'
    }
    return render(request, 'pages/contact.html', context)


# Admin

def admin_dashboard(request):
    """
    Render the admin dashboard.
    """

    return render(request, 'admin/index.html')
