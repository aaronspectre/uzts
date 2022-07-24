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