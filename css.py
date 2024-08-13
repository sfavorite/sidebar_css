mcss = '''


.sidebar {  
	height: 100%; /* 100% Full-height */  
	width: 0; /* 0 width  */
	position: fixed; /* Stay in place */  
	z-index: 1; /* Stay on top */  
	top: 0;  
	left: 0;  
	background-color: #111; /* Black*/  
  overflow-x: hidden; /* Disable horizontal scroll */  
	padding-top: 60px; /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidebar */
}

/* The sidebar links */
.sidebar a {  
	padding: 8px 8px 8px 32px;  
	text-decoration: none;  
	font-size: 25px;  
	color: #818181;  
	display: block;  
  transition: 0.3s;
}

/* When you mouse over the navigation links, change their color */
.sidebar a:hover { 
	color: #f1f1f1;
}

/* Position and style the close button (top right corner) */
.sidebar .closebtn {  
	position: absolute;  
	top: 0;  
	right: 25px;  
	font-size: 30px;  
	margin-left: 50px;
}

.sidebar:hover .closebtn {
  visibility: visible;
}

/* The button used to close the sidebar */
.closebtn {
  background-color; blue;
  visibility: hidden;
}

/* The button used to open the sidebar */
.openbtn {
	position: absolute;
	font-size: 30px;  
	cursor: pointer;  
	background-color: white;  
	color: gray;  
	padding: 10px 15px;  
	border: none;

}
            
.openbtn:hover {  
	background-color: #444;
}

/* Style page content - use this if you want to push the page content to the right when you open the side navigation */
            
#main {  
	transition: margin-left .5s; /* If you want a transition effect */  
	padding: 0px;
	height: 100vh;
}

#homepage {
	margin-left: 2.5rem;
	padding-top: 20px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}
}

/* Medium screens and up */
@media (min-width: 768px) {
	#homepage {
		margin-left: 5rem;
	}
}

/* Extra large screens and up */
@media (min-width: 1200px) {
	#homepage {
		margin-left: 10rem;
	 }
}
'''