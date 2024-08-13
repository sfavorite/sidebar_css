
myjavascript = '''
 
function openSide() { 
	document.getElementById('sideBar').style.width = '250px';
	document.getElementById('main').style.marginLeft = '250px'; 
	document.getElementById('openbtn').style.visibility = 'hidden';
}

function closeSide() { 
	document.getElementById('sideBar').style.width = '0px';
	document.getElementById('main').style.marginLeft = '0px'; 
	document.getElementById('openbtn').style.visibility = 'visible'; 
	document.getElementById('openbtn').style.background = 'white'; 
}
'''
