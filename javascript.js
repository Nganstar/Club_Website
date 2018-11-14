// When user scrolls page, execute topNavBar()
window.onscroll = function() {topNavBar()};

// Get the navbar
var navBar = document.getElementById('navbar');

// Get the offset position of navBar
var sticky = navBar.offsetTop;

// Add sticky class to navbar when you reach its scroll position. 
// Remove "sticky" when you leave the scroll position/
function topNavBar()
{
	if (window.pageYOffset >= sticky) 
	{
		navBar.classList.add('sticky');
	}
	else
	{
		navBar.classList.remove('sticky');
	}

}

