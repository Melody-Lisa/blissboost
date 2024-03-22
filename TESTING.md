# BlissBoost Testing

<img src="static/documents/blissboost_responsive.png" alt="An image representing how the site looks across different devices of varying size.">

[View the live project here.](https://blissboost-079490cc3274.herokuapp.com)

Manual testing was conducted continuously throughout the development process to ensure the functionality of various features across the site.

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validation)
  * [Python Validator](#python-validation)
  * [Lighthouse](#lighthouse)
  * [WAVE Testing](#wave-testing)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

  --------

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site along with validation of CSS. I have checked the HTML via url input of the deployed site, so as not to flag errors within the jinja templating, and the CSS has been tested by direct input.

<details><summary>Index HTML</summary>
<img src="static/documents/w3validated_index.png" alt="No Errors found.">
</details>

<details><summary>Register HTML</summary>
<img src="static/documents/w3validated_register.png" alt="No Errors found.">
</details>

<details><summary>Log In HTML</summary>
<img src="static/documents/w3validated_login.png" alt="No Errors found.">
</details>

<details><summary>Profile HTML</summary>
<img src="static/documents/w3validated_profile.png" alt="No Errors found.">
</details>

<details><summary>Edit Profile HTML</summary>
<img src="static/documents/w3validated_editprofile.png" alt="No Errors found.">
</details>

<details><summary>Community Posts HTML</summary>
<img src="static/documents/w3validated_posts.png" alt="One warning.">
</details>

In the community posts page the validator flagged up a possible misuse of aria label in the following code snippet. After reviewing the code and conducting extra tests using samsung talkback and windows narrator I have decided to keep this code as it is.

            <div class="card-reveal">

                <span class="card-title activator grey-text text-darken-4"

                 aria-label="Close Post Details">

                        Embrace serenity 🌿

                    <i class="hoverable right fa-solid fa-ellipsis-vertical">

                    </i>

                </span>

<details><summary>Add Post HTML</summary>
<img src="static/documents/w3validated_addpost.png" alt="No errors.">
</details>

<details><summary>Edit Post HTML</summary>
<img src="static/documents/w3validated_editpost.png" alt="No errors.">
</details>

<details><summary>Manage Themes HTML</summary>
<img src="static/documents/w3validated_getthemes.png" alt="No errors.">
</details>

<details><summary>Add Theme HTML</summary>
<img src="static/documents/w3validated_addtheme.png" alt="No errors.">
</details>

<details><summary>Edit Theme HTML</summary>
<img src="static/documents/w3validated_edittheme.png" alt="No errors.">
</details>

<details><summary>CSS</summary>
<img src="static/documents/w3validated_css.png" alt="No errors.">
</details>

### Javascript Validation

[JS Hint](https://jshint.com) has been used to test the vanilla javascript on the site. This flagged no major errors, but there were some warnings for undefined and unused variables. Both undefined variable errors are from code that has been copied from Materialize and all variables have been used within HTML files.

<details><summary>Vanilla Javascript</summary>
<img src="static/documents/blissboost_jshint.png" alt="Javascript Validation with js hint">
</details>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com) has been used to validate all python code on the site and ensure it is pep8 compliant. This has flagged no errors with the current code.

<details><summary>Python</summary>
<img src="static/documents/blissboost_pythonvalidation.png" alt="Javascript Validation with js hint">
</details>