from setuptools import setup

setup(
   name='todolist',
   version='1.0',
   description='A recruitment task',
   install_requires=[
      "asgiref==3.5.2",
      "Django==4.1.3",
      "djangorestframework==3.14.0",
      "pytz==2022.6",
      "sqlparse==0.4.3",
      "tzdata==2022.6",
   ],
   python_requires=">=3.0",
)