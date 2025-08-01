# Crowley Art

A Django project for managing tattoo artist profiles and portfolios with a custom user model, profile details, and modern styling.

## Main Commits

- [Initial project setup](https://github.com/Petko-Simov/CrowleyArt/commit/8db46722e858c32577b7ac5b1e12077596da8a37)  
  Created the base Django app, project structure, and initial configuration.

- [Updated navbar, profile details layout, profile edit/delete views and enhanced CSS styling](https://github.com/Petko-Simov/CrowleyArt/commit/6ddcc639434b7fb54a921dbef7ea42ea97e27358)  
  Updated navigation bar, profile views (details, edit, delete), and core CSS styles.

- [Style profile-edit page layout: separated heading, aligned form and buttons](https://github.com/Petko-Simov/CrowleyArt/commit/2a672ccf00a816e0c27e0eb3f97dfb894d60e52c)  
  Improved the layout of the profile edit page: separated heading and aligned buttons.

- [Update profile edit form to sync nickname with user.username](https://github.com/Petko-Simov/CrowleyArt/commit/96afb1019f95367c46867f447a6af89d91b7a70a)  
  Editing the nickname now updates the User’s username field under the hood.

- [Fixed ProfileDetailsForm, templates and views](https://github.com/Petko-Simov/CrowleyArt/commit/5b42e8b04cd6d4014a8cae7a1cb27914ecd25828)  
  Fixed bugs in the profile details form and its rendering views, and cleaned up templates.

- [Configure admin roles, custom validators, and add Tattoo gallery model](https://github.com/Petko-Simov/CrowleyArt/commit/fcf4e7c3094e017d615cf778212cc1540dc3e26e)  
  - Defined superuser and staff permissions groups in the Django admin  
  - Added `AppUserUsernameValidator` to enforce username rules  
  - Added `BulgarianPhoneValidator` for phone number format  
  - Refactored `ProfileDetailsForm` for clearer settings and read‑only behavior  
  - Introduced the `Tattoo` model

- [Fix login-or-register flow and gallery access prompt](<PUT_COMMIT_URL_HERE>)  
  - Added intermediary login/register prompt for accessing the gallery when unauthenticated.  
  - Ensured the Django login view respects `next` and redirects appropriately (normal login → profile, gallery-triggered login → gallery).  
  - Restored proper input styling on login form (blue borders) without breaking existing layout.  
  - Cleaned up and stabilized the access logic around gallery visibility.
