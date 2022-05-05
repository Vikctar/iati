# IATI Full Stack Developer - Interview Programming Test

## Part 1

Implement the following HTTP routes:

`POST /iatidoc`

Receives an IATI Activities XML document (from the `test_files` directory). This should validate that the root element of the document is
<iati-activities> , and store the document.

It should then return a unique identifier for the document.

## Part 2

Write a single page Web application which uses the API you've implemented in part 1 and
provides the following functionality:

- A user can browse their local filesystem and upload an IATI document (from the `test_files` directory). The UI should
  use the `POST /iatidoc` route from Part 1 to validate and store the document.
- If the document is invalid, the validation error is displayed to the user.
- If the document is valid, the browser application should display a success message and the unique identifier given to the file.

## Guiding Principles

- Your solution should include a README file with clear instructions about how to run
  your software.
- The solution must be able to run on Linux.
- Please track your project changes with git, preferably with a clear commit history instead of a single commit.
- Please return your solution via email to code@iatistandard.org attached as a compressed
  directory or add your code to a public GitHub (or other providers) repository.
- Use whichever languages and libraries you prefer, but try to keep the implementation
  as simple, as readable and as lightweight as possible.
- Your solution need only work with the provided test files - there is no requirement for
  it to work for any other IATI document.
- In the README file add your email address or a link to your GitHub profile page.
