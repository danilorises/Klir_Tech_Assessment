# KLIR TECHNICAL ASSESSMENT #

This repository contains the results for the Klir Tech Assessment, part of the Klir Interview process. All 4 tasks were completed. You can find more info regarding each one below.

## Task 1: Test Environment Setup ##

Got some issues while trying to install the app locally using npm (*axios.create is not a function. (In 'axios.create({baseURL: serverURL})', 'axios.create' is undefined).*)
Tried some fixes (thinking it might be part of the interview to get possible errors on the App fixed) but ended up deciding to proceed with Docker. Got no prior experience with it, but it was intuitive enough.

The evidence of the environment setup can be found on the `environment-setup.png` file, as requested.

## Task 2: Create a test plan and run it manually ##

The contents regarding this step are located inside the `test-plan` folder. It contains:
- **Test Plan - WCA.docx:** The Test Plan itself
- **Execution 18-05-2024.pdf:** The execution of the Test Plan
- **BUG-001.pdf** and **BUG-002.pdf:** The defects found during the execution

The only assumption made through the manual (and UI) tests was that:
Customers that had **Email** contact info but no **Name** were actually OK, since a single Contact Info is still not *No Contact Info*.

## Task 3: Create an automated API level test scenario ##

For the API Tests I've used Python + Pytest + Requests lib. As for scenarios, I went with:

- Name OK scenario (for control)
- Missing Contact Info (*as per requirements: the contactInfo object is not returned when the customer doesn't have contact information in our database.*)
- Size Calculation (*as per requirements: customer size is: Small, when # of employees is <= 2500; Medium when it is 2500 <= 5000; Big otherwise.*)

I thought on adding an Empty Name scenario on the API Tests, but there was no mention on the Requirements that the request for the API should also fail if the name was empty so I decided on leaving it out.

All files related to Task 3 can be found in the `api-tests` folder, as instructed. Please check `api-tests/README.md` for instructions on how to run the tests.

## Task 4: Create an automated UI level test scenario ##

For the UI Tests I've used Python + Pytest + Selenium Webdriver. For scenarios we have:

- Name OK scenario (again, for control)
- Empty Name scenario (*If the user clicks the button leaving the text field blank, an alert message is presented: Please provide your name.*)
- Size Calculation (*Size: if # of Employees is less than or equal to 2500, size is Small; if # of Employees is greater then 2500 and less then or equal to 5000, Medium; otherwise, its Big*)
- Missing Contact Info (*When a customer doesn't have contact info, the message No contact info available should be presented.*)

Similarly, all files related to Task 4 can be found in the `ui-tests` folder. Please check `api-tests/README.md` for instructions on how to run the tests.