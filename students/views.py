from django.contrib.auth.decorators import login_required
from background_task import background
from django.contrib.auth import login as auth_login, authenticate,logout
from django.shortcuts import render, redirect
from students.forms import *
from students.models import *
from django.http import HttpResponse
from datetime import timedelta
import time
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
        else:
            redirect('register')
    else:
        form = SignUpForm()
    return render(request, '../../students/templates/student/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print("email password",email,password)
            user = authenticate(username=email, password=password)
            if user:
              print("valed")
              auth_login(request,user)
              return redirect('home')
            else:
              return redirect('login')
        else:
            print("form invaluid")
            return redirect('login')
    else:
       form=UserLoginForm()
    return render(request, '../../students/templates/student/login.html', {'form': form})


@login_required(login_url='login/')
def charts(request):
   name=request.user
   average_score_stage_1=[0]*8
   average_score_stage_2 = [0] * 8
   average_score_stage_3 = [0] * 8

   hardware_iot_stage_1=[0]*9
   hardware_iot_stage_2 = [0] * 9
   hardware_iot_stage_3 = [0] * 9

   ai_stage_1=  [0] *  6
   ai_stage_2 = [0] * 6
   ai_stage_3 = [0] * 6

   software_stage_1=[0]*5
   software_stage_2 = [0] * 5
   software_stage_3 = [0] * 5

   product_design_stage_1= [0] * 5
   product_design_stage_2 = [0] * 5
   product_design_stage_3 = [0] * 5

   software_platforms_stage_1 = [0]*6
   software_platforms_stage_2 = [0] * 6
   software_platforms_stage_3 = [0] * 6

   programming_stage_1=[0]*4
   programming_stage_2 = [0] * 4
   programming_stage_3 = [0] * 4

   intellectual_property_stage_1 = [0] * 3
   intellectual_property_stage_2 = [0] * 3
   intellectual_property_stage_3 = [0] * 3

   innovation_stage_1 = [0] *6
   innovation_stage_2 = [0] * 6
   innovation_stage_3 = [0] * 6



   if Hardware_iot.objects.filter(student=request.user.id,stage=1).exists():
       hardware_iot_stage_1_data=Hardware_iot.objects.get(student=request.user.id,stage=1)
       average_score_stage_1[0]= hardware_iot_stage_1_data.rating
       hardware_iot_stage_1[0]=hardware_iot_stage_1_data.electronics_circuit_design
       hardware_iot_stage_1[1] = hardware_iot_stage_1_data.pcb_designing
       hardware_iot_stage_1[2] = hardware_iot_stage_1_data.embedded_hardware_platform
       hardware_iot_stage_1[3] = hardware_iot_stage_1_data.sensors_actuators
       hardware_iot_stage_1[4] = hardware_iot_stage_1_data.modules_integrations
       hardware_iot_stage_1[5] = hardware_iot_stage_1_data.system_interfaces_implementation
       hardware_iot_stage_1[6] = hardware_iot_stage_1_data.data_acquisition_techniques
       hardware_iot_stage_1[7] = hardware_iot_stage_1_data.basic_of_networking
       hardware_iot_stage_1[8] = hardware_iot_stage_1_data.power_design_for_circuits

   if Hardware_iot.objects.filter(student=request.user.id, stage=2).exists():
       hardware_iot_stage_2_data = Hardware_iot.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[0] = hardware_iot_stage_2_data.rating
       hardware_iot_stage_2[0] = hardware_iot_stage_2_data.electronics_circuit_design
       hardware_iot_stage_2[1] = hardware_iot_stage_2_data.pcb_designing
       hardware_iot_stage_2[2] = hardware_iot_stage_2_data.embedded_hardware_platform
       hardware_iot_stage_2[3] = hardware_iot_stage_2_data.sensors_actuators
       hardware_iot_stage_2[4] = hardware_iot_stage_2_data.modules_integrations
       hardware_iot_stage_2[5] = hardware_iot_stage_2_data.system_interfaces_implementation
       hardware_iot_stage_2[6] = hardware_iot_stage_2_data.data_acquisition_techniques
       hardware_iot_stage_2[7] = hardware_iot_stage_2_data.basic_of_networking
       hardware_iot_stage_2[8] = hardware_iot_stage_2_data.power_design_for_circuits

   if Hardware_iot.objects.filter(student=request.user.id, stage=3).exists():
       hardware_iot_stage_3_data = Hardware_iot.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[0] = hardware_iot_stage_3_data.rating
       hardware_iot_stage_3[0] = hardware_iot_stage_3_data.electronics_circuit_design
       hardware_iot_stage_3[1] = hardware_iot_stage_3_data.pcb_designing
       hardware_iot_stage_3[2] = hardware_iot_stage_3_data.embedded_hardware_platform
       hardware_iot_stage_3[3] = hardware_iot_stage_3_data.sensors_actuators
       hardware_iot_stage_3[4] = hardware_iot_stage_3_data.modules_integrations
       hardware_iot_stage_3[5] = hardware_iot_stage_3_data.system_interfaces_implementation
       hardware_iot_stage_3[6] = hardware_iot_stage_3_data.data_acquisition_techniques
       hardware_iot_stage_3[7] = hardware_iot_stage_3_data.basic_of_networking
       hardware_iot_stage_3[8] = hardware_iot_stage_3_data.power_design_for_circuits
       average_score_stage_3[0] = Hardware_iot.objects.get(student=request.user.id, stage=3).rating


   if Ai.objects.filter(student=request.user.id,stage=1).exists():
       ai_stage_1_data=Ai.objects.get(student=request.user.id,stage=1)
       average_score_stage_1[1]= ai_stage_1_data.rating
       ai_stage_1[0]=ai_stage_1_data.data_modelling_evaluation
       ai_stage_1[1] = ai_stage_1_data.probablity_statistics
       ai_stage_1[2] = ai_stage_1_data.applied_math_algorithms
       ai_stage_1[3] = ai_stage_1_data.applied_machine_learning
       ai_stage_1[4] = ai_stage_1_data.distributed_computing
       ai_stage_1[5] = ai_stage_1_data.edge_computing

   if Ai.objects.filter(student=request.user.id,stage=2).exists():
       ai_stage_2_data = Ai.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[1] = ai_stage_2_data.rating
       ai_stage_2[0] = ai_stage_2_data.data_modelling_evaluation
       ai_stage_2[1] = ai_stage_2_data.probablity_statistics
       ai_stage_2[2] = ai_stage_2_data.applied_math_algorithms
       ai_stage_2[3] = ai_stage_2_data.applied_machine_learning
       ai_stage_2[4] = ai_stage_2_data.distributed_computing
       ai_stage_2[5] = ai_stage_2_data.edge_computing

   if Ai.objects.filter(student=request.user.id,stage=3).exists():
       ai_stage_3_data = Ai.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[1] = ai_stage_3_data.rating
       ai_stage_3[0] = ai_stage_3_data.data_modelling_evaluation
       ai_stage_3[1] = ai_stage_3_data.probablity_statistics
       ai_stage_3[2] = ai_stage_3_data.applied_math_algorithms
       ai_stage_3[3] = ai_stage_3_data.applied_machine_learning
       ai_stage_3[4] = ai_stage_3_data.distributed_computing
       ai_stage_3[5] = ai_stage_3_data.edge_computing


   if Software.objects.filter(student=request.user.id, stage=1).exists():
       software_stage_1_data = Software.objects.get(student=request.user.id, stage=1)
       average_score_stage_1[2] = software_stage_1_data.rating

       software_stage_1[0]=software_stage_1_data.application_architecture_design
       software_stage_1[1] = software_stage_1_data.mobile_application_development
       software_stage_1[2] = software_stage_1_data.cloud_platform
       software_stage_1[3] = software_stage_1_data.web_application_development
       software_stage_1[4] = software_stage_1_data.Linux_mac_packaging


   if Software.objects.filter(student=request.user.id, stage=2).exists():
       software_stage_2_data = Software.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[2] = software_stage_2_data.rating

       software_stage_2[0] = software_stage_2_data.application_architecture_design
       software_stage_2[1] = software_stage_2_data.mobile_application_development
       software_stage_2[2] = software_stage_2_data.cloud_platform
       software_stage_2[3] = software_stage_2_data.web_application_development
       software_stage_2[4] = software_stage_2_data.Linux_mac_packaging

   if Software.objects.filter(student=request.user.id, stage=3).exists():
       software_stage_3_data = Software.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[2] = Software.objects.get(student=request.user.id, stage=3).rating

       software_stage_3[0] = software_stage_3_data.application_architecture_design
       software_stage_3[1] = software_stage_3_data.mobile_application_development
       software_stage_3[2] = software_stage_3_data.cloud_platform
       software_stage_3[3] = software_stage_3_data.web_application_development
       software_stage_3[4] = software_stage_3_data.Linux_mac_packaging






   if Product_design.objects.filter(student=request.user.id, stage=1).exists():
       product_design_stage_1_data=Product_design.objects.get(student=request.user.id, stage=1)
       average_score_stage_1[3] = product_design_stage_1_data.rating

       product_design_stage_1[0]=product_design_stage_1_data.rapid_prototyping
       product_design_stage_1[1] = product_design_stage_1_data.principles_of_industrial_design
       product_design_stage_1[2] = product_design_stage_1_data.ui_ux_Design
       product_design_stage_1[3] = product_design_stage_1_data.cad
       product_design_stage_1[4] = product_design_stage_1_data.analysis_of_mechanical_design



   if Product_design.objects.filter(student=request.user.id, stage=2).exists():
       product_design_stage_2_data = Product_design.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[3] = product_design_stage_2_data.rating

       product_design_stage_2[0] = product_design_stage_2_data.rapid_prototyping
       product_design_stage_2[1] = product_design_stage_2_data.principles_of_industrial_design
       product_design_stage_2[2] = product_design_stage_2_data.ui_ux_Design
       product_design_stage_2[3] = product_design_stage_2_data.cad
       product_design_stage_2[4] = product_design_stage_2_data.analysis_of_mechanical_design



   if Product_design.objects.filter(student=request.user.id, stage=3).exists():
       product_design_stage_3_data = Product_design.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[3] = product_design_stage_3_data.rating

       product_design_stage_3[0] = product_design_stage_3_data.rapid_prototyping
       product_design_stage_3[1] = product_design_stage_3_data.principles_of_industrial_design
       product_design_stage_3[2] = product_design_stage_3_data.ui_ux_Design
       product_design_stage_3[3] = product_design_stage_3_data.cad
       product_design_stage_3[4] = product_design_stage_3_data.analysis_of_mechanical_design


   if Software_platforms.objects.filter(student=request.user.id, stage=1).exists():
       software_platforms_stage_1_data =Software_platforms.objects.get(student=request.user.id, stage=1)
       average_score_stage_1[4] = software_platforms_stage_1_data.rating

       software_platforms_stage_1[0]=software_platforms_stage_1_data.eagle_pcb
       software_platforms_stage_1[1] = software_platforms_stage_1_data.psim_multi_sim
       software_platforms_stage_1[2] = software_platforms_stage_1_data.lab_view
       software_platforms_stage_1[3] = software_platforms_stage_1_data.matlab
       software_platforms_stage_1[4] = software_platforms_stage_1_data.tableau
       software_platforms_stage_1[5] = software_platforms_stage_1_data.tibco_spotfire




   if Software_platforms.objects.filter(student=request.user.id, stage=2).exists():
       software_platforms_stage_2_data = Software_platforms.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[4] = software_platforms_stage_2_data.rating

       software_platforms_stage_2[0] = software_platforms_stage_2_data.eagle_pcb
       software_platforms_stage_2[1] = software_platforms_stage_2_data.psim_multi_sim
       software_platforms_stage_2[2] = software_platforms_stage_2_data.lab_view
       software_platforms_stage_2[3] = software_platforms_stage_2_data.matlab
       software_platforms_stage_2[4] = software_platforms_stage_2_data.tableau
       software_platforms_stage_2[5] = software_platforms_stage_2_data.tibco_spotfire



   if Software_platforms.objects.filter(student=request.user.id, stage=3).exists():
       software_platforms_stage_3_data=Software_platforms.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[4] = software_platforms_stage_3_data.rating

       software_platforms_stage_3[0] = software_platforms_stage_3_data.eagle_pcb
       software_platforms_stage_3[1] = software_platforms_stage_3_data.psim_multi_sim
       software_platforms_stage_3[2] = software_platforms_stage_3_data.lab_view
       software_platforms_stage_3[3] = software_platforms_stage_3_data.matlab
       software_platforms_stage_3[4] = software_platforms_stage_3_data.tableau
       software_platforms_stage_3[5] = software_platforms_stage_3_data.tibco_spotfire




   if Programming.objects.filter(student=request.user.id, stage=1).exists():
       programming_stage_1_data=Programming.objects.get(student=request.user.id, stage=1)
       average_score_stage_1[5] = programming_stage_1_data.rating

       programming_stage_1[0]=programming_stage_1_data.defining_problem
       programming_stage_1[1] = programming_stage_1_data.computer_science_fundamentals
       programming_stage_1[2] = programming_stage_1_data.programming_techniques
       programming_stage_1[3] = programming_stage_1_data.programming_languages



   if Programming.objects.filter(student=request.user.id, stage=2).exists():
       programming_stage_2_data = Programming.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[5] = programming_stage_2_data.rating

       programming_stage_2[0] = programming_stage_2_data.defining_problem
       programming_stage_2[1] = programming_stage_2_data.computer_science_fundamentals
       programming_stage_2[2] = programming_stage_2_data.programming_techniques
       programming_stage_2[3] = programming_stage_2_data.programming_languages

   if Programming.objects.filter(student=request.user.id, stage=3).exists():
       programming_stage_3_data = Programming.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[5] = programming_stage_3_data.rating

       programming_stage_3[0] = programming_stage_3_data.defining_problem
       programming_stage_3[1] = programming_stage_3_data.computer_science_fundamentals
       programming_stage_3[2] = programming_stage_3_data.programming_techniques
       programming_stage_3[3] = programming_stage_3_data.programming_languages


   if Intellectual_Property.objects.filter(student=request.user.id, stage=1).exists():
       intellectual_property_stage_1_data=Intellectual_Property.objects.get(student=request.user.id, stage=1)
       average_score_stage_1[6] = intellectual_property_stage_1_data.rating

       intellectual_property_stage_1[0]=intellectual_property_stage_1_data.ip_exploration
       intellectual_property_stage_1[2] = intellectual_property_stage_1_data.patent_drafting
       intellectual_property_stage_1[2] = intellectual_property_stage_1_data.key_word_seaching


   if Intellectual_Property.objects.filter(student=request.user.id, stage=2).exists():
       intellectual_property_stage_2_data = Intellectual_Property.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[6] = intellectual_property_stage_2_data.rating

       intellectual_property_stage_2[0] = intellectual_property_stage_2_data.ip_exploration
       intellectual_property_stage_2[2] = intellectual_property_stage_2_data.patent_drafting
       intellectual_property_stage_2[2] = intellectual_property_stage_2_data.key_word_seaching


   if Intellectual_Property.objects.filter(student=request.user.id, stage=3).exists():
       intellectual_property_stage_3_data = Intellectual_Property.objects.get(student=request.user.id, stage=3)
       average_score_stage_3[6] =intellectual_property_stage_3_data.rating

       intellectual_property_stage_3[0] = intellectual_property_stage_3_data.ip_exploration
       intellectual_property_stage_3[2] = intellectual_property_stage_3_data.patent_drafting
       intellectual_property_stage_3[2] = intellectual_property_stage_3_data.key_word_seaching


   if Innovation.objects.filter(student=request.user.id, stage=1).exists():
       innovation_stage_1_data=Innovation.objects.get(student=request.user.id, stage=1)
       average_score_stage_1[7] = innovation_stage_1_data.rating

       innovation_stage_1[0]=innovation_stage_1_data.problem_validation
       innovation_stage_1[1] = innovation_stage_1_data.customer_development
       innovation_stage_1[2] = innovation_stage_1_data.solution_alternatives_exploration
       innovation_stage_1[3] = innovation_stage_1_data.problem_validation
       innovation_stage_1[4] = innovation_stage_1_data.grant_proposal_writing
       innovation_stage_1[5] = innovation_stage_1_data.milestones_planning_reporting



   if Innovation.objects.filter(student=request.user.id, stage=2).exists():
       innovation_stage_2_data = Innovation.objects.get(student=request.user.id, stage=2)
       average_score_stage_2[7] = innovation_stage_2_data.rating

       innovation_stage_2[0] = innovation_stage_2_data.problem_validation
       innovation_stage_2[1] = innovation_stage_2_data.customer_development
       innovation_stage_2[2] = innovation_stage_2_data.solution_alternatives_exploration
       innovation_stage_2[3] = innovation_stage_2_data.problem_validation
       innovation_stage_2[4] = innovation_stage_2_data.grant_proposal_writing
       innovation_stage_2[5] = innovation_stage_2_data.milestones_planning_reporting

   if Innovation.objects.filter(student=request.user.id, stage=3).exists():
       innovation_stage_3_data = Innovation.objects.get(student=request.user.id, stage=3)

       average_score_stage_3[7] = innovation_stage_3_data.rating

       innovation_stage_3[0] = innovation_stage_3_data.problem_validation
       innovation_stage_3[1] = innovation_stage_3_data.customer_development
       innovation_stage_3[2] = innovation_stage_3_data.solution_alternatives_exploration
       innovation_stage_3[3] = innovation_stage_3_data.problem_validation
       innovation_stage_3[4] = innovation_stage_3_data.grant_proposal_writing
       innovation_stage_3[5] = innovation_stage_3_data.milestones_planning_reporting


   score={
       "state_1":average_score_stage_1,
       "stage_2":average_score_stage_2,
       "stage_3":average_score_stage_3
   }
   student=Student.objects.get(username=request.user.username)

   print(score)

   return render(request, "../../students/templates/basetemplate/templates/student/chart.html", {"user_name":name, "stage_1_rating":average_score_stage_1,
                                                                              "stage_2_rating":average_score_stage_2,
                                                                              "stage_3_rating":average_score_stage_3,
                                                                              "hardware_iot_stage_1":hardware_iot_stage_1,
                                                                              "hardware_iot_stage_2": hardware_iot_stage_2,
                                                                              "hardware_iot_stage_3": hardware_iot_stage_3,
                                                                              "ai_stage_1":ai_stage_1,
                                                                              "ai_stage_2": ai_stage_2,
                                                                              "ai_stage_3": ai_stage_3,
                                                                              "software_stage_1":software_stage_1,
                                                                              "software_stage_2": software_stage_2,
                                                                                                 "software_stage_3": software_stage_3,
                                                                                                 "product_design_stage_1":product_design_stage_1,
                                                                                                 "product_design_stage_2": product_design_stage_2,
                                                                                                 "product_design_stage_3": product_design_stage_3,
                                                                                                 "software_platforms_stage_1":software_platforms_stage_1,
                                                                                                 "software_platforms_stage_2": software_platforms_stage_2,
                                                                                                 "software_platforms_stage_3": software_platforms_stage_3,
                                                                                                 "programming_stage_1":programming_stage_1,
                                                                                                 "programming_stage_2": programming_stage_2,
                                                                                                 "programming_stage_3": programming_stage_3,

                                                                                                 "intellectual_property_stage_1":intellectual_property_stage_1,
                                                                                                 "intellectual_property_stage_2": intellectual_property_stage_2,
                                                                                                 "intellectual_property_stage_3": intellectual_property_stage_3,

                                                                                                 "innovation_stage_1":innovation_stage_1,
                                                                                                 "innovation_stage_2": innovation_stage_2,
                                                                                                 "innovation_stage_3": innovation_stage_3,

                                                                                                 })


@login_required(redirect_field_name='/login')
def hardware_iot(request):
    if request.method == 'POST':
        form=Hardware_iot_forms(request.POST)

        if form.is_valid():
            stage=int(request.POST.get("stage"))
            if Hardware_iot.objects.filter(student_id=request.user.id,stage=stage).exists():
                   student_stage=Hardware_iot.objects.get(student_id=request.user.id,stage=stage)
                   student_stage.delete()
            student=Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("hardware_iot")
    else :
        form = Hardware_iot_forms()
        try:
           hwd=Hardware_iot.objects.filter(student=request.user.id).last()
           last_update=timezone.localtime(hwd.updated_at)
        except Exception as e:
            print("exeption in hardware iot last update",e)
            last_update=None

        name=request.user.first_name+" "+request.user.last_name
        if name is None:
            name="admin"
        page_name = "Hardware/Iot"
        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name,"page_name":page_name})


