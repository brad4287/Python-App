# CICD-Python-App-Deploy

This repository is for building a Python Application in Jenkins

Python application which is a command line tool "add2vals" that outputs the addition of two values. 

values is a string, "add2vals" treats both values as a string and instead concatenates the values. The "add2" function in the "calc" library (which"add2vals" imports) is accompanied by a set of unit tests. These are tested with pytest to check that this function works as expected and the results are savedto a JUnit XML report.

The delivery of the "add2vals" tool through PyInstaller converts this tool into a standalone executable file for Linux, which you can download through Jenkins and execute at the command line on Linux machines without Python.