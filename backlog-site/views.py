# ScrumDo - Agile/Scrum story management web application 
# Copyright (C) 2011 Marc Hughes, Ajay Reddy
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy (See file COPYING) of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from django.shortcuts import render_to_response, get_object_or_404
from projects.models import SiteStats
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime, date
import time
import json


def stats_data(request):
  stats = SiteStats.objects.all();
  user_data = []
  user_stats = { "label":"Users", "data":user_data}
  project_data = []
  project_stats = { "label":"Projects", "data":project_data}
  story_data = []
  story_stats = { "label":"Stories", "data":story_data, "yaxis": 2}
  for stat in stats:
    stat_time = int((time.mktime(stat.date.timetuple()) - time.timezone)*1000)
    user_data.append( [stat_time, stat.user_count] );
    project_data.append( [stat_time, stat.project_count] );
    story_data.append( [stat_time, stat.story_count] );        

  json_serializer = serializers.get_serializer("json")()
  result = json.dumps([user_stats,project_stats,story_stats])
  return HttpResponse(result) #, mimetype='application/json'