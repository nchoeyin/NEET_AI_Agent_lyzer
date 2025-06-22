from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import classonlymethod
from django.views.decorators.csrf import csrf_exempt
import httpx
import json

# Create your views here.

class LyzrAgentApiAsyncView(View):
    async def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, world!'}, status=200)
    
    @csrf_exempt
    async def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode())
            payload = {
                "user_id": data.get("user_id", "ngawangchoeying303@gmail.com"),
                "agent_id": data.get("agent_id", "6857d21e7cdac4902fe6a975"),
                "session_id": data.get("session_id", "6857d21e7cdac4902fe6a975-84mba8hghr3"),
                "message": data.get("message", "")
            }
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'https://agent-prod.studio.lyzr.ai/v3/inference/chat/',
                    headers={
                        'Content-Type': 'application/json',
                        'x-api-key': 'sk-default-pG6bwq2raM1xbNr1sJxomGdFxsEJOpNm',
                    },
                    json=payload
                )
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

