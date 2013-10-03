# Create your views here.

from django.shortcuts import render,redirect
from flight_planner.logic import geolocation

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
#from django.shortcuts import render_to_response

import json,re

SLIDER_VALUES = [100,600]
volume = geolocation.Volume()

@csrf_exempt
def home(request):
	"view for index of flight_planner"

	data = {"test":"test"}

	return render(request, 'flight_planner_index.html', data)

@csrf_exempt
def planeSetup(request):
	"view to deal with setting of plane configuration"

	planeForm = [
		{"id":"plane-speed","label":"Plane Speed","placeholder":"Speed (m/s)"},
		{"id":"plane-turn","label":"Max Turn Angle","placeholder":"Angle (deg)"},
		{"id":"plane-time","label":"Max Flight Time","placeholder":"Time (minutes)"}
		]

	print(planeForm)

	data = {
		"planeForm" : planeForm
		}

	return render(request, 'plane_setup.html', data)

@csrf_exempt
def geographicalSetup(request):

	altitudeData = volume.getAltitude()
	shapeData = volume.getShape()
	volumeData = volume.getVolume()

	data = {
		"altitudeData" : altitudeData,
		"shapeData" : shapeData,
		"volumeData" : volumeData
		}

	return render(request, 'geographical_setup.html', data)

@csrf_exempt
def routePreview(request):
	"view to deal with setting of plane configuration"

	data = {
		"test" : "test"
		}

	return render(request, 'route_preview.html', data)

@csrf_exempt
def postShape(request):

	shapeData = request.POST["postField"]
	shapeData = json.loads(shapeData)

	if (shapeData == volume.getShape()):
		return None

	volume.setShape(shapeData)

	altitudeData = volume.getAltitude()
	shapeData = volume.getShape()
	volumeData = volume.getVolume()

	data = {
		"altitudeData" : altitudeData,
		"shapeData" : shapeData,
		"volumeData" : volumeData
		}

	json_data = json.dumps(data)
	# json data is just a JSON string now. 
	return HttpResponse(json_data, mimetype="application/json")

@csrf_exempt
def postAltitude(request):

	altitudeData = request.POST["postField"][1:-1]
	altitudeData = json.loads(altitudeData)

	volume.setAltitude(altitudeData)

	altitudeData = volume.getAltitude()
	shapeData = volume.getShape()
	volumeData = volume.getVolume()

	data = {
		"altitudeData" : altitudeData,
		"shapeData" : shapeData,
		"volumeData" : volumeData
		}

	json_data = json.dumps(data)

	return HttpResponse(json_data, mimetype="application/json")