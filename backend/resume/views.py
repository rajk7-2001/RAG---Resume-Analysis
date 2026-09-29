# from django.shortcuts import render
# from django.http import HttpResponse
# from .components.pdf_text_extractor import pdf_extractor 
# from .components.execution import execution
from rest_framework.views import APIView
# from rest_framework import status
from rest_framework.response import Response

# class ResumeAnalysis(APIView):
    
#     def post(self, request):
#         pdf_file = request.FILES.get('resume')
#         jd = request .data.get("job_description")
#         if not pdf_file:
#             return Response(
#                 {"error" : "uploading resume is mandatory"},
#                 status = status.HTTP_400_BAD_REQUEST
#             )
#         if not jd:
#             return Response(
#                 {"error": "job description mandatory"},
#                 status = status.HTTP_400_BAD_REQUEST
#             )
#         resume_text = pdf_extractor(pdf_file)
#         final_response = execution(resume_text,jd)
        
        
        
#         return Response({
#             "Response" : final_response
#         })

class ResumeAnalysis(APIView):
    def post(self, request):
        return Response({
            "message": "Django API is working"
        })