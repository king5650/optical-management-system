from datetime import datetime, timezone
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

##################################################################################################################
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def get_logged_in_user(request):
    """
    View to return the logged-in user's information.
    """
    user = request.user  # This will be an instance of CustomUser
    return JsonResponse({
        "username": user.username,
        "email": user.email,
        "role": user.get_role_display(),  # Get the human-readable role
        "contact": user.contact,
        "profile_picture": user.profile_picture.url if user.profile_picture else None,
        "date_joined": user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
    })
    

import subprocess
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
import datetime

# def backup_database(request):
#     if not request.user.is_superuser:
#         return HttpResponse("Unauthorized", status=403)

#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
#     backup_filename = f"backup_{timestamp}.sql"
#     backup_path = os.path.join(settings.BASE_DIR, "backups", backup_filename)

#     try:
#         os.makedirs(os.path.dirname(backup_path), exist_ok=True)

#         subprocess.run([
#             'pg_dump',
#             '-h', 'localhost',
#             '-U', 'admin',
#             '-d', 'optical_cabinet',
#             '-f', backup_path
#         ], check=True)

#         return FileResponse(open(backup_path, 'rb'), as_attachment=True, filename=backup_filename)
#     except subprocess.CalledProcessError as e:
#         return HttpResponse(f"Backup failed: {str(e)}", status=500)
# ##################################################################################################################################


@csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect based on user role
            if user.role == 'admin':
                return JsonResponse({'redirect': 'admin_dashboard'})
            elif user.role == 'secretary':
                return JsonResponse({'redirect': 'Home_page'})
            elif user.role == 'stockist':
                return JsonResponse({'redirect': 'inventory_management'})
            else:  # Default for 'patient' or any other role
                return JsonResponse({'redirect': 'patient_home'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'GET method not allowed'}, status=405)

from django.http import JsonResponse
from .models import Patient, SaleEntry

def dashboard_counts(request):
    """
    Returns counts for inventory, appointments, and patients.
    You can add more as needed.
    """
    patient_count = Patient.objects.count()
    sales_count = SaleEntry.objects.count()
    medical_report_count = MedicalReports.objects.count()
    inventory_count = InventoryItem.objects.count()
    # patient_count = Patient.objects.count()

    # You can add more fields as needed
    data = {
        "patient_count": patient_count,
        "sales_count":  sales_count,
        "medical_report_count": medical_report_count,
        "inventory_count": inventory_count,
        
    #     "appointment_count": appointment_count,
    #     "patient_count": patient_count,
    }
    return JsonResponse(data)


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Patient

