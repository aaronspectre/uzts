menu = document.getElementById('menu')
cover = document.getElementById('transparent-cover')
navbar = document.getElementById('navbar')
top_menu = document.getElementById('navbar-main')
function show_menu(button){
	button.nextSibling.nextSibling.style.display = 'initial'
	button.style.display = 'none'
	menu.classList.add('visible-menu')
	cover.style.visibility = 'visible'
	cover.style.opacity = '.3'
	navbar.style.background = 'white'
}

function hide_menu(button){
	button.previousSibling.previousSibling.style.display = 'initial'
	button.style.display = 'none'
	menu.classList.remove('visible-menu')
	cover.style.visibility = 'hidden'
	cover.style.opacity = '0'
	navbar.style.background = 'none'
}

cover.addEventListener('click', event => {
	menu.classList.remove('visible-menu')
	document.getElementById('menu-bars').style.display = 'initial'
	document.getElementById('menu-xmark').style.display = 'none'
	cover.style.visibility = 'hidden'
	cover.style.opacity = '0'
	navbar.style.background = 'none'
})



window.addEventListener('scroll', event => {
	if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
		top_menu.style.background = 'white'
		top_menu.style.borderBottomColor = 'lightgray'
	}
	else {
		top_menu.style.background = 'none'
		top_menu.style.borderBottomColor = 'transparent'
	}
})