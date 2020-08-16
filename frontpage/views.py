from os import path
from django.http import HttpResponse
from django.shortcuts import render
import markdown

# Create your views here.

def frontpage(request):
	basepath = path.dirname(path.dirname(__file__))
	f = path.join(basepath, 'README.md')
	readme_md = open(f).read()
	readme_html = markdown.markdown(readme_md, extensions=['tables'])
	html = """
		<html>
		<head>
			<meta charset="utf-8">
 			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Primer/15.1.0/primer.css">
 			<style>
 			  th, td { padding: 0 1rem; border: 1px solid lightgray }
 			</style>
		</head>
		<body>
			<div style="padding-left: 3rem;">
				%(body)s
			</div>
		</body>
		</html>
	""" % { 'body' : readme_html }
	return HttpResponse(html)