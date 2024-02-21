// Wait for the DOM to fully load before executing JavaScript
document.addEventListener('DOMContentLoaded', function() {
  // Code to run after the DOM is loaded

  // Toggle mobile menu
  const toggleMobileMenu = () => {
      const navMenu = document.querySelector('.nav-list');
      navMenu.classList.toggle('active');
  };

  // Add event listener to mobile menu button
  const mobileMenuButton = document.querySelector('.mobile-menu-button');
  mobileMenuButton.addEventListener('click', toggleMobileMenu);

  // Smooth scrolling
  const scrollLinks = document.querySelectorAll('.nav-link');
  scrollLinks.forEach(link => {
      link.addEventListener('click', e => {
          e.preventDefault();
          const targetId = link.getAttribute('href').substring(1);
          const target = document.getElementById(targetId);
          const navHeight = document.querySelector('header').offsetHeight;
          const scrollTo = target.offsetTop - navHeight;
          window.scrollTo({
              top: scrollTo,
              behavior: 'smooth'
          });
      });
  });

  // Contact form submission
  const contactForm = document.querySelector('.contact-form');
  contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      // Perform form validation here
      const formData = new FormData(contactForm);
      // Perform AJAX request to submit form data
      fetch('submit-form.php', {
          method: 'POST',
          body: formData
      })
      .then(response => {
          if (response.ok) {
              alert('Form submitted successfully!');
              contactForm.reset();
          } else {
              throw new Error('Form submission failed!');
          }
      })
      .catch(error => {
          console.error('Error:', error);
          alert('Form submission failed. Please try again later.');
      });
  });
});

