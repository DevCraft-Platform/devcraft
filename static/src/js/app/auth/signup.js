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
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const repeatPasswordInput = document.getElementById('confirm-password');
const signupForm = document.getElementById('su-form');

// Steps ID
const step1Icon = document.getElementById('step-1');
const step2Icon = document.getElementById('step-2');
const step3Icon = document.getElementById('step-3');
const step4Icon = document.getElementById('step-4');
const step5Icon = document.getElementById('step-5');

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
    // First lets see if the password is the same as the repeat password
    repeatPasswordInput.addEventListener('change', () => {
        if (passwordInput.value !== repeatPasswordInput.value) {
            repeatPasswordInput.setCustomValidity('Passwords do not match');
        } else {
            repeatPasswordInput.setCustomValidity('');
        }
    })

    // Now lets validate the email
    emailInput.addEventListener('change', () => {
        if (!emailValidator(emailInput.value)) {
            emailInput.setCustomValidity('Invalid email');
        } else {
            emailInput.setCustomValidity('');
        }
    });

    // Now lets validate the password
    passwordInput.addEventListener('change', () => {
        if (!passwordValidator(passwordInput.value)) {
            passwordInput.setCustomValidity('Invalid password');
        } else {
            passwordInput.setCustomValidity('');
        }
    });
    // Now let's show the password requirements
    passwordInput.addEventListener('input', () => {
        const password = passwordInput.value;
        const isValid = passwordValidator(password);  // Call your password validation function
      
        // Update step-1 icon based on password strength (assuming icon exists)
        const step1Icon = document.getElementById('step-1-icon'); // Assuming ID exists
        if (isValid) {
          step1Icon.classList.add('valid'); // Add 'valid' class for visual confirmation (e.g., green checkmark)
          step1Icon.classList.remove('invalid'); // Remove any 'invalid' class (e.g., red X)
        } else {
          step1Icon.classList.add('invalid'); // Add 'invalid' class for visual feedback (e.g., red X)
          step1Icon.classList.remove('valid'); // Remove any 'valid' class
        }
      
        // Optionally hide requirements once password is valid (consider user preference):
        if (isValid) {
          passwordRequirements.style.display = 'none'; // Hide requirements if password is strong
        }
      });
      
      // Example password validation function (replace with your actual logic)
      function passwordValidator(password) {
        // Implement your custom password strength checks here (e.g., length, uppercase, lowercase, numbers, symbols)
        // Return true if password meets requirements, false otherwise
        return password.length >= 8 && // Minimum length
               /[a-z]/.test(password) && // Lowercase letter
               /[A-Z]/.test(password) && // Uppercase letter
               /[0-9]/.test(password);   // Number
      }

    // If all this is done, we can submit the form
    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = emailInput.value;
        const password = passwordInput.value;

        // Now lets send the data to the server
        const response = await fetch('/api/v1/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        // Now lets check the response
        if (response.ok) {
            // If the response is ok, we can redirect to the dashboard
            window.location.href = '/app/dashboard';
        } else {
            // If the response is not ok, we can show an error message
            const data = await response.json();
            alert(data.message);
        }
    });
}

signup(emailInput.value, passwordInput.value);