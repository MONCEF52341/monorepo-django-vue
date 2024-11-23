from django.shortcuts import render
import logging
from rest_framework.views import APIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        return Response({"status": "success"})
