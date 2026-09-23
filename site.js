// Language content and links are rendered in HTML for visitors and crawlers.
const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear();
