let container = document.getElementById('founders')
let founder = document.querySelector('.application-triple')
let amount = 1




function validate(){
	if (amount == 1){
		[...document.querySelectorAll('.remove-founder')].forEach(button => {
			button.style.opacity = '.5'
			button.setAttribute('disabled', '')
		})
	}
	else{
		[...document.querySelectorAll('.remove-founder')].forEach(button => {
			button.style.opacity = '1'
			button.removeAttribute('disabled')
		})
	}
}



function add_founder(button){
	container.appendChild(founder.cloneNode(true))
	amount ++;
	validate()
}

function remove_founder(button){
	button.parentNode.parentNode.remove()
	amount --;
	validate()
}