@login_required(redirect_field_name='/login')
def ai(request):
    if request.method == 'POST':
        form = Ai_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Ai.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Ai.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()

            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("ai")
    else:
        form = Ai_form()
        try:
            ai = Ai.objects.filter(student=request.user.id).last()
            last_update = ai.updated_at

        except Exception as e:
            print(e)
            last_update = None

        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"
        page_name = "AI/ML/Data Science"
        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name, "page_name": page_name})
@login_required(redirect_field_name='/login')
def software(request):
    if request.method == 'POST':
        form = Software_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Software.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Software.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()
            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("software")
    else:
        form = Software_form()
        try:
            software = Software_form.objects.filter(student=request.user.id).last()
            last_update = software.updated_at

        except Exception as e:
            print(e)
            last_update = None
        page_name = "Software/Application Development"
        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"

        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name, "page_name": page_name})
@login_required(redirect_field_name='/login')
def product_design(request):
    if request.method == 'POST':
        form = Product_design_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Product_design.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Product_design.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()
            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("product_design")
    else:
        form = Product_design_form()
        try:
            pd = Product_design_form.objects.filter(student=request.user.id).last()
            last_update = pd.updated_at
        except Exception as e:
            print(e)
            last_update = None
        page_name = "Product/Industrial Design"
        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"

        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name, "page_name": page_name})
