Task: 1
import re
text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":'
orange_numbers = re.findall(r'(\d+)', text)
print(orange_numbers)
out: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '648', '649', '650', '651', '652', '653', '3']

Task: 2

**Project Title: AAP (Admin and User Portal)**

**Project Description:**

AAP (Admin and User Portal) is a web-based platform designed to streamline the management of apps and user interactions. The platform consists of two main components: an Admin Facing interface and a User Facing interface. Built on Django, a high-level Python web framework, and enhanced with modern frontend technologies, AAP offers a seamless experience for both administrators and users.

**Features:**

1. **Admin Facing Component:**
   - **App Management:** Admin users can effortlessly add new Android apps to the platform, along with assigning points for user downloads.
   - **Custom Admin Panel:** The default Django Admin is replaced with a custom-designed interface tailored to the specific needs of administrators.
   - **Secure Authentication:** Admins access the system through secure authentication mechanisms, ensuring data integrity and confidentiality.

2. **User Facing Component:**
   - **User Authentication:** Users can sign up and log in securely to access their personalized dashboard.
   - **Profile Management:** Users have the ability to view and update their profiles, ensuring accurate information representation.
   - **Points Tracking:** Users can monitor the points they have earned through various activities, including app downloads.
   - **Task Completion:** A comprehensive view of tasks completed by the user is provided, offering insights into their engagement with the platform.
   - **Screenshot Upload:** Users can upload screenshots as proof of completing specific tasks, enhancing accountability and trust within the community.

**Technologies Used:**
- Backend: Django, Django REST Framework
- Frontend: javascript, html, css (User Facing Component)
- Database: SQLite3
- Authentication: Django Authentication System
- Documentation: Swagger
- Deployment: render


