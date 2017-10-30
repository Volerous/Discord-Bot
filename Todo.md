event based system in discord:
* create db for event
* index all people in the server to the db.
* create event, people, notification

* event <> person
* event <> notification
* event <> notfication <> person

Database side
===
use orm from sqlalchemy
use SQLite3

event Table
---
* event_id
* location
* time
* name

Person Table
---
* Name
* id

Notification
---
* date
* time

event <> person
---
* event.event_id
* perosn.person_id
* state

Python Side
===

functions
---
* create
* edit
* delete
* show
* cancel
* find
* going 
* can't go
* maybe
* look up facebook

### Create
**enter**: ```.event "name" "location" "time"```  
**do**:  
create event in db  
insert name, location, time  
lex and parse ```datetime terms```  
display the creation of the event  

### Edit
find 

### Delete


### Show


### Cancel


### Find


### Going 


### Can't go


### Maybe


### Look up facebook