@csrf_exempt
def add_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            patient = Patient.objects.create(
                name=data['name'],
                contact=data['contact'],
                email=data['email'],
                # address=data['address'],
                address=data.get('address', 'Yaoundé'),
                profession=data.get('profession', ''),
                age=data['age'],
                gender=data['gender']
            )
            return JsonResponse({'message': 'Patient added successfully!', 'id': patient.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update_patient(request, patient_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = get_object_or_404(Patient, id=patient_id)
        try:
            patient.name = data['name']
            patient.contact = data['contact']
            patient.email = data['email']
            patient.address = data['address']
            patient.profession = data['profession']
            patient.age = data['age']
            patient.gender = data['gender']
            patient.save()
            return JsonResponse({'message': 'Patient updated successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_patient(request, patient_id):
    if request.method == 'DELETE':
        patient = get_object_or_404(Patient, id=patient_id)
        patient.delete()
        return JsonResponse({'message': 'Patient deleted successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_patients(request):
    if request.method == 'GET':
        patients = list(Patient.objects.values())
        return JsonResponse({'patients': patients})
    return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.db.models import Q

def search_patients(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')  # Get the search query
        if query:
            # Search by name, email, or contact (case-insensitive)
            patients = Patient.objects.filter(
                Q(name__icontains=query) | Q(email__icontains=query) | Q(contact__icontains=query)
            ).values()
        else:
            # If no query, return all patients
            patients = Patient.objects.values()
        return JsonResponse({'patients': list(patients)})
    return JsonResponse({'error': 'Invalid request method'}, status=405)



from django.http import JsonResponse
from django.db.models import Q

def search_patients(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        patients = Patient.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(contact__icontains=query)
        ).values()
        return JsonResponse({'patients': list(patients)})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def list_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.values()
        return JsonResponse({'patients': list(patients)})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
###############################################################################################################################################




###############################################################################################################################################
#medical prescription system
##########################################################################################################################################################
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import MedicalReports, PrescriptionDetail, Refraction, Patient

# @csrf_exempt
# def create_medical_reportss(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             patient_id = data.get('patient_id')
#             patient = Patient.objects.get(id=patient_id)

#             # Save Medical Report
#             report = MedicalReports.objects.create(
#                 patient=patient,
#                 age_at_report=data.get('age'),
#                 profession_at_report=data.get('profession')
#             )

#             # Save Refraction
#             Refraction.objects.create(
#                 medical_report=report,
#                 sphere_od=data.get('sphere_od'),
#                 cyl_od=data.get('cyl_od'),
#                 axe_od=data.get('axe_od'),
#                 addition_od=data.get('addition_od'),
#                 sphere_og=data.get('sphere_og'),
#                 cyl_og=data.get('cyl_og'),
#                 axe_og=data.get('axe_og'),
#                 addition_og=data.get('addition_og')
#             )

#             # Save Prescription Details
#             PrescriptionDetail.objects.create(
#                 medical_report=report,
#                 ametropie=data.get('ametropie'),
#                 types_de_verre=data.get('types_de_verre'),
#                 teintes=data.get('teintes'),
#                 foyers=data.get('foyers'),
#                 port=data.get('port'),
#                 indice=data.get('indice')
#             )

#             return JsonResponse({'message': 'Medical report saved successfully!'}, status=200)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# import json
# from .models import Patient, MedicalReports, Refraction, PrescriptionDetail

# @csrf_exempt
# @require_http_methods(["POST"])
# def create_medical_report121(request):
#     try:
#         data = json.loads(request.body)

#         # 1. Retrieve the patient
#         patient_id = data.get("patient_id")
#         patient = Patient.objects.get(id=patient_id)

#         # 2. Save MedicalReport
#         report = MedicalReports.objects.create(
#             patient=patient,
#             age_at_report=data.get("age"),
#             profession_at_report=data.get("profession"),
#             pdf_file=None  # Optional for now
#         )

#         # 3. Save Refraction data
#         Refraction.objects.create(
#             medical_report=report,
#             sphere_od=data.get("sphere_od", ""),
#             cyl_od=data.get("cyl_od", ""),
#             axe_od=data.get("axe_od", ""),
#             addition_od=data.get("addition_od", ""),
#             sphere_og=data.get("sphere_og", ""),
#             cyl_og=data.get("cyl_og", ""),
#             axe_og=data.get("axe_og", ""),
#             addition_og=data.get("addition_og", "")
#         )

#         # 4. Save PrescriptionDetail
#         PrescriptionDetail.objects.create(
#             medical_report=report,
#             ametropie=data.get("ametropie", ""),
#             types_de_verre=data.get("types_de_verre", ""),
#             teintes=data.get("teintes", ""),
#             foyers=data.get("foyers", ""),
#             port=data.get("port", ""),
#             indice=data.get("indice", "")
#         )

#         return JsonResponse({'message': 'Medical report saved successfully! ✅'})

#     except Patient.DoesNotExist:
#         return JsonResponse({'error': 'Patient not found.'}, status=404)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)



# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json
# from .models import MedicalReports, Refraction, PrescriptionDetail
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def create_medical_report(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             # Step 1: Create the Medical Report
#             medical_report = MedicalReports.objects.create(
#                 patient_id=data.get('patient_id'),
#                 age_at_report=data.get('age_at_report'),
#                 profession_at_report=data.get('profession_at_report'),
#             )

#             # Step 2: Create Refraction linked to Medical Report
#             Refraction.objects.create(
#                 medical_report=medical_report,
#                 sphere_od=data.get('sphere_od', ''),
#                 cyl_od=data.get('cyl_od', ''),
#                 axe_od=data.get('axe_od', ''),
#                 addition_od=data.get('addition_od', ''),
#                 sphere_og=data.get('sphere_og', ''),
#                 cyl_og=data.get('cyl_og', ''),
#                 axe_og=data.get('axe_og', ''),
#                 addition_og=data.get('addition_og', ''),
#             )

#             # Step 3: Create PrescriptionDetail linked to Medical Report
#             PrescriptionDetail.objects.create(
#                 medical_report=medical_report,
#                 ametropie=data.get('ametropie', ''),
#                 types_de_verre=data.get('types_de_verre', ''),
#                 teintes=data.get('teintes', ''),
#                 foyers=data.get('foyers', ''),
#                 port=data.get('port', ''),
#                 indice=data.get('indice', ''),
#             )

#             return JsonResponse({"message": "Medical report saved successfully!"})

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"error": "Invalid request method"}, status=405)

# @csrf_exempt
# def create_medical_report(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             # Step 1: Create the Medical Report
#             medical_report = MedicalReports.objects.create(
#                 patient_id=data.get('patient_id'),
#                 age_at_report=data.get('age_at_report'),
#                 profession_at_report=data.get('profession_at_report'),
#             )

#             # Step 2: Create Refraction
#             Refraction.objects.create(
#                 medical_report=medical_report,
#                 sphere_od=data.get('sphere_od', ''),
#                 cyl_od=data.get('cyl_od', ''),
#                 axe_od=data.get('axe_od', ''),
#                 addition_od=data.get('addition_od', ''),
#                 sphere_og=data.get('sphere_og', ''),
#                 cyl_og=data.get('cyl_og', ''),
#                 axe_og=data.get('axe_og', ''),
#                 addition_og=data.get('addition_og', ''),
#             )

#             # Step 3: Create PrescriptionDetail
#             PrescriptionDetail.objects.create(
#                 medical_report=medical_report,
#                 ametropie=",".join(data.get("ametropie", [])),
#                 types_de_verre=",".join(data.get("types_de_verre", [])),
#                 teintes=",".join(data.get("teintes", [])),
#                 foyers=",".join(data.get("foyers", [])),
#                 port=",".join(data.get("port", [])),
#                 indice=",".join(data.get("indice", [])),
#             )

#             return JsonResponse({"message": "Medical report saved successfully!"})

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def create_medical_report(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reference_id = data.get('reference_id')
            medical_report = MedicalReports.objects.create(
                patient_id=data.get('patient_id'),
                age_at_report=data.get('age_at_report'),
                profession_at_report=data.get('profession_at_report'),
                reference_id=reference_id,
            )

            Refraction.objects.create(
                medical_report=medical_report,
                sphere_od=data.get('sphere_od', ''),
                cyl_od=data.get('cyl_od', ''),
                axe_od=data.get('axe_od', ''),
                addition_od=data.get('addition_od', ''),
                sphere_og=data.get('sphere_og', ''),
                cyl_og=data.get('cyl_og', ''),
                axe_og=data.get('axe_og', ''),
                addition_og=data.get('addition_og', ''),
            )

            PrescriptionDetail.objects.create(
                medical_report=medical_report,
                ametropie=data.get('ametropie', ''),
                types_de_verre=data.get('types_de_verre', ''),
                teintes=data.get('teintes', ''),
                foyers=data.get('foyers', ''),
                port=data.get('port', ''),
                indice=data.get('indice', ''),
            )

            return JsonResponse({
                "message": "Medical report saved successfully!",
                "report_id": medical_report.id  # Return the report ID for frontend use
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import MedicalReports, Refraction, PrescriptionDetail
from django.shortcuts import get_object_or_404

@csrf_exempt
def view_medical_report(request, report_id):
    if request.method == 'GET':
        try:
            report = get_object_or_404(MedicalReports, pk=report_id)
            refraction = getattr(report, 'refraction', None)
            prescription = getattr(report, 'prescription', None)

            data = {
                "report_id": report.id,
                "patient_id": report.patient.id,
                "patient_name": report.patient.name,
                # "age": report.age_at_report,
                "sexe": report.patient.gender,
                # "profession": report.profession_at_report,
                "age_at_report": report.age_at_report,  # <- fix here
                "sexe": report.patient.gender,
                "profession_at_report": report.profession_at_report,  # <- fix here
                "date": report.date.strftime('%Y-%m-%d'),
                # "reference": f"Pre-{report.id:06d}"
                "reference_id": report.reference_id,

            }

            # Add refraction data if available
            if refraction:
                data.update({
                    "sphere_od": refraction.sphere_od,
                    "cyl_od": refraction.cyl_od,
                    "axe_od": refraction.axe_od,
                    "addition_od": refraction.addition_od,
                    "sphere_og": refraction.sphere_og,
                    "cyl_og": refraction.cyl_og,
                    "axe_og": refraction.axe_og,
                    "addition_og": refraction.addition_og,
                })

            # Add prescription data if available
            if prescription:
                data.update({
                    "ametropie": prescription.ametropie,
                    "types_de_verre": prescription.types_de_verre,
                    "teintes": prescription.teintes,
                    "foyers": prescription.foyers,
                    "port": prescription.port,
                    "indice": prescription.indice,
                })

            return JsonResponse(data)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)


from django.http import JsonResponse
from .models import MedicalReports

def get_next_reference_id(request):
    last_report = MedicalReports.objects.order_by('-id').first()
    next_number = (last_report.id + 1) if last_report else 1
    formatted = f"Pre-{next_number:06d}"
    return JsonResponse({"reference_id": formatted})


def get_medical_report_by_reference(request, reference_id):
    try:
        report = MedicalReports.objects.get(reference_id=reference_id)
        refraction = Refraction.objects.get(medical_report=report)
        prescription = PrescriptionDetail.objects.get(medical_report=report)

        return JsonResponse({
            "reference_id": report.reference_id,
            "patient_id": report.patient.id,
            "patient_name": report.patient.name,
            "age_at_report": report.age_at_report,
            "profession_at_report": report.profession_at_report,
            "date": report.date.strftime('%Y-%m-%d'),
            "refraction": {
                "sphere_od": refraction.sphere_od,
                "cyl_od": refraction.cyl_od,
                "axe_od": refraction.axe_od,
                "addition_od": refraction.addition_od,
                "sphere_og": refraction.sphere_og,
                "cyl_og": refraction.cyl_og,
                "axe_og": refraction.axe_og,
                "addition_og": refraction.addition_og,
                
            },
            "prescription": {
                "ametropie": prescription.ametropie,
                "types_de_verre": prescription.types_de_verre,
                "teintes": prescription.teintes,
                "foyers": prescription.foyers,
                "port": prescription.port,
                "indice": prescription.indice,
#             }
            }
        })
    except MedicalReports.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)



# def get_next_reference_id(request):
#     last = MedicalReports.objects.order_by('-id').first()
#     next_id = last.id + 1 if last else 1
#     return JsonResponse({"reference_id": f"Pre-{next_id:06d}"})

# from django.http import JsonResponse
# from .models import MedicalReports, Refraction, PrescriptionDetail

# def view_medical_report(request, report_id):
#     try:
#         report = MedicalReports.objects.get(id=report_id)
#         refraction = Refraction.objects.get(medical_report=report)
#         prescription = PrescriptionDetail.objects.get(medical_report=report)

#         return JsonResponse({
#             "report_id": report.id,
#             "patient_id": report.patient.id,
#             "patient_name": report.patient.name,
#             "age": report.age_at_report,
#             "profession": report.profession_at_report,
#             "date": str(report.date),
#             "refraction": {
#                 "sphere_od": refraction.sphere_od,
#                 "cyl_od": refraction.cyl_od,
#                 "axe_od": refraction.axe_od,
#                 "addition_od": refraction.addition_od,
#                 "sphere_og": refraction.sphere_og,
#                 "cyl_og": refraction.cyl_og,
#                 "axe_og": refraction.axe_og,
#                 "addition_og": refraction.addition_og,
#             },
#             "prescription": {
#                 "ametropie": prescription.ametropie,
#                 "types_de_verre": prescription.types_de_verre,
#                 "teintes": prescription.teintes,
#                 "foyers": prescription.foyers,
#                 "port": prescription.port,
#                 "indice": prescription.indice,
#             }
#         })

#     except MedicalReports.DoesNotExist:
#         return JsonResponse({"error": "Medical report not found."}, status=404)
#     except Refraction.DoesNotExist:
#         return JsonResponse({"error": "Refraction not found."}, status=404)
#     except PrescriptionDetail.DoesNotExist:
#         return JsonResponse({"error": "Prescription detail not found."}, status=404)



# from django.http import JsonResponse
# from .models import MedicalReports

# def get_latest_report_for_patient(request, patient_id):
#     try:
#         latest = MedicalReports.objects.filter(patient_id=patient_id).order_by('-id').first()
#         if latest:
#             return JsonResponse({"report_id": latest.id})
#         else:
#             return JsonResponse({"report_id": None})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)

#####################################################################################################################################
# whatsapp automation
from rest_framework import generics, status
from rest_framework.response import Response
from .models import ScheduledMessage
from .serializers import (
    ScheduledMessageSerializer,
    ScheduledMessageDetailSerializer,
)

# Schedule a new message
class ScheduleMessageView(generics.CreateAPIView):
    serializer_class = ScheduledMessageSerializer

# List all scheduled messages
class ListScheduledMessagesView(generics.ListAPIView):
    queryset = ScheduledMessage.objects.all().order_by('-scheduled_time')
    serializer_class = ScheduledMessageDetailSerializer

# Cancel a message
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class CancelScheduledMessageView(APIView):
    def post(self, request, pk):
        message = get_object_or_404(ScheduledMessage, pk=pk)
        if message.status == "pending":
            message.status = "cancelled"
            message.save()
            return Response({"detail": "Message cancelled."})
        return Response({"detail": "Message cannot be cancelled."}, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MessageRecipient
from rest_framework import status

class UpdateRecipientStatusView(APIView):
    def post(self, request, pk):
        recipient = MessageRecipient.objects.get(pk=pk)
        recipient.status = request.data.get("status", recipient.status)
        recipient.error_message = request.data.get("error_message", recipient.error_message)
        recipient.sent_at = timezone.now() if recipient.status == 'sent' else None
        recipient.save()
        return Response({"detail": "Status updated."}, status=status.HTTP_200_OK)

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ScheduledMessage, MessageRecipient, Patient
from django.utils.dateparse import parse_datetime

@csrf_exempt
def create_scheduled_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            message_text = data.get('message')
            send_at = parse_datetime(data.get('send_at'))
            is_broadcast = data.get('is_broadcast', False)
            recipient_ids = data.get('recipient_ids', [])

            if not message_text or not send_at:
                return JsonResponse({'error': 'Message and send_at are required.'}, status=400)

            msg = ScheduledMessage.objects.create(
                message=message_text,
                send_at=send_at,
                is_broadcast=is_broadcast
            )

            if is_broadcast:
                patients = Patient.objects.all()
            else:
                patients = Patient.objects.filter(id__in=recipient_ids)

            for patient in patients:
                MessageRecipient.objects.create(
                    message=msg,
                    patient=patient,
                    status='pending'
                )

            return JsonResponse({'success': 'Message scheduled successfully.'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


##########################################################################################################################


######################################backup system#########################################################

# # views.py
# import subprocess
# import os
# import datetime
# from django.http import JsonResponse
# from django.conf import settings

# def backup_database(request):
#     try:
#         # Create a timestamped filename
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"backup_{timestamp}.sql"
#         backup_dir = request.GET.get("path")

#         if not backup_dir:
#             return JsonResponse({"error": "No backup path provided."}, status=400)

#         backup_path = os.path.join(backup_dir, filename)

#         db_settings = settings.DATABASES['default']
#         user = db_settings['USER']
#         password = db_settings['PASSWORD']
#         dbname = db_settings['NAME']
#         host = db_settings['HOST']
#         port = db_settings['PORT']

#         env = os.environ.copy()
#         env["PGPASSWORD"] = password

#         command = [
#             'pg_dump',
#             '-h', host,
#             '-p', str(port),
#             '-U', user,
#             '-F', 'c',
#             '-f', backup_path,
#             dbname,
#         ]

#         subprocess.run(command, env=env, check=True)

#         return JsonResponse({"message": "Backup created", "file": backup_path})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


# def restore_database(request):
#     try:
#         file_path = request.GET.get("file")
#         if not file_path:
#             return JsonResponse({"error": "No file provided"}, status=400)

#         db_settings = settings.DATABASES['default']
#         user = db_settings['USER']
#         password = db_settings['PASSWORD']
#         dbname = db_settings['NAME']
#         host = db_settings['HOST']
#         port = db_settings['PORT']

#         env = os.environ.copy()
#         env["PGPASSWORD"] = password

#         command = [
#             'pg_restore',
#             '-h', host,
#             '-p', str(port),
#             '-U', user,
#             '-d', dbname,
#             '-c',  # Drop objects before recreating them
#             file_path
#         ]

#         subprocess.run(command, env=env, check=True)

#         return JsonResponse({"message": "Restore completed successfully."})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


import subprocess
import os
import datetime
import shutil
import zipfile
import tempfile

from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# @require_http_methods(["POST"])
# @csrf_exempt
# def backup_database(request):
#     try:
#         backup_dir = request.POST.get("path")
#         if not backup_dir:
#             return JsonResponse({"error": "No backup path provided."}, status=400)

#         if not os.path.exists(backup_dir):
#             return JsonResponse({"error": "Provided path does not exist."}, status=400)

#         # Generate timestamp and temp paths
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         backup_name = f"backup_{timestamp}"
#         dump_file = os.path.join(tempfile.gettempdir(), f"{backup_name}.dump")
#         zip_file_path = os.path.join(backup_dir, f"{backup_name}.zip")

#         # Get DB credentials
#         db = settings.DATABASES['default']
#         env = os.environ.copy()
#         env["PGPASSWORD"] = db['PASSWORD']

#         dump_command = [
#             # 'pg_dump',
#             settings.PSQL_BIN_DIR,  # Full path from settings.py
#             '-h', db['HOST'],
#             '-p', str(db['PORT']),
#             '-U', db['USER'],
#             '-F', 'c',  # Custom format
#             '-f', dump_file,
#             db['NAME'],
#         ]

#         subprocess.run(dump_command, env=env, check=True)

#         # Create ZIP file with DB dump + media/
#         with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#             zipf.write(dump_file, arcname="db.dump")
#             media_root = settings.MEDIA_ROOT
#             for root, dirs, files in os.walk(media_root):
#                 for file in files:
#                     abs_path = os.path.join(root, file)
#                     rel_path = os.path.relpath(abs_path, media_root)
#                     zipf.write(abs_path, arcname=os.path.join("media", rel_path))

#         os.remove(dump_file)  # Clean up temp dump

#         return JsonResponse({"message": "Backup created successfully.", "file": zip_file_path})

#     except subprocess.CalledProcessError as e:
#         return JsonResponse({"error": "Backup failed. " + str(e)}, status=500)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


# @require_http_methods(["POST"])
# @csrf_exempt
# def restore_database(request):
#     try:
#         file_path = request.POST.get("file")
#         if not file_path:
#             return JsonResponse({"error": "No file provided."}, status=400)

#         if not os.path.exists(file_path):
#             return JsonResponse({"error": "Backup file not found."}, status=404)

#         # Unzip to temp directory
#         with tempfile.TemporaryDirectory() as temp_dir:
#             with zipfile.ZipFile(file_path, 'r') as zipf:
#                 zipf.extractall(temp_dir)

#             dump_file = os.path.join(temp_dir, "db.dump")
#             media_folder = os.path.join(temp_dir, "media")

#             if not os.path.exists(dump_file):
#                 return JsonResponse({"error": "Invalid backup file: db.dump missing"}, status=400)

#             # Restore database
#             db = settings.DATABASES['default']
#             env = os.environ.copy()
#             env["PGPASSWORD"] = db['PASSWORD']

#             restore_command = [
#                 'pg_restore',
#                 '-h', db['HOST'],
#                 '-p', str(db['PORT']),
#                 '-U', db['USER'],
#                 '-d', db['NAME'],
#                 '-c',  # Drop existing objects
#                 dump_file,
#             ]

#             subprocess.run(restore_command, env=env, check=True)

#             # Restore media files
#             if os.path.exists(media_folder):
#                 for root, dirs, files in os.walk(media_folder):
#                     for file in files:
#                         abs_src_path = os.path.join(root, file)
#                         rel_path = os.path.relpath(abs_src_path, media_folder)
#                         dest_path = os.path.join(settings.MEDIA_ROOT, rel_path)

#                         os.makedirs(os.path.dirname(dest_path), exist_ok=True)
#                         shutil.copy2(abs_src_path, dest_path)

#         return JsonResponse({"message": "Restore completed successfully."})

#     except subprocess.CalledProcessError as e:
#         return JsonResponse({"error": "Restore failed. " + str(e)}, status=500)
#     except zipfile.BadZipFile:
#         return JsonResponse({"error": "Invalid zip archive provided."}, status=400)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)
import os
import datetime
import tempfile
import zipfile
import shutil
import subprocess
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
@csrf_exempt
def backup_database(request):
    try:
        backup_dir = request.POST.get("path")
        if not backup_dir:
            return JsonResponse({"error": "No backup path provided."}, status=400)

        if not os.path.exists(backup_dir):
            return JsonResponse({"error": "Provided path does not exist."}, status=400)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}"
        dump_file = os.path.join(tempfile.gettempdir(), f"{backup_name}.dump")
        zip_file_path = os.path.join(backup_dir, f"{backup_name}.zip")

        db = settings.DATABASES['default']
        env = os.environ.copy()
        env["PGPASSWORD"] = db['PASSWORD']

        dump_command = [
            settings.PG_DUMP_PATH,
            '-h', db['HOST'],
            '-p', str(db['PORT']),
            '-U', db['USER'],
            '-F', 'c',
            '-f', dump_file,
            db['NAME'],
        ]

        subprocess.run(dump_command, env=env, check=True)

        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(dump_file, arcname="db.dump")
            media_root = settings.MEDIA_ROOT
            for root, dirs, files in os.walk(media_root):
                for file in files:
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, media_root)
                    zipf.write(abs_path, arcname=os.path.join("media", rel_path))

        os.remove(dump_file)

        return JsonResponse({"message": "Backup created successfully.", "file": zip_file_path})

    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": f"Backup failed: {e}"}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_http_methods(["POST"])
@csrf_exempt
def restore_database(request):
    try:
        file_path = request.POST.get("file")
        if not file_path:
            return JsonResponse({"error": "No file provided."}, status=400)

        if not os.path.exists(file_path):
            return JsonResponse({"error": "Backup file not found."}, status=404)

        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(file_path, 'r') as zipf:
                zipf.extractall(temp_dir)

            dump_file = os.path.join(temp_dir, "db.dump")
            media_folder = os.path.join(temp_dir, "media")

            if not os.path.exists(dump_file):
                return JsonResponse({"error": "Invalid backup file: db.dump missing"}, status=400)

            db = settings.DATABASES['default']
            env = os.environ.copy()
            env["PGPASSWORD"] = db['PASSWORD']

            restore_command = [
                settings.PG_RESTORE_PATH,
                '-h', db['HOST'],
                '-p', str(db['PORT']),
                '-U', db['USER'],
                '-d', db['NAME'],
                '-c',
                dump_file,
            ]

            subprocess.run(restore_command, env=env, check=True)

            if os.path.exists(media_folder):
                for root, dirs, files in os.walk(media_folder):
                    for file in files:
                        abs_src_path = os.path.join(root, file)
                        rel_path = os.path.relpath(abs_src_path, media_folder)
                        dest_path = os.path.join(settings.MEDIA_ROOT, rel_path)

                        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                        shutil.copy2(abs_src_path, dest_path)

        return JsonResponse({"message": "Restore completed successfully."})

    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": f"Restore failed: {e}"}, status=500)
    except zipfile.BadZipFile:
        return JsonResponse({"error": "Invalid zip archive provided."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)








################################################ end######################

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import MedicalReport, Patient
import json

# @csrf_exempt  # Optional: Remove if CSRF is handled on the frontend
# @require_POST
# def save_medical_report(request):
#     try:
#         data = json.loads(request.body)
        
#         # Log received data for debugging
#         print("Received data:", data)
        
#         # Fetch the patient by ID
#         try:
#             patient = Patient.objects.get(id=data['patient_id'])
#         except Patient.DoesNotExist:
#             return JsonResponse({'error': 'Patient not found'}, status=404)
        
#         # Create the medical report
#         MedicalReport.objects.create(
#             patient=patient,
#             age=data['age'],
#             sexe=data['sexe'],
#             profession=data['profession'],
#             sphere_od=data['sphere_od'],
#             cyl_od=data['cyl_od'],
#             axe_od=data['axe_od'],
#             addition_od=data['addition_od'],
#             sphere_og=data['sphere_og'],
#             cyl_og=data['cyl_og'],
#             axe_og=data['axe_og'],
#             addition_og=data['addition_og'],
#             ametropie=data.get('ametropie', ''),
#             types_de_verre=data.get('types_de_verre', ''),
#             teintes=data.get('teintes', ''),
#             foyers=data.get('foyers', ''),
#             port=data.get('port', ''),
#             indice=data.get('indice', '')
#         )

#         return JsonResponse({'message': 'Medical report saved successfully!'}, status=201)
    
#     except KeyError as e:
#         return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)
#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)



from django.http import JsonResponse
from .models import MedicalReport
from django.views.decorators.csrf import csrf_exempt

def search_medical_report(request, patient_id):
    """Retrieve a medical report by patient ID."""
    try:
        report = MedicalReport.objects.filter(patient__id=patient_id).first()
        if report:
            report_data = {
                "patient_id": report.patient.id,
                "age": report.age,
                "sexe": report.sexe,
                "profession": report.profession,
                "sphere_od": report.sphere_od,
                "cyl_od": report.cyl_od,
                "axe_od": report.axe_od,
                "addition_od": report.addition_od,
                "sphere_og": report.sphere_og,
                "cyl_og": report.cyl_og,
                "axe_og": report.axe_og,
                "addition_og": report.addition_og,
                "ametropie": report.ametropie,
                "types_de_verre": report.types_de_verre,
                "teintes": report.teintes,
                "foyers": report.foyers,
                "port": report.port,
                "indice": report.indice,
            }
            return JsonResponse(report_data, safe=False)
        else:
            return JsonResponse({'error': 'Medical report not found'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import MedicalReport, Patient
import json

@csrf_exempt
def save_medical_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
            
        print("Received data:", data)  # Debugging: Log the received data
        try:
            patient = Patient.objects.get(id=data['patient_id'])
            MedicalReport.objects.create(
                patient=patient,
                age=data['age'],
                sexe=data['sexe'],
                profession=data['profession'],
                sphere_od=data['sphere_od'],
                cyl_od=data['cyl_od'],
                axe_od=data['axe_od'],
                addition_od=data['addition_od'],
                sphere_og=data['sphere_og'],
                cyl_og=data['cyl_og'],
                axe_og=data['axe_og'],
                addition_og=data['addition_og'],
                ametropie=data.get('ametropie', ''),
                types_de_verre=data.get('types_de_verre', ''),
                teintes=data.get('teintes', ''),
                foyers=data.get('foyers', ''),
                port=data.get('port', ''),
                indice=data.get('indice', '')
            )
            return JsonResponse({'message': 'Medical report saved successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def get_medical_report(request, patient_id,):
    if request.method == 'GET':
        try:
            report = MedicalReport.objects.get(patient__id=patient_id)
       
            patient = report.patient  # Get the patient object
            print(f"Retrieved report for patient: {patient.name}")  # Debugging line
            # print(f"Retrieved report for patient: {report.patient.name}")  # Debugging line
            data = {
                "patient_id": report.patient.id,   
                "patient_name": report.patient.name,
                "age": report.age,
                "sexe": report.sexe,
                "profession": report.profession,
                "date_registered": report.date.strftime("%Y-%m-%d"),
                "sphere_od": report.sphere_od,
                "cyl_od": report.cyl_od,
                "axe_od": report.axe_od,
                "addition_od": report.addition_od,
                "sphere_og": report.sphere_og,
                "cyl_og": report.cyl_og,
                "axe_og": report.axe_og,
                "addition_og": report.addition_og,
                "ametropie": report.ametropie,
                "types_de_verre": report.types_de_verre,
                "teintes": report.teintes,
                "foyers": report.foyers,
                "port": report.port,
                "indice": report.indice,

            }
            return JsonResponse(data)
        except MedicalReport.DoesNotExist:
            return JsonResponse({'error': 'Medical report not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# @csrf_exempt
# def list_medical_reports(request, patient_id):
#     if request.method == 'GET':
#         try:
#             reports = MedicalReport.objects.filter(patient_id=patient_id).values(
#                 'id', 'ametropie', 'types_de_verre', 'teintes', 'foyers', 'port', 'indice','date_registered',
#             )
#             return JsonResponse({'reports': list(reports)})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MedicalReports, PrescriptionDetail

@csrf_exempt
def list_medical_reports(request, patient_id):
    if request.method == 'GET':
        try:
            reports = MedicalReports.objects.filter(patient_id=patient_id).select_related('prescription')

            report_list = []
            for report in reports:
                prescription = getattr(report, 'prescription', None)
                report_list.append({
                    'id': report.id,
                    'ametropie': ', '.join(prescription.ametropie) if prescription and prescription.ametropie else '',
                    'types_de_verre': ', '.join(prescription.types_de_verre) if prescription and prescription.types_de_verre else '',
                    'teintes': ', '.join(prescription.teintes) if prescription and prescription.teintes else '',
                    'foyers': ', '.join(prescription.foyers) if prescription and prescription.foyers else '',
                    'port': ', '.join(prescription.port) if prescription and prescription.port else '',
                    'indice': ', '.join(prescription.indice) if prescription and prescription.indice else '',
                    'date_registered': report.date.strftime('%Y-%m-%d'),
                })

            return JsonResponse({'reports': report_list})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



# @csrf_exempt
# def delete_medical_report(request, report_id):
#     if request.method == 'DELETE':
#         report = get_object_or_404(MedicalReport, id=report_id)
#         report.delete()
#         return JsonResponse({'message': 'Patient deleted successfully!'})
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import MedicalReport

@csrf_exempt
def delete_medical_report(request, report_id):
    if request.method == 'DELETE':
        try:
            report = MedicalReports.objects.get(id=report_id)
            report.delete()
            return JsonResponse({'message': 'Medical report deleted successfully!'})
        except MedicalReport.DoesNotExist:
            return JsonResponse({'error': 'Medical report not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def view_medical_report(request, report_id):
#     if request.method == 'GET':
#         try:
#             report = MedicalReport.objects.get(id=report_id)
#             data = {
#                 "patient_id": report.patient.id,
#                 "patient_name": report.patient.name,
#                 "age": report.age,
#                 "sexe": report.sexe,
#                 "profession": report.profession,
#                 "sphere_od": report.sphere_od,
#                 "cyl_od": report.cyl_od,
#                 "axe_od": report.axe_od,
#                 "addition_od": report.addition_od,
#                 "sphere_og": report.sphere_og,
#                 "cyl_og": report.cyl_og,
#                 "axe_og": report.axe_og,
#                 "addition_og": report.addition_og,
#                 "ametropie": report.ametropie,
#                 "types_de_verre": report.types_de_verre,
#                 "teintes": report.teintes,
#                 "foyers": report.foyers,
#                 "port": report.port,
#                 "indice": report.indice,
#             }
#             return JsonResponse(data)
#         except MedicalReport.DoesNotExist:
#             return JsonResponse({'error': 'Medical report not found'}, status=404)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Frame, Lens, OpticalAccessory
import json

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_type = data.get('item_type')
        try:
            if item_type == 'Frame':
                Frame.objects.create(
                    frame_type=data['item_subtype'],
                    unit_price=data['unit_price'],
                    stock_level=data['stock_level'],
                )
            elif item_type == 'Lens':
                Lens.objects.create(
                    lens_type=data['item_subtype'],
                    unit_price=data['unit_price'],
                    stock_level=data['stock_level'],
                )
            elif item_type == 'Optical Accessory':
                OpticalAccessory.objects.create(
                    name=data['item_subtype'],  # Name directly
                    unit_price=data['unit_price'],
                    stock_level=data['stock_level'],
                )
            return JsonResponse({'message': 'Item added successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.http import JsonResponse
from .models import Frame, Lens, OpticalAccessory

def list_frames(request):
    frames = Frame.objects.all().values("id", "frame_type", "stock_level", "unit_price", "date_added")
    return JsonResponse({"items": list(frames)})

def list_lenses(request):
    lenses = Lens.objects.all().values("id", "lens_type", "stock_level", "unit_price", "date_added")
    return JsonResponse({"items": list(lenses)})

def list_accessories(request):
    accessories = OpticalAccessory.objects.all().values("id", "name", "stock_level", "unit_price", "date_added")
    return JsonResponse({"items": list(accessories)})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Frame, Lens, OpticalAccessory

@csrf_exempt
def delete_item(request, item_type, item_id):
    """
    Delete an inventory item (Frame, Lens, or Optical Accessory).
    """
    if request.method == "DELETE":
        try:
            if item_type == "frames":
                item = Frame.objects.get(id=item_id)
            elif item_type == "lenses":
                item = Lens.objects.get(id=item_id)
            elif item_type == "accessories":
                item = OpticalAccessory.objects.get(id=item_id)
            else:
                return JsonResponse({"error": "Invalid item type"}, status=400)

            # Delete the item
            item.delete()
            return JsonResponse({"message": f"{item_type.capitalize()} item deleted successfully!"})
        except (Frame.DoesNotExist, Lens.DoesNotExist, OpticalAccessory.DoesNotExist):
            return JsonResponse({"error": "Item not found"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=405)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Frame, Lens, OpticalAccessory
import json


@csrf_exempt
def update_item(request, item_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)  # Parse the JSON body
            item_type = data.get("item_type").lower()

            # Update the item based on the type
            if item_type == "frame":
                item = Frame.objects.get(id=item_id)
            elif item_type == "lens":
                item = Lens.objects.get(id=item_id)
            elif item_type == "optical accessory":
                item = OpticalAccessory.objects.get(id=item_id)
            else:
                return JsonResponse({"error": "Invalid item type"}, status=400)

            # Update fields
            item.unit_price = data["unit_price"]
            item.stock_level = data["stock_level"]

            # Handle subtype/name separately
            if item_type == "frame":
                item.frame_type = data["item_subtype"]
            elif item_type == "lens":
                item.lens_type = data["item_subtype"]
            elif item_type == "optical accessory":
                item.name = data["item_subtype"]

            item.save()  # Save the updated item
            return JsonResponse({"message": "Item updated successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


# from django.http import JsonResponse
# from .models import Frame, Lens, OpticalAccessory

# def inventory_totals(request, item_type):
#     """
#     Calculate and return the total stock and total price for the given item type.
#     """
#     if item_type == "frames":
#         items = Frame.objects.all()
#     elif item_type == "lenses":
#         items = Lens.objects.all()
#     elif item_type == "accessories":
#         items = OpticalAccessory.objects.all()
#     else:
#         return JsonResponse({"error": "Invalid item type"}, status=400)

#     # Calculate total stock and price
#     total_stock = sum(item.stock_level for item in items)
#     total_price = sum(item.stock_level * item.unit_price for item in items)

#     return JsonResponse({
#         "total_stock": total_stock,
#         "total_price": float(total_price)
#     })



from django.http import JsonResponse
from django.db.models import Sum
from .models import Frame, Lens, OpticalAccessory

def inventory_totals(request, item_type):
    """
    Calculate and return the total stock and price for the given item type.
    Also return aggregated stock levels grouped by subtype.
    """
    if item_type == "frames":
        items = Frame.objects.values('frame_type').annotate(total_stock=Sum('stock_level'))
        stock_by_type = {item['frame_type']: item['total_stock'] for item in items}
    elif item_type == "lenses":
        items = Lens.objects.values('lens_type').annotate(total_stock=Sum('stock_level'))
        stock_by_type = {item['lens_type']: item['total_stock'] for item in items}
    elif item_type == "accessories":
        items = OpticalAccessory.objects.values('name').annotate(total_stock=Sum('stock_level'))
        stock_by_type = {item['name']: item['total_stock'] for item in items}
    else:
        return JsonResponse({"error": "Invalid item type"}, status=400)

    # Calculate total stock and price
    total_stock = sum(stock for stock in stock_by_type.values())
    total_price = sum(
        item['total_stock'] * Frame.objects.filter(frame_type=item['frame_type']).first().unit_price
        if item_type == "frames" else
        item['total_stock'] * Lens.objects.filter(lens_type=item['lens_type']).first().unit_price
        if item_type == "lenses" else
        item['total_stock'] * OpticalAccessory.objects.filter(name=item['name']).first().unit_price
        for item in items
    )

    return JsonResponse({
        "total_stock": total_stock,
        "total_price": float(total_price),
        "stock_by_type": stock_by_type
    })





# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.db.models import Sum
# from .models import Frame, Lens, OpticalAccessory
# import datetime

# @csrf_exempt
# def filter_monthly_data(request):
#     if request.method == 'GET':
#         item_type = request.GET.get('item_type')  # e.g., "Frame", "Lens", or "Optical Accessory"
#         month = int(request.GET.get('month'))  # e.g., 1 for January
#         year = int(request.GET.get('year'))  # e.g., 2024
#         sale_or_entry = request.GET.get('sale_or_entry')  # "Sales" or "Entries"

#         # Map item_type to the corresponding model
#         model_map = {
#             "Frame": Frame,
#             "Lens": Lens,
#             "Optical Accessory": OpticalAccessory,
#         }
#         model = model_map.get(item_type)

#         if not model:
#             return JsonResponse({'error': 'Invalid item type'}, status=400)

#         # Filter data by month and year
#         filtered_data = model.objects.filter(
#             date_added__year=year,
#             date_added__month=month
#         )

#         # Calculate total global amount
#         total_global_amount = filtered_data.aggregate(
#             total=Sum('unit_price')
#         )['total'] or 0.0
        
        

#         # Prepare data for the table
#         data = []
#         for item in filtered_data:
#             data.append({
#                 'month': item.date_added.strftime('%B'),
#                 'item': item.name if hasattr(item, 'name') else item.frame_type if hasattr(item, 'frame_type') else item.lens_type,
#                 'item_type': item.lens_type if hasattr(item, 'lens_type') else item.frame_type,
#                 'price': item.unit_price,
#                 'amount': item.stock_level,
#             })

#         return JsonResponse({
#             'data': data,
#             'total_global_amount': total_global_amount,
#         })
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.db.models import Sum, F
# from .models import Frame, Lens, OpticalAccessory

# @csrf_exempt
# def filter_monthly_data(request):
#     if request.method == 'GET':
#         item_type = request.GET.get('item_type')  # e.g., "Frame", "Lens", or "Optical Accessory"
#         month = int(request.GET.get('month'))  # e.g., 1 for January
#         year = int(request.GET.get('year'))  # e.g., 2024
#         sale_or_entry = request.GET.get('sale_or_entry')  # "Sales" or "Entries"

#         # Map item_type to the corresponding model
#         model_map = {
#             "Frame": Frame,
#             "Lens": Lens,
#             "Optical Accessory": OpticalAccessory,
#         }
#         model = model_map.get(item_type)

#         if not model:
#             return JsonResponse({'error': 'Invalid item type'}, status=400)

#         # Filter data by month and year
#         filtered_data = model.objects.filter(
#             date_added__year=year,
#             date_added__month=month
#         )

#         # Calculate the total global amount (unit_price * stock_level for all items)
#         total_global_amount = filtered_data.aggregate(
#             total=Sum(F('unit_price') * F('stock_level'))
#         )['total'] or 0.0

#         # Calculate totals for each item type
#         item_type_totals = filtered_data.values('frame_type' if item_type == "Frame" else 'lens_type').annotate(
#             total=Sum(F('unit_price') * F('stock_level'))
#         )

#         # Convert item_type_totals to a dictionary for easier access in the frontend
#         item_type_totals_dict = {item['frame_type'] if 'frame_type' in item else item['lens_type']: item['total']
#                                  for item in item_type_totals}

#         # Prepare data for the table
#         data = []
#         for item in filtered_data:
#             data.append({
#                 'month': item.date_added.strftime('%B'),
#                 'item': item.name if hasattr(item, 'name') else item.frame_type if hasattr(item, 'frame_type') else item.lens_type,
#                 'item_type': item.frame_type if hasattr(item, 'frame_type') else item.lens_type,
#                 'price': item.unit_price,
#                 'amount': item.stock_level,
#             })

#         return JsonResponse({
#             'data': data,
#             'total_global_amount': total_global_amount,
#             'item_type_totals': item_type_totals_dict,  # Include totals for each item type
#         })
#     return JsonResponse({'error': 'Invalid request method'}, status=405)



from django.db.models import Sum, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Frame, Lens, OpticalAccessory

from django.http import JsonResponse
from django.db.models import Sum, F
from .models import InventoryItem, SaleEntry

@csrf_exempt
def filter_monthly_data(request):
    """Filter data for monthly entries or sales."""
    if request.method == 'GET':
        item_type = request.GET.get('item_type')
        month = request.GET.get('month')
        year = request.GET.get('year')
        sale_or_entry = request.GET.get('sale_or_entry')

        if not all([item_type, month, year, sale_or_entry]):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        try:
            filters = {
                'date_added__year': year,
                'date_added__month': month,
                'category__name': item_type,
            }

            if sale_or_entry.lower() == 'entries':
                data = InventoryItem.objects.filter(**filters).values(
                    month=F('date_added__month'),
                    item=F('category__name'),
                    item_type=F('type__name'),
                    price=F('unit_price'),
                    amount=F('stock_level'),
                )
                total_amount = data.aggregate(total=Sum(F('unit_price') * F('stock_level')))['total'] or 0
            elif sale_or_entry.lower() == 'sales':
                data = SaleEntry.objects.filter(**filters).values(
                    month=F('date__month'),
                    item=F('item__category__name'),
                    item_type=F('item__type__name'),
                    price=F('price'),
                    amount=F('quantity'),
                )
                total_amount = data.aggregate(total=Sum(F('price') * F('quantity')))['total'] or 0
            else:
                return JsonResponse({'error': 'Invalid entry type.'}, status=400)

            return JsonResponse({
                'data': list(data),
                'total_global_amount': total_amount,
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



from django.http import JsonResponse
from django.db.models.functions import TruncYear
from django.db.models import Count
from .models import Frame, Lens, OpticalAccessory

def get_years(request):
    """Fetch distinct years from the inventory items."""
    try:
        # Get distinct years for each model
        frame_years = Frame.objects.annotate(year=TruncYear('date_added')).values_list('year', flat=True).distinct()
        lens_years = Lens.objects.annotate(year=TruncYear('date_added')).values_list('year', flat=True).distinct()
        accessory_years = OpticalAccessory.objects.annotate(year=TruncYear('date_added')).values_list('year', flat=True).distinct()

        # Combine and deduplicate years
        all_years = set(frame_years) | set(lens_years) | set(accessory_years)
        years_list = sorted(year.year for year in all_years)  # Sort years in ascending order

        return JsonResponse({"years": years_list}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import ItemCategory
import json

@csrf_exempt
def fetch_categories(request):
    """Fetch all categories."""
    if request.method == 'GET':
        categories = ItemCategory.objects.all().values('id', 'name')
        return JsonResponse(list(categories), safe=False)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def add_category(request):
    """Add a new category."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            category_name = data.get('name', '').strip()
            if not category_name:
                return JsonResponse({'success': False, 'message': 'Category name is required.'}, status=400)
            
            # Check for duplicates
            if ItemCategory.objects.filter(name__iexact=category_name).exists():
                return JsonResponse({'success': False, 'message': 'Category already exists.'}, status=400)
            
            # Create category
            category = ItemCategory.objects.create(name=category_name)
            return JsonResponse({'success': True, 'message': 'Category added successfully.', 'category': {'id': category.id, 'name': category.name}})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def delete_category(request, category_id):
    """Delete a category by ID."""
    if request.method == 'DELETE':
        category = get_object_or_404(ItemCategory, id=category_id)
        category.delete()
        return JsonResponse({'success': True, 'message': 'Category deleted successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def update_category(request, category_id):
    """Update an existing category."""
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            category_name = data.get('name', '').strip()
            if not category_name:
                return JsonResponse({'success': False, 'message': 'Category name is required.'}, status=400)
            
            # Check for duplicates (excluding the current category)
            if ItemCategory.objects.filter(name__iexact=category_name).exclude(id=category_id).exists():
                return JsonResponse({'success': False, 'message': 'Category already exists.'}, status=400)
            
            # Update category
            category = get_object_or_404(ItemCategory, id=category_id)
            category.name = category_name
            category.save()
            return JsonResponse({'success': True, 'message': 'Category updated successfully.', 'category': {'id': category.id, 'name': category.name}})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)



# item type section

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import ItemType, ItemCategory
import json

# @csrf_exempt
# def fetch_item_types(request):
#     """Fetch all item types, optionally filtered by category."""
#     if request.method == 'GET':
#         category_id = request.GET.get('category_id')

#         query = ItemType.objects.select_related('category').all()
#         if category_id:
#             query = query.filter(category_id=category_id)

#         item_types = query.values("id", "name", "category__name")
#         data = {
#             "item_types": list(item_types),  # Include category name
#         }
#         return JsonResponse(data)
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
@csrf_exempt
def fetch_item_types(request):
    """Fetch all item types, optionally filtered by category."""
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        type_name = request.GET.get('type_name')

        query = ItemType.objects.select_related('category').all()
        if category_id:
            query = query.filter(category_id=category_id)
        if type_name:
            query = query.filter(name=type_name)

        item_types = query.values("id", "name", "category_id", "category__name")
        data = {
            "item_types": list(item_types),
        }
        return JsonResponse(data)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

# @csrf_exempt
# def fetch_item_types(request):
#     """Fetch all item types, optionally filtered by category."""
#     if request.method == 'GET':
#         category_id = request.GET.get('category_id')

#         query = ItemType.objects.all()
#         if category_id:
#             query = query.filter(category_id=category_id)

#         item_types = query.values("id", "name", "category_id", "category__name")
#         data = {
#             "item_types": list(item_types),
#         }
#         return JsonResponse(data)
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


@csrf_exempt
def add_item_type(request):
    """Add a new item type."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            category_id = data.get('category_id')

            if not name or not category_id:
                return JsonResponse({'success': False, 'message': 'Name and category are required.'}, status=400)

            category = get_object_or_404(ItemCategory, id=category_id)
            item_type = ItemType.objects.create(name=name, category=category)
            return JsonResponse({'success': True, 'message': 'Item type added successfully.', 'item_type': {'id': item_type.id, 'name': item_type.name, 'category_id': category.id}})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


@csrf_exempt
def delete_item_type(request, item_type_id):
    """Delete an item type."""
    if request.method == 'DELETE':
        item_type = get_object_or_404(ItemType, id=item_type_id)
        item_type.delete()
        return JsonResponse({'success': True, 'message': 'Item type deleted successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


@csrf_exempt
def update_item_type(request, item_type_id):
    """Update an existing item type."""
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            category_id = data.get('category_id')

            if not name or not category_id:
                return JsonResponse({'success': False, 'message': 'Name and category are required.'}, status=400)

            category = get_object_or_404(ItemCategory, id=category_id)
            item_type = get_object_or_404(ItemType, id=item_type_id)
            item_type.name = name
            item_type.category = category
            item_type.save()

            return JsonResponse({'success': True, 'message': 'Item type updated successfully.', 'item_type': {'id': item_type.id, 'name': item_type.name, 'category_id': category.id}})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
  
    
    
#inventory system code
# import json
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .models import InventoryItem, ItemType

# def add_inventory_item(request):
#     """Add a new inventory item."""
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             item_type_id = data.get('item_type_id')
#             quantity = data.get('quantity')
#             price = data.get('price')

#             # Validation
#             if not item_type_id or not quantity or not price:
#                 return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)

#             item_type = get_object_or_404(ItemType, id=item_type_id)
#             inventory_item = InventoryItem.objects.create(
#                 type=item_type,
#                 category=item_type.category,  # Automatically associate the category
#                 unit_price=price,
#                 stock_level=quantity,
#             )
#             return JsonResponse({
#                 'success': True,
#                 'message': 'Inventory item added successfully.',
#                 'item': {
#                     'id': inventory_item.id,
#                     'category': {'id': inventory_item.category.id, 'name': inventory_item.category.name},
#                     'type': {'id': inventory_item.type.id, 'name': inventory_item.type.name} if inventory_item.type else None,
#                     'unit_price': str(inventory_item.unit_price),
#                     'stock_level': inventory_item.stock_level,
#                     'quantity_sold': inventory_item.quantity_sold,
#                     'date_added': inventory_item.date_added.strftime("%Y-%m-%d %H:%M:%S"),
#                 }
#             })
#         except json.JSONDecodeError:
#             return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
from django.http import JsonResponse
from .models import InventoryItem
from django.core.serializers import serialize

def fetch_inventory_items(request):
    """Fetch all inventory items."""
    if request.method == 'GET':
        items = InventoryItem.objects.select_related('category', 'type').all()
        data = [
            {
                "id": item.id,
                "category": item.category.name,
                "type": item.type.name if item.type else "Custom Item",
                "unit_price": str(item.unit_price),
                "stock_level": item.stock_level,
                "quantity_sold": item.quantity_sold,
                "total_value": str(item.total_value()),
                "date_added": item.date_added.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for item in items
        ]
        return JsonResponse(data, safe=False)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404


import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import ItemCategory, ItemType, InventoryItem

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ItemCategory, ItemType, InventoryItem
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from .models import ItemCategory, ItemType, InventoryItem

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import InventoryItem, ItemCategory, ItemType
import json

@csrf_exempt
def add_inventory_item(request):
    """API to add a new inventory item."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract and validate input data
            category_id = data.get('category_id')
            type_id = data.get('type_id')  # Optional
            unit_price = data.get('unit_price')
            stock_level = data.get('stock_level')

            if not category_id or not unit_price or not stock_level:
                return JsonResponse({'success': False, 'message': 'Missing required fields.'}, status=400)

            # Validate category
            category = get_object_or_404(ItemCategory, id=category_id)

            # Validate type (optional)
            item_type = None
            if type_id:
                item_type = get_object_or_404(ItemType, id=type_id)

            # Create inventory item
            inventory_item = InventoryItem.objects.create(
                category=category,
                type=item_type,
                unit_price=unit_price,
                stock_level=stock_level,
            )

            return JsonResponse({
                'success': True,
                'message': 'Inventory item added successfully.',
                'item': {
                    'id': inventory_item.id,
                    'type': item_type.name if item_type else 'Custom Item',
                    'unit_price': str(inventory_item.unit_price),
                    'stock_level': inventory_item.stock_level,
                    'date_added': inventory_item.date_added.strftime('%Y-%m-%d %H:%M:%S')
                }
            })

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

def fetch_item_types_inven(request):
    """Fetch all item types, optionally filtered by category."""
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        query = ItemType.objects.all()
        if category_id:
            query = query.filter(category_id=category_id)

        item_types = query.values("id", "name")
        return JsonResponse({"item_types": list(item_types)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import InventoryItem, ItemType, ItemCategory
import json
from django.utils.timezone import now

@csrf_exempt
@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            category_id = data.get('category')
            type_id = data.get('type')
            unit_price = data.get('unit_price')
            stock_level = data.get('stock_level')

            # Validate data
            if not all([category_id, unit_price, stock_level]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            category = ItemCategory.objects.get(id=category_id)
            item_type = ItemType.objects.get(id=type_id) if type_id else None

            item = InventoryItem.objects.create(
                category=category,
                type=item_type,
                unit_price=unit_price,
                stock_level=stock_level,
                date_added=now()
            )
            return JsonResponse({'message': 'Item added successfully', 'id': item.id}, status=201)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=405)




# def fetch_items(request):
#     items = InventoryItem.objects.all().values(
#         'id', 'type__name', 'stock_level', 'unit_price', 'date_added'
#     )
#     return JsonResponse(list(items), safe=False)
@csrf_exempt
def fetch_items(request):
    """Fetch inventory items, optionally filtered by category."""
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        query = InventoryItem.objects.select_related('type', 'category').all()

        if category_id:
            query = query.filter(category_id=category_id)

        items = query.values(
            'id', 'type__name', 'stock_level', 'unit_price', 'date_added'
        )
        return JsonResponse(list(items), safe=False)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



from django.http import JsonResponse
@csrf_exempt
def delete_item(request, item_id):
    """Delete an inventory item by ID."""
    if request.method == 'DELETE':
        try:
            item = InventoryItem.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully.'}, status=200)
        except InventoryItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)


@csrf_exempt
def update_item(request, item_id):
    """Update an inventory item by ID."""
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            category_id = data.get('category')
            type_id = data.get('type')
            unit_price = data.get('unit_price')
            stock_level = data.get('stock_level')

            if not all([category_id, unit_price, stock_level]):
                return JsonResponse({'error': 'Missing required fields.'}, status=400)

            item = InventoryItem.objects.get(id=item_id)
            item.category_id = category_id
            item.type_id = type_id
            item.unit_price = unit_price
            item.stock_level = stock_level
            item.save()

            return JsonResponse({'message': 'Item updated successfully.'}, status=200)
        except InventoryItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)








from django.http import JsonResponse
from .models import ItemType

def fetch_item_types_s(request):
    """Fetch item types based on category."""
    category_id = request.GET.get("category_id")
    if category_id:
        item_types = ItemType.objects.filter(category_id=category_id).values("id", "name")
    else:
        item_types = ItemType.objects.all().values("id", "name")

    return JsonResponse({"item_types": list(item_types)})


import logging
logger = logging.getLogger(__name__)
# @csrf_exempt
# def get_category_stock_summary(request):
#     """Fetch the stock totals for each item type in a given category."""
#     if request.method == 'GET':
#         category_id = request.GET.get('category_id')
#         logger.debug(f"Received request for category stock summary. Category ID: {category_id}")
#         if not category_id:
#             return JsonResponse({'error': 'Category ID is required.'}, status=400)

#         try:
#             items = InventoryItem.objects.filter(category_id=category_id).select_related('type')
#             stock_summary = {}

#             # Aggregate stock by type name
#             for item in items:
#                 type_name = item.type.name if item.type else 'Custom Item'
#                 stock_summary[type_name] = stock_summary.get(type_name, 0) + item.stock_level

#             return JsonResponse({'stock_summary': stock_summary}, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)


#######################################################################################################
# @csrf_exempt
# def get_category_stock_summary(request):
#     """Fetch the stock totals for each item type in a given category."""
#     if request.method == 'GET':
#         category_id = request.GET.get('category_id')
#         if not category_id:
#             return JsonResponse({'error': 'Category ID is required.'}, status=400)

#         try:
#             # Fetch inventory items for the selected category
#             items = InventoryItem.objects.filter(category_id=category_id).select_related('type')
#             stock_summary = {}

#             # Aggregate stock by item type
#             for item in items:
#                 type_name = item.type.name if item.type else 'Custom Item'
#                 stock_summary[type_name] = stock_summary.get(type_name, 0) + item.stock_level

#             return JsonResponse({'stock_summary': stock_summary}, status=200)
#         except Exception as e:
#             logger.exception("Error fetching category stock summary")
#             return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)
###########################################################################################################
from decimal import Decimal
from django.http import JsonResponse
from .models import InventoryItem
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_category_stock_summary(request):
    """Fetch the stock totals for each item type in a given category."""
    if request.method == 'GET':
        category_id = request.GET.get('category_id')  # Fetch category_id from request
        try:
            # Filter items by category if category_id is provided, else fetch all items
            items = InventoryItem.objects.filter(category_id=category_id) if category_id else InventoryItem.objects.all()

            stock_summary = {}
            total_stock = 0
            total_amount = Decimal('0.0')  # Initialize total_amount as a Decimal

            # Iterate over items to calculate total stock and amount
            for item in items:
                type_name = item.type.name if item.type else 'Custom Item'
                stock_summary[type_name] = stock_summary.get(type_name, 0) + item.stock_level
                total_stock += item.stock_level
                total_amount += item.unit_price * Decimal(item.stock_level)  # Use Decimal for consistent calculations

            return JsonResponse({
                'stock_summary': stock_summary,
                'total_stock': total_stock,
                'total_amount': float(total_amount),  # Convert Decimal to float for JSON serialization
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



# monthly sales and exits
from django.http import JsonResponse
from django.db.models import Sum, Q
from .models import SaleEntry, InventoryItem  # Import your models

from django.http import JsonResponse
from django.db.models import Sum, F, FloatField
from .models import InventoryItem, SaleEntry

def filter_report(request):
    """Filter report data based on selected filters."""
    # Get query parameters
    month = request.GET.get('month')  # e.g., "1" for January
    year = request.GET.get('year')    # e.g., "2025"
    category_id = request.GET.get('category_id')  # Category ID
    item_type_id = request.GET.get('item_type_id')  # Item Type ID
    report_type = request.GET.get('report_type')  # "sales" or "entries"

    try:
        # Validate inputs
        if not month or not year:
            return JsonResponse({'error': 'Month and year are required.'}, status=400)

        # Convert month and year to integers
        month = int(month)
        year = int(year)

        # Determine the base queryset
        if report_type == "sales":
            queryset = SaleEntry.objects.filter(date__month=month, date__year=year)
            queryset = queryset.select_related('item__type', 'item__category')  # Include related data
        elif report_type == "entries":
            queryset = InventoryItem.objects.filter(date_added__month=month, date_added__year=year)
        else:
            return JsonResponse({'error': 'Invalid report type.'}, status=400)

        # Apply category filter for `sales` or `entries`
        if category_id:
            if report_type == "sales":
                queryset = queryset.filter(item__category_id=int(category_id))
            elif report_type == "entries":
                queryset = queryset.filter(category_id=int(category_id))

        # Apply item type filter for `sales` or `entries`
        if item_type_id:
            if report_type == "sales":
                queryset = queryset.filter(item__type_id=int(item_type_id))
            elif report_type == "entries":
                queryset = queryset.filter(type_id=int(item_type_id))

        # Annotate and compute total_value
        if report_type == "sales":
            queryset = queryset.annotate(
                total_value=F('price') * F('quantity')  # Use `price` and `quantity` for `SaleEntry`
            )
        elif report_type == "entries":
            queryset = queryset.annotate(
                total_value=F('unit_price') * F('stock_level')  # Use `unit_price` and `stock_level` for `InventoryItem`
            )

        # Aggregate the total amount
        total_amount = queryset.aggregate(total=Sum('total_value', output_field=FloatField()))['total'] or 0.0

        # Format data for frontend
        report_data = []
        if report_type == "sales":
            report_data = list(queryset.values(
                'date',  # Use `date` for `SaleEntry`
                'item__type__name',
                'price',
                'quantity',
                'total_value'
            ))
        elif report_type == "entries":
            report_data = list(queryset.values(
                'date_added',  # Use `date_added` for `InventoryItem`
                'type__name',
                'unit_price',
                'stock_level',
                'total_value'
            ))

        return JsonResponse({
            'success': True,
            'data': report_data,
            'total_amount': total_amount
        }, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



from django.db.models import Sum, F, FloatField
from django.http import JsonResponse

from django.db.models import Sum, F, FloatField
from django.http import JsonResponse

def get_totals_by_type(request):
    """Fetch total amounts for all item types in a specific category."""
    category_id = request.GET.get('category_id')  # Get the category ID

    try:
        if not category_id:
            return JsonResponse({'error': 'Category ID is required.'}, status=400)

        # Filter InventoryItems by the selected category
        items = InventoryItem.objects.filter(category_id=category_id)

        # Group by item type and calculate total amount for each
        totals = (
            items
            .values("type__name")  # Group by item type name
            .annotate(
                total_amount=Sum(F("unit_price") * F("stock_level"), output_field=FloatField())
            )
        )

        # Format the response as a list of item types and their totals
        results = [{"type_name": item["type__name"], "total_amount": item["total_amount"]} for item in totals]

        return JsonResponse({
            "success": True,
            "totals": results,  # A list of all item types and their totals
        }, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




import csv
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum, F, FloatField
from .models import InventoryItem, SaleEntry
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# def export_report(request):
#     """Export the report as a CSV or PDF based on the request."""
#     # Get query parameters
#     month = request.GET.get('month')  # e.g., "1" for January
#     year = request.GET.get('year')    # e.g., "2025"
#     category_id = request.GET.get('category_id')  # Category ID
#     item_type_id = request.GET.get('item_type_id')  # Item Type ID
#     report_type = request.GET.get('report_type')  # "sales" or "entries"
#     file_format = request.GET.get('format', 'csv')  # "csv" or "pdf"

#     try:
#         # Validate inputs
#         if not month or not year:
#             return JsonResponse({'error': 'Month and year are required.'}, status=400)

#         # Convert month and year to integers
#         month = int(month)
#         year = int(year)

#         # Determine the base queryset
#         if report_type == "sales":
#             queryset = SaleEntry.objects.filter(date__month=month, date__year=year).select_related('item__type', 'item__category')
#         elif report_type == "entries":
#             queryset = InventoryItem.objects.filter(date_added__month=month, date_added__year=year)
#         else:
#             return JsonResponse({'error': 'Invalid report type.'}, status=400)

#         # Apply category filter
#         if category_id:
#             if report_type == "sales":
#                 queryset = queryset.filter(item__category_id=int(category_id))
#             elif report_type == "entries":
#                 queryset = queryset.filter(category_id=int(category_id))

#         # Apply item type filter
#         if item_type_id:
#             if report_type == "sales":
#                 queryset = queryset.filter(item__type_id=int(item_type_id))
#             elif report_type == "entries":
#                 queryset = queryset.filter(type_id=int(item_type_id))

#         # Annotate and compute total_value
#         if report_type == "sales":
#             queryset = queryset.annotate(total_value=F('price') * F('quantity'))
#         elif report_type == "entries":
#             queryset = queryset.annotate(total_value=F('unit_price') * F('stock_level'))

#         # Prepare data for export
#         if report_type == "sales":
#             data = queryset.values(
#                 'date', 'item__type__name', 'price', 'quantity', 'total_value'
#             )
#             headers = ['Date', 'Item Type', 'Price', 'Quantity', 'Total Value']
#         elif report_type == "entries":
#             data = queryset.values(
#                 'date_added', 'type__name', 'unit_price', 'stock_level', 'total_value'
#             )
#             topic = ['month', 'years', 'category_id', 'item_type_id', 'report_type']
#             headers = ['Date Added', 'Item Type', 'Unit Price', 'Stock Level', 'Total Value']

#         # Export as CSV
#         if file_format == 'csv':
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename="report.csv"'

#             writer = csv.writer(response)
#             # writer.writerow(topic)
#             writer.writerow(headers)
#             for row in data:
#                 writer.writerow(row.values())
#             return response

#         # Export as PDF
#         elif file_format == 'pdf':
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="report.pdf"'

#             pdf = canvas.Canvas(response, pagesize=letter)
#             pdf.setFont("Helvetica", 12)
#             pdf.drawString(100, 750, "Report")
#             y = 720
#             for header in headers:
#                 pdf.drawString(100, y, header)
#                 y -= 20
#             y -= 10
#             for row in data:
#                 pdf.drawString(100, y, ', '.join(str(value) for value in row.values()))
#                 y -= 20
#             pdf.save()
#             return response

#         else:
#             return JsonResponse({'error': 'Invalid format.'}, status=400)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# def export_report(request):
#     """Export the report as a CSV or PDF based on the request."""
#     import calendar
#     import csv
#     from datetime import datetime
#     from django.db.models import F
#     from django.http import HttpResponse
#     from reportlab.pdfgen import canvas
#     from reportlab.lib.pagesizes import letter

#     # Get query parameters
#     month = request.GET.get('month')  # e.g., "1" for January
#     year = request.GET.get('year')    # e.g., "2025"
#     category_id = request.GET.get('category_id')  # Category ID
#     item_type_id = request.GET.get('item_type_id')  # Item Type ID
#     report_type = request.GET.get('report_type')  # "sales" or "entries"
#     file_format = request.GET.get('format', 'csv')  # "csv" or "pdf"

#     try:
#         # Validate inputs
#         if not month or not year:
#             return JsonResponse({'error': 'Month and year are required.'}, status=400)

#         # Convert month and year to integers
#         month = int(month)
#         year = int(year)
#         month_name = calendar.month_name[month]

#         # Get the category and item type names
#         category_name = ItemCategory.objects.get(pk=category_id).name if category_id else "All Categories"
#         item_type_name = ItemType.objects.get(pk=item_type_id).name if item_type_id else "All Item Types"

#         # Determine the base queryset
#         if report_type == "sales":
#             queryset = SaleEntry.objects.filter(date__month=month, date__year=year).select_related('item__type', 'item__category')
#         elif report_type == "entries":
#             queryset = InventoryItem.objects.filter(date_added__month=month, date_added__year=year)
#         else:
#             return JsonResponse({'error': 'Invalid report type.'}, status=400)

#         # Apply category filter
#         if category_id:
#             if report_type == "sales":
#                 queryset = queryset.filter(item__category_id=int(category_id))
#             elif report_type == "entries":
#                 queryset = queryset.filter(category_id=int(category_id))

#         # Apply item type filter
#         if item_type_id:
#             if report_type == "sales":
#                 queryset = queryset.filter(item__type_id=int(item_type_id))
#             elif report_type == "entries":
#                 queryset = queryset.filter(type_id=int(item_type_id))

#         # Annotate and compute total_value
#         if report_type == "sales":
#             queryset = queryset.annotate(total_value=F('price') * F('quantity'))
#         elif report_type == "entries":
#             queryset = queryset.annotate(total_value=F('unit_price') * F('stock_level'))

#         # Prepare data for export
#         if report_type == "sales":
#             data = queryset.values(
#                 'item__type__name', 'price', 'quantity', 'total_value'
#             )
#             headers = ['Date', 'Item Type', 'Price', 'Quantity', 'Total Value']
#         elif report_type == "entries":
#             data = queryset.values(
#                 'type__name', 'unit_price', 'stock_level', 'total_value'
#             )
#             headers = ['Date', 'Item Type', 'Unit Price', 'Stock Level', 'Total Value']

#         # Add the formatted "Month Year" to the data
#         for row in data:
#             row['formatted_date'] = f"{month_name} {year}"

#         # Export as CSV
#         if file_format == 'csv':
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = f'attachment; filename="{report_type}_report_{month_name}_{year}.csv"'

#             writer = csv.writer(response)
#             # Write report details
#             writer.writerow(['Month', month_name])
#             writer.writerow(['Year', year])
#             writer.writerow(['Category', category_name])
#             writer.writerow(['Item Type', item_type_name])
#             writer.writerow(['Report Type', report_type.capitalize()])
#             writer.writerow([])  # Blank line
#             # Write headers
#             writer.writerow(headers)
#             # Write data rows
#             for row in data:
#                 writer.writerow([row['formatted_date']] + list(row.values()))
#             return response

#         # Export as PDF
#         elif file_format == 'pdf':
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = f'attachment; filename="{report_type}_report_{month_name}_{year}.pdf"'

#             pdf = canvas.Canvas(response, pagesize=letter)
#             pdf.setFont("Helvetica", 12)

#             # Add report details
#             pdf.drawString(100, 750, f"Month: {month_name}")
#             pdf.drawString(100, 735, f"Year: {year}")
#             pdf.drawString(100, 720, f"Category: {category_name}")
#             pdf.drawString(100, 705, f"Item Type: {item_type_name}")
#             pdf.drawString(100, 690, f"Report Type: {report_type.capitalize()}")
#             y = 670

#             # # Add headers
#             # pdf.setFont("Helvetica-Bold", 10)
#             # for header in headers:
#             #     pdf.drawString(100, y, header)
#             #     y -= 20

#             # # Add data rows with "Month Year" in the Date column
#             # pdf.setFont("Helvetica", 10)
#             # for row in data:
#             #     row_data = [row['formatted_date']] + list(row.values())
#             #     pdf.drawString(100, y, ', '.join(str(value) for value in row_data))
#             #     y -= 20


#             # Add headers (tabular format)
#             pdf.setFont("Helvetica-Bold", 10)
#             header_y = y  # Save the starting point for headers

#             # Dynamically calculate x positions based on the number of headers
#             num_headers = len(headers)
#             header_x_positions = [100 + (index * 100) for index in range(num_headers)]  # Adjust spacing as needed

#             # Draw headers
#             for index, header in enumerate(headers):
#                 pdf.drawString(header_x_positions[index], header_y, header)

#             # Draw separator line
#             pdf.line(90, header_y - 5, 90 + (num_headers * 100) - 10, header_y - 5)  # Draw line below headers

#             # Add data rows
#             pdf.setFont("Helvetica", 10)
#             data_y = header_y - 30  # Start adding data below headers with increased gap

#             # Set a larger gap for row spacing
#             row_height = 25  # Adjust this value to increase or decrease spacing

#             for row in data:
#                 if len(row) != num_headers:
#                     raise ValueError("Row length does not match header length!")  # Raise an error if lengths don't match
#                 for index, value in enumerate(row.values()):
#                     if isinstance(value, str) and value.startswith('202'):  # Check if the value looks like a date string
#                         try:
#                             # Parse the date string and format it
#                             parsed_date = datetime.fromisoformat(value.replace('+00:00', ''))  # Strip timezone
#                             formatted_date = parsed_date.strftime('%B %Y')  # Format as "Month Year"
#                             pdf.drawString(header_x_positions[index], data_y, formatted_date)
#                         except ValueError:
#                             pdf.drawString(header_x_positions[index], data_y, value)  # If parsing fails, print original value
#                     else:
#                         pdf.drawString(header_x_positions[index], data_y, str(value))
#                 data_y -= row_height  # Move down for the next row

#             pdf.save()
#             return response

#         else:
#             return JsonResponse({'error': 'Invalid format.'}, status=400)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

from django.http import JsonResponse, HttpResponse
from django.db.models import F
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import csv
import calendar
from datetime import datetime
from django.utils.dateformat import format as date_format
from reportlab.lib.colors import *


# def export_report(request):
#     """Export the report as a CSV or PDF based on the request."""
#     try:
#         # Get query parameters
#         month = request.GET.get('month')  # e.g., "1" for January
#         year = request.GET.get('year')    # e.g., "2025"
#         category_id = request.GET.get('category_id')  # Category ID
#         item_type_id = request.GET.get('item_type_id')  # Item Type ID
#         report_type = request.GET.get('report_type')  # "sales" or "entries"
#         file_format = request.GET.get('format', 'csv')  # "csv" or "pdf"

#         # Validate inputs
#         if not month or not year:
#             return JsonResponse({'error': 'Month and year are required.'}, status=400)
#         month = int(month)
#         year = int(year)
#         month_name = calendar.month_name[month]

#         # Fetch category and item type names
#         category_name = "All Categories"
#         if category_id:
#             category = ItemCategory.objects.filter(pk=category_id).values('name').first()
#             category_name = category['name'] if category else "Invalid Category"

#         item_type_name = "All Item Types"
#         if item_type_id:
#             item_type = ItemType.objects.filter(pk=item_type_id).values('name').first()
#             item_type_name = item_type['name'] if item_type else "Invalid Item Type"

#         # Determine the base queryset
#         if report_type == "sales":
#             queryset = SaleEntry.objects.filter(date__month=month, date__year=year).select_related('item__type', 'item__category')
#         elif report_type == "entries":
#             queryset = InventoryItem.objects.filter(date_added__month=month, date_added__year=year)
#         else:
#             return JsonResponse({'error': 'Invalid report type.'}, status=400)

#         # Apply category filter
#         if category_id:
#             if report_type == "sales":
#                 queryset = queryset.filter(item__category_id=int(category_id))
#             elif report_type == "entries":
#                 queryset = queryset.filter(category_id=int(category_id))

#         # Apply item type filter
#         if item_type_id:
#             if report_type == "sales":
#                 queryset = queryset.filter(item__type_id=int(item_type_id))
#             elif report_type == "entries":
#                 queryset = queryset.filter(type_id=int(item_type_id))

#         # Annotate and compute total_value
#         if report_type == "sales":
#             queryset = queryset.annotate(total_value=F('price') * F('quantity'))
#         elif report_type == "entries":
#             queryset = queryset.annotate(total_value=F('unit_price') * F('stock_level'))

#         # Prepare data for export
#         if report_type == "sales":
#             data = queryset.values(
#                 'item__type__name', 'item__category__name', 'quantity', 'price', 'total_value'
#             )
#             headers = ['Item Type', 'Category', 'Quantity', 'Price', 'Total Value']
#         elif report_type == "entries":
#             data = queryset.values(
#                 'type__name', 'category__name', 'stock_level', 'unit_price', 'total_value'
#             )
#             headers = ['Item Type', 'Category', 'Stock Level', 'Unit Price', 'Total Value']

#         # Export as CSV
#         if file_format == 'csv':
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = f'attachment; filename="{report_type}_report_{month_name}_{year}.csv"'

#             writer = csv.writer(response)
#             # Add metadata
#             writer.writerow(['Month', month_name])
#             writer.writerow(['Year', year])
#             writer.writerow(['Category', category_name])
#             writer.writerow(['Item Type', item_type_name])
#             writer.writerow(['Report Type', report_type.capitalize()])
#             writer.writerow([])  # Blank line for spacing
#             # Add headers
#             writer.writerow(headers)
#             # Add data rows
#             for row in data:
#                 writer.writerow(row.values())
#             return response

#         # Export as PDF
#         elif file_format == 'pdf':
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = f'attachment; filename="{report_type}_report_{month_name}_{year}.pdf"'

#             pdf = canvas.Canvas(response, pagesize=letter)
#             pdf.setFont("Helvetica", 12)

#             # Add metadata
#             pdf.drawString(100, 750, f"Month: {month_name}")
#             pdf.drawString(100, 735, f"Year: {year}")
#             pdf.drawString(100, 720, f"Category: {category_name}")
#             pdf.drawString(100, 705, f"Item Type: {item_type_name}")
            
#             pdf.drawString(100, 690, f"Report Type: {report_type.capitalize()}")

#             # pdf.setFillColor(blue)
#             # pdf.drawString(100, 700, "This is a blue text!")

#             # # Reset to default (black)
#             # pdf.setFillColor(black)
#             # pdf.drawString(100, 680, "This is black text.")

#             # header_y = 670  # Starting Y-coordinate for the headers
#             # header_height = 400  # Height of the background
#             # pdf.setFillColor(lightgrey)
#             # pdf.rect(90, header_y - header_height, len(headers) * 100, header_height, stroke=0, fill=1)

#             # Add headers
#             pdf.setFillColor(black) 
#             pdf.setFont("Helvetica-Bold", 10)
#             y = 670
#             for index, header in enumerate(headers):
#                 pdf.drawString(100 + (index * 100), y, header)
                
#             # pdf.setFillColor(black)  # Reset text color
#             # pdf.setFont("Helvetica-Bold", 10)
#             # y = 670
#             # for index, header in enumerate(headers):
#             #     pdf.drawString(100 + (index * 100), header_y - 15, header)

#             # Draw a line below the headers
            
#             line_start_x = 90
#             line_end_x = line_start_x + (len(headers) * 100) - 10
#             line_y = y - 5
#             pdf.line(line_start_x, line_y, line_end_x, line_y)

#             # Draw rows
#             pdf.setFont("Helvetica", 10)
#             y -= 20
#             for row in data:
#                 for index, value in enumerate(row.values()):
#                     pdf.drawString(100 + (index * 100), y, str(value))
#                 y -= 20
#                 if y < 50:  # Add new page if content exceeds current page height
#                     pdf.showPage()
#                     pdf.setFont("Helvetica", 10)
#                     y = 750

#             pdf.save()
#             return response

#         else:
#             return JsonResponse({'error': 'Invalid file format.'}, status=400)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

import os
import csv
import calendar
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, lightgrey, whitesmoke, HexColor
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors 
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from django.templatetags.static import static

def export_report(request):
    """Export the report as a CSV or PDF based on the request."""
    try:
        # Get query parameters
        month = request.GET.get('month')
        year = request.GET.get('year')
        category_id = request.GET.get('category_id')
        item_type_id = request.GET.get('item_type_id')
        report_type = request.GET.get('report_type')
        file_format = request.GET.get('format', 'csv')

        # Validate inputs
        if not month or not year:
            return JsonResponse({'error': 'Month and year are required.'}, status=400)

        month = int(month)
        year = int(year)
        month_name = calendar.month_name[month]

        # Fetch category and item type names
        category_name = "All Categories"
        if category_id:
            category = ItemCategory.objects.filter(pk=category_id).values('name').first()
            category_name = category['name'] if category else "Invalid Category"

        item_type_name = "All Item Types"
        if item_type_id:
            item_type = ItemType.objects.filter(pk=item_type_id).values('name').first()
            item_type_name = item_type['name'] if item_type else "Invalid Item Type"

        # Determine the base queryset
        if report_type == "sales":
            queryset = SaleEntry.objects.filter(date__month=month, date__year=year).select_related('item__type', 'item__category')
        elif report_type == "entries":
            queryset = InventoryItem.objects.filter(date_added__month=month, date_added__year=year)
        else:
            return JsonResponse({'error': 'Invalid report type.'}, status=400)

        # Apply category and item type filters
        if category_id:
            if report_type == "sales":
                queryset = queryset.filter(item__category_id=int(category_id))
            elif report_type == "entries":
                queryset = queryset.filter(category_id=int(category_id))

        if item_type_id:
            if report_type == "sales":
                queryset = queryset.filter(item__type_id=int(item_type_id))
            elif report_type == "entries":
                queryset = queryset.filter(type_id=int(item_type_id))

        # Annotate and compute total_value
        if report_type == "sales":
            queryset = queryset.annotate(total_value=F('price') * F('quantity'))
        elif report_type == "entries":
            queryset = queryset.annotate(total_value=F('unit_price') * F('stock_level'))

        # Prepare data for export
        if report_type == "sales":
            data = queryset.values(
                'item__type__name', 'item__category__name', 'quantity', 'price', 'total_value'
            )
            headers = ['Item Type', 'Category', 'Quantity', 'Price', 'Total Value']
        elif report_type == "entries":
            data = queryset.values(
                'type__name', 'category__name', 'stock_level', 'unit_price', 'total_value'
            )
            headers = ['Item Type', 'Category', 'Stock Level', 'Unit Price', 'Total Value']

        # Export as PDF
        if file_format == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{report_type}_report_{month_name}_{year}.pdf"'

            pdf = canvas.Canvas(response, pagesize=letter)
            page_width, page_height = letter
            
                # Set background color
            pdf.setFillColor(lightgrey)  # Set desired background color
            pdf.rect(0, 0, page_width, page_height, fill=1)

            # Add header
            pdf.setFont("Helvetica-Bold", 30)
            pdf.setFillColor(HexColor("#000000"))
            pdf.drawCentredString(page_width / 2, page_height - 50, "NGASSAM OPTIQUE")

            # Add subtitle
            pdf.setFont("Helvetica", 16)
            pdf.drawCentredString(page_width / 2, page_height - 80, "CABINET OPTIQUE")

            # Add description (properly formatted)
            description_lines = [
                "Vente de matériel Ophtalmique médical - Verre ophtalmique - Montures de marque",
                "N.I.U: P039116571318-RC/YAO/2023/A/351",
                "Situé derrière ADAMAQUA PALACE -",
                "Tél.: (237) 699 67 50 25 / 620 37 69 28 / 651 63 06 45",
                "",
                "",
                # "MONTHLY INVENTORY REPORT"
            ]
            pdf.setFont("Helvetica", 12)
            y = page_height - 110
            for line in description_lines:
                pdf.drawCentredString(page_width / 2, y, line)
                y -= 15
            
            pdf.setFont("Helvetica-Bold", 16)
            pdf.drawCentredString(page_width / 2, page_height - 190, "MONTHLY INVENTORY REPORT")

            # Add metadata
            pdf.setFont("Helvetica-Bold", 10)
            y -= 30
            metadata = [
                f"Month: {month_name}",
                f"Year: {year}",
                f"Category: {category_name}",
                f"Item Type: {item_type_name}",
                f"Report Type: {report_type.capitalize()}",
            ]
            for meta in metadata:
                pdf.drawString(50, y, meta)
                y -= 20



            # # Add table headers
            # pdf.setFont("Helvetica-Bold", 10)
            # pdf.setFillColor(lightgrey)
            # header_y = y - 20 
            # for index, header in enumerate(headers):
            #     pdf.drawString(60 + index * 100, y, header)


            # # Draw a horizontal line
            # pdf.setStrokeColor(black)
            # pdf.setLineWidth(1)
            # pdf.line(50, y, page_width - 50, y)
            # y -= 30
            
            # # Add table rows
            # pdf.setFont("Helvetica", 10)
            # pdf.setFillColor(black)
            # y -= 20
            # for row in data:
            #     for index, value in enumerate(row.values()):
            #         pdf.drawString(60 + index * 100, y, str(value))
            #     y -= 20
            #     if y < 50:  # Add new page if space runs out
            #         pdf.showPage()
            #         y = page_height - 50
            
            pdf.setFont("Helvetica-Bold", 10)
            pdf.setFillColor(black)
            header_y = y - 20  # Maintain the starting position for headers

            for index, header in enumerate(headers):
                pdf.drawString(60 + index * 100, header_y, header)

            # Draw separator line with spacing below headers
            top_of_line = header_y - 9  # Adjust spacing as needed
            bottom_of_line = top_of_line - 1  # Adjust line thickness as needed
            pdf.setStrokeColor(black)
            pdf.setLineWidth(1)
            pdf.line(50, top_of_line, page_width - 50, top_of_line)

            # Add table data with spacing
            y = bottom_of_line - 20  # Start table data below the line
            pdf.setFont("Helvetica", 10)
            pdf.setFillColor(black)

            for row in data:
                for index, value in enumerate(row.values()):
                    pdf.drawString(60 + index * 100, y, str(value))
                y -= 20  # Adjust spacing between rows as needed
                if y < 50:  # Add new page if space runs out
                    pdf.showPage()
                    y = page_height - 50
                    
            pdf.save()
            return response


        # Export as CSV
        elif file_format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{report_type}_report_{month_name}_{year}.csv"'
            writer = csv.writer(response)

            # Add metadata
            writer.writerow(['Month', month_name])
            writer.writerow(['Year', year])
            writer.writerow(['Category', category_name])
            writer.writerow(['Item Type', item_type_name])
            writer.writerow(['Report Type', report_type.capitalize()])
            writer.writerow([])  # Blank line
            writer.writerow(headers)
            for row in data:
                writer.writerow(row.values())
            return response

        else:
            return JsonResponse({'error': 'Invalid file format.'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# sales system.
from django.http import JsonResponse
from .models import ItemType, InventoryItem  # Import necessary models

# def get_unit_price(request):
#     """
#     Fetch the unit price for a selected item type within a category.
#     """
#     # Get query parameters
#     category_id = request.GET.get('category_id')  # Category ID
#     item_type_id = request.GET.get('item_type_id')  # Item Type ID

#     try:
#         # Validate inputs
#         if not category_id or not item_type_id:
#             return JsonResponse({'error': 'Category and item type are required.'}, status=400)

#         # Fetch the inventory item for the given category and item type
#         inventory_item = InventoryItem.objects.filter(
#             category_id=category_id,
#             type_id=item_type_id
#         ).first()

#         # Check if the item exists
#         if not inventory_item:
#             return JsonResponse({'error': 'Item not found in inventory or 0 stock level in inventory.'}, status=404)

#         # Return the unit price
#         return JsonResponse({'unit_price': float(inventory_item.unit_price)}, status=200)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

from django.http import JsonResponse
from .models import InventoryItem

def get_unit_price(request):
    """
    Fetch the unit price and total stock level for a selected item type within a category.
    """
    category_id = request.GET.get('category_id')  # Category ID
    item_type_id = request.GET.get('item_type_id')  # Item Type ID

    try:
        # Validate inputs
        if not category_id or not item_type_id:
            return JsonResponse({'error': 'Category and item type are required.'}, status=400)

        # Fetch all inventory items for this category and item type (to sum stock levels)
        inventory_items = InventoryItem.objects.filter(
            category_id=category_id,
            type_id=item_type_id
        )

        # Check if the item exists
        if not inventory_items.exists():
            return JsonResponse({'error': 'Item not found in inventory or stock level is 0.'}, status=404)

        # ✅ Calculate total stock from all inventory batches
        total_stock = sum(item.stock_level for item in inventory_items)

        # ✅ Get unit price from the first inventory batch (Assuming same price for all batches)
        unit_price = float(inventory_items.first().unit_price)

        # ✅ Debugging: Print API response to check correctness
        print(f"API Response: Unit Price={unit_price}, Stock Level={total_stock}")

        return JsonResponse({
            'unit_price': unit_price,
            'stock_level': total_stock  # ✅ Ensure stock level is included in the response
        }, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import InventoryItem

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import InventoryItem

@csrf_exempt
def update_item_price(request):
    """Update the unit price of an item type."""
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method."}, status=400)

    try:
        data = json.loads(request.body)
        item_type_id = data.get("item_type_id")
        new_price = data.get("new_price")

        if not item_type_id or not new_price:
            return JsonResponse({"error": "Missing item_type_id or new_price."}, status=400)

        # Update price in database
        inventory_item = InventoryItem.objects.filter(type_id=item_type_id).first()
        if not inventory_item:
            return JsonResponse({"error": "Item not found."}, status=404)

        inventory_item.unit_price = new_price
        inventory_item.save()

        return JsonResponse({"success": "Price updated successfully!"}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)




from django.http import JsonResponse
from .models import Patient

def fetch_patients(request):
    """Fetch all patient names and their details."""
    try:
        patients = Patient.objects.all().values('id', 'name', 'contact', 'email', 'address', 'profession', 'age', 'gender')
        return JsonResponse({'patients': list(patients)}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


from django.http import JsonResponse
from .models import Patient

def search_patient(request):
    """Search for patients by name."""
    query = request.GET.get("name", "").strip()

    if not query:
        return JsonResponse({"error": "No search query provided."}, status=400)

    patients = Patient.objects.filter(name__icontains=query).values("name", "contact", "email", "address", "age")

    return JsonResponse({"patients": list(patients)}, status=200)

from django.http import JsonResponse
from .models import InventoryItem

def check_low_stock(request):
    """Check if stock for a selected item type is low."""
    item_type_id = request.GET.get("item_type_id")

    if not item_type_id:
        return JsonResponse({"error": "Item type ID is required."}, status=400)

    inventory_item = InventoryItem.objects.filter(type_id=item_type_id).first()

    if not inventory_item:
        return JsonResponse({"error": "Item not found."}, status=404)

    return JsonResponse({
        "stock_level": inventory_item.stock_level,
        "is_low_stock": inventory_item.is_low_stock(),
        "low_stock_threshold": inventory_item.low_stock_threshold,
    })
###################################################
# # payement history
# from django.http import JsonResponse
# from .models import PaymentHistory

# def get_payment_history(request):
#     """Fetch and return all payment history records."""
#     try:
#         payments = PaymentHistory.objects.all().order_by("-payment_date").values(
#             "id", "patient__name", "total_amount", "total_vat", "total_balance", "payment_date"
#         )
#         return JsonResponse({"payments": list(payments)}, status=200)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


def fetch_payment_history(request):
    """Fetch payment history with optional filters (year, month, search)."""
    
    year = request.GET.get("year", None)
    month = request.GET.get("month", None)
    search_query = request.GET.get("search", "").strip()

    try:
        payments = PaymentHistory.objects.all()
        
        if year and year.isdigit():
            payments = payments.filter(payment_date__year=int(year))
        
        if month and month.isdigit() and int(month) > 0:
            payments = payments.filter(payment_date__month=int(month))

        if search_query:
            payments = payments.filter(
                Q(patient__name__icontains=search_query) | 
                Q(total_balance__icontains=search_query)
            )

        # ✅ Debugging: Print the number of records found
        print("Found Payment Records:", payments.count())

        payment_data = [
            {
                "id": payment.id,
                "date": payment.payment_date.strftime("%Y-%m-%d %H:%M"),
                "patient": payment.patient.name if payment.patient else "N/A",
                "amount": float(payment.total_amount),
                "total_vat": float(payment.total_vat),
                "total_balance": float(payment.total_balance),
                "method": "Cash" if payment.total_balance == float(payment.total_balance) else "Pending",
                "ref": f"PAY-{payment.id:06d}",
            }
            for payment in payments
        ]

        return JsonResponse({"payments": payment_data}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

####################################################################################### 
#refresh stock level
from django.http import JsonResponse
from .models import InventoryItem

def get_stock_level(request):
    """Fetch the current stock level of an item."""
    # category_id = request.GET.get('category_id')
    # item_type_id = request.GET.get('item_type_id')

    # try:
    #     if not category_id or not item_type_id:
    #         return JsonResponse({"error": "Missing category or item ID."}, status=400)

    #     inventory_item = InventoryItem.objects.filter(
    #         category_id=category_id,
    #         type_id=item_type_id
    #     ).first()

    #     if not inventory_item:
    #         return JsonResponse({"error": "Item not found in inventory."}, status=404)

    #     return JsonResponse({"stock_level": inventory_item.stock_level}, status=200)

    # except Exception as e:
    #     return JsonResponse({"error": str(e)}, status=500)

    """
    Fetch the total stock level for a selected item type within a category.
    """
    category_id = request.GET.get('category_id')  # Category ID
    item_type_id = request.GET.get('item_type_id')  # Item Type ID

    try:
        # Validate inputs
        if not category_id or not item_type_id:
            return JsonResponse({'error': 'Category and item type are required.'}, status=400)

        # Fetch all inventory items for this category and item type (to sum stock levels)
        inventory_items = InventoryItem.objects.filter(
            category_id=category_id,
            type_id=item_type_id
        )

        # Check if the item exists
        if not inventory_items.exists():
            return JsonResponse({'error': 'Item not found in inventory or stock level is 0.'}, status=404)

        # ✅ Calculate total stock from all inventory batches
        total_stock = sum(item.stock_level for item in inventory_items)

        # ✅ Get unit price from the first inventory batch (Assuming same price for all batches)
        unit_price = float(inventory_items.first().unit_price)

        # ✅ Debugging: Print API response to check correctness
        print(f"API Response: Unit Price={unit_price}, Stock Level={total_stock}")

        return JsonResponse({
            'unit_price': unit_price,
            'stock_level': total_stock  # ✅ Ensure stock level is included in the response
        }, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)    

#######################################################################################
#inventory_report
from django.http import JsonResponse
from .models import InventoryItem
from datetime import datetime, timedelta

def inventory_report(request):
    """Return inventory data based on filters."""
    category_id = request.GET.get("category_id")
    stock_filter = request.GET.get("stock")
    expiry_filter = request.GET.get("expiry")

    inventory = InventoryItem.objects.all()

    if category_id:
        inventory = inventory.filter(category_id=category_id)

    # ✅ Handle Stock Filtering
    if stock_filter == "Low Stock (<10)":
        inventory = inventory.filter(stock_level__lt=10)
    elif stock_filter == "Out of Stock (0)":
        inventory = inventory.filter(stock_level=0)

    # ✅ Handle Expiry Filtering Safely
    if hasattr(InventoryItem, "expiry_date"):
        from datetime import datetime, timedelta
        today = datetime.today().date()

        if expiry_filter == "Expired":
            inventory = inventory.filter(expiry_date__lt=today)
        elif expiry_filter == "Expiring Soon (<30 days)":
            inventory = inventory.filter(expiry_date__lte=today + timedelta(days=30))

        inventory_data = inventory.values(
            "type__name", "category__name", "stock_level", "unit_price", "expiry_date"
        )
    else:
        inventory_data = inventory.values("type__name", "category__name", "stock_level", "unit_price")

    return JsonResponse({"inventory": list(inventory_data)}, safe=False)


#######################################################################################
from django.http import JsonResponse
from django.db import transaction
from .models import SaleEntry, InventoryItem, Patient
import datetime

# @transaction.atomic
# def process_sale_transaction(request):
#     """Process and save a sale transaction."""
#     if request.method != "POST":
#         return JsonResponse({'error': 'Invalid request method'}, status=400)

#     try:
#         data = request.json()
#         patient_id = data.get("patient_id")
#         items = data.get("items")  # List of items sold
#         total_amount = data.get("total_amount")
#         total_vat = data.get("total_vat")
#         total_balance = data.get("total_balance")

#         if not items:
#             return JsonResponse({'error': 'No items in the transaction.'}, status=400)

#         # Validate patient
#         patient = None
#         if patient_id:
#             patient = Patient.objects.filter(id=patient_id).first()
#             if not patient:
#                 return JsonResponse({'error': 'Invalid patient ID.'}, status=400)

#         # Create SaleEntry records and update inventory
#         for item in items:
#             item_type_id = item["item_type_id"]
#             quantity_sold = item["quantity"]

#             inventory_item = InventoryItem.objects.filter(type_id=item_type_id).first()
#             if not inventory_item:
#                 return JsonResponse({'error': f'Item with ID {item_type_id} not found.'}, status=404)

#             if inventory_item.stock_level < quantity_sold:
#                 return JsonResponse({'error': f'Not enough stock for {inventory_item.type.name}.'}, status=400)

#             # Deduct stock level
#             inventory_item.stock_level -= quantity_sold
#             inventory_item.save()

#             # Create sale entry
#             SaleEntry.objects.create(
#                 item=inventory_item,
#                 quantity=quantity_sold,
#                 price=item["unit_price"],
#                 date=datetime.datetime.now()
#             )

#         return JsonResponse({'success': 'Transaction processed successfully'}, status=201)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt  # Disable CSRF for testing; remove in production!
# def process_sale_transaction(request):
#     """Process a sales transaction and update stock levels."""
#     if request.method != "POST":
#         return JsonResponse({"error": "Invalid request method."}, status=400)

#     try:
#         data = json.loads(request.body)  # Load JSON data
#         print("Received Data:", data)  # Debugging

#         if "items" not in data:
#             return JsonResponse({"error": "Missing items in request."}, status=400)

#         # Process each item (Dummy logic, replace with actual database updates)
#         for item in data["items"]:
#             item_type_id = item.get("item_type_id")
#             quantity = item.get("quantity")

#             if not item_type_id or not quantity:
#                 return JsonResponse({"error": "Invalid item data."}, status=400)

#             # Update stock level in Inventory (Example: Reduce stock)
#             from .models import InventoryItem
#             inventory_item = InventoryItem.objects.filter(type_id=item_type_id).first()
#             if inventory_item:
#                 inventory_item.stock_level -= quantity
#                 inventory_item.save()

#         return JsonResponse({"success": "Transaction processed successfully!"}, status=201)

#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON format."}, status=400)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SaleEntry, InventoryItem, Patient, PaymentHistory
from django.utils.timezone import now
from django.db import transaction

@csrf_exempt  # Disable CSRF for testing; remove in production!
def process_sale_transaction(request):
    """Process a sales transaction, save it in SaleEntry, and update stock (FIFO method)."""
    
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method."}, status=400)

    try:
        data = json.loads(request.body)  # Load JSON data

        if "items" not in data:
            return JsonResponse({"error": "Missing items in request."}, status=400)

        patient_id = data.get("patient_id")  # Optional patient ID
        total_amount = data.get("total_amount", 0)
        total_vat = data.get("total_vat", 0)
        total_balance = data.get("total_balance", 0)
        
                # ✅ Create a PaymentHistory record
        payment = PaymentHistory.objects.create(
            patient_id=patient_id,
            total_amount=total_amount,
            total_vat=total_vat,
            total_balance=total_balance
        )
        print("Saved PaymentHistory:", payment.id, payment.total_balance)  # ✅ Debugging


        with transaction.atomic():  # Ensure all updates are done together
            for item in data["items"]:
                item_type_id = item.get("item_type_id")
                quantity_sold = item.get("quantity")
                unit_price = item.get("unit_price")

                if not item_type_id or not quantity_sold:
                    return JsonResponse({"error": "Invalid item data."}, status=400)



                # **1️⃣ Deduct stock using FIFO (oldest first)**
                remaining_quantity = quantity_sold  # Track how much we need to deduct
                inventory_items = InventoryItem.objects.filter(type_id=item_type_id, stock_level__gt=0).order_by("date_added")

                for inventory_item in inventory_items:
                    if remaining_quantity <= 0:
                        break  # If fully deducted, exit loop

                    if inventory_item.stock_level >= remaining_quantity:
                        inventory_item.stock_level -= remaining_quantity
                        inventory_item.save()
                        remaining_quantity = 0  # All stock deducted
                    else:
                        remaining_quantity -= inventory_item.stock_level
                        inventory_item.stock_level = 0
                        inventory_item.save()

                if remaining_quantity > 0:
                    return JsonResponse({"error": "Not enough stock available."}, status=400)

                # **2️⃣ Record the sale in the SaleEntry table**
                SaleEntry.objects.create(
                    item_id=inventory_item.id,  # Associate with the correct inventory item
                    quantity=quantity_sold,
                    price=unit_price,
                    date=now(),
                )

        return JsonResponse({"success": "Transaction processed successfully!"}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)





from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from .models import SaleEntry, InventoryItem
from django.db import transaction
from django.core.exceptions import ValidationError
import json

@csrf_exempt
def create_sale_entry(request):
    """API endpoint to create a sale entry and deduct stock."""
    if request.method == "POST":
        try:
            # Parse request body
            data = json.loads(request.body)
            item_id = data.get('item_id')
            quantity = data.get('quantity')
            price = data.get('price')
            date = parse_datetime(data.get('date')) or timezone.now()

            if not all([item_id, quantity, price]):
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            with transaction.atomic():
                # Retrieve the inventory item
                inventory_item = InventoryItem.objects.select_for_update().get(id=item_id)

                # Check if there's enough stock
                if inventory_item.stock_level < quantity:
                    return JsonResponse({
                        'error': f"Insufficient stock for {inventory_item.type.name}. "
                                 f"Available: {inventory_item.stock_level}, Requested: {quantity}"
                    }, status=400)

                # Deduct stock
                inventory_item.stock_level -= quantity
                inventory_item.save()

                # Create SaleEntry
                SaleEntry.objects.create(
                    item=inventory_item,
                    quantity=quantity,
                    price=price,
                    date=date
                )

            return JsonResponse({'success': True, 'message': 'Sale entry created and stock updated.'}, status=201)

        except InventoryItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found.'}, status=404)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


#################################################################################### the payment and order system######################
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Order, Payment
from .serializers import OrderSerializer, PaymentSerializer

from services.order_service import OrderService
from services.payment_service import PaymentService
from services.status_service import OrderStatusService


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by("-created_at")
#     serializer_class = OrderSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Delegate creation to service layer
#         order = OrderService.create_order(
#             validated_data=serializer.validated_data,
#             user=request.user
#         )

#         output_serializer = self.get_serializer(order)
#         return Response(output_serializer.data, status=status.HTTP_201_CREATED)
#     def update(self, request, *args, **kwargs):
#         order = self.get_object()

#         serializer = self.get_serializer(order, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)

#         updated_order = OrderService.update_order(
#             order=order,
#             validated_data=serializer.validated_data
#         )

#         return Response(self.get_serializer(updated_order).data)
    
#     @action(detail=True, methods=["post"])
#     def change_status(self, request, pk=None):
#         order = self.get_object()
#         new_status = request.data.get("status")

#         try:
#             OrderStatusService.change_status(
#                 order=order,
#                 new_status=new_status,
#                 user=request.user
#             )
#         except ValueError as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({"message": "Status updated successfully"})

#     @action(detail=True, methods=["get"])
#     def summary(self, request, pk=None):
#         order = self.get_object()

#         summary_data = OrderService.get_order_summary(order)

#         return Response(summary_data)


#     @action(detail=True, methods=["post"])
#     def cancel(self, request, pk=None):
#         order = self.get_object()

#         try:
#             OrderStatusService.cancel_order(order, request.user)
#         except ValueError as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({"message": "Order cancelled successfully"})

# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all().order_by("-payment_date")
#     serializer_class = PaymentSerializer
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         try:
#             payment = PaymentService.add_payment(
#                 validated_data=serializer.validated_data,
#                 user=request.user
#             )
#         except ValueError as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(self.get_serializer(payment).data, status=status.HTTP_201_CREATED)

    
#     @action(detail=False, methods=["get"], url_path="by-order/(?P<order_id>[^/.]+)")
#     def get_by_order(self, request, order_id=None):
#         payments = Payment.objects.filter(order_id=order_id).order_by("-payment_date")
#         serializer = self.get_serializer(payments, many=True)

#         return Response(serializer.data)
"""
views_orders.py — Order, Payment, and Status views

This is a NEW file. Place it alongside your existing views.py.
Then import its functions into urls.py (shown in the corrected urls.py).

WHY A SEPARATE FILE?
─────────────────────
Your existing views.py is already 5500+ lines. Keeping all views in one file
makes it slow to navigate, harder to review, and risky to edit (one mistake
breaks everything). Splitting by domain (patients, orders, inventory…) is
the standard Django approach.

AUTHENTICATION
──────────────
Every view here uses @login_required. In your existing views.py many views
have no authentication guard — anyone who finds the URL can call them. Add
@login_required (or a token check if using DRF tokens) to every sensitive view.
"""

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from management.models import Order, Payment
from management.serializers import (
    OrderSerializer,
    OrderCreateSerializer,
    PaymentSerializer,
    PaymentCreateSerializer,
    OrderStatusHistorySerializer,
)
from services.order_service import OrderService
from services.payment_service import PaymentService
from services.status_service import OrderStatusService

# ─────────────────────────────────────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────────────────────────────────────

def _json_body(request):
    """Parse JSON body and return a dict, or {} on failure."""
    try:
        return json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return {}


# ─────────────────────────────────────────────────────────────────────────────
# Orders
# ─────────────────────────────────────────────────────────────────────────────

@csrf_exempt
@login_required
def order_list_create(request):
    """
    GET  /api/orders/         → list all orders (newest first)
    POST /api/orders/         → create a new order

    CONNECTION FLOW:
    Frontend → POST /api/orders/ → this view → OrderCreateSerializer.create()
    → OrderService.create_order() → Order + OrderItem rows saved → response
    """
    if request.method == "GET":
        orders = Order.objects.select_related(
            "patient", "prescription", "created_by", "assigned_to"
        ).prefetch_related("items", "payments").order_by("-created_at")

        # Optional status filter: GET /api/orders/?status=ready
        status_filter = request.GET.get("status")
        if status_filter:
            orders = orders.filter(status=status_filter)

        serializer = OrderSerializer(orders, many=True)
        return JsonResponse({"orders": serializer.data})

    if request.method == "POST":
        data = _json_body(request)

        # Inject the request into serializer context so create() can read request.user
        serializer = OrderCreateSerializer(
            data=data,
            context={"request": request}
        )

        if not serializer.is_valid():
            return JsonResponse({"errors": serializer.errors}, status=400)

        try:
            order = serializer.save()
            return JsonResponse(
                {"message": "Order created", "order": OrderSerializer(order).data},
                status=201
            )
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def order_detail(request, pk):
    """
    GET   /api/orders/<id>/    → retrieve a single order with items and payments
    PATCH /api/orders/<id>/    → update a draft order (items, discount, notes)

    CONNECTION FLOW (GET):
    Frontend → GET /api/orders/5/ → this view → OrderSerializer → JSON response

    CONNECTION FLOW (PATCH):
    Frontend → PATCH /api/orders/5/ → this view → OrderService.update_order()
    → recalculates totals → saves → response
    """
    order = get_object_or_404(
        Order.objects.prefetch_related("items", "payments", "status_history"),
        pk=pk
    )

    if request.method == "GET":
        serializer = OrderSerializer(order)
        return JsonResponse({"order": serializer.data})

    if request.method == "PATCH":
        data = _json_body(request)
        try:
            updated_order = OrderService.update_order(order, data)
            return JsonResponse(
                {"message": "Order updated", "order": OrderSerializer(updated_order).data}
            )
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def order_summary(request, pk):
    """
    GET /api/orders/<id>/summary/

    Returns the complete financial snapshot:
      total_amount, paid, balance, payment_status, order status.

    CONNECTION FLOW:
    Frontend needs to display "Patient owes X CFA"
    → GET /api/orders/5/summary/
    → OrderService.get_order_summary()
    → returns dict with all financial fields
    """
    order = get_object_or_404(Order, pk=pk)

    if request.method == "GET":
        summary = OrderService.get_order_summary(order)
        return JsonResponse({"summary": summary})

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def change_order_status(request, pk):
    """
    POST /api/orders/<id>/change-status/
    Body: { "status": "confirmed" }

    The service validates the transition against VALID_TRANSITIONS.
    Invalid transitions return a 400 with a descriptive error message.

    CONNECTION FLOW:
    Staff clicks "Mark as Ready" in the UI
    → POST /api/orders/5/change-status/ { "status": "ready" }
    → OrderStatusService.change_status()
    → validates draft→confirmed→in_progress→ready chain
    → writes OrderStatusHistory row
    → saves order
    → returns updated order
    """
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        data = _json_body(request)
        new_status = data.get("status")

        if not new_status:
            return JsonResponse({"error": "'status' field is required"}, status=400)

        try:
            updated_order = OrderStatusService.change_status(order, new_status, request.user)
            return JsonResponse({
                "message": f"Status changed to '{new_status}'",
                "order": OrderSerializer(updated_order).data,
                # Show user what they can do next
                "allowed_next": OrderStatusService.get_allowed_transitions(new_status),
            })
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def cancel_order(request, pk):
    """
    POST /api/orders/<id>/cancel/

    Dedicated cancellation endpoint — bypasses the normal transition chain
    but still enforces that completed/already-cancelled orders cannot be
    cancelled again.

    CONNECTION FLOW:
    Staff clicks "Cancel Order"
    → POST /api/orders/5/cancel/
    → OrderStatusService.cancel_order()
    → writes history row, sets status='cancelled'
    → response
    """
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        try:
            updated_order = OrderStatusService.cancel_order(order, request.user)
            return JsonResponse({
                "message": "Order cancelled",
                "order": OrderSerializer(updated_order).data,
            })
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def order_status_history(request, pk):
    """
    GET /api/orders/<id>/history/

    Returns the full audit log of who changed the status, when, and from/to what.
    Useful for a timeline view in the UI.
    """
    order = get_object_or_404(Order, pk=pk)

    if request.method == "GET":
        history = order.status_history.select_related("changed_by").order_by("changed_at")
        serializer = OrderStatusHistorySerializer(history, many=True)
        return JsonResponse({"history": serializer.data})

    return JsonResponse({"error": "Method not allowed"}, status=405)


# ─────────────────────────────────────────────────────────────────────────────
# Payments
# ─────────────────────────────────────────────────────────────────────────────

@csrf_exempt
@login_required
def add_payment(request):
    """
    POST /api/payments/
    Body: { "order": 5, "amount": 15000, "payment_method": "cash" }

    CONNECTION FLOW:
    Frontend → POST /api/payments/ → PaymentCreateSerializer validates shape
    → PaymentService.add_payment() validates business rules (no overpayment)
    → Payment row created → order.amount_paid and order.balance updated
    → response with the new Payment and updated order summary
    """
    if request.method == "POST":
        data = _json_body(request)

        serializer = PaymentCreateSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse({"errors": serializer.errors}, status=400)

        try:
            payment = PaymentService.add_payment(serializer.validated_data, request.user)
            return JsonResponse({
                "message": "Payment recorded",
                "payment": PaymentSerializer(payment).data,
                # Return updated summary so the frontend doesn't need a second request
                "order_summary": OrderService.get_order_summary(payment.order),
            }, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def payments_by_order(request, order_id):
    """
    GET /api/payments/by-order/<order_id>/

    Lists all payments (including refunds) for a specific order, ordered by date.

    CONNECTION FLOW:
    Frontend opens order detail page
    → GET /api/payments/by-order/5/
    → returns list of Payment rows
    → frontend renders payment history table
    """
    order = get_object_or_404(Order, pk=order_id)

    if request.method == "GET":
        payments = order.payments.order_by("payment_date")
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse({"payments": serializer.data})

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def refund_payment(request, order_id):
    """
    POST /api/payments/refund/<order_id>/
    Body: { "amount": 5000 }

    Records a negative payment (refund) and updates the order balance.
    Does NOT delete existing payment rows — preserves the full audit trail.
    """
    order = get_object_or_404(Order, pk=order_id)

    if request.method == "POST":
        data = _json_body(request)
        amount = data.get("amount")

        if not amount:
            return JsonResponse({"error": "'amount' is required"}, status=400)

        try:
            payment = PaymentService.refund_payment(order, amount, request.user)
            return JsonResponse({
                "message": "Refund recorded",
                "payment": PaymentSerializer(payment).data,
                "order_summary": OrderService.get_order_summary(order),
            }, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)





















































































# from django.db.models import F, Sum, FloatField
# from django.http import JsonResponse
# from .models import InventoryItem

# def filter_report(request):
#     """Filter report data based on selected filters."""
#     # Extract query parameters
#     month = request.GET.get('month')
#     year = request.GET.get('year')
#     category_id = request.GET.get('category_id')
#     item_type_id = request.GET.get('item_type_id')
#     report_type = request.GET.get('report_type')

#     try:
#         # Validate input
#         if not month or not year:
#             return JsonResponse({'error': 'Month and year are required.'}, status=400)

#         month = int(month)
#         year = int(year)

#         # Prepare query based on report type
#         queryset = InventoryItem.objects.filter(date_added__month=month, date_added__year=year)

#         if report_type == "sales":
#             queryset = queryset.filter(quantity_sold__gt=0)
#         elif report_type == "entries":
#             queryset = queryset.filter(quantity_sold=0)

#         # Apply category filter if provided
#         if category_id:
#             queryset = queryset.filter(category_id=category_id)

#         # Apply item type filter if provided
#         if item_type_id:
#             queryset = queryset.filter(type_id=item_type_id)

#         # Annotate total_value (unit_price * stock_level)
#         queryset = queryset.annotate(
#             total_value=F('unit_price') * F('stock_level'),
#         )

#         # Aggregate total amount
#         total_amount = queryset.aggregate(
#             total=Sum('total_value', output_field=FloatField())
#         )['total'] or 0.0

#         # Format response data
#         report_data = list(queryset.values(
#             'date_added', 'type__name', 'category__name',
#             'unit_price', 'stock_level', 'total_value',
#         ))

#         return JsonResponse({
#             'success': True,
#             'data': report_data,
#             'total_amount': total_amount,
#         }, status=200)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# @csrf_exempt
# def filter_report(request):
#     """Filter the report based on query parameters."""
#     if request.method == "GET":
#         month = request.GET.get("month")
#         year = request.GET.get("year")
#         category_id = request.GET.get("category_id")
#         item_type_id = request.GET.get("item_type_id")
#         sale_entry_type = request.GET.get("sale_entry_type")  # "sales" or "entries"

#         # Validate inputs
#         try:
#             month = int(month)
#             year = int(year)
#             if category_id:
#                 category_id = int(category_id)
#             if item_type_id:
#                 item_type_id = int(item_type_id)
#         except ValueError:
#             return JsonResponse({"error": "Invalid input fields"}, status=400)

#         # Query logic (pseudo-code, replace with actual queries)
#         report_data = []  # Fetch data based on filters
#         global_amount = 0.0  # Calculate the total amount

#         # Return the results
#         return JsonResponse({"report": report_data, "global_amount": global_amount}, status=200)

#     return JsonResponse({"error": "Invalid request method"}, status=405)

# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import InventoryItem, SaleEntry
# import csv
# from io import StringIO
# from datetime import datetime
# from django.db.models import F  # Import F for annotations
# from django.db.models import F
# from django.db.models.functions import ExtractYear, ExtractMonth
# import logging

# from django.db.models import F, Sum
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import logging

# logger = logging.getLogger(__name__)

# @csrf_exempt
# def fetch_report(request):
#     """Fetch report data for the selected filters."""
#     if request.method == 'GET':
#         year = request.GET.get('year')
#         month = request.GET.get('month')
#         category_id = request.GET.get('category_id')
#         entry_type = request.GET.get('entry_type')  # 'entry' or 'sale'

#         # Log received parameters
#         print(f"Filters: year={year}, month={month}, category_id={category_id}, entry_type={entry_type}")

#         if not all([year, month, category_id, entry_type]):
#             return JsonResponse({'error': 'All fields are required.'}, status=400)

#         try:
#             filters = {'category_id': category_id}

#             if entry_type == 'entry':
#                 filters['date_added__year'] = year
#                 filters['date_added__month'] = month
#                 data = InventoryItem.objects.filter(**filters).values(
#                     category=F('category__name'),
#                     type=F('type__name'),
#                     unit_price=F('unit_price'),
#                     stock_level=F('stock_level'),
#                 )
#             elif entry_type == 'sale':
#                 filters['date__year'] = year
#                 filters['date__month'] = month
#                 data = SaleEntry.objects.filter(**filters).values(
#                     category=F('item__category__name'),
#                     type=F('item__type__name'),
#                     quantity=F('quantity'),
#                     total_price=F('price'),
#                 )
#             else:
#                 return JsonResponse({'error': 'Invalid entry type.'}, status=400)

#             # Log the query result
#             print(f"Query Result: {data}")

#             if not data.exists():
#                 return JsonResponse({'error': 'No data found for the selected filters.'}, status=404)

#             return JsonResponse({'data': list(data)}, status=200)

#         except Exception as e:
#             print(f"Error: {e}")  # Log the error
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)



# @csrf_exempt
# def export_report(request):
#     """Export report data as CSV."""
#     if request.method == 'GET':
#         report_data = request.GET.get('data', '[]')  # Expect JSON data
#         filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = f'attachment; filename="{filename}"'

#         writer = csv.writer(response)
#         writer.writerow(['Date', 'Item Type', 'Category', 'Amount', 'Price'])
#         for row in report_data:
#             writer.writerow(row)

#         return response

#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# from django.db.models.functions import ExtractYear, ExtractMonth
# from django.http import JsonResponse

# @csrf_exempt
# def get_years_and_months(request):
#     """Fetch distinct years and months from SaleEntry."""
#     if request.method == 'GET':
#         try:
#             years = InventoryItem.objects.annotate(year=ExtractYear('date_added')).values_list('year', flat=True).distinct()
#             months = InventoryItem.objects.annotate(month=ExtractMonth('date_added')).values_list('month', flat=True).distinct()
#             return JsonResponse({
#                 'years': list(years),
#                 'months': list(months),
#             })
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)

# @csrf_exempt
# def get_sale_entry_types(request):
#     """Return available sale entry types."""
#     if request.method == 'GET':
#         try:
#             sale_entry_types = ['entry', 'sale']
#             return JsonResponse({'sale_entry_types': sale_entry_types})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)


# @csrf_exempt
# def filter_inventory_entries(request):
#     """Filter inventory entries by year and month."""
#     if request.method == 'GET':
#         year = request.GET.get('year')
#         month = request.GET.get('month')

#         try:
#             query = InventoryItem.objects.all()
#             if year:
#                 query = query.filter(date_added__year=year)
#             if month:
#                 query = query.filter(date_added__month=month)

#             entries = query.values(
#                 'id', 'category__name', 'type__name', 'unit_price', 'stock_level', 'date_added'
#             )
#             return JsonResponse({'entries': list(entries)}, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)


# @csrf_exempt
# def filter_sales_entries(request):
#     """Filter sales entries by year and month."""
#     if request.method == 'GET':
#         year = request.GET.get('year')
#         month = request.GET.get('month')

#         try:
#             query = SaleEntry.objects.all()
#             if year:
#                 query = query.filter(date__year=year)
#             if month:
#                 query = query.filter(date__month=month)

#             sales = query.values(
#                 'id', 'item__type__name', 'quantity', 'total_price', 'date'
#             )
#             return JsonResponse({'sales': list(sales)}, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)














# def update_inventory_item(request, item_id):
#     """Update an existing inventory item."""
#     if request.method == 'PUT':
#         try:
#             data = json.loads(request.body)
#             quantity = data.get('quantity')
#             price = data.get('price')

#             # Validation
#             if not quantity or not price:
#                 return JsonResponse({'success': False, 'message': 'Quantity and price are required.'}, status=400)

#             inventory_item = get_object_or_404(InventoryItem, id=item_id)
#             inventory_item.quantity = quantity
#             inventory_item.price = price
#             inventory_item.save()

#             return JsonResponse({'success': True, 'message': 'Inventory item updated successfully.'})
#         except json.JSONDecodeError:
#             return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


# def delete_inventory_item(request, item_id):
#     """Delete an inventory item."""
#     if request.method == 'DELETE':
#         inventory_item = get_object_or_404(InventoryItem, id=item_id)
#         inventory_item.delete()
#         return JsonResponse({'success': True, 'message': 'Inventory item deleted successfully.'})
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


# from django.http import JsonResponse
# from .models import InventoryItem
# from django.utils.timezone import now

# def fetch_inventory_items(request):
#     """Fetch all inventory items."""
#     if request.method == 'GET':
#         try:
#             inventory_items = InventoryItem.objects.select_related('category', 'type').all()
#             data = {
#                 "inventory_items": [
#                     {
#                         "id": item.id,
#                         "category": {"id": item.category.id, "name": item.category.name},
#                         "type": {"id": item.type.id, "name": item.type.name} if item.type else None,
#                         "unit_price": str(item.unit_price),
#                         "stock_level": item.stock_level,
#                         "quantity_sold": item.quantity_sold,
#                         "date_added": item.date_added.strftime("%Y-%m-%d %H:%M:%S"),
#                         "total_value": str(item.total_value()),  # Optional field for total value
#                     }
#                     for item in inventory_items
#                 ]
#             }
#             return JsonResponse(data)
#         except Exception as e:
#             return JsonResponse({'success': False, 'message': f'Internal Server Error: {e}'}, status=500)
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

# from django.http import JsonResponse
# from .models import ItemType

# def fetch_item_types_by_category(request, category_id):
#     """Fetch item types for a specific category."""
#     if request.method == 'GET':
#         item_types = ItemType.objects.filter(category_id=category_id).values("id", "name")
#         return JsonResponse(list(item_types), safe=False)
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Purchase
# from django.db.models import Sum


# @csrf_exempt
# def add_sale(request):
#     if request.method == "POST":
#         data = request.json()
#         try:
#             purchase = Purchase.objects.create(
#                 item_type=data.get("item_type"),
#                 item_subtype=data.get("item_subtype"),
#                 quantity=data.get("quantity"),
#                 unit_price=data.get("unit_price"),
#                 total_price=data.get("unit_price") * data.get("quantity"),
#                 patient_name=data.get("patient_name"),
#                 patient_contact=data.get("patient_contact"),
#             )
#             return JsonResponse({"success": True, "purchase_id": purchase.id})
#         except Exception as e:
#             return JsonResponse({"success": False, "error": str(e)})

#     return JsonResponse({"success": False, "error": "Invalid request method."})


# @csrf_exempt
# def filter_sales(request):
#     if request.method == "GET":
#         month = int(request.GET.get("month"))
#         year = int(request.GET.get("year"))
#         item_type = request.GET.get("item_type")

#         sales = Purchase.objects.filter(
#             date_sold__month=month,
#             date_sold__year=year,
#             item_type=item_type
#         )

#         total_sales = sales.aggregate(total=Sum("total_price"))["total"] or 0.0

#         data = [
#             {
#                 "item_type": sale.item_type,
#                 "item_subtype": sale.item_subtype,
#                 "quantity": sale.quantity,
#                 "total_price": sale.total_price,
#                 "date_sold": sale.date_sold.strftime("%Y-%m-%d"),
#             }
#             for sale in sales
#         ]

#         return JsonResponse({"data": data, "total_sales": total_sales})

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Sale, SoldItem, Frame, Lens, OpticalAccessory
# import json

# @csrf_exempt
# def fetch_patient_details(request):
#     if request.method == "GET":
#         patients = Patient.objects.all().values("id", "name", "email", "contact", "address", "age", "gender")
#         return JsonResponse({"patients": list(patients)}, status=200)
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# @csrf_exempt
# def fetch_item_price(request):
#     if request.method == "GET":
#         item_type = request.GET.get("item_type")
#         subtype = request.GET.get("subtype")
#         model_map = {
#             "Frame": Frame,
#             "Lens": Lens,
#             "Optical Accessory": OpticalAccessory,
#         }
#         model = model_map.get(item_type)
#         if not model:
#             return JsonResponse({"error": "Invalid item type"}, status=400)

#         if item_type == "Optical Accessory":
#             item = model.objects.filter(name=subtype).first()
#         else:
#             item = model.objects.filter(frame_type=subtype if item_type == "Frame" else "lens_type").first()
        
#         if not item:
#             return JsonResponse({"error": "Item not found"}, status=404)
        
#         return JsonResponse({"unit_price": item.unit_price}, status=200)
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# @csrf_exempt
# def submit_purchase(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             buyer_name = data.get("buyer_name")
#             buyer_email = data.get("buyer_email")
#             buyer_contact = data.get("buyer_contact")
#             buyer_address = data.get("buyer_address")
#             total_amount = data.get("total_amount")
#             vat_amount = data.get("vat_amount")
#             total_without_tax = data.get("total_without_tax")
#             change_to_give = data.get("change_to_give")
#             cart = data.get("cart")

#             # Create Sale
#             sale = Sale.objects.create(
#                 buyer_name=buyer_name,
#                 buyer_email=buyer_email,
#                 buyer_contact=buyer_contact,
#                 buyer_address=buyer_address,
#                 total_amount=total_amount,
#                 vat_amount=vat_amount,
#                 total_without_tax=total_without_tax,
#                 change_to_give=change_to_give,
#             )

#             # Create Sold Items
#             for item in cart:
#                 SoldItem.objects.create(
#                     sale=sale,
#                     item_type=item["item_type"],
#                     subtype=item.get("subtype"),
#                     unit_price=item["unit_price"],
#                     quantity=item["quantity"],
#                     total_price=item["total_price"],
#                     vat=item["vat"],
#                 )

#             return JsonResponse({"success": True, "sale_id": sale.id}, status=201)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)
# from django.http import JsonResponse

# def get_item_types(request, item_category):
#     """Fetch the item types for a given category."""
#     if item_category == "frames":
#         types = ["VIP", "VIP+", "VIP++", "CLASSIC"]
#     elif item_category == "lenses":
#         types = ["Simple Vision", "Progressive Stock", "Progressive Commande", "Bi-focaux"]
#     elif item_category == "accessories":
#         types = []  # No subtypes
#     else:
#         return JsonResponse({"error": "Invalid category"}, status=400)

#     return JsonResponse({"types": types})
# def get_unit_price(request, item_category):
#     """Fetch the unit price for a given item type."""
#     item_type = request.GET.get("type")
#     if item_category == "frames":
#         unit_price = Frame.objects.filter(frame_type=item_type).values_list("unit_price", flat=True).first()
#     elif item_category == "lenses":
#         unit_price = Lens.objects.filter(lens_type=item_type).values_list("unit_price", flat=True).first()
#     elif item_category == "accessories":
#         unit_price = OpticalAccessory.objects.filter(name=item_type).values_list("unit_price", flat=True).first()
#     else:
#         return JsonResponse({"error": "Invalid category"}, status=400)

#     if unit_price is None:
#         return JsonResponse({"error": "Item type not found"}, status=404)

#     return JsonResponse({"unit_price": unit_price})

# from django.http import JsonResponse

# def get_categories(request):
#     """Fetch item categories dynamically."""
#     categories = ["Frame", "Lens", "Optical Accessory"]
#     return JsonResponse({"categories": categories})
# from django.http import JsonResponse
# from .models import Frame, Lens, OpticalAccessory

# def get_unit_price(request, item_category):
#     """Fetch the unit price for a given item type."""
#     item_type = request.GET.get("type")
#     if item_category.lower() == "frames":
#         unit_price = Frame.objects.filter(frame_type=item_type).values_list("unit_price", flat=True).first()
#     elif item_category.lower() == "lenses":
#         unit_price = Lens.objects.filter(lens_type=item_type).values_list("unit_price", flat=True).first()
#     elif item_category.lower() == "accessories":
#         unit_price = OpticalAccessory.objects.filter(name=item_type).values_list("unit_price", flat=True).first()
#     else:
#         return JsonResponse({"error": "Invalid category"}, status=400)

#     if unit_price is None:
#         return JsonResponse({"error": "Item type not found"}, status=404)

#     return JsonResponse({"unit_price": unit_price})








from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Patient, Transaction, TransactionItem
from django.db.models import Sum, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Frame, Lens, OpticalAccessory, Patient, Transaction, TransactionItem
from django.db.models import F


# @csrf_exempt
# def get_patients(request):
#     """Fetch all patients."""
#     if request.method == 'GET':
#         patients = Patient.objects.all().values('id', 'name')
#         return JsonResponse({'patients': list(patients)}, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


                # @csrf_exempt
                # def get_patient_details(request, name):
                #     """Fetch patient details."""
                #     if request.method == 'GET':
                #         patient = get_object_or_404(Patient, name=name)
                #         return JsonResponse({
                #             'email': patient.email,
                #             'address': patient.address,
                #             'contact': patient.contact,
                #             'gender': patient.gender,
                #             'age': patient.age
                #         }, status=200)
                #     return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def get_item_price(request, item_type, subtype_or_name):
#     """Fetch the unit price of a specific item."""
#     if request.method == 'GET':
#         if item_type == "Frame":
#             item = get_object_or_404(Frame, frame_type=subtype_or_name)
#         elif item_type == "Lens":
#             item = get_object_or_404(Lens, lens_type=subtype_or_name)
#         elif item_type == "Optical Accessory":
#             item = get_object_or_404(OpticalAccessory, name=subtype_or_name)
#         else:
#             return JsonResponse({'error': 'Invalid item type'}, status=400)

#         return JsonResponse({'unit_price': float(item.unit_price)}, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def validate_transaction(request):
#     """Save a transaction."""
#     if request.method == 'POST':
#         data = request.json()
#         patient_name = data.get('patient')
#         items = data.get('items')
#         total_without_tax = data.get('total_without_tax')
#         total_vat = data.get('total_vat')
#         total_balance = data.get('total_balance')

#         # Find or create patient
#         patient = Patient.objects.filter(name=patient_name).first()

#         # Create transaction
#         transaction = Transaction.objects.create(
#             patient=patient,
#             total_without_tax=total_without_tax,
#             total_vat=total_vat,
#             total_balance=total_balance,
#         )

#         # Create transaction items
#         for item_data in items:
#             item_type = item_data['item_type']
#             quantity = item_data['quantity']
#             unit_price = item_data['unit_price']
#             total_price = item_data['total_price']

#             # Fetch item
#             if item_type == "Frame":
#                 item = get_object_or_404(Frame, frame_type=item_data['subtype'])
#             elif item_type == "Lens":
#                 item = get_object_or_404(Lens, lens_type=item_data['subtype'])
#             elif item_type == "Optical Accessory":
#                 item = get_object_or_404(OpticalAccessory, name=item_data['subtype'])

#             # Create transaction item
#             TransactionItem.objects.create(
#                 transaction=transaction,
#                 item_type=item_type,
#                 frame=item if item_type == "Frame" else None,
#                 lens=item if item_type == "Lens" else None,
#                 accessory=item if item_type == "Optical Accessory" else None,
#                 quantity=quantity,
#                 unit_price=unit_price,
#                 total_price=total_price,
#             )

#             # Update stock levels
#             item.stock_level = F('stock_level') - quantity
#             item.save()

#         return JsonResponse({'message': 'Transaction saved successfully!'}, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def get_item_types(request, item_type):
#     """Fetch item types based on the selected item (Frame, Lens, Optical Accessory)."""
#     if request.method == 'GET':
#         if item_type == "Frame":
#             types = Frame.objects.values_list('frame_type', flat=True).distinct()
#         elif item_type == "Lens":
#             types = Lens.objects.values_list('lens_type', flat=True).distinct()
#         elif item_type == "Optical Accessory":
#             types = OpticalAccessory.objects.values_list('name', flat=True).distinct()
#         else:
#             return JsonResponse({'error': 'Invalid item type'}, status=400)

#         return JsonResponse({'types': list(types)}, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# from django.db import transaction
# from django.http import JsonResponse
# from .models import Frame, Lens, OpticalAccessory, Purchase

# @csrf_exempt
# def validate_purchase(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)

#         patient_name = data.get('patient_name')
#         total_amount = data.get('total_amount')
#         vat_total = data.get('vat_total')
#         purchase_details = data.get('purchase_details', [])

#         if not patient_name or not purchase_details:
#             return JsonResponse({"error": "Invalid data provided."}, status=400)

#         try:
#             with transaction.atomic():
#                 # Save purchase record
#                 purchase = Purchase.objects.create(
#                     patient_name=patient_name,
#                     total_amount=total_amount,
#                     vat_total=vat_total,
#                 )

#                 # Save each purchase detail and update stock
#                 for detail in purchase_details:
#                     item_name = detail['item_name']
#                     item_type = detail['item_type']
#                     unit_price = detail['unit_price']
#                     quantity = detail['quantity']
#                     total = detail['total']

#                     # Identify item type and update stock
#                     if item_type in [choice[0] for choice in Frame.FRAME_TYPES]:
#                         frame = Frame.objects.get(frame_type=item_type)
#                         frame.stock_level -= quantity
#                         frame.quantity_sold += quantity
#                         frame.save()
#                     elif item_type in [choice[0] for choice in Lens.LENS_TYPES]:
#                         lens = Lens.objects.get(lens_type=item_type)
#                         lens.stock_level -= quantity
#                         lens.quantity_sold += quantity
#                         lens.save()
#                     else:  # Optical Accessory
#                         accessory = OpticalAccessory.objects.get(name=item_name)
#                         accessory.stock_level -= quantity
#                         accessory.quantity_sold += quantity
#                         accessory.save()

#                     # Save purchase detail
#                     purchase.details.create(
#                         item_name=item_name,
#                         item_type=item_type,
#                         unit_price=unit_price,
#                         quantity=quantity,
#                         total=total,
#                     )

#                 return JsonResponse({"message": "Purchase validated successfully!"}, status=200)

#         except Exception as e:
#             return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

#     return JsonResponse({"error": "Invalid request method."}, status=405)



from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Frame, Lens, OpticalAccessory, Purchase

from django.db import transaction
from django.http import JsonResponse
import json
from .models import Frame, Lens, OpticalAccessory, Purchase


# @csrf_exempt
# def validate_purchase(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             # Debugging: Print the received data
#             print("Data received from the frontend:", data)

#             patient_name = data.get('patient_name')
#             total_amount = data.get('total_amount')
#             vat_total = data.get('vat_total')
#             purchase_details = data.get('purchase_details', [])

#             if not patient_name or not purchase_details:
#                 return JsonResponse({"error": "Invalid data provided."}, status=400)

#             with transaction.atomic():
#                 # Save purchase record
#                 purchase = Purchase.objects.create(
#                     patient_name=patient_name,
#                     total_amount=total_amount,
#                     vat_total=vat_total,
#                 )

#                 # Save each purchase detail and update stock
#                 for detail in purchase_details:
#                     print("Processing purchase detail:", detail)  # Debugging
#                     item_name = detail['item_name']
#                     item_type = detail['item_type']
#                     unit_price = detail['unit_price']
#                     quantity = detail['quantity']
#                     total = detail['total']

#                     # Match by Frame, Lens, or Optical Accessory
#                     if item_type in [choice[0] for choice in Frame.FRAME_TYPES]:
#                         frame = Frame.objects.filter(frame_type__iexact=item_type).first()
#                         if not frame:
#                             raise ValueError(f"Frame with type '{item_type}' not found.")
#                         if frame.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Frame type '{item_type}'. Available: {frame.stock_level}, Requested: {quantity}")
#                         frame.stock_level -= quantity
#                         frame.quantity_sold += quantity
#                         frame.save()

#                     # elif item_type in [choice[0] for choice in Lens.LENS_TYPES]:
#                     #     lens = Lens.objects.filter(lens_type__iexact=item_type).first()
#                     #     if not lens:
#                     #         raise ValueError(f"Lens with type '{item_type}' not found.")
#                     #     if lens.stock_level < quantity:
#                     #         raise ValueError(f"Insufficient stock for Lens type '{item_type}'. Available: {lens.stock_level}, Requested: {quantity}")
#                     #     lens.stock_level -= quantity
#                     #     lens.quantity_sold += quantity
#                     #     lens.save()
#                     elif item_type in [choice[0] for choice in Lens.LENS_TYPES]:
#                         # Debugging: Log the item_type and available lens types
#                         print(f"Looking for lens type: {item_type}")
#                         available_lens_types = Lens.objects.values_list('lens_type', flat=True)
#                         print(f"Available lens types in the database: {list(available_lens_types)}")

#                         # Normalize item_type for comparison
#                         normalized_item_type = item_type.strip().lower()
#                         lens = Lens.objects.filter(lens_type__iexact=normalized_item_type).first()
#                         if not lens:
#                             raise ValueError(f"Lens with type '{item_type}' not found. Available types: {', '.join(available_lens_types)}")
#                         if lens.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Lens type '{item_type}'. Available: {lens.stock_level}, Requested: {quantity}")
#                         lens.stock_level -= quantity
#                         lens.quantity_sold += quantity
#                         lens.save()
#                     elif OpticalAccessory.objects.filter(name__iexact=item_type).exists():
#                         accessory = OpticalAccessory.objects.filter(name__iexact=item_type).first()
#                         if not accessory:
#                             raise ValueError(f"Optical Accessory '{item_type}' not found.")
#                         if accessory.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Optical Accessory '{item_type}'. Available: {accessory.stock_level}, Requested: {quantity}")
#                         accessory.stock_level -= quantity
#                         accessory.quantity_sold += quantity
#                         accessory.save()

#                     else:
#                         raise ValueError(f"Item not found: {item_name} ({item_type})")

#                     # Save purchase detail
#                     purchase.details.create(
#                         item_name=item_name,
#                         item_type=item_type,
#                         unit_price=unit_price,
#                         quantity=quantity,
#                         total=total,
#                     )

#                 return JsonResponse({"message": "Purchase validated successfully!"}, status=200)

#         except ValueError as ve:
#             print("ValueError:", ve)  # Debugging
#             return JsonResponse({"error": str(ve)}, status=400)
#         except Exception as e:
#             print("Exception occurred:", e)  # Debugging
#             return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

#     return JsonResponse({"error": "Invalid request method."}, status=405)


# @csrf_exempt
# def validate_purchase(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             # Debugging: Print the received data
#             print("Data received from the frontend:", data)

#             patient_name = data.get('patient_name')
#             total_amount = data.get('total_amount')
#             vat_total = data.get('vat_total')
#             purchase_details = data.get('purchase_details', [])

#             if not patient_name or not purchase_details:
#                 return JsonResponse({"error": "Invalid data provided."}, status=400)

#             with transaction.atomic():
#                 # Save purchase record
#                 purchase = Purchase.objects.create(
#                     patient_name=patient_name,
#                     total_amount=total_amount,
#                     vat_total=vat_total,
#                 )

#                 # Save each purchase detail and update stock
#                 for detail in purchase_details:
#                     print("Processing purchase detail:", detail)  # Debugging
#                     item_name = detail['item_name']
#                     item_type = detail['item_type']
#                     unit_price = detail['unit_price']
#                     quantity = detail['quantity']
#                     total = detail['total']

#                     # Extract item type for Frame and Lens
#                     if "Frame" in item_type:
#                         item_type = item_type.replace("Frame (", "").replace(")", "").strip()
#                         frame = Frame.objects.filter(frame_type__iexact=item_type).first()
#                         if not frame:
#                             raise ValueError(f"Frame with type '{item_type}' not found.")
#                         if frame.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Frame type '{item_type}'. Available: {frame.stock_level}, Requested: {quantity}")
#                         frame.stock_level -= quantity
#                         frame.quantity_sold += quantity
#                         frame.save()

#                     elif "Lens" in item_type:
#                         item_type = item_type.replace("Lens (", "").replace(")", "").strip()
#                         lens = Lens.objects.filter(lens_type__iexact=item_type).first()
#                         if not lens:
#                             raise ValueError(f"Lens with type '{item_type}' not found.")
#                         if lens.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Lens type '{item_type}'. Available: {lens.stock_level}, Requested: {quantity}")
#                         lens.stock_level -= quantity
#                         lens.quantity_sold += quantity
#                         lens.save()

#                     elif "Accessory" in item_type:
#                         accessory_name = item_name.replace("Accessory (", "").replace(")", "").strip()
#                         accessory = OpticalAccessory.objects.filter(name__iexact=accessory_name).first()
#                         if not accessory:
#                             raise ValueError(f"Optical Accessory '{accessory_name}' not found.")
#                         if accessory.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Optical Accessory '{accessory_name}'. Available: {accessory.stock_level}, Requested: {quantity}")
#                         accessory.stock_level -= quantity
#                         accessory.quantity_sold += quantity
#                         accessory.save()

#                     else:
#                         raise ValueError(f"Item not found: {item_name} ({item_type})")

#                     # Save purchase detail
#                     purchase.details.create(
#                         item_name=item_name,
#                         item_type=item_type,
#                         unit_price=unit_price,
#                         quantity=quantity,
#                         total=total,
#                     )

#                 return JsonResponse({"message": "Purchase validated successfully!"}, status=200)

#         except ValueError as ve:
#             print("ValueError:", ve)  # Debugging
#             return JsonResponse({"error": str(ve)}, status=400)
#         except Exception as e:
#             print("Exception occurred:", e)  # Debugging
#             return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

#     return JsonResponse({"error": "Invalid request method."}, status=405)




from django.http import JsonResponse
from .models import Patient

def list_patients(request):
    if request.method == 'GET':
        patients = list(Patient.objects.values('id', 'name', 'email', 'contact', 'gender', 'age'))
        return JsonResponse({"patients": patients}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)


from django.http import JsonResponse
from .models import Patient

def patient_details(request, patient_id):
    """Fetch and return details of a specific patient."""
    try:
        patient = Patient.objects.get(id=patient_id)
        return JsonResponse({
            "id": patient.id,
            "name": patient.name,
            "email": patient.email,
            "contact": patient.contact,
            "address": patient.address,
            "gender": patient.gender,
            "age": patient.age,
        })
    except Patient.DoesNotExist:
        return JsonResponse({"error": "Patient not found."}, status=404)


























































# from django.db.models import Sum
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Frame, Lens, OpticalAccessory

# @csrf_exempt
# def filter_monthly_data(request):
#     if request.method == 'GET':
#         item_type = request.GET.get('item_type')  # e.g., "Frame", "Lens", or "Optical Accessory"
#         month = int(request.GET.get('month'))  # e.g., 1 for January
#         year = int(request.GET.get('year'))  # e.g., 2024
#         sale_or_entry = request.GET.get('sale_or_entry')  # "Sales" or "Entries"

#         # Map item_type to the corresponding model
#         model_map = {
#             "Frame": Frame,
#             "Lens": Lens,
#             "Optical Accessory": OpticalAccessory,
#         }
#         model = model_map.get(item_type)

#         if not model:
#             return JsonResponse({'error': 'Invalid item type'}, status=400)

#         # Filter data by month and year
#         filtered_data = model.objects.filter(
#             date_added__year=year,
#             date_added__month=month
#         )

#         # For Optical Accessory, we don't have subtypes
#         if item_type == "Optical Accessory":
#             # Sum total for all optical accessories
#             total_global_amount = filtered_data.aggregate(
#                 total=Sum('unit_price') * Sum('stock_level')
                
#             )['total'] or 0.0

#             # Prepare data for the table
#             data = [
#                 {
#                     'month': item.date_added.strftime('%B'),
#                     'item': item.name,
#                     'item_type': "N/A",  # No subtype for optical accessories
#                     'price': item.unit_price,
#                     'amount': item.stock_level,
#                 }
#                 for item in filtered_data
#             ]

#             return JsonResponse({
#                 'data': data,
#                 'total_global_amount': total_global_amount,
#                 'item_type_totals': {},  # No subtypes, so we return an empty dict
#             })

#         # For Frame and Lens, handle subtypes as usual
#         total_global_amount = filtered_data.aggregate(
#             total=Sum('unit_price') * Sum('stock_level')
#         )['total'] or 0.0

#         # Group by subtype
#         item_type_totals = filtered_data.values('frame_type' if item_type == "Frame" else 'lens_type').annotate(
#             total=Sum('unit_price') * Sum('stock_level')
#         )

#         # Prepare data for the table
#         data = [
#             {
#                 'month': item.date_added.strftime('%B'),
#                 'item': item.frame_type if item_type == "Frame" else item.lens_type,
#                 'item_type': item.frame_type if item_type == "Frame" else item.lens_type,
#                 'price': item.unit_price,
#                 'amount': item.stock_level,
#             }
#             for item in filtered_data
#         ]

#         return JsonResponse({
#             'data': data,
#             'total_global_amount': total_global_amount,
#             'item_type_totals': {entry['frame_type' if item_type == "Frame" else 'lens_type']: entry['total'] for entry in item_type_totals},
#         })

#     return JsonResponse({'error': 'Invalid request method'}, status=405)




# from django.http import JsonResponse
# from django.db.models import Sum, F, TruncMonth
# from .models import Frame, Lens, OpticalAccessory

# def monthly_summary(request):
#     frames = (
#         Frame.objects.annotate(month=TruncMonth('date_added'))
#         .values('month', 'frame_type')
#         .annotate(
#             total_quantity=Sum('stock_level'),
#             total_price=Sum(F('stock_level') * F('unit_price'))
#         )
#         .order_by('month')
#     )

#     lenses = (
#         Lens.objects.annotate(month=TruncMonth('date_added'))
#         .values('month', 'lens_type')
#         .annotate(
#             total_quantity=Sum('stock_level'),
#             total_price=Sum(F('stock_level') * F('unit_price'))
#         )
#         .order_by('month')
#     )

#     accessories = (
#         OpticalAccessory.objects.annotate(month=TruncMonth('date_added'))
#         .values('month', 'name')
#         .annotate(
#             total_quantity=Sum('stock_level'),
#             total_price=Sum(F('stock_level') * F('unit_price'))
#         )
#         .order_by('month')
#     )

#     return JsonResponse({
#         "frames": list(frames),
#         "lenses": list(lenses),
#         "accessories": list(accessories),
#     })
# from django.db.models import Sum, F
# from django.db.models.functions import ExtractMonth, ExtractYear
# from django.http import JsonResponse
# from .models import Frame, Lens, OpticalAccessory

# def monthly_summary(request):
#     frames = (
#         Frame.objects.annotate(
#             month=ExtractMonth('date_added'),
#             year=ExtractYear('date_added')
#         )
#         .values('year', 'month', 'frame_type')
#         .annotate(
#             total_quantity=Sum('stock_level'),
#             total_price=Sum(F('stock_level') * F('unit_price'))
#         )
#         .order_by('year', 'month')
#     )

#     # Debugging: Print the data
#     print("Frames:", list(frames))

#     lenses = (
#         Lens.objects.annotate(
#             month=ExtractMonth('date_added'),
#             year=ExtractYear('date_added')
#         )
#         .values('year', 'month', 'lens_type')
#         .annotate(
#             total_quantity=Sum('stock_level'),
#             total_price=Sum(F('stock_level') * F('unit_price'))
#         )
#         .order_by('year', 'month')
#     )

#     print("Lenses:", list(lenses))

#     accessories = (
#         OpticalAccessory.objects.annotate(
#             month=ExtractMonth('date_added'),
#             year=ExtractYear('date_added')
#         )
#         .values('year', 'month', 'name')
#         .annotate(
#             total_quantity=Sum('stock_level'),
#             total_price=Sum(F('stock_level') * F('unit_price'))
#         )
#         .order_by('year', 'month')
#     )

#     print("Accessories:", list(accessories))

#     return JsonResponse({
#         "frames": list(frames),
#         "lenses": list(lenses),
#         "accessories": list(accessories),
#     })


# from django.http import JsonResponse
# from django.db.models import Sum, F
# from django.db.models.functions import ExtractMonth, ExtractYear
# from .models import Frame, Lens, OpticalAccessory

# def get_monthly_entries_sales(request):
#     """
#     View to retrieve monthly sales or entries data for a given month, year, item, and item type.
#     """
#     # Retrieve parameters from the request
#     month = request.GET.get('month')  # Expected as a numeric value (1-12)
#     year = request.GET.get('year')  # Expected as a numeric value (e.g., 2024)
#     item_type = request.GET.get('item')  # Frame, Lens, or Optical Accessory
#     item_subtype = request.GET.get('item_type')  # VIP, Simple Vision, etc.
#     sale_or_entry = request.GET.get('sale_or_entry')  # Sale or Entry

#     if not all([month, year, item_type]):
#         return JsonResponse({'error': 'Month, year, and item type are required parameters.'}, status=400)

#     try:
#         # Map the item type to the corresponding model
#         model_map = {
#             'Frame': Frame,
#             'Lens': Lens,
#             'Optical Accessory': OpticalAccessory
#         }

#         model = model_map.get(item_type)
#         if not model:
#             return JsonResponse({'error': 'Invalid item type.'}, status=400)

#         # Filter and annotate based on sale or entry
#         filter_kwargs = {
#             'date_added__month': month,
#             'date_added__year': year,
#         }

#         if item_subtype:
#             if item_type == 'Frame':
#                 filter_kwargs['frame_type'] = item_subtype
#             elif item_type == 'Lens':
#                 filter_kwargs['lens_type'] = item_subtype
#             elif item_type == 'Optical Accessory':
#                 filter_kwargs['name'] = item_subtype

#         # Query the database
#         if sale_or_entry == 'Entry':
#             queryset = model.objects.filter(**filter_kwargs).annotate(
#                 total_quantity=Sum('stock_level'),
#                 total_amount=Sum(F('stock_level') * F('unit_price'))
#             )
#         elif sale_or_entry == 'Sale':
#             queryset = model.objects.filter(**filter_kwargs).annotate(
#                 total_quantity=Sum('quantity_sold'),
#                 total_amount=Sum(F('quantity_sold') * F('unit_price'))
#             )
#         else:
#             return JsonResponse({'error': 'Invalid sale or entry value. Choose "Sale" or "Entry".'}, status=400)

#         # Convert the data to a list of dictionaries
#         data = list(queryset.values('id', 'date_added', 'unit_price', 'total_quantity', 'total_amount'))

#         # Calculate global amount
#         global_amount = sum(item['total_amount'] for item in data if item['total_amount'])

#         return JsonResponse({
#             'data': data,
#             'global_amount': global_amount,
#         })

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)








# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.dateparse import parse_datetime
# from .models import Frame, Lens, OpticalAccessory
# import json

# # Helper function to parse and validate request data
# def parse_request_data(request):
#     try:
#         data = json.loads(request.body)
#         return data
#     except json.JSONDecodeError:
#         return None


# @csrf_exempt
# def add_frame(request):
#     if request.method == "POST":
#         data = parse_request_data(request)
#         if not data:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)

#         try:
#             frame = Frame.objects.create(
#                 frame_type=data["type"],
#                 unit_price=data["unit_price"],
#                 stock_level=data["stock_level"],
#                 date_added=parse_datetime(data.get("date_added", None)) or None,
#             )
#             return JsonResponse({"message": "Frame added successfully!", "id": frame.id})
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"error": "Invalid request method"}, status=405)


# @csrf_exempt
# def add_lens(request):
#     if request.method == "POST":
#         data = parse_request_data(request)
#         if not data:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)

#         try:
#             lens = Lens.objects.create(
#                 lens_type=data["type"],
#                 unit_price=data["unit_price"],
#                 stock_level=data["stock_level"],
#                 date_added=parse_datetime(data.get("date_added", None)) or None,
#             )
#             return JsonResponse({"message": "Lens added successfully!", "id": lens.id})
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"error": "Invalid request method"}, status=405)


# @csrf_exempt
# def add_accessory(request):
#     if request.method == "POST":
#         data = parse_request_data(request)
#         if not data:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)

#         try:
#             accessory = OpticalAccessory.objects.create(
#                 name=data["type"],  # Optical Accessories have no specific types
#                 unit_price=data["unit_price"],
#                 stock_level=data["stock_level"],
#                 date_added=parse_datetime(data.get("date_added", None)) or None,
#             )
#             return JsonResponse({"message": "Accessory added successfully!", "id": accessory.id})
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"error": "Invalid request method"}, status=405)


# @csrf_exempt
# def delete_item(request, model, item_id):
#     model_map = {"frame": Frame, "lens": Lens, "accessory": OpticalAccessory}
#     if model not in model_map:
#         return JsonResponse({"error": "Invalid model"}, status=400)

#     try:
#         obj = model_map[model].objects.get(id=item_id)
#         obj.delete()
#         return JsonResponse({"message": f"{model.capitalize()} deleted successfully!"})
#     except model_map[model].DoesNotExist:
#         return JsonResponse({"error": f"{model.capitalize()} not found"}, status=404)


# @csrf_exempt
# def update_item(request, model, item_id):
#     model_map = {"frame": Frame, "lens": Lens, "accessory": OpticalAccessory}
#     if model not in model_map:
#         return JsonResponse({"error": "Invalid model"}, status=400)

#     if request.method == "PUT":
#         data = parse_request_data(request)
#         if not data:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)

#         try:
#             obj = model_map[model].objects.get(id=item_id)
#             obj.unit_price = data.get("unit_price", obj.unit_price)
#             obj.stock_level = data.get("stock_level", obj.stock_level)
#             if model != "accessory":
#                 obj.type = data.get("type", getattr(obj, "type", None))
#             obj.save()
#             return JsonResponse({"message": f"{model.capitalize()} updated successfully!"})
#         except model_map[model].DoesNotExist:
#             return JsonResponse({"error": f"{model.capitalize()} not found"}, status=404)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"error": "Invalid request method"}, status=405)


# @csrf_exempt
# def list_items(request, model):
#     model_map = {"frame": Frame, "lens": Lens, "accessory": OpticalAccessory}
#     if model not in model_map:
#         return JsonResponse({"error": "Invalid model"}, status=400)

#     try:
#         objects = model_map[model].objects.all()
#         data = [
#             {
#                 "id": obj.id,
#                 "type": getattr(obj, "frame_type", getattr(obj, "lens_type", obj.name)),
#                 "unit_price": str(obj.unit_price),
#                 "stock_level": obj.stock_level,
#                 "quantity_sold": obj.quantity_sold,
#                 "date_added": obj.date_added.strftime("%Y-%m-%d %H:%M:%S"),
#             }
#             for obj in objects
#         ]
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Frame, Lens, OpticalAccessory
# import json

# # Helper function to serialize inventory data
# def serialize_inventory(item):
#     return {
#         "id": item.id,
#         "type": getattr(item, "frame_type", getattr(item, "lens_type", item.name)),
#         "stock_level": item.stock_level,
#         "unit_price": float(item.unit_price),
#         "date_added": item.date_added.strftime("%Y-%m-%d %H:%M:%S"),
#     }

# # Common function to handle different models
# def get_model(item_type):
#     if item_type == "frame":
#         return Frame
#     elif item_type == "lens":
#         return Lens
#     elif item_type == "optical_accessory":
#         return OpticalAccessory
#     else:
#         return None

# @csrf_exempt
# def list_items(request, item_type):
#     model = get_model(item_type)
#     if not model:
#         return JsonResponse({"error": "Invalid item type"}, status=400)

#     items = model.objects.all()
#     data = [serialize_inventory(item) for item in items]
#     return JsonResponse(data, safe=False)

# @csrf_exempt
# def add_item(request, item_type):
#     if request.method == "POST":
#         try:
#             model = get_model(item_type)
#             if not model:
#                 return JsonResponse({"error": "Invalid item type"}, status=400)

#             data = json.loads(request.body)
#             if item_type == "optical_accessory":
#                 item = model.objects.create(
#                     name=data["name"],
#                     unit_price=data["unit_price"],
#                     stock_level=data["stock_level"],
#                 )
#             else:
#                 item = model.objects.create(
#                     frame_type=data.get("type") if item_type == "frame" else None,
#                     lens_type=data.get("type") if item_type == "lens" else None,
#                     unit_price=data["unit_price"],
#                     stock_level=data["stock_level"],
#                 )
#             return JsonResponse(serialize_inventory(item), status=201)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# @csrf_exempt
# def update_item(request, item_type, item_id):
#     if request.method == "PUT":
#         try:
#             model = get_model(item_type)
#             if not model:
#                 return JsonResponse({"error": "Invalid item type"}, status=400)

#             item = model.objects.get(id=item_id)
#             data = json.loads(request.body)

#             if item_type == "optical_accessory":
#                 item.name = data["name"]
#             else:
#                 if item_type == "frame":
#                     item.frame_type = data["type"]
#                 elif item_type == "lens":
#                     item.lens_type = data["type"]

#             item.unit_price = data["unit_price"]
#             item.stock_level = data["stock_level"]
#             item.save()

#             return JsonResponse(serialize_inventory(item), status=200)
#         except model.DoesNotExist:
#             return JsonResponse({"error": f"{item_type} not found"}, status=404)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# @csrf_exempt
# def delete_item(request, item_type, item_id):
#     if request.method == "DELETE":
#         try:
#             model = get_model(item_type)
#             if not model:
#                 return JsonResponse({"error": "Invalid item type"}, status=400)

#             item = model.objects.get(id=item_id)
#             item.delete()
#             return JsonResponse({"message": f"{item_type.capitalize()} deleted successfully"}, status=204)
#         except model.DoesNotExist:
#             return JsonResponse({"error": f"{item_type} not found"}, status=404)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)






















































































from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from io import BytesIO
import os

from .models import MedicalReport

def generate_pdf(medical_report):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 750, f"Medical Report for: {medical_report.patient.name}")
    c.drawString(100, 730, f"Date: {medical_report.date}")
    c.drawString(100, 710, f"Age: {medical_report.age}")
    c.drawString(100, 690, f"Sex: {medical_report.sexe}")
    c.drawString(100, 670, f"Profession: {medical_report.profession}")
    c.drawString(100, 650, f"Ametropie: {medical_report.ametropie}")
    c.drawString(100, 630, f"Types de Verre: {medical_report.types_de_verre}")
    c.drawString(100, 610, f"Teintes: {medical_report.teintes}")
    c.drawString(100, 590, f"Foyers: {medical_report.foyers}")
    c.drawString(100, 570, f"Port: {medical_report.port}")
    c.drawString(100, 550, f"Indice: {medical_report.indice}")
    c.save()
    buffer.seek(0)

    return buffer.getvalue()
    



from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import MedicalReport
from .views import generate_pdf

def save_pdf(request, report_id):
    report = get_object_or_404(MedicalReport, id=report_id)

    # Generate the PDF
    pdf_content = generate_pdf(report)

    # Save to File Field
    file_path = f'medical_reports/{report.patient.name}_report_{report.id}.pdf'
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    with open(full_path, 'wb') as f:
        f.write(pdf_content)

    report.pdf_file = file_path
    report.save()

    return HttpResponse("PDF Generated and Saved!")


def print_pdf(request, report_id):
    report = get_object_or_404(MedicalReport, id=report_id)
    pdf_content = generate_pdf(report)
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="medical_report_{report.id}.pdf"'
    return response

# # views.py
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import MedicalReport
# from .serializers import MedicalReportSerializer

# @api_view(['GET'])
# def get_medical_report(request, patient_id):
#     try:
#         report = MedicalReport.objects.get(patient__id=patient_id)
#         serializer = MedicalReportSerializer(report)
#         return Response(serializer.data, status=200)
#     except MedicalReport.DoesNotExist:
#         return Response({'error': 'Report not found'}, status=404)




from django.http import FileResponse

def download_pdf(request, report_id):
    report = get_object_or_404(MedicalReport, id=report_id)
    if report.pdf_file:
        return FileResponse(open(report.pdf_file.path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponse("No PDF found for this report.")






# # from django.shortcuts import get_object_or_404
# # from django.http import JsonResponse
# # from django.views.decorators.csrf import csrf_exempt
# # from .models import MedicalReport, Patient
# # import json

# # @csrf_exempt
# # def list_medical_reports(request, patient_id):
# #     """List all medical reports for a specific patient."""
# #     if request.method == 'GET':
# #         reports = MedicalReport.objects.filter(patient_id=patient_id).values()
# #         return JsonResponse({'medical_reports': list(reports)})
# #     return JsonResponse({'error': 'Invalid request method'}, status=405)

# # @csrf_exempt
# # def create_medical_report(request):
# #     """Create a new medical report."""
# #     if request.method == 'POST':
# #         data = json.loads(request.body)
# #         patient = get_object_or_404(Patient, id=data['patient_id'])
# #         try:
# #             report = MedicalReport.objects.create(
# #                 patient=patient,
# #                 age=data['age'],
# #                 sexe=data['sexe'],
# #                 profession=data['profession'],
# #                 sphere_od=data['sphere_od'],
# #                 cyl_od=data['cyl_od'],
# #                 axe_od=data['axe_od'],
# #                 addition_od=data['addition_od'],
# #                 sphere_og=data['sphere_og'],
# #                 cyl_og=data['cyl_og'],
# #                 axe_og=data['axe_og'],
# #                 addition_og=data['addition_og'],
# #                 ametropie=data['ametropie'],
# #                 types_de_verre=data['types_de_verre'],
# #                 teintes=data['teintes'],
# #                 foyers=data['foyers'],
# #                 port=data['port'],
# #                 indice=data['indice'],
# #             )
# #             return JsonResponse({'message': 'Medical report created successfully!', 'id': report.id})
# #         except Exception as e:
# #             return JsonResponse({'error': str(e)}, status=400)
# #     return JsonResponse({'error': 'Invalid request method'}, status=405)

# # @csrf_exempt
# # def get_medical_report(request, report_id):
# #     """Retrieve details of a specific medical report."""
# #     if request.method == 'GET':
# #         report = get_object_or_404(MedicalReport, id=report_id)
# #         return JsonResponse({'medical_report': {
# #             'id': report.id,
# #             'patient_name': report.patient.name,
# #             'date': report.date,
# #             'age': report.age,
# #             'sexe': report.sexe,
# #             'profession': report.profession,
# #             'sphere_od': report.sphere_od,
# #             'cyl_od': report.cyl_od,
# #             'axe_od': report.axe_od,
# #             'addition_od': report.addition_od,
# #             'sphere_og': report.sphere_og,
# #             'cyl_og': report.cyl_og,
# #             'axe_og': report.axe_og,
# #             'addition_og': report.addition_og,
# #             'ametropie': report.ametropie,
# #             'types_de_verre': report.types_de_verre,
# #             'teintes': report.teintes,
# #             'foyers': report.foyers,
# #             'port': report.port,
# #             'indice': report.indice,
# #         }})
# #     return JsonResponse({'error': 'Invalid request method'}, status=405)
