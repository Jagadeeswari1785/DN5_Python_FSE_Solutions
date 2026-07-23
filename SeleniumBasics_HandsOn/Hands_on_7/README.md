## Page Object Model (POM)

In a flat Selenium script, if the Submit button ID changes from `submit` to `btn-submit`, every test containing that locator must be updated.

In the Page Object Model, the locator is stored in one Page class. Updating it in one place automatically fixes every test that uses that page, making the framework easier to maintain and reuse.