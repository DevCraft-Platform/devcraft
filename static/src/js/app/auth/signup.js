/**
 * SignUp.js - Route: /app/auth/signup
 * Author: INovomiast2
 * Created: 2024-11-04
 * -----------------------------------
 * 
 * Contents:
 *  - Animation on entrance
 *  - Form Validation
 *  - Form Submission
 *  - Form Submission Response
 *  - Form Submission Error
 *  - Form Submission Success
 *  - Form Submission Failure
 *  - Form Submission Loading
 *  - Form Submission Reset
 *  - Redirect to /app/dashboard
 *  - Redirect to /app/auth/signin
 * -----------------------------------´
 * 
 * (C) 2024 DevCraft - All rights reserved
 */

// Importing modules


// Importing Id's
const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');
const repeatPasswordInput = document.querySelector('#confirm-password');
const signupForm = document.querySelector('#su-form');

// Animation on entrance
/*
 * We use the library animista to animate the signup form on entrance.
* The class 'swing-in-top-fwd' is added to the form on page load.
*   
* This class is defined in the file static/src/scss/app/auth/signup.scss
* and is responsible for the animation.
* 
* STATUS: WORKING ✅
*/
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#signup-form').classList.add('swing-in-top-fwd');
});

// Form Validation
/**
 * This is a set of functions that validates the form fields.
 * It includes:
 *  - Email validation
 *  - Password Encryption
 *  - Password validation
 *  - Form Validator
 */

// Email validation
const emailValidator = (email) => {
    // For this, I will use a regular expression to validate the email.
    // The regular expression is as follows:
    //  - The email must contain an '@' symbol.
    //  - The email must contain a domain name.
    //  - The domain name must contain a '.' symbol.
    //  - The domain name must contain a domain extension.
    //  - The domain extension must be at least 2 characters long.
    //  - The domain extension must be at most 4 characters long.
    //  - The domain extension must contain only letters.
    //  - The domain extension must be lowercase.
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-z]{2,4}$/;
    return emailRegex.test(email);
};

// Password Validation
const passwordValidator = (password) => {
    // The password must contain at least 8 characters.
    // The password must contain at least 1 uppercase letter.
    // The password must contain at least 1 lowercase letter.
    // The password must contain at least 1 number.
    // The password must contain at least 1 special character.
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$/;
    return passwordRegex.test(password);
};

// Repeat Password Validation
const repeatPasswordValidator = (password, repeatPassword) => {
    return password === repeatPassword;
};

const signup = async (email, password) => {
    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!emailValidator(email)) {
            Notification.caller('error', 'Invalid email address');
            return;
        }
    });
}

signup(emailInput.value, passwordInput.value);