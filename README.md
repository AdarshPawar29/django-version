# django-version
Django setup which can handle the versioning of data and its models. 

- Try School Application
I have added version end point to see `classroom` model versions. 

`classroom_versions/<your-classroom-id>` will show all versions 
- To revert through versions use

`classroom_versions_revert/<your-classroom-id>/<version-index>`

## How to create versions? 

Example:
Any changes you make to models connected to the classroom model will result in the creation of a new version with the updated information. 
