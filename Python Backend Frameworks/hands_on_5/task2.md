Step 1: Open courses/models.py
Add a to_dict() method to every model.

Example:

def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "code": self.code,
        "credits": self.credits
    }
Step 2: Open courses/routes.py
Replace the existing in-memory list logic with SQLAlchemy queries.

Step 3: Update the GET route
Replace the old code with:

Course.query.all()
Convert the results using to_dict() before returning JSON.

Step 4: Update the POST route
Instead of appending to a list:

Create a Course object.

Add it to the session.

Commit the transaction.

db.session.add(course)
db.session.commit()
Return the new course with 201 Created.

Step 5: Update GET by ID
Use:

Course.query.get_or_404(id)
If the course doesn't exist, Flask automatically returns 404.

Step 6: Update the PUT route
Fetch the course using get_or_404().

Update its fields.

Commit the changes.

Step 7: Update the DELETE route
Fetch the course using get_or_404().

Delete it:

db.session.delete(course)
db.session.commit()
Return a success response.

Step 8: Add a Students route
Create:

GET /api/courses/<id>/students/
Use a JOIN query to fetch all students enrolled in that course.
