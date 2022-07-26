function removeField(self){
	self.parentNode.remove()
	sequence --;
	editSequence()
}
function editSequence(){
	document.getElementById('sequence').value = sequence
}



let sequence = 0
let form = document.getElementById('post-form')



function createButton(){
	let button = document.createElement('button')
	let minus = document.createElement('i')
	minus.classList.add('fal')
	minus.classList.add('fa-minus')
	button.setAttribute('type', 'button')
	button.appendChild(minus)
	button.addEventListener('click', event => {removeField(button)})
	return button
}


function addHeading(){
	let node = document.createElement('div')
	let heading = document.createElement('input')
	node.classList.add('post-section-module')
	heading.setAttribute('placeholder', 'Title')
	heading.setAttribute('type', 'text')
	heading.setAttribute('name', `heading-${sequence}`)
	node.appendChild(heading)
	node.appendChild(createButton())
	sequence ++;
	form.appendChild(node)
	editSequence()
}

function addText(){
	let textarea = document.createElement('textarea')
	let node = document.createElement('div')
	textarea.setAttribute('placeholder', 'Text')
	textarea.setAttribute('rows', '10')
	node.classList.add('post-section-module')
	textarea.setAttribute('name', `text-${sequence}`)
	node.appendChild(textarea)
	node.appendChild(createButton())
	sequence ++;
	form.appendChild(node)
	editSequence()
}

function addImage(){
	let image = document.createElement('input')
	let node = document.createElement('div')
	image.setAttribute('type', 'file')
	image.setAttribute('accept', 'image/png, image/jpeg')
	node.classList.add('post-section-module')
	image.setAttribute('name', `image-${sequence}`)
	node.appendChild(image)
	node.appendChild(createButton())
	sequence ++;
	form.appendChild(node)
	editSequence()
}