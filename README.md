# AudioFilesCRUDAPI

## Endpoints for audiofiles

---
```
CREATE: /create/<audioFileType> - creates a new instance of that audioFileType
GET/READ: /get/<audioFileType> - gets all instances of that audioFileType
GET/READ: /get/<audioFileType>/<int:pk> - gets single object of that audioFileType depending on the pk passed
UPDATE: /update/<audioFileType>/<int:pk> - updates given instance as primary key is passed, and of that audioFileType
DELETE: /delete/<audioFileType>/<int:pk> - deletes given instance as primary key is passed, and of that audioFileType
```
---
## NOTE:
* available "audioFileType" types: audiobook, podcast, song
* please ensure participants field data is inserted in this format, {'participants':"['test1','test2]"}
* django-mysql's ListCharField field is used, which requires list to be passed of type CharField with max length validation
* api working validation are done both via DRF's template view and POSTMAN
---