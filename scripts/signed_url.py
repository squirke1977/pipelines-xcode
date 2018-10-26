#!/usr/bin/python

import jinja2
import os

build_dir = os.environ.get("AGENT_BUILDDIRECTORY")

print(build_dir)

working_directory = build_dir + "/installapplications/"
output_directory = build_dir + "/installapplications/payload/Library/LaunchDaemons/"

what = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(working_directory)
print(output_directory)
print(what)

templateLoader = jinja2.FileSystemLoader(searchpath=working_directory)
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("com.erikng.installapplications.template")
filename = output_directory + "com.erikng.installapplications.plist"

print(filename)

outputfile = open(filename, 'w')
complete = template.render({"bootstrap_url":os.environ.get("SIGNED_URL")})
outputfile.write(complete)
outputfile.close()
