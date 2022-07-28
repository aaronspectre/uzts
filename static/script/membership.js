let side_menu_additional = document.querySelectorAll('.side-menu-additional')
let side_menu_main = document.querySelector('.side-menu-main')
let side_menu_button = document.getElementById('side-menu-button')
let side_menu_cover = document.getElementById('navbar-cover')
let side_menu_state = false

function close_additional(){
	for (var i = side_menu_additional.length - 1; i >= 0; i--) {
		side_menu_additional[i].style.transform = 'translateX(-27vw)'
	}
}


document.querySelector('body').addEventListener('click', event => {
	if (event.target.id == 'navbar-cover'){
		close_additional()
		side_menu_main.style.transform = 'translateX(-27vw)'
		side_menu_button.style.background = 'transparent'
		side_menu_button.style.color = 'black'
		side_menu_cover.style.display = 'none'
		side_menu_cover.style.visibility = 'hidden'
		side_menu_state = false

		side_menu_button.textContent = 'MENU'

	}
})
side_menu_button.addEventListener('click', event => {
	if (side_menu_state){
		close_additional()
		side_menu_main.style.transform = 'translateX(-27vw)'
		side_menu_button.style.background = 'transparent'
		side_menu_button.style.color = 'white'
		side_menu_cover.style.display = 'none'
		side_menu_cover.style.visibility = 'hidden'
		side_menu_state = false

		side_menu_button.textContent = 'MENU'
	}
	else{
		side_menu_button.style.background = 'white'
		side_menu_button.style.color = 'black'
		side_menu_main.style.transform = 'translateX(5vw)'
		side_menu_cover.style.visibility = 'visible'
		side_menu_cover.style.display = 'block'
		side_menu_state = true

		event.target.textContent = 'CLOSE'
	}
})
let triggers = document.querySelectorAll('.additional-menu-trigger')
for (var i = triggers.length - 1; i >= 0; i--) {
	triggers[i].addEventListener('click', event => {
		close_additional()
		document.getElementById(event.target.getAttribute('data-target')).style.transform = 'translateX(31vw)'
	})
}

window.addEventListener('scroll', event => {
	if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
		side_menu_button.style.borderRightColor = '#2C3333'
		side_menu_button.style.color = '#2C3333'
	}
	else {
		side_menu_button.style.borderRightColor = 'white'
		side_menu_button.style.color = 'white'
	}
})