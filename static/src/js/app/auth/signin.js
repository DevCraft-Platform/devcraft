/**
 * Signin.js - Route: /app/auth/signin
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
 *  - Redirect to /app/auth/signup
 *  - Redirect to /app/auth/forgot
 * -----------------------------------´
 * 
 * (C) 2024 DevCraft - All rights reserved
 */

// Importing modules


// Importing Id's
const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');

// Animation on entrance
/*
 * We use the library animista to animate the signin form on entrance.
*  The class 'swing-in-top-fwd' is added to the form on page load. 
*  This class is defined in the file static/src/scss/app/auth/signin.scss
*  and is responsible for the animation.
*
*  STATUS: WORKING ✅
 */
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#login_form').classList.add('swing-in-top-fwd');
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
    //  - The domain name must contain a top-level domain.
    //  - The top-level domain must contain at least 2 characters.
    
    const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (regex.test(email)) {
        return {"status": true}
    } else {
        return {"error": "Invalid Email Address", "status": false};
    }
}

// Password Encryption
const passwordEncryptor = (password) => {
    // This will encrypt the password using a hashing algorithm.
    // Then it will return it as a string, and it will be compared
    // with the hashed password in the database. If they match, the
    // user will be logged in.
    const hashedPassword = CryptoJS.SHA256(password).toString(CryptoJS.enc.Base64);
    return hashedPassword;
}

// Password validation
const passwordValidator = (password) => {
    // We will validate the password encrypting it and
    // checking if the password encrypted is the same as the
    // password in the database.
    const encryptedPassword = passwordEncryptor(password);
    // Do a API call to the server to the checker
    // If the password is correct, return true
    // Else, return false
    fetch('/api/auth/check-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            password: encryptedPassword
        })
    }).then(response => response.json()).then(data => {
        try {
            if (data === undefined)
            {
                return ({'error': 'Invalid Password', 'status': false})
            }
            if (data.isValid === false) {
                return ({'error': 'Invalid Password', 'status': false})
            }
            if (data.isValid === true) {
                return ({'status': true})
            }
        }
        catch (error) {
            return ({'error': error, 'status': false})
        }
    });
}

// Form Validator
const formValidator = (email, password) => {

}

// Form Submission
/**
 * This function is responsible for submitting the form data to the server.
 * It includes:
 *  - Form Submission Response
 *  - Form Submission Error
 *  - Form Submission Success
 *  - Form Submission Failure
 *  - Form Submission Loading
 *  - Form Submission Reset
 */

// Form Submission Response
const formSubmissionResponse = (response) => {

}

// Form Submission Error
const formSubmissionError = (error) => {

}

// Form Submission Success
const formSubmissionSuccess = (data) => {

}

// Form Submission Failure
const formSubmissionFailure = (data) => {

}

// Form Submission Loading
const formSubmissionLoading = () => {

}

// Form Submission Reset
const formSubmissionReset = () => {

}

// Redirect to /app/dashboard
/**
 * This function is responsible for redirecting the user to the dashboard.
 * It includes:
 *  - Redirect to /app/dashboard
 */

// Redirect to /app/dashboard
const redirectToDashboard = () => {

}

/**
 * This function is responsible for redirecting the user to the signup page.
 * It includes:
 *  - Redirect to /app/auth/signup
 */

// Redirect to /app/auth/signup
const redirectToSignup = () => {

}

// PACK
/**
 * This function takes all the other fucntions and packs them into one function.
 * It includes:
 * - Animation on entrance
 * - Form Validation
 * - Form Submission
 * - Redirect to /app/dashboard
 * - Redirect to /app/auth/signup
 * - Redirect to /app/auth/forgot
 */

// PACK
const signin = () => {
    // Check for form submission
    document.querySelector('#login_form').addEventListener('submit', (e) => {
        // Now let's prevent the form from submitting
        e.preventDefault();
        // Now let's get the form data
        const emailValue = emailInput.value;
        const passwordValue = passwordInput.value;
        // Now let's validate the form data
        if (emailValidator(email).status === true)
        {
            if (passwordValidator(passwordValue).status === true) {
                // Now let's submit the form data
                fetch('/api/auth/signin', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: emailValue,
                        password: passwordValue
                    })
                }).then(response => response.json()).then(data => {
                    try {
                        if (data === undefined)
                        {
                            console.error('Invalid Response');
                        }
                        if (data.status === 'success') {
                            console.log('Signin Successful');
                            // Take the sessionId and username and store it in the session storage
                            sessionStorage.setItem('session', JSON.stringify(data.session));
                            // Redirect to the dashboard
                            window.location.href = `/app/dashboard/${data.session.username}`;
                        }
                        if (data.status === 'failure') {
                            console.error('Signin Failed');
                        }
                    } catch (e) {
                        console.error(e);
                    }
                });
            }
        }
    });
}

signin()

// End of file