@login_required(redirect_field_name='/login')
def software_platforms(request):
    if request.method == 'POST':
        form = Software_platforms_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Software_platforms.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Software_platforms.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()
            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("software_platforms")
    else:
        form = Software_platforms_form()
        try:
            sp = Software_platforms_form.objects.filter(student=request.user.id).last()
            last_update = sp.updated_at
        except Exception as e:
            print(e)
            last_update = None

        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"
        page_name = "Software Platform"
        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name, "page_name": page_name})
@login_required(redirect_field_name='/login')
def programming(request):
    if request.method == 'POST':
        form = Programming_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Programming.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Programming.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()
            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("programming")
    else:
        form = Programming_form()
        try:
            p = Programming_form.objects.filter(student=request.user.id).last()
            last_update = p.updated_at
        except Exception as e:
            print(e)
            last_update = None

        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"
        page_name = "Programming - Application Platform"

        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name, "page_name": page_name})
@login_required(redirect_field_name='/login')
def intellectual_property(request):
    if request.method == 'POST':
        form = Intellectual_Property_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Intellectual_Property.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Intellectual_Property.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()
            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("intellectual_property")
    else:
        form = Intellectual_Property_form()
        try:
            ip = Intellectual_Property_form.objects.filter(student=request.user.id).last()
            last_update = ip.updated_at
        except Exception as e:
            print(e)
            last_update = None

        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"
        page_name = "IPR"

        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name, "page_name": page_name})

@login_required(redirect_field_name='/login')
def innovation(request):
    if request.method == 'POST':
        form = Innovation_form(request.POST)
        if form.is_valid():
            stage = int(request.POST.get("stage"))
            if Innovation.objects.filter(student_id=request.user.id, stage=stage).exists():
                student_stage = Innovation.objects.get(student_id=request.user.id, stage=stage)
                student_stage.delete()
            student = Student.objects.get(email=request.user.email)
            form.save(student)
            return redirect("innovation")
    else:
        form = Innovation_form()
        try:
            i = Innovation_form.objects.filter(student=request.user.id).last()
            last_update = i.updated_at
        except Exception as e:
            print(e)
            last_update = None

        name = request.user.first_name + " " + request.user.last_name
        if name is None:
            name = "User"
        page_name="Innovation"

        return render(request, '../templates/basetemplate/templates/student/update_gie.html',
                      {'form': form, "last_updated": last_update, "user_name": name,"page_name":page_name})

@login_required(redirect_field_name='/login')
def logout_request(request):
    logout(request)
    return redirect("login")


def dummytaskinit(request):
    every_monday_morning()
    return HttpResponse("tasked started !!")

def every_monday_morning():
    print("This is run every Monday morning at 7:30")

