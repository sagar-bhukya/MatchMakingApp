```
# MatchMakingApp

Overview
This project involved enhancing a FastAPI-based backend application for a Marriage Matchmaking App. The tasks included implementing endpoints for updating and deleting user profiles, finding potential matches, and validating email addresses.
Approach
Project Structure Analysis:
I followed the existing structure with files like main.py, models.py, database.py, and schemas.py.

Endpoint Implementation:
Update User Endpoint: Added PUT endpoint (/users/{user_id}) to update user details using UserUpdate schema.
Delete User Endpoint: Added DELETE endpoint (/users/{user_id}) to remove a user profile.
Find Matches Endpoint: Added GET endpoint (/users/{user_id}/matches) to find potential matches based on city and gender.

Data Validation:
Email Validation: Used EmailStr type from Pydantic in UserCreate and UserUpdate schemas to ensure valid email addresses.


Assumptions Made
User Matching Criteria: Based on the same city and opposite gender.
Email Uniqueness: Ensured email addresses are unique for each user.
Database Integrity: Assumed SQLite database is set up and operational.

Testing and Validation
Tested using manual HTTP requests via Postman.
Swagger api : http://127.0.0.1:8000/docs
```


