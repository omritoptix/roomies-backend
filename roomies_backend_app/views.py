from django.shortcuts import render_to_response
from django.template.context import RequestContext




def porthole(request):
    '''
used for cross domain requests
'''
    return render_to_response('nerdeez-ember/porthole.html', locals(), context_instance=RequestContext(request))
 
def proxy(request):
    '''
used for cross domain requests
'''
    return render_to_response('nerdeez-ember/proxy.html', locals(), context_instance=RequestContext(request))

