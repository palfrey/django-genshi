from django.conf import settings
from django.http import HttpResponse

from django_genshi.context import Context
from django_genshi.loader import get_template, select_template

__all__ = ['render_to_stream', 'render_to_response']

def render_to_stream (template_name, dictionary = None,
                      context_instance = None):
	if isinstance (template_name, (list, tuple)):
		template = select_template (template_name)
	else:
		template = get_template (template_name)
		
	if context_instance:
		context_instance.update (dictionary)
	else:
		context_instance = Context (dictionary)
		
	return template.generate (context_instance)
	
def render_to_response (*args, **kwargs):
	charset = settings.DEFAULT_CHARSET
	content_type = settings.DEFAULT_CONTENT_TYPE
	
	stream = render_to_stream (*args, **kwargs)
	text = stream.render ('html', encoding = charset,
	                      strip_whitespace = False)
	full_content_type = '%s; charset=%s' % (content_type, charset)
	return HttpResponse (text, content_type = full_content_type)
	
