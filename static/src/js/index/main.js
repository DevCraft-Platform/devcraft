// This is the main.js for the index page (Home Page) of the website.
// This file is included in the index.html file.

// Getting Started Button
const getStartedButton = document.getElementById('get-started-btn');

getStartedButton.addEventListener('click', () => {
  window.location.href = '/app/auth/signup';
});