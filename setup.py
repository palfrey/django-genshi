from setuptools import setup, Extension

version = '1.0.0'

setup (
	name = 'django-genshi',
	version = version,
	description = "Django integration for Genshi",
	author = "John Millikin",
	author_email = "jmillikin@gmail.com",
	license = "MIT",
	url = "https://launchpad.net/django-genshi",
	download_url = "http://cheeseshop.python.org/pypi/django-genshi/%s" % version,
	platforms = ["Platform Independent"],
	classifiers = [
		"Development Status :: 4 - Beta",
		"Framework :: Django",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Text Processing :: Markup :: HTML",
		"Topic :: Text Processing :: Markup :: XML",
	],
	keywords = ["django", "genshi"],
)
