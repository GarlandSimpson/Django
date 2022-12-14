from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404


class CourseListView(generic.ListView):
    """Generic class-based course list view"""
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        """Override get_queryset() to provide list of objects"""
        # query top 10 popular classes based on total_enrollment
        courses = Course.objects.order_by('-total_enrollment')[:10]
        return courses


# class CourseListView(View):
#     """Class-based course list view"""
#     # Handle get request
#     def get(self, request):
#         context = {}
#         # query the top 10 popular classes based on total_enrollment
#         course_list = Course.objects.order_by('-total_enrollment')[:10]
#         context['course_list'] = course_list
#         return render(request, 'onlinecourse/course_list.html', context)

# Function based views

# Function-based course list view
# def popular_course_list(request):
#    context = {}
#    if request.method == 'GET':
#        course_list = Course.objects.order_by('-total_enrollment')[:10]
#        context['course_list'] = course_list
#        return render(request, 'onlinecourse/course_list_no_css.html', context)


class CourseDetailsView(generic.DetailView):
    """Generic class-based course list view"""
    model = Course
    template_name = 'onlinecourse/course_detail.html'


# class CourseDetailsView(View):
#     """Class-based course details view"""
#     def get(self, request, *args, **kwargs):
#         """Handle GET request"""
#         context = {}
#         # Get URL parameter pk from keyword argument list
#         course_id = kwargs.get('pk')
#         try:
#             # Get course object based on course_id
#             course = Course.objects.get(pk=course_id)
#             # Append course object to context
#             context['course'] = course
#             # render HTTP response with template
#             return render(request, 'onlinecourse/course_detail.html', context)
#         except Course.DoesNotExist:
#             raise Http404("No course matches the given id")


# Function-based course_details view
# def course_details(request, course_id):
#    context = {}
#    if request.method == 'GET':
#        try:
#            course = Course.objects.get(pk=course_id)
#            context['course'] = course
#            return render(request, 'onlinecourse/course_detail.html', context)
#        except Course.DoesNotExist:
#            raise Http404("No course matches the given id.")


class EnrollView(View):
    """Class-based enroll view"""
    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course, pk=course_id)
        # Increase total_enrollment by 1
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))


# Function-based enroll view
# def enroll(request, course_id):
#    if request.method == 'POST':
#       course = get_object_or_404(Course, pk=course_id)
#       # Create an enrollment
#       course.total_enrollment += 1
#       course.save()
#       return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))
